#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 80.py
# @Author: guolei
# @Time  : 15/07/2019 10:49 AM
# @Desc  :
# @Ans   :不超过2个，只需要比较该值和前两个值是否不同，如果不同，就可以给当前数组赋值，如果同，说明已经有2个了
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for n in nums :
            if t < 2 or nums[t - 2] != n:
                nums[t] = n
                t += 1
        return t

obj = Solution()
nums = [1,1,1,2,2,3]
print obj.removeDuplicates(nums)