#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 47.py
# @Author: guolei
# @Time  : 02/05/2019 9:38 AM
# @Desc  :全排列2，数组中包含重复元素，返回所有不重复的全排列
# @Ans   :深度优先搜素。每次去掉一个元素形成新数组，然后往已有list添加
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        new_nums = sorted(nums)
        self.DFS([],new_nums)
        return self.res

    def DFS(self,cur_list,nums):
        if(not nums):
            self.res.append(cur_list[:])
            #return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.DFS(cur_list + [nums[i]],nums[:i] + nums[i+1:])




nums = [1,2,1]
obj = Solution()
print obj.permuteUnique(nums)