/*
 * @lc app=leetcode.cn id=33 lang=java
 *
 * [33] 搜索旋转排序数组
 */
// 解题思路
// 1.二分查找       
//  1.数组是部分有序的,可以进行二分验证
//  2.算法时间复杂度O(logn)

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length < 3) {
            for (int i=0; i < nums.length; i++) {
                if (nums[i] == target) {
                    return i;
                }
            }
            return -1;
        }

        int left = 0;
        int right = nums.length - 1;
        int mid = findOrder(nums, left, right);
        if (mid == -1) {
            return -1;
        }
        

        // 查找左边
        left = 0;
        right = mid - 1;
        int ret = search(nums, target, left, right);

        if (ret != -1) {
            return ret;
        }

        left = mid;
        right = nums.length - 1;
        ret = search(nums, target, left, right);
        if (ret != -1) {
            return ret;
        }
        return -1;
    }

    private int findOrder(int[] nums, int left, int right) {
        if (nums[left] < nums[right])
            return 0;

        while (left <= right) {
            int pivot = (left + right) / 2;
            if (nums[pivot] > nums[pivot + 1])
                return pivot + 1;
            else {
                if (nums[pivot] < nums[left])
                    right = pivot - 1;
            else
                left = pivot + 1;
            }
        }
        return 0;

    }

    private int search(int[] nums, int target, int left, int right) {
        int mid;
        while (left <= right) {
            mid = (left + right) /2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
     
    public static void main(String[] args) {
        Solution obj = new Solution();
        int ret = obj.search(new int[]{6,7,8,9,1,2,3,4,5}, 2);
        System.out.println(ret);
    }
}
// @lc code=end

