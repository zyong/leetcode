#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
# 题目理解，回文子串，就是在大的回文串下有多少个小回文串

# 解题思路
# 1。dp
#   1.subproblem 找到每个子结构，就是每个字符串取值范围，判断里面是否有回文串
#   2. dp数组 dp[i][j] = True/False i 左边元素的idx j是右边元素的idx
#   dp[i][j] 表示这个值是否是回文
#   3. dp方程 dp[i][j] = True if dp[i-1][j+1] and i-j >2
# 2.分治
#   1。循环遍历从左到右，然后逐步分开两边看是否为回文
# 3.从中心往两侧延伸
#  按中心位置，只有字母和空隙吧，字母N个，空隙N-1，一共2N-1
# https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode/
# 

# @lc code=start
class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        #  按中心位置，只有字母和空隙吧，字母N个，空隙N-1，一共2N-1
        for center in range(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

# class Solution(object):
#     def countSubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """    
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         count = 0
        
#         for i in range(n):
#             for j in range(i, -1, -1):
#                 if s[i] == s[j]:
#                     if i - j <= 2 or (i - j > 2 and dp[i-1][j+1]):
#                         count += 1
#                         dp[i][j] = True

#         return count


# class Solution(object):
#     def countSubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not s:
#             return 0
        
#         def countPalindrem(left, right):
#             count = 0
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 count += 1
#                 left -= 1
#                 right +=1
#             return count
        
#         count = 0
#         for i in range(len(s)):
#             # 回文串为奇数的情况下
#             # 每个字符都单独是一个回文子串
#             # 从这个字符扩展开，如果能找到相等的，也是回文子串
#             # 由于每个位置的相同回文子串都不算相同，所以可以遍历来找
#             count += countPalindrem(i, i)
#             # 回文串为偶数的情况下
#             count += countPalindrem(i, i+1)
        
#         return count
        
# @lc code=end

