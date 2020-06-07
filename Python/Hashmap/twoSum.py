# -*- coding:utf-8 -*-

# 解题思路
# 1、两边循环，两个指针，第一个指针指向当前元素，第二个指针依次指向数组后续元素
#  每次循环都检查值是否与要求相等
#  优点：代码逻辑简单
#  缺点: 慢
#   时间复杂度O(n^2)
#   空间复杂度O(1)
# 2、hash实现 将数组转化为hash存储，循环一遍数组计算是否在hash中，
# 需要注意hash表里面的key是数组的value，值是数组的key
#  优点：代码也很简单的，而且效率老高
#   时间复杂度O(n)，空间复杂度O(n)
#   实测 嵌套循环3000+ms，hash两遍循环30+ms
# 3、一遍hash法，这个方法能成立的原因是加法需要的两个元素，
# 当第二个元素被查询的时候第一个元素已经在hash表里面了


import collections

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length < 2:
            return False
        
        d = collections.defaultdict(int)
        for i in range(length):
            result = target - nums[i]
            if result in d and d[result] != i:
                return [d[result], i]
            d[nums[i]] = i # 要先检查是否已在hash里面，然后再进行添加操作

        return False


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         length = len(nums)
#         if not length:
#             return False
#         d = collections.defaultdict(int)

#         for i in range(length):
#             d[nums[i]] = i
        
#         for i in range(length):
#             result = target - nums[i]
#             if result in d and  d.get(result) != i:
#                 return [i, d.get(result)]
            
#         return False
                



# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i = 0
#         j = 0
#         length = len(nums)
#         while True:
#             if j >= length:
#                 return False
            
#             master = nums[j]
#             for i in range(j+1, length):
#                 iterm = nums[i]
#                 if master + iterm == target:
#                     return [j, i]
#             j = j + 1