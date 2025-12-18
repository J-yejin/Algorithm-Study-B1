def f(a,b,c):
    if a==0:
        R.append(c)
    if a:
        if a+b>B:
            if (a+b-B,B,c) not in V:
                V.add((a+b-B,B,c))
                f(a+b-B,B,c)
        else:
            if (0,a+b,c) not in V:
                V.add((0,a+b,c))
                f(0,a+b,c)
        if a+c>C:
            if (a+c-C,b,C) not in V:
                V.add((a+c-C,b,C))
                f(a+c-C,b,C)
        else:
            if (0,b,a+c) not in V:
                V.add((0,b,a+c))
                f(0,b,a+c)
    if b:
        if a+b>A:
            if (A,a+b-A,c) not in V:
                V.add((A,a+b-A,c))
                f(A,a+b-A,c)
        else:
            if (a+b,0,c) not in V:
                V.add((a+b,0,c))
                f(a+b,0,c)
        if b+c>C:
            if (a,b+c-C,C) not in V:
                V.add((a,b+c-C,C))
                f(a,b+c-C,C)
        else:
            if (a,0,b+c) not in V:
                V.add((a,0,b+c))
                f(a,0,b+c)
    if c:
        if a+c>A:
            if (A,b,a+c-A) not in V:
                V.add((A,b,a+c-A))
                f(A,b,a+c-A)
        else:
            if (a+c,b,0) not in V:
                V.add((a+c,b,0))
                f(a+c,b,0)
        if c+b>B:
            if (a,B,c+b-B) not in V:
                V.add((a,B,c+b-B))
                f(a,B,c+b-B)
        else:
            if (a,b+c,0) not in V:
                V.add((a,b+c,0))
                f(a,b+c,0)


    return

A,B,C = map(int,input().split())
S = [0,0,C]
V = set()
V.add((0,0,C))
R = []
f(0,0,C)
print(*sorted(R))