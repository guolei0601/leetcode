#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 945_2.py
# @Author: guolei
# @Time  : 16/07/2019 10:04 PM
# @Desc  :
# @Ans   : 用普通方法，以此计算每个重复的数需要增加的次数超时。改进算法后，先对数组排序，遍历一遍数组，每个值都会对下一个值有个期望，小于期望则增加步数，大于期望则重新评估下一个数期望
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        expect = -1
        res = 0
        for i in A:
            if i < expect:
                res += expect - i
                expect += 1
            else:
                expect = i + 1
        return res

obj = Solution()
A = [3,2,1,2,1,7]
print obj.minIncrementForUnique(A)


