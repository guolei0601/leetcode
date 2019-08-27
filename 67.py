#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 67.py
# @Author: guolei
# @Time  : 02/05/2019 8:15 PM
# @Desc  :二进制求和
# @Ans   :利用python特性
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]