#
# @lc app=leetcode.cn id=115 lang=python
#
# [115] 不同的子序列
#
# 解题思路
# 1.DP
#   1.subproblem 找到子序列就等于找到每个字符互相匹配的各种情况
#  模式字符的每一个在前面一个匹配的情况下能找到当前的匹配，直到结尾就表示找到一个
#   所以问题就演变为找每个模式字符在原字符里面的匹配情况

#   2.dp数组 
#   dp[i][j] i为匹配串的长度+1， j为模式串的长度+1
#   加一的原因是方便dp函数逻辑，dp[0][0] = 1 ，就是在模式串和匹配串前面加空字符。
#   数组的第一行都设为1，表示空集和所有字符匹配
#   第一列的剩余部分都设为0，表示字符在空集里面找不到子串

#   3.dp方程 如果字符相同，就要把上一个字符比较的结果和当前字符前一次比较的结果相加
#   表示当前到当前为止完整的匹配次数。
#   if s[i-1] == t[j-1] dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
#   else: dp[i][j] = dp[i][j-1]
# https://leetcode-cn.com/problems/distinct-subsequences/solution/c-9847-er-wei-dong-tai-gui-hua-10xing-yi-wei-dong-/

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        
        dp = [0] * (n+1)

        for i in range(n+1):
            dp[i] = 1
        
        for i in range(0,m):
            # 每次取第一个值
            pre = dp[0]
             # 第一列的值为0，相当于dp[1][0] = 0
            dp[0] = 0
            for j in range(0, n):
                # 先保存当前值
                cur = dp[j+1]
                if s[j] == t[i]:
                    # 用前值dp[j] + 上一轮的值pre
                    dp[j+1] = dp[j] + pre 
                else:
                    dp[j+1] = dp[j]
                # 将当前值赋值给pre下一次计算使用
                # 相当于dp[i-1][j-1]的值
                pre = cur
        return dp[-1]
        
        

# class Solution(object):
#     def numDistinct(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: int
#         """
#         n = len(s)
#         m = len(t)
#         dp = [[0] * (n+1) for _ in range(m+1)]
        
#         for i in range(n):
#             dp[0][i] = 1
        
#         for j in range(1,m):
#             dp[j][0] = 0
        
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if t[i-1] == s[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
#                 else:
#                     dp[i][j] = dp[i][j-1]
                    
#         return dp[-1][-1]
        
        
        
# @lc code=end

