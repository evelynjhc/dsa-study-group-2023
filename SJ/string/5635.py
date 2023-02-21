import sys
sys.stdin = open('input.txt')

n = int(input())
old = ['a', 12, 31, 2010]
young = ['a', 1, 1, 1990]
for i in range(n):
    name, day, month, year = list(map(str, input().split()))
    if int(year) < int(old[-1]):
        old = [name, day, month, year]
    elif int(year) == int(old[-1]):
        if int(month) < int(old[-2]):
            old = [name, day, month, year]
        elif int(month) == int(old[-2]):
            if int(day) < int(old[-3]):
                old = [name, day, month, year]

    if int(year) > int(young[-1]):
        young = [name, day, month, year]
    elif int(year) == int(young[-1]):
        if int(month) > int(young[-2]):
            young = [name, day, month, year]
        elif int(month) == int(young[-2]):
            if int(day) > int(young[-3]):
                young = [name, day, month, year]

print(young[0])
print(old[0])
