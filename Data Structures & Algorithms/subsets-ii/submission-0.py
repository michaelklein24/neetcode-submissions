class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i: int, combination: List[int]):
            if i == len(nums):
                res.append(combination.copy())
                return
            
            combination.append(nums[i])
            backtrack(i + 1, combination)
            combination.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, combination)
        
        backtrack(0, [])
        return res