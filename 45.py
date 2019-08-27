#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 45.py
# @Author: guolei
# @Time  : 02/05/2019 8:55 AM
# @Desc  :跳跃游戏2
# @Ans   :贪心算法，记录当前能跳到的最大位置，以及上一次能跳到的最大位置。当上一次跳到的最大位置等于当前的位置时，则不得不跳。注意数组长度为1的情况
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        step = 0
        cur_max_location = 0
        last_max_location = 0
        for i in range(len(nums)):
            cur_max_location = max(cur_max_location,nums[i] + i)
            if i == last_max_location:
                step += 1
                last_max_location = cur_max_location
                if cur_max_location >= len(nums) -1 :
                    break
        return step