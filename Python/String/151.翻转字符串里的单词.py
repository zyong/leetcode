# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#
# 解题思路
# 1.先分隔为list，然后反转list
# 2.先反转，然后分list，再每个单词反转

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))
            
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    ret = obj.reverseWords("the sky is blue")
    print(ret)
    
