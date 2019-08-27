#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 53.py
# @Author: guolei
# @Time  : 02/05/2019 8:39 PM
# @Desc  : 最大自序和
# @Ans   : 动态规划，dp[i] = max(dp[i-1] + nums[i],nums[i])
import collections
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(list)
        res = dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i],nums[i])
            res   = max (res,dp[i])
        return res