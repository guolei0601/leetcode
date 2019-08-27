#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 56.py
# @Author: guolei
# @Time  : 02/05/2019 9:50 PM
# @Desc  :合并区间
# @Ans   :思路 先对list进行sort，然后动态更新结果集最后一个元素
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals : return []
        intervals = sorted(intervals)
        res = list()
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0],max(res[-1][1],intervals[i][1])]
            else :
                res.append(intervals[i])
        return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
obj = Solution()
print obj.merge(intervals)