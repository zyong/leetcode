# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=709 lang=python
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # if len(str) == 0:
        #     return str
        
        # n = len(str)
        # new_str = ""
        # for i in range(n):
        #     if 65 <= ord(str[i]) <= 90:
        #         new_str += chr(ord(str[i]) + 32)
        #     else:
        #         new_str += str[i]
        # return new_str
        return ''.join([chr(ord(c)+32) if 65 <= ord(c) <= 90 else c for c in str])


# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    ret = obj.toLowerCase("Hello")
    print(ret)
