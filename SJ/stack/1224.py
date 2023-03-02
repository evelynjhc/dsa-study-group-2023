import sys
sys.stdin = open('input.txt')

# 후위 표기식으로 변환한 문자열을 계산할 함수 생성
# 만약 주어진 문자열을 순회하며 연산자를 만나면
# 스택의 마지막 두 요소를 뽑아서 연산자의 연산 수행 후 스택에 추가
def cal(num_list, stack):
    for num in num_list:
        if num in '*+':
            x = stack.pop()
            y = stack.pop()
            if num == '*':
                stack.append(y * x)
            elif num == '+':
                stack.append(x + y)
        # 연산자가 아닐 경우에는 스택에 숫자로 변환하여 추가
        else:
            stack.append(int(num))
    # 스택의 마지막에 있는 최종 결과값 반환
    return stack[-1]

for tc in range(1, 11):
    n = int(input())
    num_list = input()
    stack = []
    result = []

    # 주어진 문자열을 순회하며, 연산자나 괄호를 만나면
    # 스택에 아무것도 없는 경우에는 연산자를 스택에 추가
    for num in num_list:
        if num in '(*+)':
            if not stack:
                stack.append(num)
            # 스택이 비어있지 않다면, 여는 괄호의 경우에만 바로 스택에 추가
            # 연산자가 곱하기라면, 스택이 비어있지 않고 스택의 마지막 요소가 곱하기인 동안
            # 스택의 마지막 요소들을 result에 추가한 뒤 곱하기 연산자를 스택에 추가
            # 연산자가 곱하기라면, 스택이 비어있지 않고, 스택의 마지막 요소가 곱하기와 더하기인 동안
            # 스택의 마지막 요소들을 뽑아서 result에 추가한 뒤, 더하기 연산자를 스택에 추가
            # 연산자가 닫는 괄호라면, 스택에서 여는 괄호를 만날 때까지 마지막 연산자들을 뽑아서
            # result에 추가한 뒤, 스택에서 여는 괄호를 제거
            else:
                if num == '(':
                    stack.append(num)
                elif num == '*':
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(num)
                elif num == '+':
                    while stack and stack[-1] in '*+':
                        result += stack.pop()
                    stack.append(num)
                elif num == ')':
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
        # 만난 요소가 연산자가 아니라면, result에 추가
        else:
            result += num
    # 문자열을 모두 순회한 후에 스택에 남아있는 요소가 있다면,
    # 없어질 때 까지 스택의 마지막 요소를 뽑아서 result에 추가
    while stack:
        result += stack.pop()
    # 계산 함수에는 result 문자열과 빈 스택을 넣어 호출
    print(f'#{tc} {cal(result, [])}')