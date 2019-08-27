#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 93.py
# @Author: guolei
# @Time  : 21/07/2019 10:09 AM
# @Desc  :复原ip地址
# @Ans   :1、暴力求解 2、回溯法。 每三位数满足 1、首数字不能为0，除非是0 2、数字不能大于255。
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        output,segments = [],[]
        def valid (segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        #如果最后的位置验证通过就加入到outpu里
        def update_output(cur_pos):
            segment = s[cur_pos+1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def DFS(prev_pos = -1 ,dots = 3):
            for curr_pos in range(prev_pos + 1, min(n-1,prev_pos + 4)):
                segment = s[prev_pos+1:curr_pos+1]
                if valid(segment):
                    segments.append(segment)
                    if dots -1 == 0:
                        update_output(curr_pos)
                    else:
                        DFS(curr_pos,dots-1)
                    segments.pop()

        DFS()
        return output
