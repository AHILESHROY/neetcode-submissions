class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        temp=nums.copy()
        for i in temp:
            nums.append(i)
        return nums
            
          