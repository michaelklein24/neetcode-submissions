import collections

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list) # vals are tuples (timestamp, val)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        l, r = 0, len(arr) - 1
        prev = None
        while l <= r:
            m = (l + r) // 2
            if timestamp < arr[m][0]:
                r = m - 1
            elif timestamp > arr[m][0]:
                prev = arr[m]
                l = m + 1
            else:
                return arr[m][1]

        return "" if prev == None else prev[1]