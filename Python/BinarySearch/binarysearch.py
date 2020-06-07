# 解题思路
# 1.使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
#   1.由于部分有序，只要找到nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]
#  
class Solution(object):
    def binarySearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def binary(left, right):
            if left == right:
                return -1
            
            mid = (left + right) // 2
            if mid - 1 >= 0 and mid + 1 < len(nums):
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:     
                    return mid
                
            left_mid = binary(left, mid)
            right_mid = binary(mid + 1, right)
            return left_mid if left_mid > 0 else right_mid
            
            
        
        return binary(0, len(nums) - 1)
        
         
if __name__ == "__main__":
    obj = Solution()
    print(obj.binarySearch([ 1, 2, 3, 4, 5, 6, 7, 8]))