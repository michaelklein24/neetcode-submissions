class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        
        def backtrack(t: int, i: int, combination: List[int]):
            if i >= len(nums) or nums[i] > t:
                return
            
            if t == nums[i]:
                combination.append(nums[i])
                result.append(combination[::])
                combination.pop()
                return
            
            t -= nums[i]
            combination.append(nums[i])
            backtrack(t, i, combination[::])
            combination.pop()
            
            t += nums[i]
            backtrack(t, i + 1, combination[::])
        
        backtrack(target, 0, [])
        return result