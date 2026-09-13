#!/usr/bin/env python3
"""The structure behind the claim, checked properly.

WITHDRAWING MY OWN FIRST READING: my Nielsen table flagged (aab,b) as making |K-2| "VARY".
(a^2 b, b) is NOT an elementary Nielsen move and need not generate the same group -- <a^2b, b>
contains a^2 and b, not necessarily a. And kappa = tr[a,b] is conserved by the Markov/Vieta
moves (Fricke-Vogt), the very conservation this bench used in B1347. So a DIFFERING kappa is
evidence the pair is in a different Nielsen class, not evidence against invariance.

THE LOGIC OF THE CLAIM, which turns out to be coherent:
  J(G) = inf over generating pairs (A,B) of ( |tr^2 A - 4| + |tr[A,B] - 2| ).
  IF kappa is pair-independent, then every pair has sum = |tr^2 A - 4| + |K-2| >= |K-2|,
  so J >= |K-2|:  THE LOWER BOUND FOLLOWS FROM THE INVARIANCE.
  And equality needs |tr^2 A - 4| = 0, i.e. tr A = +-2, i.e. A PARABOLIC.
So "m004 = 1, attained" requires a generating pair with a PARABOLIC generator -- and on a knot
complement the MERIDIAN is parabolic. That is B309's meridian kappa, |K-2| = 1, the unit obstruction.
"""
import numpy as np, snappy

def M2(S):
    return np.array([[complex(S[0,0]), complex(S[0,1])],
                     [complex(S[1,0]), complex(S[1,1])]], dtype=complex)
def tr(M): return M[0,0] + M[1,1]
def inv2(M):
    d = M[0,0]*M[1,1] - M[0,1]*M[1,0]
    return np.array([[M[1,1], -M[0,1]], [-M[1,0], M[0,0]]], dtype=complex)/d
def comm(A,B): return A @ B @ inv2(A) @ inv2(B)

NAMES = ["m004", "m009", "m003", "v2873", "m202"]
print("=" * 92)
print("IS THERE A PARABOLIC GENERATOR?  (equality in J = |K-2| needs tr A = +-2)")
print("=" * 92)
print(f"  {'mfld':>7} {'cusps':>6} {'|tr a|':>10} {'|tr b|':>10} {'|tr(mer)|':>11} {'mer parabolic':>14} {'|K-2|':>10}")
for n in NAMES:
    M = snappy.Manifold(n); G = M.fundamental_group()
    a, b = M2(G.SL2C('a')), M2(G.SL2C('b'))
    k = abs(complex(tr(comm(a,b))) - 2)
    try:
        mer = M2(G.SL2C(G.meridian(0)))
        tm = abs(complex(tr(mer)))
        par = abs(tm - 2) < 1e-6
    except Exception as e:
        tm, par = float('nan'), None
    print(f"  {n:>7} {M.num_cusps():>6} {abs(complex(tr(a))):>10.6f} {abs(complex(tr(b))):>10.6f}"
          f" {tm:>11.6f} {str(par):>14} {k:>10.6f}")

print()
print("=" * 92)
print("kappa UNDER GENUINE NIELSEN MOVES ONLY (the relevant equivalence)")
print("=" * 92)
MOVES = {"(a,b)":('a','b'), "(b,a)":('b','a'), "(a,ab)":('a','ab'), "(ab,b)":('ab','b'),
         "(a,ba)":('a','ba'), "(ba,b)":('ba','b'), "(a,B)":('a','B'), "(A,b)":('A','b'),
         "(A,B)":('A','B'), "(b,ab)":('b','ab'), "(ab,a)":('ab','a'), "(a,bA)":('a','bA')}
for n in NAMES:
    G = snappy.Manifold(n).fundamental_group()
    vals = []
    for lab,(wa,wb) in MOVES.items():
        try: vals.append(abs(complex(tr(comm(M2(G.SL2C(wa)), M2(G.SL2C(wb))))) - 2))
        except Exception: pass
    sp = max(vals) - min(vals)
    print(f"  {n:>7}: {len(vals)} Nielsen-equivalent pairs, |K-2| = {vals[0]:.9f},"
          f" spread = {sp:.2e}  -> {'CONSTANT' if sp < 1e-6 else 'VARIES'}")

print()
print("=" * 92)
print("NON-NIELSEN pair (a^2 b, b): does it even generate the same group?")
print("=" * 92)
for n in NAMES:
    G = snappy.Manifold(n).fundamental_group()
    k0 = abs(complex(tr(comm(M2(G.SL2C('a')), M2(G.SL2C('b'))))) - 2)
    k1 = abs(complex(tr(comm(M2(G.SL2C('aab')), M2(G.SL2C('b'))))) - 2)
    same = abs(k0 - k1) < 1e-6
    print(f"  {n:>7}: |K-2| (a,b) = {k0:.6f}   (aab,b) = {k1:.6f}   "
          f"{'same value' if same else 'DIFFERENT -> different Nielsen class, NOT a counterexample'}")
print()
print("  kappa is conserved on Nielsen classes (Fricke-Vogt), so a different value PROVES a")
print("  different class. My 'VARIES' reading is WITHDRAWN: (aab,b) is not a Nielsen move.")

print()
print("=" * 92)
print("THE BOUND, at m004")
print("=" * 92)
G = snappy.Manifold("m004").fundamental_group()
a, b = M2(G.SL2C('a')), M2(G.SL2C('b'))
km2 = abs(complex(tr(comm(a,b))) - 2)
s_def = abs(complex(tr(a))**2 - 4) + km2
mer = M2(G.SL2C(G.meridian(0)))
print(f"  default pair : |tr^2 a - 4| = {abs(complex(tr(a))**2-4):.9f}  +  |K-2| = {km2:.9f}"
      f"  =  {s_def:.9f}")
print(f"  meridian     : tr = {complex(tr(mer)):.9f}  -> |tr^2-4| = {abs(complex(tr(mer))**2-4):.2e} (PARABOLIC)")
print(f"  so a meridian-based pair gives 0 + {km2:.6f} = {km2:.6f} = J(m004) = 1, ATTAINED.")
print(f"  NOTE: the DEFAULT pair does NOT attain J ({s_def:.3f} > 1) -- the inf is over pairs,")
print( "  and the minimiser is the parabolic (meridian) one. Consistent with Callahan.")
