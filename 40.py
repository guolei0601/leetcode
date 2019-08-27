#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 40.py
# @Author: guolei
# @Time  : 01/05/2019 6:42 PM
# @Desc  :组合总和2
# @Ans   :这个只需要在39题基础上更改最小使用数字
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        print candidates
        self.res = []
        self.DFS(candidates,target,[],0)
        return self.res
    def DFS(self,candidates,target,cur_list,cur_index):
        if target == 0 :
            self.res.append(cur_list[:])
        else :
            if len(candidates) == 0 or candidates[0] > target :
                return
            else:
                for i in range(len(candidates)):
                    if candidates[i] > target :
                        return #后面的数都比target大，不需要再比了
                    #注意，该条件是为了避免下次查的数跟上次的一样而造成重复，同时注意i > 0 ，因为 如果当len（a） = 1时，a[-1] == a[0]，默认会跳过
                    if candidates[i-1] == candidates[i]  and i >0 :
                        continue
                    cur_list.append(candidates[i])
                    self.DFS(candidates[i+1:],target - candidates[i],cur_list,i)
                    cur_list.pop()

candidates = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5]
target = 10
obj = Solution()
print obj.combinationSum2(candidates,target)
