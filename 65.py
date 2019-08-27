#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 65.py
# @Author: guolei
# @Time  : 02/05/2019 5:46 PM
# @Desc  :有效数字
# @Ans   :如果遍历方式比较麻烦。直接调用系统函数出结果
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False