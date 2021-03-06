'''
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.levelOrderArr = []
    
    def levelOrderBottom(self,node:TreeNode)->list:
        if node is None:
            return []
        self.levelOrderBottom(node.left)
        self.levelOrderBottom(node.right)
        if node.left or node.right is not None:
            arr = [node.left.val,node.right.val]
            self.levelOrderArr.append(arr)
        return self.levelOrderArr+ [[node.val]]
if __name__ == "__main__":
    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    D = TreeNode(15)
    E = TreeNode(7)
    A.left = B
    A.right = C
    C.left = D
    C.right = E
    s = Solution()
    print(s.levelOrderBottom(A))
        