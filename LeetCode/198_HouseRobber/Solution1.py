# coding=utf8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :解题方法: 动态规划,Dynamic Programming
        :解题思路: dp[N]表示在面临第N个房间时小偷可以获得的最大收益，
        面对第N间房时，小偷有两种选择:偷或不偷;
        若选择偷，那么dp[N] = nums[N-1] + dp[N-2],nums[N-1]是从第N个房间可抢到的钱;
        若选择不偷，那么dp[N] = dp[N-1];
        综上: dp[N] = max(nums[N-1] + dp[N-2],dp[N-1]).
        dp[0]为0,dp[1]为抢第一个房间可获得的最大收益,dp[2]为抢第二个房间可获得的最大收益,以此类推.

        此方法空间复杂度O(N)
        """
        size = len(nums)
        dp = [0] * (size + 1)
        if size:
            dp[1] = nums[0]
        for i in range(2,size+1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[size]

nums = [8,3,6,15,4,9,7,10]
print Solution().rob(nums)
