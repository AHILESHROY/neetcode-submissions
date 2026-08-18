class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1, l2 = len(word1), len(word2)
        l = min(l1, l2)

        left = 0

        while left < l:
            res += word1[left]
            res += word2[left]
            left += 1

        while left < l1:
            res += word1[left]
            left += 1

        while left < l2:
            res += word2[left]
            left += 1

        return res