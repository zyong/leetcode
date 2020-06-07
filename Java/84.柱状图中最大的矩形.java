/*
 * @lc app=leetcode.cn id=84 lang=java
 *
 * [84] 柱状图中最大的矩形
 * 
 * 
 * 暴力
 * 1、两轮循环
 *  找最大的高和宽，遍历数组，找到从头到尾元素间最小的高，使用距离*高得到每次的面积
 *  比较算出最大面积
 */

// @lc code=start
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack <Integer> stack = new Stack <>();
        int n = heights.length;
        stack.push(-1);
        int maxarea = 0;
        for (int i = 0; i < n; ++i) {
            // 枚举每个柱子的边界，通过边界计算每个高能得到的最大面积
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i])
                maxarea = Math.max(maxarea, heights[stack.pop()] * (i - stack.peek() - 1));
            stack.push(i);
        }
        // 如果栈非空，证明里面的柱子都是很矮的，所以没有可以比较的柱子那么他们可以直接用heights的长度来计算
        while (stack.peek() != -1)
            maxarea = Math.max(maxarea, heights[stack.pop()] * (heights.length - stack.peek() -1));
        return maxarea;
    }
}


// force brute
/* class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxarea = 0;
        int minHeight = Integer.MAX_VALUE;
        int distance = 0;
        int n = heights.length;
        for (int i=0; i<n; i++) {
            minHeight = heights[i];
            for (int j=i; j<n; j++) {
                distance = j-i + 1;
                minHeight = Math.min(minHeight, heights[j]);
                maxarea = Math.max(maxarea, minHeight * distance);
            }
        }

        return maxarea;
    }
} */
// @lc code=end

