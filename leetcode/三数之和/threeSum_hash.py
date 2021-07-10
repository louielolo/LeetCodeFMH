from  typing import List
class Solution:    
    def __init__(self):
        self.hashMap={}
        self.data = []
    
    def makeHash(self, t):
        t.sort()
        t_string = [str(i) for i in t]
        key = ' '.join(t_string)
        return key

    def twoSum(self, target_index, nums):
        Map={}
        target = -nums[target_index]
        zero_flag = 0
        for i in range(len(nums)):
            if i==target_index:
                continue
            exp = target - nums[i]
            if nums[i] in Map:
                # 若重复直接pass
                if(exp in Map and zero_flag):
                        pass
                else:
                    if(exp == nums[i] and exp == 0):
                        zero_flag = 1
                    Map[exp] = nums[i]
                    t = [nums[target_index], nums[i], exp]
                    key = self.makeHash(t)
                    if key in self.hashMap:
                        pass
                    else:
                        self.data.append(t)
                        self.hashMap[key] = 1
            else:
                Map[exp] = nums[i]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) >= 3:
            for i in range(len(nums)):
                self.twoSum(i, nums)
        return self.data

if __name__ == '__main__':
    s = Solution()
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(s.threeSum(nums))