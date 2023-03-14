'''
    runtime: 255 ms Beats 63.30%
    memory: 16.8 MB Beats 37.6%
'''

class BrowserHistory:
    def __init__(self, homepage: str):
        self.visited = deque([homepage])
        self.forwarded = deque()
        self.popped = None

    def visit(self, url: str) -> None:
        self.forwarded.clear()
        self.visited.append(url)

    def back(self, steps: int) -> str:
        steps = self.validate_steps(steps, len(self.visited) - 1)
        for _ in range(steps):
            self.forwarded.append(self.visited.pop())
        return self.visited[-1]

    def forward(self, steps: int) -> str:
        steps = self.validate_steps(steps, len(self.forwarded))
        for _ in range(steps):
            self.visited.append(self.forwarded.pop())
        return self.visited[-1]
    
    def validate_steps(self, steps: int, stack_size: int):
        return steps if stack_size > steps else stack_size