#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#
# 解题思路
# 1.使用牛顿迭代法
#   1.设置随机值R，R/2可以将计算提速，同时要排除0，1的情况
#   2.使用r = (r + x/r)/2的公式不断循环
# 知识点
# 1。切线方程  
# 在平面直角坐标系中，如果直线L经过点A(x1,y1)和B(x2,y2) ，其中x1≠x2，
# 那么k=y2-y1/x2-x1 是L的一个方向向量，于是直线L的斜率 ,再由k=tanα（0≤α<π），
# 可求出直线L的倾斜角α.记tanα=k，y-y0=k(x - x0)方程叫做直线的点斜式方程(切线方程)，
# 其中是直线上一点。
# 2.y=x^n的导数公式
# f(xn)=nx^n-1
# 所以 y=x^2的导数等于y`=2x, x0=2 y0=4 k=4
# y-4=4(x-2) y=4x-8+4=4x-4
# https://leetcode-cn.com/problems/sqrtx/solution/niu-dun-die-dai-fa-by-loafer/
# https://www.zhihu.com/question/20690553
# 平方根用牛顿迭代法思想
# 1.求平方根函数为y=x^2, 方程的根就是就是一个实数的开平方值
# 2.
# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 or num == 0:
            return True
        
        r = num/2
        x = num
        while r * r > x:
            r = (r + x/r) / 2
        return True if r * r == num else False
        
# @lc code=end

