/*
 * @lc app=leetcode.cn id=1044 lang=cpp
 *
 * [1044] 最长重复子串
 */
#include <string>
#include <vector>
#include <cmath>
#include <unordered_set>

using namespace std;

// @lc code=start
class Solution {
private:
    int search(int L, int a, long modules, int n, vector<int> nums) {
        long h = 0;

        for (int i = 0; i < L; ++i) 
            h = (h * a + nums[i]) % modules;

        // already seen hashes of strings of length L
        unordered_set<long> seen = unordered_set<long>();
        seen.insert(h);

        // const value to be used often : a**L % modulus
        long aL = 1;

        for (int i = 1; i <= L; ++i) 
            aL = (aL * a) % modules;

        for (int start = 1; start < n - L + 1; ++start) {
            h = (h * a - nums[start - 1] * aL % modules + modules) % modules;
            h = (h + nums[start + L - 1]) % modules;
            if (seen.find(h) != seen.end()) return start;
            seen.insert(h);
        }
        return -1;
    }

public:
    string longestDupSubstring(string S) {
        unsigned int a = 26;
        unsigned int n = S.size();
        vector<int> nums;
        for (int i = 0; i < n; ++i) 
            nums.push_back(S.at(i) - 'a');

        unsigned int L = 0;
        uint32_t left = 1;
        uint32_t right = n;

        long modules = (long)pow(2, 32);
        while (left != right) {
            L = (left + right) / 2;
            if (search(L, a, modules, n, nums) != -1)
                left = L + 1;
            else 
                right = L;
        }
        int start = search(left - 1, a, modules, n, nums);
        return start != -1 ? S.substr(start, left - 1) : "";


    }
};
// @lc code=end

