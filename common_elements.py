class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        freqB = {}
        for num in B:
            if num in freqB:
                freqB[num] += 1
            else:
                freqB[num] = 1

        ans = []
        for num in A:
            if num in freqB and freqB[num] > 0:
                ans.append(num)
                freqB[num] -= 1  # reduce count so duplicates are handled properly
        return ans