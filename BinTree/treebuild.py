class TreeNode(object):
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree(object):
    def __init__(self):
        self.root = None

def DLR(treenode):
    """Degree Left Right前序遍历"""
    #使用递归方法
    if treenode is None:
        return
    print(treenode.data)
    DLR(treenode.left)
    DLR(treenode.right)

def LDR(treenode):
    """Left Degree Right中序遍历"""
    #使用递归方法
    if treenode is None:
        return
    LDR(treenode.left)
    print(treenode.data)
    LDR(treenode.right)

def LRD(treenode):
    """Left Right Degree后序遍历"""
    if treenode is None:
        return
    LRD(treenode.left)
    LRD(treenode.right)
    print(treenode.data)

if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    A.left,A.right = B,C
    B.left,B.right = D,E
    C.left = F
    DLR(A)
    print("------------------------------------------------")
    LDR(A)
    print("------------------------------------------------")
    LRD(A)
