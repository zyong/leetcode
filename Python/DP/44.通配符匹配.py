#
# @lc app=leetcode.cn id=44 lang=python
#
# [44] 通配符匹配
#
# 解题思路
# 考虑和编辑距离一样的情况，将当做字符串来处理。
# 1 dp
#   匹配的几种情况
#    1.*匹配，有两种情况
#       1.*号没有匹配字符
#       2.*号匹配1个or 多个字符
#    2.？匹配，只匹配一个字符，结果等于上一轮匹配结果
#    3.字符匹配，等于上一轮匹配结果和本轮匹配结果
#  1.subproblem 最终匹配等于前面每轮匹配的结果 and 本轮匹配的结果
#  2.dp数组 dp[p_idx][s_idx] p_idx 模式串索引 s_idx 字符串索引
#  3.dp方程 
#    1. * 
#       dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1]
#       dp[p_idx][s_idx] = True
#    2. ?
#       dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1]
#    3. 其他字符
#       dp[p_idx][s_idx] = dp[p_idx-1][s_idx-1] and p[p_idx-1] == s[s_idx-1]

# 2 dp
#   排除不匹配的情况，
#       1.由于除*外只能单个字符匹配，如果匹配模式除*外比待匹配字符串还长，肯定是false的
#   1、subproblem 
#   本轮匹配的结果建立在上一轮的基础上，如果上一轮都不匹配，本轮也肯定匹配不上，所以最终匹配的子问题就是每轮匹配的结果  
#   *匹配所有字符包括空字符，其他字符匹配单个字符
#   
#   2、dp数组
#       dp[n+1] dp[0] = True n为s的长度，增加一个辅助空字符解决dp计算问题
#   3、dp方程
#       if p[i] == '*': dp[n] = dp[n-1] or dp[n]
#       else: dp[n+1] = dp[n] and (p[i] == s[i] or p[i] == '?')

# 3 FSM 有限状态机
# https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p%2Bs)-time
#   1.构造有限自动机
#       当前状态+输入 -> 新状态  f(s0, x) = s1
#       1.*不改变状态
#       2.其他字符的匹配前移一个状态
#   2.使用状态机来解析匹配字符串
#       1.每个字符+'*'+'?'都可以对应到一个状态到第二个状态的变化 
#       2.只有在通配符匹配的情况下才能到达最后一个状态，不会提前or达不到，如果提前or达不到都是不匹配

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        transfer = {}
        state = 0
        
        # 构造自动机
        for char in p:
            if char == '*':
                # *不改变状态
                transfer[state, char] = state
            else:
                # 单个字符匹配，状态改变为下一个状态
                transfer[state, char] = state + 1
                state += 1
        
        # 接受状态为最后的状态
        accept = state
        states = set([0])
        
        for char in s:
            # 就是说状态机里面
            states = set([transfer.get((at, token)) for at in states for token in [char, '*', '?']])
        
        return accept in states


# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         length = len(s)
#         # 如果p的长度去掉*还比s的长度长，证明不可能匹配
#         # 因为单字符和？都只能匹配一个
#         if len(p) - p.count('*') > length:
#             return False
#         # 构建dp数组，第一个是额外添加的空字符，所以用True
#         dp = [True] + [False]*length
#         for i in p:
#             if i != '*':
#                 # use the reversed builtin because for every dp[n+1] we use the previous 'dp'
#                 # 这里避免了一个问题就是使用变量cur保存当前值，然后下一次循环还要把cur赋值给pre
#                 for n in reversed(range(length)):
#                     dp[n+1] = dp[n] and (i == s[n] or i == '?')
#             else:
#                 # 第一种情况 上一轮n-1匹配那肯定本轮能匹配上
#                 # 第二种情况是上一轮已经把本轮的字符匹配上了比如*，本轮也不用匹配
#                 for n in range(1, length+1):
#                     dp[n] = dp[n-1] or dp[n]
#             # 常规初始化第一列的情况，由于添加一个元素
#             # 第一次为True 后面每轮只能模式为*才能匹配，
#             # 而且还要上一轮匹配的情况下，如果上一匹配本轮匹配也没用
#             dp[0] = dp[0] and i == '*'
#         return dp[-1]
        
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         s_len = len(s)
#         p_len = len(p)
        
#         # base cases
#         if p == s or p == '*':
#             return True
#         if p == '' or s == '':
#             return False
        
#         # init all matrix except [0][0] element as False
#         d = [ [False] * (s_len + 1) for _ in range(p_len + 1)]
#         # 0，0元素时补充的#元素，肯定是相等的
#         d[0][0] = True
        
#         # DP compute 
#         for p_idx in range(1, p_len + 1):
#             # the current character in the pattern is '*'
#             # *号匹配的情况，虽然写的是p-idx-1 因为模式串的长度是不变的，但是dp数组的长度+1，所以模式串-1就是当前串
#             if p[p_idx - 1] == '*':
#                 s_idx = 1
#                 # d[p_idx - 1][s_idx - 1] is a string-pattern match 
#                 # on the previous step, i.e. one character before.
#                 # Find the first idx in string with the previous math.
#                 # 去掉dp前值不为True的情况，前值不匹配，当前的模式也匹配不了
#                 while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
#                     s_idx += 1
#                 # If (string) matches (pattern), 
#                 # when (string) matches (pattern)* as well
#                 # *匹配到的位置的结果，第一个值设置为前值的结果，这个值是上一次匹配最后的True
#                 d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
#                 # If (string) matches (pattern), 
#                 # when (string)(whatever_characters) matches (pattern)* as well
#                 # 如果字符串还有其他字符可以匹配，*匹配的其他字符都是True
#                 while s_idx < s_len + 1:
#                     d[p_idx][s_idx] = True
#                     s_idx += 1
#             # the current character in the pattern is '?'
#             # 由于？只能匹配一个字符，所以看前值匹配的结果是什么，当前的匹配结果就是什么
#             elif p[p_idx - 1] == '?':
#                 for s_idx in range(1, s_len + 1): 
#                     d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] 
#             # the current character in the pattern is not '*' or '?'
#             # 非模式的情况，就一个个字符匹配
#             else:
#                 for s_idx in range(1, s_len + 1): 
#                     # Match is possible if there is a previous match
#                     # and current characters are the same
#                     # 匹配的原因在于前值匹配，同时当前值也匹配
#                     d[p_idx][s_idx] = \
#                     d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]  
                                                               
#         return d[p_len][s_len]

# @lc code=end

