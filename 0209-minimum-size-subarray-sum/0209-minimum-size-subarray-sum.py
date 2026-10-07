class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        sum = 0
        min_lenght = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_lenght = min(min_lenght, right - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if min_lenght == float('inf') else min_lenght
        