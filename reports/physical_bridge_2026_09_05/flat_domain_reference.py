"""Separate stdlib/Fraction-only R89 finite reference; not nonauthor review."""
from fractions import Fraction as F
import json

WORD = "aabbAbAABBaB"


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def derivative(x,y,target):
    matrices = {}
    for name,value in (("a",x),("b",y)):
        n = int(name == target)
        matrices[name] = [[F(value),F(n)],[F(0),F(1)]]
        matrices[name.upper()] = [[1/F(value),-F(n)/F(value)],[F(0),F(1)]]
    p = [[F(1),F(0)],[F(0),F(1)]]
    for c in WORD:
        p = mul(p,matrices[c])
    assert p[0][0] == p[1][1] == 1 and p[1][0] == 0
    return p[0][1]


def rank(rows,cols):
    a = [list(map(F,row)) for row in rows]
    pivot = 0
    for col in range(cols):
        pick = next((i for i in range(pivot,len(a)) if a[i][col]),None)
        if pick is None:
            continue
        a[pivot],a[pick] = a[pick],a[pivot]
        d = a[pivot][col]
        a[pivot] = [z/d for z in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                d = a[i][col]
                a[i] = [v-d*w for v,w in zip(a[i],a[pivot])]
        pivot += 1
    return pivot


def cohomology(x,y,k,attachment=None):
    f = [derivative(x,y,"a"),derivative(x,y,"b")]+[F(0)]*k
    if attachment is None:
        d0 = [[F(x-1)],[F(y-1)]]+[[F(1)] for _ in range(k)]
        n0 = 1
    else:
        n0 = 1+k
        d0 = [[F(x-1)]+[F(0)]*k,[F(y-1)]+[F(0)]*k]
        d0 += [[F(1)]+[F(attachment if i == j else 0) for j in range(k)] for i in range(k)]
    assert all(sum(f[i]*d0[i][j] for i in range(2+k)) == 0 for j in range(n0))
    a,b = rank(d0,n0),rank([f],2+k)
    return [n0-a,2+k-a-b,1-b,0]


def run():
    checked,rows = 0,[]
    for x,y in ((1,1),(-1,1),(1,-1),(-1,-1)):
        base = cohomology(x,y,0)
        assert base == ([1,2,1,0] if (x,y) == (1,1) else [0,0,0,0])
        checked += 1
        for k in range(6):
            b = cohomology(x,y,k)
            want = base if k == 0 else [0,k-base[0]+base[1],base[2],0]
            assert b == want and b[1]-b[0]-b[2]+b[3] == k
            checked += 1
            for t in (0,1,-1):
                c = cohomology(x,y,k,t)
                want = [b[0]+k,*b[1:]] if t == 0 else base
                assert c == want and c[1]-c[0]-c[2]+c[3] == 0
                checked += 1
            rows.append({"x":x,"y":y,"k":k,"relative":b})
    print(json.dumps({"passed":checked,"checks":checked,"rows":rows,"physics_derived":False}),flush=True)


if __name__ == "__main__":
    run()
