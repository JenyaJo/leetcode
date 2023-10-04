class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        for num in range(1, len(nums)):
            result[num] = result[num - 1] * nums[num - 1]
        right = nums[-1]
        for num in range(len(nums) - 2, -1, -1):
            result[num] *= right
            right *= nums[num]
        return result
