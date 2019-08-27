#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 48.py
# @Author: guolei
# @Time  : 02/05/2019 11:27 AM
# @Desc  :图像旋转
# @Ans   :先以对角线旋转，再以水平中线旋转
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(length-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[length-1-j][length-1-i]
                matrix[length - 1 - j][length - 1 - i] = temp
                #matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #print matrix
        for i in range(length //2):
            for j in range(length):
                matrix[i][j],matrix[length-1-i][j] = matrix[length-1-i][j], matrix[i][j]
        #print  matrix


obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj.rotate(matrix)

