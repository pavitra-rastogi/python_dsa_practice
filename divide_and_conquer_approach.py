# You are given an array A of integers of length N and two indices, B and C.
# Your task is to sort the subarray [B, C] within the given array. The rest of the array should remain unchanged.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def sortSubarray(self, A, B, C):
        N=len(A)
        def merge_array(A,s,m,e):
            p1=s
            p2=m+1
            c=[]
            while(p1<=m and p2<=e):
                if A[p1]<A[p2]:
                    c.append(A[p1])
                    p1+=1
                else:
                    c.append(A[p2])
                    p2+=1
            while(p1<=m):
                c.append(A[p1])
                p1+=1
            while(p2<=e):
                c.append(A[p2])
                p2+=1
            
            k=s
            for ele in c:
                A[k]=ele
                k+=1

        def merge_sort(A,s=B,e=C):
            if s==e:
                return
            m=(e+s)//2
            merge_sort(A,s,m)
            merge_sort(A,m+1,e)
            merge_array(A,s,m,e)

        merge_sort(A,B,C)
        return A 


