#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 63.py
# @Author: guolei
# @Time  : 03/05/2019 12:53 AM
# @Desc  :不同路径2
# @Ans   :很显然，动态规划求解。跟1不同的是，如果是当前位置为1，则走到该位置的方式有0
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]* n for _ in range(m)]
        flag_a = flag_b = 0
        #注意初试化方式
        for a in range(m):
            if obstacleGrid[a][0] == 1:
                flag_a = 1
            if flag_a == 1:
                dp[a][0] = 0
            else:
                dp[a][0] = 1
        for b in range(n):
            if(obstacleGrid[0][b]) == 1 :
                flag_b = 1
            if flag_b == 1:
                dp[0][b] = 0
            else:
                dp[0][b] = 1

        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

obstacleGird = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
obj = Solution()
print obj.uniquePathsWithObstacles(obstacleGird)




