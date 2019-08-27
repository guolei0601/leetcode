#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 78.py
# @Author: guolei
# @Time  : 02/07/2019 3:22 PM
# @Desc  :
# @Ans   :回溯法
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total = len(nums)
        def f(start,current):
            for i in range(start,total):
                current.append(nums[i])
                res.append(current[:])
                f(i+1,current)
                current.pop()
                #current = []
        res=[]
        f(0,[])
        res.append([])
        return res


obj = Solution()
print obj.subsets([1,2,3,5])


