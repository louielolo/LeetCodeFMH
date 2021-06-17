from collections import deque
class MaxQueue:

    def __init__(self):
        self.dq = deque()

    def max_value(self) -> int:
        if self.q:
            return max(self.dq)
        else:
            return -1


    def push_back(self, value: int) -> None:
        self.dq.append(value)


    def pop_front(self) -> int:
        return self.dq.popleft() if self.dq else -1