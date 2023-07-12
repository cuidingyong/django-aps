#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      apscheduler_serializers
   Description:
   Author:          dingyong.cui
   date：           2023/7/6
-------------------------------------------------
   Change Activity:
                    2023/7/6
-------------------------------------------------
"""
from rest_framework import serializers

__all__ = [
    'RegisteredFuncQuerySerializers',
    'SchedulerJobAddSerializers'
]


class RegisteredFuncQuerySerializers(serializers.Serializer):  # noqa
    func_name = serializers.CharField(max_length=256, required=False, help_text='定时任务方法名')


class TriggerParamsSerializers(serializers.Serializer):  # noqa
    start_time = serializers.CharField(help_text='开始执行时间', required=False)
    end_time = serializers.CharField(help_text='结束执行时间', required=False)
    year = serializers.CharField(help_text='年', required=False)
    day_of_week = serializers.CharField(help_text='周', required=False)
    month = serializers.CharField(help_text='月', required=False)
    day = serializers.CharField(help_text='日', required=False)
    week = serializers.CharField(help_text='周', required=False)
    hour = serializers.CharField(help_text='小时', required=False)
    minute = serializers.CharField(help_text='分钟', required=False)
    second = serializers.CharField(help_text='秒', required=False)

    def validate(self, attrs):
        day_of_week = attrs.get('day_of_week')
        day = attrs.get('day')
        if day_of_week and day:
            raise serializers.ValidationError('Both "day" and "day_of_week" cannot be selected')
        return attrs


class TriggerSerializers(serializers.Serializer):  # noqa
    trigger_type = serializers.CharField(max_length=64, help_text='触发器类型')
    trigger_params = TriggerParamsSerializers(help_text='触发器参数')


class SchedulerJobAddSerializers(serializers.Serializer):  # noqa
    name = serializers.CharField(max_length=256, help_text='定时任务名称')
    func_module = serializers.CharField(max_length=256, help_text='方法所属模块')
    func_name = serializers.CharField(max_length=256, help_text='方法名')
    func_args = serializers.ListField(required=False, default=None, help_text='方法参数')
    func_kwargs = serializers.DictField(required=False, default=None, help_text='方法关键字参数')
    trigger = TriggerSerializers(help_text='触发器')
