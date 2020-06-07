#-*- coding:utf-8 -*-
# 
# KMP 字符串匹配算法
# 算法思想
# 1.计算pattern的前缀和后缀相同的位置，构建一个字典y {字符:index}, 
# 字符就是pattern的每个字符，index就是字符在前缀中对应的位置
# 2.逐一比较字符串，遇到部分匹配的情况就跳到字典y对应的字符位置
# 重复上述逻辑，知道找到结果 or 没有匹配

class Solution(object):
    def kmpMatch(self, text1, text2):
        n = len(text1)
        m = len(text2)
        
        y = self.computePrefix(text2)

        q = 0
        for i in range(n):
            while q > 0 and text2[q] != text1[i]:
                q = y[q]
        
            if text2[q] == text1[i]:
                q = q + 1
            print(i, q, m)
            if q == m:
                print("pattern {} find in {}".format(text2, text1))
                q = y[q-1]
    
    def computePrefix(self, text):
        m = len(text)
        # 前缀匹配位置数组
        next = [0  * 1 for _ in range(m)]
        # 第一个位置为0
        k = -1
        q = 0
        next[0] = -1
        
        while q  < m -1:
            # 判断当前字符和新的前缀值是否匹配，如果不匹配，就找它上一次匹配字符，看与当前字符是否匹配
            # 直到前缀都没有结果 or 找到一个匹配的前缀字符
            # 找到一个匹配字符，k+1表示q字符匹配的位置
            if k == -1 or text[k] == text[q]:
                k += 1
                q += 1
                # print(text, k, q)
                if text[k] == text[q]:
                    next[q] = next[k]
                else:
                    next[q] = k
            else:
                k = next[k]
        return next
    
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.computePrefix('ababaca'))
    
    ret = obj.kmpMatch('bacbabababacabab', 'ababaca')
    
    