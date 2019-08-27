#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 84.py
# @Author: guolei
# @Time  : 03/05/2019 1:09 PM
# @Desc  :柱状图中的最大矩形
# @Ans   : 第 i 到 j 的面积等于 min(heights[i],heights[j]) * (j - i +1) ，暴力求解超时了，泪牛满面~
# @Ans   :单调增栈解决。碰到比如果栈顶  > 当前值 ，则计算当前所有最大的面积。仔细观察可知道，计算了包含所有柱子的最大面积。

class Solution(object):
    def largestRectangleArea(self,heights):
        heights.append(0) #注意因为碰到小的才会计算前面的面积，所以在后面加一个0
        length = len(heights)
        res = 0
        cur_stack = []
        for i in range(length):
            while len(cur_stack) > 0 and heights[i] < heights[cur_stack[-1]] :
                top = cur_stack.pop()
                res = max(res,heights[top] * (i if len(cur_stack) == 0 else (i-cur_stack[-1] -1)))
            cur_stack.append(i)
        return res

    def largestRectangleArea_1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        length = len(heights)
        for i in range(length) :
            cur_min = heights[i]
            for j in range(i,length):
                cur_min = min(cur_min,heights[j])
                res = max(res,(j-i+1)* cur_min)
        return res

obj = Solution()
heights = [2,1,5,6,2,3]
print obj.largestRectangleArea(heights)
