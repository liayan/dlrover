# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acceleration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='acceleration.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x61\x63\x63\x65leration.proto\x12\x05proto\x1a\x1bgoogle/protobuf/empty.proto\"4\n\x1eGetAutoAccelerationTaskRequest\x12\x12\n\nprocess_id\x18\x01 \x01(\x05\"C\n\x12OptimizationMethod\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\x0c\x12\x0f\n\x07tunable\x18\x03 \x01(\x08\"2\n\x08Strategy\x12&\n\x03opt\x18\x01 \x03(\x0b\x32\x19.proto.OptimizationMethod\"\x1f\n\x0e\x41nalysisMethod\x12\r\n\x05names\x18\x01 \x03(\t\"\xe7\x01\n\x14\x41utoAccelerationTask\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x11\n\ttask_type\x18\x02 \x01(\t\x12\x14\n\x0cprocess_mode\x18\x03 \x01(\t\x12#\n\x08strategy\x18\x04 \x01(\x0b\x32\x0f.proto.StrategyH\x00\x12\x30\n\x0f\x61nalysis_method\x18\x05 \x01(\x0b\x32\x15.proto.AnalysisMethodH\x00\x12\x1d\n\x13parallel_group_info\x18\x06 \x01(\x0cH\x00\x12\x12\n\ntime_limit\x18\x07 \x01(\x05\x42\x0b\n\ttask_info\"\xc2\x01\n\x1a\x41utoAccelerationTaskResult\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x12\n\nprocess_id\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x08\x12#\n\x08strategy\x18\x04 \x01(\x0b\x32\x0f.proto.StrategyH\x00\x12\x14\n\nmodel_meta\x18\x05 \x01(\x0cH\x00\x12\x17\n\rdryrun_result\x18\x06 \x01(\x0cH\x00\x12\x11\n\ttask_type\x18\x07 \x01(\tB\x08\n\x06result2\xba\x01\n\x17\x41utoAccelerationService\x12N\n\x08get_task\x12%.proto.GetAutoAccelerationTaskRequest\x1a\x1b.proto.AutoAccelerationTask\x12O\n\x12report_task_result\x12!.proto.AutoAccelerationTaskResult\x1a\x16.google.protobuf.Emptyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_GETAUTOACCELERATIONTASKREQUEST = _descriptor.Descriptor(
  name='GetAutoAccelerationTaskRequest',
  full_name='proto.GetAutoAccelerationTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_id', full_name='proto.GetAutoAccelerationTaskRequest.process_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=110,
)


_OPTIMIZATIONMETHOD = _descriptor.Descriptor(
  name='OptimizationMethod',
  full_name='proto.OptimizationMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.OptimizationMethod.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='proto.OptimizationMethod.config', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tunable', full_name='proto.OptimizationMethod.tunable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=179,
)


_STRATEGY = _descriptor.Descriptor(
  name='Strategy',
  full_name='proto.Strategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opt', full_name='proto.Strategy.opt', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=231,
)


_ANALYSISMETHOD = _descriptor.Descriptor(
  name='AnalysisMethod',
  full_name='proto.AnalysisMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='proto.AnalysisMethod.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=264,
)


_AUTOACCELERATIONTASK = _descriptor.Descriptor(
  name='AutoAccelerationTask',
  full_name='proto.AutoAccelerationTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='proto.AutoAccelerationTask.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='proto.AutoAccelerationTask.task_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_mode', full_name='proto.AutoAccelerationTask.process_mode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='proto.AutoAccelerationTask.strategy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='analysis_method', full_name='proto.AutoAccelerationTask.analysis_method', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parallel_group_info', full_name='proto.AutoAccelerationTask.parallel_group_info', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_limit', full_name='proto.AutoAccelerationTask.time_limit', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='task_info', full_name='proto.AutoAccelerationTask.task_info',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=267,
  serialized_end=498,
)


_AUTOACCELERATIONTASKRESULT = _descriptor.Descriptor(
  name='AutoAccelerationTaskResult',
  full_name='proto.AutoAccelerationTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='proto.AutoAccelerationTaskResult.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_id', full_name='proto.AutoAccelerationTaskResult.process_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.AutoAccelerationTaskResult.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='proto.AutoAccelerationTaskResult.strategy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_meta', full_name='proto.AutoAccelerationTaskResult.model_meta', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dryrun_result', full_name='proto.AutoAccelerationTaskResult.dryrun_result', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='proto.AutoAccelerationTaskResult.task_type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='result', full_name='proto.AutoAccelerationTaskResult.result',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=501,
  serialized_end=695,
)

_STRATEGY.fields_by_name['opt'].message_type = _OPTIMIZATIONMETHOD
_AUTOACCELERATIONTASK.fields_by_name['strategy'].message_type = _STRATEGY
_AUTOACCELERATIONTASK.fields_by_name['analysis_method'].message_type = _ANALYSISMETHOD
_AUTOACCELERATIONTASK.oneofs_by_name['task_info'].fields.append(
  _AUTOACCELERATIONTASK.fields_by_name['strategy'])
_AUTOACCELERATIONTASK.fields_by_name['strategy'].containing_oneof = _AUTOACCELERATIONTASK.oneofs_by_name['task_info']
_AUTOACCELERATIONTASK.oneofs_by_name['task_info'].fields.append(
  _AUTOACCELERATIONTASK.fields_by_name['analysis_method'])
_AUTOACCELERATIONTASK.fields_by_name['analysis_method'].containing_oneof = _AUTOACCELERATIONTASK.oneofs_by_name['task_info']
_AUTOACCELERATIONTASK.oneofs_by_name['task_info'].fields.append(
  _AUTOACCELERATIONTASK.fields_by_name['parallel_group_info'])
_AUTOACCELERATIONTASK.fields_by_name['parallel_group_info'].containing_oneof = _AUTOACCELERATIONTASK.oneofs_by_name['task_info']
_AUTOACCELERATIONTASKRESULT.fields_by_name['strategy'].message_type = _STRATEGY
_AUTOACCELERATIONTASKRESULT.oneofs_by_name['result'].fields.append(
  _AUTOACCELERATIONTASKRESULT.fields_by_name['strategy'])
_AUTOACCELERATIONTASKRESULT.fields_by_name['strategy'].containing_oneof = _AUTOACCELERATIONTASKRESULT.oneofs_by_name['result']
_AUTOACCELERATIONTASKRESULT.oneofs_by_name['result'].fields.append(
  _AUTOACCELERATIONTASKRESULT.fields_by_name['model_meta'])
_AUTOACCELERATIONTASKRESULT.fields_by_name['model_meta'].containing_oneof = _AUTOACCELERATIONTASKRESULT.oneofs_by_name['result']
_AUTOACCELERATIONTASKRESULT.oneofs_by_name['result'].fields.append(
  _AUTOACCELERATIONTASKRESULT.fields_by_name['dryrun_result'])
_AUTOACCELERATIONTASKRESULT.fields_by_name['dryrun_result'].containing_oneof = _AUTOACCELERATIONTASKRESULT.oneofs_by_name['result']
DESCRIPTOR.message_types_by_name['GetAutoAccelerationTaskRequest'] = _GETAUTOACCELERATIONTASKREQUEST
DESCRIPTOR.message_types_by_name['OptimizationMethod'] = _OPTIMIZATIONMETHOD
DESCRIPTOR.message_types_by_name['Strategy'] = _STRATEGY
DESCRIPTOR.message_types_by_name['AnalysisMethod'] = _ANALYSISMETHOD
DESCRIPTOR.message_types_by_name['AutoAccelerationTask'] = _AUTOACCELERATIONTASK
DESCRIPTOR.message_types_by_name['AutoAccelerationTaskResult'] = _AUTOACCELERATIONTASKRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAutoAccelerationTaskRequest = _reflection.GeneratedProtocolMessageType('GetAutoAccelerationTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTOACCELERATIONTASKREQUEST,
  '__module__' : 'acceleration_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetAutoAccelerationTaskRequest)
  })
_sym_db.RegisterMessage(GetAutoAccelerationTaskRequest)

OptimizationMethod = _reflection.GeneratedProtocolMessageType('OptimizationMethod', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZATIONMETHOD,
  '__module__' : 'acceleration_pb2'
  # @@protoc_insertion_point(class_scope:proto.OptimizationMethod)
  })
_sym_db.RegisterMessage(OptimizationMethod)

Strategy = _reflection.GeneratedProtocolMessageType('Strategy', (_message.Message,), {
  'DESCRIPTOR' : _STRATEGY,
  '__module__' : 'acceleration_pb2'
  # @@protoc_insertion_point(class_scope:proto.Strategy)
  })
_sym_db.RegisterMessage(Strategy)

AnalysisMethod = _reflection.GeneratedProtocolMessageType('AnalysisMethod', (_message.Message,), {
  'DESCRIPTOR' : _ANALYSISMETHOD,
  '__module__' : 'acceleration_pb2'
  # @@protoc_insertion_point(class_scope:proto.AnalysisMethod)
  })
_sym_db.RegisterMessage(AnalysisMethod)

AutoAccelerationTask = _reflection.GeneratedProtocolMessageType('AutoAccelerationTask', (_message.Message,), {
  'DESCRIPTOR' : _AUTOACCELERATIONTASK,
  '__module__' : 'acceleration_pb2'
  # @@protoc_insertion_point(class_scope:proto.AutoAccelerationTask)
  })
_sym_db.RegisterMessage(AutoAccelerationTask)

AutoAccelerationTaskResult = _reflection.GeneratedProtocolMessageType('AutoAccelerationTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _AUTOACCELERATIONTASKRESULT,
  '__module__' : 'acceleration_pb2'
  # @@protoc_insertion_point(class_scope:proto.AutoAccelerationTaskResult)
  })
_sym_db.RegisterMessage(AutoAccelerationTaskResult)



_AUTOACCELERATIONSERVICE = _descriptor.ServiceDescriptor(
  name='AutoAccelerationService',
  full_name='proto.AutoAccelerationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=698,
  serialized_end=884,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_task',
    full_name='proto.AutoAccelerationService.get_task',
    index=0,
    containing_service=None,
    input_type=_GETAUTOACCELERATIONTASKREQUEST,
    output_type=_AUTOACCELERATIONTASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='report_task_result',
    full_name='proto.AutoAccelerationService.report_task_result',
    index=1,
    containing_service=None,
    input_type=_AUTOACCELERATIONTASKRESULT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTOACCELERATIONSERVICE)

DESCRIPTOR.services_by_name['AutoAccelerationService'] = _AUTOACCELERATIONSERVICE

# @@protoc_insertion_point(module_scope)
