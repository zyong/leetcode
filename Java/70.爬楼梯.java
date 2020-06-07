/*
 * @lc app=leetcode.cn id=70 lang=java
 *
 * [70] 爬楼梯
 */
// 解题思路
// 1.递归
//  1.上到当前层有两种办法，一种是上一层+1，一种是上上层+2
//  2.f(3) = f(1) + f(2)
//    f(4) = f(3) + f(2) 依次类推
// @lc code=start
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        int f1, f2, f3 = 0;
        f1 = 1;
        f2 = 2;
        f3 = 3;
        for (int i=3; i <= n; i++) {
            f3 = f2 + f1;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }

}
// @lc code=end

