#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 32.py
# @Author: guolei
# @Time  : 2019/4/30 上午11:27
# @Desc  :LeetCode 32 最长有效括号长度
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = []
        total = len(s)
        start = 0
        for i in range(total):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 0:
                    start = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        max_len = max(i-start+1,max_len)
                    else:
                        max_len = max(i-stack[-1],max_len)
        return max_len

obj = Solution()
str = ")()()"
print obj.longestValidParentheses(str)