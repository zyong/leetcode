#-*- coding:utf-8 -*-
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#
# 解题思路
# 1.DP
#   1.subproblem 本来最大收益等于本轮卖出得到的，卖出的前提是上一轮已经买入；
#   也就是说本轮的买卖结果依赖上一轮的结果，所以每一轮计算最大值就是子问题
 
#   2.DP数组 dp[k][i] k为交易次数 i为0，1 0 是持有不交易 1 卖出不持有
#   3.DP方程 

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        k = 2 #只能交易两次
        dp = [[0]*2 for _ in range(k+1)]
        for i in range(k+1):
            dp[i][1] = float('-inf')
            
        for price in prices:
            # 交易次数从最大次数开始，不可能从1次开始交易到k次，就是k逐步减少
            for i in range(k, 0, -1):
                dp[i][0] = max(dp[i][0], dp[i][1] + price)
                dp[i][1] = max(dp[i][1], dp[i-1][0] - price)
                
        return dp[-1][0]
        

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         n = len(prices)
#         if n <= 1:
#             return 0
        
#         max_list = []
#         cur, prev = 0, prices[0]
#         for i in range(1, n):
#             cur = prices[i]
#             if cur > prev :
#                 max_list.append(cur - prev)
#                 prev = cur
#             elif cur < prev:
#                 prev = cur
                
#         max_list.sort(reverse=True)
#         return max_list[0] + max_list[1]

        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    # ret = obj.maxProfit(2, [2,4,1])
    # ret = obj.maxProfit(2, [3,2,6,5,0,3])
    # ret = obj.maxProfit(2, [])
    # ret = obj.maxProfit([1,2])
    ret = obj.maxProfit([3,3,5,0,0,3,1,4])
    print(ret)