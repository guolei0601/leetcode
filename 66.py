#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 66.py
# @Author: guolei
# @Time  : 02/05/2019 8:24 PM
# @Desc  :加 1
# @Ans   :
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cur_str = str(int(''.join([str(i) for i in digits])) + 1)
        return [int(j) for j in cur_str]

obj = Solution()
digits = [1,2,3]
print obj.plusOne(digits)