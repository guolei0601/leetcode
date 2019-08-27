#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 44.py
# @Author: guolei
# @Time  : 02/05/2019 1:01 AM
# @Desc  :通配符匹配
# @Ans   :动态规划解决
class Solution(object):
    def isMatch(self, s, p) :
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        """
        #dp[i+1][j+1] 表示 s(0~i) 是否匹配 p(0~j)
        m,n = len(s),len(p)
        dp =[[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(n):
            if p[j] == '*' and dp[0][j]:
                dp[0][j+1] = True #当s为空时，第j个字符为*，并且前一个匹配的情况下，才为True
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif (p[j] == '*'):
                    dp[i+1][j+1] = dp[i][j] or dp[i+1][j] or dp[i][j+1]
        return dp[m][n]

s = "abc"
p = "*"
obj = Solution()
print obj.isMatch(s,p)