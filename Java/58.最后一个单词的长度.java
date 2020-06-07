/*
 * @lc app=leetcode.cn id=58 lang=java
 *
 * [58] 最后一个单词的长度
 */

// @lc code=stsbart
class Solution {
    public int lengthOfLastWord(String s) {
        System.out.print(s.trim().lastIndexOf(' '));
        return s.trim().length()-s.trim().lastIndexOf(' ') - 1;
    }
}
// @lc code=end

