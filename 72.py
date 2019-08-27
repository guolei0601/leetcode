#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 72.py
# @Author: guolei
# @Time  : 03/05/2019 8:55 AM
# @Desc  :编辑距离
# @Ans   :动态规划 dp[i][j] 表示第一个word 从位置i到第二个word2 j处的最短步数。insert f(i,j) = f(i,j-1) +1 ，replace f(i,j) = f(i-1,j-1) + , remove  f(i,j) = f(i-1,j) + 1
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [[0]* (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for a in range(1,m+1):
            for b in range(1,n+1):
                if word1[a-1] == word2[b-1]: #如果当前要比较的两个位置的字符相同
                    dp[a][b] = dp[a-1][b-1]
                else:
                    dp[a][b] = min (dp[a][b-1],dp[a-1][b-1],dp[a-1][b]) + 1
        return dp[m][n]


word1 = ""
word2 = "b"

obj = Solution()
print obj.minDistance(word1,word2)
