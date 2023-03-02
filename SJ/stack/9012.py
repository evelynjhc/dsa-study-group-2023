import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(t):
    result = 'YES'
    stack = []
    for i in input():
        if i == '(':
            stack.append('(')
        else:
            if stack:
                stack.remove(stack[-1])
            else:
                result = 'NO'
    if stack:
        result = 'NO'

    print(result)