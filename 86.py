#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 86.py
# @Author: guolei
# @Time  : 16/07/2019 6:07 PM
# @Desc  :
# @Ans   :创建两个链表，分别是小于x链表和大于x链表，遍历完把小于x的链表的尾指针指向大于x链表的头指针，核心点 创建哑指针
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small =  s  = ListNode(-1)
        big = b = ListNode(-1)
        while head :
            if(head.val < x) :
                s.next = ListNode(head.val)
                s = s.next
            else :
                b.next = ListNode(head.val)
                b = b.next
            head = head.next
        s.next = big.next
        return small.next