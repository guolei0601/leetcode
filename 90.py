#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 90.py
# @Author: guolei
# @Time  : 16/07/2019 8:48 PM
# @Desc  :
# @Ans   :
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        self.getCurAns(ans,nums,0,[])
        return ans

    def getCurAns(self,ans,nums,start,cur_ans):
        #注意此处添加方式，增加一个list的写法
        ans.append(cur_ans[:])
        #print ans
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1] :
                continue
            cur_ans.append(nums[i])
            self.getCurAns(ans,nums,i+1,cur_ans)
            cur_ans.pop()

obj = Solution()
nums = [1,2,2,2,2]
print obj.subsetsWithDup(nums)