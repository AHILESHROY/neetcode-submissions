from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no=Counter(nums)
        print(no)
        for key,value in no.items():
            if value >1:
        
        

                return True
        return False  

        