class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        added = [False] * len(nums)

        def backtrack(permutation: List[int]):
            if len(permutation) == len(nums):
                res.append(permutation[::])
                return
    
            for i in range(len(nums)):
                if not added[i]:
                    added[i] = True
                    permutation.append(nums[i])
                    backtrack(permutation)

                    permutation.pop()
                    added[i] = False
        
        backtrack([])
        return res