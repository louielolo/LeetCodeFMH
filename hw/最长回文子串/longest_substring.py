"""
描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
（注意：记得加上while处理多个测试用例）

输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度

示例1
输入：
cdabbacc
复制
输出：
4
复制
说明：
abba为最长的回文子串 
"""
import sys
class Solution:
    def __init__(self):
        self.count = 0
        self.substring = []
        self.length_output = 0
    def substring_scan(self,string,left,right):
        l = left
        r = right
        is_circle = 0
        while l>=0 and r<len(string):
            if string[l]==string[r] :
                if l!=r:
                    is_circle = 1
                l -= 1
                r += 1
            else:
                return l,r,(r-l-1)*is_circle
        return l,r,(r-l-1)*is_circle
    def longest_substring(self,string):
        length_output = 0
        if len(string)<2:
            return 0
        for i in range(0,len(string)):
            [l1,r1,length1] = self.substring_scan(string,i,i)
            [l2,r2,length2] = self.substring_scan(string,i,i+1)
            length_output = max(length1,length2,length_output)
        if length_output > 1:
            return length_output
        else:
            return 0
if __name__ == '__main__':
    getline = lambda :sys.stdin.readline().strip()
    line = getline()
    s = Solution()
    while line:
        print(s.longest_substring(line))
        line = getline()
