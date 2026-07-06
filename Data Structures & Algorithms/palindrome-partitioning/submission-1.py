class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        res=[]    
        def bt(path,start):
            if len(s)==start:
                res.append(path[:])
                return 
            for end in range(start,len(s)):
                if is_pal(start,end):
                    path.append(s[start:end+1])
                    bt(path,end+1)
                    path.pop()

        bt([],0)            
        return res