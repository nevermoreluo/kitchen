from django.db import models



class RecordTimeModel(models.Model):
    """
    记录创建时间和修改时间的Model,抽象Model基类
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
