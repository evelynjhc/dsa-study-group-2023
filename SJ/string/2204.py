import sys
sys.stdin = open('input.txt')

while True:
    n = int(input())
    if n != 0:
        words = []
        copy = []
        for i in range(n):
            word = input()
            words.append(word)
            copy.append(word.lower())

        mini = 0
        for j in range(n):
            if copy[j] < copy[mini]:
                mini = j
        print(words[mini])

    else:
        break