# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=771 lang=python
#
# [771] 宝石与石头
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # count = 0

        # for c in S:
        #     if c in J:
        #         count += 1
        # return count

        return len([c for c in S if c in J])
        
# @lc code=end
if __name__ == "__main__":
    obj  = Solution()
    ret = obj.numJewelsInStones("aA", "aAAbbbb")
    print(ret)
