#
# @lc app=leetcode.cn id=836 lang=python
#
# [836] 矩形重叠
#
# 解题思路
# 1.判断两个图形是否重叠，就看各个边是否相遇
# 两个矩形 r1 r2
#   1.如果R2在左边 r2.x2 < r1.x1
#   2.如果R2在上面 r2.y1 > r1.y2
#   3.如果R2在右边 r2.x1 > r1.x2
#   4.如果R2在下面 r2.y2 < r1.y1

# @lc code=start
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        r1x1,r1y1,r1x2,r1y2 = rec1
        r2x1,r2y1,r2x2,r2y2 = rec2
        
        return not (r2x2 < r1x1 or\
            r2y1 > r1y2 or\
            r2x1 > r1x2 or\
            r2y2 < r1y1)
                
        
# @lc code=end

