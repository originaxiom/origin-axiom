#!/usr/bin/env python3
"""B1078 -- the rung spectrum is ATTAINED: the paper's eleven-element bound is TIGHT.

Theorem thm:rungspec bounds dim z(S) above by an eleven-element set and Remark
rem:spectrumscope withdraws the claim that the values are attained, because the evidence
was a SAMPLE: 16 coordinate subsets (B1075) plus 440 random rational directions, giving
{12, 30, 78}.  The remark says the realized set "appears on present evidence to be far
smaller" and asks for an enumeration of the subspace lattice rather than a sample.

The subspace lattice of C is infinite, so no sample can close it.  This closes it by
STRUCTURE instead:

  (1) e6 = z(C) (+) V', C acts as literally ZERO on z(C) and semisimply on V'.
  (2) Hence for EVERY subspace S <= C,      dim z(S) = 12 + sum{ m_L : L|_S = 0 },
      so the rung function is the flat-function of a finite hyperplane arrangement --
      30 weights in a 4-dimensional space.  The infinite lattice becomes 109 flats.
  (3) Enumerate the flats.  All eleven values occur.

Steps (1) and (2) are exact over Q (charpoly factorisation).  The plane classification in
step (4) is exact over Q.  The flat enumeration in step (3) is exhaustive at three
FAITHFUL primes -- primes at which the 30 weights stay distinct with the multiplicities
computed exactly over Q.  Scope is stated in FINDINGS.md and repeated at the end here.

QUANTIFIER (COMPUTE_THE_PROGRAM): the ALGEBRA layer, over the object's own charge algebra
C.  Nothing is claimed about the class, the sisters or the rows.

NOT PREREGISTERED, and saying so is part of the record.  This arc grew out of an
exploratory probe sequence -- the structure was found first and the controls written
afterwards.  What protects it instead is that every control is FALSIFIABLE BY THE
CORPUS rather than by this file: the sixteen-subset table must reproduce B1075's exact
values, the (8,16)-plane control must return 6 weights of total multiplicity 18 (=30),
the cubic must generate B866's field K, three independent primes must agree, and every
rung value banked by B866/B874/B892/B1075 by other methods must land in the enumerated
spectrum.  If the arrangement picture were wrong, those fail.  See PREREGISTRATION.md.
"""
import collections
import itertools
import json
import os
import sys
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B1068_j2t_charge_field"))
import e8_build as E                                                   # noqa: E402

E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
DIM = 6 + len(E6_ROOTS)
OF = [i for i in range(6)] + [E.N + E.IDX[r] for r in E6_ROOTS]
INV = {g: i for i, g in enumerate(OF)}
DEG = [8, 14, 16, 22]
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def brk6(u, v):
    return {INV[g]: c for g, c in E.br({OF[i]: c for i, c in u.items()},
                                       {OF[i]: c for i, c in v.items()}).items()}


# ------------------------------------------------------- the charge algebra C, over Q
E6A = sp.Matrix(E.E6_A)
cv = E6A.T.solve(sp.Matrix([2] * 6))
h = {j: Fr(sp.Rational(cv[j]).p, sp.Rational(cv[j]).q) for j in range(6) if cv[j] != 0}
ee = {}
for j in range(6):
    ee = E.vadd(ee, E.ev(tuple(1 if i == j else 0 for i in range(8))))
ff = {}
for j in range(6):
    pos = tuple(1 if i == j else 0 for i in range(8))
    neg = tuple(-t for t in pos)
    q = sp.Rational(cv[j])
    ff = E.vadd(ff, {E.N + E.IDX[neg]: Fr(q.p, q.q) / E.eps(pos, neg)})


def hw(n):
    cands = [r for r in E6_ROOTS
             if int(list(E.br(h, E.ev(r)).values())[0] if E.br(h, E.ev(r)) else 0) == n]
    M = sp.zeros(E.DIM, len(cands))
    for j, r in enumerate(cands):
        for k, val in E.br(ee, E.ev(r)).items():
            M[k, j] = sp.Rational(val.numerator, val.denominator)
    ns = M.nullspace()
    v = {}
    for j, r in enumerate(cands):
        co = sp.Rational(ns[0][j])
        if co:
            v = E.vadd(v, {E.N + E.IDX[r]: Fr(co.p, co.q)})
    return v


x_, y_ = sp.symbols("x y")
tf = x_**5 * y_ - x_ * y_**5
Wf = x_**8 + 14 * x_**4 * y_**4 + y_**8
ADJ = {8: Wf, 14: sp.expand(tf * Wf), 16: sp.expand(Wf**2), 22: sp.expand(tf * Wf**2)}
C = {}
for n in DEG:
    top = hw(n)
    P = sp.Poly(ADJ[n], x_, y_)
    acc, cur = {}, top
    for k in range(n + 1):
        co = P.coeff_monomial(x_**(n - k) * y_**k)
        if co:
            q = sp.Rational(sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n))
            acc = E.vadd(acc, E.vmul(Fr(q.p, q.q), cur))
        cur = E.br(ff, cur)
    C[n] = {INV[g]: c for g, c in acc.items()}

AD = {}
for n in DEG:
    M = sp.zeros(DIM, DIM)
    for j in range(DIM):
        for i, c in brk6(C[n], {j: Fr(1)}).items():
            M[i, j] = sp.Rational(c.numerator, c.denominator)
    AD[n] = M

print("=" * 78)
print("CONTROLS -- run before any result is read")
print("=" * 78)
gate("e6 carrier: 72 roots, dim 78", len(E6_ROOTS) == 72 and DIM == 78)
gate("four charges built at degrees 8/14/16/22", sorted(C) == DEG)
gate("all six pairwise charge brackets vanish (C abelian)",
     not [1 for a, b in itertools.combinations(DEG, 2)
          if any(v != 0 for v in brk6(C[a], C[b]).values())])
zC = sp.Matrix.vstack(*[AD[n] for n in DEG]).nullspace()
gate("dim z(C) = 12, reproducing B1075 and B874 sec.2 exactly over Q", len(zC) == 12,
     f"got {len(zC)}")

# B1075's sixteen-coordinate-subset table, reproduced exactly
tab = {}
for k in range(5):
    for sub in itertools.combinations(DEG, k):
        tab[sub] = DIM if not sub else \
            DIM - sp.Matrix.vstack(*[AD[n] for n in sub]).rank()
exp = {(): 78, (8,): 30, (16,): 30, (8, 16): 30}
gate("B1075's sixteen-subset table reproduced exactly",
     all(tab[s] == exp.get(s, 12) for s in tab),
     "{12, 30, 78} -- the SAMPLE this arc replaces")
if FAILED:
    raise SystemExit("controls failed -- nothing may be read")

# --------------------------------------------- (1) the decomposition, exact over Q
print()
print("=" * 78)
print("(1) THE DECOMPOSITION  e6 = z(C) (+) V'  -- exact over Q")
print("=" * 78)
R = AD[8] + 2 * AD[14] + 3 * AD[16] + 5 * AD[22]
t = sp.symbols("t")
fac = sp.factor_list(R.charpoly(t).as_expr())[1]
orb = []
for f, m in fac:
    d = sp.Poly(f, t).degree()
    if sp.Poly(f, t).as_expr() == t:
        gate(f"the zero weight has multiplicity 12 = dim z(C)", m == 12, f"got {m}")
    else:
        orb.append((d, m))
print(f"\n  charpoly(R) = t^12 * " +
      " * ".join(f"q{d}^{m}" if m > 1 else f"q{d}" for d, m in orb))
print("  weight orbits (Galois orbit size x multiplicity):")
for d, m in sorted(orb):
    print(f"      {d:2d} weights of multiplicity {m}   -> {d*m:2d} dimensions")
NW = sum(d for d, m in orb)
gate("dimensions account exactly: 12 + sum(orbit x mult) = 78",
     12 + sum(d * m for d, m in orb) == 78)
gate("thirty non-zero weights in three Galois orbits", NW == 30, f"got {NW}")
Rp = R.copy()
for _ in range(7):
    Rp = Rp * Rp
V0 = Rp.nullspace()
gate("the generalised zero-space IS z(C) (dim 12)", len(V0) == 12)
B0 = sp.Matrix.hstack(*V0)
gate("C acts as literally ZERO on z(C) -- not merely nilpotently",
     all((AD[n] * B0).is_zero_matrix for n in DEG))

print("""
  CONSEQUENCE, and it is the whole point:

      dim z(S)  =  12  +  sum{ m_L : L a weight with L|_S = 0 }        for EVERY S <= C

  The rung function is the flat-function of an arrangement of 30 hyperplanes in a
  4-dimensional space.  The subspace lattice of C is infinite; its image under dim z
  is not.  A sample cannot close this question and an enumeration can.""")

# --------------------------------------------- (2) the (8,16)-plane, exact over Q
print()
print("=" * 78)
print("(2) THE (8,16)-PLANE, CLASSIFIED COMPLETELY -- exact over Q")
print("=" * 78)
W = AD[16].columnspace()
BW = sp.Matrix.hstack(*W)
gate("W = im(ad x16) has dimension 48", len(W) == 48)


def restrict(M):
    cols = []
    for j in range(BW.cols):
        sol, prm = BW.gauss_jordan_solve(M * BW[:, j])
        cols.append(sol)
    return sp.Matrix.hstack(*cols)


R16, R8 = restrict(AD[16]), restrict(AD[8])
gate("W is invariant under ad(x8) and ad(x16)", True)
gate("ad(x16)|W is invertible", R16.det() != 0)
Q = R16.inv() * R8
cpQ = sp.factor_list(Q.charpoly(t).as_expr())
g = None
for f, m in cpQ[1]:
    if sp.Poly(f, t).degree() == 3:
        g, mg = sp.Poly(f, t), m
gate("charpoly(Q) is a single CUBIC raised to the 16th power",
     g is not None and mg == 16 and len(cpQ[1]) == 1,
     f"exponent {mg} = the jump 46-30 = 16, DERIVED not assumed")
gate("that cubic is irreducible over Q", g.is_irreducible)
u = sp.symbols("u")
cub = sp.Poly(u**3 - 12 * u - 5, u)


def sqfree(n):
    n = int(n)
    s = 1
    for pp, e in sp.factorint(abs(n)).items():
        if e % 2:
            s *= pp
    return s


dg, dc = sp.discriminant(g), sp.discriminant(cub)
gate("its discriminant has the SAME squarefree part as x^3-12x-5",
     sqfree(dg) == sqfree(dc) == 77, f"{sqfree(dg)} vs {sqfree(dc)}")
K = sp.QQ.algebraic_field(sp.rootof(cub.as_expr(), 0))
degs = sorted(sp.Poly(f, t).degree()
              for f, _ in sp.factor_list(sp.Poly(g.as_expr(), t, domain=K))[1])
gate("it acquires a ROOT in K = Q[x]/(x^3-12x-5), so it generates K itself",
     degs == [1, 2], f"factor degrees over K: {degs}")
print("""
  So on the (8,16)-plane, for x = a*x8 + b*x16 and (a,b) != 0:

      dim z(x) = 30 + (16 if -b/a is a root of the cubic, else 0)

  exactly, over ANY field.  Over Q the cubic is irreducible, so the answer is 30 for
  every rational direction -- which is why the sample never saw the 46.  Over K it is
  46 on one line, and over the splitting field on all three.  B866 read this 46 off a
  55-digit numeric spectral gap; here it is exact, and its 16 is derived.""")

# --------------------------------------------- (3) the flats
print()
print("=" * 78)
print("(3) THE FLAT ENUMERATION -- exhaustive, at three faithful primes")
print("=" * 78)


def weights_mod_p(p):
    Mp = {n: [[int(AD[n][i, j].p) * pow(int(AD[n][i, j].q), p - 2, p) % p
               for j in range(DIM)] for i in range(DIM)] for n in DEG}

    def mul(M, v):
        return [sum(M[i][j] * v[j] for j in range(DIM)) % p for i in range(DIM)]
    Rm = [[(Mp[8][i][j] + 2 * Mp[14][i][j] + 3 * Mp[16][i][j] + 5 * Mp[22][i][j]) % p
           for j in range(DIM)] for i in range(DIM)]

    def nullsp(A):
        A = [row[:] for row in A]
        piv, r = [], 0
        for c in range(DIM):
            pr = next((i for i in range(r, DIM) if A[i][c]), None)
            if pr is None:
                continue
            A[r], A[pr] = A[pr], A[r]
            iv = pow(A[r][c], p - 2, p)
            A[r] = [x * iv % p for x in A[r]]
            for i in range(DIM):
                if i != r and A[i][c]:
                    f = A[i][c]
                    A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(DIM)]
            piv.append(c)
            r += 1
        free = [c for c in range(DIM) if c not in piv]
        out = []
        for fc in free:
            v = [0] * DIM
            v[fc] = 1
            for i, c in enumerate(piv):
                v[c] = (-A[i][fc]) % p
            out.append(v)
        return out
    ws = []
    for a in range(p):
        Ea = nullsp([[(Rm[i][j] - (a if i == j else 0)) % p for j in range(DIM)]
                     for i in range(DIM)])
        if not Ea:
            continue
        v = Ea[0]
        nzi = next(i for i in range(DIM) if v[i])
        lam = []
        for n in DEG:
            w = mul(Mp[n], v)
            s = w[nzi] * pow(v[nzi], p - 2, p) % p
            if any((w[i] - s * v[i]) % p for i in range(DIM)):
                return None                     # R fails to separate: not faithful
            lam.append(s)
        ws.append((tuple(lam), len(Ea)))
    if sum(m for _, m in ws) != DIM:
        return None
    return ws


def rk(vs, p):
    A = [list(v) for v in vs]
    r = 0
    for c in range(4):
        pr = next((i for i in range(r, len(A)) if A[i][c] % p), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = pow(A[r][c], p - 2, p)
        A[r] = [x * iv % p for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] % p:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(4)]
        r += 1
    return r


PRIMES = [409, 421, 487]
runs = {}
for p in PRIMES:
    ws = weights_mod_p(p)
    nz = [(l, m) for l, m in ws if any(l)]
    cnt = sorted(collections.Counter(m for _, m in nz).items())
    faithful = len(nz) == 30 and cnt == [(1, 12), (3, 18)]
    gate(f"p={p} is FAITHFUL: 30 distinct weights, multiplicities matching the exact "
         f"Q-orbits", faithful, str(cnt))
    onP = [(l, m) for l, m in nz if l[0] == 0 and l[2] == 0]
    gate(f"p={p} control: exactly 6 weights (total multiplicity 18) vanish on the "
         f"(8,16)-plane, giving 12+18 = 30",
         len(onP) == 6 and sum(m for _, m in onP) == 18)
    flats = {}
    for k in range(5):
        for sub in itertools.combinations(range(30), k):
            vs = [nz[i][0] for i in sub]
            if (rk(vs, p) if vs else 0) != k:
                continue
            r = k
            flats[frozenset(i for i in range(30) if rk(vs + [nz[i][0]], p) == r)] = r
    spec = collections.defaultdict(set)
    for F, r in flats.items():
        spec[12 + sum(nz[i][1] for i in F)].add(4 - r)
    runs[p] = (len(flats), {v: tuple(sorted(d)) for v, d in spec.items()})
    print(f"      -> {len(flats)} flats, spectrum {sorted(spec)}")

gate("all three faithful primes give the SAME flat lattice and the SAME spectrum",
     len({(n, tuple(sorted(s.items()))) for n, s in runs.values()}) == 1)
NF, SPEC = runs[PRIMES[0]]
SPEC = {v: list(d) for v, d in SPEC.items()}
BOUND = [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]
gate("the spectrum equals the paper's eleven-element upper bound EXACTLY",
     sorted(SPEC) == BOUND, str(sorted(SPEC)))

print()
print("=" * 78)
print("THE RESULT")
print("=" * 78)
print(f"\n  {NF} flats.  Realized rung spectrum:\n")
for v in sorted(SPEC):
    print(f"      dim z(S) = {v:2d}   attained at subspaces S of dimension {SPEC[v]}")
print(f"""
  Theorem thm:rungspec bounds dim z(S) by exactly this eleven-element set and calls the
  containment possibly strict.  IT IS TIGHT: every one of the eleven is attained.

  Remark rem:spectrumscope says the realized spectrum "appears on present evidence to be
  far smaller" than the eleven values.  That was the sample talking.  The evidence was 16
  coordinate subsets and 440 random rational directions; the strata carrying the other
  eight values are proper subvarieties, which a random rational direction misses with
  probability 1.  The sample was not unlucky -- it was the wrong instrument.

  In particular dim z(S) = 14 IS attained, at 3-dimensional S.  Theorem thm:smt reads
  "if a 14-dimensional locus occurs, its type is forced".  The occurrence is no longer
  an assumption.""")

CROSS = {12: "B874 sec.2, B1075", 14: "B892 (via B874's amendment)", 18: "B892 (same)",
         30: "B874 sec.1, B1075", 46: "B866", 78: "trivially, S=0"}
print("\n  Independently banked, by other methods, before this arc:")
for v in sorted(CROSS):
    print(f"      {v:2d}  <- {CROSS[v]}")
gate("every independently banked rung value lies in the enumerated spectrum",
     all(v in SPEC for v in CROSS))

RES = {"dim_z_C": 12, "weight_orbits": [[d, m] for d, m in sorted(orb)],
       "n_weights": NW, "n_flats": NF,
       "spectrum": sorted(SPEC),
       "paper_bound": BOUND,
       "bound_is_tight": sorted(SPEC) == BOUND,
       "attained_at_subspace_dims": {str(v): SPEC[v] for v in SPEC},
       "plane_cubic": str(g.as_expr()),
       "plane_cubic_generates_K": degs == [1, 2],
       "faithful_primes": PRIMES,
       "coordinate_subset_sample": sorted({tab[s] for s in tab}),
       "scope": ("Steps (1) and (2) are exact over Q. The flat enumeration is exhaustive "
                 "at three faithful primes, not certified over Qbar: mod-p reduction can "
                 "only ADD linear dependencies among weights, so a flat could in "
                 "principle be coarser than its Qbar counterpart. Three independent "
                 "primes agree, and six of the eleven values are independently banked. "
                 "The exact-over-Qbar flat lattice is registered as the residue.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")

print(f"""
  SCOPE -- what is certified how:
    exact over Q      : dim z(C)=12; the decomposition e6 = z(C) (+) V' with C acting as
                        zero on z(C); the three weight orbits 6x3, 12x1, 12x3; the master
                        formula; the (8,16)-plane cubic and that it generates K.
    three faithful    : the 109 flats and the eleven attained values.
      primes            Mod-p reduction can only ADD dependencies, so this is not yet a
                        Qbar certificate.  Registered as the residue.
    NOT claimed       : anything about the class, the sisters, the rows, or any real form.
                        No physical identification -- Gate 5 untouched.""")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
