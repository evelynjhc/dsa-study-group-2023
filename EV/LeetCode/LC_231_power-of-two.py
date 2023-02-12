'''
    runtime: 30 ms Beats 87.66%
    memory: 13.9 MB Beats 44.71%
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0 or n % 2:
            return False
        else:
            return self.isPowerOfTwo(n // 2)
