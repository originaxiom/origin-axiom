#!/usr/bin/env python3
"""xB014 cells Z1-Z5 -- Path A: the scale ladder.  Sealed in PREREGISTRATION.md
(sha256 bc8a71ed..., commit 63fc1f1, pushed BEFORE this file existed).

B207's banked negative is RE-DERIVED, not cited (xB010).  The base rate decides, not the story.
Gate 5 untouched.
"""
import math
import warnings

import mpmath as mp
import snappy
import sympy as sp

warnings.filterwarnings("ignore")
mp.mp.dps = 30
PHI = (1 + sp.sqrt(5))/2


def v0():
    L = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9
    return mp.mpf(3)**mp.mpf('1.5')/(4*mp.pi**2)*mp.zeta(2)*L/2


def tor(M):
    t = 1
    for c in M.homology().elementary_divisors():
        if c:
            t *= c
    return t


def Z1():
    """RE-DERIVE B207: does its negative cover THIS tower?"""
    print("Z1       RE-DERIVING B207 -- 'the family carries no intrinsic exponential hierarchy'")
    print("         B207 varies m (the METALLIC family R^m L^m). This arc varies n (the CYCLIC")
    print("         TOWER (LR)^n over ONE object). Are they the same family?  Computed:\n")
    print(f"         {'m':>2}  {'R^m L^m':<12}{'volume':>12}{'log lambda_m':>14}   B207's family")
    vols = []
    for m in range(1, 7):
        w = 'R'*m + 'L'*m
        M = snappy.Manifold('b++'+w)
        A = sp.eye(2)
        for ch in w:
            A = A*(sp.Matrix([[1, 1], [0, 1]]) if ch == 'L' else sp.Matrix([[1, 0], [1, 1]]))
        t = int(A.trace())
        lam = (t + sp.sqrt(t*t-4))/2
        v = float(M.volume())
        vols.append(v)
        print(f"         {m:>2}  {w:<12}{v:>12.6f}{float(sp.log(lam)):>14.6f}")
    print(f"\n         B207's volumes: BOUNDED, {vols[0]:.4f} -> {vols[-1]:.4f}, ratio"
          f" {vols[-1]/vols[0]:.3f} -- O(1), and log lambda_m grows LOGARITHMICALLY.")
    assert vols[-1]/vols[0] < 4, "B207's boundedness does not reproduce"
    print("\n         THIS arc's tower, same computation:")
    print(f"         {'n':>2}  {'(LR)^n':<12}{'volume':>12}{'|torsion|':>12}   this arc's family")
    tv = []
    for n in range(1, 7):
        M = snappy.Manifold('b++'+'LR'*n)
        v = float(M.volume())
        tv.append((v, tor(M)))
        print(f"         {n:>2}  {'(LR)^'+str(n):<12}{v:>12.6f}{tor(M):>12}")
    assert tv[-1][0]/tv[0][0] > 5, "the tower is not unbounded"
    # a first draft asserted a MAGNITUDE (tor_6 > 100*tor_2) and it failed at 320 < 500 --
    # a badly chosen test, not a failed fact. The property that matters is the RATE, so it
    # is the rate that is asserted: (1/n) log|torsion| -> log(phi^2), and the step ratio
    # tor_{n+1}/tor_n -> phi^2. Fixed before any verdict.
    rates = [math.log(tv[i][1])/(i+1) for i in range(1, len(tv))]
    target = float(sp.log(PHI**2))
    assert abs(rates[-1] - target) < 0.01, (rates, target)
    assert rates[-1] > rates[0], "the rate is not increasing toward the Mahler measure"
    print(f"\n         volumes UNBOUNDED (linear, ratio {tv[-1][0]/tv[0][0]:.1f} at n=6) and torsion")
    print(f"         EXPONENTIAL ({tv[0][1]} -> {tv[-1][1]}).")
    print("Z1 PASS  B207 IS SCOPED, NOT DISPUTED: it tested the m-family (bounded, logarithmic)")
    print("         and this tower is the n-family (unbounded, exponential). ITS NEGATIVE DOES")
    print("         NOT COVER THIS PATH -- and B207 itself names the entry point as the")
    print("         'entropy/volume' rate, which Z3 computes.")


def Z2():
    """the ladder, against Silver-Williams / Gonzalez-Acuna-Short."""
    print("\nZ2       THE LADDER, against the cited theorem (VERIFIED, not assumed)")
    alex = sp.Poly(sp.expand((sp.Symbol('t')**2 - 3*sp.Symbol('t') + 1)), sp.Symbol('t'))
    roots = sp.solve(alex.as_expr(), sp.Symbol('t'))
    mahler = max(abs(complex(r)) for r in roots)
    print(f"         4_1 Alexander Delta = t^2 - 3t + 1, roots {[sp.nsimplify(r) for r in roots]}")
    print(f"         Mahler measure M(Delta) = {mahler:.10f}   phi^2 = {float(PHI**2):.10f}")
    assert abs(mahler - float(PHI**2)) < 1e-12
    print(f"\n         {'n':>2}{'|torsion|':>12}{'(1/n) log|tor|':>16}{'closed form':>20}")
    fib, luc = [0, 1], [2, 1]
    for _ in range(20):
        fib.append(fib[-1]+fib[-2])
        luc.append(luc[-1]+luc[-2])
    for n in range(2, 10):
        M = snappy.Manifold('b++'+'LR'*n)
        T = tor(M)
        cf = luc[n]**2 if n % 2 else 5*fib[n]**2
        print(f"         {n:>2}{T:>12}{math.log(T)/n:>16.6f}{('L_%d^2' % n if n%2 else '5 F_%d^2' % n):>12} = {cf:<6}")
        assert T == cf, (n, T, cf)
    print(f"\n         so |torsion| = L_n^2 (n odd) and 5 F_n^2 (n even) EXACTLY, and the rate")
    print(f"         converges to log M = log(phi^2) = {float(sp.log(PHI**2)):.10f}.")
    print("Z2 PASS  the cited theorem reproduces, and the torsion is Fibonacci/Lucas exactly.")
    print("         HONEST SCOPE, stated here: this growth is GENERIC -- Silver-Williams applies")
    print("         to EVERY fibred knot. Only the RATE is m004's, and the rate is just its")
    print("         Alexander polynomial, already banked. The ladder's EXISTENCE is not news.")


def Z3():
    """the both-faces ratio."""
    print("\nZ3       THE BOTH-FACES RATIO  log lambda / vol")
    V = v0()
    lam2 = PHI**2
    vol4 = mp.mpf(str(float(snappy.Manifold('m004').volume())))
    r = mp.mpf(str(float(sp.log(lam2))))/vol4
    print(f"         numerator   log lambda = log(phi^2) = {float(sp.log(lam2)):.12f}   <- GOLDEN")
    print(f"         denominator vol(m004)  = 24 * v0     = {mp.nstr(vol4,14)}   <- EISENSTEIN")
    print(f"                                  v0 is (3 sqrt3 / 4 pi^2) zeta(2) L(chi_-3,2) / 2")
    print(f"         ratio  log lambda / vol = {mp.nstr(r,14)}")
    print(f"\n         CONSTANT along the tower, because both scale with n:")
    for n in range(1, 6):
        M = snappy.Manifold('b++'+'LR'*n)
        ln = float(sp.log(PHI**(2*n)))
        print(f"           n={n}: log lambda_n / vol_n = {ln/float(M.volume()):.12f}")
    print("\n         so the ratio combines BOTH cornerstones in one dimensionless number, and")
    print("         it is exactly the quantity B207 named as where a hierarchy would enter.")
    return float(r)


def Z4(r4):
    """THE DECISIVE CELL -- the base rate."""
    print("\nZ4       THE BASE RATE -- is m004 EXTREMAL for log lambda / vol?")
    km = 1/(3*math.pi)
    print(f"         Kojima-McShane: vol <= 3 pi log lambda, so the ratio >= 1/(3pi) = {km:.6f}")
    print(f"         m004's ratio = {r4:.6f}  ({r4/km:.2f}x the bound)\n")
    rows = []
    import itertools
    seen = set()
    for n in range(2, 9):
        for t in itertools.product('LR', repeat=n):
            w = ''.join(t)
            if 'L' not in w or 'R' not in w:
                continue
            if min(w[i:]+w[:i] for i in range(n)) != w:
                continue
            A = sp.eye(2)
            for ch in w:
                A = A*(sp.Matrix([[1, 1], [0, 1]]) if ch == 'L' else sp.Matrix([[1, 0], [1, 1]]))
            tr = int(A.trace())
            if tr <= 2:
                continue
            lam = (tr + math.sqrt(tr*tr-4))/2
            try:
                v = float(snappy.Manifold('b++'+w).volume())
            except Exception:
                continue
            nm = snappy.Manifold('b++'+w).identify()
            nm = nm[0].name().split('(')[0] if nm else w
            if nm in seen:
                continue
            seen.add(nm)
            rows.append((math.log(lam)/v, nm, w, v))
    rows.sort(reverse=True)
    print(f"         {len(rows)} once-punctured-torus bundles (cyclically reduced words, len 2..8)")
    print(f"         ranked by log lambda / vol, top 8:")
    for i, (rr, nm, w, v) in enumerate(rows[:8]):
        print(f"           {i+1:>2}. {nm:<12} {w:<10} vol {v:>9.6f}   ratio {rr:.6f}"
              f"{'   <== m004' if nm == 'm004' else ''}")
    rank = [i for i, x in enumerate(rows) if x[1] == 'm004']
    rank = rank[0]+1 if rank else None
    print(f"\n         m004's rank: {rank} of {len(rows)}   (max = {rows[0][0]:.6f})")
    extremal = (rank == 1)
    print(f"         is m004 the MAXIMUM? {extremal}")
    return extremal, rank, len(rows), rows


def Z5(extremal, rank, N, rows, r4):
    print("\nZ5       VERDICT against the kill condition declared in the seal")
    if extremal:
        print("\nZ5 -> OUTCOME A: m004 IS EXTREMAL for the both-faces ratio among the bundles")
        print("         tested. The ladder carries something object-specific and PATH A LIVES.")
    else:
        print(f"\nZ5 -> OUTCOME B: m004 is rank {rank} of {N} -- NOT extremal.")
        print("         >> PATH A DIES, and the seal required this in one paragraph. <<")
    print("\n         WHAT IS ESTABLISHED EITHER WAY:")
    print("           - B207 is SCOPED, not disputed: its negative tested the m-family and")
    print("             does not cover the n-tower (Z1).")
    print("           - the tower's torsion is EXACTLY L_n^2 / 5 F_n^2 with rate log(phi^2),")
    print("             reproducing Silver-Williams -- but that growth is GENERIC to every")
    print("             fibred knot, so its existence is not news (Z2).")
    print(f"           - the both-faces ratio is {r4:.6f}, constant along the tower, combining")
    print("             the golden numerator with the Eisenstein denominator (Z3).")
    print("\n         WHAT IS NOT CLAIMED: that a dimensionless ladder is a SCALE in the")
    print("         physical sense, or that it crosses B1012's wall -- that wall is about a")
    print("         DIMENSIONFUL quantity and a ladder supplies a dimensionless index. No")
    print("         identification is made (E82) and no physics is read.")


if __name__ == "__main__":
    Z1()
    Z2()
    r4 = Z3()
    ex, rank, N, rows = Z4(r4)
    Z5(ex, rank, N, rows, r4)
    print("\nVERIFIED")
