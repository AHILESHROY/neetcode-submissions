class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_prod=-10
        prod=1

        for i in nums:
            prod=prod*i
            mx_prod=max(mx_prod,prod)
            if prod==0:
                prod=1
        prod=1        
        for i in nums[::-1]:
            prod=prod*i
            mx_prod=max(mx_prod,prod)
            if prod==0:
                prod=1  
        return mx_prod