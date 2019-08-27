#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 42.py
# @Author: guolei
# @Time  : 01/05/2019 9:16 PM
# @Desc  : 接雨水
# @Ans   :思路，先找到最高挡板，然后从左向最高逼近，以及从右边向最高逼近，过程中计算面积，样不用担心最高挡板不存在的问题。每次只需要找到更高的挡板，
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int        """
        area = 0
        highest = 0
        for i in range(len(height)):
            if height[i] > height[highest] :
                highest = i
        #从左开始遍历，找到0到highest的面积：
        cur_high = 0
        for i in range(highest):
            if height[i] > cur_high :
                cur_high = height[i]
            else :
                area += cur_high - height[i]
        #从右开始遍历，找到lengh -1 到 highest面积：
        cur_high = 0
        for j in range(len(height)-1,highest,-1) :
            if cur_high < height[j] :
                cur_high = height[j]
            else :
                area += cur_high - height[j]
        return area
obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print obj.trap(height)
