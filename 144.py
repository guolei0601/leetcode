#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 144.py
# @Author: guolei
# @Time  : 21/07/2019 4:39 PM
# @Desc  :二叉树的前序遍历
# @Ans   :
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if not root :
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res

    #使用栈 进行迭代 前序遍历，注意入栈时，先入右节点（输出的时候左节点先出栈）
    def preorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack :
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res