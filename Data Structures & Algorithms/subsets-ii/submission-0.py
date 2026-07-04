class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def bt(index,path):
            if index==len(nums):
                if path not in res:     
                    res.append(path[:])
                return
            if index>len(nums):
                return
            
            bt(index+1,path)
            path.append(nums[index])
            bt(index+1,path)
            path.pop()
        bt(0,[])
        return res    
