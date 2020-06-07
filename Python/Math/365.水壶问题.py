#
# @lc app=leetcode.cn id=365 lang=python
#
# [365] 水壶问题
#
# 解题思路
# 1.使用数学公式
# 要满足两个水壶能计算出第三个的数量，必须满足 ax+bx=z 公式，z <= x + y
#   1.如果z比x+y大，是无法装满z的
#   2.任何一个水壶只能执行三个动作，倒满，倒空，倒向另一个壶
    
# https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/

# @lc code=start

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
    
        def gcd(a, b):
            c = min(a,b)
            for i in range(c, 1, -1):
                if a % i == 0 and b % i == 0:
                    return i
        
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % gcd(x, y) == 0
    
# @lc code=end

