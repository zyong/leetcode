# -*- coding:utf-8 -*-
# 解题思路
# 1.递归
#   1.傻递归
#   2.去重递归
# 2.斐波拉系数
# 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        1:1
        2:2
        3: f(1) + f(2) 等于前两次走法之和，因为f(1)走2步到f(3),f(2)走一步到f(3),两个的和构成3
        4: f(3) + f(2)
        实际上就是求fibnacci数列
        解决算法问题的办法就是找重复子问题
        """
        f1, f2, f3 = 1, 2, 3
        if n <= 2:
            return n
        # 使用n + 1是因为range参数的第二个在循环中不包含
        # 取3的原因是fibnacci数列是从1开始的不是0，所以3正好的第三个数
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
        
        
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(10))
