# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        pass
    def MaxDepth(self,root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.MaxDepth(root.left),self.MaxDepth(root.right))+1
    def MinDepth(self,root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return min(self.MinDepth(root.left),self.MinDepth(root.right))+1
    
    def DLR(self,root: TreeNode,elem_list: list) -> list:
        if root is None:
            return elem_list
        else:
            elem_list.append(root.val)
            self.DLR(root.left,elem_list)
            self.DLR(root.right,elem_list)
            return elem_list
            

if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    A.right = B
    B.right = C
    C.right = D
    s = Solution()
    elem_list = []
    print(s.MaxDepth(A))
    print(s.MinDepth(A))
    print(s.DLR(A,elem_list))
    