class Solution:
    def findMin(self, nums: List[int]) -> int:
        def isSorted(startI, endI) -> bool:
            return nums[startI] <= nums[endI]

        result = float('inf')
        l, r = 0, len(nums) - 1


        while l <= r:
            m = (l + r) // 2
            if isSorted(l, m):
                result = min(result, nums[l])
                l = m + 1
            else:
                result = min(result, nums[m])
                r = m - 1
        
        return result

            