import sys
sys.stdin = open('input.txt')

# 1이 연속되는 숫자가 가장 긴 경우를 찾기 위한 함수를 생성
# 가로줄 단위, 세로줄 단위 문자열을 생성하고
# 행렬의 가로 혹은 세로 길이 중 긴 숫자부터 1을 줄여나가며
# 재귀 함수로 함수 인자에 넣은 값을 찾았을 때,
# 그 값을 반환할 수 있도록 함
def solve(arr, num):
    # 가로 줄 단위 문자열을 생성하여,
    # 행렬의 가로, 세로 중 긴 숫자로 구성된
    # 1이 있는지 확인하는 과정 진행
    for i in range(n):
        for j in range(m):
            if '1' * num in ''.join(arr[i]):
                return num

    # 동일한 과정을 세로 줄 단위 문자열에서 진행
    for i in range(m):
        temp = ''
        for j in range(n):
            temp += arr[j][i]
        if '1' * num in temp:
            return num

    # 만약 인자로 넣은 숫자 만큼 1이 연속되지 않는다면,
    # 동일한 함수에 같은 arr를 넣고 num은 1을 줄여 진행
    return solve(arr, num-1)

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(str, input().split())) for _ in range(n)]

    # 행렬의 가로와 세로 중 긴 것을 함수 인자로 넣어줌
    if n < m:
        num = m
    else:
        num = n

    print(f'#{tc} {solve(arr, num)}')
