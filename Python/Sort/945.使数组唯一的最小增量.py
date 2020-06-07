# -*- coding:utf-8 -*-
# 
# @lc app=leetcode.cn id=945 lang=python
#
# [945] 使数组唯一的最小增量
#
# 解题思想：
# 上面由于有多次的循环来累加计数，导致时间复杂度过大，如果把多次变为一次就可以将时间复杂度控制到O(N),
#  这里只需要提前知道哪些数字是没有用过的，然后将重复的数字直接变化为非重复的数字就可以。
# 使用的办法就是count = j - i 
# j 为未出现的数，i为重复的数，一遍循环减去重复的数，在有重复数的情况下进行上述变化。
# 这里重复出现的数和最后变化的数是可以任意选择的，不影响最后结果，
# 因为将 P 增加到 X 并且将 Q 增加到 Y，
# 与将 P 增加到 Y 并且将 Q 增加到 X 都需要进行 (X + Y) - (P + Q) 次操作。
# 例如当数组 A 为 [1, 1, 1, 1, 3, 5] 时，
# 我们发现有 3 个重复的 1，且没有出现过 2，4 和 6，
# 因此一共需要进行 (2 + 4 + 6) - (1 + 1 + 1) = 9 次操作。

# @lc code=start
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = [0] * 80000
        for x in A:
            count[x] += 1
        
        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                # +变化的次数
                taken += count[x] - 1
                # 有1个是不要变的，count[x] - 1是这个意思，x来乘是这个数需要变化几次
                ans -= x * (count[x] - 1) 
            elif taken > 0 and count[x] == 0:
                #-1次变化
                taken -= 1
                ans += x
        
        return ans
    
# class Solution(object):
#     def minIncrementForUnique(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         A.sort()
#         d = {}
#         count = 0
#         for x in A:
#             while x in d:
#                 count += 1
#                 x += 1
#             d[x] = 1
#         return count
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    import random
    a = []
    for i in range(0,40000):
        a.append(random.randint(0,5000))
    print(a)
    count = obj.minIncrementForUnique(a)
    print(count)