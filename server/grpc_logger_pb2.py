# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_logger.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11grpc_logger.proto\"S\n\nLogMessage\x12\x1a\n\x06\x61genda\x18\x01 \x01(\x0e\x32\n.LogAgenda\x12\x18\n\x05level\x18\x02 \x01(\x0e\x32\t.LogLevel\x12\x0f\n\x07message\x18\x03 \x01(\t\"+\n\x0fWriteLogRequest\x12\x18\n\x03log\x18\x01 \x01(\x0b\x32\x0b.LogMessage\"\"\n\x10WriteLogResponse\x12\x0e\n\x06status\x18\x01 \x01(\t**\n\tLogAgenda\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x0cHEALTH_CHECK\x10\x01*_\n\x08LogLevel\x12\x15\n\x11LOG_LEVEL_WARNING\x10\x00\x12\x12\n\x0eLOG_LEVEL_INFO\x10\x01\x12\x13\n\x0fLOG_LEVEL_ERROR\x10\x02\x12\x13\n\x0fLOG_LEVEL_FATAL\x10\x03\x32?\n\nLogService\x12\x31\n\x08WriteLog\x12\x10.WriteLogRequest\x1a\x11.WriteLogResponse\"\x00\x62\x06proto3')

_LOGAGENDA = DESCRIPTOR.enum_types_by_name['LogAgenda']
LogAgenda = enum_type_wrapper.EnumTypeWrapper(_LOGAGENDA)
_LOGLEVEL = DESCRIPTOR.enum_types_by_name['LogLevel']
LogLevel = enum_type_wrapper.EnumTypeWrapper(_LOGLEVEL)
DEFAULT = 0
HEALTH_CHECK = 1
LOG_LEVEL_WARNING = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_ERROR = 2
LOG_LEVEL_FATAL = 3


_LOGMESSAGE = DESCRIPTOR.message_types_by_name['LogMessage']
_WRITELOGREQUEST = DESCRIPTOR.message_types_by_name['WriteLogRequest']
_WRITELOGRESPONSE = DESCRIPTOR.message_types_by_name['WriteLogResponse']
LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGE,
  '__module__' : 'grpc_logger_pb2'
  # @@protoc_insertion_point(class_scope:LogMessage)
  })
_sym_db.RegisterMessage(LogMessage)

WriteLogRequest = _reflection.GeneratedProtocolMessageType('WriteLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITELOGREQUEST,
  '__module__' : 'grpc_logger_pb2'
  # @@protoc_insertion_point(class_scope:WriteLogRequest)
  })
_sym_db.RegisterMessage(WriteLogRequest)

WriteLogResponse = _reflection.GeneratedProtocolMessageType('WriteLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITELOGRESPONSE,
  '__module__' : 'grpc_logger_pb2'
  # @@protoc_insertion_point(class_scope:WriteLogResponse)
  })
_sym_db.RegisterMessage(WriteLogResponse)

_LOGSERVICE = DESCRIPTOR.services_by_name['LogService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGAGENDA._serialized_start=187
  _LOGAGENDA._serialized_end=229
  _LOGLEVEL._serialized_start=231
  _LOGLEVEL._serialized_end=326
  _LOGMESSAGE._serialized_start=21
  _LOGMESSAGE._serialized_end=104
  _WRITELOGREQUEST._serialized_start=106
  _WRITELOGREQUEST._serialized_end=149
  _WRITELOGRESPONSE._serialized_start=151
  _WRITELOGRESPONSE._serialized_end=185
  _LOGSERVICE._serialized_start=328
  _LOGSERVICE._serialized_end=391
# @@protoc_insertion_point(module_scope)
