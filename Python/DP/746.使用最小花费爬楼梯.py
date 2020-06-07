#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 使用最小花费爬楼梯
#

# 解题思路
# DP
# 1.subproblem 爬到最高层的方法只有从n-1层 or n-2层来的，
# 每次可以走1step or 2step
# 2.DP数组  dp[n+1] 加1的原因是要上到顶层，但是顶层不在cost里面
# 这里cost也要加个顶层的值
# 3.DP方程 dp[i] = min(dp[i-1], dp[i-2]) + cost[i]


# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 一种是小于3的情况
        n = len(cost)
        if 1 < n < 3:
            return min(cost[0], cost[1])
        elif n == 0:
            return 0
        
        
        # 大于等于3
        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
            
        return dp[n]
        
        
        
# @lc code=end