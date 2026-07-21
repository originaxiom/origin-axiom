#!/usr/bin/env python3
"""
B739 Stage B recompute — target B489 (self-interaction tower, cyclic-cover tower of 4_1).

CLAIM KILLED (banked): "The cyclic-cover tower of 4_1 carries SM gauge-symmetry enhancement
(handoff falsification test: DGG of b++(RL)^4); plus 4c: m206(3,1) = 5_2 complement bridging
to the twist-knot SU(3) family."

DISCRIMINATING FACT (two prongs, both recomputed here from the arc's own conventions):
  (A) DGG is abelian at every tower level: b++(RL)^n has N = 2n ideal tetrahedra and 1 cusp
      on its canonical (layered/monodromy) triangulation, hence DGG gauge rank N - c = 2n-1,
      i.e. gauge group U(1)^{2n-1} — abelian, never enhanced.  The handoff's own falsification
      test is n=4: rank 7, U(1)^7.  The only cited nonabelian-enhancement route (Gang-Yonekura
      twist-knot SU(3)) is inapplicable because every level n>=2 has H1 torsion != 0, so is NOT
      a knot complement in S^3 (knot exteriors have H1 = Z).
  (B) 4c: vol(m206(3,1)) = 2.568971 (CLOSED, = m160(1,2)) whereas vol(S^3 \\ 5_2) = 2.828122
      (CUSPED).  Closed != cusped and the volumes differ, so "m206(3,1) = 5_2 complement" is false.

CONVENTIONS DECLARED (E1) — the arc left these implicit; choices made explicit here:
  * Bundle notation: b++(RL)^n = SnapPy once-punctured-torus-bundle 'b++' + 'RL'*n, i.e. the
    mapping torus of A1^n with A1 = R*L = [[2,1],[1,1]] (R=[[1,1],[0,1]], L=[[1,0],[1,1]]).
    SnapPy's constructor yields the layered (monodromy) triangulation: one ideal tetrahedron
    per monodromy letter, so N = 2n; this is the triangulation on which the arc's rank
    formula is evaluated (DGG rank is triangulation-dependent in general).
  * DGG rank formula (the arc's declared convention, per Dimofte-Gaiotto-Gukov, "Gauge
    theories labelled by three-manifolds"): T[M] built from an ideal triangulation with N
    tetrahedra of a c-cusped M has gauge group U(1)^{N-c} — ABELIAN BY CONSTRUCTION.
    What is computable and discriminating in-sandbox: N(n) = 2n and c = 1 (giving rank 2n-1),
    plus the H1 obstruction blocking the twist-knot enhancement theorem.
  * Lucas numbers: L(0)=2, L(1)=1, L(k)=L(k-1)+L(k-2).
  * Alexander polynomial of 4_1: Delta(t) = t^2 - 3t + 1 (normalization irrelevant: only
    |Res(Delta, t^n - 1)| is used; it equals |det(A1^n - I)| since Delta = charpoly(A1)).
  * "Rectangular cusp": Re(cusp modulus) = 0 in SnapPy's default cusp basis, tol 1e-9.
  * Volume tolerance: 1e-9 absolute (SnapPy double precision); banked 6-decimal volumes
    compared after rounding to 6 decimals.
  * Knot-complement obstruction: a knot exterior in S^3 has H1 = Z (Alexander duality);
    torsion(H1) != 0 therefore proves "not a knot complement in S^3".

Determinism: no wall-clock, no randomness, no network.  SnapPy 3.3.2 + sympy exact integer
arithmetic, as declared by the arc ("SnapPy 3.3.2 + exact matrix arithmetic").

Citation chain: the banked kill's pointer to B487/B488 is consistent-with only; the kill is
computed in-arc, so no citation hop is load-bearing.  Nothing here touches CLAIMS; no SM
quantity is computed (Gate 5) — U(1)^{2n-1} is a statement about the mathematical DGG
construction, i.e. the kill itself.
"""

import sys
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
import snappy

checks = []          # (label, passed_bool, detail)


def check(label, passed, detail=""):
    checks.append((label, bool(passed), detail))
    print(f"[{'PASS' if passed else 'FAIL'}] {label}" + (f"  -- {detail}" if detail else ""))


print("=" * 78)
print("B489 recompute: DGG abelianness of the cyclic-cover tower of 4_1, and 4c")
print(f"python {sys.version.split()[0]}, snappy {snappy.__version__}, sympy {sp.__version__}")
print("=" * 78)

# ---------------------------------------------------------------------------
# PART 1 — exact integer arithmetic (no SnapPy): trace/torsion laws of the tower
# ---------------------------------------------------------------------------
print("\n--- PART 1: exact arithmetic of A1 = RL = [[2,1],[1,1]] ---")

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
A1 = R * L
check("A1 = R*L = [[2,1],[1,1]], det 1", A1 == sp.Matrix([[2, 1], [1, 1]]) and A1.det() == 1,
      f"A1={A1.tolist()}")


def lucas(k):
    a, b = 2, 1  # L(0), L(1)
    for _ in range(k):
        a, b = b, a + b
    return a


t = sp.symbols('t')
Delta = t**2 - 3*t + 1  # Alexander polynomial of 4_1 = charpoly of A1
check("Delta_{4_1}(t) = charpoly(A1)", sp.expand(A1.charpoly(t).as_expr() - Delta) == 0)

NMAX = 8
exact = {}  # n -> (trace, torsion_order, invariant_factors)
print(f"\n{'n':>2} {'tr(A1^n)':>9} {'L(2n)':>6} {'|det(A1^n-I)|':>14} {'|L(2n)-2|':>10} "
      f"{'|Res(Delta,t^n-1)|':>18}  SNF torsion")
for n in range(1, NMAX + 1):
    An = A1**n
    tr = int(An.trace())
    d = abs(int((An - sp.eye(2)).det()))
    res = abs(int(sp.resultant(Delta, t**n - 1, t)))
    # Smith normal form of A1^n - I  ->  torsion subgroup of H1(mapping torus)
    snf = smith_normal_form(An - sp.eye(2), domain=sp.ZZ)
    invf = [abs(int(snf[i, i])) for i in range(2)]
    invf_nt = [f for f in invf if f not in (0, 1)]
    exact[n] = (tr, d, invf_nt)
    print(f"{n:>2} {tr:>9} {lucas(2*n):>6} {d:>14} {abs(lucas(2*n)-2):>10} {res:>18}  "
          f"Z/{invf[0]} + Z/{invf[1]} -> torsion {invf_nt}")
    assert tr == lucas(2*n) and d == abs(lucas(2*n) - 2) and res == d

check("trace law tr(A1^n)=L(2n), torsion law |det(A1^n-I)|=|L(2n)-2|=|Res(Delta,t^n-1)| "
      f"(Fox-Weber), n=1..{NMAX}", True)

# odd/even split: L(2n) = L(n)^2 - 2(-1)^n
split_ok = all(lucas(2*n) == lucas(n)**2 - 2*(-1)**n for n in range(1, NMAX + 1))
check("odd/even split L(2n)=L(n)^2-2(-1)^n  (odd n: torsion=L(n)^2; even n: (L(n)-2)(L(n)+2))",
      split_ok,
      "odd torsions " + str([lucas(n)**2 for n in (1, 3, 5, 7)])
      + ", even torsions " + str([(lucas(n)-2)*(lucas(n)+2) for n in (2, 4, 6, 8)]))
check("even-n torsion divisible by 5", all((lucas(n)-2)*(lucas(n)+2) % 5 == 0 for n in (2, 4, 6, 8)))

# ---------------------------------------------------------------------------
# PART 2 — SnapPy tower n=1..8: tets, cusps, DGG rank, volume, H1, cusp shape
# ---------------------------------------------------------------------------
print("\n--- PART 2: the tower in SnapPy — N tets, cusps, DGG rank = N - c, vol, H1, cusp ---")

banked_census = {1: 'm004', 2: 'm206', 3: 's961', 4: 't12839', 5: 'o10_150696', 8: 'otet16_00026'}
banked_H1 = {1: [], 2: [5], 3: [4, 4], 4: [3, 15], 5: [11, 11], 8: [21, 105]}

v4 = float(snappy.Manifold('m004').volume())
print(f"vol(m004) = {v4:.10f}")

tower_ok = True
print(f"\n{'n':>2} {'tets':>4} {'cusps':>5} {'DGGrank':>7} {'gauge grp':>10} {'volume':>13} "
      f"{'vol/v4':>10} {'Re(cusp mod)':>13}  H1 / census")
for n in range(1, NMAX + 1):
    M = snappy.Manifold('b++' + 'RL' * n)
    N_tet = M.num_tetrahedra()
    c = M.num_cusps()
    rank = N_tet - c                     # the arc's DGG rank convention
    vol = float(M.volume())
    mod = M.cusp_info()[0]['modulus']
    H = M.homology()
    # SnapPy homology invariant factors (drop the Z factors and trivial 1s)
    coeffs = [x for x in H.elementary_divisors() if x not in (0, 1)]
    idents = [str(X).split('(')[0] for X in M.identify()]
    row_ok = (N_tet == 2 * n and c == 1 and rank == 2 * n - 1
              and abs(vol - n * v4) < 1e-9
              and abs(complex(mod).real) < 1e-9
              and coeffs == exact[n][2])
    if n in banked_census:
        row_ok = row_ok and (banked_census[n] in idents) and coeffs == banked_H1[n]
    tower_ok = tower_ok and row_ok
    print(f"{n:>2} {N_tet:>4} {c:>5} {rank:>7} {'U(1)^' + str(rank):>10} {vol:>13.9f} "
          f"{vol / v4:>10.7f} {complex(mod).real:>13.2e}  H1={H}  {idents}")

check("tower n=1..8: N=2n tets, 1 cusp  =>  DGG rank 2n-1, gauge group U(1)^{2n-1} (ABELIAN); "
      "vol = n*vol(4_1) to <1e-9; Re(cusp modulus)=0 (rectangular); H1 torsion = SNF(A1^n - I); "
      "census IDs match banked table", tower_ok)

M4 = snappy.Manifold('b++' + 'RL' * 4)
r4 = M4.num_tetrahedra() - M4.num_cusps()
check("handoff falsification test at n=4: DGG rank 7, U(1)^7 — NO enhancement",
      M4.num_tetrahedra() == 8 and M4.num_cusps() == 1 and r4 == 7,
      f"N={M4.num_tetrahedra()}, c={M4.num_cusps()}, rank={r4}")

# general-n statement: N = 2n is structural (one tetrahedron per monodromy letter in the
# layered triangulation), verified above for n=1..8; hence rank = 2n-1 for ALL n under the
# arc's convention.
print("\n(general n: the layered triangulation of b++(RL)^n has one tetrahedron per letter,")
print(" so N=2n, c=1, rank=2n-1 for every n — verified instance-wise for n=1..8 above)")

# ---------------------------------------------------------------------------
# PART 3 — n=2 is THE degree-2 cyclic cover of 4_1
# ---------------------------------------------------------------------------
print("\n--- PART 3: b++(RL)^2 = the unique degree-2 cover of the figure-eight ---")
m004 = snappy.Manifold('m004')
covers_all = m004.covers(2, cover_type='all')
covers_cyc = m004.covers(2, cover_type='cyclic')
iso = covers_cyc[0].is_isometric_to(snappy.Manifold('m206'))
iso2 = covers_cyc[0].is_isometric_to(snappy.Manifold('b++RLRL'))
check("m004 has exactly one degree-2 cover (H1=Z => unique index-2 subgroup), it is cyclic, "
      "and it is isometric to m206 = b++(RL)^2",
      len(covers_all) == 1 and len(covers_cyc) == 1 and iso and iso2,
      f"#covers(all)={len(covers_all)}, #covers(cyclic)={len(covers_cyc)}, "
      f"iso to m206: {iso}, iso to b++RLRL: {iso2}")

# ---------------------------------------------------------------------------
# PART 4 — the enhancement escape route is blocked: n>=2 levels are NOT knot complements
# ---------------------------------------------------------------------------
print("\n--- PART 4: Gang-Yonekura twist-knot SU(3) inapplicable: n>=2 not knot complements ---")
not_knot_ok = all(exact[n][1] > 1 for n in range(2, NMAX + 1))
check("H1 torsion order |L(2n)-2| > 1 for n=2..8  =>  H1 != Z  =>  no level n>=2 is a knot "
      "complement in S^3 (knot exteriors have H1=Z)  =>  the twist-knot SU(3) theorem cannot "
      "apply to any tower level above the base", not_knot_ok,
      "torsion orders n=2..8: " + str([exact[n][1] for n in range(2, NMAX + 1)]))

# ---------------------------------------------------------------------------
# PART 5 — 4c: m206(3,1) vs the 5_2 complement
# ---------------------------------------------------------------------------
print("\n--- PART 5: 4c — 'm206(3,1) = 5_2 complement' refuted on volume + closed/cusped ---")
F = snappy.Manifold('m206(3,1)')
vol_F = float(F.volume())
sol_F = F.solution_type()
# 'filled' status: cusp 0 carries the (3,1) filling, so the manifold is CLOSED
filled = not F.cusp_info()[0]['complete?']
K52 = snappy.Manifold('5_2')
vol_K = float(K52.volume())
cusped_K = K52.num_cusps() == 1 and K52.cusp_info()[0]['complete?']
m160 = snappy.Manifold('m160(1,2)')
iso_alt = F.is_isometric_to(m160)

print(f"m206(3,1): volume = {vol_F:.9f}, solution type = {sol_F}, cusp filled (CLOSED): {filled}")
print(f"5_2 complement: volume = {vol_K:.9f}, cusped: {cusped_K}")
print(f"m206(3,1) isometric to m160(1,2): {iso_alt}  (vol m160(1,2) = {float(m160.volume()):.9f})")
print(f"volume gap |{vol_F:.6f} - {vol_K:.6f}| = {abs(vol_F - vol_K):.6f}")

check("vol(m206(3,1)) = 2.568971 (banked), manifold CLOSED", round(vol_F, 6) == 2.568971 and filled)
check("vol(5_2 complement) = 2.828122 (banked), manifold CUSPED", round(vol_K, 6) == 2.828122 and cusped_K)
check("m206(3,1) = m160(1,2) (banked cross-ID)", bool(iso_alt))
check("4c REFUTED: closed != cusped AND volumes differ by 0.259151 >> tol  =>  "
      "m206(3,1) is NOT the 5_2 complement; the surgery bridge to the twist-knot family is dead",
      filled and cusped_K and abs(vol_F - vol_K) > 0.25)

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
n_fail = sum(1 for _, p, _ in checks if not p)
print(f"CHECKS: {len(checks) - n_fail}/{len(checks)} passed")
if n_fail == 0:
    print("VERDICT: RECONFIRMED — the discriminating fact recomputes true in both prongs:")
    print("  (A) DGG gauge rank of b++(RL)^n is N-c = 2n-1 with N=2n tets, c=1 (verified")
    print("      n=1..8, incl. the n=4 falsification test: rank 7, U(1)^7); the gauge group")
    print("      U(1)^{2n-1} is abelian by the DGG construction, and the twist-knot SU(3)")
    print("      enhancement route is blocked: every level n>=2 has H1 torsion |L(2n)-2| > 1,")
    print("      hence is not a knot complement in S^3.  No SM gauge-symmetry enhancement")
    print("      anywhere in the tower.")
    print("  (B) 4c: vol(m206(3,1)) = 2.568971 (closed, = m160(1,2)) vs vol(5_2 complement)")
    print("      = 2.828122 (cusped): the claimed identification is false.")
else:
    print("VERDICT: NOT RECONFIRMED — see FAIL lines above.")
print("=" * 78)
sys.exit(0 if n_fail == 0 else 1)
