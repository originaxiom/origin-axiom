#!/usr/bin/env python3
"""B470 RF3 — the quantum tower at level 15, BOTH alphabets; P-QB verified exactly.
P-QB: det(Par . W(w_n)) = -omega^{(#L - #R)(w_n) mod 3} (from det Wl = omega, det Wr = conj)."""
import sys, os
sys.path.insert(0, os.path.join('..','B465_monodromy_intake'))
sys.path.insert(0, os.path.join('..','B467_family_residue_wall'))
from exact_engine import build, matmul, find_root_of_unity
from det_check import detmod

def word_op(w, Wr, Wl, Par, p):
    M = [[1 if i==j else 0 for j in range(15)] for i in range(15)]
    for ch in w:
        M = matmul(M, Wr if ch=='R' else Wl, p)
    return matmul(Par, M, p)

def tower_words(n, A, B):
    s = {0:"b", 1:"a"}
    for k in range(2,n+1): s[k] = s[k-1]+s[k-2]
    return {k: "".join(A if c=="a" else B for c in s[k]) for k in s}

for p in (61,):
    z15 = find_root_of_unity(p, 15)
    omega = pow(z15, 5, p)
    z, i4, W1, W2, Par = build(p, c=1)
    # elementary factors: Wl = D, Wr = W1 . D^{-1}
    D = [[pow(z,(j*(j-1)//2)%15,p) if i==j else 0 for j in range(15)] for i in range(15)]
    Dinv = [[pow(D[j][j],p-2,p) if i==j else 0 for j in range(15)] for i in range(15)]
    Wr = matmul(W1, Dinv, p)
    for alpha, (Aw, Bw) in [("LETTER", ("R","L")), ("BODY", ("RL","RRLL"))]:
        print(f"== {alpha} tower, p={p} ==", flush=True)
        W = tower_words(10, Aw, Bw)
        ok = True
        for n in range(2, 11):
            w = W[n]
            M = word_op(w, Wr, D, Par, p)
            d = detmod(M, p)
            nl, nr = w.count('L'), w.count('R')
            pred = (-(pow(omega, (nl-nr) % 3, p))) % p
            hit = d == pred
            ok &= hit
            # order of M (bounded)
            P = [row[:] for row in M]; order = None
            for k in range(1, 241):
                if all(P[i][j] % p == (1 if i==j else 0) for i in range(15) for j in range(15)):
                    order = k; break
                P = matmul(P, M, p)
            dsym = '-1' if d == p-1 else ('-w' if d == (-(omega))%p else ('-w2' if d == (-(pow(omega,2,p)))%p else d))
            print(f"  n={n:>2} len={len(w):>3} #L-#R={nl-nr:>3} det={dsym:>3} P-QB={'PASS' if hit else 'FAIL'} ord={order}", flush=True)
        print(f"  P-QB overall: {'VERIFIED' if ok else 'FAILED'}", flush=True)
print("DONE", flush=True)
