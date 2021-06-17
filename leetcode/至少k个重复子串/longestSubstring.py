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
import collections
class Solution:
    def __init__(self):
        self.count = collections.Counter
        self.max_length = 0

    def longestSubstring(self,s: list,k: int) -> int:
        if s is None or len(s) < 1 or max(list(self.count(s).values()))<k:
            return 0
        if len(s)==1 and k==1:
            return 1
        for i in range(len(s)):
            if len(s)>1:
                for j in range(i+1,len(s)+1):
                    if min(list(self.count(s[i:j]).values()))>=k:
                        self.max_length = max(j-i,self.max_length)
        return self.max_length

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring('aaabb',3))