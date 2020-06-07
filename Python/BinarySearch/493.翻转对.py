#
# @lc app=leetcode.cn id=493 lang=python
#
# [493] 翻转对
#
# 解题思路
# 1 暴力
#   1 两遍循环找每个翻转对 (超时)
# 2 二分查找 
#  1.bisect查找
#   2.将数组倒序，以元素的两倍值插入
#   3.后出现的元素如果插入点已有元素的后面，就是比已有元素大2倍


# @lc code=start
import bisect
class Solution:
    def reversePairs(self, nums):
        # binary search
        if nums == []: return 0
        ans, arr = 0, []
        for num in reversed(nums):
            ans += bisect.bisect_left(arr, num)
            bisect.insort(arr, num * 2) # O(N) but actually it's very fast
        return ans

# 暴力 超时
# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n < 2:
#             return 0

#         ans = set()
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[j] * 2 < nums[i]:
#                     ans.add((i,j))

#         return len(ans)
        
# @lc code=end

