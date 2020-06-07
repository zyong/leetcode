# -*- coding:utf-8 -*-
# 
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#
# 解题思路
# 1.递归
#   1.傻递归
#   3级台阶是从1级台阶和2级台阶上来的，1级台阶一次上2级就是3级，2级台阶一次上1级就是3级，依次类推
#   fn = fn-1 + fn-2
#   2.去重递归 
#   由于傻递归一路下来会有很多重复的计算，导致时间复杂度大大增加，所以使用缓存的机制可以提高效率
# 2.斐波拉系数
#   1:1
#   2:2
#   3: f(1) + f(2) 等于前两次走法之和，因为f(1)走2步到f(3),f(2)走一步到f(3),两个的和构成3
#   4: f(3) + f(2)
#   实际上就是求fibnacci数列
#   解决算法问题的办法就是找重复子问题
# 
# @lc code=start
# 傻递归
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        
#         mem = {}
        
#         def f(n):
#             if n == 1 or n == 2:
#                 return n
#             # 加缓存的递归
#             if n in mem:
#                 return mem[n]
#             else:
#                 mem[n] = f(n-1) + f(n-2)

#             return mem[n]
        
#         return f(n)
        
# 2 斐波拉系数
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1, f2, f3 = 1, 2, 3
        if n <= 2:
            return n
        # 使用n + 1是因为range参数的第二个在循环中不包含
        # 取3的原因是fibnacci数列是从1开始的不是0，所以3正好的第三个数
        for _ in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(10))
