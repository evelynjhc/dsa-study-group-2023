'''
    runtime: 123 ms Beats 74.63%
    memory: 14.9 MB Beats 5%
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter, t_counter = Counter(list(s)), Counter(list(t))

        if s_counter == t_counter:
            return 0
        
        differences = s_counter - t_counter
        return sum(differences.values())