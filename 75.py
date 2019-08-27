#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 75.py
# @Author: guolei
# @Time  : 15/07/2019 10:29 AM
# @Desc  :
# @Ans   :分别用一个指针表示当前0位置的右侧，2位置的左侧和当前的位置。这两个位置分别用来交换数据。
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        total = len(nums)
        if total < 2 :
            return nums
        zero_dire = 0
        two_dire  = total - 1
        cur_dire  = 0
        while cur_dire <= two_dire :
            if nums[cur_dire] == 0 and cur_dire != zero_dire:
                nums[zero_dire] , nums[cur_dire] = nums[cur_dire] ,nums[zero_dire]
                zero_dire += 1
            elif nums[cur_dire] == 2 and cur_dire != two_dire:
                nums[two_dire], nums[cur_dire] = nums[cur_dire], nums[two_dire]
                two_dire -= 1
            else :
                cur_dire += 1
        return nums

obj = Solution()
nums= [0,0]
print obj.sortColors(nums)

