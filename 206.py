#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 206.py
# @Author: guolei
# @Time  : 20/07/2019 2:59 PM
# @Desc  :反转链表
# @Ans   :迭代法，创建一个节点存储下一个位置
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre