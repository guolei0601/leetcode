#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 31.py
# @Author: guolei
# @Time  : 2019/4/25 上午11:22
# @Desc  :该题没看懂题意，看了评论才解出来，先找到 nums[i-1] < nums[i]，找不到则不存在更大的，找到则再从i处查比nums[i]大且最小的数a[j]，交换a[i],a[j]，再把i处到最后数据交换位置即为更大排列
class Solution(object):
    def nextPermutation(self,  nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = total = len(nums) -1
        if i == 0 : return nums
        while i >= 1 :
            if nums[i] > nums[i-1] :
                break
            else :
                i -= 1

        #找到了i的位置，如果i=1，说明是倒叙排列，不存在更大一个
        if i== 0:
            nums.reverse()
        else :
            #找到i，并且i>1，说明有更大列表，此时需要找到j
            j = i
            while j <= total :
                if nums[j] > nums[i-1] :
                    j += 1
                else :
                    break
            nums[i-1],nums[j-1] = nums[j-1],nums[i-1]
            sub_nums = nums[i:]
            sub_nums.reverse()
            nums[i:] = sub_nums

obj =  Solution()
nums = [1,5,1]
obj.nextPermutation(nums)
#nums[1:].reverse()
for i in  nums :
    print i