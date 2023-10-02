class Solution:
    """Hardcore way to solve problem, without using of the binary search"""
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == int(target):
                    return [x, y]
        return []
