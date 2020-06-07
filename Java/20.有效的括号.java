import java.util.HashMap;
import java.util.Stack;
/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */
/*
 * 解题思路
 * 1、数据结构stack，只要按照字符顺序进栈和出栈就可以验证结果
 *  1.每次发现) } ]就出栈看是否匹配，不匹配就验证失败
 */


// @lc code=start
class Solution {
    // Hash Table that take care of the mappings.
    private HashMap<Character, Character> mappings;

    // Class Intialize method
    public Solution() {
        this.mappings = new HashMap<Character, Character>();
        this.mappings.put(')', '(');
        this.mappings.put('}', '{');
        this.mappings.put(']', '[');
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (this.mappings.containsKey(c)) {
                char topElement = stack.empty() ? '#' : stack.pop();

                if (topElement != this.mappings.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }

        }
        
        
        return stack.isEmpty();
    }
}
// @lc code=end

