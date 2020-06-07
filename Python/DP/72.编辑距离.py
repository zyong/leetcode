#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# 解题思路
# 每个字符的变化存在6中情况
#   1.A单词增加一个字符
#   2.B单词增加一个字符
#   3.A单词减少一个字符
#   4.B单词减少一个字符
#   5.A单词替换一个字符
#   6.B单词替换一个字符
# 由于题目是要变化为同一个单词，所以
#   1.A单词增加一个字符和B单词减少一个字符相同；
#   2.A单词减少一个字符和B单词增加一个字符相同；
#   3.A单词替换一个字符和B单词替换一个字符相同；
# 所以整个变化改为3中情况
#   1.A单词增加一个字符
#   2.B单词增加一个字符（第一中情况A单词少，第二种是B单词少）
#   3.A单词替换一个字符（字符数量一致，只需要替换字符就可以满足）
# https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
# 1.dp
#   1.subproblem 整个单词的最小变化次数等于单词的一部分字符的最小变化次数
#   2.dp数组    dp[i][j] i为A单词数量+1，j为B单词数量+1 加一是为解决dp计算问题，在A和B的前面加上空字符，
#   保证i-1和j-1的计算是正确的，同时空字符不会影响整个变化次数
#   dp[i][j-1] 为A的前i个字符，B的前j-1个字符的子问题，就是在A的第i个字符，添加一个字符就可以是A和B相等，
#   最小变化为dp[i][j-1] + 1
#   dp[i-1][j] 为A的前i-1个字符，B的前j个字符的子问题，就是在B的第j个字符，添加一个字符就可以让A和B相等
#   最小变化为dp[i-1][j] + 1
#   dp[i-1][j-1] 为A的前i-1个字符和B的前j-1个字符，再替换一个字符就可以满足两个单词相等
#   3.dp方程    1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        # 边界情况，一个字符为空
        if m*n == 0:
            return n+m
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 初始化值
        for j in range(1, n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            dp[i][0] = i
            
        # 第0个字符是辅助字符，不需要改变
        dp[0][0] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    # 当两个字符相同的时候，
                    # i和j-1的位置word1已经在这个字符上，word2还差一个，所以要加1
                    # i-1和j的位置word2已经在这个位置上，word1还差一个，所以要加1
                    # i-1和j-1的位置word1和word2已经变化为相同结果，所以不用变化
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1])
                else:
                    # 当两个字符不同的时候，每个结果都需要一次变化来生成正确的结果
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

        
        return dp[-1][-1]
        
        
        
        
        
        
# @lc code=end

if __name__ == "__main__":
    pass