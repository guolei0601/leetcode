#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 59.py
# @Author: guolei
# @Time  : 02/05/2019 9:35 PM
# @Desc  :旋转矩阵2
# @Ans   :跟54题类似，只要找到拐点，然后赋值
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]
        print res
        i,j,di,dj = 0,0,0,1
        for m in range(1,n * n+1):
            res[i][j] = m
            if  res[(i + di) % n ][(j+dj) % n] > 0:
                di,dj = dj,-di
            i += di
            j += dj
        return res

n =3
obj = Solution()
print obj.generateMatrix(3)