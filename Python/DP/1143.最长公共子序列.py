#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#
# 解题思路
# 1.递归
#   1.对第一个字符串的每个字符取和不取构造出子序列
#   2.在第二个字符串中查找，如果找到就是记录+1
# 时间复杂度： 2^N
#
# 2.动态规划  最长公共子序列
#   1.subproblem 
#   就是当前字符串的LCS等于子串的LCS+1，以及子串的LCS中最大的一个值
#   2.dp数组
#   dp[i][j] i 是text1的长度+1，j是text2的长度+1
#   长度+1是提供0，0两个空字符串给dp方程使用，就是在这个位置的时候不会有任何的有效值
#   3.dp方程
#   if s1[-1] == s2[-1] LCS(s1,s2) = LCS(s1-1, s2-1) + 1
#   if s1[-1] != s2[-1] LCS(s1,s2) = max(LCS(s1-1, s2), LCS(s1, s2-1))

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        
        
        

# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         m, n = len(text1), len(text2)
        
#         # 补充一列和一行空字符串
#         dp = [[0] * (n+1) for _ in range(m+1)]
        
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     # 1、取斜对角值，就是当前的字符与上一个肯定不同
#                     # 所以斜对角的值就是到当前的最大lcs长度
#                     # 2、为什么dp[i-1][j-1]要用j-1,不是j，
#                     # 避免一行里面有两个相同的，会出现取两次的情况，而最长子串只出现一次
#                     # 示例  "jdkblakcl" "kdjekm"
#                     dp[i][j] = dp[i-1][j-1] + 1
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         return dp[-1][-1]

# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         # 边界情况
#         if not text1 or not text2:
#             return 0
        
#         s1 = text1
#         s2 = text2
        
#         def dp(i, j):
#             if i == -1 or j == -1:
#                 return 0
#             if s1[i] == s2[j]:
#                 return dp(i-1, j-1) + 1
#             else:
#                 return max(dp(i-1, j), dp(i, j-1)) 
#         return dp(len(s1) - 1, len(s2) - 1)
            
        
            
# @lc code=end

