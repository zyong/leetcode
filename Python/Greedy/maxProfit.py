#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#
# 解题思路
# 1.贪心
#   1.只要每天有收益，就是总结果就是最好的，不用找最大的差值
# 遇到问题，要把各种情况考虑清楚
# 股票买卖策略：

# 单独交易日： 设今天价格 p1 明天价格 p2 则今天买入、明天卖出可赚取金额 p2 - p1 （负值代表亏损）。
# 连续上涨交易日： 设此上涨交易日股票价格分别为 p1, p2, ... , pn，则第一天买最后一天卖收益最大，即 pn - p1​	
#  ；等价于每天都买卖，即 pn - p1=(p2 - p1)+(p3 - p2)+...+(pn - p{n-1})。
# 连续下降交易日： 则不买卖收益最大，即不会亏钱。

# 算法流程：

# 遍历整个股票交易日价格列表 price，策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。
# 设 tmp 为第 i-1 日买入与第 i 日卖出赚取的利润，即 tmp = prices[i] - prices[i - 1] ；
# 当该天利润为正 tmp > 0，则将利润加入总利润 profit；当利润为 00 或为负，则直接跳过；
# 遍历完成后，返回总利润 profit。
# 复杂度分析：

# 时间复杂度 O(N) ： 只需遍历一次price；
# 空间复杂度 O(1) ： 变量使用常数额外空间。


# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        length = len(prices)
        
        total = 0
        for i in range(length):
            if i - 1 >= 0 and prices[i] - prices[i-1] > 0:
                total += prices[i] - prices[i-1]
            
        return total
        
        
        
        
# @lc code=end

