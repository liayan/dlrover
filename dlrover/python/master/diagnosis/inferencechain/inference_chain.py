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

from typing import List

from dlrover.python.common.log import default_logger as logger
from dlrover.python.master.diagnosis.inferencechain.inference import (
    Inference,
    InferenceOperator,
    combine_inferences,
)
from dlrover.python.master.diagnosis.operator.operator import (
    register_operators,
)
from master.diagnosis.diagnosis import DiagnosisDataManager


class InferenceChain:
    """
    InferenceChain is used to diagnose training failures
    """

    def __init__(self, inferences: List[Inference]):
        self.inferences = inferences
        self.operators = register_operators()

    def infer(self) -> List[Inference]:
        inferences = self.inferences
        while True:
            has_new_inference = False
            new_infs: List[Inference] = []
            for inference in inferences:
                try:
                    operator = self.get_operator(inference)
                    infs = operator.infer(inferences)
                    if len(infs) > 0:
                        has_new_inference = True
                        new_infs = combine_inferences(new_infs, infs)
                    else:
                        new_infs.append(inference)
                except Exception as e:
                    logger.exception(e)
                    new_infs.append(inference)

            if has_new_inference:
                inferences = new_infs
            else:
                break
        return inferences

    def get_operator(self, inference: Inference) -> InferenceOperator:
        for operator in self.operators:
            if operator.is_compatible(inference):
                return operator
        raise TypeError(f"no compatible operator for {inference}")
