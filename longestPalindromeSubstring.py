class Solution:
    # @param A : string
    # @return a string
    def longestPalindrome(self, A):
        n = len(A)
        if n <= 1:
            return A

        start = 0
        max_len = 1

        def expand_around_center(left, right):
            while left >= 0 and right < n and A[left] == A[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(n):
            # Odd length
            l1, r1 = expand_around_center(i, i)
            if r1 - l1 + 1 > max_len:
                start = l1
                max_len = r1 - l1 + 1

            # Even length
            l2, r2 = expand_around_center(i, i + 1)
            if r2 - l2 + 1 > max_len:
                start = l2
                max_len = r2 - l2 + 1

        return A[start:start + max_len]
