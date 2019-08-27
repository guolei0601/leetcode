#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 33.py
# @Author: guolei
# @Time  : 01/05/2019 9:44 AM
# @Desc  :搜索逆转排序数组，基本思路，先二分查找到旋转的位置，再以此位置为边界，左右两边各二分查找
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums) == 0):
            return -1
        elif(len(nums) == 1):
            return 0 if nums[0] == target else -1
        divide_index = self.binarySearchMin(0,len(nums)-1,nums)
        #print divide_index
        #exit(0)
        res = res_left = res_right = -1
        if divide_index > 0:
            res_left = self.binarySearch(0,divide_index-1,nums,target)
        if res_left != -1 :
            return res_left
        res_right = self.binarySearch(divide_index,len(nums)-1,nums,target)
        if res_right != -1 :
            return res_right
        return res

    def binarySearchMin(self,left,right,nums):
        if nums[left] <= nums[right]:
            return left
        else:
            mid = int((left + right) /2 )
            left_min = self.binarySearchMin(left,mid,nums)
            right_min = self.binarySearchMin(mid+1,right,nums)
            return left_min if(nums[left_min] < nums[right_min]) else right_min

    def binarySearch(self,left,right,nums,target):
        if left >= right:
            if nums[right] != target:
                return -1
            else:
                return right
        if nums[left] > target:
            return -1
        elif nums[left] == target:
            return left
        else :
            mid = int((left + right)/2)
            if nums[mid] < target :
                return self.binarySearch(mid+1,right,nums,target)
            elif nums[mid] == target:
                return mid
            else:
                return self.binarySearch(left,mid,nums,target)

nums = [2,2,2,2]
obj = Solution()
print obj.search(nums,4)

