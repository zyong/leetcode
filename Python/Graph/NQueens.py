#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N皇后
#   https://leetcode-cn.com/problems/n-queens/
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#   a b c d e f g h
# 8       q         8 
# 7             q   7
# 6     q           6
# 5               q 5
# 4  q              4
# 3         q       3
# 2q                2
# 1           q     1
#   a b c d e f g h
# 上图为 8 皇后问题的一种解法。
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

# 示例:
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。


# 解题思路
# 1、回溯
#   1。由于皇后的规则，每行每列每个对角线都只能有一个皇后存在，所以每放上一个之后这行就不能放置了；
#   2. 就可以递归一下一行然后依次放上一个棋子，如果这个位置不行就到一行的下一个位置，等于是循环这行的每个格子
#   3. 当这个棋子把这行走完都没有一个位置是符合要求的，就退回这个棋子，重走上一颗棋子的循环


# @lc code=start
class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            # 如果queens的总量等于n，证明已经是全部queen的数量，就可以添加一次结果然后重新开始
            row = len(queens)
            if row==n:
                result.append(queens)
                return None
            for col in range(n):
                # 循环每一个queen,queens里面存的就是列数据，就是那些列有queen了，就不能存了
                # row-col=const和row+col=const,可以通过坐标系做
                # row-col(): x-y=0,x-y=1,x-y=2
                # row+col: x+y=0,x+y=1,x+y=2
                # 可以这样验证数据是否正确
                if col not in queens and row-col not in xy_dif and row+col not in xy_sum: 
                    DFS(queens+[col], xy_dif+[row-col], xy_sum+[row+col])
        result = []
        DFS([],[],[])
        
        # 嵌套语法糖，col是从0算起的，所以'.' * i不会影响到Q的输出
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

# class Solution:
#     def solveNQueens(self, n):
#         def could_place(row, col):
#             # hill diagonals 主斜线
#             # dale_diagonals 次斜线
#             # row + col 等于次斜线的数据，可以画个坐标轴来看，x+y=0, x+y=2, x+y=-2, x+y=-4
#             # row - col 等于主斜线的数据, x-y=0, x-y=2, x-y=-2, x-y=4
#             # 任何一项已经大于1就表示不能放置，所以直接用not就可以了
#             return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
#         def place_queen(row, col):
#             queens.add((row, col))
#             cols[col] = 1
#             hill_diagonals[row - col] = 1
#             dale_diagonals[row + col] = 1
        
#         def remove_queen(row, col):
#             queens.remove((row, col))
#             cols[col] = 0
#             hill_diagonals[row - col] = 0
#             dale_diagonals[row + col] = 0
        
#         def add_solution():
#             solution = []
#             for _, col in sorted(queens):
#                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
#             output.append(solution)
        
#         def backtrack(row = 0):
#             for col in range(n):
#                 if could_place(row, col):
#                     place_queen(row, col)
#                     # 最后一行已经成功了
#                     if row + 1 == n:
#                         add_solution()
#                     else:
#                     # 递归下一个棋子
#                         backtrack(row + 1)
#                     # 如果不能递归下去了，就证明这个棋子是错误的，就回退一个棋子
#                     remove_queen(row, col)
        
#         cols = [0] * n
        
#         # 主对角线，为什么要这么多设置，因为画图知道对角线就有那么多
#         hill_diagonals = [0] * (2 * n - 1)
#         # 次对角线
#         dale_diagonals = [0] * (2 * n - 1)
        
#         queens = set()
#         output = []
#         backtrack()
#         return output

# @lc code=end

