#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 62.py
# @Author: guolei
# @Time  : 03/05/2019 12:23 AM
# @Desc  :不同路径
# @Ans   :很显然，动态规划很容易实现.注意给每个靠墙的赋值1.因为仅有一种走法，另外注意m行n列的数组创建方式
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for i in range(m)]
        for a in range(m):
            dp[a][0] = 1
        for b in range(n):
            dp[0][b] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

m,n = 7,3
obj = Solution()
print obj.uniquePaths(m,n)