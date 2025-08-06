class Solution:
    # @param A : integer
    def solve(self, A):
        if A == 0:
            return
        self.solve(A - 1)
        print(A, end=' ')

# Create instance and call the method
sol = Solution()
sol.solve(9)
print()  # To move to a new line after output

