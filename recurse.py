class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A<10:
            return A
        return (A%10) + self.solve(A // 10)

# sum of digits of a number