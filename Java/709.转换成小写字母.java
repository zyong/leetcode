/*
 * @lc app=leetcode.cn id=709 lang=java
 *
 * [709] 转换成小写字母
 */

// @lc code=start
// class Solution {
//     public String toLowerCase(String str) {
//         StringBuilder sb = new StringBuilder();
// 		for (int i = 0; i < str.length(); i++) {
// 			sb.append(Character.toLowerCase(str.charAt(i)));
// 		}
// 		return sb.toString();
//     }
// }

class Solution {
    public String toLowerCase(String str) {
        StringBuilder sb = new StringBuilder();
		char ch;
		int value = 0;
		for (int i = 0; i < str.length(); i++) {
			ch = str.charAt(i);
			value = ch;
			if (value >= 65 && value <= 90) {
				value = str.charAt(i) + 32;
				ch = (char) value;
			}
			sb.append(ch);
		}
		return sb.toString();
    }
}
// @lc code=end

