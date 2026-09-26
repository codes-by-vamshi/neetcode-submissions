class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in hashMap:
                hashMap[sorted_str].append(i)
            else:
                hashMap[sorted_str] = [i]
        output = []
        for k,v in hashMap.items():
            output.append(v)
        return output