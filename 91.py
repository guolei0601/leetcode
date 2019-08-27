#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 91.py
# @Author: guolei
# @Time  : 17/07/2019 10:20 AM
# @Desc  :
# @Ans   :动态规划，注意 0 这个特殊数字
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = len(s)
        res = [0 for i in range(total + 1)]
        if s[0] == "0":
            return 0
        res[0]= res[1] = 1
        for i in range(2,total+1):
            if s[i-1] == "0":
                if(int(s[i-2]) > 2 or int(s[i-2]) == 0):
                    return 0
                elif i > 2 :
                    res[i] = res[i-2]
                else :
                    res[i] = res[i - 1]
            else:
                if int(s[i-2:i]) > 26 or s[i-2] == "0":
                    res[i] = res[i-1]
                else:
                    res[i] = res[i-1] + res[i-2]
        return res[total]

obj = Solution()
s = "12123"
print obj.numDecodings(s)
