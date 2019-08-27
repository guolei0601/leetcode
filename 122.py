#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 122.py
# @Author: guolei
# @Time  : 03/05/2019 3:32 PM
# @Desc  :买卖股票2
# @Ans   :注意，这跟美股的性质。当天买入，也可卖出。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for day in range(len(prices) -1 ):
            profit += (0 if prices[day] > prices[day+1] else prices[day+1] - prices[day])
        return profit
