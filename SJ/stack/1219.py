import sys
sys.stdin = open('input.txt')

# 좌표를 이동하며 길을 찾을 함수 생성
# 스택은 처음에 스타트를 넣고 시작하며
# 방문 여부 판별을 위한 visited 리스트 생성
def DFS(start):
    stack = [start]
    visited = [0] * 100
    # 스택이 있는 동안 반복을 진행하며
    # 스타트는 스택의 마지막 요소를 뽑아서 할당
    while stack:
        start = stack.pop()
        visited[start] = 1
        # 도착해야할 곳은 99이므로,
        # 조사 도중 도착했다면 1을 반환
        if start == 99:
            return 1
        # 배열의 범위 동안 스타트에서 쉬프트로 갈 수 있는 길이 있고,
        # 이전에 쉬프트에 방문한 적이 없다면,
        # 스택에 쉬프트를 추가
        for shift in range(100):
            if load[start][shift] == 1 and visited[shift] == 0:
                stack.append(shift)
    # 스택이 모두 없어졌는데도 1이 반환되지 않았다면 0을 반환
    return 0

# 데이터는 주어지는 길을 표시하기 위한 출발지, 도착지 정보 쌍이며
# 로드는 데이터 정보를 표시하기 위한 배열
for q in range(10):
    tc, e = list(map(int, input().split()))
    data = list(map(int, input().split()))
    load = [[0] * 100 for _ in range(100)]

    # 정보 쌍이 주는 길 존재 여부를 로드에 1로 표기
    for i in range(e):
        load[data[i*2]][data[i*2+1]] = 1

    print(f'#{tc} {DFS(0)}')
