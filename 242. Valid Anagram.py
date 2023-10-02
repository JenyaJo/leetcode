class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        cache1 = {}
        cache2 = {}
        for i in s:
            if i in cache1:
                cache1[i] += 1
            else:
                cache1[i] = 0
        for i in t:
            if i in cache2:
                cache2[i] += 1
            else:
                cache2[i] = 0
        return cache1 == cache2