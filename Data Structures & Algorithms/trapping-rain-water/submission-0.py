class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        left,right=0,len(height)-1
        l_max=0
        r_max=0
        while left < right:
            if height[left] < height[right]:
                if l_max<=height[left]:
                    l_max=height[left]
                else:
                    water+=l_max-height[left]
                left+=1    
            else:
                if r_max<=height[right]:
                    r_max=height[right]
                else:
                    water+=r_max-height[right]
                right-=1
        return water        






        
                


        