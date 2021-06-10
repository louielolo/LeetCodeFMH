# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor_recur(self, number):
        if number ==1:
            return 1
        if number == 2:
            return 2
        return self.jumpFloor_recur(number-1)+self.jumpFloor_recur(number-2)
        # write code here
    
    def jumpFloor_loop(self,number):
        if number ==1:
            return 1
        if number == 2:
            return 2
        pre,post = 1,2
        for i in range(3,number+1,1):
            sum = pre+post
            pre = post
            post = sum
        return sum
if __name__=='__main__':
    s = Solution()
    steps = int(input())
    print(s.jumpFloor_recur(steps))
    print(s.jumpFloor_loop(steps))