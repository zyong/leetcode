# -*- coding:utf-8 -*-
# 解题思路
# 1. 使用栈结构来存储括号字符，匹配就丢掉，不匹配就返回false，知道检查完所有字符
#     1.设置一个stack
#     2.设置一个dict变量，填充括号字符来验证输入
#     3.python可以循环s，获得每个字符，如果字符不在dict的key里面就存入栈中
#     4.如果字符char在dict的key中，就弹出dict中字符，比较是不是dict的值，如果
#     是就匹配成功，如果不是就匹配失败
# 这个设计巧妙的地方在于使用一个dict来存在括号对，这样处理很方便的解决了验证问题

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        """
        stack = []
        dic = {'}':'{', ']':'[', ')':'('}
        
        for c in s:
            if c in dic:
                top = stack.pop() if stack else '#'
            
                if dic[c] != top:
                    return False
            else:
                stack.append(c)
            
        return not stack

            
