'''
    runtime: 342 ms Beats 13.3%
    memory: 16.1 MB Beats 45.85%
'''

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        dev_per_row = [Counter(row)['1'] for row in bank if Counter(row)['1']]
        row_count = len(dev_per_row)
        
        if row_count <= 1:
            return 0
        
        beam_count = 0
        for i in range(row_count - 1):
            beam_count += dev_per_row[i] * dev_per_row[i + 1]
        return beam_count
