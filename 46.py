#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 46.py
# @Author: guolei
# @Time  : 02/05/2019 9:27 AM
# @Desc  :求一个没有重复的数组的全排列
# @Ans   :回溯算法
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS([],nums)
        return self.res

    def DFS(self,cur_list,nums):
        if(not nums):
            self.res.append(cur_list[:])
        for i in range(len(nums)):
            self.DFS(cur_list + [nums[i]],nums[:i]+ nums[i+1:])

nums = [1,3,2]
obj = Solution()
print obj.permute(nums)
