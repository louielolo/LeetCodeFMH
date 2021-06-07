from singlelinked import *
class Solution:
    def reverse(head):
        if head.next is None:
            return head
        last = SingleNode()
        last = Solution.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

if __name__ == '__main__':
    one = SingleNode(1)
    two = SingleNode(2)
    three = SingleNode(3)
    one.next = two
    two.next = three
    newhead = Solution.reverse(one)
    print("ok")

