#!/usr/bin/env python3
"""B474 — the exact tier x commutator cross-table (see FINDINGS)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B465_monodromy_intake'))
sys.path.insert(0, os.path.join(HERE, '..', 'B468_z3_adjudication'))
from exact_engine import build, matmul
from collections import Counter

def matinv(M, p):
    n = len(M)
    A = [row[:] + [1 if i==j else 0 for j in range(n)] for i,row in enumerate(M)]
    for c in range(n):
        piv = next(i for i in range(c,n) if A[i][c] % p)
        A[c], A[piv] = A[piv], A[c]
        inv = pow(A[c][c], p-2, p)
        A[c] = [(x*inv)%p for x in A[c]]
        for i in range(n):
            if i != c and A[i][c]:
                f = A[i][c]
                A[i] = [(a-f*b)%p for a,b in zip(A[i],A[c])]
    return [r[n:] for r in A]

def commutator_traces(p=61):
    z, i4, W1, W2, Par = build(p, c=1)
    W1p = [[[1 if i==j else 0 for j in range(15)] for i in range(15)]]
    for _ in range(19): W1p.append(matmul(W1p[-1], W1, p))
    W2p = [[[1 if i==j else 0 for j in range(15)] for i in range(15)]]
    for _ in range(11): W2p.append(matmul(W2p[-1], W2, p))
    ctr = {}
    for j in range(20):
        for l in range(12):
            A = W1p[j]; B = W2p[l]
            C = matmul(matmul(A,B,p), matmul(matinv(A,p), matinv(B,p), p), p)
            t = sum(C[i][i] for i in range(15)) % p
            ctr[(j,l)] = t if t <= p//2 else t - p
    return ctr

def main():
    import adjudicate as ADJ
    ctr = commutator_traces()
    pp = ADJ.exact_tiers()
    cross = Counter()
    for (x,y), z_ in pp.items():
        cross[(ADJ.TIER[z_], ctr[(x,y)])] += 1
    ok = (cross[('free',15)] == 0 and cross[('rs',15)] == 20 and cross[('qrs',15)] == 10
          and cross[('qs',-5)] == 20 and cross[('dark',15)] == 54 and cross[('dark',3)] == 16)
    for tier in ['free','rs','qs','qrs','dark']:
        print(tier, {t: cross[(tier,t)] for t in (-5,-1,3,15)})
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
