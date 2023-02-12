'''
    runtime: 1743 ms Beats 16.81%
    memory: 105 MB Beats 5.31%
'''

class Solution:
    def invert_n_reverse(self, s: list[int]) -> list[int]:
        inverted = [num ^ 1 for num in s]
        return list(reversed(inverted))
    
    def bin_str(self, n: int) -> list[int]:
        if n == 1:
            return [0]
        prev = self.bin_str(n - 1)
        return prev + [1] + self.invert_n_reverse(prev)

    def findKthBit(self, n: int, k: int) -> str:
        result = list(map(str, self.bin_str(n)))
        return result[k - 1]
