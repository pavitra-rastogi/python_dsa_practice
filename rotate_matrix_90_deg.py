class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n=len(A)
        for i in range(n):
            for j in range(i,n):
                temp=A[i][j]
                A[i][j]=A[j][i]
                A[j][i]=temp
                #transpose done now reverse each row
        
        for i in range(n):
            A[i].reverse()
        return A
