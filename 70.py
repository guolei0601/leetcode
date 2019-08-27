#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 70.py
# @Author: guolei
# @Time  : 02/05/2019 7:10 PM
# @Desc  :爬楼梯
# @Ans   :DFS，深度优先搜索,超时了竟然……，用动态规划，res[i] = res[i-1] + res[i-2]，表示最后一次是在前一个台阶跳一步（1台阶） ，或者 前两个台阶跳一步（2台阶）
import collections
class Solution(object):
    def climbStairs(self,n):
        res = collections.defaultdict(list)
        res[0] = 1
        res[1] = 1
        for i in range(2,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

    def climbStairs_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        cur_location = 0
        self.DFS(n,0)
        return self.res
    def DFS(self,n,cur_location):
        if cur_location + 1 == n or cur_location == n:#剩下1个台阶，只有1种可能，跳1步
            self.res += 1
            return
        for i in range(1,3):
            self.DFS(n,cur_location + i)

n = 0
obj = Solution()
print obj.climbStairs(n)