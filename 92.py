#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 92.py
# @Author: guolei
# @Time  : 20/07/2019 2:19 PM
# @Desc  :
# @Ans   :此题的关键是利用回溯模拟指针向左移动。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        l = r = head
        stop = False
        def huisu(l,r,m,n,stop):
            if n == 1:
                return
            r = r.next
            if m > 1:
                l = l.next
            huisu(l,r,m-1,n-1,stop)
            if l == r or r.next == l :
                stop = True
            if not stop:
                l.val ,r.val = r.val,l.val
                l = l.next
        huisu(l,r,m,n,stop)
        return head