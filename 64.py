#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 64.py
# @Author: guolei
# @Time  : 03/05/2019 1:14 AM
# @Desc  :最小路径和
# @Ans   :很显然，怎么又是动态规划
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]* n for _ in range(m)]
        flag_a = flag_b = 0
        dp[0][0] = grid[0][0]
        #注意初试化方式
        for a in range(1,m):
            dp[a][0] = dp[a-1][0] + grid[a][0]
        for b in range(1,n):
            dp[0][b] = dp[0][b-1] + grid[0][b]

        for i in range(1,m):
            for j in range(1,n):
                    dp[i][j] = min(dp[i-1][j] , dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
obj = Solution()
print obj.minPathSum(grid)