import java.util.HashMap;
import java.util.Map;



/*
 * @lc app=leetcode.cn id=76 lang=java
 *
 * [76] 最小覆盖子串
 * 
 * 针对字符类型数据，存储使用字符数组性能会提升很多
 * 
 * 双指针
 *  1、右指针不断向右查找，从找到的那个指针开始找下一个不在子串中的字符；记录两字符间距离
 *     当所有字符都找到后缩小l，查找下一个满足要求的位置；比对每次找到的所有长度，最短的就是所求解；
 * 
 * 
 */


// @lc code=start
// 
class Solution {
    int[] ori = new int[128];
    int[] cnt = new int[128];

    public String minWindow(String s, String t) {
        int tLen = t.length();
        int match = 0;
        int t_map_size = 0;

        for (int i=0; i<tLen; i++) {
            ori[(int)t.charAt(i) - (int)('0')]++;
        }
        for (int i=0; i<ori.length; i++) if (ori[i] > 0) t_map_size++;

        int l = 0;
        int r = -1;
        int len = Integer.MAX_VALUE;
        int ansL = -1;
        int ansR = -1;
        int sLen = s.length();
        while (r < sLen) {
            ++r;
            if (r < sLen && ori[(int)s.charAt(r) - (int)'0'] > 0) {
                int c = (int)s.charAt(r) - (int)'0';
                cnt[c]++;
                if (ori[c] == cnt[c]) match++;

                // 已经满足要求了，移动l减小范围
                while (match == t_map_size) {
                    if (r - l + 1 < len) {
                        // 一个更好的答案
                        len = r - l + 1;
                        ansL = l;
                        ansR = l + len;
                    }
                    c = (int)s.charAt(l) - (int)'0';

                    // 如果元素在ori里面，要减去相关值
                    if (ori[c] > 0) {
                        cnt[c]--;
                        if (cnt[c] < ori[c]) match--;
                    }
                    l++;
                }
            }
        }
        return ansL == -1 ? "" : s.substring(ansL, ansR);
    }

}

/* 
class Solution {
    Map<Character, Integer> ori = new HashMap<>();
    Map<Character, Integer> cnt = new HashMap<>();

    public String minWindow(String s, String t) {
        int tLen = t.length();
        for (int i = 0; i < tLen; i++) {
            char c = t.charAt(i);
            ori.put(c, ori.getOrDefault(c, 0) + 1);
        }

        int l = 0;
        int r = -1;
        int len = Integer.MAX_VALUE;
        int ansL = -1;
        int ansR = -1;
        int sLen = s.length();
        while (r < sLen) {
            ++r;
            if (r < sLen && ori.containsKey(s.charAt(r))) {
                cnt.put(s.charAt(r), cnt.getOrDefault(s.charAt(r), 0) + 1);
            }
            while (check() && l <= r) {
                if (r - l + 1 < len) {
                    len = r - l + 1;
                    ansL = l;
                    ansR = l + len;
                }
                if (ori.containsKey(s.charAt(l))) {
                    cnt.put(s.charAt(l), cnt.getOrDefault(s.charAt(l), 0) - 1);
                }
                ++l;
            }
        }
        return ansL == -1 ? "" : s.substring(ansL, ansR);
    }
    
    public boolean check() {
        Iterator iter = ori.entrySet().iterator(); 
        while (iter.hasNext()) { 
            Map.Entry entry = (Map.Entry) iter.next(); 
            Character key = (Character) entry.getKey(); 
            Integer val = (Integer) entry.getValue(); 
            if (cnt.getOrDefault(key, 0) < val) {
                return false;
            }
        } 
        return true;
    }
} */


// @lc code=end

