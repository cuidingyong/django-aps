#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      urls
   Description:
   Author:          dingyong.cui
   date：           2023/7/11
-------------------------------------------------
   Change Activity:
                    2023/7/11
-------------------------------------------------
"""
from django.urls import path

from aps.views.apscheduler_view import RegisteredFuncQueryView

urlpatterns = [
    path(r'func/query', RegisteredFuncQueryView.as_view())
]