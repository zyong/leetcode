# -*- ˜coding:utf-8 -*-˜
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # if len(s) == 0:
        #     return 0
        
        # import re
        # arr = re.split("\s+", str.strip(str(s)))
        # if len(arr) > 0:
        #     return len(arr.pop())
        # else:
        #     return len(s)
        return len(s.strip().split()[-1]) if len(s.strip()) > 0 else 0
        # s = s.strip(' ')
        # s_list = s.split(" ")
        # return len(s_list[-1])
        
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    ret =obj.lengthOfLastWord(" aa d cc ") 
    ret =obj.lengthOfLastWord(" a  b c d eew ")
    print(ret)

