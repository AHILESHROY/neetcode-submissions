class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=min(len(word1),len(word2))
        i=0
        res=""
        while i<length:
            res+=word1[i]+word2[i]
            i+=1
        res+=word1[i:]
        res+=word2[i:]    
        return res