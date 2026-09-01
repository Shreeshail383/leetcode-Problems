class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)
        for j in range(n):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1
        