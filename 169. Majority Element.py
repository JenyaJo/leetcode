class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cache = {}
        major = len(nums)/2
        for i in nums:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
            if cache[i] > major:
                return i
