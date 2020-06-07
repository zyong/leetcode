import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=151 lang=java
 *
 * [151] 翻转字符串里的单词
 */

// @lc code=start
class Solution {
    public String reverseWords(String s) {
        // 除去开头和末尾的空白字符
        s = s.trim();
        // 正则匹配连续的空白字符作为分隔符分割
        List<String> wordList = Arrays.asList(s.split("\\s+"));
        Collections.reverse(wordList);
        return String.join(" ", wordList);
    }
}

// class Solution {
//     public StringBuilder trimSpaces(String s) {
//         int left = 0, right = s.length() - 1;
//         // 去掉字符串开头的空白字符
//         while (left <= right && s.charAt(left) == ' ') ++left;

//         // 去掉字符串末尾的空白字符
//         while (left <= right && s.charAt(right) == ' ') --right;

//         // 将字符串间多余的空白字符去除
//         StringBuilder sb = new StringBuilder();
//         while (left <= right) {
//             char c = s.charAt(left);

//             if (c != ' ') sb.append(c);
//             else if (sb.charAt(sb.length() - 1) != ' ') sb.append(c);

//             ++left;
//         }
//         return sb;
//     }

//     public void reverse(StringBuilder sb, int left, int right) {
//         while (left < right) {
//             char tmp = sb.charAt(left);
//             sb.setCharAt(left++, sb.charAt(right));
//             sb.setCharAt(right--, tmp);
//         }
//     }

//     public void reverseEachWord(StringBuilder sb) {
//         int n = sb.length();
//         int start = 0, end = 0;

//         while (start < n) {
//             // 循环至单词的末尾
//             while (end < n && sb.charAt(end) != ' ') ++end;
//             // 翻转单词
//             reverse(sb, start, end - 1);
//             // 更新start，去找下一个单词
//             start = end + 1;
//             ++end;
//         }
//     }

//     public String reverseWords(String s) {
//         StringBuilder sb = trimSpaces(s);

//         // 翻转字符串
//         reverse(sb, 0, sb.length() - 1);

//         // 翻转每个单词
//         reverseEachWord(sb);

//         return sb.toString();
//     }
// }
// @lc code=end

