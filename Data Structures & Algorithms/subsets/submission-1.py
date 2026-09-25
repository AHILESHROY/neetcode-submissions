class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(subset,index):
            if index>=len(nums):
                arr=subset.copy()
                return res.append(arr)
            subset.append(nums[index])
            bt(subset,index+1)
            subset.pop()
            bt(subset,index+1)
        bt([],0)
        return res