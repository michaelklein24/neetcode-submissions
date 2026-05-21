class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openCount: int, closeCount: int, parenthesis: str):
            if openCount == closeCount and openCount == n:
                res.append(parenthesis[::])
                return
            
            if openCount > closeCount:
                backtrack(openCount, closeCount + 1, parenthesis + ")")

            if openCount < n or openCount == closeCount:
                backtrack(openCount + 1, closeCount, parenthesis + "(")


        backtrack(1, 0, "(")
        return res