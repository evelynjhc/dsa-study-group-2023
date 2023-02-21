import sys
sys.stdin = open('input.txt')

tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        students = {}
        for i in range(1, n+1):
            students[i] = input()

        earings = []
        for i in range(2 * len(students) - 1):
            a, b = list(map(str, input().split()))
            if a not in earings:
                earings.append(a)
            else:
                earings.remove(a)

        for i in earings:
            print(f'{tc} {students[int(i)]}')
            tc += 1


