import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=680 lang=java
 *
 * [680] 验证回文字符串 Ⅱ
 * 
 * 判断回文串
 * 1、双指针法
 * 如果每次都删除一个字符然后判断是否回文串会O(n^2)时间复杂度会超时
 * 简化的方法是仅仅在出现字符不等的情况下，减少一个左边的元素or一个右边的元素，
 * 然后判断后面的元素是否能满足要求
 */

// @lc code=start
class Solution {
    public boolean validPalindrome(String s) {
        int low = 0;
        int high = s.length() - 1;
        while (low < high) {
            char c1 = s.charAt(low);
            char c2 = s.charAt(high);
            if (c1 == c2) {
                low++;
                high--;
            } else {
                boolean flag1 = true;
                boolean flag2 = true;
                // 右边删除一个字符看能否相等
                for (int i = low, j = high - 1; i < j; i++, j--) {
                    char c3 = s.charAt(i);
                    char c4 = s.charAt(j);
                    if (c3 != c4) {
                        flag1 = false;
                        break;
                    }
                }
                // 左边删除一个字符看能否相等
                for (int i = low + 1, j = high; i < j; i++, j--) {
                    char c3 = s.charAt(i);
                    char c4 = s.charAt(j);
                    if (c3 != c4) {
                        flag2 = false;
                        break;
                    }
                }
                return flag1 || flag2;
            }
        }
        return true;
    }
}

// O(n^2)超时
/* class Solution {
    public boolean validPalindrome(String s) {
        if(valid(s)) {
            return true;
        }

        StringBuilder sb;
        for (int i=0; i<s.length(); i++) {
            sb = new StringBuilder(s);
            sb.deleteCharAt(i);
            if (valid(sb.toString())) {
                return true;
            }
        }
        return false;
    }

    private boolean valid(String s) {
        int n = s.length();
        char[] cs = s.toCharArray();
        int left = 0;
        int right = n-1;
        while (left < right) {
            if (cs[left++] != cs[right--]) {
                return false;
            }
        }
        return true;
    }
} */
// @lc code=end

