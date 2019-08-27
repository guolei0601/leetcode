#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 52.py
# @Author: guolei
# @Time  : 02/05/2019 3:42 PM
# @Desc  :
# @Ans   :
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(row):
            if row == n :
                self.res += 1
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
        self.res = 0
        record_res = [-1 for _ in xrange(n)] #其中，key对应行数，value对应列
        #column = 0
        DFS(0)
        return self.res

n = 4
obj = Solution()
print obj.totalNQueens(n)