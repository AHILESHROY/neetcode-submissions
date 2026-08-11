import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if not nums:
            return 0
        op=1
        count=1
        
        heapq.heapify(nums)
        
        t=heapq.heappop(nums)
        while nums:
            t1=heapq.heappop(nums)
            if t+1==t1:
                count+=1
                t=t1
            else:
                count=1
                t=t1
            op=max(count,op)       
        return op     