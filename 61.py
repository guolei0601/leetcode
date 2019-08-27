#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 61.py
# @Author: guolei
# @Time  : 02/05/2019 11:44 PM
# @Desc  : 旋转链表
# @Ans   :
#Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        res_list = []
        length = 0
        real_move = 0
        res = res_cur =ListNode(0)
        while cur is not None :
            length += 1
            res_list.append(cur.val)
            cur = cur.next
        real_move =  k % length
        if real_move == 0:
            return head
        else:
            new_list = res_list[length-real_move:] + res_list[:length-real_move]#得到最新的顺序，此时只需要把该list转换成对应的链表即可
            for num in new_list:
                res_cur.next = ListNode(num)
                res_cur = res_cur.next
            return res.next



