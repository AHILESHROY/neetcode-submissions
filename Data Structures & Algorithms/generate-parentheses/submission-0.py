class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        string=[]
        Open ,Close=0,0
        def bt(Open,Close):
            
            if Open==Close==n:
                res.append("".join(string))
                return
            if Open<n:
                string.append("(")

                bt(Open+1,Close)
                string.pop()
            if Close<Open:
                string.append(")")
                bt(Open,Close+1)
                string.pop()

        bt(0,0)
        return res