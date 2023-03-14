import sys
sys.stdin = open('input.txt')

while True:
    s = input()
    if s == '.':
        break
    else:
        result = 'yes'
        stack = []
        for i in s:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'
        if stack:
            result = 'no'

    print(result)