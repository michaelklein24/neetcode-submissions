class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = set()
        def backtrack(runningSum: int, combination: List[int]):
            if runningSum == target:
                combination.sort()
                combinations.add(tuple(combination))
                return
            if runningSum > target:
                return
            
            for num in nums:
                combination.append(num)
                runningSum += num
                backtrack(runningSum, combination.copy())
                runningSum -= num
                combination.pop()
        
        backtrack(0, [])
        return [list(combination) for combination in combinations]