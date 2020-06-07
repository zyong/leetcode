/*
 * @lc app=leetcode.cn id=287 lang=java
 *
 * [287] 寻找重复数
 * 
 * 题设是有n+1个数字的数组，而其中的数只有1-n
 * 1、二分查找
 * 原理：
 *  1、数组的元素都是1-n的整数，中间只有一个数字是重复的，那么重复的个数
 *  设置target为要找到的重复数，[1,target - 1]的数字都是不重复的，
 *  计算的cnt应该等于target - 1, [target, n]的数字由于有一个重复的，
 *  所以cnt要大于target,这样在找到第一个大于mid的时候，target就找到了
 * 
 * 2、快慢指针
 * // https://leetcode-cn.com/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode-solution/
 *  1、快慢指针原理重点这里面有环，不好理解的店就是相遇后slow指针重置到0，然后再找到快指针的位置就是重复点
 *   有环的原因是数组上有两个或以上的相同的值，用索引->value，会有两个值相同的索引，都会引导到相同的结果，
 *   在相同索引和结果的变化下形成环；
 *  2、在有环的时候，通过快慢两个指针，找到环入口的位置，由于两个指针相遇只会在环的范围内，这样可以假设慢指针
 *   走了a步到环入口，右走了b步与快指针相遇，然后慢指针从0开始于快指针同时走a步相遇，这个时候快指针也是以同样
 *   的步幅，快指针走了c，慢指针走了a，2(a+b) = a+b + kL, L为环的长度，a = kL - b
 *      a=(k−1)L+(L−b)=(k−1)L+c, 等于说慢指针走a步，快指针走c+(k-1)L 刚好在环入口相遇
 */

// @lc code=start
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}

// 二分查找
// 重复数由于是1-n的值，数组有1+n个元素，其中有个元素重复
// 假设i为重复元素index，target为重复元素值，会有小于i的元素的出现次数小于target，cnt[i] <= target
// 大于等于i的元素的出现次数大于target的，因为有重复值
/* class Solution {
    public int findDuplicate(int[] nums) { 
        int n = nums.length;
        int l = 1;
        int r = n - 1;
        int ans = -1;
        while (l<=r) {
            int mid = (l+r)>>1;
            int cnt = 0;
            for (int i=0; i< n; i++) {
                if (nums[i] <= mid) {
                    cnt++;
                }
            }
            if (cnt <= mid) {
                l = mid + 1;
            } else {
                r = mid - 1;
                ans = mid;
            }
        }
        return ans;
    }
} */

/* 

class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length;
        int l = 1;
        int r = n - 1;
        int ans = -1;
        while (l <= r) {
            int mid = (l+r) >> 1;
            int cnt = 0;
            for (int i=0; i<n; i++) {
                if (nums[i] <= mid) {
                    cnt++;
                }
            }
            if (cnt <= mid) {
                l = mid + 1;
            } else {
                r = mid - 1;
                ans = mid;
            }
        }
        return ans;
    }
} */
// @lc code=end

