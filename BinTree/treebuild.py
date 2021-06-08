class TreeNode(object):
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree(object):
    def __init__(self):
        self.root = None


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
