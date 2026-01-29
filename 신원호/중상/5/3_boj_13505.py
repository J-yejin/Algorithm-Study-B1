# boj 13505 두수 XOR

# trie라고 하는 자료구조에 대해 알아야 한다...
# 여러개의 문자열 중 내가 찾고자하는 문자열이 존재하는지 확인하기 위한 자료구조 (문자열 검색)
# insert: 문자열을 trie에 추가, search: 특정 문자열이 존재하는지 탐색
# 본 문제에서는 search를 계량하여 number의 각 digit과 반대되는 비트를 가진 숫자를 탐색한다.
# dict를 베이스로 하여 class로 구현

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, number):
        node = self.root
        for digit in number:
            if digit not in node:
                node[digit] = {}
            node = node[digit]
        node['#'] = True

    def search(self, number):
        node = self.root
        digits = []
        for digit in number:
            if digit == '1':
                find = '0'
            else:
                find = '1'
            if find in node:
                digits.append('1')
                node = node[find]
            else:
                digits.append('0')
                node = node[digit]
        return int('0b' + ''.join(digits), 2)

trie = Trie()
N = int(input())
nums = list(map(int ,input().split()))
max_len = len(bin(max(nums))[2:])
binary = []
for num in nums:
    temp = bin(num)[2:]
    if len(temp) < max_len:
        temp = '0' * (max_len - len(temp)) + temp
    binary.append(temp)
for num in binary:
    trie.insert(num)

result = 0
for num in binary:
    temp = trie.search(num)
    if result < temp:
        result = temp
print(result)