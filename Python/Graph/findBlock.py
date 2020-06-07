# -*- coding:utf-8 -*-
# 
# 
# 解题思路
# 1.扫描所有组 DFS
#   1.从第一个元素开始，一次进行遍历，
#   如果找到一个元素是black，就开始向四周找相同元素
# 
# 
class Solution(object):
    def findBlock(self, board, pos):
        """
        :type board: List[List[int]] 1 为黑色圆形 0 为无
        :type pos: List[int] 
        :rtype: number
        """
        if not board: return 0
        
        res, used = [], set()
        m, n = len(board), len(board[0])
        
        def dfs(i, j, cnt, group): 
            # 四个方向查找
            for x, y in [[-1,0], [1,0], [0,1], [0,-1]]:
                dx, dy = i + x, j+y
                if 0 <= dx < m and 0 <= dy < n:
                    if (dx,dy) not in group and board[dx][dy] == 1:
                        group.add((dx, dy))
                        used.add((dx,dy))
                        dfs(dx, dy, cnt+1, group)
            
            if group not in res:
                res.append(group)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 and (i, j) not in used:
                    used.add((i,j))
                    dfs(i, j, 1, {(i,j)})
        
        for item in res:
            # print(item)
            if tuple(pos) in item:
                print(len(item))
        
        return res

if __name__ == "__main__":
    obj = Solution()
    ret = obj.findBlock([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        (0,9)
    )
    print(ret)