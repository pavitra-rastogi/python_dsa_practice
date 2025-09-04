class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans=[]
        max_ar=max(A)
        min_ar=min(A)
        freq_ar=[0]*(max_ar-min_ar+1)
        for i in range(len(A)):
            index=A[i]-min_ar
            freq_ar[index]+=1
        for i in range(len(freq_ar)):
            freq=freq_ar[i]
            num=i+min_ar
            for _ in range(freq):
                ans.append(num)
        return ans


