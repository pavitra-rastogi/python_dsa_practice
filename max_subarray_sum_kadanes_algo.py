class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0  # Handle empty array (though problem guarantees non-empty)
        
        curr_sum = A[0]
        max_sum = A[0]
        
        for i in range(1, len(A)):
            curr_sum = max(A[i], curr_sum + A[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

# This is Kadane's algorithm
