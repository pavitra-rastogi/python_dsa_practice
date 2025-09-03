import math
from functools import cmp_to_key

class Solution:
    @staticmethod
    def factors(num):
        if num == 0:
            return 0
        count = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if i * i == num:   # perfect square
                    count += 1
                else:
                    count += 2
        return count

    @staticmethod
    def comparator(a, b):
        factors_a = Solution.factors(a)
        factors_b = Solution.factors(b)

        if factors_a < factors_b:
            return -1
        elif factors_a > factors_b:
            return 1
        else:
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

    def solve(self, A):
        A=sorted(A, key=cmp_to_key(Solution.comparator))
        return A
