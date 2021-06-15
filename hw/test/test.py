import sys

class Solution:
    def __init__(self):
        pass
    def is_maxlen_dictsorted(self,pool:list,character:str) -> str:
        if pool is None or len(pool) < 1:
            return
        else:
            pool_bychar = []
            for i in range(len(pool)):
                if pool[i][0]==character:
                    pool_bychar.append(pool[i])
            """找到列表中最长的接龙单词,相同时字典序最小"""
            #先按长度排序后，识别相同字符长度的个数，index为count-1为接龙的单词
            if len(pool_bychar)>1:
                pool_bylen = sorted(pool_bychar,reverse=True)
                len_list = [len(elem) for elem in pool_bylen]
                if len(pool_bylen)>1:
                    next_word_index = len_list.count(len(pool_bylen[0]))-1
                    return pool_bylen[next_word_index]
                #如果按长度排序后，首位单词长于其他单词，返回第一个
                else:
                    return pool_bylen[0]
            return None
    def jielong(self,pool:list,start:str) -> str:
        jielong = start
        """成语接龙"""
        for i in range(len(pool)):
            #循环迭代上一个和下一个单词
            character = start[-1]
            pool.remove(start)
            next_word = self.is_maxlen_dictsorted(pool, character)
            if next_word is not None:
                jielong = jielong+next_word[1:]
                start = next_word
            else:
                return jielong
            #再也找不到下一个时跳出循环
        return jielong
        
if __name__ == '__main__':
    getline = lambda :sys.stdin.readline().strip()
    start_index = getline()
    wordnum = getline()
    wordpool = [getline() for i in range(int(wordnum))]
    start = wordpool[int(start_index)]
    s = Solution()
    print(s.jielong(wordpool,start))