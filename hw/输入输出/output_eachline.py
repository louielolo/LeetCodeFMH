import sys

if __name__ == '__main__':
    getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
    line = getline()
    while line:
        print(line) #在forloop或while循环中，处理一个输出一个
        line = getline()