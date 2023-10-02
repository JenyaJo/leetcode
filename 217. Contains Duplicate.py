class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        cache = {}
        for i in nums:
            if i in cache:
                return True
            else:
                cache[i] = 1
