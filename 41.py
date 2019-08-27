#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 41.py
# @Author: guolei
# @Time  : 01/05/2019 7:55 PM
# @Desc  :缺失的第一个正数
# @Ans   :先遍历一遍，把一个数num放到a[num]上，注意负数和大于数组长度的数不处理，最后找到key和value不等的哪个数，即是要找的第一个正数。注意python中交换数组中两元素的方法,并且交换完需要回退一下，因为当前位置数据已换，但没判断。另外要交换的地方相等则不交换，否则出现死循环。
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        flag = False
        if nums_len == 0 :
            return 1
        i = 0
        while i < len(nums) :
            if flag :
                flag = False
                i -= 1
                continue

            if   nums[i] > 0 and nums[i] <= nums_len  and nums[i] != nums[nums[i] -1]:
                swap = nums[nums[i] -1]
                nums[nums[i] -1] = nums[i]
                nums[i] = swap
                flag = True
            i += 1
                #nums[i],nums[temp -1 ] = nums[temp -1],temp

        for i in range(nums_len):
            if i + 1 != nums[i] :
                return i+1
        return nums_len + 1

nums = [2,2]
obj = Solution()
print obj.firstMissingPositive(nums)