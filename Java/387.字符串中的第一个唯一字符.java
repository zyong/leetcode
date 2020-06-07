import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=387 lang=java
 *
 * [387] 字符串中的第一个唯一字符
 */

// @lc code=start
class Solution {
    public int firstUniqChar(String s) {
        if(s==null || s.length()==0) {
            return -1;
        }
        char[] ca = s.toCharArray();
        Map<Character, Integer> charsPositions = new HashMap<>();
        List<Integer> uniqsPositions = new ArrayList<>();
        for (int i=0; i<ca.length; i++) {
            char c = ca[i];
            if (charsPositions.containsKey(c)) {
                Integer charFirstPosition = charsPositions.get(c);
                uniqsPositions.remove(charFirstPosition);
            } else {
                charsPositions.put(c,i);
                uniqsPositions.add(i);
            }
        }
        return uniqsPositions.isEmpty() ? -1 : uniqsPositions.get(0);
    }
}
// @lc code=end

