import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateDistanceFromOrigin(point: List[int]):
            return math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)

        minHeap = [] # [(distance, [x, y])]

        for point in points:
            heapq.heappush(minHeap, (calculateDistanceFromOrigin(point), point))

        result = []
        while len(result) < k:
            result.append(heapq.heappop(minHeap)[1])
        
        return result