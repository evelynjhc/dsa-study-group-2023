'''
    runtime: 32 ms Beats 65.66%
    memory: 13.7 MB Beats 92.58%
'''

def maxDepth(self, s: str) -> int:
    stack = []
    depth, max_depth = 0, 0
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ')':
            if stack:
                stack.pop()
                depth -= 1
            else:
                return -1 
    if stack:
        return -1
    return max_depth
