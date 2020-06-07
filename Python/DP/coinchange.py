# -*- coding:utf-8 -*-

# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。
# 示例 1:
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 说明:
# 你可以认为每种硬币的数量是无限的。
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#
# 解题思路
# 1. 暴力：递归  指数级
# 2、广度优先遍历
#   1.就是以总金额为根，每次层迭代所有元素
#   2.将每次的中间结果保存下来，比如F(3)的计算结果存起来，可能有F(2) + F(1), 可能有F(1) + F(1) + F(1)
#   https://leetcode-cn.com/problems/coin-change/solution/ling-qian-dui-huan-by-leetcode/
#   3.最后找到层数最少结果为0的结点
#   
# 3.动态规划
#   1.单纯贪心会有错误情况，可以使用动态规划划分子问题
#   示例 [1,5,11] 15 
#  F(15) = F(15 - 11) + F(4) = F(4) + 1  = F(1)+F(1)+F(1) + 1
#  F(15) = F(15 - 5) + F(10) =  F(10) + 1
#  F(15) = F(15 - 1) + F(14) = F(14) + 1
#   2.subproblem  F(i-1)
#   3.DP数组 F(i) = min(F(i-1)) + 1 就是每种情况比较后的最小路径那个值
# 

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_val = amount + 1
        dp = [max_val] * max_val
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return  dp[amount] if dp[amount] <= amount else -1
         

        

# from collections import defaultdict
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if len(coins) == 0:
#             return -1
#         if amount == 0:
#             return 0
        
#         count = defaultdict()
        
#         def change(lastAmount):
#             if lastAmount < 0: return -1
#             if lastAmount == 0: return 0
#             if lastAmount in count: 
#                 return count[lastAmount]
            
#             minVal = float('inf')

#             for coin in coins:
#                 res = change(lastAmount - coin)
#                 if res >= 0 and res < minVal:
#                     minVal = res + 1

#             count[lastAmount] = -1 if minVal == float('inf') else minVal
#             return count[lastAmount]
        
#         change(amount)
#         return count[amount]
            
# F(s) = F(s - c) + 1
# 本层的解等于上层解 + 本层这一次的解（就是加1的意义）
# 有些解答肯定是无解的，所以F(s)部分值为无限大，就是无解
# 自下而上求解，可以逐步求出小的金额的最优解，这样就可以得到更大金额的解
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if len(coins) == 0:
#             return -1
        
#         if amount == 0:
#             return 0
        
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0
#        # 每次coin的迭代都可以对应F(s)的多个解或无解
#        # 从多个解中找到最小的那个解就是子问题的最优解
#         for coin in coins:
#             for x in range(coin, amount + 1):
#                 dp[x] = min(dp[x], dp[x - coin] + 1)
#         return dp[amount] if dp[amount] != float('inf') else -1 
        

# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         coins = sorted(coins, reverse=True)
#         N = len(coins)
#         self.ans = 99999999

#         def dfs(i = 0, total = amount, count = 0):
#             if total == 0:
#                 if count < self.ans:
#                     self.ans = count
#                 return

#             if i >= N:
#                 return

#             now = coins[i]
#             k = total / now
#             while k >= 0:
#                 if count + k >= self.ans:
#                     break
#                 dfs(i + 1, total - now * k, count + k)
#                 k -= 1

#         dfs()
#         return -1 if self.ans == 99999999 else self.ans

# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    print(obj.coinChange([186,419,83,408],6249))
    # print(obj.coinChange([1,2,5],11))


