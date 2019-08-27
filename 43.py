#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 43.py
# @Author: guolei
# @Time  : 01/05/2019 10:46 PM
# @Desc  :字符串相乘
# @Ans   :思路是跟手写乘法类似，假设两乘数的长度分别为m,n，则乘完会有n个数，n个数再相加（中间需要补零操作），结果很糟糕，领先5%
# @Ans   :利用 长度m * 长度n = m+n or m+n -1 特性。及第i，j的位置相乘，保存在位置i+i+1，以及每次相加最多有一个进位。领先30%
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        add = 0
        res_list = []
        for i in range(len(num1) + len(num2)):
            res_list.append(0)
        for i in range(len(num1)-1,-1,-1):
            cur_res = ""
            for j in range(len(num2)-1,-1,-1):
                a = int(num1[i])
                b = int(num2[j])
                cur_multi = a * b + add + res_list[i+j+1]
                cur_num = cur_multi % 10
                add  = cur_multi // 10
                res_list[i+j+1] = cur_num
                res_list[i+j] += add
                add = 0
        if res_list[0] == 0:
            res_list = res_list[1:]
        res = ""
        for m in res_list:
            res += str(m)
        return res
        #res = ''.join(res_list)
        #return res if res[0] =='0' else res[1:]

        #对res_list中的n个数进行求和,注意str2的长度大于等于str1
    # def add_two_str(self,str1,str2):
    #     if str1 == "":
    #         return str2
    #     else:
    #         len_2 = len(str2)
    #         len_1 = len(str1)
    #         #补齐
    #         for m in range(len_2 - len_1):
    #             str1 = "0" + str1
    #         add = 0
    #         res = ""
    #         for m in range(len_2-1,-1,-1):
    #           a = int(str1[m])
    #           b = int(str2[m])
    #           cur_sum = a + b + add
    #           add = cur_sum // 10
    #           cur_num = cur_sum % 10
    #           res = str(cur_num) + res
    #         if add > 0 :
    #             res = str(add) + res
    #         return res
obj = Solution()
num1 = "999"
num2 = "999"
print obj.multiply(num1,num2)

