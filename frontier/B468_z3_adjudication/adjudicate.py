#!/usr/bin/env python3
"""B468 — the Z/3 "color" handoff (Chat-1, 2026-07-07): the det contradiction
adjudicated exactly, the cross-table computed exactly, the continents settled.

THE CONTRADICTION: Chat-1 claims det(W1) = zeta15^5 = omega (refuting Chat-2's
det = -1-everywhere and my banked det_check). Adjudication below: BOTH SEATS ARE
RIGHT ABOUT DIFFERENT OPERATORS — the third construction-identity resolution of
the night. det(D) = omega EXACTLY (Chat-1's Gauss exponent 455 = C(15,3) is
right FOR D ALONE); det(Wr) = conj(omega) (the Fourier conjugation they
dropped); det(W1) = det(Wr.Wl) = 1 (banked, PR #617). The word family
Par.W1^j.W2^l has det = -1 UNIFORMLY (multiplicativity). The omega^{j+2l}
pattern with slope 2 is exactly what the ELEMENTARY-TWIST family
Par.Wl^j.Wr^l produces: det = -omega^j.conj(omega)^l = -omega^{j+2l}.
"""
import os
import sys
from collections import Counter, deque
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B465_monodromy_intake"))
sys.path.insert(0, os.path.join(HERE, "..", "B467_family_residue_wall"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))

from exact_engine import build, matmul, find_root_of_unity
from det_check import detmod


def part1_dets():
    print("== 1. the det adjudication (exact, F_p at two primes) ==")
    for p in (61, 421):
        z15 = find_root_of_unity(p, 15)
        omega = pow(z15, 5, p)                      # zeta15^5 = the cube root
        z, i4, W1, W2, Par = build(p, c=1)
        # rebuild the elementary factors exactly as the engine does
        N = 15
        gs = sum(pow(z, (j * j) % 15, p) for j in range(15)) % p
        sqrt15 = (-i4 * gs) % p
        inv_s = pow(sqrt15, p - 2, p)
        D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)]
             for i in range(N)]
        dD = detmod(D, p)
        dW1, dW2, dPar = detmod(W1, p), detmod(W2, p), detmod(Par, p)
        # Wr = W1 . D^{-1}
        Dinv = [[pow(D[j][j], p - 2, p) if i == j else 0 for j in range(N)] for i in range(N)]
        Wr = matmul(W1, Dinv, p)
        dWr = detmod(Wr, p)
        print(f"  p={p}: det(D)={'omega' if dD == omega else dD}  "
              f"det(Wr)={'omega^2 (=conj)' if dWr == pow(omega, 2, p) else dWr}  "
              f"det(W1)={dW1}  det(W2)={dW2}  det(Par)={dPar % p == p - 1 and '-1'}")
        assert dD == omega and dWr == pow(omega, 2, p) and dW1 == 1 and dW2 == 1
    print("  VERDICT: Chat-1's mechanism (455 = C(15,3), det D = omega) is right FOR D;")
    print("  the Fourier factor contributes conj(omega); det(W1) = 1 (banked, PR #617).")
    print("  Word family Par.W1^j.W2^l: det = -1 UNIFORMLY (multiplicativity) — Chat-2 right.")
    print("  Elementary-twist family Par.D^j.Wr^l: det = -omega^{j+2l} — Chat-1's pattern,")
    print("  slope 2 = conj on the cube root; 80/80/80 by (j+2l) mod 3 on the 20x12 grid.")
    cnt = Counter((j + 2 * l) % 3 for j in range(20) for l in range(12))
    print(f"  class sizes of (j+2l) mod 3 on Z/20 x Z/12: {dict(cnt)}")


def exact_tiers():
    """B459's exact construction, reproduced: per-point vanishing pattern."""
    from step0_exact_matrices import build_theta_W, matrix_order, pair_smatrix
    import cyclo_engine as E
    W1 = build_theta_W(1)
    W2 = build_theta_W(2)
    _, p1 = matrix_order(W1)
    _, p2 = matrix_order(W2)
    sm = pair_smatrix(p1, p2)
    chan = {i: {(a, b): v[i] for (a, b), v in sm.items() if v[i] != 0} for i in range(4)}
    per_point = {}
    for x in range(20):
        for y in range(12):
            zpat = []
            for i in range(4):
                t = E.ZERO
                for (a, b), val in chan[i].items():
                    t = E.add(t, E.scal(Fr(val), E.zeta((3 * a * x + 5 * b * y) % 60)))
                zpat.append(1 if t == E.ZERO else 0)
            per_point[(x, y)] = tuple(zpat)
    return per_point


TIER = {(0, 0, 0, 0): 'free', (0, 0, 1, 1): 'rs', (0, 1, 0, 1): 'qs',
        (0, 1, 1, 1): 'qrs', (1, 1, 1, 1): 'dark'}


def part2_crosstable(per_point):
    print("\n== 2. the exact tier x (x+2y mod 3) cross-table (B459 machinery) ==")
    table = Counter()
    for (x, y), z in per_point.items():
        table[(TIER[z], (x + 2 * y) % 3)] += 1
    tiers = ['free', 'rs', 'qs', 'qrs', 'dark']
    print(f"  {'tier':>6} | {'c=0':>4} {'c=1':>4} {'c=2':>4} | total")
    for t in tiers:
        row = [table[(t, c)] for c in range(3)]
        print(f"  {t:>6} | {row[0]:>4} {row[1]:>4} {row[2]:>4} | {sum(row)}")
    dark_row = [table[('dark', c)] for c in range(3)]
    print(f"  dark distribution across classes: {dark_row} "
          f"(Chat-1's float claim: 34/9/10 with 53 dark — exact dark total is {sum(dark_row)})")
    return table


def part3_continents(per_point):
    print("\n== 3. the continents (free-tier connected components, exact, torus 4-adjacency) ==")
    free = {pt for pt, z in per_point.items() if z == (0, 0, 0, 0)}
    seen = set()
    sizes = []
    for start in sorted(free):
        if start in seen:
            continue
        comp = 0
        dq = deque([start])
        seen.add(start)
        while dq:
            (x, y) = dq.popleft()
            comp += 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nb = ((x + dx) % 20, (y + dy) % 12)
                if nb in free and nb not in seen:
                    seen.add(nb)
                    dq.append(nb)
        sizes.append(comp)
    print(f"  free tier size: {len(free)}; components: {sorted(sizes, reverse=True)}")
    print(f"  '8 equal continents of 15' claim: "
          f"{'CONFIRMED' if sorted(sizes) == [15]*8 else 'REFUTED as stated (see sizes)'}")
    return sizes


def part4_confinement():
    print("\n== 4. the 'confinement rule' scan (numeric, seam-package complex build) ==")
    N = 15
    zc = np.exp(2j * np.pi / N)
    Dn = np.diag([zc ** ((j * (j - 1) // 2) % N) for j in range(N)])
    F = np.array([[zc ** ((i * j) % N) for j in range(N)] for i in range(N)]) / np.sqrt(N)
    Wl = Dn
    Wr = (F @ Dn @ F.conj().T).conj().T
    W1 = Wr @ Wl
    W2 = Wr @ Wr @ Wl @ Wl
    Par = np.zeros((N, N), complex)
    for j in range(N):
        Par[(-j) % N, j] = 1
    W1p = [np.linalg.matrix_power(W1, j) for j in range(20)]
    W2p = [np.linalg.matrix_power(W2, l) for l in range(12)]
    rng = np.random.default_rng(468)
    viol_nonzero_where_rule_zero = 0
    zero_where_rule_nonzero = 0
    trials = 4000
    for _ in range(trials):
        j1, j2 = rng.integers(0, 20, 2)
        l1, l2 = rng.integers(0, 12, 2)
        val = np.trace(Par @ W1p[j1] @ W2p[l1] @ W1p[j2] @ W2p[l2])
        color_sum = ((j1 + 2 * l1) + (j2 + 2 * l2)) % 3
        if color_sum != 0 and abs(val) > 1e-9:
            viol_nonzero_where_rule_zero += 1
        if color_sum == 0 and abs(val) < 1e-9:
            zero_where_rule_nonzero += 1
    print(f"  {trials} random 4-tuples: nonzero-despite-color!=0: {viol_nonzero_where_rule_zero}; "
          f"zero-despite-color=0: {zero_where_rule_nonzero}")
    print("  the rule 'trace nonzero ONLY when colors sum to 0 mod 3': "
          + ("REFUTED (violations exist)" if viol_nonzero_where_rule_zero else "not refuted"))


if __name__ == '__main__':
    part1_dets()
    pp = exact_tiers()
    part2_crosstable(pp)
    part3_continents(pp)
    part4_confinement()
    print("\nDONE")
