# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='workflow.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eworkflow.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eRunningRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\" \n\rRunningResult\x12\x0f\n\x07message\x18\x01 \x01(\t2b\n\x08Workflow\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x12,\n\x07Running\x12\x0f.RunningRequest\x1a\x0e.RunningResult\"\x00\x62\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=46,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=77,
)


_RUNNINGREQUEST = _descriptor.Descriptor(
  name='RunningRequest',
  full_name='RunningRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='RunningRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=112,
)


_RUNNINGRESULT = _descriptor.Descriptor(
  name='RunningResult',
  full_name='RunningResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='RunningResult.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['RunningRequest'] = _RUNNINGREQUEST
DESCRIPTOR.message_types_by_name['RunningResult'] = _RUNNINGRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)

RunningRequest = _reflection.GeneratedProtocolMessageType('RunningRequest', (_message.Message,), dict(
  DESCRIPTOR = _RUNNINGREQUEST,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:RunningRequest)
  ))
_sym_db.RegisterMessage(RunningRequest)

RunningResult = _reflection.GeneratedProtocolMessageType('RunningResult', (_message.Message,), dict(
  DESCRIPTOR = _RUNNINGRESULT,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:RunningResult)
  ))
_sym_db.RegisterMessage(RunningResult)



_WORKFLOW = _descriptor.ServiceDescriptor(
  name='Workflow',
  full_name='Workflow',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=148,
  serialized_end=246,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='Workflow.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Running',
    full_name='Workflow.Running',
    index=1,
    containing_service=None,
    input_type=_RUNNINGREQUEST,
    output_type=_RUNNINGRESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKFLOW)

DESCRIPTOR.services_by_name['Workflow'] = _WORKFLOW

# @@protoc_insertion_point(module_scope)
