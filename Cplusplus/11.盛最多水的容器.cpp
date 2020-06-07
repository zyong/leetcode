/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        int heightSize = int(height.size());
        for (int index1 = 0; index1 < heightSize; index1++) {
          for (int index2 = index1 + 1; index2 < heightSize; index2++) {
            int length = index2 - index1;
            int heightSize = height[index1] < height[index2] ? height[index1] : height[index2];
            int tmpSize = length * heightSize;
            if (tmpSize > result) {
              result = tmpSize;
            }
          }
        }
        return result;
    }
};
// @lc code=end

