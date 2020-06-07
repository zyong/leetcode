#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#
# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
# 如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
# 示例:

# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"

# 解题思路
# 1.就是每个2k个反转前k个，不足2k的反转前k个，不足k的反转剩余的
# 也就是每次跳过2k反转k个就可以，走到不足2k的时候已经不足k的时候把前k个反转了就好

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

# @lc code=end


