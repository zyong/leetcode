/*
 * @lc app=leetcode.cn id=560 lang=java
 *
 * [560] 和为K的子数组
 */

// @lc code=start
// class Solution {
//     public int subarraySum(int[] nums, int k) {
//         int count = 0;
//         for (int start = 0; start < nums.length; ++start) {
//             int sum = 0;
//             for (int end = start; end >= 0; --end) {
//                 sum += nums[end];
//                 if (sum == k) {
//                     count++;
//                 }
//             }
//         }
//         return count;
//     }
// }

// 方案就是K = Sum(i) - Sum(j), 0 < j < i, K的值存在于j,i之间
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0; 
        int pre = 0;
        HashMap<Integer, Integer> mp = new HashMap <>();
        // 和为0出现1次
        mp.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            // 计算到现在为止前面的和
            pre += nums[i];
            // 如果
            if (mp.containsKey(pre - k))
                count += mp.get(pre - k);
            mp.put(pre, mp.getOrDefault(pre, 0) + 1);
        }
        return count;
    }
}
// @lc code=end

