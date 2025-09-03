class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    # merge and sort 2 sorted arrays
    def solve(self, A, B):
        p1=0
        p2=0
        c=[]
        N=len(A)
        M=len(B)

        while(p1<N and p2<M):
            if A[p1]<B[p2]:
                c.append(A[p1])
                p1+=1
            else:
                c.append(B[p2])
                p2+=1
        while(p1<N):
            c.append(A[p1])
            p1+=1
        while(p2<M):
            c.append(B[p2])
            p2+=1
        
        return c