class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            ext=(n>>i)&1
            if ext==1:
                res|=(1<<(31-i))
        return res        