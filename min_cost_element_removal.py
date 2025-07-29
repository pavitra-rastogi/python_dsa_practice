class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)  # Remove largest elements first
        total_cost = 0
        current_sum = sum(A)

        for i in range(len(A)):
            total_cost += current_sum
            current_sum -= A[i]

        return total_cost
