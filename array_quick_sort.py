class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N=len(A)

        def partition(A,L,R):
            i=L
            j=L 
            pivot=A[R]
            while(j<R):
                if A[j]<pivot:
                    A[i],A[j]=A[j],A[i]
                    i+=1
                j+=1
            A[i],A[R]=A[R],A[i]
            return i

        def quick_sort(A,L=0,R=N-1):
  
            if L>=R:
                return
            p_index=partition(A,L,R)

            quick_sort(A,L,p_index-1)
            quick_sort(A,p_index+1,R)
        
        quick_sort(A, 0, N - 1)
        return A