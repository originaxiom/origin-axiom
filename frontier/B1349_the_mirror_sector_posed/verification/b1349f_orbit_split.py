"""Settle addendum 1's OPEN item: how do the 8 rational directions split between the two orbits?

Addendum 1 left this "INDICATED, NOT ESTABLISHED", and it is not cosmetic: if the construction is
confined to ONE orbit, the anchor is log2(rationals IN THAT ORBIT), not log2(8). A 4/4 split would
read 2 bits instead of 3.

DONE EXACTLY. The orbit enumeration drifted THREE times in B1348/B1349 on floats (reporting sizes
68, 370, 423, none dividing 720). Here every coordinate is an exact element of Q(zeta_60) and
projective canonicalisation is exact division in that field -- so two directions compare equal iff
they ARE equal. The orbit-stabiliser invariant (|orbit| must divide 720) is asserted, not hoped for.
"""
import importlib.util, os, math
import sympy as sp
from sympy import Rational as Q

HERE = os.path.dirname(os.path.abspath(__file__))
sp2 = importlib.util.spec_from_file_location("exact60", os.path.join(HERE, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(X)
S, T, W, red, conj, mmul, PHI, z = X.S, X.T, X.W, X.red, X.conj, X.mmul, X.PHI, X.z
N = 6; ix = {w: i for i, w in enumerate(W)}; I6 = sp.eye(N)
def cmat(A): return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
R6 = T; L6 = mmul(mmul(cmat(S), cmat(T)), S)

Bev = sp.zeros(N, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1

def restrict(M6):
    """exact restriction to the even sector: Bev is a 0/1 selection, so read off the blocks."""
    rows = [ix[(0,0)], ix[(1,1)], ix[(0,1)], ix[(0,2)]]          # one representative per even basis vec
    out = sp.zeros(4, 4)
    for a, r in enumerate(rows):
        for b in range(4):
            out[a, b] = red(sp.expand(sum(M6[r, t] * Bev[t, b] for t in range(N))))
    return out

R4, L4 = restrict(R6), restrict(L6)
# CONTROL: the restriction must be faithful to the 6-dim action on the even subspace
for M6, M4, nm in [(R6, R4, "R"), (L6, L4, "L")]:
    lhs = sp.Matrix(N, 4, lambda i, j: red(sp.expand(sum(M6[i, t] * Bev[t, j] for t in range(N)))))
    rhs = sp.Matrix(N, 4, lambda i, j: red(sp.expand(sum(Bev[i, t] * M4[t, j] for t in range(4)))))
    assert sp.simplify(lhs - rhs) == sp.zeros(N, 4), f"{nm} does not preserve the even sector"
print("  [PASS] R and L restrict exactly to the theta-even sector (M6 . Bev = Bev . M4)")

def inv60(e):
    """exact inverse in Q(zeta_60) = Q[z]/Phi_60"""
    return red(sp.invert(sp.Poly(red(e), z).as_expr(), PHI, gens=z))

def canon(v):
    """exact projective canonical form: divide by the first nonzero entry."""
    v = [red(sp.expand(x)) for x in v]
    for x in v:
        if sp.simplify(x) != 0:
            iv = inv60(x)
            return tuple(sp.srepr(red(sp.expand(y * iv))) for y in v)
    raise ValueError("zero vector")

def act(M, v):
    return [red(sp.expand(sum(M[i, t] * v[t] for t in range(4)))) for i in range(4)]

RAT = {"e1=(1,0,0,0)": [1, 0, 0, 0], "e2=(0,1,0,0)": [0, 1, 0, 0],
       "e3=(0,0,1,0)": [0, 0, 1, 0], "e4=(0,0,0,1)": [0, 0, 0, 1],
       "(1,0,0,-1/2)": [1, 0, 0, Q(-1, 2)], "(1,0,0,1)": [1, 0, 0, 1],
       "(0,1,1,0)":    [0, 1, 1, 0],        "(0,1,-1/2,0)": [0, 1, Q(-1, 2), 0]}

def orbit(v0, cap=800):
    seen = {canon(v0)}
    frontier = [[sp.sympify(x) for x in v0]]
    while frontier:
        nxt = []
        for v in frontier:
            for M in (R4, L4):
                w = act(M, v)
                k = canon(w)
                if k not in seen:
                    seen.add(k); nxt.append(w)
                    if len(seen) > cap: raise RuntimeError("orbit exceeded cap")
        frontier = nxt
    return seen

print()
print("=" * 78)
print("ORBITS OF THE 8 RATIONAL DIRECTIONS -- exact, with the orbit-stabiliser invariant asserted")
print("=" * 78)
orbits = []            # list of (set, [names])
for name, v in RAT.items():
    O = orbit(v)
    n = len(O)
    assert 720 % n == 0, f"|orbit| = {n} does NOT divide 720 -- orbit-stabiliser violated"
    placed = False
    for rec in orbits:
        if canon(v) in rec[0]:
            rec[1].append(name); placed = True; break
    if not placed:
        orbits.append((O, [name]))
    print(f"  {name:>16s}: |orbit| = {n:3d}   |Stab| = {720 // n:3d}   "
          f"{'(new orbit)' if not placed else '(already seen)'}")

print()
print("=" * 78)
print("THE SPLIT")
print("=" * 78)
for i, (O, names) in enumerate(orbits, 1):
    print(f"  orbit {i}: size {len(O):3d}  contains {len(names)} of the 8 rationals: {names}")
tot = sum(len(n) for _, n in orbits)
assert tot == 8, tot
sizes = sorted(len(n) for _, n in orbits)
print(f"\n  split = {sizes}   over {len(orbits)} distinct orbit(s)")
print(f"  anchor cost if the construction is confined to ONE orbit: "
      f"log2({max(sizes)}) = {math.log2(max(sizes)):.3g} bits")
print(f"  anchor cost if it may use ANY of the 8:                    log2(8) = 3 bits")
