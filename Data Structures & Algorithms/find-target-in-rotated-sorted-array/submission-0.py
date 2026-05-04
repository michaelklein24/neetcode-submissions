class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def isSorted(start, end):
            return nums[start] <= nums[end]
        
        def binarySearch(l, r):
            while l <= r: 
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    return m
            return -1


        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if isSorted(l, m):
                if nums[l] <= target <= nums[m]:
                    return binarySearch(l, m)
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    return binarySearch(m, r)
                else:
                    r = m - 1
        
        return -1
