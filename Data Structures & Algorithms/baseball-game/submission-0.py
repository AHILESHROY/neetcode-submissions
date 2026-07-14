class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=0
        stack=[]
        for i in operations:
            if i=="+":
                temp1=int(stack[-1])
                temp2=int(stack[-2])
                stack.append(temp1+temp2)
            elif i =="D":
                temp1=int(stack[-1])
                stack.append(2*temp1)
            elif i=="C":
                stack.pop()
            else:
                stack.append(i)            
        for i in stack:
            res+=int(i)
        return res            