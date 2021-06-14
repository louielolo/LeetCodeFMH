"""
链接：https://www.nowcoder.com/questionTerminal/37548e94a270412c8b9fb85643c8ccc2
来源：牛客网
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
示例1
输入
"["
输出
false
示例2
输入
"[]"
输出
true
"""
import sys
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
class Solution:
    def __init__(self):
        self.embrace_dict = {']':'[','}':'{',')':'(','{':'}','[':']','(':')'}
        self.legal_flag = True
    def is_evenstack(self,stack):
        stack_length = stack.size()
        if stack_length > 0:
            if stack_length % 2 == 0:
                return True
            else:
                return False
        return False
if __name__ == '__main__':
    getline = lambda: sys.stdin.readline().strip().strip("\"") #利用lambda定义读取数据函数
    line = getline()
    s = Solution()
    stack = Stack()
    output = True
    while line:
        for elem in line:
            stack.push(elem)
        if s.is_evenstack(stack):
            while stack.size():
                elem_pre = stack.pop()
                elem_post = stack.pop()
                if elem_post == s.embrace_dict[elem_pre]:
                    output = output and True
                else:
                    output = output and False
        else:
            output = output and False
        if output:
            print('true')
        else:
            print('false')
        line = getline()