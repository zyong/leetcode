#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
# 解题思路
# 1.贪心
#   1.如果跳跃能一直跳直到跳过最后一个点，那肯定就能跳到最后一个点
#   
# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        k = 0
        for i in range(len(nums)):
            # 如果追上k了就证明k这里有个点无法往前跳了，而且中间的值都无法超过这个k点
            # 因为后面有个循环在+后面的值元素
            if i > k: return False
            # 更新能跳的最远距离，可能当前k能跳的值没有当前值大，也就是跳的更远
            # 这也就解决了跳远后最后值很小跳不出而中间值确很大问题，
            k = max(k, i + nums[i]) 
            
        return True
    
        
# @lc code=end

