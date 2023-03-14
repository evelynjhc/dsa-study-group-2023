'''
    runtime: 246 ms Beats 18.14%
    memory: 13.9 MB Beats 71.26%
'''

def findTheWinner(self, n: int, k: int) -> int:
    q = deque(range(1, n + 1))

    while len(q) > 1:
        for _ in range(k - 1):
            q.append(q.popleft())
        q.popleft()

    return q[0]