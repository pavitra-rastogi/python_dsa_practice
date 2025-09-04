# Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], 
# if we split the array into some number of "chunks" (partitions), and individually sort each chunk. 
# After concatenating them in order of splitting, the result equals the sorted array.
# What is the most number of chunks we could have made?
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        max_so_far = -1
        N = len(A)
        for i in range(N):
            max_so_far = max(max_so_far, A[i])
            if max_so_far == i:
                count += 1
        return count
