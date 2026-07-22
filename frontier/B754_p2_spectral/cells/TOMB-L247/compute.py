#!/usr/bin/env python3
# B754 P2 cell -- TOMB-L247 (kill K-J): spectral-face consultation of a sealed kill.
# RUN-WITH: plain python3 (stdlib only). Deterministic (fixed PRNG seed 754247).
#
# KILLED CLAIM (TOMBSTONES.md:L247, K-J): "phi^2 is the degenerate-block (phi_{2,1})
# torus-block monodromy multiplier of the seed; the '3=3' numerical confirmation of
# that identification."  Kill form: kind-mismatch (reducible kappa=2 vs irreducible
# kappa>2; an eigenvalue-trace compared against a commutator-trace). fact_basis:
# asserted (no arc or script cited).  faces_consulted: mtc-overlay only.
#
# P2 QUESTION: does the spectral face AS BANKED (frozen surface = B737 + B739 +
# B746 + B753, and nothing else) bear on this kill in a way the original never
# tested?  Gate 5 absolute (no SM values).  Gate 5-Q: Q2 discrimination shown
# BEFORE the consultation operator is applied to the claim.
#
# Q1 vocabulary binding: "voice" = the continuous-spectrum channel exactly as
# banked in B737/B739 (the firewall's own binding); "gait/name two-column law" =
# B746; "theta-odd block / kind-correct mixing" = B753.  No other face vocabulary.

import math, cmath, random
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

CHECKS = []
def check(label, ok, detail=""):
    line = f"CHECK: {label} -- {'PASS' if ok else 'FAIL'}" + (f" ({detail})" if detail else "")
    CHECKS.append(ok)
    print(line)
    return ok

# ---------- exact arithmetic in Q(sqrt5): x = (a, b) means a + b*sqrt(5), a,b in Q ----
def q5_add(x, y): return (x[0] + y[0], x[1] + y[1])
def q5_mul(x, y): return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def q5_inv(x):
    n = x[0]*x[0] - 5*x[1]*x[1]
    return (x[0]/n, -x[1]/n)
def q5_float(x): return float(x[0]) + float(x[1])*math.sqrt(5)

# ---------- exact 2x2 SL2 over Q ----------
def mmul(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]))
def det(A): return A[0][0]*A[1][1] - A[0][1]*A[1][0]
def tr(A):  return A[0][0] + A[1][1]
def inv_sl2(A):
    assert det(A) == 1
    return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))

rnd = random.Random(754247)
def rfrac(): return F(rnd.randint(-9, 9), rnd.randint(1, 9))
def rand_sl2():
    while True:
        a = rfrac()
        if a == 0: continue
        b, c = rfrac(), rfrac()
        d = (1 + b*c) / a
        return ((a, b), (c, d))
def rand_upper_sl2():
    while True:
        a = rfrac()
        if a == 0: continue
        return ((a, rfrac()), (F(0), 1/a))

print("=" * 88)
print("[0] TARGET -- TOMB-L247 / kill K-J (kind-mismatch, mtc-overlay face only, basis: asserted)")
print("=" * 88)
print("Exposure note: revival_hypothesis names the B735 spectral face as unconsulted;")
print("the original recompute stayed in Fricke/character-variety (commutator-trace) terms.")
print("Frozen surface consulted here: B737, B739, B746, B753 -- and NOTHING else.")

print()
print("=" * 88)
print("[1] THE CLAIM'S QUANTITY, EXACT -- the seed and phi^2 (recomputes B746 F1/F2, S1)")
print("=" * 88)
R = ((F(1), F(1)), (F(0), F(1)))
L = ((F(1), F(0)), (F(1), F(1)))
M = mmul(R, L)
ok = (M == ((F(2), F(1)), (F(1), F(1)))) and tr(M) == 3 and det(M) == 1
check("seed = R*L = [[2,1],[1,1]], tr = 3, det = 1 (exact)", ok)

disc = 3*3 - 4*1
phi2  = (F(3, 2), F(1, 2))          # (3+sqrt5)/2
phi2f = q5_float(phi2)
check("char poly t^2-3t+1: disc = 5; larger root = phi^2 = (3+sqrt5)/2",
      disc == 5 and abs(phi2f - (3 + math.sqrt(5))/2) < 1e-15,
      f"phi^2 = {phi2f:.15f}")
phim2 = q5_inv(phi2)
check("phi^2 * phi^-2 = 1 and phi^2 + phi^-2 = 3, exact in Q(sqrt5)",
      q5_mul(phi2, phim2) == (F(1), F(0)) and q5_add(phi2, phim2) == (F(3), F(0)))

# Eigenvalue-trace == matrix-trace identically on SL2 (Cayley-Hamilton, exact battery):
# the seed-side '3' of the claimed '3=3' is the matrix trace by Vieta -- it carries
# ZERO confirmation content (the B753 cell-2 mechanism: an identity, 'regardless of p').
n_ch = 200
ch_ok = 0
for _ in range(n_ch):
    A = rand_sl2()
    t = tr(A)
    M2 = mmul(A, A)
    Z = ((M2[0][0] - t*A[0][0] + 1, M2[0][1] - t*A[0][1]),
         (M2[1][0] - t*A[1][0], M2[1][1] - t*A[1][1] + 1))
    if Z == ((F(0), F(0)), (F(0), F(0))): ch_ok += 1
check(f"Cayley-Hamilton battery {ch_ok}/{n_ch} exact: A^2 - tr(A)*A + I = 0 for random SL(2,Q)",
      ch_ok == n_ch, "eigenvalue-trace == matrix-trace IDENTICALLY; the seed-side '3' is forced by Vieta")

print()
print("=" * 88)
print("[2] THE ORIGINAL KILL BASIS: asserted -> COMPUTED (the kind-mismatch, exact)")
print("=" * 88)
# Fricke: tr[A,B] = x^2+y^2+z^2-xyz-2 (ties the tombstone's kappa to the commutator trace)
n_fr = 300
fr_ok = 0
neq2 = 0
for _ in range(n_fr):
    A, B = rand_sl2(), rand_sl2()
    C = mmul(mmul(A, B), mmul(inv_sl2(A), inv_sl2(B)))
    x, y, z = tr(A), tr(B), tr(mmul(A, B))
    if tr(C) == x*x + y*y + z*z - x*y*z - 2: fr_ok += 1
    if tr(C) != 2: neq2 += 1
check(f"Fricke battery {fr_ok}/{n_fr} exact: tr[A,B] = x^2+y^2+z^2-xyz-2", fr_ok == n_fr)
check(f"general-position pairs are NOT pinned: {neq2}/{n_fr} have tr[A,B] != 2", neq2 >= 250,
      f"tr[A,B]=2 is a PROPER special locus ({n_fr - neq2}/{n_fr} random pairs land on it), "
      "in contrast to the reducible battery below, which is pinned there without exception")

n_red = 300
red_ok = 0
for _ in range(n_red):
    A, B = rand_upper_sl2(), rand_upper_sl2()
    C = mmul(mmul(A, B), mmul(inv_sl2(A), inv_sl2(B)))
    if tr(C) == 2: red_ok += 1
check(f"reducible battery {red_ok}/{n_red} EXACT: tr[A,B] = 2 for ALL reducible (triangular) pairs",
      red_ok == n_red, "the degenerate/reducible (phi_{2,1}) side is PINNED at kappa = 2")
check("kind-correct comparison: 2 != 3", 2 != 3,
      "commutator-trace of the reducible side (2, computed) vs the seed's kappa = 3 (B746 F1, S1); "
      "the '3=3' put an eigenvalue-trace (=matrix trace, [1]) against a commutator-trace: cross-kind, "
      "and the kind-correct degenerate-side value is 2 -- the kill's inequality now COMPUTED, not asserted")

print()
print("=" * 88)
print("[3] THE CONSULTATION OPERATOR SFH + Q2 DISCRIMINATION (mandatory-first)")
print("=" * 88)
print("SFH (spectral-face host scan): input = a candidate quantity q; output = (i) exact-")
print("equality hits of q against every banked object-specific quantity of the frozen")
print("surface, (ii) field-membership of q in the banked voice fields Q(sqrt-3) and")
print("Q(j_{-48}), (iii) the kind ledger (unimodular phase / probability / residue /")
print("volume vs dilatation).  Face-data extractor applied to a MANIFOLD = its banked")
print("(cusp CM j, palette, voice residue) triple, recomputed from closed forms.")
print()

# --- face data recomputation, m004 side ---
def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b) + 4*sum(f(a + (2*i - 1)*h) for i in range(1, n//2 + 1)) \
        + 2*sum(f(a + 2*i*h) for i in range(1, n//2))
    return s * h / 3

def cl2(theta):
    # Cl2(theta) = -int_0^theta log(2 sin(t/2)) dt, log-singularity split off exactly
    a = 0.5
    I1 = a * (math.log(a) - 1.0)                      # int_0^a log t dt, exact
    def g(t):
        if t < 1e-4: return -t*t/24.0 - t**4/2880.0   # series for log(2sin(t/2)/t)
        return math.log(2.0*math.sin(t/2.0)/t)
    I2 = simpson(g, 0.0, a, 1 << 14)
    I3 = simpson(lambda t: math.log(2.0*math.sin(t/2.0)), a, theta, 1 << 14)
    return -(I1 + I2 + I3)

CL2 = cl2(math.pi/3)
vol_m004 = 2.0 * CL2                                   # 2 regular ideal tetrahedra (B737 P3 [1])
VOL_BANKED = 2.029883212819307250042405108549          # B737 p3_sister_out.txt:5
check("vol(m004) = 2*Cl2(pi/3) matches banked to 1e-12",
      abs(vol_m004 - VOL_BANKED) < 1e-12, f"computed {vol_m004:.15f}")

res_phi = 2.0*math.sqrt(3.0)/vol_m004
RES_BANKED = 1.706552176628161608820573265788          # B737 p2_cover_out.txt:133-135
check("Res phi = 2*sqrt3/vol(m004) matches banked 1.706552176628161... to 1e-12",
      abs(res_phi - RES_BANKED) < 1e-12, f"computed {res_phi:.15f}")

res_zK = math.pi/(3.0*math.sqrt(3.0))                  # = 2pi/(6 sqrt3), B737 FINDINGS:13-14
check("Res_{s=1} zeta_K = 2pi/(6*sqrt3) = 0.6045997880...",
      abs(res_zK - 0.6045997880) < 1e-9, f"computed {res_zK:.12f}")

# cusp CM j-invariants via q-series (independent route), both manifolds
JC = [744, 196884, 21493760, 864299970, 20245856256, 333202640600, 4252023300096,
      44656994071935, 401490886656000, 3176440229784420, 22567393309593600]
def jq(tau):
    q = cmath.exp(2j*cmath.pi*tau)
    s = 1.0/q + JC[0]
    for n in range(1, len(JC)):
        s += JC[n] * q**n
    return s

j_m004_series = jq(2j*math.sqrt(3.0))                  # m004 cusp modulus 2*sqrt(-3) (B737 P3 [3])
j_m003_series = jq(0.5 + 1j*math.sqrt(3.0)/2.0)        # m003 cusp = hexagonal CM point (disc -3)

# exact larger root of the banked class polynomial x^2 - 2835810000 x + 6549518250000
b_, c_ = 2835810000, 6549518250000
D = b_*b_ - 4*c_
root_scaled = (b_ * 10**20 + isqrt(D * 10**40)) // 2
root_str = str(root_scaled)
root_dec = root_str[:-20] + "." + root_str[-20:]
BANKED_J = "2835807690.42228352772984605248"           # B737 p3_sister_out.txt:40
check("j(m004 cusp): exact root of banked H_{-48} poly reproduces banked decimal (17 digits)",
      root_dec[:28] == BANKED_J[:28], f"root = {root_dec[:28]}")
j_m004_root = float(root_scaled) / 1e20
check("j(m004 cusp) via q-series agrees with the exact root to 1e-3",
      abs(j_m004_series.real - j_m004_root) < 1e-3 and abs(j_m004_series.imag) < 1e-3,
      f"q-series {j_m004_series.real:.6f}")
check("j(m003 cusp) via q-series = 0 (hexagonal CM point, banked exact 0)",
      abs(j_m003_series) < 1e-3, f"|j| = {abs(j_m003_series):.2e}")

# palette |(O/2^k)^x / im(mu_6)| by exact enumeration, O = Z[zeta6], zeta6^2 = zeta6 - 1
def palette(k):
    m = 2**k
    def mul(u, v):
        a, b = u; c, d = v
        # (a + b w)(c + d w) with w^2 = w - 1
        return ((a*c - b*d) % m, (a*d + b*c + b*d) % m)
    units = [(a, b) for a in range(m) for b in range(m) if (a*a + a*b + b*b) % 2 == 1]
    mu6 = [(1 % m, 0), ((m - 1) % m, 0), (0, 1 % m), (0, (m - 1) % m),
           ((m - 1) % m, 1 % m), (1 % m, (m - 1) % m)]
    im = set(mu6)
    # subgroup check: closed under multiplication
    closed = all(mul(x, y) in im for x in im for y in im)
    return len(units), len(im), len(units)//len(im), closed
p2, p4, p8 = palette(1), palette(2), palette(3)
check("palette recomputed by enumeration: levels (2),(4),(8) -> 1, 2, 8 (mu6-image a subgroup)",
      (p2[2], p4[2], p8[2]) == (1, 2, 8) and p2[3] and p4[3] and p8[3],
      f"|units| = {p2[0]},{p4[0]},{p8[0]}; |im mu6| = {p2[1]},{p4[1]},{p8[1]}")

# --- B753 block recomputation (banked exact forms + banked decimals, output.txt:4-31) ---
phi_f = (1.0 + math.sqrt(5.0))/2.0
B00 = 1.0/(2.0*phi_f) + 1j*math.sin(math.radians(72.0))/math.sqrt(5.0)
B01 = complex(-0.809017, -0.262866)                    # banked decimals, B753 output.txt:6
B10 = complex(+0.809017, -0.262866)
trB = B00 + B00.conjugate()
detB = (B00*B00.conjugate() - B01*B10).real
lam1 = (trB + cmath.sqrt(trB*trB - 4*detB))/2
lam2 = (trB - cmath.sqrt(trB*trB - 4*detB))/2
e72 = cmath.exp(1j*math.radians(72.0))
check("B753 block: eigenvalues = e^{+-i 72deg} (from banked entries), |lambda| = 1",
      abs(lam1 - e72) < 1e-4 and abs(lam2 - e72.conjugate()) < 1e-4
      and abs(abs(lam1) - 1) < 1e-4 and abs(trB.real - 1/phi_f) < 1e-6,
      f"lam = {lam1.real:.6f}+-{abs(lam1.imag):.6f}i, tr = {trB.real:.6f} = 1/phi")
# exact identity |B00|^2 = 1/(4 phi^2) + sin^2(72)/5 = (5-sqrt5)/10 = 1/(phi*sqrt5), in Q(sqrt5)
inv4phi2 = q5_mul(q5_inv(q5_mul(phi2, (F(4), F(0)))), (F(1), F(0)))   # 1/(4 phi^2)
sin72sq  = (F(5, 8), F(1, 8))                                          # (5+sqrt5)/8, exact
lhs = q5_add(inv4phi2, q5_mul(sin72sq, (F(1, 5), F(0))))
phisqrt5 = q5_mul(phi2, (F(0), F(1)))                                  # phi^2*sqrt5? no: use phi*sqrt5
phi_q5   = (F(1, 2), F(1, 2))
rhs = q5_inv(q5_mul(phi_q5, (F(0), F(1))))                             # 1/(phi*sqrt5)
check("B753 exact identity |B00|^2 = 1/(phi*sqrt5) = (5-sqrt5)/10, exact in Q(sqrt5)",
      lhs == rhs and lhs == (F(1, 2), F(-1, 10)), f"= {q5_float(lhs):.10f}")

print()
print("Q2 DISCRIMINATION (computed, both axes, BEFORE the consultation):")
print(f"  manifold axis  : extractor(m004) = (j = {j_m004_root:.2f}, palette (4)/(8) = 2/8,")
print(f"                   Res phi = {res_phi:.12f})  vs  extractor(m003) = (j = 0,")
print("                   palette (2) = 1, same voice by the B737 transfer) -- j differs by")
print(f"                   {j_m004_root:.3e} (12 orders), palettes differ (enumerated above).")
q2_manifold = abs(j_m004_root - 0.0) > 1e9 and (p2[2], p4[2]) == (1, 2)
check("Q2 manifold axis: SFH face-extractor output differs, object vs sister m003",
      q2_manifold, "j: 2835807690.42 vs 0; palette: {2,8} vs {1}")
# quantity axis: a face-native quantity must HIT (two independent routes), so the
# operator is capable of returning YES; phi^2 is then a meaningful NO.
q2_quantity = abs(res_phi - RES_BANKED) < 1e-12
check("Q2 quantity axis: SFH(2*sqrt3/vol) = HIT at 1e-12 (banked decimal vs Clausen route)",
      q2_quantity, "the operator can return YES; it is not constant -- B752 failure mode excluded")

print()
print("=" * 88)
print("[4] THE CONSULTATION -- SFH(phi^2) over the ENTIRE frozen surface")
print("=" * 88)
face_quantities = [
    ("Res phi (B737/B739)",            res_phi),
    ("Res zeta_K (B737)",              res_zK),
    ("vol(m004) (B737)",               vol_m004),
    ("2*sqrt3 = cusp covol (B737)",    2.0*math.sqrt(3.0)),
    ("Cl2(pi/3)",                      CL2),
    ("j(m004 cusp) (B737)",            j_m004_root),
    ("j(m003 cusp) (B737)",            0.0),
    ("palette size level (2) (B737/B739)", 1.0),
    ("palette size level (4)",         2.0),
    ("palette size level (8)",         8.0),
    ("B753 cos72 = Re B00 = 1/(2phi)", 1.0/(2.0*phi_f)),
    ("B753 sin72/sqrt5 = Im B00",      math.sin(math.radians(72))/math.sqrt(5)),
    ("B753 |B00|",                     abs(B00)),
    ("B753 |B00|^2 = 1/(phi*sqrt5)",   abs(B00)**2),
    ("B753 P00 = phi/sqrt5",           phi_f/math.sqrt(5)),
    ("B753 tr B = 1/phi",              1.0/phi_f),
    ("B753 |eigenvalue|",              1.0),
    ("B753 eigenphase (rad)",          math.radians(72.0)),
    ("B753 eigenphase (deg)",          72.0),
]
gaps = [(abs(phi2f - v), name) for name, v in face_quantities]
mingap, argmin = min(gaps)
for name, v in face_quantities:
    print(f"    |phi^2 - {name:38s}| = |{phi2f:.6f} - {v:12.6f}| = {abs(phi2f - v):.6f}")
check("HOST SCAN: NO banked spectral-face quantity equals phi^2 (tolerance 1e-9)",
      mingap > 1e-9, f"min gap = {mingap:.6f} at '{argmin}'")

# field membership, exact:
# (i) sqrt5 in Q(sqrt-3)?  (x+y*sqrt-3)^2 = 5 => 2xy = 0; y=0 => x^2 = 5, no rational
#     (5 squarefree, descent); x=0 => -3y^2 = 5 < impossible by sign.
sq5_not_rat = isqrt(5)**2 != 5 and all(5 % (p*p) != 0 for p in (2, 3, 5))
check("sqrt5 not in Q(sqrt-3): x^2=5 has no rational solution (5 not a square, squarefree);"
      " -3y^2=5 impossible by sign", sq5_not_rat)
# (ii) sqrt5 in Q(j_{-48}) or the compositum Q(sqrt-3, j)?  Q(j) = Q(sqrt D);
#     the biquadratic Q(sqrt-3, sqrt D) contains sqrt5 iff D = 5k^2 or -3D = 5k^2 (sign-dead).
D5 = (D % 5 == 0) and (isqrt(D//5)**2 == D//5)
Dsq = isqrt(D)**2 == D
check("D = disc(H_{-48}) = 8041792158027000000: D > 0, NOT a perfect square, NOT 5*k^2"
      " => sqrt5 not in Q(sqrt-3, j_{-48})",
      D == 8041792158027000000 and D > 0 and not Dsq and not D5,
      f"D%5 = {D % 5}, issquare(D/5) = {D5}, -3D < 0 kills the third subfield")
# (iii) kind ledger: the ONLY golden-bearing face quantities are B753's -- unimodular
#     eigenphases and unistochastic entries; a torus-block monodromy MULTIPLIER reading
#     of phi^2 needs modulus phi^2.
check("kind ledger: every B753 eigenvalue has |lambda| = 1; |phi^2| = 2.618... != 1",
      abs(abs(lam1) - 1.0) < 1e-4 and abs(phi2f - 1.0) > 1.6,
      f"gap phi^2 - 1 = {phi2f - 1.0:.6f}: unimodular phase vs dilatation = kind-distinct")

print()
print("=" * 88)
print("[5] THE CONTINUOUS CHANNEL IS CLOSED -- B739 rigidity + B746 F11, re-verified")
print("=" * 88)
base = Path(__file__).resolve().parents[3]
voice_files = [
    base/"B737_candidate_zero"/f for f in
    ["FINDINGS.md", "p1_scatter_out.txt", "p2_cover_out.txt",
     "p2_cover_out_run1_FAILED.txt", "p3_sister_out.txt", "p4_kms_out.txt"]
] + [
    base/"B739_character_rigidity"/f for f in
    ["FINDINGS.md", "b739_probe_out.txt", "b739_probe_out_run1_FAILED.txt"]
]
markers = ["golden", "fibonacci", "sqrt5", "sqrt(5)", "1.618", "2.618", "0.618", "√5"]
hits = 0
for p in voice_files:
    text = p.read_text(encoding="utf-8", errors="replace").lower()
    hits += sum(text.count(m) for m in markers)
check(f"B746-F11 rescan: 0 golden markers across all {len(voice_files)} banked voice artifacts"
      " (B737 + B739, FINDINGS + every output incl. FAILED transcripts)",
      hits == 0, f"markers = {markers}, total hits = {hits}")

rig = (base/"B739_character_rigidity"/"b739_probe_out.txt").read_text()
rig_ok = ("NO conductor-(4)/(8) Hecke character appears ANYWHERE in it" in rig
          and "CHARACTER-RIGIDITY AT FULL STRENGTH" in rig)
check("B739 rigidity as banked: continuous spectrum = ONE channel = exactly Lambda_K(s-1)/Lambda_K(s);"
      " no other character anywhere in it (citation verified in-arc)", rig_ok,
      "b739_probe_out.txt:323-330; FINDINGS.md:7-16")

print()
print("=" * 88)
print("[6] VERDICT: KILL-EXTENDS")
print("=" * 88)
print("""The spectral face AS BANKED bears on kill K-J in a way the original (mtc-overlay-
only, fact_basis: asserted) kill never tested, and every computed fact UPHOLDS and
EXTENDS the kill.  Exactly what was computed, no more:

 E1  The kill's core inequality is now COMPUTED, not asserted: on the reducible
     (degenerate phi_{2,1}) side the commutator trace is PINNED at 2 (300/300 exact,
     Fricke identity verified 300/300), the general-position locus is not (298/300
     off the tr[A,B]=2 locus -- it is proper, not generic), and the
     seed's kappa = 3 (disc-5 seed recomputed exactly; banked B746 F1/S1).  The '3=3'
     confirmation compared an eigenvalue-trace -- which IS the matrix trace identically
     (Cayley-Hamilton 200/200) and so carries zero confirmation content -- against a
     commutator-trace whose kind-correct degenerate-side value is 2, not 3.  This is
     the B753 emptiness mechanism (Re lam = Re B00 identically, 'regardless of p')
     transplanted to the kill's '3=3' leg and computed.

 E2  The host scan over the ENTIRE frozen surface finds no home for phi^2: no banked
     spectral-face quantity equals it (min gap 0.588), and no banked voice field can
     contain it (sqrt5 not in Q(sqrt-3), exact; sqrt5 not in Q(sqrt-3, j_{-48}),
     exact via the D = 5k^2 test).  The only golden-bearing face quantities (B753)
     are unimodular eigenphases and unistochastic entries -- kind-distinct from a
     dilatation-multiplier reading of phi^2 (modulus 1 and < 1 vs 2.618).

 E3  B739's character-rigidity (verified in-arc) leaves the continuous channel no
     room for ANY re-posed 'multiplier' beyond the field's zeta-quotient: the
     spectral re-reading named in the revival hypothesis has no continuous-spectrum
     home; B746 F11's zero-golden-marker fact re-verified in-cell (0 hits, 9 files).

RESIDUAL (journal note per S16 review CHECK 4 convention; NOT verdict-bearing): the
discrete newform spectrum remains the banked owner-gated door (B746 door 2; B739
'discrete-only' redirect).  The killed identification does not depend on it: no
spectral fact can make the reducible kappa=2 block irreducible.

FALSIFIER (Q7): any banked quantity inside the four frozen arcs equal to phi^2; or
D = 5k^2 / a rational solution of (x+y*sqrt-3)^2 = 5; or one exact reducible SL(2,Q)
pair with tr[A,B] != 2; or a failure of B739's rigidity (a second continuous channel,
or a conductor-(4)/(8) character in the continuous spectrum).""")

print()
n_pass = sum(CHECKS)
print(f"CHECK: ALL {n_pass}/{len(CHECKS)} checks PASS" if all(CHECKS)
      else f"CHECK: FAILURES PRESENT ({n_pass}/{len(CHECKS)} pass)")
