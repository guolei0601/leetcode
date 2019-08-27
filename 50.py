#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 50.py
# @Author: guolei
# @Time  : 02/05/2019 12:39 PM
# @Desc  :pow(x,y)
# @Ans   :利用性质 x ^ n = x^2 ^ n/2 ，当n是负数时，结果只需要是倒数即可
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1.0
        i = abs(n)
        while (i != 0) :
            if (i %2 != 0):
                res *= x
            x *= x
            i = i//2
        return res if n > 0 else 1/res
obj = Solution()
x = 2.000000
n = 2
print obj.myPow(x,n)

