#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
# 二分查找
# 1.找旋转后的最大位置，就是不断分两半找一个点比前面小，比后面小的index
#   1.使用递归操作
#   2.使用循环操作


# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        def binary(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2
            if mid - 1 >= 0 and mid + 1 < len(nums):
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:     
                    return mid + 1
                
            left_mid = binary(left, mid)
            right_mid = binary(mid + 1, right)
            return right_mid if nums[left_mid] > nums[right_mid] else left_mid
            
            
        
        mid = binary(0, len(nums) - 1)
        return nums[mid]

# @lc code=end

