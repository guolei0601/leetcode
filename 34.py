#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 34.py
# @Author: guolei
# @Time  : 01/05/2019 11:11 AM
# @Desc  :在排序数组中找目标元素的起始及结束位置。思路，先二分查找到一个该数的位置，然后对该数左边，找等于target且位置最小，右边等于target且位置最大的target，最后进行位置组合。
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1:
            if nums[0] != target:
                return [-1,-1]
            return [0,0]
        divided = self.binarySearch(0,len(nums)-1,nums,target)
        if divided != -1 :
            res_left = self.binarySearchLeft(0,divided,nums,target)
            res_right = self.binarySearchRight(divided+1,len(nums)-1,nums,target)
            if res_left != -1 :
                return[res_left,max (divided,res_right)]
            else:
                return[divided,max (divided,res_right)]
        return res

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

    def binarySearchLeft(self,left,right,nums,target):

        #只有一个数的情况
        if left >= right :
            if nums[right] == target:
                return right
            return -1

        if nums[left] > target :
            return -1
        elif nums[left] == target:
            return left
        else:
            mid = (left + right) // 2
            res_left = self.binarySearchLeft(left,mid,nums,target)
            res_right = self.binarySearchLeft(mid+1,right,nums,target)
            if res_left != -1:
                return res_left
            if res_right != -1:
                return res_right
            return -1

    def binarySearchRight(self, left, right, nums, target):

        #只有一个数的情况
        if left >= right :
            if nums[right] == target:
                return right
            return -1
        if nums[right] < target :
            return -1
        elif nums[right] == target:
            return right
        else:
            mid = (left + right) // 2
            res_left = self.binarySearchRight(left,mid,nums,target)
            res_right = self.binarySearchRight(mid+1,right,nums,target)
            return max(res_left,res_right)

obj = Solution()
nums = [2,2]
target = 3
print obj.searchRange(nums,target)
