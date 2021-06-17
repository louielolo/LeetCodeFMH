"""
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
示例 1：

输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2：

输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""
class Solution:
    def __init__(self):
        self.maxnum = 0
    def longestSubstring(self,string:str,k:int) -> str:
        if string is None or len(string)==0:
            return self.maxnum
        if len(string)==1:
            return 1
        for i in range(len(string)):
            prestr = string[i]
            for j in range(1,len(string)):
                poststr = string[j]
                if poststr == prestr:
                    self.maxnum = max(j-i+1,self.maxnum)
                else:
                    break
        return self.maxnum
                