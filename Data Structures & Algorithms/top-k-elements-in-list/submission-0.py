class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        h=[]
        res=[]
        for i,j in c.items():
            heapq.heappush(h,[-j,i])
        while k>0:
            t=heapq.heappop(h)[1]
            res.append(t)
            k-=1    
        return res