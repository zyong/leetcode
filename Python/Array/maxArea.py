# -*- coding:utf-8 -*-
# 11.盛最多水的容器
# https://leetcode-cn.com/problems/container-with-most-water/
# 解题思路
# 1.要满足容器体积最大，需要宽和高足够大，宽和高足够大的前提是元素本身够高
# 两个元素够远，只有在两边的元素够远，所以从两边开始寻找，然后如果要比两边
# 更大，必须柱子值更大才行，这时需要将两个计算元素里面小的那个继续往下寻找，如果
# 有更高的元素，并且乘积比前面的值更大那就是最后结果
# 2. 元素够高要求，元素值大，这个可以遍历元素知道
# 3. 元素够远要求，构成的两个元素相隔元素越多越好
# 4. 使用两个变量，分别指向数组的头和尾部，计算两个数组值
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head, tail = 0, len(height) - 1
        max_area = 0

        while head < tail:
            max_area = max(max_area, 
                           min(height[head], height[tail]) * 
                                (tail - head)
                        )
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1

        return max_area


#       res = 0
#         left, right = 0, len(lst)-1
#         while left < right:
#                 res = max(res, min(lst[left], lst[right])*(right-left))
#                 if lst[left] < lst[right]:
#                     left += 1
#                 else:
#                     right -= 1
#             return res 
            

 
if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea([1, 7, 6, 2, 5, 4, 8, 3, 7, 9]))
