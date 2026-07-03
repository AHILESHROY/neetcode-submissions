class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def backtrack(index,path):
            #base

            if index==len(nums):
                res.append(path.copy())
                return
            backtrack(index+1,path)

            path.append(nums[index])
            backtrack(index+1,path) 
            path.pop() 
        backtrack(0,[])
        return res
         