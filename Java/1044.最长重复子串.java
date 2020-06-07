/*
 * @lc app=leetcode.cn id=1044 lang=java
 *
 * [1044] 最长重复子串
 */
// https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode/
// @lc code=start
class Solution {
    /*
    Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        Return start position if the substring exits and -1 otherwise.
        Rabin-Karp 多项式Rolling Hash搜索至少2次特定长度子串。
        */
    public int search(int L, int a, long modulus, int n, int[] nums) {
        // compute the hash of string S[:L]
        long h = 0;
        // 为了保证安全每次都模上modules，小于modules的保持不变，大于modules会减少到modules内
        for (int i = 0; i < L; ++i) 
            h = (h * a + nums[i]) % modulus;

        // already seen hashes of strings of length L
        HashSet<Long> seen = new HashSet();
        seen.add(h);

        // const value to be used often : a**L % modulus
        long aL = 1;

        for (int i = 1; i <= L; ++i) 
            aL = (aL * a) % modulus;

        for (int start = 1; start < n - L + 1; ++start) {
            // compute rolling hash in O(1) time
            // 移除最高位的字符，移除最高位的部分,
            // h1 = (h0 - nums[start-1] * a^(L-1)) * a + nums[start + L - 1] * a^0 
            // 由于Java存在最大值限制，所以这里对每个结果都取模
            // 对中间数取模，是防止数据上溢，再加上modules避免数据差异过小
            h = (h * a - nums[start - 1] * aL % modulus + modulus) % modulus;
            h = (h + nums[start + L - 1]) % modulus;
            if (seen.contains(h)) return start;
            seen.add(h);
        }
        return -1;
    }


    public String longestDupSubstring(String S) {
        int n = S.length();
        // convert string to array of integers
        // to implement constant time slice
        int[] nums = new int[n];
        for (int i = 0; i < n; ++i) 
            nums[i] = (int)S.charAt(i) - (int)'a';

        // base value for the rolling hash function
        int a = 26;

        // modulus value for the rolling hash function to avoid overflow
        long modulus = (long)Math.pow(2, 32);

        // binary search, L = repeating string length
        int left = 1;
        int right = n;
        int L;

        /**
         *  特别的二分查找，查找的前提是，一个子串存在，可能+1的情况也存在，这样可以一直循环找到最大重复串
         *  这样避免长子串存在小子串问题导致的子串查询错误
            1、每次搜索变化长度的字符串，看这个长度的字符串在String中是否有重复子串
            2、如果有看L+1 + (n-L-1)/2 长度子串有没有
            3、如果没有看1+(L-1)/2长度子串有没有
         */ 
        while (left != right) {
            L = left + (right-left)/ 2;
            if (search(L, a, modulus, n, nums) != -1)
                left = L + 1;
            else 
                right = L;
        }
        // 最后left和right相等，结果有两个，
        // 1、找到相同的子串，结果肯定是left - 1,最大重复子串之后肯定是找不到结果的，导致left==right
        // 2、没找到，查找上述L是找不到的
        int start = search(left - 1, a, modulus, n, nums);
        return start != -1 ? S.substring(start, start + left - 1) : "";
    }
}
// @lc code=end

