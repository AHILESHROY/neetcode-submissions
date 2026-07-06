class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        def backtrack(path):
            if len(nums)==len(path) and path not in res:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True   
                path.append(nums[i]) 
                backtrack(path)
                path.pop()
                used[i]=False  
        backtrack([])
        return res              