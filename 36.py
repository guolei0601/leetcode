#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 36.py
# @Author: guolei
# @Time  : 01/05/2019 12:11 PM
# @Desc  :有效的数独，注意该题容易阐述误区：有效的数独不一定是可解的。该题只用判断是否有效即可，可不可解不用关心。
# @Ans   :分别创建3个列表，存储行、列、3*3的值，针对每一个数进行判断行、列 3*3表中是否有这个数，有则失败，没则继续,注意第 x,y个数对应的行列，小表 分别是 x,y， 3 * （x //3） + y //3
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row , col , cell = [{}, {}, {}, {}, {}, {}, {}, {}, {}],[{}, {}, {}, {}, {}, {}, {}, {}, {}],[{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for i in range(9):
            for j in range(9):
                num = 3 * (i//3) + (j//3)
                char = board[i][j]
                if char != '.':
                    if char not in row[i].keys() and char not in col[j].keys() and char not in cell[num].keys():
                        row[i][char] = 'x'
                        col[j][char] = 'x'
                        cell[num][char] = 'x'
                    else:
                        return False
        return True

# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

board = [
         ["1","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]
         ]

obj = Solution()
print obj.isValidSudoku(board)