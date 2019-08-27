#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 73.py
# @Author: guolei
# @Time  : 26/06/2019 4:49 PM
# @Desc  :
# @Ans   :先遍历一遍矩阵，用首行和首列存储第i行和第j列是否要变0.如果a[i][j] = 0 则 给 a[i][0] 和 a[0][j]赋0 ，注意a[0][0]必须只标志一行或一列，需要另外一个标志位
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R) :
            #注意此处遍历第一列数据，如果把该语句写到下一层循环会浪费很多时间
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        #注意此时应该先遍历内层的进行赋值
        for i in range(1,R):
            for j in range(1,C):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
        #注意此时先遍历行，再遍历列
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        if is_col == True :
            for i in range(R):
                matrix[i][0] = 0


