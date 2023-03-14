import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
menber = []
for _ in range(n):
    menber.append(list(map(str, sys.stdin.readline().split())))

for i in range(n):
    menber[i][0] = int(menber[i][0])

menber.sort(key= lambda x: x[0])

for i in menber:
    print(*i)