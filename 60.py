#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 60.py
# @Author: guolei
# @Time  : 02/05/2019 10:53 PM
# @Desc  :第k个排列
# @Ans   :根据数学逻辑，第1位，有(n-1)!个数，第二位有(n-2)!个数
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums =[]
        factorial = [1]
        fact = 1
        for i in range(1,n+1):
            nums.append(i)
            fact *= i
            factorial.append(fact)
        res = []
        k -= 1
        for i in range(n-1,-1,-1):
            index = k // factorial[i]
            res.append(str(nums.pop(index)))
            k -= index * factorial[i]
        return ''.join(res)


n ,k = 3,3
obj = Solution()
print obj.getPermutation(n,k)