#!/usr/bin/env python3
"""B666 cell 4 (R21-9): exhaustive verification of every step of the
pair-evenness proof on the FULL W(D4) (192) and the FULL W(E6) (51840).

Exact arithmetic in every decisive step (python ints / sympy exact).

Steps verified:
  S0  symbolic identities: f self-reciprocal; f(z) = -z*(t - z - 1/z);
      f(z)*f(1/z) = (t - z - 1/z)^2.
  S1  the exact integer charpoly routine (Faddeev-LeVerrier over Z)
      == sympy charpoly on all of W(D4) and on 25 sampled W(E6) elements.
  S2  char_w factors COMPLETELY into cyclotomics, every element.
  S3  the structure identity, every element, as an exact integer
      polynomial identity in x:
        char_{w+w^-1}(x) = (x-2)^{a1} * (x+2)^{a2} * prod_m psi_m(x)^{2*a_m}
      (a_m = multiplicity of Phi_m in char_w; psi_m = min poly of
      zeta_m + zeta_m^-1).  Hence det B_w = char_{w+w^-1}(t) =
      (t-2)^{a1} (t+2)^{a2} * Lambda^2 with Lambda in Z.
  S4  det w = (-1)^{a2} and a1 == a2 (mod 2) (even rank), every element.
  S5  the parity corollary counts on the banked grids:
      odd v_p(t^2-4) -> agreement |W|/|W|; even/control -> exactly |W|/2.
  S6  the per-pair obstruction witness: the Phi_9 orbit at p=3, t=5.
      v_3(psi_9(5)) = 1 (odd) and psi_9 == (x-1)^3 mod 3 (3 totally
      ramified in Q(zeta_9)^+), so the three Galois-conjugate per-pair
      products each carry v_3 = 2/3: per-pair evenness FAILS in the
      ramified case; the ORBIT/TOTAL product = psi_9(5)^2, v_3 = 2, even.
"""
import itertools
import random
import sys

import sympy as sp

random.seed(666)

x, t = sp.symbols('x t')

# ---------------------------------------------------------------- S0
print("== S0: symbolic identities ==")
f = x**2 - t*x + 1
i1 = sp.cancel(x**2 * f.subs(x, 1/x) - f)
i2 = sp.cancel(f - (-x)*(t - x - 1/x))
i3 = sp.cancel(f * f.subs(x, 1/x) - (t - x - 1/x)**2)
assert i1 == 0, i1
assert i2 == 0, i2
assert i3 == 0, i3
print("  f self-reciprocal: x^2 f(1/x) == f(x)          OK")
print("  f(z) == -z*(t - z - 1/z)                        OK")
print("  f(z)*f(1/z) == (t - z - 1/z)^2                  OK")

# ------------------------------------------------- integer poly utils
# polynomials = descending int coefficient lists, leading coeff first

def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] += ai * bj
    return r


def ppow(a, k):
    r = [1]
    for _ in range(k):
        r = pmul(r, a)
    return r


def pdivmod(a, b):
    """divide by MONIC b, exact integer synthetic division."""
    assert b[0] == 1
    a = list(a)
    n, m = len(a), len(b)
    if n < m:
        return [1], a          # caller checks remainder
    q = []
    for i in range(n - m + 1):
        c = a[i]
        q.append(c)
        if c:
            for j in range(1, m):
                a[i + j] -= c * b[j]
    r = a[n - m + 1:]
    return q, r


def peval(a, v):
    r = 0
    for c in a:
        r = r * v + c
    return r


def is_zero(a):
    return all(c == 0 for c in a)

# ------------------------------------------------------ exact matrices

def matmul(A, B):
    n = len(A)
    Bt = list(zip(*B))
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in Bt)
                 for row in A)


def madd(A, B):
    return tuple(tuple(a + b for a, b in zip(ra, rb))
                 for ra, rb in zip(A, B))


def ident(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n))
                 for i in range(n))


def charpoly_int(A):
    """det(xI - A) coefficients, descending, exact (Faddeev-LeVerrier)."""
    n = len(A)
    Mk = ident(n)
    c = [1]
    for k in range(1, n + 1):
        AM = matmul(A, Mk)
        tr = sum(AM[i][i] for i in range(n))
        assert tr % k == 0
        ck = -(tr // k)
        c.append(ck)
        Mk = tuple(tuple(AM[i][j] + (ck if i == j else 0) for j in range(n))
                   for i in range(n))
    return c

# ------------------------------------------- cyclotomic / psi tables
MLIST = [m for m in range(1, 60) if sp.totient(m) <= 6]
PHI = {}
PSI = {}
for m in MLIST:
    PHI[m] = [int(c) for c in sp.Poly(sp.cyclotomic_poly(m, x), x).all_coeffs()]
    if m == 1:
        PSI[m] = [1, -2]
    elif m == 2:
        PSI[m] = [1, 2]
    else:
        mp = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / m), x)
        cs = [int(c) for c in sp.Poly(mp, x).all_coeffs()]
        assert cs[0] == 1
        assert len(cs) - 1 == sp.totient(m) // 2
        PSI[m] = cs
print("== psi_m table (min poly of zeta_m + 1/zeta_m), m with phi(m)<=6 ==")
for m in MLIST:
    print(f"  m={m:2d}  psi_m coeffs (desc) = {PSI[m]}")


def cyclo_factor(cp):
    """factor a product-of-cyclotomics charpoly; return {m: a_m}."""
    rem = list(cp)
    a = {}
    for m in MLIST:
        while len(rem) >= len(PHI[m]):
            q, r = pdivmod(rem, PHI[m])
            if is_zero(r):
                a[m] = a.get(m, 0) + 1
                rem = q
            else:
                break
    assert rem == [1], f"non-cyclotomic residue {rem} in {cp}"
    return a


def predicted_charS(a):
    """(x-2)^{a1} (x+2)^{a2} prod_{m>=3} psi_m(x)^{2 a_m}"""
    r = [1]
    for m, am in a.items():
        if m == 1:
            r = pmul(r, ppow([1, -2], am))
        elif m == 2:
            r = pmul(r, ppow([1, 2], am))
        else:
            r = pmul(r, ppow(PSI[m], 2 * am))
    return r


def lambda_int(a, tv):
    """Lambda = prod_{m>=3} psi_m(t)^{a_m}  (a rational integer)."""
    r = 1
    for m, am in a.items():
        if m >= 3:
            r *= peval(PSI[m], tv) ** am
    return r

# ------------------------------------------------------------- groups

def build_wd4():
    out = []
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((1, -1), repeat=4):
            if signs.count(-1) % 2:
                continue
            M = [[0] * 4 for _ in range(4)]
            for i, j in enumerate(perm):
                M[i][j] = signs[i]
            out.append(tuple(tuple(r) for r in M))
    return out


def build_we6():
    """BFS closure of the six simple reflections (root basis).
    Bourbaki E6: chain 1-3-4-5-6, node 2 attached to 4 (0-indexed here)."""
    adj = {(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)}
    C = [[0] * 6 for _ in range(6)]
    for i in range(6):
        C[i][i] = 2
    for (i, j) in adj:
        C[i][j] = C[j][i] = -1
    gens = []
    for i in range(6):
        S = [list(r) for r in ident(6)]
        for j in range(6):
            S[i][j] -= C[i][j]
        gens.append(tuple(tuple(r) for r in S))
    for s in gens:                       # reflections are involutions
        assert matmul(s, s) == ident(6)
    e = ident(6)
    elems = {e: e}                       # element -> exact inverse
    frontier = [e]
    while frontier:
        nxt = []
        for g in frontier:
            gi = elems[g]
            for s in gens:
                h = matmul(g, s)
                if h not in elems:
                    elems[h] = matmul(s, gi)   # (gs)^-1 = s g^-1
                    nxt.append(h)
        frontier = nxt
    return elems


def inv_from_finite_order(w, cap=40):
    """exact inverse via w^(ord-1); every Weyl element has small order."""
    p = w
    prev = ident(len(w))
    for _ in range(cap):
        if p == ident(len(w)):
            return prev
        prev = p
        p = matmul(p, w)
    raise RuntimeError("order cap exceeded")

# --------------------------------------------------------------- runs

def vp(n, p):
    assert n != 0
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def run_group(name, elems_with_inv, tp_grid, expect, sympy_check_all):
    W = list(elems_with_inv.items())
    n = len(W[0][0])
    print(f"\n== {name}: |W| = {len(W)}, rank {n} ==")
    counts = {(tv, p): 0 for (tv, ps) in tp_grid for p in ps}
    det_plus = 0
    seen_a9 = None
    sample_idx = (set(range(len(W))) if sympy_check_all
                  else set(random.sample(range(len(W)), 25)))
    for idx, (w, wi) in enumerate(W):
        assert matmul(w, wi) == ident(n)
        cw = charpoly_int(w)
        if idx in sample_idx:
            scp = [int(c) for c in
                   sp.Matrix(w).charpoly(x).all_coeffs()]
            assert scp == cw, (scp, cw)                       # S1
        a = cyclo_factor(cw)                                  # S2
        a1, a2 = a.get(1, 0), a.get(2, 0)
        S = madd(w, wi)
        cS = charpoly_int(S)
        assert cS == predicted_charS(a), (cw, cS)             # S3
        detw = cw[-1]            # char_w(0) = det(-w) = det(w), n even
        assert detw == (-1) ** a2                             # S4
        assert (a1 - a2) % 2 == 0                             # S4
        if detw == 1:
            det_plus += 1
        if a.get(9, 0) and seen_a9 is None:
            seen_a9 = (cw, a)
        for (tv, ps) in tp_grid:                              # S5
            detB = peval(cS, tv)
            assert detB != 0
            # structure re-check at the integer level:
            lam = lambda_int(a, tv)
            assert detB == (tv - 2) ** a1 * (tv + 2) ** a2 * lam * lam
            for p in ps:
                if detw == (-1) ** vp(detB, p):
                    counts[(tv, p)] += 1
    print(f"  S1 exact-charpoly vs sympy: {len(sample_idx)} elements   OK")
    print(f"  S2 full cyclotomic factorization: {len(W)}/{len(W)}      OK")
    print(f"  S3 structure identity char_S = (x-2)^a1 (x+2)^a2 prod "
          f"psi^2am: {len(W)}/{len(W)}  OK")
    print(f"  S3' det B_w = (t-2)^a1 (t+2)^a2 Lambda^2, Lambda in Z: "
          f"all (t,w) cells  OK")
    print(f"  S4 det w = (-1)^a2 and a1=a2 mod 2: {len(W)}/{len(W)}    OK")
    print(f"  #(det w = +1) = {det_plus}  (half = {len(W)//2})")
    for (tv, ps) in tp_grid:
        d = tv * tv - 4
        for p in ps:
            v = vp(d, p)
            got = counts[(tv, p)]
            exp = expect[(tv, p)]
            tag = "ODD v_p -> ALL" if v % 2 else "EVEN v_p -> HALF"
            print(f"  S5 t={tv} p={p:2d} v_p(t^2-4)={v} agree {got}/{len(W)}"
                  f"  expected {exp}  [{tag}]")
            assert got == exp, (tv, p, got, exp)
    if seen_a9:
        print(f"  order-9 spectrum present: char_w = {seen_a9[0]}, "
              f"a = {seen_a9[1]}")
    return seen_a9


# W(D4)
wd4 = {w: inv_from_finite_order(w) for w in build_wd4()}
assert len(wd4) == 192
d4_grid = [(4, [2, 3, 13]), (5, [3, 7, 13]), (7, [3, 5, 13]),
           (8, [2, 3, 5, 13])]
d4_expect = {(4, 2): 96, (4, 3): 192, (4, 13): 96,
             (5, 3): 192, (5, 7): 192, (5, 13): 96,
             (7, 3): 96, (7, 5): 192, (7, 13): 96,
             (8, 2): 96, (8, 3): 192, (8, 5): 192, (8, 13): 96}
run_group("W(D4)", wd4, d4_grid, d4_expect, sympy_check_all=True)

# W(E6)
we6 = build_we6()
assert len(we6) == 51840, len(we6)
e6_grid = [(5, [3, 7, 13])]
e6_expect = {(5, 3): 51840, (5, 7): 51840, (5, 13): 25920}
seen = run_group("W(E6)", we6, e6_grid, e6_expect, sympy_check_all=False)
assert seen is not None, "expected a Phi_9 element in W(E6) (degree 9)"

# ---------------------------------------------------------------- S6
print("\n== S6: the per-pair obstruction witness (Phi_9, p=3, t=5) ==")
psi9 = PSI[9]
val = peval(psi9, 5)
print(f"  psi_9 = {psi9}; psi_9(5) = {val} = {sp.factorint(val)}")
assert vp(val, 3) == 1
mod3 = [c % 3 for c in psi9]
target = [c % 3 for c in ppow([1, 1], 3)]
print(f"  psi_9 mod 3 = {mod3}; (x+1)^3 mod 3 = {target}")
assert mod3 == target
print("  v_3(psi_9(5)) = 1 (ODD) and psi_9 == (x+1)^3 mod 3:")
print("  3 is totally ramified in Q(zeta_9)^+ (e = 3, standard cyclotomic")
print("  theory); the unique prime above 3 is Galois-stable, so the three")
print("  Galois-conjugate lambda's carry equal valuation v_3 = 1/3 each;")
print("  each PER-PAIR product lambda^2 has v_3 = 2/3 -- NOT even, not an")
print("  integer.  The ORBIT total is psi_9(5)^2 with v_3 = 2: EVEN.")
print("  => pair-evenness is an ORBIT/TOTAL-level truth; the naive")
print("     per-pair strengthening is FALSE exactly at ramified primes.")

print("\nALL CHECKS PASSED")
