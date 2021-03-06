from FinbotServer.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from FinbotServer.protocol.TProtocol import TProtocolException
import sys
from FinbotServer.transport import TTransport

class LoginResultType(object):
    SUCCESS = 1
    REQUIRE_QRCODE = 2
    REQUIRE_DEVICE_CONFIRM = 3

    _VALUES_TO_NAMES = {
        1: "SUCCESS",
        2: "REQUIRE_QRCODE",
        3: "REQUIRE_DEVICE_CONFIRM",
    }

    _NAMES_TO_VALUES = {
        "SUCCESS": 1,
        "REQUIRE_QRCODE": 2,
        "REQUIRE_DEVICE_CONFIRM": 3,
    }


class IdentityProvider(object):
    UNKNOWN = 0
    LINE = 1
    NAVER_KR = 2

    _VALUES_TO_NAMES = {
        0: "UNKNOWN",
        1: "LINE",
        2: "NAVER_KR",
    }

    _NAMES_TO_VALUES = {
        "UNKNOWN": 0,
        "LINE": 1,
        "NAVER_KR": 2,
    }


class ErrorCode(object):
    ILLEGAL_ARGUMENT = 0
    AUTHENTICATION_FAILED = 1
    DB_FAILED = 2
    INVALID_STATE = 3
    EXCESSIVE_ACCESS = 4
    NOT_FOUND = 5
    INVALID_LENGTH = 6
    NOT_AVAILABLE_USER = 7
    NOT_AUTHORIZED_DEVICE = 8
    INVALID_MID = 9
    NOT_A_MEMBER = 10
    INCOMPATIBLE_APP_VERSION = 11
    NOT_READY = 12
    NOT_AVAILABLE_SESSION = 13
    NOT_AUTHORIZED_SESSION = 14
    SYSTEM_ERROR = 15
    NO_AVAILABLE_VERIFICATION_METHOD = 16
    NOT_AUTHENTICATED = 17
    INVALID_IDENTITY_CREDENTIAL = 18
    NOT_AVAILABLE_IDENTITY_IDENTIFIER = 19
    INTERNAL_ERROR = 20
    NO_SUCH_IDENTITY_IDENFIER = 21
    DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY = 22
    ILLEGAL_IDENTITY_CREDENTIAL = 23
    UNKNOWN_CHANNEL = 24
    NO_SUCH_MESSAGE_BOX = 25
    NOT_AVAILABLE_MESSAGE_BOX = 26
    CHANNEL_DOES_NOT_MATCH = 27
    NOT_YOUR_MESSAGE = 28
    MESSAGE_DEFINED_ERROR = 29
    USER_CANNOT_ACCEPT_PRESENTS = 30
    USER_NOT_STICKER_OWNER = 32
    MAINTENANCE_ERROR = 33
    ACCOUNT_NOT_MATCHED = 34
    ABUSE_BLOCK = 35
    NOT_FRIEND = 36
    NOT_ALLOWED_CALL = 37
    BLOCK_FRIEND = 38
    INCOMPATIBLE_VOIP_VERSION = 39
    INVALID_SNS_ACCESS_TOKEN = 40
    EXTERNAL_SERVICE_NOT_AVAILABLE = 41
    NOT_ALLOWED_ADD_CONTACT = 42
    NOT_CERTIFICATED = 43
    NOT_ALLOWED_SECONDARY_DEVICE = 44
    INVALID_PIN_CODE = 45
    NOT_FOUND_IDENTITY_CREDENTIAL = 46
    EXCEED_FILE_MAX_SIZE = 47
    EXCEED_DAILY_QUOTA = 48
    NOT_SUPPORT_SEND_FILE = 49
    MUST_UPGRADE = 50
    NOT_AVAILABLE_PIN_CODE_SESSION = 51

    _VALUES_TO_NAMES = {
        0: "ILLEGAL_ARGUMENT",
        1: "AUTHENTICATION_FAILED",
        2: "DB_FAILED",
        3: "INVALID_STATE",
        4: "EXCESSIVE_ACCESS",
        5: "NOT_FOUND",
        6: "INVALID_LENGTH",
        7: "NOT_AVAILABLE_USER",
        8: "NOT_AUTHORIZED_DEVICE",
        9: "INVALID_MID",
        10: "NOT_A_MEMBER",
        11: "INCOMPATIBLE_APP_VERSION",
        12: "NOT_READY",
        13: "NOT_AVAILABLE_SESSION",
        14: "NOT_AUTHORIZED_SESSION",
        15: "SYSTEM_ERROR",
        16: "NO_AVAILABLE_VERIFICATION_METHOD",
        17: "NOT_AUTHENTICATED",
        18: "INVALID_IDENTITY_CREDENTIAL",
        19: "NOT_AVAILABLE_IDENTITY_IDENTIFIER",
        20: "INTERNAL_ERROR",
        21: "NO_SUCH_IDENTITY_IDENFIER",
        22: "DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY",
        23: "ILLEGAL_IDENTITY_CREDENTIAL",
        24: "UNKNOWN_CHANNEL",
        25: "NO_SUCH_MESSAGE_BOX",
        26: "NOT_AVAILABLE_MESSAGE_BOX",
        27: "CHANNEL_DOES_NOT_MATCH",
        28: "NOT_YOUR_MESSAGE",
        29: "MESSAGE_DEFINED_ERROR",
        30: "USER_CANNOT_ACCEPT_PRESENTS",
        32: "USER_NOT_STICKER_OWNER",
        33: "MAINTENANCE_ERROR",
        34: "ACCOUNT_NOT_MATCHED",
        35: "ABUSE_BLOCK",
        36: "NOT_FRIEND",
        37: "NOT_ALLOWED_CALL",
        38: "BLOCK_FRIEND",
        39: "INCOMPATIBLE_VOIP_VERSION",
        40: "INVALID_SNS_ACCESS_TOKEN",
        41: "EXTERNAL_SERVICE_NOT_AVAILABLE",
        42: "NOT_ALLOWED_ADD_CONTACT",
        43: "NOT_CERTIFICATED",
        44: "NOT_ALLOWED_SECONDARY_DEVICE",
        45: "INVALID_PIN_CODE",
        46: "NOT_FOUND_IDENTITY_CREDENTIAL",
        47: "EXCEED_FILE_MAX_SIZE",
        48: "EXCEED_DAILY_QUOTA",
        49: "NOT_SUPPORT_SEND_FILE",
        50: "MUST_UPGRADE",
        51: "NOT_AVAILABLE_PIN_CODE_SESSION",
    }

    _NAMES_TO_VALUES = {
        "ILLEGAL_ARGUMENT": 0,
        "AUTHENTICATION_FAILED": 1,
        "DB_FAILED": 2,
        "INVALID_STATE": 3,
        "EXCESSIVE_ACCESS": 4,
        "NOT_FOUND": 5,
        "INVALID_LENGTH": 6,
        "NOT_AVAILABLE_USER": 7,
        "NOT_AUTHORIZED_DEVICE": 8,
        "INVALID_MID": 9,
        "NOT_A_MEMBER": 10,
        "INCOMPATIBLE_APP_VERSION": 11,
        "NOT_READY": 12,
        "NOT_AVAILABLE_SESSION": 13,
        "NOT_AUTHORIZED_SESSION": 14,
        "SYSTEM_ERROR": 15,
        "NO_AVAILABLE_VERIFICATION_METHOD": 16,
        "NOT_AUTHENTICATED": 17,
        "INVALID_IDENTITY_CREDENTIAL": 18,
        "NOT_AVAILABLE_IDENTITY_IDENTIFIER": 19,
        "INTERNAL_ERROR": 20,
        "NO_SUCH_IDENTITY_IDENFIER": 21,
        "DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY": 22,
        "ILLEGAL_IDENTITY_CREDENTIAL": 23,
        "UNKNOWN_CHANNEL": 24,
        "NO_SUCH_MESSAGE_BOX": 25,
        "NOT_AVAILABLE_MESSAGE_BOX": 26,
        "CHANNEL_DOES_NOT_MATCH": 27,
        "NOT_YOUR_MESSAGE": 28,
        "MESSAGE_DEFINED_ERROR": 29,
        "USER_CANNOT_ACCEPT_PRESENTS": 30,
        "USER_NOT_STICKER_OWNER": 32,
        "MAINTENANCE_ERROR": 33,
        "ACCOUNT_NOT_MATCHED": 34,
        "ABUSE_BLOCK": 35,
        "NOT_FRIEND": 36,
        "NOT_ALLOWED_CALL": 37,
        "BLOCK_FRIEND": 38,
        "INCOMPATIBLE_VOIP_VERSION": 39,
        "INVALID_SNS_ACCESS_TOKEN": 40,
        "EXTERNAL_SERVICE_NOT_AVAILABLE": 41,
        "NOT_ALLOWED_ADD_CONTACT": 42,
        "NOT_CERTIFICATED": 43,
        "NOT_ALLOWED_SECONDARY_DEVICE": 44,
        "INVALID_PIN_CODE": 45,
        "NOT_FOUND_IDENTITY_CREDENTIAL": 46,
        "EXCEED_FILE_MAX_SIZE": 47,
        "EXCEED_DAILY_QUOTA": 48,
        "NOT_SUPPORT_SEND_FILE": 49,
        "MUST_UPGRADE": 50,
        "NOT_AVAILABLE_PIN_CODE_SESSION": 51,
    }


class VerificationMethod(object):
    NO_AVAILABLE = 0
    PIN_VIA_SMS = 1
    CALLERID_INDIGO = 2
    PIN_VIA_TTS = 4
    SKIP = 10

    _VALUES_TO_NAMES = {
        0: "NO_AVAILABLE",
        1: "PIN_VIA_SMS",
        2: "CALLERID_INDIGO",
        4: "PIN_VIA_TTS",
        10: "SKIP",
    }

    _NAMES_TO_VALUES = {
        "NO_AVAILABLE": 0,
        "PIN_VIA_SMS": 1,
        "CALLERID_INDIGO": 2,
        "PIN_VIA_TTS": 4,
        "SKIP": 10,
    }


class TalkException(TException):
    """
    Attributes:
     - code
     - reason
     - parameterMap
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None, ),  # 1
        (2, TType.STRING, 'reason', 'UTF8', None, ),  # 2
        (3, TType.MAP, 'parameterMap', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, code=None, reason=None, parameterMap=None,):
        self.code = code
        self.reason = reason
        self.parameterMap = parameterMap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.reason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.parameterMap = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.parameterMap[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('TalkException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.reason is not None:
            oprot.writeFieldBegin('reason', TType.STRING, 2)
            oprot.writeString(self.reason.encode('utf-8') if sys.version_info[0] == 2 else self.reason)
            oprot.writeFieldEnd()
        if self.parameterMap is not None:
            oprot.writeFieldBegin('parameterMap', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
            for kiter7, viter8 in self.parameterMap.items():
                oprot.writeString(kiter7.encode('utf-8') if sys.version_info[0] == 2 else kiter7)
                oprot.writeString(viter8.encode('utf-8') if sys.version_info[0] == 2 else viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class VerificationSessionData(object):
    """
    Attributes:
     - sessionId
     - method
     - callback
     - nomarizediPhone
     - countryCode
     - nationalSignificantNumber
     - availableVerificationMethods
     - callerIdMask
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'sessionId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'method', None, None, ),  # 2
        (3, TType.STRING, 'callback', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'nomarizediPhone', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'countryCode', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'nationalSignificantNumber', 'UTF8', None, ),  # 6
        (7, TType.I32, 'availableVerificationMethods', None, None, ),  # 7
        (8, TType.STRING, 'callerIdMask', 'UTF8', None, ),  # 8
    )

    def __init__(self, sessionId=None, method=None, callback=None, nomarizediPhone=None, countryCode=None, nationalSignificantNumber=None, availableVerificationMethods=None, callerIdMask=None,):
        self.sessionId = sessionId
        self.method = method
        self.callback = callback
        self.nomarizediPhone = nomarizediPhone
        self.countryCode = countryCode
        self.nationalSignificantNumber = nationalSignificantNumber
        self.availableVerificationMethods = availableVerificationMethods
        self.callerIdMask = callerIdMask

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.sessionId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.method = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.callback = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.nomarizediPhone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.countryCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.nationalSignificantNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.availableVerificationMethods = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.callerIdMask = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('VerificationSessionData')
        if self.sessionId is not None:
            oprot.writeFieldBegin('sessionId', TType.STRING, 1)
            oprot.writeString(self.sessionId.encode('utf-8') if sys.version_info[0] == 2 else self.sessionId)
            oprot.writeFieldEnd()
        if self.method is not None:
            oprot.writeFieldBegin('method', TType.I32, 2)
            oprot.writeI32(self.method)
            oprot.writeFieldEnd()
        if self.callback is not None:
            oprot.writeFieldBegin('callback', TType.STRING, 3)
            oprot.writeString(self.callback.encode('utf-8') if sys.version_info[0] == 2 else self.callback)
            oprot.writeFieldEnd()
        if self.nomarizediPhone is not None:
            oprot.writeFieldBegin('nomarizediPhone', TType.STRING, 4)
            oprot.writeString(self.nomarizediPhone.encode('utf-8') if sys.version_info[0] == 2 else self.nomarizediPhone)
            oprot.writeFieldEnd()
        if self.countryCode is not None:
            oprot.writeFieldBegin('countryCode', TType.STRING, 5)
            oprot.writeString(self.countryCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryCode)
            oprot.writeFieldEnd()
        if self.nationalSignificantNumber is not None:
            oprot.writeFieldBegin('nationalSignificantNumber', TType.STRING, 6)
            oprot.writeString(self.nationalSignificantNumber.encode('utf-8') if sys.version_info[0] == 2 else self.nationalSignificantNumber)
            oprot.writeFieldEnd()
        if self.availableVerificationMethods is not None:
            oprot.writeFieldBegin('availableVerificationMethods', TType.I32, 7)
            oprot.writeI32(self.availableVerificationMethods)
            oprot.writeFieldEnd()
        if self.callerIdMask is not None:
            oprot.writeFieldBegin('callerIdMask', TType.STRING, 8)
            oprot.writeString(self.callerIdMask.encode('utf-8') if sys.version_info[0] == 2 else self.callerIdMask)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginResult(object):
    """
    Attributes:
     - authToken
     - certificate
     - verifier
     - pinCode
     - type
     - lastPrimaryBindTime
     - displayMessage
     - sessionForSMSConfirm
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'authToken', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'certificate', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'verifier', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'pinCode', 'UTF8', None, ),  # 4
        (5, TType.I32, 'type', None, None, ),  # 5
        (6, TType.I64, 'lastPrimaryBindTime', None, None, ),  # 6
        (7, TType.STRING, 'displayMessage', 'UTF8', None, ),  # 7
        (8, TType.STRUCT, 'sessionForSMSConfirm', (VerificationSessionData, VerificationSessionData.thrift_spec), None, ),  # 8
    )

    def __init__(self, authToken=None, certificate=None, verifier=None, pinCode=None, type=None, lastPrimaryBindTime=None, displayMessage=None, sessionForSMSConfirm=None,):
        self.authToken = authToken
        self.certificate = certificate
        self.verifier = verifier
        self.pinCode = pinCode
        self.type = type
        self.lastPrimaryBindTime = lastPrimaryBindTime
        self.displayMessage = displayMessage
        self.sessionForSMSConfirm = sessionForSMSConfirm

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.authToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pinCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.lastPrimaryBindTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.displayMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.sessionForSMSConfirm = VerificationSessionData()
                    self.sessionForSMSConfirm.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LoginResult')
        if self.authToken is not None:
            oprot.writeFieldBegin('authToken', TType.STRING, 1)
            oprot.writeString(self.authToken.encode('utf-8') if sys.version_info[0] == 2 else self.authToken)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 2)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 3)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.pinCode is not None:
            oprot.writeFieldBegin('pinCode', TType.STRING, 4)
            oprot.writeString(self.pinCode.encode('utf-8') if sys.version_info[0] == 2 else self.pinCode)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 5)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.lastPrimaryBindTime is not None:
            oprot.writeFieldBegin('lastPrimaryBindTime', TType.I64, 6)
            oprot.writeI64(self.lastPrimaryBindTime)
            oprot.writeFieldEnd()
        if self.displayMessage is not None:
            oprot.writeFieldBegin('displayMessage', TType.STRING, 7)
            oprot.writeString(self.displayMessage.encode('utf-8') if sys.version_info[0] == 2 else self.displayMessage)
            oprot.writeFieldEnd()
        if self.sessionForSMSConfirm is not None:
            oprot.writeFieldBegin('sessionForSMSConfirm', TType.STRUCT, 8)
            self.sessionForSMSConfirm.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginRequest(object):
    """
    Attributes:
     - type
     - identityProvider
     - identifier
     - password
     - keepLoggedIn
     - accessLocation
     - systemName
     - certificate
     - verifier
     - secret
     - e2eeVersion
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ),  # 1
        (2, TType.I32, 'identityProvider', None, None, ),  # 2
        (3, TType.STRING, 'identifier', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'password', 'UTF8', None, ),  # 4
        (5, TType.BOOL, 'keepLoggedIn', None, None, ),  # 5
        (6, TType.STRING, 'accessLocation', 'UTF8', None, ),  # 6
        (7, TType.STRING, 'systemName', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'certificate', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'verifier', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'secret', 'UTF8', None, ),  # 10
        (11, TType.I32, 'e2eeVersion', None, None, ),  # 11
    )

    def __init__(self, type=None, identityProvider=None, identifier=None, password=None, keepLoggedIn=None, accessLocation=None, systemName=None, certificate=None, verifier=None, secret=None, e2eeVersion=None,):
        self.type = type
        self.identityProvider = identityProvider
        self.identifier = identifier
        self.password = password
        self.keepLoggedIn = keepLoggedIn
        self.accessLocation = accessLocation
        self.systemName = systemName
        self.certificate = certificate
        self.verifier = verifier
        self.secret = secret
        self.e2eeVersion = e2eeVersion

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.identityProvider = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.identifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.keepLoggedIn = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.accessLocation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.systemName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.secret = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.e2eeVersion = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LoginRequest')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.identityProvider is not None:
            oprot.writeFieldBegin('identityProvider', TType.I32, 2)
            oprot.writeI32(self.identityProvider)
            oprot.writeFieldEnd()
        if self.identifier is not None:
            oprot.writeFieldBegin('identifier', TType.STRING, 3)
            oprot.writeString(self.identifier.encode('utf-8') if sys.version_info[0] == 2 else self.identifier)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 4)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        if self.keepLoggedIn is not None:
            oprot.writeFieldBegin('keepLoggedIn', TType.BOOL, 5)
            oprot.writeBool(self.keepLoggedIn)
            oprot.writeFieldEnd()
        if self.accessLocation is not None:
            oprot.writeFieldBegin('accessLocation', TType.STRING, 6)
            oprot.writeString(self.accessLocation.encode('utf-8') if sys.version_info[0] == 2 else self.accessLocation)
            oprot.writeFieldEnd()
        if self.systemName is not None:
            oprot.writeFieldBegin('systemName', TType.STRING, 7)
            oprot.writeString(self.systemName.encode('utf-8') if sys.version_info[0] == 2 else self.systemName)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 8)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 9)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.secret is not None:
            oprot.writeFieldBegin('secret', TType.STRING, 10)
            oprot.writeString(self.secret.encode('utf-8') if sys.version_info[0] == 2 else self.secret)
            oprot.writeFieldEnd()
        if self.e2eeVersion is not None:
            oprot.writeFieldBegin('e2eeVersion', TType.I32, 11)
            oprot.writeI32(self.e2eeVersion)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
