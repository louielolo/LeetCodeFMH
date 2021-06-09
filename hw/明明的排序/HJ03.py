import sys

if __name__ == '__main__':
    getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
    line = getline()
    while line:
        s = [int(getline()) for i in range(int(line))] #获取随机生成的数字
        a = sorted(list(set(s))) #去重并排序
        for i in a: print(i) #输出多行
        line = getline()