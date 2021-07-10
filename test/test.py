#找到数组重复元素前k个最多的
class Solution:
    def findCountMaxK(self,arr:list,k)->list:
        dict_origin = {}
        #去重，找到独立的元素
        arr_elem = set(arr)
        #遍历元素，找到每个元素的个数，存入字典
        for i in arr_elem:
            dict_origin[i] = arr.count(i)
        #按元素个数value值排序
        sorted_dict = sorted(dict_origin.items(),key=lambda item:item[1],reverse=True)
        #取出前几个
        output_arr = []
        for i in range(k):
            output_arr.append(sorted_dict[i][0])
        return output_arr

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,2,2,3,3,3,3,3,1,4,5,6,7,8]
    k = 3
    print(s.findCountMaxK(arr,k))
            