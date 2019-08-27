#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 79.py
# @Author: guolei
# @Time  : 02/07/2019 3:24 PM
# @Desc  :
# @Ans   :回溯法，深度优先搜索
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        mark =   [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        #print mark
        for j in range(len(board)):
            for k in range(len(board[0])):
                if self.checkCurWord(j,k,board,word,mark,0):
                    return True
        return False

    def checkCurWord(self,m,n,board,word,mark,cur_num):
        if cur_num == len(word) -1:
            return board[m][n] == word[cur_num]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        if board[m][n] == word[cur_num]:
            mark[m][n] = True
            for direction in directions:
                m_new = m + direction[0]
                n_new = n + direction[1]
                #print m_new,n_new,len(board),len(board[0]),mark[m_new][n_new]
                if 0<=m_new<len(board) and 0<=n_new<len(board[0]) and not mark[m_new][n_new] \
                        and self.checkCurWord(m_new,n_new,board,word,mark,cur_num+1):
                    return True
            mark[m][n] = False
        return False

obj = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print obj.exist(board,word)