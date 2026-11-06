class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        ele = None
        for i in range(len(nums)):
            if count == 0:
                count = 1
                ele = nums[i]
            elif nums[i] == ele:
                count += 1
            else:
                count -= 1
        
        count1 = 0
        for i in range(len(nums)):
            if nums[i] == ele:
                count1 += 1
        if count1 > len(nums) / 2:
            return ele
        return -1