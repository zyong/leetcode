#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

# 注意你不能在买入股票前卖出股票。

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

# 解题思路
#  只允许完成依次交易
# 1.DP
#   1.subproblem 最大利润只会出现在最大利差之间，所以要找最大利差 
#       1.就是要找两个点，一个点是高点前的最低点，一个点是下一个低点前的最高点
#       2.比较每次这样的利差，看那个最大
#   2.dp数组 一个记录最小值，一个记录最大值
#   3.dp方程 f(i) = f(max) - f(min)
# 2。DP
#   1.suproblem 这一次不交易和这一次交易的最大值
#   2.dp方程
# Case I: k = 1
# For this case, we really have two unknown variables on each day: T[i][1][0] and T[i][1][1], and the recurrence relations say:
# T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
# T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) = max(T[i-1][1][1], -prices[i])
# @lc code=start

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        T_i0 = 0
        T_i1 = float('-inf')
        
        for price in prices:
            T_i0 = max(T_i0, T_i1 + price)
            T_i1 = max(T_i1, - price)
            print(T_i0, T_i1)
        
        return T_i0

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
        
#         n = len(prices)
#         if n == 0: return 0
        
#         prev, cur, total = prices[0], 0, 0 
        
#         for i in range(1, n):
#             cur = prices[i]
#             if prev > cur:
#                 prev = cur
#             else:
#                 total = max(total, cur - prev)
#         return total           
        
        
# @lc code=end

