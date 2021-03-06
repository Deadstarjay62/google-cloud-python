# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog_v1beta1/proto/timestamps.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/datacatalog_v1beta1/proto/timestamps.proto",
    package="google.cloud.datacatalog.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\034com.google.cloud.datacatalogP\001ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\370\001\001"
    ),
    serialized_pb=_b(
        '\n7google/cloud/datacatalog_v1beta1/proto/timestamps.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xa5\x01\n\x10SystemTimestamps\x12/\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x65xpire_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampBp\n\x1c\x63om.google.cloud.datacatalogP\x01ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\xf8\x01\x01\x62\x06proto3'
    ),
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR],
)


_SYSTEMTIMESTAMPS = _descriptor.Descriptor(
    name="SystemTimestamps",
    full_name="google.cloud.datacatalog.v1beta1.SystemTimestamps",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.datacatalog.v1beta1.SystemTimestamps.create_time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.cloud.datacatalog.v1beta1.SystemTimestamps.update_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="expire_time",
            full_name="google.cloud.datacatalog.v1beta1.SystemTimestamps.expire_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=127,
    serialized_end=292,
)

_SYSTEMTIMESTAMPS.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SYSTEMTIMESTAMPS.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SYSTEMTIMESTAMPS.fields_by_name[
    "expire_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name["SystemTimestamps"] = _SYSTEMTIMESTAMPS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemTimestamps = _reflection.GeneratedProtocolMessageType(
    "SystemTimestamps",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SYSTEMTIMESTAMPS,
        __module__="google.cloud.datacatalog_v1beta1.proto.timestamps_pb2",
        __doc__="""Timestamps about this resource according to a particular system.
  
  
  Attributes:
      create_time:
          Output only. The creation time of the resource within the
          given system.
      update_time:
          Output only. The last-modified time of the resource within the
          given system.
      expire_time:
          Output only. The expiration time of the resource within the
          given system.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.SystemTimestamps)
    ),
)
_sym_db.RegisterMessage(SystemTimestamps)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
