class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i: int, subset: List[int]):
            if (i >= len(nums)):
                result.append(subset)
                return
            
            # Decision to include int
            subset.append(nums[i])
            dfs(i + 1, subset[::])

            # Decision to not include int
            subset.pop()
            dfs(i + 1, subset[::])
        
        dfs(0, [])
        return result
            