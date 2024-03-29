#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 83.py
# @Author: guolei
# @Time  : 15/07/2019 3:12 PM
# @Desc  :
# @Ans   :
# Definition for singly-linked list.
# class ListNode(object):
#      def __init__(self, x):
#          self.val = x
#          self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current  = head
        while current != None and current.next != None :
            if(current.next.val == current.val) :
                current.next = current.next.next
            else :
                current = current.next
        return head