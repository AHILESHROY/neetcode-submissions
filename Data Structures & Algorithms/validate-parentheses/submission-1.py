class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        openp=0
        openpa=["[","{","("]
        closepa=["]","}",")"]
        closep=0
        for i in s:
            if i in openpa:
                openp+=1
                stack.append(i)
            else:
                if closep<openp and  openpa[closepa.index(i)]==stack[-1]:
                    stack.pop()
                    openp-=1
                else:
                    closep+=1    
        if len(stack)==0 and closep==0:
            return True
        else:
            return False            
            