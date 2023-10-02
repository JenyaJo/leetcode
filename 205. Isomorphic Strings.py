class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cacheTS, cacheST = {}, {}
        for i in range(len(s)):
            if t[i] not in cacheST:
                cacheST[t[i]] = s[i]
            if s[i] not in cacheTS:
                cacheTS[s[i]] = t[i]
            if cacheTS[s[i]] != t[i] or cacheST[t[i]] != s[i]:
                return False
        return True
