# SW Expert Academy
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYYKdGQ6Qh0DFAVw&contestProbId=AV134DPqAA8CFAYh&probBoxId=AYYKdGRKQh4DFAVw&type=PROBLEM&problemBoxTitle=HomeWork&problemBoxCnt=1

import sys
sys.stdin = open('input.txt')

T = 10 # 테스트 케이스는 10개 주어짐
for tc in range(1, T+1): # 테스트 케이스만큼 반복 순회
    weith = int(input()) # 다음 줄 인자를 가로 총 길이로 받음
    build = list(map(int, input().split())) # 다음 줄 인자들을 숫자 리스트로 받음

    house = 0 # 조망권이 확보된 세대는 0개로 시작
    for i in range(2, weith-2): # i가 가로 모든 가로축 요소를 순회하는 동안
        home = [] # 빈 리스트 생성
        if build[i] - build[i-1] >= 1: # 왼쪽 첫 번째 집이 한 칸 이상 낮다면, 홈 리스트에 건물 높이 차이 추가
            home.append(build[i] - build[i-1])
            if build[i] - build[i-2] >= 1: # 왼쪽 두 번째 집이 한 칸 이상 낮다면, 홈 리스트에 건물 높이 차이 추가
                home.append(build[i] - build[i-2])
                if build[i] - build[i+1] >= 1: # 오른쪽 첫 번째 집이 한 칸 이상 낮다면, 홈 리스트에 건물 높이 차이 추가
                    home.append(build[i] - build[i+1])
                    if build[i] - build[i+2] >= 1: # 오른쪽 두 번째 집이 한 칸 이상 낮다면, 홈 리스트에 건물 높이 차이 추가
                        home.append(build[i] - build[i+2])

        if len(home) == 4: # 만약 리스트에 추가된 요소가 4개라면
            min_num = home[0] # 그 중 가장 작은 값을 찾아 리스트를 순회
            for j in home:
                if j < min_num: # j가 최솟값보다 작다면 최솟값 갱신
                    min_num = j
            house += min_num # 최종 최솟값을 하우스 값에 합산

    print(f'#{tc} {house}') # 모든 요소들의 하우스 값 출력