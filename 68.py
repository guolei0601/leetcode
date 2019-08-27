#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : 68.py
# @Author: guolei
# @Time  : 02/05/2019 6:41 PM
# @Desc  :文本左右对齐
# @Ans   :该题没用到任何算法，只需要把边界考虑清楚即可
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return list()
        res ,row = list(),list()
        words_len, cur_total = len(words),0
        i = 0
        while i < words_len:
            if len(words[i]) + cur_total <= maxWidth:
                cur_total += len(words[i]) + 1 #此处加1，表示加1个空格
                row.append(words[i])
                i += 1
                continue
            #该分配字符串了，注意该循环中的字符串都表示不是最后一次
            if len(row) == 1:
                res.append(str(row[0]) + ' '*(maxWidth-len(row[0])))
            else :
                extra_space = maxWidth - cur_total + len(row)
                num_space   = extra_space // (len(row) -1)
                pre_space   = extra_space % (len(row) -1)
                temp = ''
                for cur_str in row[:-1]:#注意此时只需要遍历到倒数第一个，最后一个直接放末尾
                    if pre_space > 0:
                        temp += str(cur_str) + ' '*(num_space +1)#把多于的空格分出去
                        pre_space -= 1
                    else:#分完空格了
                        temp += str(cur_str) + ' ' * num_space
                temp += str(row[-1])
                res.append(temp)
            cur_total = 0
            row = list()
        #对最后一个list进行处理，就是处理最后一行
        tmp = ' '.join(row)
        res.append(tmp + ' '*(maxWidth - len(tmp)))
        return res
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
obj = Solution()
print obj.fullJustify(words,maxWidth)