class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1=0
        s2=0
        res=""
        min_len=min(len(word1),len(word2))
        while s1<min_len and s2<min_len:
            res+=word1[s1]+word2[s2]
            print(res)
            s1+=1
            s2+=1
        if s1<len(word1):
        
            res+=word1[s1:]
        
        if s2<len(word2):
            res+=word2[s2:]
        return res