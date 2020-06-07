# -*- coding:utf-8 -*-
from functools import lru_cache

@lru_cache(maxsize=128)
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        def _fib(N):
            if N in (0,1):
                return N
            return _fib(N-1) + _fib(N-2)
        
        return _fib(N)

# class Solution(object):
#     def fib(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
        
# #         0 or 1 都是自己
#         if (N < 2):
#             return N
        
        
#         f1 = 0
#         f2 = 1
#         f3 = 1
#         for _ in range(2, N + 1):
#             f3 = f2 + f1
#             f1 = f2
#             f2 = f3
            
#         return f3
    

if __name__ == "__main__":
    obj = Solution()
    import math
    import time
    from datetime import datetime
    
    start = time.time()
    mstart = datetime.utcnow()
    ret = obj.fib(100)
        
    end = time.time()
    print((end - start) * 1000)