import sys
sys.stdin = open('input.txt')

# 후위 표기식으로 변환한 식을 계산할 함수 생성
# 주어진 식을 순회하며 연산자를 만나면,
# 스택에서 마지막 두 요소를 뽑아 연산자에 따른 계산 수행
def cal(num_list, stack):
    for num in num_list:
        if num in '*+':
            x = stack.pop()
            y = stack.pop()
            if num == '*':
                stack.append(y * x)  # 순서에 유의
            elif num == '+':
                stack.append(y + x)
        # 만약 연산자가 아니라면 스택에 숫자로 변환하여 추가
        else:
            stack.append(int(num))
    # 최종적으로 스택의 마지막 요소로 있는 전체 계산 값 반환
    return stack[-1]

for tc in range(1, 11):
    n = int(input())
    num_list = input()
    stack = []
    result = ''
    # 주어진 인풋 문자열을 순회하며 연산자를 만나고,
    # 스택이 비어있다면, 스택에 연산자 추가
    for num in num_list:
        if num in '*+':
            if stack == []:
                stack.append(num)
            # 스택이 비어있지 않다면, 곱하기 연산자의 경우,
            # 스택에 남아있는 곱셈들을 모두 result에 추가 한 뒤,
            # 스택에 곱하기 연산자를 추가
            else:
                if num == '*':
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(num)  # 다시 현재 연산자를 추가해주는 과정 잊지 말기
                # 스택이 비어있지 않고, 더하기 연산자의 경우,
                # 스택의 모든 요소를 result에 추가 한 뒤,
                # 스택에 더하기 연산자를 추가
                elif num == '+':
                    while stack:
                        result += stack.pop()
                    stack.append(num)  # 다시 현재 연산자를 추가해주는 과정 잊지 말기
        # 연산자가 아니라면 그냥 result에 추가
        else:
            result += num
    # 문자열 순회를 끝마치고도 스택이 비어있지 않다면,
    # 스택이 비어있게 될 때까지 남은 요소들을 result에 추가
    while stack:
        result += stack.pop()
    # 후위 표기식으로 변환한 문자열과 빈 스택으로 계산 함수 호출
    print(f'#{tc} {cal(result, [])}')