import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 입력된 번호를 순회하기 위하여 문자열로 받음
    # 겹치는 숫자를 확인하고 삭제하기 위한 스택 생성
    n, num = list(map(str, input().split()))
    stack = []
    # 숫자 n의 범위(num 길이)동안 순회하며
    # 스택에 이미 들어가있는 요소가 있고,
    # num i번째 요소와 스택의 마지막 요소가 같다면
    # 스택의 마지막 요소를 삭제하며
    # 그렇지 않다면 num i번째 요소를 스택에 추가
    for i in range(int(n)):
        if stack and stack[-1] == num[i]:
            stack.pop()
        else:
            stack.append(num[i])
    # 스택에 들어 있는 문자열을 더해서 정답 출력
    print(f'#{tc} {"".join(stack)}')