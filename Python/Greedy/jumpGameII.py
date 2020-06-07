#-*- coding:utf-8 -*-
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#
# 解题思路
# 1.贪心算法 （要找到跳跃次数最少的解）
#   1. 就是找到每次跳跃里面跳的最远的那个
#   2. 每次都在下一次跳跃里面找跳的最远你的那个， 直到到达终点
#   3. 考虑末尾元素问题，如果到末尾会再加一次，但是不能在前面减少，因为可能直接就跳过末尾了，会少算一次
# https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/
# 2.贪心算法
# 
# @lc code=start
# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
                    
#         maxDistance = 0
#         # 指针停止点
#         end = 0
#         step = 0
#         #不算末尾元素，因为一定会到末尾就不影响
#         for i in range(len(nums) - 1):
#             maxDistance = max(maxDistance, nums[i] + i)
#             if i == end:
#                 end = maxDistance
#                 step += 1
                
#             print(i, step)
                
#         return step
    
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                    
        maxDistance = 0
        # 指针停止点，一定要用停止位置来验证之前的最大值
        end = 0
        step = 0
        #不算末尾元素，因为一定会到末尾就不影响
        for i in range(len(nums) - 1):
            maxDistance = max(maxDistance, nums[i] + i)
            if i == end:
                end = maxDistance
                step += 1
                                
        return step
        
# @lc code=end


if __name__ == "__main__":
    obj = Solution()
    print(obj.jump([2,3,1,1,4]))