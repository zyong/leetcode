/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 * 
 * 
 * 
 * 双指针
 *  1、右指针不断向右查找，从找到的那个指针开始找下一个不在子串中的字符；记录两字符间距离
 *     当所有字符都找到后缩小l，查找下一个满足要求的位置；比对每次找到的所有长度，最短的就是所求解；
 * 
 */


#include <string>

using namespace std;

// @lc code=start
// 
class Solution {
public:

    string minWindow(string s, string t) {
        int left = 0, right = 0;
        int s_size = s.size(), t_size = t.size();
        // ascii 包含128字符，不包括扩展Ascii
        int t_map[128] = {0}, s_map[128] = {0};
        // 统计字符数量
        for (char c: t) ++t_map[c];
        
        int t_map_size = 0;
        // 计算有多少中字符存在
        for (int i = 0; i < 128; ++i) if (t_map[i]) ++t_map_size;

        int match = 0;
        int start = 0; // record the starting point for getting substring
        int min_length = INT32_MAX;
        
        while (right < s_size) {
            char c = s[right];
            if (t_map[c]) {
                ++s_map[c];
                if (s_map[c] == t_map[c]) ++match;
            }
            ++right;
            while (match == t_map_size) {
                int length = right - left;
                if (length < min_length) {
                    start = left;
                    min_length = length;
                }
                char c = s[left];
                // writing if in this way can save time and space. Moreover, this may be the only correct way.
                if (t_map[c]) {
                    --s_map[c];
                    if (s_map[c] < t_map[c]) --match;
                }
                ++left;
            }
        }
        return min_length == INT32_MAX ? "" : s.substr(start, min_length);
    }
};


// @lc code=end

