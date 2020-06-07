import java.util.HashSet;

/**
 * @lc app=leetcode.cn id=1044 lang=java
 * 
 * 最长重复子串
 * 解题思路
 * 1、二分查找+Robin-Karp
 *  1.找最长字符串
 *   解决的问题是找到最大有效子串
 *  2.查找子串在原字符串中是否重复
 *   验证重复子串
 */
public class Solution {
    public String longestDupSubstring(String S) {
        int n = S.length();

        // 因为是26个字母
        int a = 26;

        // 转化为整形数组
        int[] nums = new int[n];
        for (int i=0; i<n; i++) {
            nums[i] = (int)S.charAt(i) - (int)'a';
        }

        // 计算moduels
        long modules = (long)Math.pow(2, 32);


        // 二分查找
        int left = 0;
        int right = S.length();
        int L;

        while (left != right) {
            L = left + (right - left) /2;
            if (search(L, a, n, nums, modules) != -1) {
                left = L + 1;
            } else {
                right = L;
            }
        }

        int start = search(left - 1, a, n, nums, modules);
        return start != -1 ? S.substring(start, start + left - 1) : "";
    }

    private int search(int L, int a, int n, int[] nums, long modules) {
        long h = 0;
        for (int i = 0; i < L; ++i) 
            h = (h * a + nums[i]) % modules;
            
        HashSet<Long> seen = new HashSet();
        seen.add(h);

        long aL = 1;

        for (int i = 1; i <= L; ++i) 
            aL = (aL * a) % modules;

        for (int start = 1; start < n - L + 1; start++) {
            h = (h * a - nums[start - 1] * aL % modules + modules) % modules;
            h = (h + nums[start + L - 1]) % modules;
            if (seen.contains(h)) {
                return start;
            }
            seen.add(h);
        }
        return -1;
    }
}