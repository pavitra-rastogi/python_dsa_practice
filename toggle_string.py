class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans=[]
        for char in A:
            if 65<=ord(char)<=90:
                ans.append(chr(ord(char)+32))    #upper case to lower case
            elif 97<=ord(char)<=122:
                ans.append(chr(ord(char)-32))
        return "".join(ans)