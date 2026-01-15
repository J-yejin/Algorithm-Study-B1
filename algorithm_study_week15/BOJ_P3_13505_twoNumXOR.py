# 트라이 자료구조 실습 문제
# 트라이란? 비트마스킹 (이진수)를 활용하여 빠르게 XOR 문제를 해결하기 위한 자료구조
# 어떻게 생겼는가?
# 예. 2 (010) 과 5 (101) 이 있을 때
trie = {
    0:{ # 2의 첫번째 비트
        1:{  # 2의 두번째 비트
            0:{  # 2의 세번째 비트
                ...
            }
        }
    },
    1:{ # 5의 첫번째 비트
        0:{  # 5의 두번째 비트
            1:{  # 5의 세번째 비트
                ...
            }
        }
    }
}

# 이런식으로 십진수를 이진수로 표현해 각각의 자릿수마다의 비트를 저장하는 자료구조


import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 트라이에 숫자를 넣는 함수 (길 뚫기)
def insert(root, num):
    node = root
    # 30번째 비트부터 0번째 비트까지 내려감 (문제 조건상 2^30 미만)
    for i in range(29, -1, -1):
        # 현재 자릿수의 비트 (0 또는 1) 추출
        bit = (num >> i) & 1

        # 해당 비트로 가는 길이 없으면 새로 딕셔너리 생성
        if bit not in node:
            node[bit] = {}

        # 다음 노드(딕셔너리)로 이동
        node = node[bit]


# 트라이에서 최대 XOR 짝을 찾는 함수 -> 노드 활용
def query(root, num):
    node = root
    xor_val = 0

    for i in range(29, -1, -1):
        bit = (num >> i) & 1
        target = 1 - bit  # 내가 원하는 길 (반대 비트)

        # 1. 원하는(반대) 길이 있으면 그쪽으로
        if target in node:
            xor_val += (1 << i)  # 결과값의 해당 자릿수를 1로 만듦
            node = node[target]

        # 2. 없으면 어쩔 수 없이 같은 비트로
        else:
            # XOR 결과는 0이므로 더할 게 없음
            node = node[bit]

    return xor_val


# 트라이의 시작점 (빈 딕셔너리)
trie_root = {}

# [첫 번째 for문]: 모든 숫자를 트라이에 넣기
for num in nums:
    insert(trie_root, num)

max_xor = 0

# [두 번째 for문]: 각 숫자마다 최적의 짝을 찾아 최댓값 갱신
for num in nums:
    # 내 숫자(num)를 던져주면, 가장 큰 XOR 값을 리턴받음
    result = query(trie_root, num)
    max_xor = max(max_xor, result)

print(max_xor)