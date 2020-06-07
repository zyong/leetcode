#-*- coding:utf-8 -*-
# BFS题
# 不能进入的格子就是阻塞，其他都是可以正常走的格子
# 每次走的方向是4个，可以使用数组来表示

class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        if not m and not n:
            return 0
        
        used = set()
        q = []
        ans = 0

        q.append((0,0))

        while q:
            i,j = q.pop()
            
            # 这个计算方式快很多，同时通过i == m or j==n 可以避免添加的时候的其他判断
            if i % 10 + i // 10 + j % 10 + j // 10 > k: 
                continue
            ans += 1

            for x,y in [(1,0),(0,1)]:
                i0,j0 = i+x, j+y
                if 0 <= i0 < m and 0 <= j0 < n:
                    if (i0,j0) not in used:
                        q.append((i0,j0))
                        used.add((i0,j0))

        return  ans
    
if __name__ == "__main__":
    obj = Solution()
    ret = obj.movingCount(1,2,1)
    print(ret)