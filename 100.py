#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 100.py
# @Author: guolei
# @Time  : 21/07/2019 5:56 PM
# @Desc  :相同的数
# @Ans   :递归实现，中序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isEqual(p,q):
            if not p and not q :
                return True
            if not p or not q:
                return False
            if p.val != q.val :
                return False
            return isEqual(p.left,q.left) and isEqual(p.right,q.right)
        return isEqual(p,q)