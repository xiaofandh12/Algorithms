# coding=utf8
# House Robber I的升级版，分两种情况调用House Robber I，第一种情况：不包括第一个房间，第二种情况：不包括第二个房间
class Solution(object):
    def rob(self, nums):
        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return nums[0]
        # 调用rob_HouseRobberI函数需要用：self.rob_HouseRobber，也即前面要加上self
        return max(self.rob_HouseRobberI(nums[1:len(nums)]), self.rob_HouseRobberI(nums[0:len(nums)-1]))

    def rob_HouseRobberI(self, num):
        size = len(num)
        NonTake = 0
        Take = 0
        for i in range(size):
            temp = NonTake
            NonTake = max(NonTake, Take)
            Take = temp + nums[i]
        return max(NonTake, Take)

#nums = [8,3,6,15,4,9,7,10]
nums = []
print Solution().rob(nums)
