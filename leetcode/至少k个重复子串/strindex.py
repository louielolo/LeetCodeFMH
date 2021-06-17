class Solution:
    def strindex(self,str1: str,str2: str) -> list:
        """查找目标字符在字符串中的索引"""
        if str1 and str2 is None:
            return
        str1_len = len(str1)
        str2_len = len(str2)
        index_list = []
        i = 0
        while str2 in str1[i:]:
            ind = str1.index(str2,i,str1_len)
            index_list.append(ind)
            i = ind + str2_len
        return index_list
    

if __name__ == '__main__':
    s = Solution()
                