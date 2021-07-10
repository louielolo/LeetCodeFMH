class Solution:
    def findKthLargeElem(self,arr:list)->int:
        pass
    def bubblesort(self,arr:list)->list:
        if len(arr)<=1:
            return arr
        for j in range(len(arr)-1):
            for i in range(len(arr)-1-j):
                if arr[i]>arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
        return arr

    def quicksort(self,arr:list)->list:
        if len(arr)<=1:
            return arr
        base = arr[0]
        smaller = [i for i in arr if i < base ]
        larger = [i for i in arr if i > base]
        return self.quicksort(smaller)+[base]+self.quicksort(larger)

if __name__ == '__main__':
    arr = [1,-1,6,2,5,3,-2]
    s = Solution()
    print(s.bubblesort(arr))
    print(s.quicksort(arr))