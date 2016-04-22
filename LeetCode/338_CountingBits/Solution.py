# coding=utf8
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        解题思路: ans[n] = ans[n >> 1] + (n & 1)
        """
        ans = [0 for i in range(num+1)]
        for x in range(1, num+1):
            ans[x] = ans[x >> 1] + (x & 1)
        return ans

print Solution().countBits(10)
