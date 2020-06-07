/*
 * @lc app=leetcode.cn id=69 lang=java
 *
 * [69] x 的平方根
 */

//  解题思路
// 1.二分查找
//  1. 一个数的平方根，总是在0和这个数之间，就有个查找的范围
//  2.每次查找完修改两个边界，来改变查找的范围
// 当 x≥2 时，它的整数平方根一定小于 x/2 且大于 0，即 0 < a < x/2. 
// 由于 a 一定是整数，此问题可以转换成在有序整数集中寻找一个特定值，因此可以使用二分查找。

// 2.袖子计算器法
//  1.通常，袖珍计算器通过对数表或其他方式计算指数函数和自然对数。那么考虑将求平方根的运算转换为指数运算和对数运算：
// sqrt{x} = e^1/2logx
// 整数平方根
// 存在整数 aa 满足 a^2 ≤x<(a+1)^2 ，称 aa 为 xx 的 整数平方根。从几何角度来看，整数平方根就是小于 xx 的最大正方形的边长。
// https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode/
// 2.牛顿迭代
// @lc code=start
// class Solution {
//     public int mySqrt(int x) {
//       if (x < 2) return x;
  
//       int left = (int)Math.pow(Math.E, 0.5 * Math.log(x));
//       int right = left + 1;
//       return (long)right * right > x ? left : right;
//     }
//   }
  

class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        } 
        // 左边不会比2小
        int left = 2; 
        // 右边一定不会比X/2大
        int right = x/2;
        int mid;
        long num;
        while (left <= right) {
            // 设置范围很关键,要是left + (right -left)/2
            mid = left + (right - left) / 2;
            num = (long)mid * mid;
            if (num > x) {
                right = mid - 1;
            } else if (num < x) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        // 如果左右值都修改,取右值,如果只修改右取左值
        return right;
    }
}
// @lc code=end

