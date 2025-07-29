#Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # A=[1,2,3,4,5,6]
        # 3 ie A[2]=[4,5,6]
        ans=-1
        A.sort()
        n=len(A)
        for i in range(n):
            num=n-1-i
            if i<n-1 and A[i]==A[i+1]:
                continue
            if A[i]==num:
                ans=1
        return ans
