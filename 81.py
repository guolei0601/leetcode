#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 81.py
# @Author: guolei
# @Time  : 15/07/2019 1:32 PM
# @Desc  :
# @Ans   :两次二分查找，注意第一次二分查找的时候找到分割的位置，加了一个标志位，用以区别是返回左位置还是右位置
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums) == 0):
            return False
        elif(len(nums) == 1):
            return True if nums[0] == target else False
        divide_index = self.binarySearchMin(0,len(nums)-1,nums,False)
        #print divide_index
        #exit(0)
        res = res_left = res_right = -1
        if divide_index > 0:
            res_left = self.binarySearch(0,divide_index-1,nums,target)
        if res_left != -1 :
            return True
        res_right = self.binarySearch(divide_index,len(nums)-1,nums,target)
        if res_right != -1 :
            return True
        return False

    def binarySearchMin(self,left,right,nums,equal_flag):
        if nums[left] < nums[right]:
            if equal_flag == True :
                return right
            else :
                return left

        elif nums[left] == nums[right]:
            if left + 1 <= right-1:
                return self.binarySearchMin(left+1,right-1,nums,True)
            else :
                return left
        else:
            mid = int((left + right) /2 )
            left_min = self.binarySearchMin(left,mid,nums,False)
            right_min = self.binarySearchMin(mid+1,right,nums,False)
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

nums = [1,2,2,2,0,1,1]
obj = Solution()
print obj.search(nums,0)
