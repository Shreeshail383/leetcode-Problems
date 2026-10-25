class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for n in nums:
            res ^= n
        return res
