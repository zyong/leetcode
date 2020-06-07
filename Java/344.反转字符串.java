/*
 * @lc app=leetcode.cn id=344 lang=java
 *
 * [344] 反转字符串
 */

// @lc code=start
class Solution {
    public void reverseString(char[] s) {
        if (s.length == 0) {
            return;
        }
        int i = 0;
        int j = s.length - 1;
        char c;
        while(true) {
            if (i >= j) {
                break;
            }
            c = s[i];
            s[i] = s[j];
            s[j] = c;
            i++;
            j--;
        }
    }
}
// @lc code=end

