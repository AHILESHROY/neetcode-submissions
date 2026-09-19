class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap={i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)     
        op=[]
        visit,cycle=set(),set()
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False    
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)   
            visit.add(crs)    
            op.append(crs)
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return op        