# runner.py

class Solution:
    def solve(self, A):
        first_index = {}
        min_index = float('inf')
        result = -1
        i = 0
        for ele in A:
            if ele in first_index:
                if first_index[ele] < min_index:
                    min_index = first_index[ele]
                    result = ele
            else:
                first_index[ele] = i
            i += 1

        return result



if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [3, 2, 1, 2, 3],     # Expected output: 2
        [1, 2, 3, 4],        # Expected output: -1
        [5, 5, 6, 7],        # Expected output: 5
        [10, 20, 10, 30, 20], # Expected output: 10
        [10, 5, 3, 4, 3, 5, 6] # Expected output: 5
    ]

    case_number = 1
    for case in test_cases:
        result = sol.solve(case)
        print("Test case", case_number, ":", case, "->", result)
        case_number += 1
