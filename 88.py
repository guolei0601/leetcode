#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 88.py
# @Author: guolei
# @Time  : 16/07/2019 6:47 PM
# @Desc  :
# @Ans   :采用双指针法，从后往前排序，时间复杂度 m + n ，空间复杂度 O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        point_a = m - 1
        point_b = n - 1
        now_loc = m + n - 1
        while point_a >= 0 and point_b >= 0 :
            if(nums1[point_a] > nums2[point_b]) :
                nums1[now_loc] = nums1[point_a]
                point_a -= 1
            else :
                nums1[now_loc] = nums2[point_b]
                point_b -= 1
            now_loc -= 1
        if point_a < 0 :
            while point_b >= 0:
                nums1[now_loc] = nums2[point_b]
                point_b -= 1
                now_loc -= 1

        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

obj = Solution()
print obj.merge(nums1,m,nums2,n)