"""https://leetcode.com/problems/move-zeroes"""
def moveZeroes(nums: List[int]) -> None:
    return nums.sort(key=lambda x: x == 0)
