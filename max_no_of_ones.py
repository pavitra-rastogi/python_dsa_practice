# Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        index_freq={}
        min_index=0
        count=[0]*n
        for i in range(n):
            index_freq[i]=0
            for j in range(n):
                if A[i][j]==1:
                    index_freq[i]+=1
        max_value = -1
        lowest_key = 0
    
    # Single pass to find max value and lowest key
        for key, value in index_freq.items():
            if value > max_value:
                max_value = value
                lowest_key = key
            elif value == max_value:
                lowest_key = min(lowest_key, key)
    
    #print(lowest_key)
        return lowest_key
