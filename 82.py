#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 82.py
# @Author: guolei
# @Time  : 15/07/2019 10:12 PM
# @Desc  :
# @Ans   :创建两个指针，分别是之前指针和当前指针。如果前指针和 当前指针不等 且当前指针和下一个指针不等，则该数据不重复
# Definition for singly-linked list.
class ListNode(object):
      def __init__(self, x):
          self.val = x
          self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = t = pre = None
        cur = head
        while head :
            if self.checkEqual(pre,cur) and self.checkEqual(cur,cur.next):
                if new_head == None :
                    new_head = ListNode(head.val)
                    t = new_head
                else :
                    t.next = ListNode(head.val)
                    t = t.next
            pre = head
            cur = head = head.next
        return new_head

    def checkEqual(self,A,B):
        if A == None or B == None or A.val != B.val:
            return True
        return False