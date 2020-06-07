# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#
# 解题思路
# 有三种情况
#   1.股票数据为空，无法交易 or k = 0不允许交易，结果都是0
#   2.股票运行多次交易，并且交易量大于股票交易日期，相当于不限次，最大利润就等于每次都进行交易的利润
#   3.股票运行有限次数，并且交易次数小于股票交易日期，就需要考虑每次交易的最大值，然后把有限次数里面出现的k个最大值相加
#   也就等于每次都取上一次交易的最大值

# 1 DP
#   1. subproblem 3个变量
#   每天的股价i，交易次数k , 买or卖的状态s 为0，1 0 不持有股票就是卖出了，1是持有股票就是买入
#   经过k次交易的最高收益等于dp[i][k][s], 最后一次的状态等于前一次的状态最大值+当天卖出的所得 or 前一次的最大值
#   
#   2. dp数组 dp[i][k][s] i = len(prices) + 1, dp[0][k][0] = 0 因为股票没开始交易结果肯定是0，同理dp[0][k][1] = 0
#   3. dp方程
#       dp[k][0] = max(dp[k][0], dp[k][1] + prices[i])
#       dp[k][1] = max(dp[k][1], dp[k-1][0] - prices[i])
#       k次交易的结果的存在要满足上一次如果没有交易这次交易了, 就是i-1的k-1次没有交易，如果上一次已经交易了k次今天就不可能交易了
# 3.DP
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems%E4%BD%9C%E8%80%85%EF%BC%9Alabuladong%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-w-5/%E6%9D%A5%E6%BA%90%EF%BC%9A%E5%8A%9B%E6%89%A3%EF%BC%88LeetCode%EF%BC%89%E8%91%97%E4%BD%9C%E6%9D%83%E5%BD%92%E4%BD%9C%E8%80%85%E6%89%80%E6%9C%89%E3%80%82%E5%95%86%E4%B8%9A%E8%BD%AC%E8%BD%BD%E8%AF%B7%E8%81%94%E7%B3%BB%E4%BD%9C%E8%80%85%E8%8E%B7%E5%BE%97%E6%8E%88%E6%9D%83%EF%BC%8C%E9%9D%9E%E5%95%86%E4%B8%9A%E8%BD%AC%E8%BD%BD%E8%AF%B7%E6%B3%A8%E6%98%8E%E5%87%BA%E5%A4%84%E3%80%82
# If k is positive infinity, then there isn't really any difference between k and k - 1 (wonder why? see my comment below), 
# which implies T[i-1][k-1][0] = T[i-1][k][0] and T[i-1][k-1][1] = T[i-1][k][1]. 
# Therefore, we still have two unknown variables on each day: T[i][k][0] and T[i][k][1] with k = +Infinity, 
# and the recurrence relations say:
# T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
# T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-1][k][0] - prices[i])
# where we have taken advantage of the fact that T[i-1][k-1][0] = T[i-1][k][0] for the second equation. 
# The O(n) time and O(1) space solution is as follows:
# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        if k > n:
            dp = [0,1]
            dp[0] = 0
            dp[1] = float('-inf')
            for price in prices:
                pre = dp[0]
                dp[0] = max(dp[0], dp[1] + price)
                dp[1] = max(dp[1], pre - price)
            return dp[0]
        
        dp = [[0] * 2 for _ in range(k+1)]
        for i in range(k+1):
            dp[i][1] = float('-inf')
            
        for price in prices:
            # 交易次数从最大次数开始，不可能从1次开始交易到k次，就是k逐步减少
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + price)
                dp[j][1] = max(dp[j][1], dp[j-1][0] - price)

        return dp[-1][0]
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    # ret = obj.maxProfit(2, [2,4,1])
    # ret = obj.maxProfit(2, [3,2,6,5,0,3])
    # ret = obj.maxProfit(2, [])
    ret = obj.maxProfit(1, [1,2])
    # ret = obj.maxProfit(2, [3,3,5,0,0,3,1,4])

    print(ret)