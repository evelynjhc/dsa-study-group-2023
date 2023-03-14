import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
word = []
for _ in range(n):
     temp = sys.stdin.readline().strip()
     if temp not in word:
         word.append(temp)

word.sort()
word.sort(key= len)

for i in word:
    print(i)