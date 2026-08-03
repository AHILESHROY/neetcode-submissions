class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        res=[]
        res.append(bin(a+b))
        return str(res[0][2:])