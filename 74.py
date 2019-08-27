#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 74.py
# @Author: guolei
# @Time  : 15/07/2019 9:47 AM
# @Desc  :
# @Ans   :二分查找。把该m*n的矩阵看成个长度为m*n虚拟数组，其中第k个元素对应的行是 k // n ，对应的列是 k % n
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0 :
            return False
        n = len(matrix[0])
        left =  0
        right = m * n - 1

        while left <= right :
            mid = (left + right) // 2
            if matrix[mid // n][mid % n ] == target :
                return True
            elif matrix[mid // n][mid % n ] > target :
                right = mid - 1
            else :
                left  = mid + 1
        return False

obj = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
print obj.searchMatrix(matrix,target)
