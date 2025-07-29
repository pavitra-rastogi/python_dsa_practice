class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        n = len(A)
        for i in range(B):
            min_idx = i
            for j in range(i + 1, n):
                if A[j] < A[min_idx]:
                    min_idx = j
            if min_idx != i:
                A[i], A[min_idx] = A[min_idx], A[i]
        return A[B - 1]
