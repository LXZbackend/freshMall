from django.db import models
from jsonfield import JSONField
import copy
from django.utils import timezone
from .logics import model_to_dict


class BaseModel(models.Model):

    """
    所有类的基类
    """

    create_time = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间')
    extinfo = JSONField(
        blank=True, null=True, default={}, help_text='扩展字段')

    class Meta:
        abstract = True

    def canonical(self, exclude=None):
        return model_to_dict(self, exclude)

    @classmethod
    def add_one_object(cls, **kwargs):
        """ 添加一个新的实例
        """
        valid_fields = cls._get_all_valid_fields()
        kws = copy.copy(kwargs)
        extinfo = dict()
        for k, v in kws.items():
            if k not in valid_fields:
                extinfo[k] = v
                kwargs.pop(k)
        if 'extinfo' in kwargs:
            if isinstance(kwargs['extinfo'], dict):
                extinfo.update(kwargs.get('extinfo'))
            else:
                kwargs.pop('extinfo')
        kwargs.update(extinfo=extinfo)
        if 'create_time' in valid_fields:
            kwargs.update(create_time=timezone.now())
        obj = cls(**kwargs)
        obj.save()
        return obj

    @classmethod
    def get_one_object(cls, filters):
        obj = cls.objects.get(**filters)
        return obj

    @classmethod
    def _get_all_valid_fields(cls):
        if not isinstance(cls, models.base.ModelBase):
            return tuple()
        return set(cls._meta.get_all_field_names())

    @classmethod
    def get_object_list(cls, filters={}, exclude_filters={},
                        order_by=('-pk', ), values=None,
                        page_index=None, page_size=None):
        """ 获取对象列表
        """
        objs = cls.objects.filter(**filters)\
                  .exclude(**exclude_filters)\
                  .order_by(*order_by)
        if values:
            objs = objs.values(*values)
        if all(map(lambda x: x is not None, (page_index, page_size))):
            start = page_index * page_size
            end = start + page_size
            objs = objs[start: end]
        return objs
