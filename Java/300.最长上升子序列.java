import java.util.Arrays;
import java.util.Collections;

/*
 * @lc app=leetcode.cn id=300 lang=java
 *
 * [300] 最长上升子序列
 *
 * 
 * 1.解题思路
 *  DP 
 *  1. subproblem A的最长上升子序列，等于A-1的最长上升子序列+1
 *  2. DP数组 dp[n]
 *  3. DP方程 
 *   if nums[i] > nums[i-1] dp[n] = max(dp[i], dp[j] + 1)
 *   else d[n] = 0
 */


// @lc code=start
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int[] dp = new int[n+1];
        int maxval = 0;
        dp[0] = 1;
        for (int i=0; i<n; i++) {
            maxval = 0;
            for (int j=0; j<i; j++) {
                if (nums[i] > nums[j]) {
                    maxval = Math.max(maxval, dp[j]); 
                }
            }
            //每轮求当前值的最长上升序列
            dp[i] = maxval + 1;
        }
        
        // 求数组集合里面的最大值
        return Arrays.stream(dp).max().getAsInt();
    }
}
// @lc code=end

