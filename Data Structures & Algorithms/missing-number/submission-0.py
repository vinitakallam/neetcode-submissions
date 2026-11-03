class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        diff = len(nums)
        for i in range(len(nums)):
            diff += i - nums[i]
        return diff