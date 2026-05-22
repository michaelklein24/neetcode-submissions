class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def isPalindrome(string: str, l: int, r: int):
            while l < r:
                if string[l] != string[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        def backtrack(i: int):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    backtrack(j + 1)
                    partition.pop()

        backtrack(0)
        return res