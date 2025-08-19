class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        if n == 0:
            return 0

        Lmax = [0] * n
        Rmax = [0] * n

        # Fill Lmax
        Lmax[0] = A[0]
        for i in range(1, n):
            Lmax[i] = max(Lmax[i - 1], A[i])

        # Fill Rmax
        Rmax[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            Rmax[i] = max(Rmax[i + 1], A[i])

        # Calculate trapped water
        ans = 0
        for i in range(n):
            ans += min(Lmax[i], Rmax[i]) - A[i]

        return ans
