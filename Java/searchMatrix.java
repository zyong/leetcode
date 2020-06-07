/*
 * @lc app=leetcode.cn id=74 lang=java
 *
 * [74] 搜索二维矩阵
 */
// 题目
// 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

// 每行中的整数从左到右按升序排列。
// 每行的第一个整数大于前一行的最后一个整数。

// 解题思路
// 数据时按维升序排列的,每行也是升序
// 1. 二分查找第二维的数据
//   1.循环第一维,使二分查找变成一维的
//   2.每次循环在一行数据里面二分查找指定值,找到就返回,如果数据依据大于指定值返回无此数据

// @lc code=start
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) {
            return false;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;

        // 一遍循环的二分查找
        int left = 0;
        int right = rows * cols - 1;

        while (left <= right) {
            int mid = (left + right) /2;
            if (matrix[mid / cols][mid % cols] == target) {
                return true;
            } else if (matrix[mid / cols][mid % cols] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // 两遍循环的二分查找
        // for (int i=0; i<rows; i++) {
        //     int left = 0;
        //     int right = cols - 1;
        //     int[] nums = matrix[i];
        //     while (left <= right) {
        //         int mid = (left + right) /2;
                
        //         if (nums[mid] == target) {
        //             return true;
        //         } else if (nums[mid] < target) {
        //             left = mid + 1;
        //         } else {
        //             right = mid - 1;
        //         }
        //     }
        // }
        return false;

    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int[][] matrix = {
            {1,2,3,4,5},
            {6,7,8,9,10}
        };
        obj.searchMatrix(matrix, 2);
    }
}
// @lc code=end


