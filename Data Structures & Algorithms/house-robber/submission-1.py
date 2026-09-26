class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])
        max_till = [nums[0], max(nums[0], nums[1])]
        for i in range(2,len(nums)):
            max_till.append(max(nums[i]+max_till[i-2], max_till[i-1]))
        return max_till[-1]