# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#
# 解题思路
# 多次买卖等于不限次数买卖，交易的最大利润等于每天都交易取最大利润

# 1.dp
#   1.subproblem 多次买卖的最大值，等于每次获利最大的和值
#   2.dp数组  不需要，只需要知道前面的最小值和最大值就可以
#   3.dp方程  f(n) = f(n-1) + f(n-2) 
# 2.贪心
#   1.只要每天有收益，就是总结果就是最好的，不用找最大的差值


# @lc code=start
# DP
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0, float('-inf')]
        for price in prices:
            pre = dp[0]
            dp[0] = max(dp[0], dp[1] + price)
            dp[1] = max(dp[1], pre - price)
        return dp[0]

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         T_i0 = 0
#         T_i1 = float('-inf')
        
#         for price in prices:
#             T_i0_old = T_i0  #只能用上一次的值
#             # 今天持有是上一次就卖出了今天还没有买入，or 上一次就买入了今天再卖出
#             # 今天不持有股票等于上一次就卖出了，今天也不买入 or 昨天买入了今天买入
#             T_i0 = max(T_i0, T_i1 + price)
#             T_i1 = max(T_i1, T_i0_old - price)
#             # print(T_i0, T_i1)
        
#         return T_i0

# 贪心
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
        
#         n = len(prices)
#         if n <= 1:
#             return 0
        
#         cur, prev,total = 0, prices[0], 0
#         for i in range(1, n):
#             cur = prices[i]
#             total += max(0, cur - prev)
#             prev = cur
        
#         return total
        

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 0:
#             return 0
#         length = len(prices)
        
#         total = 0
#         for i in range(length):
#             if i - 1 >= 0 and prices[i] - prices[i-1] > 0:
#                 total += prices[i] - prices[i-1]
            
#         return total

# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    ret = obj.maxProfit([2,4,1])
    print(ret)