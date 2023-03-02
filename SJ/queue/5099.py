import sys
sys.stdin = open('input.txt')

# 화덕의 크기, 피자의 개수를 각각 n,m에 할당
# 몇 번째 피자인지 정보를 남기기 위해서 enumerate 함수를 사용하여 pizza 정보 저장
# 화덕에 들어가 있는 피자 정보를 담기 위한 queue bake 생성
T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    pizza = list(enumerate(map(int, input().split()),start= 1))
    bake = []

    # 화덕의 크기 동안 pizza 첫 번째 요소 bake에 추가
    # pizza 첫 번째 요소 삭제
    for j in range(n):
        bake.append(pizza.pop(0))

    # bake 길이가 1이라면 최종 피자가 결정
    # 그 전까지 반복을 진행
    # bake[0][1] -> 남은 치즈양이 0이 아니면
    # bake 해당 요소 치즈양이 절반으로 줄어든 피자로 교체
    while len(bake) != 1:
        if bake[0][1]//2:
            bake.append((bake[0][0], bake[0][1]//2))
            bake.pop(0)
        # 남은 치즈양이 0이라면
        # 해당 피자를 꺼내고, pizza 첫 번째 요소 bake 이동
        else:
            bake.pop(0)
            if pizza:
                bake.append(pizza.pop(0))

        # bake 길이가 1이라면, 최종 피자가 결정
        # 해당 피자의 인덱스 출력 후 종료
        if len(bake) == 1:
            print(f'#{tc} {bake[0][0]}')
            break
