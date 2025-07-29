class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        sum=0
        for i in range(len(A)):
            sum+=A[i][i]
        return sum

