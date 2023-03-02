import sys
sys.stdin = open('input.txt')

# 후위 표기식으로 바꾼 문자열 result를 계산할 함수 생성
# 문자열을 순회하며 문자열의 요소가 연산자가 아니라면,
# 스택에 숫자로 변환한 해당 요소를 추가
# 연산자를 만나면 이전 두 값을 빼내어 해당 연산 수행
# 최종적으로 스택의 마지막 요소는 전 요소를 계산한 값
def cal(num_list, stack):
    for num in num_list:
        if num != '+':
            stack.append(int(num))
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
    return stack[-1]

for tc in range(1, 11):
    n = int(input())
    num_list = input()
    stack = []
    result = ''

    # 인풋 값을 순회하며 연산자를 만나면
    # 스택이 비었는지 확인 후,
    # 비어있지 않으면 스택의 마지막 요소를 꺼내 result에 추가
    # 비어있다면 스택에 해당 연산자 추가
    for num in num_list:
        if num == '+':
            if stack:
                result += stack.pop()
                stack.append(num)
            else:
                stack.append(num)
        # 만약 만난 값이 연산자가 아니라면,
        # result에 해당 숫자를 추가
        else:
            result += num
    # 과정이 끝난 이후에 스택에 남아있는 요소는
    # 모두 result에 추가
    while stack:
        result += stack.pop()

    print(f'#{tc} {cal(result, [])}')