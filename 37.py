#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 37.py
# @Author: guolei
# @Time  : 01/05/2019 1:26 PM
# @Desc  :解数独，其中给的数独只有唯一解
# @Ans 思路，每次填入一个数，然后判断填入一个数后是否是有效数独。注意判断数据是否有效时，是在已经有效的基础上判断加入一个新字符是否有效。跟36题的有效不一样，按照36题处理方式会超时。
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1,10):
                        #注意此处先判断是否有效再更改值
                        res = self.checkSudo(board,i,j,str(k))
                        if res == False :
                            continue
                        board[i][j] = str(k)
                        if self.solveSudoku(board) == True :
                           # print board
                            return True
                        else :
                            board[i][j] = '.'
                    return False
        return True

    # def checkSudo(self,board):
    #     row, col, cell = [{}, {}, {}, {}, {}, {}, {}, {}, {}],\
    #                      [{}, {}, {}, {}, {}, {}, {}, {}, {}], \
    #                      [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    #     for i in range(9):
    #         for j in range(9):
    #             num = 3 * (i // 3) + (j // 3)
    #             char = board[i][j]
    #             if char != '.':
    #                 if char not in row[i] and char not in col[j] and char not in cell[num]:
    #                     row[i][char] = 'x'
    #                     col[j][char] = 'x'
    #                     cell[num][char] = 'x'
    #                 else:
    #                     return False
    #     return True

    def checkSudo(self,board,i,j,char):
        for m in range(9):
            if board[m][j] == char :
                return False
            if board[i][m] == char :
                return False
            #注意此处小3宫格的遍历方式
            if board[3 * (i//3) + m //3][3*(j//3) + m%3] == char:
                return False
        return True



board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]

obj = Solution()
print obj.solveSudoku(board)