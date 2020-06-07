#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s):
        stack = []
        res = ""
        multi = 0
        
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


"""
 class Solution(object):
    def decodeString(self, s):
        
        stack = []
        ptr = 0
        
        def get_digital(c, ptr):
            sub = ""
            sub += c
            ptr += 1
            while ptr < len(s) and s[ptr].isdigit():
                sub += s[ptr]
                ptr += 1
            return sub
        
       
        
        while ptr < len(s):
            c = s[ptr]
            if c.isdigit():
                num = get_digital(c, ptr)
                if len(num) > 1:
                    ptr += len(num)
                else:
                    ptr += 1
                
                stack.append(int(num))
            elif c.isalpha() or c == '[':
                stack.append(c)
                ptr += 1
            else:
                ptr += 1
                sub = []
                while stack[-1] != '[':
                    sub.append(stack.pop(-1))
                stack.pop(-1)
                times = stack.pop(-1)
                sub = sub[::-1]
                stack.append("".join(sub) * int(times))
                print("".join(sub) * int(times))
        
        return "".join(stack)
         """
        
# @lc code=end

