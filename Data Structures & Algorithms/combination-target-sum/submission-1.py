class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=0
        res=[]
        def backtrack(index,path,ans):
            if ans==target:
                res.append(path.copy())
                return
            if ans>target:
                return    
            if index==len(nums):
                return    
            backtrack(index+1,path,ans)
            path.append(nums[index])
            
            ans+=nums[index]
    
            backtrack(index,path,ans)
            
            path.pop()
            ans-=nums[index]
        backtrack(0,[],ans)
        return res