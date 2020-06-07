#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# 解题思路
# 1.并查集
#   1.找到所有的O，如果它在边界上 or 着与边界上的O相邻，就划分为一个集合
#   2.其他元素划分为另外一个集合
#   3.遍历所有节点，与边界上的集合进行比较
# 2.两步
# Phase 1: “Save” every O-region touching the border, changing its cells to ‘S’.
# Phase 2: Change every ‘S’ on the board to ‘O’ and everything else to ‘X’.
# @lc code=start
# class Solution:
#     def solve(self, board):
#         if not any(board): return

#         m, n = len(board), len(board[0])
#         save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
#         while save:
#             i, j = save.pop()
#             if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
#                 board[i][j] = 'S'
#                 save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

#         for row in board:
#                 for i, c in enumerate(row):
#                     row[i] = 'XO'[c == 'S']

# class Solution:
#     def solve(self, board):
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         f = {}
#         def find(x):
#             f.setdefault(x, x)
#             if f[x] != x:
#                 f[x] = find(f[x])
#             return f[x]
#         def union(x, y):
#             f[find(y)] = find(x)

            
            
#         if not board or not board[0]:
#             return
#         row = len(board)
#         col = len(board[0])
#         dummy = row * col
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j] == "O":
#                     if i == 0 or i == row - 1 or j == 0 or j == col - 1:
#                         union(i * col + j, dummy)
#                     else:
#                         for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                             if board[i + x][j + y] == "O":
#                                 union(i * col + j, (i + x) * col + (j + y))
#         for i in range(row):
#             for j in range(col):
#                 if find(dummy) == find(i * col + j):
#                     board[i][j] = "O"
#                 else:
#                     board[i][j] = "X"

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

# time out
# class Solution(object):
#     def solve(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
#         if not board:
#             return None
        
#         # 构建并查集，并查集初始就是自己指向自己的集合
#         def init(n):
#             p = [x for x in range(n)]
#             return p 
        
#         def find(i):
#             root = i
#             while p[root] != root:
#                 root = p[root]
#             return root
        
#         def union(i,j):
#             root1 = find(i)
#             root2 = find(j)
#             if root1 == root2: return
#             p[root1] = root2
            
#         def isConnection(i,j):
#             root1 = find(i)
#             root2 = find(j)
#             return root1 == root2
        
#         def node(i, j):
#             return i * n + j
        
#         m = len(board)
#         n = len(board[0])
#         p = init(m*n + 1)
#         edge = m * n
        
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'O':
#                     if i == 0 or j == 0 or i == m - 1 or j == n - 1:
#                         union(node(i,j), edge)
#                     else:
#                         if i > 0 and board[i-1][j] == 'O':
#                             union(node(i,j), node(i-1, j))
#                         if j > 0 and board[i][j-1] == 'O':
#                             union(node(i,j), node(i,j-1))
#                         if i + 1 < m and board[i + 1][j] == 'O':
#                             union(node(i,j), node(i+1, j))
#                         if j + 1 < n and board[i][j+1] == 'O':
#                             union(node(i,j), node(i,j+1))
        
        
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'O' and not isConnection(node(i,j), edge):
#                     board[i][j] = 'X'
#         return board     
        
# @lc code=end

