import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    bracket = input()
    stack = []
    result = 1
    for i in bracket:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
        else:
            pass

    else:
        if stack:
            result = 0

    print(f'#{tc} {result}')