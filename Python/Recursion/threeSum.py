# -*- coding:utf-8 -*-
# 15.三数之和
# https://leetcode-cn.com/problems/3sum/
# 解题思路：
# .暴力求解为O(N³)时间复杂度，可以通过双指针动态消去无效解来优化。
# .双指针法铺垫：先将给定nums排序，复杂度O(NlogN)
# .双指针思路：固定 3 个指针中最左（最小）数字的指针 k，
    # 双指针 i，j 分设在数组索引 (k, len(nums))(k,len(nums)) 两端，
    # 通过双指针交替向中间移动，记录对于每个固定指针 k 的所有满足
    # nums[k] + nums[i] + nums[j] == 0 的 i,j 组合：
    # 1.当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，
    # 即 3 个数字都大于 0 ，在此固定指针 k 之后不可能再找到结果了。
    # 2.当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：
    # 因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
    # 3.i，j 分设在数组索引 (k, len(nums))(k,len(nums)) 两端，
    # 当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
    #     . 当s < 0时，i += 1并跳过所有重复的nums[i]；
    #     . 当s > 0时，j -= 1并跳过所有重复的nums[j]；
    #     . 当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，
    # 防止记录到重复组合。

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
       

        """
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):  # [8]
            if nums[i] > 0:
                break  # [7]
            if i > 0 and nums[i] == nums[i-1]:
                continue  # [1]

            l, r = i+1, length-1  # [2]
            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if total < 0:  # [3]
                    l += 1
                elif total > 0:  # [4]
                    r -= 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r-1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res
