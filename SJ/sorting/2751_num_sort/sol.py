import sys
sys.stdin = open('input.txt')

num = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    num.append(int(sys.stdin.readline().strip()))

num.sort()

for i in num:
    print(i)