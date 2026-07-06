class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        nums.sort(reverse=True)
        target=total//k
        used=[False]*len(nums)
        subsetsum=0
        def bt(subsetsum,k,index):
            if k==0:
                return True

            if subsetsum==target:
                return bt(0,k-1,0)
            for i in range(index,len(nums)):
                if used[i] or subsetsum+nums[i]>target:
                    continue
                used[i]=True    
                if bt(subsetsum+nums[i],k,i+1):
                    return True
                used[i]=False
            return False 
        return bt(0,k,0)

