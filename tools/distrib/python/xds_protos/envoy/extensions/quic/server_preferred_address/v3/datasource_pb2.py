# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/quic/server_preferred_address/v3/datasource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBenvoy/extensions/quic/server_preferred_address/v3/datasource.proto\x12\x31\x65nvoy.extensions.quic.server_preferred_address.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xf9\x03\n&DataSourceServerPreferredAddressConfig\x12\x82\x01\n\x0bipv4_config\x18\x01 \x01(\x0b\x32m.envoy.extensions.quic.server_preferred_address.v3.DataSourceServerPreferredAddressConfig.AddressFamilyConfig\x12\x82\x01\n\x0bipv6_config\x18\x02 \x01(\x0b\x32m.envoy.extensions.quic.server_preferred_address.v3.DataSourceServerPreferredAddressConfig.AddressFamilyConfig\x1a\xba\x01\n\x13\x41\x64\x64ressFamilyConfig\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32 .envoy.config.core.v3.DataSourceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12.\n\x04port\x18\x02 \x01(\x0b\x32 .envoy.config.core.v3.DataSource\x12\x36\n\x0c\x64nat_address\x18\x03 \x01(\x0b\x32 .envoy.config.core.v3.DataSource:\x08\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x42\xd1\x01\n?io.envoyproxy.envoy.extensions.quic.server_preferred_address.v3B\x0f\x44\x61tasourceProtoP\x01Zsgithub.com/envoyproxy/go-control-plane/envoy/extensions/quic/server_preferred_address/v3;server_preferred_addressv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.quic.server_preferred_address.v3.datasource_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n?io.envoyproxy.envoy.extensions.quic.server_preferred_address.v3B\017DatasourceProtoP\001Zsgithub.com/envoyproxy/go-control-plane/envoy/extensions/quic/server_preferred_address/v3;server_preferred_addressv3\272\200\310\321\006\002\020\002'
  _DATASOURCESERVERPREFERREDADDRESSCONFIG_ADDRESSFAMILYCONFIG.fields_by_name['address']._options = None
  _DATASOURCESERVERPREFERREDADDRESSCONFIG_ADDRESSFAMILYCONFIG.fields_by_name['address']._serialized_options = b'\372B\005\212\001\002\020\001'
  _DATASOURCESERVERPREFERREDADDRESSCONFIG._options = None
  _DATASOURCESERVERPREFERREDADDRESSCONFIG._serialized_options = b'\322\306\244\341\006\002\010\001'
  _globals['_DATASOURCESERVERPREFERREDADDRESSCONFIG']._serialized_start=244
  _globals['_DATASOURCESERVERPREFERREDADDRESSCONFIG']._serialized_end=749
  _globals['_DATASOURCESERVERPREFERREDADDRESSCONFIG_ADDRESSFAMILYCONFIG']._serialized_start=553
  _globals['_DATASOURCESERVERPREFERREDADDRESSCONFIG_ADDRESSFAMILYCONFIG']._serialized_end=739
# @@protoc_insertion_point(module_scope)