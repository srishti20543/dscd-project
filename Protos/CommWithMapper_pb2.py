# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommWithMapper.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x43ommWithMapper.proto\"\xcd\x01\n\x0eMappingRequest\x12\x13\n\x0b\x64irectories\x18\x01 \x03(\t\x12\x34\n\rtypeOfRequest\x18\x02 \x01(\x0e\x32\x1d.MappingRequest.TypeOfRequest\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x10\n\x08reducers\x18\x04 \x01(\x05\x12\x0b\n\x03ids\x18\x05 \x03(\t\"B\n\rTypeOfRequest\x12\r\n\tWordCount\x10\x00\x12\x11\n\rInvertedIndex\x10\x01\x12\x0f\n\x0bNaturalJoin\x10\x02\"\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\t2A\n\x0e\x43ommWithMapper\x12/\n\x0f\x63onnectToMapper\x12\x0f.MappingRequest\x1a\t.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CommWithMapper_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPPINGREQUEST._serialized_start=25
  _MAPPINGREQUEST._serialized_end=230
  _MAPPINGREQUEST_TYPEOFREQUEST._serialized_start=164
  _MAPPINGREQUEST_TYPEOFREQUEST._serialized_end=230
  _RESPONSE._serialized_start=232
  _RESPONSE._serialized_end=258
  _COMMWITHMAPPER._serialized_start=260
  _COMMWITHMAPPER._serialized_end=325
# @@protoc_insertion_point(module_scope)
