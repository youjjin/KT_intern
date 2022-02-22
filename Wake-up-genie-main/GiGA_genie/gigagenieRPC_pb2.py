# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gigagenieRPC.proto

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
  name='gigagenieRPC.proto',
  package='kt.gigagenie.ai.speech',
  syntax='proto3',
  serialized_pb=_b('\n\x12gigagenieRPC.proto\x12\x16kt.gigagenie.ai.speech\"q\n\x08reqVoice\x12\x39\n\nreqOptions\x18\x01 \x01(\x0b\x32#.kt.gigagenie.ai.speech.reqVoiceOptH\x00\x12\x16\n\x0c\x61udioContent\x18\x02 \x01(\x0cH\x00\x42\x12\n\x10streamingRequest\")\n\x0breqVoiceOpt\x12\x0c\n\x04mode\x18\x01 \x01(\x05\x12\x0c\n\x04lang\x18\x02 \x01(\x05\"3\n\x07resText\x12\x10\n\x08resultCd\x18\x01 \x01(\x05\x12\x16\n\x0erecognizedText\x18\x02 \x01(\t\"3\n\x07reqText\x12\x0c\n\x04lang\x18\x01 \x01(\x05\x12\x0c\n\x04mode\x18\x02 \x01(\x05\x12\x0c\n\x04text\x18\x03 \x01(\t\"\'\n\x06resUrl\x12\x10\n\x08resultCd\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t\"u\n\x08resVoice\x12<\n\nresOptions\x18\x01 \x01(\x0b\x32&.kt.gigagenie.ai.speech.resVoiceResultH\x00\x12\x16\n\x0c\x61udioContent\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streamingResponse\"2\n\x0eresVoiceResult\x12\x10\n\x08resultCd\x18\x01 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\"H\n\x0creqQueryText\x12\x11\n\tqueryText\x18\x01 \x01(\t\x12\x13\n\x0buserSession\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x03 \x01(\t\"\x92\x01\n\x0cresQueryText\x12\x10\n\x08resultCd\x18\x01 \x01(\x05\x12\r\n\x05uword\x18\x02 \x01(\t\x12\x0e\n\x06sysAct\x18\x03 \x01(\t\x12\x0c\n\x04nAct\x18\x04 \x01(\t\x12\x10\n\x08sPattern\x18\x05 \x01(\t\x12\x31\n\x06\x61\x63tion\x18\x06 \x03(\x0b\x32!.kt.gigagenie.ai.speech.dssAction\"\x81\x01\n\tdssAction\x12\x0c\n\x04mesg\x18\x01 \x01(\t\x12\r\n\x05\x61\x46\x65\x65l\x18\x02 \x01(\t\x12\x0f\n\x07submesg\x18\x03 \x01(\t\x12\x10\n\x08\x61\x63tGroup\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x63tType\x18\x05 \x01(\t\x12\x10\n\x08srchWord\x18\x06 \x01(\t\x12\x11\n\tserviceId\x18\x07 \x01(\t\"{\n\rreqQueryVoice\x12>\n\nreqOptions\x18\x01 \x01(\x0b\x32(.kt.gigagenie.ai.speech.reqQueryVoiceOptH\x00\x12\x16\n\x0c\x61udioContent\x18\x02 \x01(\x0cH\x00\x42\x12\n\x10streamingRequest\"G\n\x10reqQueryVoiceOpt\x12\x0c\n\x04lang\x18\x01 \x01(\x05\x12\x13\n\x0buserSession\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x03 \x01(\t\"_\n\x0fresQueryByVoice\x12\x10\n\x08resultCd\x18\x01 \x01(\x05\x12\x0e\n\x06intent\x18\x02 \x01(\t\x12\x12\n\nparameters\x18\x03 \x01(\t\x12\x16\n\x0erecognizedText\x18\x04 \x01(\t2\xd8\x03\n\tGigagenie\x12X\n\rgetVoice2Text\x12 .kt.gigagenie.ai.speech.reqVoice\x1a\x1f.kt.gigagenie.ai.speech.resText\"\x00(\x01\x30\x01\x12U\n\x10getText2VoiceUrl\x12\x1f.kt.gigagenie.ai.speech.reqText\x1a\x1e.kt.gigagenie.ai.speech.resUrl\"\x00\x12\\\n\x13getText2VoiceStream\x12\x1f.kt.gigagenie.ai.speech.reqText\x1a .kt.gigagenie.ai.speech.resVoice\"\x00\x30\x01\x12[\n\x0bqueryByText\x12$.kt.gigagenie.ai.speech.reqQueryText\x1a$.kt.gigagenie.ai.speech.resQueryText\"\x00\x12_\n\x0cqueryByVoice\x12%.kt.gigagenie.ai.speech.reqQueryVoice\x1a$.kt.gigagenie.ai.speech.resQueryText\"\x00(\x01\x62\x06proto3')
)




_REQVOICE = _descriptor.Descriptor(
  name='reqVoice',
  full_name='kt.gigagenie.ai.speech.reqVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqOptions', full_name='kt.gigagenie.ai.speech.reqVoice.reqOptions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audioContent', full_name='kt.gigagenie.ai.speech.reqVoice.audioContent', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='streamingRequest', full_name='kt.gigagenie.ai.speech.reqVoice.streamingRequest',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=46,
  serialized_end=159,
)


_REQVOICEOPT = _descriptor.Descriptor(
  name='reqVoiceOpt',
  full_name='kt.gigagenie.ai.speech.reqVoiceOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='kt.gigagenie.ai.speech.reqVoiceOpt.mode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='kt.gigagenie.ai.speech.reqVoiceOpt.lang', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=161,
  serialized_end=202,
)


_RESTEXT = _descriptor.Descriptor(
  name='resText',
  full_name='kt.gigagenie.ai.speech.resText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultCd', full_name='kt.gigagenie.ai.speech.resText.resultCd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recognizedText', full_name='kt.gigagenie.ai.speech.resText.recognizedText', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=204,
  serialized_end=255,
)


_REQTEXT = _descriptor.Descriptor(
  name='reqText',
  full_name='kt.gigagenie.ai.speech.reqText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lang', full_name='kt.gigagenie.ai.speech.reqText.lang', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='kt.gigagenie.ai.speech.reqText.mode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='kt.gigagenie.ai.speech.reqText.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=257,
  serialized_end=308,
)


_RESURL = _descriptor.Descriptor(
  name='resUrl',
  full_name='kt.gigagenie.ai.speech.resUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultCd', full_name='kt.gigagenie.ai.speech.resUrl.resultCd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='kt.gigagenie.ai.speech.resUrl.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=310,
  serialized_end=349,
)


_RESVOICE = _descriptor.Descriptor(
  name='resVoice',
  full_name='kt.gigagenie.ai.speech.resVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resOptions', full_name='kt.gigagenie.ai.speech.resVoice.resOptions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audioContent', full_name='kt.gigagenie.ai.speech.resVoice.audioContent', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='streamingResponse', full_name='kt.gigagenie.ai.speech.resVoice.streamingResponse',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=351,
  serialized_end=468,
)


_RESVOICERESULT = _descriptor.Descriptor(
  name='resVoiceResult',
  full_name='kt.gigagenie.ai.speech.resVoiceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultCd', full_name='kt.gigagenie.ai.speech.resVoiceResult.resultCd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='kt.gigagenie.ai.speech.resVoiceResult.format', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=470,
  serialized_end=520,
)


_REQQUERYTEXT = _descriptor.Descriptor(
  name='reqQueryText',
  full_name='kt.gigagenie.ai.speech.reqQueryText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queryText', full_name='kt.gigagenie.ai.speech.reqQueryText.queryText', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userSession', full_name='kt.gigagenie.ai.speech.reqQueryText.userSession', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='kt.gigagenie.ai.speech.reqQueryText.deviceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=522,
  serialized_end=594,
)


_RESQUERYTEXT = _descriptor.Descriptor(
  name='resQueryText',
  full_name='kt.gigagenie.ai.speech.resQueryText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultCd', full_name='kt.gigagenie.ai.speech.resQueryText.resultCd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uword', full_name='kt.gigagenie.ai.speech.resQueryText.uword', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sysAct', full_name='kt.gigagenie.ai.speech.resQueryText.sysAct', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nAct', full_name='kt.gigagenie.ai.speech.resQueryText.nAct', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sPattern', full_name='kt.gigagenie.ai.speech.resQueryText.sPattern', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='kt.gigagenie.ai.speech.resQueryText.action', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=597,
  serialized_end=743,
)


_DSSACTION = _descriptor.Descriptor(
  name='dssAction',
  full_name='kt.gigagenie.ai.speech.dssAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mesg', full_name='kt.gigagenie.ai.speech.dssAction.mesg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aFeel', full_name='kt.gigagenie.ai.speech.dssAction.aFeel', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submesg', full_name='kt.gigagenie.ai.speech.dssAction.submesg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actGroup', full_name='kt.gigagenie.ai.speech.dssAction.actGroup', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actType', full_name='kt.gigagenie.ai.speech.dssAction.actType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='srchWord', full_name='kt.gigagenie.ai.speech.dssAction.srchWord', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceId', full_name='kt.gigagenie.ai.speech.dssAction.serviceId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=746,
  serialized_end=875,
)


_REQQUERYVOICE = _descriptor.Descriptor(
  name='reqQueryVoice',
  full_name='kt.gigagenie.ai.speech.reqQueryVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqOptions', full_name='kt.gigagenie.ai.speech.reqQueryVoice.reqOptions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audioContent', full_name='kt.gigagenie.ai.speech.reqQueryVoice.audioContent', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='streamingRequest', full_name='kt.gigagenie.ai.speech.reqQueryVoice.streamingRequest',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=877,
  serialized_end=1000,
)


_REQQUERYVOICEOPT = _descriptor.Descriptor(
  name='reqQueryVoiceOpt',
  full_name='kt.gigagenie.ai.speech.reqQueryVoiceOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lang', full_name='kt.gigagenie.ai.speech.reqQueryVoiceOpt.lang', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userSession', full_name='kt.gigagenie.ai.speech.reqQueryVoiceOpt.userSession', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='kt.gigagenie.ai.speech.reqQueryVoiceOpt.deviceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1002,
  serialized_end=1073,
)


_RESQUERYBYVOICE = _descriptor.Descriptor(
  name='resQueryByVoice',
  full_name='kt.gigagenie.ai.speech.resQueryByVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultCd', full_name='kt.gigagenie.ai.speech.resQueryByVoice.resultCd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intent', full_name='kt.gigagenie.ai.speech.resQueryByVoice.intent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='kt.gigagenie.ai.speech.resQueryByVoice.parameters', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recognizedText', full_name='kt.gigagenie.ai.speech.resQueryByVoice.recognizedText', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1075,
  serialized_end=1170,
)

_REQVOICE.fields_by_name['reqOptions'].message_type = _REQVOICEOPT
_REQVOICE.oneofs_by_name['streamingRequest'].fields.append(
  _REQVOICE.fields_by_name['reqOptions'])
_REQVOICE.fields_by_name['reqOptions'].containing_oneof = _REQVOICE.oneofs_by_name['streamingRequest']
_REQVOICE.oneofs_by_name['streamingRequest'].fields.append(
  _REQVOICE.fields_by_name['audioContent'])
_REQVOICE.fields_by_name['audioContent'].containing_oneof = _REQVOICE.oneofs_by_name['streamingRequest']
_RESVOICE.fields_by_name['resOptions'].message_type = _RESVOICERESULT
_RESVOICE.oneofs_by_name['streamingResponse'].fields.append(
  _RESVOICE.fields_by_name['resOptions'])
_RESVOICE.fields_by_name['resOptions'].containing_oneof = _RESVOICE.oneofs_by_name['streamingResponse']
_RESVOICE.oneofs_by_name['streamingResponse'].fields.append(
  _RESVOICE.fields_by_name['audioContent'])
_RESVOICE.fields_by_name['audioContent'].containing_oneof = _RESVOICE.oneofs_by_name['streamingResponse']
_RESQUERYTEXT.fields_by_name['action'].message_type = _DSSACTION
_REQQUERYVOICE.fields_by_name['reqOptions'].message_type = _REQQUERYVOICEOPT
_REQQUERYVOICE.oneofs_by_name['streamingRequest'].fields.append(
  _REQQUERYVOICE.fields_by_name['reqOptions'])
_REQQUERYVOICE.fields_by_name['reqOptions'].containing_oneof = _REQQUERYVOICE.oneofs_by_name['streamingRequest']
_REQQUERYVOICE.oneofs_by_name['streamingRequest'].fields.append(
  _REQQUERYVOICE.fields_by_name['audioContent'])
_REQQUERYVOICE.fields_by_name['audioContent'].containing_oneof = _REQQUERYVOICE.oneofs_by_name['streamingRequest']
DESCRIPTOR.message_types_by_name['reqVoice'] = _REQVOICE
DESCRIPTOR.message_types_by_name['reqVoiceOpt'] = _REQVOICEOPT
DESCRIPTOR.message_types_by_name['resText'] = _RESTEXT
DESCRIPTOR.message_types_by_name['reqText'] = _REQTEXT
DESCRIPTOR.message_types_by_name['resUrl'] = _RESURL
DESCRIPTOR.message_types_by_name['resVoice'] = _RESVOICE
DESCRIPTOR.message_types_by_name['resVoiceResult'] = _RESVOICERESULT
DESCRIPTOR.message_types_by_name['reqQueryText'] = _REQQUERYTEXT
DESCRIPTOR.message_types_by_name['resQueryText'] = _RESQUERYTEXT
DESCRIPTOR.message_types_by_name['dssAction'] = _DSSACTION
DESCRIPTOR.message_types_by_name['reqQueryVoice'] = _REQQUERYVOICE
DESCRIPTOR.message_types_by_name['reqQueryVoiceOpt'] = _REQQUERYVOICEOPT
DESCRIPTOR.message_types_by_name['resQueryByVoice'] = _RESQUERYBYVOICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

reqVoice = _reflection.GeneratedProtocolMessageType('reqVoice', (_message.Message,), dict(
  DESCRIPTOR = _REQVOICE,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.reqVoice)
  ))
_sym_db.RegisterMessage(reqVoice)

reqVoiceOpt = _reflection.GeneratedProtocolMessageType('reqVoiceOpt', (_message.Message,), dict(
  DESCRIPTOR = _REQVOICEOPT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.reqVoiceOpt)
  ))
_sym_db.RegisterMessage(reqVoiceOpt)

resText = _reflection.GeneratedProtocolMessageType('resText', (_message.Message,), dict(
  DESCRIPTOR = _RESTEXT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.resText)
  ))
_sym_db.RegisterMessage(resText)

reqText = _reflection.GeneratedProtocolMessageType('reqText', (_message.Message,), dict(
  DESCRIPTOR = _REQTEXT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.reqText)
  ))
_sym_db.RegisterMessage(reqText)

resUrl = _reflection.GeneratedProtocolMessageType('resUrl', (_message.Message,), dict(
  DESCRIPTOR = _RESURL,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.resUrl)
  ))
_sym_db.RegisterMessage(resUrl)

resVoice = _reflection.GeneratedProtocolMessageType('resVoice', (_message.Message,), dict(
  DESCRIPTOR = _RESVOICE,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.resVoice)
  ))
_sym_db.RegisterMessage(resVoice)

resVoiceResult = _reflection.GeneratedProtocolMessageType('resVoiceResult', (_message.Message,), dict(
  DESCRIPTOR = _RESVOICERESULT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.resVoiceResult)
  ))
_sym_db.RegisterMessage(resVoiceResult)

reqQueryText = _reflection.GeneratedProtocolMessageType('reqQueryText', (_message.Message,), dict(
  DESCRIPTOR = _REQQUERYTEXT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.reqQueryText)
  ))
_sym_db.RegisterMessage(reqQueryText)

resQueryText = _reflection.GeneratedProtocolMessageType('resQueryText', (_message.Message,), dict(
  DESCRIPTOR = _RESQUERYTEXT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.resQueryText)
  ))
_sym_db.RegisterMessage(resQueryText)

dssAction = _reflection.GeneratedProtocolMessageType('dssAction', (_message.Message,), dict(
  DESCRIPTOR = _DSSACTION,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.dssAction)
  ))
_sym_db.RegisterMessage(dssAction)

reqQueryVoice = _reflection.GeneratedProtocolMessageType('reqQueryVoice', (_message.Message,), dict(
  DESCRIPTOR = _REQQUERYVOICE,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.reqQueryVoice)
  ))
_sym_db.RegisterMessage(reqQueryVoice)

reqQueryVoiceOpt = _reflection.GeneratedProtocolMessageType('reqQueryVoiceOpt', (_message.Message,), dict(
  DESCRIPTOR = _REQQUERYVOICEOPT,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.reqQueryVoiceOpt)
  ))
_sym_db.RegisterMessage(reqQueryVoiceOpt)

resQueryByVoice = _reflection.GeneratedProtocolMessageType('resQueryByVoice', (_message.Message,), dict(
  DESCRIPTOR = _RESQUERYBYVOICE,
  __module__ = 'gigagenieRPC_pb2'
  # @@protoc_insertion_point(class_scope:kt.gigagenie.ai.speech.resQueryByVoice)
  ))
_sym_db.RegisterMessage(resQueryByVoice)



_GIGAGENIE = _descriptor.ServiceDescriptor(
  name='Gigagenie',
  full_name='kt.gigagenie.ai.speech.Gigagenie',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1173,
  serialized_end=1645,
  methods=[
  _descriptor.MethodDescriptor(
    name='getVoice2Text',
    full_name='kt.gigagenie.ai.speech.Gigagenie.getVoice2Text',
    index=0,
    containing_service=None,
    input_type=_REQVOICE,
    output_type=_RESTEXT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getText2VoiceUrl',
    full_name='kt.gigagenie.ai.speech.Gigagenie.getText2VoiceUrl',
    index=1,
    containing_service=None,
    input_type=_REQTEXT,
    output_type=_RESURL,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getText2VoiceStream',
    full_name='kt.gigagenie.ai.speech.Gigagenie.getText2VoiceStream',
    index=2,
    containing_service=None,
    input_type=_REQTEXT,
    output_type=_RESVOICE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='queryByText',
    full_name='kt.gigagenie.ai.speech.Gigagenie.queryByText',
    index=3,
    containing_service=None,
    input_type=_REQQUERYTEXT,
    output_type=_RESQUERYTEXT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='queryByVoice',
    full_name='kt.gigagenie.ai.speech.Gigagenie.queryByVoice',
    index=4,
    containing_service=None,
    input_type=_REQQUERYVOICE,
    output_type=_RESQUERYTEXT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GIGAGENIE)

DESCRIPTOR.services_by_name['Gigagenie'] = _GIGAGENIE

# @@protoc_insertion_point(module_scope)
