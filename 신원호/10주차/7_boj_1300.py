# boj 1300 K번째 수
# 이분 탐색을 써야겠다는 것에 도달하더라도 바로 끝나지 않는 문제...
# 코드 자체는 간략한 것에 비해 생각해야 할 것이 많았다.

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

# B[n] = ((n - 1)//N + 1) * ((n - 1) % N + 1) 1-base index 기준
# 직접 구현? 메모리고 시간이고 다 터지겠지
# dp? 결국 그 크기만큼 리스트 필요하니까 안될거고
# 그리디도 아마...안될것 같고
# 숫자 크기만 보면 이분 탐색에 준하는 아이디어를 무조건 적용시켜야 할텐데...
# log(10**10) = 33.2 ...

lower = 1
upper = N ** 2

while lower <= upper:
    mid = (lower + upper) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)

    if cnt >= K:
        upper = mid - 1
    else:
        lower = mid + 1

print(lower)