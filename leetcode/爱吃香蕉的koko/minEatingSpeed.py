class Solution:
    def minEatingSpeed(self,piles: list,H: int)->int:
        def possible(K):
            return sum((p-1)/K+1 for p in piles) <= H
        lo,hi =  1,max(piles)
        while lo<hi:
            mi = (lo+hi)/2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
if __name__ == '__main__':
    piles = [3,6,7,11]
    H = 8
    s = Solution()
    print(s.minEatingSpeed(piles,H))