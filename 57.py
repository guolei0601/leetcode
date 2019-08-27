#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 57.py
# @Author: guolei
# @Time  : 02/05/2019 4:09 PM
# @Desc  :插入区间
# @Ans   :创建左指针和右指针，问题转化为找到这俩指针
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        start = newInterval[0]
        end   = newInterval[1]
        new_start = new_end = ""
        for i in range(len(intervals)):
            index_left = intervals[i][0]
            index_right = intervals[i][1]
            if start <= index_left or start <= index_right:  #找到了左指针的位置，此时只要找到右指针即可
                new_start = min(start, index_left)
                for j in range(i,len(intervals)):
                    if end < intervals[j][0] and new_end =="":
                        new_end = end
                        res_list.append([new_start,new_end])
                    else:
                        end = max(intervals[j][1],end)
                    if new_end != "": #表示找到了，后面的直接往里面添加就行了
                        res_list.append(intervals[j][:])
                if (new_end == ""):#找到最后都未找到，则添加
                    res_list.append([new_start,end])
                break
            else:#继续找左指针
                res_list.append(intervals[i][:])
        if (new_start == ""):#找到最后都没找到左指针，则加入到队列里面
            res_list.append(newInterval[:])
        return res_list
intervals = [[2,5],[6,7],[8,9]]
newInterval = [0,1]
obj = Solution()
print obj.insert(intervals,newInterval)