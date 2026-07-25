class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        temp=[]
        count=collections.Counter(trust[i][1] for i in range(len(trust)))
        for i in range(len(trust)):
            temp.append(trust[i][0])
        for key,value in count.items():
            if count[key]==n-1 and key not in temp:
                return key
        return -1        
