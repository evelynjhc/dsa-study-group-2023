import sys
sys.stdin = open('input.txt')

arr = [[0] * 100 for q in range(100)]
n = int(input())
count = 0
for w in range(n):
    a, b = list(map(int, input().split()))
    for i in range(a, a+10):
        for j in range(b, b+10):
            if arr[i][j] == 0:
                arr[i][j] += 1
                count += 1

print(count)