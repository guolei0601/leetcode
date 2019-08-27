#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 71.py
# @Author: guolei
# @Time  : 26/06/2019 4:06 PM
# @Desc  :
# @Ans   : 使用栈解决。 ..出栈 .不入栈  其他入栈

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_arr = path.split('/')

        for i in path_arr:
            if i == "..":
                if stack :
                    stack.pop()
            elif i and i != '.':
                stack.append(i)
        return '/' + '/'.join(stack)