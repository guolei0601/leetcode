#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 38.py
# @Author: guolei
# @Time  : 01/05/2019 4:12 PM
# @Desc  : 报数
# @Ans   : 从1开始遍历一遍即可

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        #cur_char = res[0]
        for i in range(n-1):
            count = 0
            cur_res  = ""
            cur_char = res[0]
            for char in res:
                if char == cur_char :
                    count += 1
                else:
                    cur_res += str(count) + str(cur_char)
                    count = 1
                    cur_char = char
            #把最后一次的加上
            cur_res += str(count) + str(cur_char)
            res = cur_res
        return res
n = 4
obj = Solution()
print obj.countAndSay(n)


