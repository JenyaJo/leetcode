class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        start = 0
        end = len(nums) - 1
        middle = len(nums) // 2
        if nums[start] < nums[middle] and nums[middle] < nums[end]:
            return nums[start]
        elif nums[start] < nums[middle] and nums[middle] > nums[end]:
            return Solution.findMin(self, nums[middle:end+1])
        elif nums[start] > nums[middle] and nums[middle] < nums[end]:
            return Solution.findMin(self, nums[start:middle+1])
        else:
            return nums[end]
