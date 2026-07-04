class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        temp =[x for x in range(1,n+1)]

        def backtrack(index,path):
            if len(path)==k:
                res.append(path.copy())
                return
               
            if index==len(temp):
                return    
            backtrack(index+1,path)
            path.append(temp[index])
            backtrack(index+1,path)    
            path.pop()


        backtrack(0,[])

        return res    
