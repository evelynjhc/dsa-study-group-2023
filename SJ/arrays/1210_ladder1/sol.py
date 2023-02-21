import sys
sys.stdin = open('input.txt')

for q in range(1, 11):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for w in range(100)]

    goal = 0
    for j in range(102): # 리스트의 양 옆에 [0]을 더해준 것 유의
        if arr[99][j] == 2: # 2로 표시되어 있는 마지막 줄 골 찾기
            goal = j

    di = [0, 0, -1] # 좌, 우, 위 방향만으로 이동
    dj = [-1, 1, 0] # 만약 좌,우 길이 있다면 먼저 이동

    i = 99 # i는 99부터 거꾸로 올라가며 조사
    j = goal # j는 goal 위치에서 시작
    while i > 0:
        for k in range(3): # di, dj 리스트의 수 동안
            ni = i + di[k] # 방향 탐색 과정
            nj = j + dj[k]
            if arr[ni][nj] == 1: # 이동과정
                arr[i][j] = 0 # 현재 있는 곳은 0으로 설정
                i = ni # 좌표 새로 지정
                j = nj

    print(f'#{tc} {j-1}')







    # print(f'#{tc}' {result - 1}) # arr를 임의적으로 늘렸던 것 주의