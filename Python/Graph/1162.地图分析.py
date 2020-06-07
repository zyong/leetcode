#
# @lc app=leetcode.cn id=1162 lang=python
#
# [1162] 地图分析
#
# 解题思路
# BFS
# 1.循环grid里面的0
# 2.然后对0的格子进行四周扩散，找为1的格子
# 3.找到一个为1的格子就计算曼哈顿距离
# 4.保留最近的一个距离
# 5.中间会有很多重复，需要memory
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/solution/li-qing-si-lu-wei-shi-yao-yong-bfs-ru-he-xie-bfs-d/

# @lc code=start

        
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        queue = []
        # 将所有的陆地格子加入队列
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
        # 如果我们的地图上只有陆地或者海洋，请返回 -1。
        if len(queue) == 0 or len(queue) == N * N:
            return -1

        distance = -1
        while len(queue) > 0:
            distance += 1
            # 这里一口气取出 n 个结点，以实现层序遍历
            n = len(queue)
            for i in range(n):
                r, c = queue.pop(0)
                # 遍历上边单元格
                if r-1 >= 0 and grid[r-1][c] == 0:
                    grid[r-1][c] = 2
                    queue.append((r-1, c))
                # 遍历下边单元格
                if r+1 < N and grid[r+1][c] == 0:
                    grid[r+1][c] = 2
                    queue.append((r+1, c))
                # 遍历左边单元格
                if c-1 >= 0 and grid[r][c-1] == 0:
                    grid[r][c-1] = 2
                    queue.append((r, c-1))
                # 遍历右边单元格
                if c+1 < N and grid[r][c+1] == 0:
                    grid[r][c+1] = 2
                    queue.append((r, c+1))

        return distance


# class Solution(object):
#     def maxDistance(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         if not grid or not grid[0]:
#             return -1

#         m, n = len(grid), len(grid[0])
#         ans = []

#         def bfs(i1, j1):
#             used = {}
#             q = []
#             q.append((i1,j1,0))
#             while q:
#                 i, j, step = q.pop()
#                 for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
#                     if 0 <= x+i < m and 0 <= y+j < n:
#                         a = x + i
#                         b = y + j
#                         if (a,b) in used:
#                             continue
#                         q.append((a,b,step+1))
#                         used[(i1,j1)] = True
#                         if grid[a][b] == 1:  return step + 1
                       
#             return -1

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     ans.append(bfs(i,j))

#         return max(ans)
        
# @lc code=end

