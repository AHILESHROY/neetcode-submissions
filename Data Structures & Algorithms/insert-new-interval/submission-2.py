class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        if not intervals: return []
        prev=intervals[0]
        l=len(intervals)
        i=1
        while i<l:
            curr=intervals[i]
            if prev[1]>=curr[0]:
                prev[1]=max(prev[1], curr[1])
                intervals.pop(i)
                l-=1
            else:
                prev=intervals[i]
                i+=1
        return intervals