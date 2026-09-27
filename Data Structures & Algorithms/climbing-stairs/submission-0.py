class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways_tillNow = [1,2]
        for i in range(2,n):
            ways_tillNow.append(ways_tillNow[-1]+ways_tillNow[-2])
        return ways_tillNow[-1]