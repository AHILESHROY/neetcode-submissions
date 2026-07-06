class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        used=[False]*len(nums)
        def backtrack(path):
            
            if len(nums)==len(path):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i >0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                used[i]=True   
                path.append(nums[i]) 
                backtrack(path)
                path.pop()
                used[i]=False  
        backtrack([])
        return res              