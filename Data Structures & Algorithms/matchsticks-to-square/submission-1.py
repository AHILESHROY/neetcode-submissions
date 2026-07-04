class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        per_side=sum(matchsticks)/4
        if sum(matchsticks)%4!=0:
            return False
        matchsticks.sort(reverse=True)
        used=[False]*len(matchsticks)
        def bt(index,k,subsetsum):
            if k==1:
                return True

            if subsetsum==per_side:
                return bt(0,k-1,0)
            for i in range(index,len(matchsticks)):
                if used[i] or subsetsum+matchsticks[i]>per_side:
                    continue
                used[i]=True    
                if bt(i+1,k,subsetsum+matchsticks[i]):
                    return True
                used[i]=False
            return False            
        return bt(0,4,0)

