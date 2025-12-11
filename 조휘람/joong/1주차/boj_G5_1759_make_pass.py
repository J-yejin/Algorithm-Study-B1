import sys

sys.stdin = open('input.txt')

L, C = map(int, input().split())
word = sorted(input().split())
base = ['a', 'e', 'i', 'o', 'u']
result = ''


def recur(n, k, result, cnt_1, cnt_2):
    if n == L:
        if cnt_1 >= 1 and cnt_2 >= 2:
            print(result)
        return

    for i in range(k, C):
        if word[i] in base:
            recur(n + 1, i + 1, result + word[i], cnt_1 + 1, cnt_2)
        else:
            recur(n + 1, i + 1, result + word[i], cnt_1, cnt_2 + 1)


recur(0, 0, result, 0, 0)
