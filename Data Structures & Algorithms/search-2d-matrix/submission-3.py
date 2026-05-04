class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0])
        col_len = len(matrix)
        total_len = row_len * col_len
        print(f"total length: {total_len}")

        l, r = 0, total_len - 1

        def getVal(index: int):
            rowI = index // row_len
            colI = index % row_len
            return matrix[rowI][colI]

        while l <= r:
            m = (l + r) // 2
            lVal, mVal, rVal = getVal(l), getVal(m), getVal(r)

            print(f"l:{l}, r:{r}, m:{m}")
            print(f"lVal:{lVal}, rVal:{rVal}, mVal:{mVal}")

            if lVal == target or mVal == target or rVal == target:
                return True
            elif target < mVal:
                r = m - 1
            else:
                l = m + 1
        
        return False