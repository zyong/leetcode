# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
# 官方题解
# https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode/
# 
# 
# 解题思路
# 第一种情况，)前面直接就是(，可以+2 + dp[i-1]
# 第二种情况，)后面是)，就要判断前一个)的前面是不是(使前面一组为一对，如果是就再判断这一对前面是不是
# 1.动态规划
#   1.subproblem  
# 最长有效括号，如果本次括号有效，就看上一次的括号是否也有效，有效就相加"()(()"
#   2.DP数组 与字符串长度相同 dp[n]
#   3.DP方程 
#   dp[i] = 2 + dp[i-2]



# @lc code=start        
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        maxans = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i - 2 >= 0:
                        dp[i] = 2 + dp[i-2] 
                    else:
                        dp[i] = 2
                        # i > 上次的已经匹配的数量，同时在上一次匹配前有'('
                elif i - dp[i-1] > 0 and s[i-dp[i-1] - 1] == '(':
                    # 在前一个匹配项前还有元素，需要把前面的匹配也加上
                    if i-dp[i-1] >= 2:
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                    # 在前面一个匹配项前面已经没有足够匹配的括号了，就前一个匹配项+2
                        dp[i] = dp[i-1] + 2
                maxans = max(dp[i], maxans) 
        return maxans
        
        
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    # ret = obj.longestValidParentheses("(()")
    # ret = obj.longestValidParentheses("()(())")
    ret = obj.longestValidParentheses("())")
    print(ret)
    
    