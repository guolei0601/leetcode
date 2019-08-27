#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 55.py
# @Author: guolei
# @Time  : 02/05/2019 8:39 AM
# @Desc  :跳跃游戏
# @Ans   :贪心算法，计算每一步能跳跃到的最大位置，如果当前最大能跳到的位置小于当前的位置，则停止（此时对应为0的情况）
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_location = 0
        for i in range(len(nums)):
            if i > max_location :
                return False
            max_location = max(max_location,i+nums[i])
            if max_location >= len(nums) -1 :
                return True