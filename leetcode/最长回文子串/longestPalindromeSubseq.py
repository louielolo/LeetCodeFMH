class Solution:
    def __init__(self):
        self.maxlength = 0
    
    def traverse(self,s: str,left: int,right: int)->int:
        for 
    def longestPalindromeSubseq(self,s: str):
        for i in range(len(str)):
            len1 = self.traverse(s,i,i)
            len2 = self.traverse(s,i,i+1)
            return max(len1,len2)
