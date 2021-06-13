"""
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度大于2的子串重复
输入描述：
一组或多组长度超过2的字符串。每组占一行
输出描述：
如果符合要求输出：OK，否则输出NG
"""
import re
import sys
class Solution:
    def substring_duplicate(self,pwd):
        if pwd is not None and len(pwd)>=3:
            for i in range(len(pwd)-3):
                if pwd.count(pwd[i:i+3])>1:
                    return False
        return True
    def complex_rule(self,pwd):
        condition = 0
        if pwd is None or len(pwd)<1 or pwd.isalpha() or pwd.isdigit() or pwd.isspace():  #是否是纯字母构成,字母和数字的组合,纯数字构成
            return False
        if re.search(r'\d+', pwd):
            condition = 1
        if re.search(r'[a-z]+', pwd):
            condition += 1
        if re.search(r'[A-Z]+', pwd):
            condition += 1
        if re.search(r'[!@#$%^&*()_+=-]+', pwd):
            condition += 1
        if condition >=3:
            return True
        else:
            return False
        return False

    def pw_sw_verify(self,pwd):
        if self.complex_rule(pwd) and self.substring_duplicate(pwd):
            print('OK')
        else:
            print('NG')

if __name__ == '__main__':
    s = Solution()
    getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
    pwd = getline()
    while pwd:
        s.pw_sw_verify(pwd)
        pwd = getline()