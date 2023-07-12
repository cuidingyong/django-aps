#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      discover_service
   Description:
   Author:          dingyong.cui
   date：           2023/7/6
-------------------------------------------------
   Change Activity:
                    2023/7/6
-------------------------------------------------
"""
from typing import List, Dict

from django.db import transaction

from aps.repository import apscheduler_func_model_mapper
from aps.settings import aps_settings
from aps.utils.common import check_table_exist
from aps.utils.discover import autodiscover_aps


class DiscoverService:

    def __init__(self, schema: str = None):
        self._schema = schema

    @property
    def schema(self):
        if self._schema is None:
            self._schema = aps_settings.DEFAULT_DISCOVER_SCHEMA

        return self._schema

    def get_apscheduler_funcs(self, name: str = None):
        if self.schema == 'database':
            return apscheduler_func_model_mapper.get_aps_funcs(name)

        return self.discover_apscheduler(name)

    @staticmethod
    def discover_apscheduler(name: str = None) -> List[Dict]:
        """ Discover apscheduler functions

        param: name - which function name contain it
        """
        aps_funcs = autodiscover_aps()
        if name is None:
            return aps_funcs
        aps_name_funcs = []
        for aps_func in aps_funcs:
            if name in aps_func.get('func_name'):
                aps_name_funcs.append(aps_func)

        return aps_name_funcs

    @classmethod
    def sync_aps_to_db(cls):
        """ Synchronize auto discover aps function to the database

        """
        aps_funcs = autodiscover_aps()
        with transaction.atomic():
            apscheduler_func_model_mapper.delete_aps_funcs(is_all=True)
            apscheduler_func_model_mapper.save_aps_funcs(aps_funcs)
