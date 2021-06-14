import sys
class Solution:
    pass

if __name__ == '__main__':
    getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
    line = getline()
    s = Solution()
    while line:
        print(s.comove(line))
        s = [int(elem) for elem in line.split()] #去掉空格输入
        line = getline()