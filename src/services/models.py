"""

"""
from django.db.models import CharField, URLField, GenericIPAddressField, IntegerField, CASCADE, ForeignKey, \
    TextChoices, BooleanField, DateTimeField
from django.utils.translation import gettext_lazy as _
from framework.models import RecordTimeModel


class CloudServiceProvider(RecordTimeModel):
    """
    服务器提供商

    Attributes:
        name (str): 服务商名称
        homepage (str): 服务商主页
        account (str): 账号
    """
    name: CharField = CharField(max_length=100)
    homepage: URLField = URLField()
    account: CharField = CharField(max_length=20)


class VPS(RecordTimeModel):
    """
    VPS服务器信息

    Attributes:
        hostname (str): vps hostname
        IPv4 (str): IP地址
        SSH_Port (int): ssh端口
        provider (ForeignKey): 服务提供商
        expired (datetime): 过期时间
    """
    hostname: CharField = CharField(max_length=200)
    IPv4: GenericIPAddressField = GenericIPAddressField()
    SSH_Port: IntegerField = IntegerField(default=22)
    provider: ForeignKey = ForeignKey(CloudServiceProvider, on_delete=CASCADE)
    expired: DateTimeField = DateTimeField('date VPS expired')


class Service(RecordTimeModel):
    """
    Service in VPS
    Attributes:
        vps (ForeignKey): vps机器
        name (str): 名称
        des (str): 描述
        port (int): 服务占用端口
    """
    vps: ForeignKey = ForeignKey(VPS, on_delete=CASCADE)
    name: CharField = CharField(max_length=30)
    des: CharField = CharField(max_length=100)
    port: IntegerField = IntegerField()


class DetectType(TextChoices):
    """
    DetectType
    """
    DNS = 'DNS', _('dns')
    HTTPS = 'HTTPS', _('http')
    TCP_PORT = 'TCPPort', _('port')
    PING = 'Ping', _('ping')


class DetectSetting(RecordTimeModel):
    """
    监控设置

    Attributes:
        name (str): 监控名称
        url (str): 监控探测地址
        method (str): HTTP方法
        hostname (str): 监控hostname
        port (int): 监控端口
        maxretries (int): 重试次数
        weight (int): 权重
        active (int):
        _type (DetectType): 监控探测类型
        interval (int): 探测间隔
        retryInterval (int): 探测重试间隔
        resendInterval (int):
        keyword (str):
        expiryNotification (bool):
        ignoreTls (bool):
        upsideDown (bool):
        maxredirects (int):
        dns_resolve_type (str):
        dns_resolve_server (str):
    """
    name: CharField = CharField(max_length=30)
    url: URLField = URLField(max_length=100)
    method: CharField = CharField(max_length=10)
    hostname: CharField = CharField(max_length=30)
    port: IntegerField = IntegerField(default=0)
    maxretries: IntegerField = IntegerField(default=0)
    weight: IntegerField = IntegerField(default=2000)
    active: IntegerField = IntegerField(default=1)
    _type: CharField = CharField(max_length=10, choices=DetectType.choices, default=DetectType.HTTPS)
    interval: IntegerField = IntegerField(default=60)
    retryInterval: IntegerField = IntegerField(default=60)
    resendInterval: IntegerField = IntegerField(default=0)
    keyword: CharField = CharField(max_length=30)
    expiryNotification: BooleanField = BooleanField(default=False)
    ignoreTls: BooleanField = BooleanField(default=False)
    upsideDown: BooleanField = BooleanField(default=False)
    maxredirects: IntegerField = IntegerField(default=10)
    dns_resolve_type: CharField = CharField(max_length=20, default="A")
    dns_resolve_server: GenericIPAddressField = GenericIPAddressField()
    # = IntegerField() accepted_statuscodes
    # dns_last_result = IntegerField()
