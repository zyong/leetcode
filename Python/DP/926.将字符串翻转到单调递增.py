# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=926 lang=python
#
# [926] 将字符串翻转到单调递增
#
# 解题思路
# 1、dp
# 题目需要将0和1组成的字符串变化为000，111，000111,这样的序列
# 需要返回经过多少次翻转变化成这个结果，同时要求递增，有两种情况
#   - 当前字符为1
#       翻转为1和dp[i][0]保持一致，翻转次数加1
#       dp[i][0] = dp[i-1][0] + 1 为1的情况，需要翻转只能是前面是0的情况
#       dp[i][1] = min(dp[i-1][1],dp[i-1][0]) 不用翻转就看那中情况的最小
#   - 当前字符为0
#       翻转为1和dp[i][1]保持一致，翻转次数加一
#       dp[i][1] = min(dp[i-1][1] + 1, dp[i-1][0] + 1) 0翻转为1可以上一个为0 or 1，取最小值
#       dp[i][0] = dp[i-1][0] 需要保持递增所以只能取0的值
# 
#   1.subproblem 
#   2.dp数组  dp[i][1] dp[i][0] 1 表示为1的情况到当前的最小翻转 为0表示到当前的值为0最小翻转
#   3.dp方程 
# 
# 
# 2.dp
# https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/solution/zhi-jian-dong-tai-gui-hua-python-4xing-dai-ma-by-k/
# 当前的字符串中“1”出现的次数用 one 表示，它的最佳解为 t 次。
# 在末尾新添加一个字符时，
# 如果该字符为“1”，出现“1”的次数为 one+1，最佳解不变仍为 t 次。
# 如果该字符为“0”，出现“1”的次数不变仍为 one，最佳解有两种情况：
# 1）将末尾“0”转为“1”，则共需要 t+1 次；
# 2）末尾“0”不变，将字符串中的“1”全部转为“0”，则共需要 one 次。
# 取两种情况的最小值，即 min(one, t + 1)。

# @lc code=start
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        t, one = 0, 0
        for c in S:
            t, one = (t, one + 1) if c == '1' else (min(one, t + 1), one)
        return t

# class Solution(object):
#     def minFlipsMonoIncr(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
        
#         if not S:
#             return 0
        
#         n = len(S)
#         dp = [[0] * 2 for _ in range(n)]
        
#         for i in range(n):
#             if S[i] == '1':
#                 dp[i][0] = dp[i-1][0] + 1
#                 dp[i][1] = min(dp[i-1][1], dp[i-1][0])
#             else:
#                 dp[i][1] = min(dp[i-1][0] + 1, dp[i-1][1] + 1)
#                 dp[i][0] = dp[i-1][0]
#         # 输出要看哪种情况最小
#         return min(dp[-1][0], dp[-1][1])
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    ret = obj.minFlipsMonoIncr("00011000")
    print(ret)