"""Separate Fraction rank implementation; imports no native science or SymPy."""
from fractions import Fraction as F
from itertools import combinations
import json


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def rank(a):
    a = [list(map(F, row)) for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][j]; a[r] = [v/d for v in a[r]]
        for k in range(len(a)):
            if k != r:
                d = a[k][j]
                a[k] = [v-d*w for v,w in zip(a[k], a[r])]
        r += 1
    return r


def exterior(a):
    pairs = list(combinations(range(len(a)), 2))
    result = zeros(len(pairs))
    for row, (k, l) in enumerate(pairs):
        for col, (i, j) in enumerate(pairs):
            result[row][col] = ((a[k][i] if l == j else 0) -
                                (a[l][i] if k == j else 0) +
                                (a[l][j] if k == i else 0) -
                                (a[k][j] if l == i else 0))
    return result


def dims(a, b):
    n = len(a)
    r0 = rank(a+b)
    r1 = rank([[-v for v in rb]+ra for ra,rb in zip(a,b)])
    # Read all entries of d1*d0 independently.
    assert all(sum((-b[i][k]*a[k][j]+a[i][k]*b[k][j] for k in range(n)), F(0)) == 0
               for i in range(n) for j in range(n))
    return [n-r0, 2*n-r0-r1, n-r1]


def run():
    checks = {}
    for p,q in ((0,0),(1,0),(0,1),(1,1),(1,-1),(2,3)):
        a,b = zeros(5),zeros(5)
        a[0][2],a[1][3],a[2][4] = F(1),F(1),F(p)
        b[0][1],b[2][3],b[1][4] = F(1),F(1),F(q)
        checks[f'W:{p}:{q}'] = dims(a,b) == ([1,3,2] if p or q else [2,4,2])
        checks[f'L2W:{p}:{q}'] = dims(exterior(a),exterior(b)) == ([2,5,3] if p or q else [3,6,3])
    # Rational adjoint torus comparators, NOT faithful geometric cusps.
    # Nonzero z's share a fixed nilpotent; its torus quotient is1.
    for z,w in ((1,2),(1,3),(2,5),(-1,2)):
        a = [[F(0),F(-2*z),F(-z*z)],[F(0),F(0),F(z)],[F(0),F(0),F(0)]]
        b = [[F(0),F(-2*w),F(-w*w)],[F(0),F(0),F(w)],[F(0),F(0),F(0)]]
        pi = zeros(6,2); pi[0][0],pi[3][1]=F(1),F(1)
        checks[f'adjoint:{z}:{w}'] = dims(a,b)==[1,2,1]
        checks[f'pi:{z}:{w}'] = rank([v+p for v,p in zip(a+b,pi)])-rank(a+b)==1
    return checks


if __name__ == '__main__':
    result=run()
    print(json.dumps({'checks':result,'total':len(result),'all':all(result.values())}, sort_keys=True))
    raise SystemExit(0 if all(result.values()) else 1)
