"""FINAL k-table: exponent k in [A,B] = s*mu^k (mu=A^-m t) for the metallic family.

Extends the previously-banked 6 points (m in {1,2}, o in {3,4}) with BRONZE (m=3).
Each cell: scan random Newton on the general-m bundle system (validated against figure-eight
m=1 / silver m=2), keep reps that (i) solve the FULL bundle relations tAt^-1=phi(A),
tBt^-1=phi(B), (ii) are irreducible (Burnside), (iii) have non-central longitude, then read
the integer k of the MATRIX identity [A,B]=s*mu^k. Two independent seed streams per cell.

RESULT (n=3):           o=3        o=4
            m=1 (gold)   k=4        k=3
            m=2 (silver) k=4        k=2
            m=3 (bronze) k=1        k=3      <-- NEW; REFUTES k=4-m(o-3) (would predict 4 and 1)
"""
from __future__ import annotations
import numpy as np
from collections import Counter
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from metallic_construct import newton, irred, exponent


def phiA_phiB(A, B, m):
    C = np.linalg.matrix_power(A, m) @ B          # phi(B) = A^m B
    return A @ np.linalg.matrix_power(C, m), C      # phi(A) = A*(A^m B)^m


def cell(m, o, spec, n=3, seeds=400, want=4):
    out = {}
    for seedbase in (2, 99):
        sp = np.array(spec, complex); sp = sp / np.prod(sp) ** (1.0 / n)
        A = np.diag(sp); rng = np.random.default_rng(seedbase)
        cnt = Counter(); clean = 0; minerr = 9.0
        for s in range(seeds):
            B, t, r = newton(A, m, rng)
            if B is None or r > 1e-10 or abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > 1e4:
                continue
            if not irred(A, B):
                continue
            # full-relation gate
            phiA, phiB = phiA_phiB(A, B, m)
            ti = np.linalg.inv(t)
            if np.max(np.abs(t @ A @ ti - phiA)) > 1e-8 or np.max(np.abs(t @ B @ ti - phiB)) > 1e-8:
                continue
            # non-central longitude gate
            Ai = np.linalg.inv(A); lam = A @ B @ Ai @ np.linalg.inv(B)
            if np.max(np.abs(lam - np.trace(lam) / n * np.eye(n))) < 1e-3:
                continue
            s_, k_, err = exponent(A, B, t, m)
            if err < 1e-8:
                cnt[(s_, k_)] += 1; clean += 1; minerr = min(minerr, err)
            if clean >= want:
                break
        out[seedbase] = (dict(cnt), minerr)
    return out


if __name__ == "__main__":
    w = np.exp(2j * np.pi / 3); i_ = 1j
    cells = [
        (1, 3, [1, w, w ** 2]), (2, 3, [1, w, w ** 2]), (3, 3, [1, w, w ** 2]),
        (1, 4, [1, i_, -i_]),  (2, 4, [1, i_, -i_]),  (3, 4, [1, i_, -i_]),
    ]
    print("k in [A,B]=s*mu^k, mu=A^-m t, SL(3), full-relation + irreducible + non-central-longitude:")
    for m, o, spec in cells:
        res = cell(m, o, spec)
        s2 = res[2]; s99 = res[99]
        agree = set(s2[0]) == set(s99[0]) and len(s2[0]) == 1
        print(f"  m={m} o={o}: seed2={s2[0]} (minerr {s2[1]:.0e})  seed99={s99[0]}  "
              f"{'[robust]' if agree else '[CHECK]'}")
    print("\nPrediction k=4-m(o-3): m=1,2 ok; m=3 predicts o3->4,o4->1 -- BOTH WRONG (got 1 and 3). REFUTED.")
