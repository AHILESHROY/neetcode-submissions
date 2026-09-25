class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==n:
            return [[i for i in range(1,n+1)]]
        arr=[i for i in range(1,n+1)]
        op=[]
        def bt(res,index):
            if index>=n :
                
                if len(res)==k :
                    a=res.copy()
                    return op.append(a)
                return    
            res.append(arr[index])
            bt(res,index+1)
            res.pop()
            bt(res,index+1)

        bt([],0)
        return op