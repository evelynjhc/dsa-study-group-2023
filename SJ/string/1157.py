w = input()
w = w.upper()

num = {}
for q in w:
    num[q] = 1

count = 0
for i in range(len(w)):
    num[w[i]] += 1

maxi = max(num.values())
result = []
for i in num:
    if num[i] == maxi:
        result.append(i)

if len(result) > 1:
    print('?')
else:
    print(result[0])