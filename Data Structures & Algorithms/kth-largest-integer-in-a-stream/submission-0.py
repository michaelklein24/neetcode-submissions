import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = nums
        heapq.heapify_max(self.max_heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.max_heap, val)
        k_largest = heapq.nlargest(self.k, self.max_heap)
        return k_largest[-1]
        
