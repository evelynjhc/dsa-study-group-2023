n  = input()

num = []
for i in n:
    num.append(int(i))

new = ''
for j in range(len(num)):
    maxy = num[0]
    for i in num:
        if i > maxy:
            maxy = i
    new += str(maxy)
    num.remove(maxy)

print(new)