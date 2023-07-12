#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      trigger_models
   Description:
   Author:          dingyong.cui
   date：           2023/7/12
-------------------------------------------------
   Change Activity:
                    2023/7/12
-------------------------------------------------
"""
import datetime
from typing import Union, Text

from pydantic import BaseModel


class CronTrigger(BaseModel):
    year: Union[Text, None] = None
    month: Union[Text, None] = None
    week: Union[Text, None] = None
    day: Union[Text, None] = None
    day_of_week: Union[Text, None] = None
    hour: Union[Text, None] = None
    minute: Union[Text, None] = None
    second: Union[Text, None] = None
    start_date: Union[Text, datetime, None] = None
    end_date: Union[Text, datetime, None] = None


class IntervalTrigger(BaseModel):
    weeks: Union[Text, None] = None
    days: Union[Text, None] = None
    hours: Union[Text, None] = None
    minutes: Union[Text, None] = None
    seconds: Union[Text, None] = None
    start_date: Union[Text, datetime, None] = None
    end_date: Union[Text, datetime, None] = None
    timezone: Union[Text, datetime.tzinfo, None] = None
    jitter: Union[int, None] = None

