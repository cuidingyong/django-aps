#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      service_test
   Description:
   Author:          dingyong.cui
   date：           2023/7/7
-------------------------------------------------
   Change Activity:
                    2023/7/7
-------------------------------------------------
"""
from aps.utils.register import aps_register


@aps_register
def add2(m: int, n: int, x: int = 2):
    return m + n + x


@aps_register
def add3(m, n, x):
    return m + n + x


class ApsTest:
    """注释1"""

    def __init__(self):
        pass

    @aps_register
    def add1(self, a: int, b: int):
        """注释2.

        Args:
            a: 参数a
            b: 参数b

        Returns:
            一个数字

            10

        Raises:

        """
        def addd():
            return None
        print(a + b)
        return a + b
