#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 58.py
# @Author: guolei
# @Time  : 02/05/2019 8:32 PM
# @Desc  :返回最后一个单词的长度
# @Ans   :
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])