#!/usr/bin/env python3
"""Verify the relayed |kappa-2| values, and the two structural claims riding on them.

CLAIMED: |kappa-2| is a genuine invariant and a LOWER bound on J, with
  m004 = 1 (attained, per Callahan), m009 = sqrt2, m003 = 4, v2873 = 3 sqrt3, m202 = 7.

Two things to check besides the five numbers:
 (A) INVARIANCE. kappa = tr[a,b] is computed FROM A GENERATING PAIR. E72 (this bench's own
     class) is exactly this symbol carrying two numbers on two different pairs. So: does
     kappa change under Nielsen moves on the pair?
 (B) BOUND DIRECTION. Jorgensen: for non-elementary discrete <A,B>,
        |tr^2 A - 4| + |tr[A,B] - 2| >= 1,
     and J(G) = inf over GENERATING PAIRS of that sum. For any particular pair the sum is
     therefore an UPPER bound on J, not a lower one -- and |kappa-2| alone is only part of
     the sum. Checked numerically below.
"""
import itertools
import numpy as np
import snappy

def M2(S):
    """SnapPy SimpleMatrix -> numpy 2x2 complex"""
    return np.array([[complex(S[0, 0]), complex(S[0, 1])],
                     [complex(S[1, 0]), complex(S[1, 1])]], dtype=complex)

TARGET = {"m004": ("1", 1.0), "m009": ("sqrt2", 2 ** 0.5), "m003": ("4", 4.0),
          "v2873": ("3 sqrt3", 3 * 3 ** 0.5), "m202": ("7", 7.0)}

def tr(M):
    return M[0, 0] + M[1, 1]

def inv2(M):
    d = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    return np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=complex) / d

def comm(A, B):
    return A @ B @ inv2(A) @ inv2(B)

print("=" * 96)
print("THE FIVE VALUES, on the geometric holonomy of the DEFAULT presentation")
print("=" * 96)
print(f"  {'mfld':>7} {'gens':>5} {'|K-2| measured':>16} {'claimed':>10} {'match':>6}"
      f" {'|tr^2 a-4|':>12} {'Jorgensen sum':>14}")
rows = {}
for name, (lbl, val) in TARGET.items():
    M = snappy.Manifold(name)
    G = M.fundamental_group()
    n = G.num_generators()
    a, b = M2(G.SL2C('a')), M2(G.SL2C('b'))
    k = complex(tr(comm(a, b)))
    km2 = abs(k - 2)
    t2 = abs(complex(tr(a)) ** 2 - 4)
    jsum = t2 + km2
    ok = abs(km2 - val) < 1e-6
    rows[name] = dict(n=n, km2=km2, t2=t2, jsum=jsum, claimed=val, ok=ok)
    print(f"  {name:>7} {n:>5} {km2:>16.9f} {lbl:>10} {str(ok):>6} {t2:>12.9f} {jsum:>14.9f}")

print()
print("=" * 96)
print("(A) IS kappa AN INVARIANT?  Nielsen moves on the generating pair (2-generator cases)")
print("=" * 96)
for name in TARGET:
    G = snappy.Manifold(name).fundamental_group()
    if G.num_generators() != 2:
        print(f"  {name:>7}: {G.num_generators()} generators -- not a 2-generator presentation, skipped")
        continue
    base = abs(complex(tr(comm(M2(G.SL2C('a')), M2(G.SL2C('b'))))) - 2)
    vals = {}
    # Nielsen moves that preserve the generated group: (a,b)->(b,a), (a,ab), (a,b^-1), (a^-1,b), (ab,b)
    for lab, (wa, wb) in {"(a,b)": ('a','b'), "(b,a)": ('b','a'), "(a,ab)": ('a','ab'),
                          "(a,B)": ('a','B'), "(A,b)": ('A','b'), "(ab,b)": ('ab','b'),
                          "(a,ba)": ('a','ba'), "(aab,b)": ('aab','b')}.items():
        try:
            k = complex(tr(comm(M2(G.SL2C(wa)), M2(G.SL2C(wb)))))
            vals[lab] = abs(k - 2)
        except Exception as e:
            vals[lab] = None
    spread = max(v for v in vals.values() if v is not None) - min(v for v in vals.values() if v is not None)
    print(f"  {name:>7}: |K-2| over 8 generating pairs -> "
          + ", ".join(f"{l}={v:.6f}" for l, v in vals.items() if v is not None))
    print(f"          {'CONSTANT' if spread < 1e-6 else 'VARIES'}  (spread {spread:.6f})")

print()
print("=" * 96)
print("(B) BOUND DIRECTION: is |kappa-2| a LOWER bound on J, as claimed?")
print("=" * 96)
print("  J(G) = inf over generating pairs of ( |tr^2 A - 4| + |tr[A,B] - 2| ).")
print("  For m004, Callahan/Jorgensen give J = 1 (attained).")
m = rows["m004"]
print(f"  m004: default pair gives |tr^2 a - 4| = {m['t2']:.9f}, |K-2| = {m['km2']:.9f},"
      f" sum = {m['jsum']:.9f}")
print(f"        |K-2| = {m['km2']:.6f} vs J = 1  ->  |K-2| {'>=' if m['km2'] >= 1 else '<'} J")
for name in ("m009", "m003", "v2873", "m202"):
    r = rows[name]
    print(f"  {name:>7}: |K-2| = {r['km2']:.6f}   full sum for this pair = {r['jsum']:.6f}"
          f"   (the sum is an UPPER bound on J; |K-2| alone is <= the sum)")
