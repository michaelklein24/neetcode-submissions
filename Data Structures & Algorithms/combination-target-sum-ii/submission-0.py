class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(t: int, i: int, combination: List[int]):
            if t == 0:
                result.append(combination[::])
                return

            if i >= len(candidates) or candidates[i] > t:
                return        

            combination.append(candidates[i])
            backtrack(t - candidates[i], i + 1, combination[::])
            combination.pop()
 
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(t, i + 1, combination[::])
        
        backtrack(target, 0, [])
        return result