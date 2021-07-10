class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def reverseListNode(self,head:ListNode)->ListNode:
        if head is None:
            return None
        last = self.reverseListNode(head.next)
        head.next.next = head
        head.next = None
        return last





if __name__ == '__main__':
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    s = Solution()
    print(s.reverseListNode(A).val)