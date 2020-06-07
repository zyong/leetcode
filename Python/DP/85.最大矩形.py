#
# @lc app=leetcode.cn id=85 lang=python
#
# [85] 最大矩形
#
# 解题思路
# 1.dp
#   1. subproblem 每个格子能够达到的最大面积，等于当前格子所在列最大宽*最大高
#   2. dp数组 dp[i][j] i 表示行 j表示列 dp表示这个格子的最大有效宽度
#   3. dp方程
#       width = dp[i][j] = dp[i][j-1] + 1 if matrix[i][j] == 1 else 1
#       width = min(width, dp[k][j])
#       area = max(width * (i-k+1), maxarea)
# 复杂度分析
# 时间复杂度 : O(N^2M)。由于需要遍历同一列中的值，计算每个点对应最大面积需要O(N)。
# 对全部N * M个点都要计算，因此总共O(N) * O(NM) = O(N^2M)。
# 空间复杂度 : O(NM)。我们分配了一个等大的数组，用于存储每个点的最大宽度。

# 2.dp
# 给定一个最大矩形，其高为 h， 左边界 l，右边界 r，
# 在矩形的底边，区间 [l, r]内必然存在一点，其上连续1的个数（高度）<=h。
# 若该点存在，则由于边界内的高度必能容纳h，以上述方法定义的矩形会向上延伸到高度h，再左右扩展到边界 [l, r] ，于是该矩形就是最大矩形。
# 若不存在这样的点，则由于[l, r]内所有的高度均大于h，可以通过延伸高度来生成更大的矩形，因此该矩形不可能最大。
# 综上，对于每个点，只需要计算h， l，和 r - 矩形的高，左边界和右边界。
# 使用动态规划，我们可以在线性时间内用上一行每个点的 h，l，和 r 计算出下一行每个点的的h，l，和r。


# @lc code=start
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        
        maxarea = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 数据的格式要注意，必须是‘0’字符
                if matrix[i][j] == '0': continue
                
                # update width
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                
                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    # 到这层最大的宽度，有些层中间为0，宽度就会缩小
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        
        return maxarea

        
            
        
        
        
        
# class Solution(object):
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         if not matrix: return 0

#         m = len(matrix)
#         n = len(matrix[0])

#         left = [0] * n # initialize left as the leftmost boundary possible
#         right = [n] * n # initialize right as the rightmost boundary possible
#         height = [0] * n

#         maxarea = 0

#         for i in range(m):

#             cur_left, cur_right = 0, n
#             # update height
#             for j in range(n):
#                 if matrix[i][j] == '1': height[j] += 1
#                 else: height[j] = 0
#             # update left
#             for j in range(n):
#                 if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
#                 else:
#                     left[j] = 0
#                     cur_left = j + 1
#             # update right
#             for j in range(n-1, -1, -1):
#                 if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
#                 else:
#                     right[j] = n
#                     cur_right = j
#             # update the area
#             for j in range(n):
#                 maxarea = max(maxarea, height[j] * (right[j] - left[j]))

#         return maxarea

# @lc code=end

