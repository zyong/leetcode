#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
# 
# 解题思路
# 1.贪心算法
#   1.每次胃口最小孩子的最优解，如果饼干不能满足胃口小的就更不能满足胃口大的
#   2.考虑几种情况
#       1.能满足的情况，孩子吃完没有剩的， +1
#       2.不能满足，孩子吃完还不够 0


# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s or not g:
            return 0
        # 饼干是有限的，尽量从最小的饼干开始满足最小胃口的孩子，
        # 所以排序后最小的在前，循环饼干只要满足了就投喂
        g.sort()
        s.sort()
        length_s = len(s)
        length_g = len(g)
        res = 0
        idx_g = 0
        for i in range(length_s):
            # print(g[i], cookie)
            if g[idx_g] <= s[i]:
                res += 1
                if idx_g + 1 < length_g:
                    idx_g += 1
                else:
                    break

        return res
        
        
# @lc code=end

