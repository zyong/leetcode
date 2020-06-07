# -*- coding:utf-8 -*-

class Solution(object):
    def findMin(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        ans = []
        while left < right:
            mid = (left + right) / 2
            ans.append(mid)
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    
if __name__ == "__main__":
    obj = Solution()
    # ret = obj.findMin([10, 14, 19, 26, 27, 31, 33, 35, 42, 44], 31)
    ret = obj.findMin([2,4,6,8, 10, 12, 14, 16, 18,20, 22], 16)
    print(ret)