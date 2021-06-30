"""
描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）

本题有多组输入，请使用while(cin>>)处理

输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述：
输出排好序的数字

输入：
8
1 2 4 9 3 55 64 25
0
5
1 2 3 4 5
1
复制
输出：
1 2 3 4 9 25 55 64
5 4 3 2 1
"""
import sys
if __name__ == '__main__':
    getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
    randnum = getline()
    while randnum:
        list = getline()
        s = [int(elem) for elem in list.split()]
        if getline()=='0':
            sort_flag = False
        else:
            sort_flag = True
        a = sorted(s,reverse=sort_flag)
        print(' '.join(str(i) for i in a))
        randnum = getline()