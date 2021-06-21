"""
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

二叉搜索树的定义如下：

任意节点的左子树中的键值都 小于 此节点的键值。
任意节点的右子树中的键值都 大于 此节点的键值。
任意节点的左子树和右子树都是二叉搜索树。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxSum = 0

    def is_BST(self,root: TreeNode):
        if root.left and root.right is None:
            return True
        if root.left is not None:
            return False
    def findMax(self,root):
        pass
    def findMin(self,root):
        pass
    def getSum(self,root):
        pass
    def traverse(self,root: TreeNode):
        """前序遍历的位置,就是干活的位置，如果主函数不能递归，就写一个专门递归的方法来完成遍历功能"""
        if root is None:
            return
        #只有左右子树均为BST，该root的树才可能为BST
        if not self.is_BST(root.left) or not self.is_BST(root.right):
            goto next
        leftmax = self.findMax(root.left)
        rightmin = self.findMin(root.right)
        #如果root的val比左边小，比右边大，就不是BST
        if root.val <= leftmax or root.val >= rightmin:
            goto next
        #如果条件都符合，开始计算BST的和
        leftsum = self.getSum(root.left)
        rightsum = self.getSum(root.right)
        bstSum = leftsum + rightsum +root.val
        self.maxSum = max(bstSum,self.maxSum)

        """递归的位置"""
        next
        self.traverse(root.left)
        self.traverse(root.right)
        return self.maxSum

    def maxSumBST(self,root:TreeNode)->int:
        self.maxSumBST(root.left)
        self.maxSumBST(root.right)
        if root.left and root.right is not None:
            return max(root.left.val + root.right.val + root.val)



