#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 35.py
# @Author: guolei
# @Time  : 2019/4/28 下午11:29
# @Desc  :搜素插入位置，二分查找法，注意分界符
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = len(nums)
        if total == 0:
            return 0
        elif total == 1:
            return 0 if nums[0] >= target else 1
        else:
            return self.subSearchInsert(0, total, nums, target)

    def subSearchInsert(self, left, right, nums, target):
        mid = int((left + right) / 2)
        if left == right:
            return left  if nums[left] >= target else left + 1
        elif left + 1 == right:
            if nums[left]  >= target : return left
            elif nums[right] >= target : return right
            else : return right +1
        elif nums[mid] >= target:
            return self.subSearchInsert(left, mid, nums, target)
        else:
            return self.subSearchInsert(mid, right, nums, target)
obj = Solution()
print obj.searchInsert([1, 3, 5, 6], 7)