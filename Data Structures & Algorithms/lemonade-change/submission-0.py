class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens=0
        fives=0
        for i in range(len(bills)):
            if bills[i]==5:
                fives+=1
            elif bills[i] ==10:
                if fives>0:
                    fives-=1
                    tens+=1
                else:
                    return False
            else:
                if tens > 0 and fives > 0:
                    tens-=1
                    fives-=1
                elif fives>2 :
                    fives-=3
                else:
                    return False
        return True                


