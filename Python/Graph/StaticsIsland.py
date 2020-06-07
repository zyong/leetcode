# @lc code=start
#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
# 
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
# 一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
# 示例 1:
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1

#
# 解题思路
# 1.深度优先搜索
#   1.线性扫描整个二维网格，如果一个结点包含 1，则以其为根结点启动深度优先搜索。
#   2.在深度优先搜索过程中，每个访问过的结点被标记为 0。计数启动深度优先搜索的根结点的数量，即为岛屿的数量。
#   3.把格子为1的自己和周边等于1的格子都设置为0

#   
# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        
        res = 0
        
        # 设置当前元素值为0，方便计算，而且对每个上下左右遇到为1的都执行一遍DFS，是之都为0
        # 这样这个岛屿就不存在了，再遇到后面的1时，就是一个新的岛屿了
        def DFS(grid, r, c):
            # terminator
            grid[r][c] = '0'

            # 检查上下左右, 注意r-1 or c -1存在等于0的情况
            if r - 1 >= 0 and grid[r - 1][c] == '1': DFS(grid, r - 1, c)
            if r + 1 < row and grid[r + 1][c] == '1': DFS(grid, r + 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == '1': DFS(grid, r, c - 1)
            if c + 1 < col and grid[r][c + 1] == '1': DFS(grid, r, c + 1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    DFS(grid, i, j)
        return res
        
# @lc code=end


        
# @lc code=end

