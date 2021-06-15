import sys
import collections

class Solution:
    def leastInterval(self, tasks:list, n: int) -> int:
        freq = collections.Counter(tasks)

        # 任务总数
        m = len(freq) #任务种类数
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid) #算法优化的部分，减少遍历次数
            
            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j
            
            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time

if __name__ == '__main__':
    s = Solution()
    tasks = ["A","A","A","A","A","A","B","B","B","B","B","B"]
    n = 1.5
    leastInterval = s.leastInterval(tasks,n)
    print(leastInterval)