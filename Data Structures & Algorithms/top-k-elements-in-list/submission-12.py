class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        first_ind = 0
        hashMap = {}
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[first_ind]:                
                continue
            count = i - first_ind
            if count in hashMap:
                hashMap[count].append(sorted_nums[first_ind])
            else:
                hashMap[count] = [sorted_nums[first_ind]]
            first_ind = i
        print(first_ind)
        if first_ind != len(sorted_nums) - 1:
            count = len(sorted_nums) - first_ind
            if count in hashMap:
                hashMap[count].append(sorted_nums[first_ind])
            else:
                hashMap[count] = [sorted_nums[first_ind]]
        else:
            if 1 in hashMap:
                hashMap[1].append(sorted_nums[first_ind])
            else:
                hashMap[1] = [sorted_nums[first_ind]]
        counts = sorted(list(hashMap.keys()))[::-1]
        print(hashMap)
        output = []
        for i in counts:
            output+=hashMap[i]
            if len(output) >= k:
                return output[:k]