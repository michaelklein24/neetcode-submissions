class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def backtrack(i, curr):
            if curr == target:
                res.append(combination.copy())
                return

            if curr > target or i >= len(nums):
                return
            
            backtrack(i + 1, curr)

            curr += nums[i]
            combination.append(nums[i])
            backtrack(i, curr)
            combination.pop()
            curr -= nums[i]

        backtrack(0, 0)
        return res
