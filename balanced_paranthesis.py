class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        st=[]
        for ch in A:
            if ch in ["(","{","["]:
                st.append(ch)
            elif ch==")" and len(st)>0 and st[-1]=="(":
                st.pop()
            elif ch=="}" and len(st)>0 and st[-1]=="{":
                st.pop()
            elif ch=="]" and len(st)>0 and st[-1]=="[":
                st.pop()
            else:
                return 0
        if len(st)==0:
            return 1
        else:
            return 0
