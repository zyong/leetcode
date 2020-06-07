/*
 * @lc app=leetcode.cn id=541 lang=java
 *
 * [541] 反转字符串 II
 */

// @lc code=start
class Solution {
    public String reverseStr(String s, int k) {
        int i = 0; 
        char[] chars = s.toCharArray();
        while (i < chars.length) {
            
            int end = i + k - 1;
            if (end > chars.length - 1)
                end = chars.length - 1;
            
            reverse(chars, i, end);
            
            i = i + 2 * k;
        }
        
        return new String(chars);
    }

    private void reverse(char[] chars, int left, int right) {
        
        while (left < right) {
            char tmp = chars[left];
            chars[left] = chars[right];
            chars[right] = tmp;
            left++;
            right--;
        }
    }
}
// @lc code=end

