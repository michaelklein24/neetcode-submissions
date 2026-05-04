class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            m = (l + r) // 2
            n = half - m - 1 - 1

            aLeft = A[m] if m >= 0 else float("-inf")
            bLeft = B[n] if n >= 0 else float("-inf")
            aRight = A[m + 1] if m + 1 < len(A) else float("inf")
            bRight = B[n + 1] if n + 1 < len(B) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 1:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft >= bRight:
                r = m - 1
            else:
                l = m + 1
