#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 77.py
# @Author: guolei
# @Time  : 26/06/2019 9:07 PM
# @Desc  :
# @Ans   :回溯法
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def f(start,current):
            if len(current) == k :
                res.append(current[:])
            for i in range(start,n+1):
                current.append(i)
                f(i+1,current)
                #注意此处删除栈顶元素，是为了新的元素进入（另外一种可能）
                current.pop()
        f(1,[])
        return res

obj = Solution()
print obj.combine(4,2)

