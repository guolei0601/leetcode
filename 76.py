#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 76.py
# @Author: guolei
# @Time  : 03/05/2019 9:58 AM
# @Desc  :最小覆盖子串
# @Ans   :
#思路：滑动窗口 + 字符计数 ，其中需要创建 长度为'z' - 'A' 的list，分别表示 key + 'a' 的个数。每次动态滑动窗口，动态更新 这个list。如果list包含目标所有字符，则 左窗口右移，否则，右窗口右移动
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s,len_t = len(s),len(t)
        if len_s < len_t : return ""
        res_fre = [0  for _ in range(58)]#'A' ~ 'z' 共 58 个字符
        cur_fre = [0  for _ in range(58)] #cur_fre当前正遍历的seq ，res_fre 值 t映射出来的 seq，其值一直不变。
        for i in range(len_t): res_fre[ord(t[i]) - ord('A')] += 1
        l,r = 0 ,0
        res_edge = [-1,len_s +1] #注意初始化左右边界需要在正常范围之外
        while(l <= len_s - len_t): #最小窗口下循环
            if r - l < len_t:
                if r < len_s :
                    cur_fre[ord(s[r]) - ord('A') ] += 1
                    r += 1
                else :
                    break
            i = 0
            for i in range(58) : #'A' ~ 'z' 共 58 个字符
                if cur_fre[i] < res_fre[i] : #表示当前的窗口跟结果不一致,注意最后一步不管比不比都会退出循环
                    break
            if i <= 57  and cur_fre[i] < res_fre[i]: #当前的窗口跟结果不一致的时候，右窗口需要移动1
                if r < len_s:
                    cur_fre[ord(s[r]) - ord('A')] += 1
                    r = r + 1
                else :
                    break
            else : #表示当前窗口 跟结果一致，此时需要更新res_edge，并且左指针右移(如果长度刚好等于len_t，则直接返回)
                if l == 603 :
                    print 0
                if r - l == len_t :
                    return s[l:r]
                else :
                    if r - l < res_edge[1] - res_edge[0]:
                        res_edge = [l,r]
                    cur_fre[ord(s[l]) - ord('A')] -= 1
                    l += 1
        return  "" if res_edge[0] == -1 else s[res_edge[0]:res_edge[1]]

S = "wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon"
T = "ozgzyywxvtublcl"
obj = Solution()
print  obj.minWindow(S,T)