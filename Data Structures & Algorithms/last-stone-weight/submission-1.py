import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(max_heap:=[-x for x in stones])
        while len(max_heap)>1:
            s1=-heapq.heappop(max_heap)
            s2=-heapq.heappop(max_heap)
            if s2<s1:
                heapq.heappush(max_heap,s2-s1)
            print(max_heap)
        max_heap.append(0)
        return abs(max_heap[0])

