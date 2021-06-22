"""
给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

示例 1：

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：下面是两条和最小的下降路径，用加粗标注：
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
示例 2：

输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：下面是一条和最小的下降路径，用加粗标注：
[[-19,57],
 [-40,-5]]
示例 3：

输入：matrix = [[-48]]
输出：-48

提示：

n == matrix.length
n == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import sys
class Solution:
    """寻找下降路径最小"""
    def __init__(self):
        self.memo = []

    def dp(self,matrix:list,i:int,j:int):
        # 索引合法性检查
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 99999
        # base case,类似递归到最后的返回值
        if i == 0:
            return matrix[0][j]
        # 备忘录查找，防止重复查找
        if self.memo[i][j]!=66666:
            return self.memo[i][j]
        #递归部分,状态转移部分
        self.memo[i][j] = matrix[i][j]+min(self.dp(matrix,i-1,j),self.dp(matrix,i-1,j-1),self.dp(matrix,i-1,j+1))
        return self.memo[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """主函数"""
        n = len(matrix)
        res = sys.maxsize
        # 备忘录里的初始化为66666
        self.memo = [[66666]*n for _ in range(n)]
        # 终点可能在matrix[n-1]的任意一列
        for j in range(n):
            res = min(res,self.dp(matrix,n-1,j))
        return res



if __name__ == '__main__':
    s = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(s.minFallingPathSum(matrix))