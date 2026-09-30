class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet={}
        wallet[5]=0
        wallet[10]=0
        wallet[20]=0

        for bill in bills:
            if bill==5:
                wallet[5]=wallet.get(5,0)+1
            if bill==10:
                if wallet[5]>0:
                    wallet[5]-=1
                    wallet[10]+=1
                else:
                    return False
            if bill==20:
                if wallet[10] and wallet[5]:
                    wallet[10]-=1         
                    wallet[5]-=1
                    wallet[20]+=1
                elif wallet[5]>=3:
                    wallet[5]-=3
                    wallet[20]+=1
                else:
                    return False
        return True                    
                    

        