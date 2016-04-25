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

        此方法空间复杂度O(1)
        """
        size = len(nums)
        Take = 0 #抢当前房间获得的收益
        NonTake = 0 #不抢当前房间获得的收益
        for i in range(size):
            temp = NonTake
            #在一个循环开始的时候，Take表示抢了前一个房间获得的收益，NonTake表示未抢前一个房间获得的收益；
            #下面要算的是不抢当前房间或抢当前房间所能获得的收益
            #不抢当前房间可获得的收益，为前一个房间抢或没抢的最大值
            #NonTake和dp[N]不一样，dp[N]是到第N个房间小偷可获得的最大收益，NonTake为小偷不抢第N个房间获得的收益
            NonTake = max(Take, NonTake)
            Take = temp + nums[i] #抢了当前房间的收益，为不抢前一个房间获得的收益加上抢了当前房间获得的收益
        return  max(NonTake, Take)

nums = [8,3,6,15,4,9,7,10]
print Solution().rob(nums)
