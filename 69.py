#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 69.py
# @Author: guolei
# @Time  : 02/05/2019 7:34 PM
# @Desc  : x的平方根
# @Ans   : 每次2分x，判断其平方,太慢了，仅击败 5%。换成二分查找
class Solution(object):

    def mySqrt(self,x):
        l,r = 0,x
        while l != r:
            mid = (l+ r) // 2
            if x < mid * mid:
                r = mid
            else:
                l = mid + 1
        return l -1 if l*l > x else l
    def mySqrt_1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 :
            return 0
        if x < 4:
            return 1
        start = x
        #找到最小的start，其满足再二分，其平方将比x小
        res = 0
        while True :
            start //= 2
            if(start *  start < x):
                break
        start = (start + 1 ) * 2
        while True:
            if((start-1) * (start-1) < x and start * start > x):
                res = start -1
                break
            elif start * start == x:
                res = start
                break
            start -= 1
        return res

x = 6
obj = Solution()
print obj.mySqrt(x)