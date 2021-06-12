"""
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）
"""
import sys
class Solution:
    def __init__(self):
        self.coordinate = [0,0]
    
    def is_legal(self,operation):
        if operation is not None and len(operation)>0 and operation[0] in ['A','S','D','W'] and operation[1:].isdigit():
            return True
        else:
            return False

    def comove(self,operation):
        switch = {
            'A': lambda x:[self.coordinate[0]-x,self.coordinate[1]],
            'S': lambda x:[self.coordinate[0],self.coordinate[1]-x],
            'D': lambda x:[self.coordinate[0]+x,self.coordinate[1]],
            'W': lambda x:[self.coordinate[0],self.coordinate[1]+x] 
        }
        if self.is_legal(operation):
            try:
                self.coordinate = switch[operation[0]](int(operation[1:]))
            except KeyError as e:
                pass
            return self.coordinate
        else:
            return self.coordinate

if __name__ == '__main__':
    getline = lambda: input().split(';') #利用lambda定义读取数据函数
    line = getline()
    s = Solution()
    for elem in line:
        last_coordinate = s.comove(elem)
    print(','.join(str(i) for i in last_coordinate))
