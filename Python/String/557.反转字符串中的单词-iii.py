# -*- coding:utf-8 -*-

# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#
# 解题思路
# 1.分隔成list，然后每个单词单独反转
# 字符串要转换为list单独反转

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        arr = s.split()
            
        for i,s1 in enumerate(arr):
            s1 = list(s1)
            s1.reverse()
            arr[i] = "".join(s1)
        
        return " ".join(arr)
    
    
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    ret = obj.reverseWords("Let's take LeetCode contest")
    if ret == "s'teL ekat edoCteeL tsetnoc":
        print("reverse success")
    else:
        print("reverse failed")
    
