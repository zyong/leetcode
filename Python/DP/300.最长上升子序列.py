#-*- coding:utf-8 -*-
# @lc app=leetcode.cn id=   q'q lang=python
#
# [300] 最长上升子序列
#
# 解题思路
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
# dp[i]取的最长升序子序列，必须dp[i-1]为最大，然后加上nums[i]，在满足nums[i]>nums[i-1]的情况下
# 这里有个问题就是不能仅仅和前面的一个元素比较，因为前一个元素可能很小，但是在它这前构建一个上升子串了，
# 前一个元素只是继承，这个时候的比较是错误的，需要从0<=j<i 这样的范围内比较
# 1.dp
#   1.subproblem n的最长上升子序列的长度，等于n-1的最长上升子序列+1
#   2.dp数组 dp[0] = 1 添加第一个为1，就是当前数字也算
#   3.dp方程 
#   if nums[i] > nums[j] dp[i] = max(dp[j]) + 1


# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 0
        
        dp = []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
            
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    # ret = obj.lengthOfLIS([10,9,2,5,3,4])
    ret = obj.lengthOfLIS([4,10,4,3,8,9])
    print(ret)
    
