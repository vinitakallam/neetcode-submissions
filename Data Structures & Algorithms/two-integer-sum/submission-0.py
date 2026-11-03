class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sorted(nums)
        diffhash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffhash:
                return [diffhash[diff], i]
            else: 
                diffhash[n] = i