# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#  
# 题目
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 解题思路
# 数据时按维升序排列的,每行也是升序
# 1. 二分查找第二维的数据
#   1.循环第一维,使二分查找变成一维的
#   2.每次循环在一行数据里面二分查找指定值,找到就返回,如果数据依据大于指定值返回无此数据

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            left = 0
            right = col
            nums = matrix[i]
            while left <= right:
                if left == right:
                    if left < col and nums[left] == target:
                        return True
                    else:
                        break   
                mid = (left + right)//2
                if nums[mid] == target:
                    return True
                
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
        
        return False
                    
                    
     
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    print(obj.searchMatrix([[1],[3]], 3))