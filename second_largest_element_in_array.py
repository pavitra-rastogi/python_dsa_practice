class Solution:
    def solve(self, A):
        if len(A) < 2:
            return -1

        first = second = -1
        for num in A:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        return second if second != -1 else -1