class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        diag_sum=0
        r=0
        c=len(A)-1
        while(r<len(A) and c>=0):
            diag_sum+=A[r][c]
            r+=1
            c-=1
        return diag_sum
