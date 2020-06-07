#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
# 解题思路
# 1 递归 深度优先搜索
#   1. 先遍历左括号，然后左括号减一
#   2.判断右括号是否大于左括号，如果大于就输出右括号，然后右括号减一
#   3。判断左右括号是不是都输出了，如果是保存字符串结果
# 2 递归 广度优先搜索
# 解答 https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
#   1.一层一层的遍历节点，需要记录已经添加的节点，以及还未添加的节点
#   2.需要在每层记录的节点信息里面记录left, right，括号字符串状态
# 3.DP
#   1.subproblem 就是在"()"中间和右边每次是添加"" 还是“()"的问题
#   2。DP数组 0 "" 1 "()"
#   3. DP方程  "(" + k + ")" + m， m和k为上述0 or 1 


# @lc code=start
# DP 
class Solution(object):
    def generateParenthesis(self, n):
        if n==0:
            return []
        
        all_list=[[''],['()']]
        # 已经有2个括号了，是res里面的括号，不是all_list里面的
        # 所以从2开始
        for i in range(2,n+1):
            combs=[]
            # 在这个2个括号里面再加中情况怎么加，i等于已经两边加括号的情况
            for j in range(i):
                # 从两边向中间取all_list的值，j为0 1 2 ，i-1-j为2 1 0
                # 这样两边取值相反
                # print(all_list)
                list_p=all_list[j]
                list_q=all_list[i-1-j]
                for k in list_p:
                    for m in list_q:
                        res= '('+k+')'+m
                        # 这个是把几次的情况合一，然后提供给all_list, 
                        # 因为上面循环每次就把所有上次构造的情况都输出了，
                        # 如果分散会导致每边产生的结果不一样
                        combs.append(res)
            all_list.append(combs)

        return all_list[n]

# class Solution(object):
#     def generateParenthesis(self, n):
#         def generate(p, left, right):
#             if right >= left >= 0:
#                 if not right:
#                     yield p
#                 for q in generate(p + '(', left-1, right): yield q
#                 for q in generate(p + ')', left, right-1): yield q
#         return list(generate('', n, n))


# class Solution(object):
#     def generateParenthesis(self, n):
#         def generate(p, left, right, parens=[]):
#             if left:         generate(p + '(', left-1, right)
#             if right > left: generate(p + ')', left, right-1)
#             if not right:    parens += p,
#             return parens
#         return generate('', n, n)       
        
        

# from collections import deque

# class Node(object):
#     def __init__(self, res='', left=0, right=0):
#         self.res = res
#         self.left = left
#         self.right = right


# # BFS
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         res = []
#         queue = deque()
#         queue.append(Node('', n, n))
        
#         while queue:
#             length = len(queue)
            
#             for i in range(length):
#                 node = queue.pop()
#                 if node.left == 0 and node.right == 0:
#                     res.append(node.res)
                
#                 if node.left > 0:
#                     queue.append(Node(node.res + '(', node.left - 1, node.right))
#                 if node.right > 0 and node.right > node.left:
#                     queue.append(Node(node.res + ')', node.left, node.right - 1))
                
#         return res
            
        

# DFS
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         res = []
        
#         def _generate(str, left, right):
#             # terminator
#             if left == 0 and right == 0:
#                 res.append(str)
#                 return
            
#             if left > 0: _generate(str + "(", left - 1, right)
#             if right > left: _generate(str + ")", left, right - 1)
            
#         _generate('', n, n)
#         return res


# @lc code=end

