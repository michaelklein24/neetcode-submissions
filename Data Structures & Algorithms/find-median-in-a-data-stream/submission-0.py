import heapq
class MedianFinder:

    def __init__(self):
        self.leftBound = [] # maxHeap
        self.rightBound = [] # minHeap

    def addNum(self, num: int) -> None:
        if not self.leftBound or num <= self.leftBound[0]:
            heapq.heappush_max(self.leftBound, num)
        else:
            heapq.heappush(self.rightBound, num)

        if len(self.leftBound) > len(self.rightBound) + 1:
            heapq.heappush(self.rightBound, heapq.heappop_max(self.leftBound))
        elif len(self.rightBound) > len(self.leftBound):
            heapq.heappush_max(self.leftBound, heapq.heappop(self.rightBound))

    def findMedian(self) -> float:
        if len(self.leftBound) > len(self.rightBound):
            return self.leftBound[0]
        elif len(self.rightBound) > len(self.leftBound):
            return self.rightBound[0]
        else:
            return (self.rightBound[0] + self.leftBound[0]) / 2
        