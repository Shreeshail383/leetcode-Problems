class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        count = 0
        prefixSum = 0

        for n in nums:
            prefixSum += n
            if prefixSum - k in map:
                count += map[prefixSum - k]
            map[prefixSum] = map.get(prefixSum, 0) + 1
        return count
        