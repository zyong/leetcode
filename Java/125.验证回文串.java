/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return true;

        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            if (Character.isLetter(c) || Character.isDigit(c)) {
                sb.append(c);
            }
        }
        return sb.toString().equalsIgnoreCase(sb.reverse().toString());
    }
}


class Solution {
    public boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return true;

        s = s.replaceAll("[^a-zA-Z0-9]+", "");

        StringBuilder sb = new StringBuilder(s);
        String rs = sb.reverse().toString();

        return rs.equalsIgnoreCase(s);
    }
}

// @lc code=end

