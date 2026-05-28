class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []

        def backtrack(i: int, curr: int):
            if curr == target:
                res.append(combination.copy())
                return res

            if i >= len(candidates) or target < curr:
                return

            combination.append(candidates[i])
            curr += candidates[i]
            backtrack(i + 1, curr)
            combination.pop()
            curr -= candidates[i]

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
        
            backtrack(i + 1, curr)


        backtrack(0, 0)
        return res