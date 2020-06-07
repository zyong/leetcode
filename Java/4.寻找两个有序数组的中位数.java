/*
 * @lc app=leetcode.cn id=4 lang=java
 *
 * [4] 寻找两个有序数组的中位数
 */

/* 
 方法1
1、合并两个数组，去中间值
2、二分查找
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
@hackerhuang comment

 */
 
// @lc code=start
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        // 设置nums2的长度一定要大于nums1避免j的值为负数
        //  j = (m + n + 1)/2 - i
        if (m > n) return findMedianSortedArrays(nums2, nums1);

        int imin = 0;
        int imax = m;

        while (imin <= imax) {
            int i = imin +  (imax - imin) / 2;
            int j = (m + n + 1) / 2 - i;
            
            // 找到判断条件当前值，边界值的判断借助下面的向左向右的逻辑
            // 设置最大最小值，由于极值在数组两边，不影响中间值的取值结果
            // i=0证明A数组太大，无法取到需要的值
            // i=m证明A数组太小
            // j=0 or j=n 同理
            int A_left = i == 0 ? Integer.MIN_VALUE : nums1[i - 1];
            int A_right = i == m ? Integer.MAX_VALUE : nums1[i];
            int B_left = j == 0 ? Integer.MIN_VALUE : nums2[j - 1];
            int B_right = j == n ? Integer.MAX_VALUE : nums2[j];
            
            // 如果判断条件左边大于右边，证明数值大了，要缩小
            if (A_left > B_right) {
                imax = i - 1;
            // 如果判断条件B左边大于A右边，证明数值小了，要扩大
            } else if (B_left > A_right) {
                imin = i + 1;
            } else {
                // 找到符合条件的元素，取左边最大和右边最小，
                // 如果是奇数左边最大小于右边最小，取左边
                // 如果是偶数，会存在取中间两个数的平均数
                int max_left = A_left > B_left ? A_left : B_left;
                int min_right = A_right > B_right ? B_right : A_right;
                if ((m + n) % 2 == 1) 
                    return max_left;
                else 
                    return (max_left + min_right) / 2.0;
            }
        }
        return -1;
    }
}



// 合并两个数组，找中间值
/* class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int l = 0;
        int r = 0;
        int[] nums3 = new int[nums1.length + nums2.length];
        int index = 0;
        while (l < nums1.length && r < nums2.length) {
            if (nums1[l] <= nums2[r]) {
                nums3[index++] = nums1[l++];
            } else {
                nums3[index++] = nums2[r++];
            }
        }


        while (l < nums1.length) {
            nums3[index++] = nums1[l++];
        }

        while (r < nums2.length) {
            nums3[index++] = nums2[r++];
        }
        
        if (nums3.length % 2 == 1) {
            return (double)nums3[nums3.length / 2];
        } else {
            return (double)(nums3[nums3.length /2 - 1] + nums3[nums3.length / 2]) / 2;
        }

    }
} */

// @lc code=end

