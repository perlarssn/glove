# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request.proto',
  package='state',
  serialized_pb='\n\rrequest.proto\x12\x05state\"V\n\x07Request\x12(\n\x04type\x18\x01 \x02(\x0e\x32\x1a.state.Request.RequestType\"!\n\x0bRequestType\x12\x08\n\x04INFO\x10\x00\x12\x08\n\x04JOIN\x10\x01')



_REQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='state.Request.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=77,
  serialized_end=110,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='state.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='state.Request.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=24,
  serialized_end=110,
)

_REQUEST.fields_by_name['type'].enum_type = _REQUEST_REQUESTTYPE
_REQUEST_REQUESTTYPE.containing_type = _REQUEST;
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:state.Request)


# @@protoc_insertion_point(module_scope)
