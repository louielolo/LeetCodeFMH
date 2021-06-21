# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.treelist = []
        self.leftmax = 0
        self.rightmin = 0

    def inorder(self,root: TreeNode)->list:
        if root is None:
            return self.treelist
        self.inorder(root.left)
        self.treelist.append(root.val)
        self.inorder(root.right)
        return self.treelist

    def findmax(self,root: TreeNode)-> int:
        max = root.val
        if root.left is not None:
            maxLeft = self.findmax(root.left)
            max = max if max > maxLeft else maxLeft 
        if root.right is not None:
            maxRight = self.findmax(root.right)
            max = max if max > maxRight else maxRight
        return max
    def findmin(self,root: TreeNode)-> int:
        min = root.val
        if root.left is not None:
            minLeft = self.findmax(root.left)
            min = min if min < minLeft else minLeft
        if root.right is not None:
            minRight = self.findmin(root.right)
            min = min if min < minRight else minRight
        return min
    def is_BST(self,root:TreeNode,operator='inorder')->bool:
        """判断二叉树是否为BST"""
        #空树是二叉搜索树
        if root is None:
            return True
        #方法一：中序遍历后，二叉树列表将从小到大排列，若是，为BST；否，不是BST
        if operator == 'inorder':
            listBT = self.inorder(root)
            for i in range(1,len(listBT)):
                if listBT[i]>listBT[i-1]:
                    continue
                else:
                    return False
            return True
        #方法二：root.val 比root.left.val大，比root.right.val小的话不正确
        if operator == 'minmax':
            if root.left is not None and self.findmax(root.left)>root.val:
                return False
            if root.right is not None and self.findmin(root.right)<root.val:
                return False
            return self.is_BST(root.left) and self.is_BST(root.right)
        #约束需要传递到左右子树的子结点去
        return self.is_BST(root,None,None)


if __name__ == '__main__':
    A = TreeNode(10)
    B = TreeNode(5)
    C = TreeNode(15)
    D = TreeNode(6)
    E = TreeNode(20)
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(4)
    e = TreeNode(6)
    A.left = B
    A.right = C
    C.left = D
    C.right = E
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    s1 = Solution()
    s2 = Solution()
    print(s1.is_BST(A,'minmax'))
    print(s2.is_BST(a,'minmax'))