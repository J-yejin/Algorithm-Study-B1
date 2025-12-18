D = [(1,0),(0,1),(-1,0),(0,-1)]
def a(s,d):
    rr,rc,br,bc = s
    res = 1
    if (rr*d[0])+(rc*d[1]) >= (br*d[0])+(bc*d[1]):
        while True:
            rdr,rdc = rr+d[0],rc+d[1]
            if 0<=rdr<N and 0<=rdc<M and B[rdr][rdc] != '#':
                if (rdr,rdc) == ans:
                    rr,rc = rdr,rdc
                    res = 0
                    break
                else: rr,rc = rdr,rdc
            else: break
        while True:
            bdr,bdc = br+d[0],bc+d[1]
            if 0<=bdr<N and 0<=bdc<M and B[bdr][bdc] != '#':
                if (bdr,bdc) == ans:
                    return ''
                if bdr == rr and bdc == rc: break
                else: br,bc = bdr,bdc
            else: break
    else:
        while True:
            bdr,bdc = br+d[0],bc+d[1]
            if 0<=bdr<N and 0<=bdc<M and B[bdr][bdc] != '#':
                if (bdr,bdc) == ans:
                    return ''
                br,bc = bdr,bdc
            else: break
        while True:
            rdr,rdc = rr+d[0],rc+d[1]
            if 0<=rdr<N and 0<=rdc<M and B[rdr][rdc] != '#':
                if rdr == br and rdc == bc: break
                elif (rdr,rdc) == ans:
                    res = 0
                    break
                else: rr,rc = rdr,rdc
            else: break
    return (rr,rc,br,bc) if res else 0

N,M = map(int,input().split())

B = [[*input()]for _ in range(N)]
for r in range(N):
    for c in range(M):
        if B[r][c] == 'B':
            blue = (r,c)
            B[r][c] = '.'
        if B[r][c] == 'R':
            red = (r,c)
            B[r][c] = '.'
        if B[r][c] == 'O':
            ans = (r,c)
            B[r][c] = '.'

V = {(*red,*blue)}
S = {(*red,*blue)}
n = 0
f = 1
while S and n<10 and f:
    n+=1
    C = set()
    for d in D:
        if f==0: break
        for s in S:
            A = a(s,d)
            if not A:
                if A == 0:
                    print(n)
                    f = 0
                    break
                else: continue
            elif A not in V: C.add(A)
    if f==0: break
    S = C
    V.update(C)
if f: print(-1)