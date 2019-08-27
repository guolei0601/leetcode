#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 51.py
# @Author: guolei
# @Time  : 02/05/2019 3:20 PM
# @Desc  :N皇后问题
# @Ans   :回溯算法,重复的条件需要再想想
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(row):
            if row == n :
                self.res.append(record_res[:])
                #print record_res
                return
            for column in range(n):
                judge = 0
                for i in range(row):
                    if record_res[i] == column or abs(record_res[i] - column) == abs(i-row):
                        judge = 1
                        break
                if judge == 0 :
                    record_res[row] = column
                    DFS(row + 1)
        self.res = []
        record_res = [-1 for _ in xrange(n)] #其中，key对应行数，value对应列
        DFS(0)
        new_res = []
        for cur_list in self.res:
            one = []
            for row in range(n):
                one_str = ""
                col = cur_list[row]
                for j in range(n):
                    if(j != col):
                        one_str +='.'
                    else :
                        one_str += 'Q'
                one.append(one_str)
            new_res.append(one[:])

        return new_res

n = 4
obj = Solution()
print obj.solveNQueens(n)
