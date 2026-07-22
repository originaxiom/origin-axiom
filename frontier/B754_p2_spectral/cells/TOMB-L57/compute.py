#!/usr/bin/env python3
"""B754 P2 cell — TOMB-L57 (the CS-crossover k~4 <-> n=4 value-kill) vs the banked
spectral face (B737 / B739 / B746 / B753, frozen per PREREGISTRATION.md).

KILLED CLAIM (speculations/TOMBSTONES.md L57 block): "the Chern-Simons level crosses
over near k~4, matching the rank n=4" read as structure.  KILL (B742 Stage-B recompute,
frontier/B742_negatives_hunt_p1/recompute/TOMB-L57/): k_c(m) = 2*pi/theta_m - 2 with
theta_m = max geometric-tetrahedron shape arg is m-DEPENDENT (4, 2, 1.7645 at m=1,2,3)
=> a figure-eight-volume coincidence, not structure.

WHAT THE KILL NEVER TESTED (the B' exposure): a LEVEL-INDEXED re-derivation of k_c —
the revival hypothesis names the congruence tower (m003 at level (2), m004 at level (4);
filtration named per E23: the ray-class filtration Cl_n = (O/n)^x / im(mu_6) over
O = Z[omega], K = Q(sqrt(-3)), n in {(2),(4),(8)} — the exact filtration B737 computes
in-arc; level assignments banked there from B734 + cc3 addendum, three-seat, with the
in-arc computed shadow = the conductor-4 cusp order of m004).

THIS CELL consults the frozen face against exactly that gap: it varies the LEVEL at
FIXED geometry (the sister pair m003/m004: same volume, same shape data, different
banked level) — the converse of the kill's sweep, which varied geometry (m) and never
touched level.  Every face-source fact used is (i) grep-verified inside the cited arc's
committed artifact and (ii) recomputed here as its computable shadow.

Conventions C1-C4 are the kill's own (B742 recompute, re-declared verbatim in spirit):
  C1 metallic member m = punctured-torus bundle b++ R^m L^m (m=1 == m004, checked);
  C2 level-k phase lattice (2*pi/(k+2))*Z;
  C3 theta_m = max arg over geometric tetrahedron shapes;
  C4 k_c = 2*pi/theta_m - 2.
Gate 5: pure mathematics (shapes, volumes, levels, zeta values); no SM quantities.
Gate 5-Q: Q2 discrimination computed in section [2] BEFORE the face is consulted;
Q6 specialness carried by the sister comparator m003 (+ the Gieseking parent m000 and
generic census comparators m006, m009), all in-cell.
Deterministic: fixed inputs, no randomness, no wall-clock, no network.
Environment: plain python3 (3.12), snappy 3.3.2 (ManifoldHP), mpmath, sympy.
"""

import cmath
import math
import pathlib
import sys

import mpmath
import snappy
import sympy as sp

mpmath.mp.dps = 45

REPO = pathlib.Path(__file__).resolve().parents[4]
FAILED = []


def check(label, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"CHECK: [{tag}] {label}" + (f"  -- {detail}" if detail else ""))
    if not ok:
        FAILED.append(label)


def lob(theta):
    """Lobachevsky function Lob(t) = Cl_2(2t)/2."""
    return mpmath.re(mpmath.clsin(2, 2 * theta)) / 2


def kc_of(manifold_name_or_word):
    """The kill's own operator (C3/C4): k_c = 2*pi/theta_max - 2 from HP shapes."""
    M = snappy.ManifoldHP(manifold_name_or_word)
    shapes = [complex(z) for z in M.tetrahedra_shapes("rect")]
    args = [cmath.phase(z) for z in shapes]
    assert all(a > 0 for a in args), "non-geometric solution"
    theta = max(args)
    return 2 * math.pi / theta - 2, theta, shapes, M


print("=" * 78)
print("TOMB-L57 x the frozen spectral face: is the crossover level level-indexed?")
print("=" * 78)

# ---------------------------------------------------------------- [0] kill source
tomb = (REPO / "speculations" / "TOMBSTONES.md").read_text()
check("kill source: TOMBSTONES.md carries the banked kill verbatim",
      "TESTED-NEGATIVE / DEAD.** Tested across `m` and killed cleanly (Chat-1 seven-hints A4)" in tomb
      and "k≈4`, matching the rank" in tomb)

# ------------------------------------------------- [1] the kill basis, re-anchored
print("\n[1] The kill basis re-anchored (the banked B742 conventions C1-C4)")
M1 = snappy.ManifoldHP("b++RL")
check("C1 anchor: b++RL is isometric to m004",
      M1.is_isometric_to(snappy.ManifoldHP("m004")))

kc = {}
for m in (1, 2, 3):
    word = "b++" + "R" * m + "L" * m
    k, theta, shapes, M = kc_of(word)
    kc[m] = k
    # Lobachevsky sum ties the ANGLE datum to the VOLUME datum (the kill's wording)
    vol_lob = mpmath.mpf(0)
    for z in shapes:
        a = cmath.phase(z)
        b = cmath.phase(1 / (1 - z))
        c = math.pi - a - b
        vol_lob += lob(a) + lob(b) + lob(c)
    print(f"  m={m}: theta_max = {theta:.12f}, k_c = {k:.12f}, vol = {float(M.volume()):.12f}")
    check(f"m={m}: Lobachevsky angle-sum volume matches SnapPy (<1e-9)",
          abs(float(vol_lob) - float(M.volume())) < 1e-9)

check("kill re-anchor: k_c(1) = 4 exactly (theta = pi/3 to 1e-12)",
      abs(kc[1] - 4) < 1e-10)
check("kill re-anchor: k_c(2) = 2 exactly (theta = pi/2 to 1e-12)",
      abs(kc[2] - 2) < 1e-10)
check("kill re-anchor: k_c(3) = 1.7645... != 4",
      abs(kc[3] - 1.7645125193) < 1e-6 and abs(kc[3] - 4) > 0.5)
check("kill re-anchor: m-dependent AND k_c = n = 4 only at m=1 (the banked kill stands as scoped)",
      abs(kc[2] - kc[1]) > 0.5 and abs(kc[3] - kc[1]) > 0.5
      and abs(kc[1] - 4) < 0.5 and abs(kc[2] - 4) > 0.5 and abs(kc[3] - 4) > 0.5)

# -------------------------------------------- [2] Q2: the operator discriminates
print("\n[2] Q2 discrimination of the consultation operator (BEFORE the face is used)")
print("  Operator X(M) = (k_c(M) by C3/C4, level-datum(M) where the face banks one).")
kc4, th4, sh4, M4 = kc_of("m004")
kc3, th3, sh3, M3 = kc_of("m003")
kc0, th0, sh0, M0 = kc_of("m000")   # the Gieseking parent (1 tetrahedron)
kc6, th6, sh6, M6 = kc_of("m006")   # generic census comparator 1 (deterministic)
kc9, th9, sh9, M9 = kc_of("m009")   # generic census comparator 2 (deterministic)
print(f"  X k_c-component: m004 (object)  = {kc4:.12f}")
print(f"                   m003 (sister)  = {kc3:.12f}")
print(f"                   m000 (parent)  = {kc0:.12f}")
print(f"                   m006 (generic) = {kc6:.12f}")
print(f"                   m009 (generic) = {kc9:.12f}")
check("Q2: operator separates the object from generic census input (m006)",
      abs(kc6 - 4) > 0.1, f"k_c(m006) = {kc6:.6f} != 4")
check("Q2: operator separates the object from generic census input (m009)",
      abs(kc9 - 4) > 0.1, f"k_c(m009) = {kc9:.6f} != 4")
check("Q2: the two generic outputs also differ from each other (no constant operator)",
      abs(kc6 - kc9) > 0.1)
# the level-datum component separates the SISTERS (computed in [3]); k_c does not:
check("Q2/Q6: the sisters are genuinely distinct manifolds (not isometric)",
      not M3.is_isometric_to(M4))

# ------------------- [3] face layer 1 (B737): the banked level data, recomputed
print("\n[3] Face source B737 (sister/level probe): grep-verify in-arc, then recompute")
p3 = (REPO / "frontier" / "B737_candidate_zero" / "p3_sister_out.txt").read_text()
check("B737 in-arc: 'level (2)  [m003]' with '#characters = 1' present",
      "level (2)  [m003]" in p3 and "#characters = 1" in p3)
check("B737 in-arc: 'level (4)  [m004 std]' with '#characters = 2' present",
      "level (4)  [m004 std]" in p3 and "#characters = 2" in p3)
check("B737 in-arc: conductor-4 identity '2*sqrt(-3) = 4*omega + 2 exactly: True' present",
      "2*sqrt(-3) = 4*omega + 2 exactly: True" in p3)
check("B737 in-arc: class-generic regular-ideal-tessellation membership stated",
      "regular-ideal-tessellation membership" in p3)

# recompute shadow (a): ray-class palette |Cl_n| = |(O/n)^x / im(mu_6)| at n = 2,4,8
def palette(n):
    """Brute-force (O/2^k)^x / im(mu_6) over O = Z[omega], omega^2 = -1-omega."""
    def mul(u, v):
        a, b = u
        c, d = v
        return ((a * c - b * d) % n, (a * d + b * c - b * d) % n)
    units = [(a, b) for a in range(n) for b in range(n)
             if (a * a - a * b + b * b) % 2 == 1]     # 2 inert: unit <=> odd norm
    img, cur = {(1, 0)}, (1, 0)
    for _ in range(6):                                 # mu_6 = <zeta_6 = 1 + omega>
        cur = mul(cur, (1, 1))
        img.add(cur)
    return len(units) // len(img)

pal = {2: palette(2), 4: palette(4), 8: palette(8)}
print(f"  recomputed ray-class palette |Cl_n|: (2) -> {pal[2]}, (4) -> {pal[4]}, (8) -> {pal[8]}")
check("B737 shadow recomputed: palette 1 / 2 / 8 at levels (2)/(4)/(8)",
      (pal[2], pal[4], pal[8]) == (1, 2, 8))

# recompute shadow (b): the cusp-lattice split (the in-arc computed level shadow)
mod3 = complex(M3.cusp_info()[0].modulus)
mod4 = complex(M4.cusp_info()[0].modulus)
j3 = mpmath.kleinj((1 + mpmath.sqrt(-3)) / 2) * 1728
j4 = mpmath.kleinj(mpmath.mpc(0, 2) * mpmath.sqrt(3)) * 1728
b = mpmath.mpf(2835810000)
root = b / 2 + mpmath.sqrt(b * b - 4 * mpmath.mpf(6549518250000)) / 2
check("cusp moduli recomputed: m003 = zeta_6 (hexagonal), m004 = 2*sqrt(3)*i (<1e-12)",
      abs(mod3 - complex(0.5, math.sqrt(3) / 2)) < 1e-12
      and abs(mod4 - complex(0, 2 * math.sqrt(3))) < 1e-12)
check("j(m003 cusp) = 0 exactly-to-1e-40 (maximal order, disc -3)",
      abs(j3) < mpmath.mpf("1e-40"))
check("j(m004 cusp) = larger root of the banked disc -48 class polynomial (<1e-30)",
      abs(j4 - root) < mpmath.mpf("1e-30"),
      "x^2 - 2835810000 x + 6549518250000 (B737 p3, algdep-banked; verified exactly here)")
z = sp.sqrt(-3)
check("conductor-4 identity recomputed exactly: 2*sqrt(-3) = 4*omega + 2, omega = (-1+sqrt(-3))/2",
      sp.simplify(2 * z - (4 * (sp.Rational(-1, 2) + z / 2) + 2)) == 0)

# --------------- [4] THE UNCONSULTED AXIS: vary level at fixed geometry (sisters)
print("\n[4] The axis the kill never varied: LEVEL at FIXED geometry")
vol3 = mpmath.mpf(str(M3.volume()))
vol4 = mpmath.mpf(str(M4.volume()))
check("sisters share the geometry datum: vol(m003) = vol(m004) (<1e-50)",
      abs(vol3 - vol4) < mpmath.mpf("1e-50"))
check("sisters share the shape datum: all shapes of BOTH = e^{i pi/3} (<1e-12)",
      all(abs(zz - complex(0.5, math.sqrt(3) / 2)) < 1e-12 for zz in sh3 + sh4))
check("hence k_c(m003) = k_c(m004) = 4 (both to 1e-10) — k_c is CLASS data",
      abs(kc3 - 4) < 1e-10 and abs(kc4 - 4) < 1e-10)
check("the Gieseking parent m000 (1 regular tetrahedron): k_c = 4 as well — the whole "
      "tessellation class sits at k_c = 4",
      abs(kc0 - 4) < 1e-10 and abs(sh0[0] - complex(0.5, math.sqrt(3) / 2)) < 1e-12)

print("\n  The level-indexed re-derivation of k_c (the revival hypothesis), computed:")
print("    banked level datum:  m003 -> (2), palette 1;   m004 -> (4), palette 2")
print(f"    computed crossover:  k_c(m003) = {kc3:.10f};  k_c(m004) = {kc4:.10f}")
# Reading R1: k tracks the level ((4) <-> 4). Then m003 at (2) must cross at 2.
check("R1 'k_c = level' DEAD: predicts k_c(m003) = 2, computed 4",
      abs(kc3 - 2) > 1.5)
# Reading R2: k tracks the palette. Then m004 must cross at 2 (and m003 at 1).
check("R2 'k_c = palette size' DEAD: predicts k_c(m004) = 2, computed 4",
      pal[4] == 2 and abs(kc4 - pal[4]) > 1.5)
# Reading R3: k_c is ANY function of the banked level datum. The sisters differ in
# EVERY face-banked level layer (level (2) vs (4); palette 1 vs 2; cusp order maximal
# vs conductor-4; j = 0 vs 2835807690.42...) yet k_c is IDENTICAL — and across m the
# kill already showed k_c varies where no banked level varies. The index that fits all
# computed values is theta_max (the shape/volume datum), exactly the kill's reading.
check("R3 level-DECOUPLING computed: level data differ at every banked layer, k_c identical",
      pal[2] != pal[4] and abs(j3 - j4) > 1 and abs(kc3 - kc4) < 1e-10)

# --------- [5] face layer 2 (B739): the continuous channel is level-blind, and its
# ---------     one object-datum is the VOLUME reciprocal (recomputed, two routes)
print("\n[5] Face source B739 (character rigidity): grep-verify in-arc, then recompute")
p39 = (REPO / "frontier" / "B739_character_rigidity" / "b739_probe_out.txt").read_text()
check("B739 in-arc: 'NO conductor-(4)/(8) Hecke character appears ANYWHERE' present",
      "NO conductor-(4)/(8) Hecke character appears ANYWHERE" in p39)
check("B739 in-arc: residue value 1.706552176628161608820573265788 present (banked)",
      "1.706552176628161608820573265788" in p39)
L2 = (mpmath.zeta(2, mpmath.mpf(1) / 3) - mpmath.zeta(2, mpmath.mpf(2) / 3)) / 9
zK2 = mpmath.zeta(2) * L2
res_geo = 2 * mpmath.sqrt(3) / vol4
res_an = 2 * mpmath.pi ** 2 / (9 * zK2)
vol_orb = 3 * mpmath.sqrt(3) * zK2 / (4 * mpmath.pi ** 2)
print(f"  route G (geometric):  2*sqrt(3)/vol(m004)  = {mpmath.nstr(res_geo, 31)}")
print(f"  route A (analytic):   2*pi^2/(9*zeta_K(2))  = {mpmath.nstr(res_an, 31)}")
check("L(2,chi_-3) recomputed (Hurwitz) matches B737's banked 55-digit value head",
      mpmath.nstr(L2, 20) == "0.78130241289648629687")
check("residue two-route agreement (<1e-40): the continuous channel's ONE object-datum "
      "is 1/vol — a VOLUME reciprocal, not a level index",
      abs(res_geo - res_an) < mpmath.mpf("1e-40"))
check("Humbert chain recomputed: vol(m004)/vol_orb = 12 (<1e-30)",
      abs(vol4 / vol_orb - 12) < mpmath.mpf("1e-30"))
print("  => B739 (verified in-arc): the continuous channel of the object carries NO")
print("     level-(4)/(8) character term at all — there is no level-dependent quantity")
print("     in the banked continuous spectrum from which a level-indexed k could be")
print("     sourced; its scattering entry is the LEVEL-1 base quotient Lambda_K(s-1)/")
print("     Lambda_K(s), and its sole object normalization is 1/vol (recomputed above).")

# ------- [6] face layers 3-4 (B753 phase, B746 columns): no face datum gives k = 4
print("\n[6] Face sources B753 / B746: the face's own numbers do not re-derive k = 4")
p53 = (REPO / "frontier" / "B753_mixing_structure" / "output.txt").read_text()
check("B753 in-arc: eigenvalues +0.309017+-0.951057j (= e^{+-i 72deg}) present",
      "+0.309017+0.951057j" in p53 and "+0.309017-0.951057j" in p53)
phi = (1 + sp.sqrt(5)) / 2
check("B753 shadow recomputed: cos(72deg) = 1/(2*phi) exactly (sympy)",
      sp.simplify(sp.cos(2 * sp.pi / 5) - 1 / (2 * phi)) == 0)
k753 = 2 * sp.pi / (2 * sp.pi / 5) - 2          # C2 lattice hit by the banked phase
check("B753 phase into the C2 lattice: 2*pi/(k+2) = 72deg gives k = 3 != 4 — the face's "
      "one banked eigenphase does NOT re-derive the crossover",
      sp.simplify(k753 - 3) == 0)
check("the crossover angle is NOT the face's mixing angle: cos(theta_geom) = cos(60deg) "
      "= 1/2 (rational), vs cos(72deg) = 1/(2*phi) (golden) — exactly distinct",
      sp.simplify(sp.cos(sp.pi / 3) - sp.Rational(1, 2)) == 0
      and sp.simplify(sp.Rational(1, 2) - 1 / (2 * phi)) != 0)
sc = (REPO / "frontier" / "B746_golden_ledger" / "spot_checks.txt").read_text()
check("B746 in-arc: S4 'palette {1,2,8} powers of 2' + '5 absent' present (spectral "
      "data of the object is 5-free)",
      "palette {1,2,8} powers of 2" in sc and "5 absent" in sc)
phif = (1 + math.sqrt(5)) / 2
check("B746 column guard: no golden marker in the crossover values (k_c(1),k_c(2) "
      "integers; |k_c(3)-phi| > 0.1, |k_c(3)-1/phi| > 0.1)",
      abs(kc[3] - phif) > 0.1 and abs(kc[3] - 1 / phif) > 0.1,
      "k_c inputs are tetrahedron-shape/volume data = the GEOMETRIC column of the "
      "two-column law (B746 F11/E-column); the kill's 'volume accident' lives there")

# ------------------------------------------------------------------ [7] verdict
print("\n" + "=" * 78)
if FAILED:
    print(f"VERDICT: BLOCKED — {len(FAILED)} check(s) failed: {FAILED}")
    sys.exit(1)
print("VERDICT: KILL-EXTENDS")
print("""
Computed, exactly and no more:
 (1) The kill re-anchors under its own conventions: k_c = 4, 2, 1.7645 at m = 1,2,3
     (m-dependent; = n = 4 at m=1 only), with the angle datum tied to the volume by
     the Lobachevsky sum — the banked basis reproduced, not cited.
 (2) The axis the kill never varied — LEVEL at fixed geometry — is answered by the
     frozen face: the sister pair m003/m004 (not isometric; identical volume to
     1e-50 and identical shapes e^{i pi/3}) has IDENTICAL crossover k_c = 4, while
     every face-banked level datum differs between them (level (2) vs (4); ray-class
     palette 1 vs 2, recomputed; cusp order maximal (j=0) vs conductor-4 (disc -48,
     j = the banked class-poly root, recomputed to 1e-30)). The Gieseking parent
     m000 sits at k_c = 4 as well. The crossover is CLASS data; the level is OBJECT
     data; a level-indexed re-derivation of k_c fails at its first computable
     instance, in both readings (R1 'k = level' predicts 2 at m003, computed 4;
     R2 'k = palette' predicts 2 at m004, computed 4).
 (3) The banked continuous-spectral surface cannot supply any other level index:
     B739 (verified in-arc) leaves NO conductor-(4)/(8) character anywhere in the
     continuous channel, and its single object-datum recomputes as 2*sqrt(3)/vol =
     2*pi^2/(9*zeta_K(2)) (two routes, <1e-40) — a VOLUME reciprocal.
 (4) The face's one banked eigenphase (72deg, B753) lands at lattice k = 3 != 4;
     the crossover angle (60deg, rational cosine) is not a face angle; no golden
     marker appears in any k_c value (B746 column guard).
EXTENSION BANKED: the kill 'figure-eight-VOLUME coincidence, not structure' gains
the level-decoupling column — the k~4 <-> n=4 match also fails as a level-(4) match,
because the level-(2) sister crosses at the same k_c = 4. The revival hypothesis's
named mechanism (congruence-tower re-indexing of k_c) is computed dead on the only
level data the frozen face banks. Nothing beyond these computations is claimed; the
m>=2 members' own congruence structure (different trace fields) is outside the
frozen surface and outside this cell.
""")
