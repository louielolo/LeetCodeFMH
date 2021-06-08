from singlelinked import *
class Solution:
    def reverse(self,head):
        """reverse定义
        输入一个节点head,以head为起点，将链表反转，返回反转后的头节点
        """
        if head.next is None or head is None:
            return head
        else:
            last = SingleNode
            last = self.reverse(head.next)
            head.next.next = head
            head.next = None
            return last
    
    def reversetop(self,head,n):
        """reversetop定义
        输入一个节点head，"""

if __name__ == '__main__':
    one = SingleNode(1)
    two = SingleNode(2)
    three = SingleNode(3)
    four = SingleNode(4)
    five = SingleNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = None
    s = Solution()
    s.reverse(one)
    print("ok")

