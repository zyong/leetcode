# -*- coding:utf-8 -*-
# 125. 验证回文串
# 首先是什么是回文，它是对给你的文本，不论正着反着内容都是一样的，这个是回文。
# 解题思路
# 1.去掉输入文本中非字母和数字字符
# 2、验证逆序字符是否正确
#
class palindrome(object):
    def isPalindrome(self, s):
        """
         :type s: str
        :rtype: bool
        """
        s = s.lower()
        filtered_s = self._filterAlphaAndNumber(s)
        return filtered_s == filtered_s[::-1]

    def _filterAlphaAndNumber(self, s):
        import re
        s = re.sub(r'[^a-z0-9]+', "", s)
        return s
    
if __name__ == "__main__":
    obj = palindrome()
    obj.isPalindrome('A man, a plan, a canal: Panama')

        
        