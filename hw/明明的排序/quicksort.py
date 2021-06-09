def quicksort(listorigin:list) -> list:
    """快速排序"""
    #使用递归的方法
    if len(listorigin)>1:
        mid = listorigin[0]
        left = quicksort([elem for elem in listorigin[1:] if elem < mid])
        right = quicksort([elem for elem in listorigin[1:] if elem > mid])
        return left + [mid] + right
    else:
        return listorigin
