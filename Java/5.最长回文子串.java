/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// 1、中心扩散法
//   1、回文子串都是从中心向两端延伸，每次延伸的字符都是相等的
//   2、回文串有奇数和偶数个两种数量
// 2、DP

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return "";

        int start = 0;
        int end = 0;
        for (int i=0; i<s.length(); i++) {
            int len1 = expandCenter(s, i, i);
            int len2 = expandCenter(s, i, i+1);

            int len = Math.max(len1, len2);
            // len 比 现有长度要长 
            if (len > end - start) {
                start = i - (len - 1)/2;
                end = i + len/2;
            }
        }
        return s.substring(start, end + 1);

    }

    private int expandCenter(String s, int left, int right) {
        int i = left;
        int j = right;
        while (i>=0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        // 最后一次加完是不相等的，所以减一
        return j - i - 1;
    }
}
// @lc code=end

