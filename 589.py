#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 589.py
# @Author: guolei
# @Time  : 21/07/2019 5:40 PM
# @Desc  : N叉数的前序遍历
# @Ans   :
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for cur in root.children:
                root = cur
                helper(root)
        helper(root)
        return res