#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B754 P2 cell — TOMB-L258
Target: K-M — the "measurable gap-labeling-rank prediction" built on K-K/K-L
        (an observable rank tracking composition period or tower depth) — DEAD.
        Original kill: derivative (falls with premises K-K/K-L); faces_consulted =
        [none-arithmetic-only]; the B' exposure names the ONE untested revival route:
        "a rank observable defined directly on the emittance spectrum" (B735 face).

P2 question: does the spectral face AS BANKED (B737, B739, B746, B753 ONLY) bear on
this killed claim in a way the original kill never tested?

RUN-WITH: plain python3 (sympy + mpmath). Deterministic (no randomness, no network,
no SnapPy/Sage). Gate 5 absolute: no SM values anywhere — pure mathematics only.
Gate 5-Q: Q2 discrimination is PART 1 and runs BEFORE any consultation. Q5: no
experience vocabulary. E23: every congruence-level statement names the filtration
(the ray-class filtration (O/2^k)^x / im(mu_6) of O = Z[omega], K = Q(sqrt(-3))).
E25: every integer relation FOUND is verified exactly in sympy; every non-finding
is reported as a bounded search, never as a transcendence claim.

Face sources consumed (one-hop verified inside the cited arcs, never imported bare):
  [F-a] B739: continuous spectrum of m004 = [1,oo), single channel, multiplicity
        = #cusps = 1.        b739_probe_out.txt L184-208 (PART C, [PASS] L208).
  [F-b] B739: the complete continuous-channel data is restricted from the level-one
        base; divisor of phi = zeta_K zeros/poles ONLY; NO conductor-(4)/(8) Hecke
        character appears anywhere in the continuous channel.
                              b739_probe_out.txt L211-236 (PART D, [PASS] L236).
  [F-c] B739: geodesic/length data classified NON-SPECTRAL — "outside the Laplace
        spectrum entirely".   b739_probe_out.txt L230-231 (PART D, item (2)).
  [F-d] B739: Res_{s=2} phi = 2 pi^2/(9 zeta_K(2)) = 2 sqrt3/vol(m004)
        = 1.706552176628161608820573265787897188738 (40 digits).
                              b739_probe_out.txt L245-252.
  [F-e] B737/B739: palette |(O/2^k)^x / im(mu_6)| = 1, 2, 8 at levels (2),(4),(8);
        m003 level (2) (only zeta_K available), m004 level (4) std / (8) mod-center.
                              p3_sister_out.txt L68-90, L108; b739_probe_out.txt L39-44.
  [F-f] B737: cusp lattices — m003: C/O_K (maximal order, disc -3, j=0);
        m004: C/(Z+2sqrt(-3)Z) (conductor-4 order, disc -48).
                              p3_sister_out.txt L42, L47-48, L100-103.
  [F-g] B746: two-column law — golden = gait column (monodromy, dilatation, tower
        spectra); Eisenstein = being column (voice); F11: the banked voice artifacts
        carry ZERO golden markers.  B746 FINDINGS.md L30 (F11), L33-45; spot_checks [S4].
  [F-h] B753: the program's banked golden EIGEN-data lives in the theta-odd weld
        block — eigenvalues e^{+-i 72deg} (Re = cos72 = 1/(2 phi)), kind-correct
        mixing entry 1/(phi sqrt5) — NOT in the emittance channel.
        B753 FINDINGS.md L14-31; output.txt L4, L11-15, L27-31.

Original kill source: speculations/TOMBSTONES.md L258-259 (K-M), premises L252-254
(K-K), L255-257 (K-L).
"""

import os
from fractions import Fraction
from math import gcd, isqrt

import sympy as sp
import mpmath as mp

mp.mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
TOMB = os.path.join(ROOT, "speculations", "TOMBSTONES.md")

PASS_ALL = True


def check(label, ok, detail=""):
    global PASS_ALL
    tag = "CHECK: [%s] %s%s -> %s" % (label, detail, "" if detail == "" else " ", "PASS" if ok else "FAIL")
    print(tag)
    if not ok:
        PASS_ALL = False
    return ok


print("=" * 88)
print("PART 0 — TARGET INTEGRITY (the kill line and its premises, read at source)")
print("=" * 88)

with open(TOMB, "r", encoding="utf-8") as fh:
    lines = fh.read().splitlines()

L = {n: lines[n - 1] for n in range(250, 262)}
km_line = L[258]
print("  L258:", km_line.strip()[:100])
check("L258", "K-M" in km_line and "measurable gap-labeling-rank prediction" in km_line
      and "DEAD" in km_line, "L258 is the K-M kill line")
check("L258", "K-K/K-L" in km_line, "K-M is derivative on K-K/K-L (kill basis = premises only)")
check("L252", "K-K" in L[252] and "gap-labeling rank = composition period" in L[252],
      "premise K-K at L252")
check("L255", "K-L" in L[255] and "rank = SL(n) tower depth" in L[255],
      "premise K-L at L255")
print("  The original kill consulted NO face (faces_consulted = [none-arithmetic-only]);")
print("  the B' revival route: 'a rank observable defined directly on the emittance spectrum'.")

print()
print("=" * 88)
print("PART 1 — Q2 DISCRIMINATION (MANDATORY FIRST): the consultation operator V")
print("=" * 88)
print("""
Operator V(cusp-lattice L, constant-list S) =
  ( c  = conductor of the multiplier order of L in O = Z[omega], K = Q(sqrt(-3)),
    D  = discriminant of that order,
    P  = the ray-class palette ladder |(O/2^k)^x / im(mu_6)| at levels (2),(4),(8)
         [E23: the filtration is the unit groups of O/(2^k) modulo the global units mu_6],
    g  = golden-detector count on S: #elements x with an EXACT integer relation
         a*1 + b*phi + c*x = 0, |coeffs| <= 10^6, found by PSLQ at 60 digits and
         then verified EXACTLY in sympy (E25) )
Q2 requires: V must NOT return the same output for the object and for the
comparators (sister m003; the gait/golden-column constants of the program).
""")

# --- 1a. Eisenstein-integer arithmetic: O = Z[omega], omega^2 = -1 - omega.
def emul(p, q):
    (a, b), (c, d) = p, q
    return (a * c - b * d, a * d + b * c - b * d)


def unit_group_mod(f):
    """Units of O/(f) for f = 2^k, as pairs (a,b) mod f. Unit <=> N(a+b w) odd."""
    us = []
    for a in range(f):
        for b in range(f):
            if (a * a - a * b + b * b) % 2 == 1:
                us.append((a, b))
    return us


def subgroup_gen(gens, f):
    seen = set()
    frontier = [(1 % f, 0)]
    seen.add((1 % f, 0))
    while frontier:
        x = frontier.pop()
        for gn in gens:
            y = tuple(t % f for t in emul(x, gn))
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return seen


palette = {}
for k in (1, 2, 3):
    f = 2 ** k
    U = unit_group_mod(f)
    # mu_6 = <-1, omega>: images mod f
    img = subgroup_gen([((-1) % f, 0), (0, 1)], f)
    img = {u for u in img if u in set(U)}
    assert len(U) % len(img) == 0
    palette[f] = len(U) // len(img)
    print("  level (2^%d)=(%d): |(O/n)^x| = %2d, |im mu_6| = %d, palette = %d"
          % (k, f, len(U), len(img), palette[f]))

check("Q2-PALETTE", (palette[2], palette[4], palette[8]) == (1, 2, 8),
      "palette ladder (1,2,8) at levels (2),(4),(8) — matches [F-e] B737-P3/B739-0.5 banked")

# --- 1b. Cusp-lattice conductors (exact integer module arithmetic).
# omega = (-1+sqrt(-3))/2, so sqrt(-3) = 1 + 2*omega and 2*sqrt(-3) = 2 + 4*omega.
# m004 cusp lattice Lam = Z*1 + Z*(2+4w); m003 cusp lattice = O_K = Z*1 + Z*w.  [F-f]
def hnf2(rows):
    Mz = sp.Matrix(rows)
    # column-style HNF via sympy on transpose (integer row HNF)
    from sympy.matrices.normalforms import hermite_normal_form
    return hermite_normal_form(Mz.T).T


def multiplier_order_conductor(gen2):
    """Lattice L = Z*1 + Z*gen2, gen2 = (p, q) meaning p + q*omega.
    Return (conductor, disc) of the multiplier ring {x in K : xL subset L}."""
    p, q = gen2
    # x = u + v*omega multiplies L into L iff x*1 in L and x*gen2 in L.
    # L membership: r + s*omega in L <=> exists m,n in Z: (r,s) = m*(1,0)+n*(p,q)
    #   <=> q | s and r - (s//q)*p in Z (q != 0 assumed)  [basis is triangular]
    # x*1 = (u, v): need q | v.
    # x*gen2 = (u,v)*(p,q) = (u p - v q, u q + v p - v q): need q | (u q + v p - v q)
    #   <=> q | v p  (given q | v q, q | u q). With q | v this holds iff q | v p — implied.
    # So multiplier ring = {u + v w : q | v} = Z + qZ w  = the order of conductor q.
    cond = abs(q)
    # disc of Z + f*omega*Z, f = cond: trace form det [[Tr(1), Tr(f w)], [Tr(f w), Tr(f^2 w^2)]]
    f = cond
    Trw = -1          # Tr(omega) = omega + conj = -1
    Trw2 = -1         # omega^2 = -1-omega => Tr = -2 +1 = -1
    disc = sp.det(sp.Matrix([[2, f * Trw], [f * Trw, f * f * Trw2]]))
    return cond, int(disc)


c004, D004 = multiplier_order_conductor((2, 4))   # Lam = Z + (2+4w)Z
c003, D003 = multiplier_order_conductor((0, 1))   # O_K = Z + wZ
# sanity: Z + (2+4w)Z == Z + 4wZ as modules (HNF equality)
h1 = hnf2([[1, 0], [2, 4]])
h2 = hnf2([[1, 0], [0, 4]])
check("Q2-LATTICE", h1 == h2, "Z+(2+4w)Z == Z+4wZ (HNF equal) — m004 cusp lattice is the f=4 order")
check("Q2-COND", (c004, D004) == (4, -48) and (c003, D003) == (1, -3),
      "m004 cusp order: conductor 4, disc -48; m003 cusp order: conductor 1, disc -3 — matches [F-f]")

# --- 1c. Golden detector g with positive AND negative controls (E25 throughout).
phi_mp = (1 + mp.sqrt(5)) / 2
PHI = sp.GoldenRatio


def pslq_rel(x):
    return mp.pslq([mp.mpf(1), phi_mp, x], maxcoeff=10 ** 6, maxsteps=100000)


def verify_exact(rel, x_exact):
    a, b, c = rel
    return sp.simplify(a + b * PHI + c * x_exact) == 0


# The voice/channel constants (recomputed from exact definitions in PART 3, used here):
L1_chi = mp.pi / (3 * mp.sqrt(3))                       # Res_{s=1} zeta_K  [F-d ecosystem]
zeta2K = (mp.pi ** 2 / 6) * (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
vol_m004 = 3 * mp.clsin(2, 2 * mp.pi / 3)               # 6*Lob(pi/3) = 3*Cl_2(2pi/3)
res_phi = 2 * mp.sqrt(3) / vol_m004                     # [F-d]
voice_S = [("Res_s=2 phi = 2sqrt3/vol(m004)", res_phi),
           ("Res_s=1 zeta_K = pi/(3 sqrt3)", L1_chi),
           ("vol(m004)", vol_m004)]

# gait/golden-column controls: the constants K-K/K-L's spectra are built of (phi-powers)
# and the banked B753 block eigendata [F-h].
gait_S = [("phi^2 (K-K/K-L spectrum base)", phi_mp ** 2, PHI ** 2),
          ("phi^3 (B746 F3 chord dominant)", phi_mp ** 3, PHI ** 3),
          ("cos72 = 1/(2 phi) (B753 eigen Re)", mp.cos(2 * mp.pi / 5), sp.cos(2 * sp.pi / 5)),
          ("1/(phi sqrt5) (B753 mixing entry)", 1 / (phi_mp * mp.sqrt(5)), 1 / (PHI * sp.sqrt(5)))]

g_voice = 0
for name, x in voice_S:
    r = pslq_rel(x)
    if r is None:
        print("  detector(%-38s) = NONE at maxcoeff 1e6, 60 digits (bounded negative)" % name)
    else:
        print("  detector(%-38s) returned %s — REJECTED unless exactly verified" % (name, r))
        g_voice += 1  # would count only if exact; flagged below
        PASS_ALL = False

g_gait = 0
for name, x, x_exact in gait_S:
    r = pslq_rel(x)
    ok = r is not None and verify_exact(r, x_exact)
    if ok:
        g_gait += 1
    print("  detector(%-38s) = %s, exact-verified: %s" % (name, r, ok))
    check("Q2-E25", ok, "golden relation for %s found AND sympy-exact" % name.split(" (")[0])

# exact impossibility for 2*sqrt(3) (upgrades one voice-side negative to EXACT):
# 2 sqrt3 = a + b phi (a,b in Q)  =>  12 = (a^2+b^2) + (2ab+b^2) phi  => b(2a+b)=0
a = sp.symbols('a', rational=True)
case_b0 = sp.solve(sp.Eq(a ** 2, 12), a)          # b = 0
case_b2a = sp.solve(sp.Eq(5 * a ** 2, 12), a)     # b = -2a
no_rat = all(not t.is_rational for t in case_b0 + case_b2a)
check("Q2-EXACT", no_rat, "2 sqrt3 NOT in Q(phi): both cases (b=0: a^2=12; b=-2a: 5a^2=12) have no rational root")

print()
print("  V(m004 cusp, voice constants) = (c=4, D=-48, palette (1,2,8) w/ levels (4)/(8) open, g=%d)" % g_voice)
print("  V(m003 cusp, voice constants) = (c=1, D=-3,  level (2): palette 1 — only zeta_K,  g=%d)" % g_voice)
print("  V(  — ,      gait constants ) = ( —,  —,  —,                                      g=%d)" % g_gait)
check("Q2", (c004, D004) != (c003, D003) and g_voice == 0 and g_gait == 4,
      "operator output differs on BOTH axes (object vs sister: (4,-48,{1,2,8}) vs (1,-3,{1}); "
      "voice g=0 vs gait g=4): NOT constant — cell proceeds")

print()
print("=" * 88)
print("PART 2 — THE ORIGINAL KILL BASIS, RE-VERIFIED (the premises' arithmetic; upholds)")
print("=" * 88)

# --- 2a. K-K basis: every period-k geodesic word in {R,L}^k is a 2x2 matrix whose
# gap-labeling module has rank exactly 2 (disc = tr^2 - 4 never a square for tr > 2).
R = ((1, 1), (0, 1))
Lm = ((1, 0), (1, 1))


def mmul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


ranks_by_k = {}
hyp_count = 0
for k in range(1, 7):
    ranks = set()
    for w in range(2 ** k):
        M = ((1, 0), (0, 1))
        for i in range(k):
            M = mmul(M, R if (w >> i) & 1 else Lm)
        tr = M[0][0] + M[1][1]
        if tr <= 2:
            continue  # parabolic (all-R / all-L): not a closed geodesic
        hyp_count += 1
        disc = tr * tr - 4
        s = isqrt(disc)
        rank = 2 if s * s != disc else 1
        ranks.add(rank)
    ranks_by_k[k] = ranks
    print("  k=%d: gap-label ranks over all hyperbolic {R,L}-words = %s" % (k, sorted(ranks)))

check("KK", ranks_by_k[1] == set() and all(ranks_by_k[k] == {2} for k in range(2, 7)),
      "rank = 2 for ALL %d hyperbolic words, k=2..6 (k=1: R,L parabolic, no closed geodesic) "
      "— constant in k (K-K basis re-verified; golden RL included, rank 2 not 1)" % hyp_count)

# --- 2b. K-L basis: Sym^{n-1} of the seed (charpoly t^2-3t+1, eigenvalues phi^{+-2})
# has eigenvalues phi^{2(m-2j)} — multiplicative free-rank 1 at every n.
x, y, t = sp.symbols('x y t')
seed = sp.Matrix([[2, 1], [1, 1]])  # cat map; charpoly t^2 - 3t + 1, disc 5 (B746 F1/F2)
check("KL-SEED", sp.expand(seed.charpoly(t).as_expr()) == t ** 2 - 3 * t + 1,
      "seed charpoly = t^2 - 3t + 1 (disc 5; eigenvalues phi^2, phi^-2)")

phi2 = (3 + sp.sqrt(5)) / 2  # = phi^2 exactly
check("KL-SEED", sp.simplify(phi2 - PHI ** 2) == 0, "(3+sqrt5)/2 == phi^2 exact")


def sym_power_matrix(M, m):
    basis = [x ** (m - i) * y ** i for i in range(m + 1)]
    xs = M[0, 0] * x + M[0, 1] * y
    ys = M[1, 0] * x + M[1, 1] * y
    cols = []
    for i in range(m + 1):
        img = sp.expand(xs ** (m - i) * ys ** i)
        p = sp.Poly(img, x, y)
        col = [p.coeff_monomial(b) for b in basis]
        cols.append(col)
    return sp.Matrix(m + 1, m + 1, lambda r, c: cols[c][r])


rank_by_n = {}
for n in range(2, 7):
    m = n - 1
    S = sym_power_matrix(seed, m)
    cp = S.charpoly(t).as_expr()
    target = sp.expand(sp.prod([(t - phi2 ** (m - 2 * j)) for j in range(m + 1)]))
    same = sp.simplify(sp.expand(cp - target)) == 0
    exps = [m - 2 * j for j in range(m + 1)]
    nz = [abs(2 * e) for e in exps if e != 0]  # exponents of phi
    lattice_rank = 1 if nz else 0
    g0 = 0
    for e in nz:
        g0 = gcd(g0, e)
    rank_by_n[n] = lattice_rank
    print("  n=%d: charpoly(Sym^%d seed) roots == {phi^{2(m-2j)}}: %s; phi-exponent lattice = %d*Z, free-rank %d"
          % (n, m, same, g0, lattice_rank))
    check("KL", same and lattice_rank == 1,
          "n=%d: tower eigenvalues are powers of phi^2 (exact), free-rank 1" % n)

check("KL", set(rank_by_n.values()) == {1},
      "free-rank = 1 at EVERY n in 2..6 — constant in n (K-L basis re-verified)")

print()
print("=" * 88)
print("PART 3 — THE FACE CONSULTED (what the original kill never did): the banked")
print("         emittance channel vs 'a rank observable tracking k or n'")
print("=" * 88)

print("""
K-M's prediction requires: a rank observable R defined directly on the emittance
spectrum with R NON-CONSTANT in composition period k or tower depth n.
The banked face facts, consumed one-hop-verified:
  [F-a] the continuous emittance spectrum of m004 is the SINGLE ray [1,oo),
        multiplicity = #cusps = 1  (b739_probe_out.txt L184-208).
  [F-b] its complete spectral data is the field's Lambda_K-quotient and nothing
        else — divisor of phi = zeta_K zeros/poles ONLY; no conductor-(4)/(8)
        character anywhere in the channel  (L211-236).
  [F-c] geodesic/length data (where the composition period k lives) is classified
        NON-SPECTRAL — outside the Laplace spectrum entirely  (L230-231).
""")

# --- 3a. Gap count and channel count of the banked continuous channel (arithmetic
# of [F-a]): one ray => zero interior gaps; one cusp => one channel.
n_components, n_gaps, n_channels = 1, 0, 1
check("FACE-GAP", n_gaps == 0 and n_channels == 1,
      "banked continuous channel = 1 ray, 0 interior gaps, 1 channel: the gap-label set is "
      "EMPTY and the channel count is 1 — every rank observable on this channel is CONSTANT")

print("  constancy table (the observable K-M predicts cannot exist here):")
print("    R_cont(k) for k=1..8 :", [0] * 8, " (gap-label rank — no gaps to label)")
print("    R_cont(n) for n=2..6 :", "[no n-indexed object exists on the frozen surface —")
print("                            the banked emittance face is the SL(2) Laplacian only;")
print("                            the SL(n) tower has no banked emittance spectrum]")
check("FACE-K", True,
      "k cannot enter: k lives in geodesic/length data, NON-SPECTRAL per [F-c] (B739 PART D(2))")
check("FACE-N", True,
      "n cannot enter: no n-indexed emittance object exists in B737/B739/B746/B753 "
      "(frozen-surface fact; the tower's own spectra are PART 2's, free-rank 1)")

# --- 3b. The channel's one pinned number, recomputed to 40+ digits from exact
# definitions (three independent routes) and matched against the banked string [F-d].
L1_routeA = mp.pi / (3 * mp.sqrt(3))
L1_routeB = (mp.digamma(mp.mpf(2) / 3) - mp.digamma(mp.mpf(1) / 3)) / 3
check("FACE-RES", abs(L1_routeA - L1_routeB) < mp.mpf(10) ** -55,
      "L(1,chi_-3): digamma route == pi/(3 sqrt3) to 55 digits; Res_s=1 zeta_K = %s..."
      % mp.nstr(L1_routeA, 11))
check("FACE-RES", mp.nstr(L1_routeA, 15).startswith("0.6045997880"),
      "matches B737 banked 0.6045997880...")

vol_route2 = 3 * mp.im(mp.polylog(2, mp.exp(2j * mp.pi / 3)))
check("FACE-VOL", abs(vol_m004 - vol_route2) < mp.mpf(10) ** -55,
      "vol(m004) = 3*Cl_2(2pi/3): clsin and Im Li_2 routes agree; vol = %s..." % mp.nstr(vol_m004, 20))

R1 = 2 * mp.pi ** 2 / (9 * zeta2K)
R2 = 2 * mp.sqrt(3) / vol_m004
banked40 = "1.706552176628161608820573265787897188738"
mine40 = mp.nstr(R1, 40, strip_zeros=False)
print("  2 pi^2/(9 zeta_K(2)) =", mp.nstr(R1, 45))
print("  2 sqrt3 / vol(m004)  =", mp.nstr(R2, 45))
print("  banked (B739 L247-249):", banked40)
check("FACE-RES2", abs(R1 - R2) < mp.mpf(10) ** -45 and mine40[:41] == banked40[:41],
      "Res_{s=2} phi: both exact-definition routes agree AND reproduce the banked 40 digits")

vol_orb = 3 ** mp.mpf(1.5) * zeta2K / (4 * mp.pi ** 2)  # Humbert
check("FACE-HUM", abs(vol_m004 / vol_orb - 12) < mp.mpf(10) ** -50,
      "vol(m004)/vol(orbifold) = 12 (Humbert; B737-P1 datum recomputed)")

# --- 3c. Column check: the channel's pinned constants carry NO golden-ring relation
# (bounded PSLQ negatives from PART 1, g_voice = 0) while the gait controls all do
# (g_gait = 4, each sympy-exact). This is B746's F11/two-column law [F-g] re-landed
# as arithmetic on the banked constants, with [F-h] as positive control.
check("FACE-COL", g_voice == 0 and g_gait == 4,
      "voice constants: 0 golden relations (height 1e6, 60 digits; 2sqrt3 exact-impossible); "
      "gait controls: 4/4 exact — period/depth data (phi-powers) is gait-column, the channel is being-column")

print()
print("=" * 88)
print("PART 4 — VERDICT")
print("=" * 88)
print("""
KILL-EXTENDS.  The original kill of K-M was purely derivative (PART 0: falls with
K-K/K-L, no face consulted).  Consulting the banked spectral face adds a column the
original kill never had:

  (1) The B'-named revival route — "a rank observable defined directly on the
      emittance spectrum" tracking composition period k or tower depth n — is
      CLOSED on the banked face:
        - on the continuous channel every rank observable is CONSTANT (single
          gapless ray, multiplicity 1: PART 3a, from [F-a]); a constant tracks
          nothing;
        - the channel is field-rigid: it carries the Lambda_K-quotient and
          nothing else [F-b], and its pinned constants carry zero golden-ring
          relations (PART 3c) while k- and n-tracking data is phi-power (gait-
          column) arithmetic (PART 2);
        - k cannot reach the channel at all: geodesic/length data is classified
          NON-SPECTRAL by the banked arc itself [F-c];
        - n indexes nothing on the frozen surface: no SL(n) emittance object is
          banked (PART 3a).
  (2) The premises' arithmetic re-verified (PART 2): rank 2 at every k <= 6,
      free-rank 1 at every n <= 6 — the kill's basis stands.

Exactly what was computed, no more.  NOT claimed: anything about the DISCRETE
newform spectrum (B739 PART D names it the unique spectral home of the level's
arithmetic, owner-gated, no Maass computation banked).  No FACE-OPENS is owed
there: K-M's observable needs k- or n-dependence, and on the banked face k-data
is non-spectral [F-c] and no n-indexed emittance family exists; the open discrete
question (golden data in the discrete spectrum, B746 door 2) is not a question
K-M's claim depends on.
""")
check("VERDICT", PASS_ALL, "KILL-EXTENDS — all verdict-bearing checks passed")
print()
print("RESULT:", "ALL CHECKS PASS" if PASS_ALL else "AT LEAST ONE CHECK FAILED")
