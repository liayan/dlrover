# Copyright 2024 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import threading
import time
from typing import List

from dlrover.python.common.log import default_logger as logger
from dlrover.python.diagnosis.common.constants import DiagnosisConstant
from dlrover.python.diagnosis.common.diagnosis_action import DiagnosisAction
from dlrover.python.diagnosis.common.diagnosis_data import DiagnosisData
from dlrover.python.diagnosis.common.inference_chain import (
    InferenceAttribute,
    InferenceDescription,
    InferenceName,
    InferenceOperator,
)
from dlrover.python.diagnosis.inferencechain.coordinate_solutions import (
    coordinate_solutions,
)
from dlrover.python.diagnosis.inferencechain.inference_chain import (
    Inference,
    InferenceChain,
    combine_inferences,
)
from dlrover.python.diagnosis.inferencechain.inferenceoperator.operator import (  # noqa: E501
    get_master_observe_operators,
)
from dlrover.python.master.diagnosis.diagnosis_data_manager import (
    DiagnosisDataManager,
)
from dlrover.python.master.node.job_context import get_job_context


class DiagnosisManager:
    """
    DiagnosisManager is to manage all diagnosis issues in a training job
    """

    def __init__(self):
        self._is_observing_started = False
        self._data_manager: DiagnosisDataManager = DiagnosisDataManager(600)
        self._diagnostician: Diagnostician = Diagnostician(self._data_manager)
        self._job_context = get_job_context()

    def collect_diagnosis_data(self, data: DiagnosisData):
        self._data_manager.store_data(data)

    def pre_check(self):
        logger.info("Start Diagnosis Manager to pre-check training...")

        # TODO
        pre_checks = []
        self._diagnostician.register_pre_check(pre_checks)
        pass

    def start_observing(self):
        logger.info("Start Diagnosis Manager to observing training...")
        self._is_observing_started = True

        problems: List[Inference] = [
            Inference(
                InferenceName.TRAINING,
                InferenceAttribute.ISORNOT,
                InferenceDescription.HANG,
            )
        ]
        self._diagnostician.register_training_problems(problems)

        operators = get_master_observe_operators(self._data_manager)
        self._diagnostician.register_observing_operators(operators)

        try:
            thread = threading.Thread(
                target=self._diagnose,
                name="diagnose_failures",
                daemon=True,
            )
            thread.start()
            if thread.is_alive():
                logger.info("Diagnosis Manager is started")
        except Exception as e:
            logger.error(
                f"Failed to start the diagnosis manager thread. Error: {e}"
            )

    def stop_observing(self):
        logger.info("Stop Diagnosis Manager to observing training.")
        self._is_observing_started = False

    def _diagnose(self):
        logger.info("Start to diagnose failures for observing.")
        while True:
            if not self._is_observing_started:
                logger.info("Stop to diagnose failures for observing.")
                break

            observed_problems = self._diagnostician.observe_training()
            action = self._diagnostician.diagnose_problems(observed_problems)
            self._job_context.enqueue_action(action)

            time.sleep(
                DiagnosisConstant.MASTER_DIAGNOSIS_OBSERVING_INTERVAL_SECS
            )


class Diagnostician:
    """
    Diagnostician is to observe training problems and explore solutions to
    those problems during training.
    """

    def __init__(self, data_manager):
        self._data_manager = data_manager
        self._pre_checks: List[Inference] = []
        self._training_problems: List[Inference] = []
        self._observing_operators: List[InferenceOperator] = []
        self._diagnosis_operators: List[InferenceOperator] = []

    def register_pre_check(self, pre_checks: List[Inference]):
        self._pre_checks = pre_checks

    def register_training_problems(self, problems: List[Inference]):
        self._training_problems = problems

    def register_observing_operators(self, operators: List[InferenceOperator]):
        self._observing_operators = operators

    def observe_training(self) -> List[Inference]:
        """
        To check if any problem in _training_problems happen

        Return:
            observed problems
        """
        if len(self._training_problems) == 0:
            logger.warning("No training problem is registered.")
            return []
        observed_problems: List[Inference] = []
        for problem in self._training_problems:
            ic = InferenceChain([problem], self._observing_operators)
            ob_problems = ic.infer()
            observed_problems = combine_inferences(
                observed_problems, ob_problems
            )
        return observed_problems

    def diagnose_problems(self, problems: List[Inference]) -> DiagnosisAction:
        """
        Generate the diagnosis action for observed problem

        Args:
            problems: observed problems
        Return:
            diagnosis action
        """
        solutions: List[Inference] = []
        for problem in problems:
            logger.info(f"observed problems: {problem}")
            ic = InferenceChain([problem], self._diagnosis_operators)
            sols = ic.infer()
            if len(sols) > 0:
                solutions = combine_inferences(solutions, sols)

        return coordinate_solutions(solutions)