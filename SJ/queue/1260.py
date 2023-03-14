import sys
sys.stdin = open('input.txt')

# 깊이 우선 탐색을 위한 함수 생성
# stack 추가 시, 길이 많을 때 문제 발생
# 재귀함수로 풀이
def DFS(s):
    stack = [s]
    visit_dfs[s] = 1

    while stack:
        now = stack.pop()
        print(now, end= ' ')
        for j in range(1, v+1):
            if arr[now][j] == 1 and visit_dfs[j] == 0:
                DFS(j)

# 넓이 우선 탐색을 위한 함수 생성
# queue 이용 방식
def BFS(s):
    queue = [s]
    visit_bfs[s] = 1

    while queue:
        now = queue.pop(0)
        print(now, end= ' ')
        for j in range(1, v+1):
            if arr[now][j] == 1 and visit_bfs[j] == 0:
                queue.append(j)
                visit_bfs[j] = 1
    return

# 주어지는 인자들을 받아 길 정보 표시
v, e, s = list(map(int, sys.stdin.readline().split()))
arr = [[0] * (v+1) for _ in range(v+1)]

for i in range(e):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr[a][b] = arr[b][a] = 1

# 방문 여부 확인을 위한 배열 생성
visit_dfs = [0] * (v+1)
visit_bfs = [0] * (v+1)

DFS(s)
print()
BFS(s)
