#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 54.py
# @Author: guolei
# @Time  : 02/05/2019 9:00 PM
# @Desc  :旋转矩阵
# @Ans   :方法1；每次先读取首行，再逆时针旋转，以此执行此操作，直到为空。方法2：按照题意走，走过就给赋值0，遇到0就判断拐点，注意该方法判断下一步的巧妙方式
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r,i,j,di,dj = [],0,0,0,1
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = 0
                if matrix[(i+di) %len(matrix)][ (j+ dj) % len(matrix[0])] == 0:
                    di,dj = dj,-di
                i += di
                j += dj
        return r

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
obj = Solution()
print obj.spiralOrder(matrix)