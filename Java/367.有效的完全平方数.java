
/*
 * @lc app=leetcode.cn id=367 lang=java
 *
 * [367] 有效的完全平方数
 */
// 解题思路
// 1.二分查找
//  1.找到一个数的平方等于当前数就是完全平方数
// 2.完全平方数可以通过累加从1往后的奇数找到，
// 1 = 1;
// 4 = 1 + 3;
// 9 = 1 + 3 + 5;
// 16 = 1 + 3 + 5 + 7;

// @lc code=start
class Solution {
    public boolean isPerfectSquare(int num) {
      if (num < 2) return true;
  
      int i = 1;
      while (num > 0) {
         num = num - i;
         i = i + 2;
      }
      return num == 0;
    }
  }
// class Solution {
//     public boolean isPerfectSquare(int num) {
//       if (num < 2) return true;
  
//       long x = num / 2;
//       while (x * x > num) {
//         x = (x + num / x) / 2;
//       }
//       return (x * x == num);
//     }
//   }
  
// @lc code=end


