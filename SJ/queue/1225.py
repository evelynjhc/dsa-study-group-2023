import sys
sys.stdin = open('input.txt')

for case in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    # password 항목 중 0이 생긴다면, 반복을 중단
    # 1 사이클은 1 ~ 5 범위로 구성
    # 맨 앞 숫자에서 i 번를 빼준 후 맨 뒤에 추가
    # 맨 앞 숫자는 삭제
    while True:
        if 0 not in password:
            for i in range(1, 6):
                if password[0]-i > 0:
                    password.append(password[0]-i)
                    password.pop(0)
                # 만약 맨 앞 숫자에서 i를 뺀 값이 0보다 작다면
                # 0으로 숫자를 넣은 뒤 반복문 중단
                else:
                    password.append(0)
                    password.pop(0)
                    break
        else:
            break

    print(f'#{tc}', end= ' ')
    for i in password:
        print(i, end= ' ')
    print()

