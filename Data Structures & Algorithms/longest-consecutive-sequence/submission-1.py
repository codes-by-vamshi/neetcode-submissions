class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 0
        maxi = [0,1]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                maxi[1] += 1
            else:
                maxi[0] = max(maxi[0], maxi[1])
                maxi[1] = 1
        return max(maxi)