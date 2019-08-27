#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 121.py
# @Author: guolei
# @Time  : 03/05/2019 3:19 PM
# @Desc  :买卖股票的最佳时机
# @Ans   :动态规划解决
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        min_stock = 9999999
        for i in range(len(prices)):
            min_stock = min (min_stock,prices[i])
            res = max (res,prices[i] - min_stock)
        return res