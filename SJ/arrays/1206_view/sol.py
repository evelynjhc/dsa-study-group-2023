import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    build = list(map(int, input().split()))

    home = 0
    di = [-2, -1, 1, 2]
    for i in range(2, n-2):
        mini = 255
        for j in range(4):
            ni = i + di[j]
            if build[i] - build[ni] < 1:
                mini = 0
                continue
            if build[i] - build[ni] < mini:
                mini = build[i] - build[ni]
        home += mini

    print(f'#{tc} {home}')

