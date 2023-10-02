class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        cache = {}
        for i in nums:
            if i in cache.keys():
                return i
            else:
                cache[i] = None
