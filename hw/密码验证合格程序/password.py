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
class Solution:
    def substring_duplicate(self,pw):
        pass
    def complex_rule(self,pw):
        if pw is None or len(pw)<1 or pw.isalpha() or pw.isalnum or pw.isdigit() or pw.isspace():  #是否是纯字母构成,字母和数字的组合,纯数字构成
            return False
        if re.search(pw)

    def pw_sw_verify(self,pw):
        pass

if __name__ = '__main__':
    s = Solution()
    getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
    line = getline()
    while line:
        s.pw_sw_verify(line)
        line = getline()