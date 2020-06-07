# -*- coding:utf-8 -*-
# 84. 柱状图中最大的矩形
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

# 解题思路
# 1.循环
#   1.两个指针,一个在头一个在尾,此时的width最大,height不一定最大
#   然后不断移动两个指针里面矮的那个,知道找到一个高的柱子来替换,比较柱子产生面积大小
#   2.在两边时宽最大,内部柱子要产生最大的面积只有高比两边高才行,这个时候移动高度小的指针去找更高的元素
#   才能找到最大面积
# 复杂度分析
# 时间复杂度：O(n^2)。 需要枚举所有可能的柱子对。
# 空间复杂度：O(1) 。不需要额外的空间。
# 2.分治
#   1.先算出最小的高度,然后以所有柱子的宽度算出面积
#   2.然后以最小的高度为中心,划分左边和右边的柱子,重复上面的计算过程
#   3. 最后比较大小
# 复杂度分析
# 时间复杂度：
# 平均开销：O(nlogn)
# 最坏情况：O(n^2)。如果数组中的数字是有序的，分治算法将没有任何优化效果。
# 空间复杂度：O(n)。最坏情况下递归需要 O(n) 的空间。



class Solution(object):
    def calculateArea(self, heights, start, end):
        if start > end:
            return 0
        minindex = start
        for i in range(start, end + 1):
            if heights[minindex] > heights[i]:
                minindex = i
        return max(heights[minindex] * (end - start + 1), max(
            self.calculateArea(heights, start, minindex - 1), 
            self.calculateArea(heights, minindex + 1, end))
                   )
    
    
    def largestRectangleArea(self, heights):
        return self.calculateArea(heights, 0, len(heights) - 1)
    


# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         if len(heights) == 0:
#         return
#         """
#         if len(heights) == 0:
#             return 0
        
#         left, right = 0, len(heights) - 1
#         maxArea = 0
        
#         for i in range(left, right + 1):
#             height = float('inf')
#             for j in range(i, right + 1):
#                 width = j - i + 1
#                 height = min(heights[j], height)
#                 maxArea = max(maxArea, width * height)
        
#         return maxArea
 

# import sys
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int

#         """
        
#         i, j, k = 0, 0, 0
#         length = len(heights)
#         if length < 2 and length > 0:
#             return heights[0]
#         if length == 0:
#             return 0

#         maxArea = 0
  
        
#         for i in range(0, length):
#             for j in range(length - 1, i, -1):
#                 minVal = sys.maxsize
#                 if 0 in heights[i:j]:
#                     continue
#                 for k in range(i, j + 1):

#                     minVal = min(heights[k], minVal)

#                 maxArea = max(maxArea, (j - i + 1) * minVal)
#                 print minVal, i, j
            
#         return maxArea        

if __name__ == "__main__":
    obj = Solution()
    print(obj.largestRectangleArea([0,2,0]))