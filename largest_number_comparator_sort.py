from functools import cmp_to_key

class Solution:
    @staticmethod
    def comparator(a, b):
        x, y = str(a), str(b)
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    def largestNumber(self, A):
        A.sort(key=cmp_to_key(Solution.comparator))
        if A[0] == 0:
            return "0"
        else:
            return "".join(map(str, A))
