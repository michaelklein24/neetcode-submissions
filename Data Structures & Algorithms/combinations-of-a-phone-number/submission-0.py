class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        combination = []        
        phoneMapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i: int):
            if i >= len(digits):
                res.append("".join(combination))
                return

            letters = phoneMapping[digits[i]]

            for letter in letters:
                combination.append(letter)
                backtrack(i + 1)
                combination.pop()

        backtrack(0)

        return res