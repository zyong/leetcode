import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/*
 * @lc app=leetcode.cn id=438 lang=java
 *
 * [438] 找到字符串中所有字母异位词
 */

/**
 * 解题思路
 * 1、滑动窗口 
 *   1、使用p字符串找到所有的字符，计算p的长度
 *   2、从s的第一个字符开始找在p字符串里面的字符，找到一个就取相同长度的字符串
 *      看字符串里面的字符串和p的字符是否相同。
 *   3、
 */
// @lc code=start
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<>();
        if (s==null || s.length() == 0 || p == null || p.length() == 0) 
            return list;
        
        int[] hash = new int[256];
        for (char c: p.toCharArray()) {
            hash[c]++;
        }
        int left = 0;
        int right = 0;
        int count = p.length();

        while (right < s.length()) {
           // 在s字符串里面的字符，每次count会被减一，当count==0的时候证明
           // 不在p中字符，最后是小于0的，因为初值为0再减少就小于0了
            if (hash[s.charAt(right)] > 0) {
                count--;
            }
            hash[s.charAt(right)]--;
            right++;

            if (count == 0) {
                list.add(left);
            }

              // hash中的值>=0表示存在于p中的值，如果这个值不在下次的查找循环里面了，就必须要增加一个count，
            // 使下次查找的结果符合p的长度和字符
            // right-left=p.length()表示一个新的p长度开始了，需要缩小left和right距离，使其刚好等于p长度
            // 考虑几种情况：
            // 1、刚好存在left到right的距离是一个p字符串，count=0的时候刚好一个p字符串
            // 2、left到right不是一个p字符串，count一直大于0，left和right的距离适中保持在p的长度，left一定会++
            //   1、不包含p中字符
            //      2、包含p中字符
            //        1、包含重复的p中字符，这个重复的p中字符导致需要给hash中的这个字符++
            //      并且由于存在多个重复p中字符，所以在hash中的这个字符会小于0，所以不能仅仅在>=0的情况下相加
            
            if (right - left == p.length()) {
                if (hash[s.charAt(left)] >= 0) {
                    count++;
                }
                hash[s.charAt(left)]++;
                left++;
            }
        }
        return list;
    }
}

// class Solution {
//     public List<Integer> findAnagrams(String s, String p) {
//         List<Integer> list = new ArrayList<>();
//         if (s == null || s.length() == 0 || p == null || p.length() == 0) return list;
//         int[] hash = new int[256]; //character hash
//         for (char c : p.toCharArray()) {
//             hash[c]++;
//         }
//         //two points, initialize count to p's length
//         int left = 0;
//         int right = 0;
//         int count = p.length();
//         while (right < s.length()) {
//             //move right everytime, if the character exists in p's hash, decrease the count
//             //current hash value >= 1 means the character is existing in p
//             if (hash[s.charAt(right++)]-- >= 1) {
//                 count--; 
//             }
            
//             //when the count is down to 0, means we found the right anagram
//             //then add window's left to result list
//             // 存在的前提是left和right保持p的长度的基础上，count=0了，证明是p的异位词
//             if (count == 0) list.add(left);
        
//             //if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
//             //++ to reset the hash because we kicked out the left
//             //only increase the count if the character is in p
//             //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
//           
//             if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0) count++;
//         }
//         return list;
//     }

// }



// @lc code=end

