'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import os
class Solution:
    def __init__(self):
        self.outputArr = []
    def excludeZero(self,sortedArr:list)->list:
        outputArr = []
        zeroPos = sortedArr.index(0)
        pre_i = 666666
        pre_j = 777777
        for i in range(0,zeroPos):
            if zeroPos >= 1 :
                if sortedArr[i] != pre_i:
                    for j in range(i+1,zeroPos):
                        if sortedArr[j]!=pre_j and (0-(sortedArr[i]+sortedArr[j])) in sortedArr[zeroPos+1:]:
                            outputArr.append([sortedArr[i],sortedArr[j],0-(sortedArr[i]+sortedArr[j])])
                        pre_j = sortedArr[j]
            else:
                return outputArr
            pre_i = sortedArr[i]
            pre_j = 777777
        return outputArr
    def includeZero(self,setArr:list)->list:
        outputArr = []
        zeroPos = setArr.index(0)
        for i in range(0,zeroPos):
            if -1*setArr[i] in setArr[zeroPos+1:]:
                outputArr.append([setArr[i],0,-1*setArr[i]])
        return outputArr
    def threeSum(self,nums:list)->list:
        arr = []
        arr1 = []
        arr2 = []
        arr3 = []
        nums.append(0)
        '''寻找不重复的和为0三元素'''
        sortedArr = sorted(nums)
        #先找不含0元素的
        arr1 = self.excludeZero(sortedArr)
        sortedArr = sorted(nums,reverse=True)
        arr2 = self.excludeZero(sortedArr)
        #去重后寻找含0元素的
        if nums.count(0)>1:
            setArr = sorted(set(nums))
            arr3 = self.includeZero(setArr)
        else:
            arr3 = []
        if sortedArr.count(0)>3:
            arr4 = [[0,0,0]]
        else:
            arr4 = []
        arr = arr1+arr2+arr3+arr4
        return arr

if __name__ == '__main__':
    s = Solution()
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(s.threeSum(nums))
        
        
