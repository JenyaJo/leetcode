class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sums = sum(nums[0:k])
        res = -10000000
        for i in range(0, len(nums)-k+1):
            if i != 0:
                sums -= nums[i-1]
                sums += nums[i+k-1]
            res = max(res, sums)
        return res / k
