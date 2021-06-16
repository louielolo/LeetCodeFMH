# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def getDepth(self,root: TreeNode) -> int:
        """可以获取节点的Depth和Height"""
        if root is None:
            return 0
        else:
            return max(self.MaxDepth(root.left),self.MaxDepth(root.right))+1   
    def getElemPreOrder(self,root: TreeNode,elem_list: list) -> list:
        """将树中的元素都放入列表"""
        if root is None:
            return elem_list
        else:
            elem_list.append(root.val)
            self.getElemPreOrder(root.left,elem_list)
            self.getElemPreOrder(root.right,elem_list)
            return elem_list
    def sortedArrayToBST(self,arr:list) -> TreeNode:
        """使用有序列表中的元素，创建平衡二叉树"""
        #数量合适的话可建满二叉树
        if not arr:
            return None
        mid = (len(arr))//2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrayToBST(arr[:mid])
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root
    def preorder(self,root:TreeNode):
        """前序遍历，根节点左节点右节点"""
        if root is None:
            return None
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def is_balanceBST(self,root: TreeNode):
        """判断是否为平衡二叉树"""
        if root is None:
            return True
        if self.is_balanceBST(root.left) and self.is_balanceBST(root.right) and abs(self.getDepth(root.left)-self.getDepth(root.right))<=1:
            return True
        else:
            return False
            

if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(5)
    D = TreeNode(4)
    E = TreeNode(3)
    F = TreeNode(6)
    G = TreeNode(7)
    H = TreeNode(8)
    I = TreeNode(9)
    J = TreeNode(10) 
    A.left = B
    A.right = C
    B.left = D
    D.left = G
    G.left = H
    C.left = E
    C.right = F
    F.right = I
    I.right = J
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(4)
    e = TreeNode(3)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f   
    s = Solution()
    elem_list = []
    print(s.MaxDepth(A))
    print(s.MinDepth(A))
    print(s.DLR(A,elem_list))
    sorted_arr = sorted(elem_list)
    print(sorted_arr)
    root = s.sortedArrayToBST(sorted_arr)
    s.preorder(root)
    if s.is_balanceBST(A):
        print('true')
    else:
        print('false')
    if s.is_balanceBST(a):
        print('true')
    else:
        print('false')      
    