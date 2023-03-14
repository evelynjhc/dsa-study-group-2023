import sys
sys.stdin = open('input.txt')

# 위치를 조정하며 미로를 풀어갈 함수 생성
# 최초 queue는 now 좌표로 설정
# 방문여부와 이동한 칸 수를 알기 위한 visited 배열 생성
def BFS(arr, now):
    queue = [now]
    visited = [[0] * n for _ in range(n)]

    # queue 존재하는 동안 반복 진행
    # now에는 queue 첫 요소 할당
    while queue:
        now = queue.pop(0)
        # 만약, now == goal 이라면,
        # 골 직전까지의 방문 칸수를 반환
        if now == goal:
            return visited[now[0]][now[1]] - 1
        # 상, 하, 좌, 우 로 좌표를 움직이기 위한 리스트 생성
        # 상하좌우 방향으로 다음 좌표들을 조사하며
        # 다음 좌표가 배열안에 있고, 방문한 적이 없으며,
        # arr 상 벽이 아닐 때, queue에 추가
        # visited 에는 방문한 칸수를 누적해서 저장
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                queue.append([ni, nj])
                visited[ni][nj] = visited[now[0]][now[1]] + 1
    # 최종적으로 goal 도착 불가하다면 0 리턴
    return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    # 도착지점의 좌표 goal 할당
    # 출발지점의 좌표 start 할당
    goal = []
    start = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                goal = [i, j]
            elif arr[i][j] == 2:
                start = [i, j]
    # 함수를 호출하며 함수에는 arr, 출발지점 대입
    print(f'#{tc} {BFS(arr, start)}')
