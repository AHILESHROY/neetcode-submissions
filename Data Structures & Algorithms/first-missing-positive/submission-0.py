class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=max(nums)
        if a>0:
            for i in range(1,a):
                if  i not in nums:
                    return i
            return a+1
        else:
            return 1            