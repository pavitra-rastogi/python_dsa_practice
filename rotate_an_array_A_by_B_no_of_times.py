class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    def solve(self, A, B):
        n = len(A)
        B = B % n

        def reverse_li(li, s, e):
            i = s
            j = e
            while i < j:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp
                i += 1
                j -= 1
            return li

        reverse_li(A, 0, n - 1)
        reverse_li(A, 0, B - 1)
        reverse_li(A, B, n - 1)

        return A