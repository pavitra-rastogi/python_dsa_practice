# Determine the "GOOD"ness of a given string A, where the "GOOD"ness is defined by the length of the longest substring that contains no repeating characters. The greater the length of this unique-character substring, the higher the "GOOD"ness of the string.
# Your task is to return an integer representing the "GOOD"ness of string A.
# Note: The solution should be achieved in O(N) time complexity, where N is the length of the string.
# Problem Constraints
# 1 <= size(A) <= 106
# Strng consists of lowerCase,upperCase characters and digits are also present in the string A.
# Input Format
# Single Argument representing string A.
# Output Format
# Return an integer denoting the maximum possible length of substring without repeating characters.
# Example Input
# Input 1:
#  A = "abcabcbb"
# Input 2:
#  A = "AaaA"
# Example Output
# Output 1:
#  3
# Output 2:
#  2


class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
		last_seen= dict()
		left = 0
		max_len = 0
		for right in range(len(A)):
			ch = A[right]
			if ch in last_seen and last_seen[ch] >= left :
				left = last_seen[ch] + 1
			last_seen[ch] = right
			max_len = max(max_len, right - left + 1)
		return max_len