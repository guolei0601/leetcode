#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 89.py
# @Author: guolei
# @Time  : 16/07/2019 7:28 PM
# @Desc  :
# @Ans   :参考提示 镜像反射法 二进制数左边加1 = 二进制的位数左移 1 。采用动态规划法，以此算出所有值
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            h = 1 << i
            for j in range(len(res) -1 ,-1,-1):
                res.append(h + res[j])
        return res
obj = Solution()
print obj.grayCode(2)