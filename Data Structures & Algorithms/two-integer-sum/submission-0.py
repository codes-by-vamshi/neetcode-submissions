class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for ind, val in enumerate(nums):
            if val in hashMap:
                return [hashMap[val], ind]
            diff = target - val
            if diff not in hashMap:
                hashMap[diff] = ind