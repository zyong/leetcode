/*
 * @lc app=leetcode.cn id=974 lang=java
 *
 * [974] 和可被 K 整除的子数组
 * 同余定理：两个数模K的结果相等, 其差能被K整除
 * 
 * 
 */

// @lc code=start
// 两次计算结果
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] record = new int[K];
        record[0] = 1;
        int sum = 0;
        int ans = 0;
        for (int elem: A) {
            sum += elem;
            int modules = (sum % K + K) % K;
            record[modules]++;
        }

        for (int v: record) {
            // 全排列计算有多少种有效的组合
            // 排列组合计算 A(n,m)＝n(n-1)(n-2)……(n-m+1)＝n!/(n-m)!
            ans += v * (v - 1)/2;
        }

        return ans;
    }
}

// 一次计算结果
/* class Solution {
    public int subarraysDivByK(int[] A, int K) {
        // 整数的模的结果再模的范围内，所以可以用整形数组
        int[] record = new int[K];
        // 当结果为0的时候已经可以整除了，所以提前+1
        record[0] = 1;
        int sum = 0;
        int ans = 0;
        for (int elem: A) {
            // 从小的和值开始求，结果是要得到大的sum与小的和值的差，能否整除K
            // 如果相等应用同余定理就能整除K了
            sum += elem;
            // 注意 Java 取模的特殊性，当被除数为负数时取模结果为负数，需要纠正
            // sum % K + K 再取模是为了避免模为负数结果的情况
            // 取模为负数的情况是sum已经超出范围，已经为负数，所以模的结果为负数
            int modulus = (sum % K + K) % K;
            int same = record[modulus];
            ans += same;
            record[modulus] = same + 1;
        }
        return ans;
    }
} */

// @lc code=end

