#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 145.py
# @Author: guolei
# @Time  : 21/07/2019 5:15 PM
# @Desc  :二叉树的后续遍历
# @Ans   :
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if not root :
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res
#逆向思维，先 右 、中、左 输出，然后对结果求逆
    def postorderTraversal(self, root):
        res = []
        if not root :
            return res
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
            res.append(tmp.val)
        return res[::-1]
