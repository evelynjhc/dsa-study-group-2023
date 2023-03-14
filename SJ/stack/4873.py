import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    w = input()
    stack = []
    for i in w:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')
