#
# @lc app=leetcode.cn id=289 lang=python
#
# [289] 生命游戏
#
#解题思路
# 1.使用副本
# 判断每个格子8个方向的4个状态结果和
#   1.如果活的少于2个，记录i,j位置细胞死亡
#   2.如果活的有2|3个，记录i,j位置细胞活
#   3.如果活的细胞超过3个，记录i,j位置细胞死亡
#   4.如果死细胞周围正好有3个活细胞，则死细胞复活
# 复制一个board，作为数据来源，计算其结果，然后修改board的值
# 2.不适用副本
#   1.需要对board进行染色，活细胞死了使用-1，死细胞活了使用2
# @lc code=start

# 不复制副本
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # 遍历面板每一个格子里的细胞
        for row in range(rows):
            for col in range(cols):

                # 对于每一个细胞统计其八个相邻位置里的活细胞数量
                live_neighbors = 0
                for neighbor in neighbors:

                    # 相邻位置的坐标
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 查看相邻的细胞是否是活细胞
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # 规则 1 或规则 3 
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 代表这个细胞过去是活的现在死了
                    board[row][col] = -1
                # 规则 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 代表这个细胞过去是死的现在活了
                    board[row][col] = 2

        # 遍历 board 得到一次更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


# 复制一个副本
# class Solution(object):
#     def gameOfLife(self, board):
#         """
#         :type board: List[List[int]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
#         if not board:
#             return 
        
#         m = len(board)
#         n = len(board[0])

#         new = [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 new[i][j] = board[i][j]

#         for i in range(m):
#             for j in range(n):
#                 live_cells = 0
#                 dead_cells = 0
#                 for x,y in [(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(0,-1)]:
#                     if 0 <= x+i < m and 0 <= y+j < n:
#                         i0 = x+i
#                         j0 = y+j
#                         if new[i0][j0] == 1:
#                             live_cells += 1
#                         else:
#                             dead_cells += 1
#                 if live_cells > 3 or live_cells < 2: board[i][j] = 0
#                 if (new[i][j] == 0 and live_cells == 3) or \
#                      (new[i][j] == 1 and live_cells in [2,3]): 
#                     board[i][j] = 1
        
# @lc code=end

