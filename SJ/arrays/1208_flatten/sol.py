import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        maxi = 1
        maxi_idx = 0
        mini = 100
        mini_idx = 0
        for j in range(len(box)):
            if box[j] > maxi:
                maxi = box[j]
                maxi_idx = j
            if box[j] < mini:
                mini = box[j]
                mini_idx = j
        if maxi - mini <= 1:
            break
        else:
            box[maxi_idx] -= 1
            box[mini_idx] += 1

    result_max = 1
    result_min = 100
    for i in box:
        if i > result_max:
            result_max = i
        if i < result_min:
            result_min = i
    print(f'#{tc} {result_max-result_min}')