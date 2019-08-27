#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 39.py
# @Author: guolei
# @Time  : 01/05/2019 6:19 PM
# @Desc  :组合总和
# @Ans   :使用DFS求解，参考网上写法
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,candidates[0])
        return self.resList

    def dfs(self,candidates,sublist,target,min_can_use):
        if target == 0:
            self.resList.append(sublist[:])
        else :
            for i in candidates :
                #因为已经拍过序了，不用再比下去了
                if i > target :
                    return
                #表示已经使用过了，不加这句话结果会重复
                if i < min_can_use:
                    continue
                sublist.append(i)
                self.dfs(candidates,sublist,target - i,i)
                #pop是因为上一次数深度优先搜索完毕，需要加入下一个数
                sublist.pop()

candidates = [2,3,6,7]
target = 7
obj = Solution()
print obj.combinationSum(candidates,7)
