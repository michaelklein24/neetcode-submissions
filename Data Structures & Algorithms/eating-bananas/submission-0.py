import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTime(rate: int):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            return hours
        
        l, r = 1, max(piles)
        k = float('inf')

        while l <= r:
            m = (l + r) // 2
            hours = calcTime(m)

            if hours > h:
                l = m + 1
            else:
                k = min(k, m)
                r = m - 1

        return k
