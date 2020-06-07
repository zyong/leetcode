#-*- coding:utf-8 -*-
# 利用模等原理判断字符串是否包含另外一个子串

# 解题思路
# 1.固定一个素数q 为模
# 2.计算P串的长度和S串的长度
# 3.循环计算与P串长度相等的串，比较s子串和P串的模，如果相等就输出，如果不等就剔除头字符，添加一个尾字符
# 重新计算模，重新计算的方式为ts+1 = (d(ts- T[s+1]h) + T[s+m+1]) mod q
# 计算公式使用了霍纳法则，就是不断提取x来构造一个循环的计算结构的发展
# 
# 时间复杂度:预处理时间O(m) 最坏情况匹配时间O((n-m+1)m) 期望匹配时间O(n+m)
# 空间复杂度: O(n)

class Solution(object):
    def rabinkarb(self, text1, text2, d, q):
        n = len(text1)
        m = len(text2)
        h = (d ** (m-1)) % q
        p = 0
        t = 0
        for i in range(0, m):
            p = (d * p + int(text2[i])) % q
            t = (d * t + int(text1[i])) % q

        for s in range(0, n - m):
            if p == t:
                for i in range(m):
                    if text1[s+i] != text2[i]:
                        break
                print(text1[s:s+m], text2)
            t = (d * (t - int(text1[s]) * h) + int(text1[s+m])) % q
            

if __name__ == "__main__":
    obj = Solution()
    obj.rabinkarb('23456', '345', 10, 13) 

        