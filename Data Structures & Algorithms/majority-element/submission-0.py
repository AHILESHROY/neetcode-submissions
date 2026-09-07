from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        m=0
        res=0
        for key,values in freq.items():
            if values>m:
                m=values
                res=key
        return res        