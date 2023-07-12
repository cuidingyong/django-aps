#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      apscheduler_func_model_mapper
   Description:
   Author:          dingyong.cui
   date：           2023/7/7
-------------------------------------------------
   Change Activity:
                    2023/7/7
-------------------------------------------------
"""
from typing import Union, List, Dict

from aps.models import ApschedulerFunc


def get_aps_funcs(name: str = None, **kwargs) -> Union[List, None]:
    if name:
        kwargs.setdefault('func_name__contains', name)
    aps_funcs_queryset = ApschedulerFunc.objects.filter(
        **kwargs
    )
    if aps_funcs_queryset.exists():
        return list(aps_funcs_queryset.values())

    return None


def save_aps_funcs(aps_funcs: List[Dict]):
    objs = []
    for aps_func in aps_funcs:
        objs.append(ApschedulerFunc(**aps_func))
    ApschedulerFunc.objects.bulk_create(
        objs
    )


def delete_aps_funcs(conditions: Dict = None, is_all: bool = False):
    if is_all:
        queryset = ApschedulerFunc.objects.all()
    else:
        queryset = ApschedulerFunc.objects.filter(
            **conditions
        )
    deleted, _rows_count = queryset.delete()

    return deleted
