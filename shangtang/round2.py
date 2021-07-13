'''
int a = 10;
int b = 20;

#ifdef MACRO1
std::string s1 = “1”;
#endif

#ifdef MACRO2
std::string s1=“2”;
#ifdef MACRO3
std::string s3 = “.”;
#endif
#endif
'''
#silu1
import sys
class Solution:
    def __init__(self):
        #存放宏定义位置的二维数组
        self.macroList = []
    def searchMacro(self,txt,up,down):
        count = 0
        while up >0 and down < len(txt):

            if not txt[up].index('#ifdef'):
                up -= 1
            else:
                self.macroList[count].append(up)
            if not txt[down].index('#endif'):
                down += 1
            else:
                self.macroList[count].append(down)
            count += 1
    def deleteTest(self,arr:list):
        '''按照列表中一对数组，将之间行删除'''
    def deleteMacro(self,text):
        '''delete micro in cpp file'''
        #读取文件
        txt = read(text,r)
        for line in range(txt):
            if line.index('#ifdef') and line.index('#endif'):
                macroList = self.searchMacro(txt, line-1,line+1)
        #根据数组存放位置将之间的删除 
        self.deleteTest(macroList)
