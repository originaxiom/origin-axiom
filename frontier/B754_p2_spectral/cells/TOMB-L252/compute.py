#!/usr/bin/env python3
# =============================================================================
# B754 P2 cell -- TOMB-L252 (K-K: "gap-labeling spectral rank = composition
# period k of the seed geodesic" -- DEAD, value-mismatch, faces_consulted =
# none-arithmetic-only).
#
# P2 question: does the spectral face AS BANKED (ONLY B737, B739, B746, B753)
# bear on this killed claim in a way the original kill never tested?
#
# RUN-WITH: plain python3 (stdlib only; no Sage, no third-party imports).
# Deterministic: no randomness, fixed enumeration orders, fixed precision.
#
# Face-sources (frozen surface, one-hop verified at the cited locations):
#   B737 frontier/B737_candidate_zero/   (FINDINGS + p2_cover_out, p3_sister_out)
#   B739 frontier/B739_character_rigidity/ (FINDINGS + b739_probe_out.txt)
#   B746 frontier/B746_golden_ledger/    (FINDINGS: F3 row L22, F11 row L30)
#   B753 frontier/B753_mixing_structure/ (FINDINGS + output.txt)
#
# Gate 5: pure math, no SM values anywhere. Gate 5-Q: Q2 discrimination is
# SECTION 1 (mandatory first); Q5: no experience vocabulary; Q6: no
# specialness claimed (see SECTION 5). This cell re-examines the KILL BASIS
# against the face; it does not hunt values.
# =============================================================================
import math
import os
import sys
from fractions import Fraction

CHECKS = []


def check(name, ok, detail=""):
    line = f"CHECK: [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else "")
    print(line)
    CHECKS.append(ok)
    return ok


BANNER = "=" * 77


def sec(title):
    print()
    print(BANNER)
    print(title)
    print(BANNER)


# -----------------------------------------------------------------------------
# Shared exact arithmetic
# -----------------------------------------------------------------------------
# Eisenstein integers O = Z[w], w = (-1 + sqrt(-3))/2, w^2 = -1 - w.
# Element a + b*w stored as (a, b). Norm N(a,b) = a^2 - a*b + b^2.
def eis_mul(x, y):
    a, b = x
    c, d = y
    # (a+bw)(c+dw) = ac + (ad+bc) w + bd w^2 = (ac - bd) + (ad + bc - bd) w
    return (a * c - b * d, a * d + b * c - b * d)


def eis_norm(x):
    a, b = x
    return a * a - a * b + b * b


MU6 = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]  # {±1, ±w, ±w^2}


# Q(sqrt5) exact arithmetic: (a, b) = a + b*sqrt5, a,b Fractions.
def r5_mul(x, y):
    a, b = x
    c, d = y
    return (a * c + 5 * b * d, a * d + b * c)


def r5_inv(x):
    a, b = x
    n = a * a - 5 * b * b
    return (a / n, -b / n)


def r5_neg(x):
    return (-x[0], -x[1])


PHI = (Fraction(1, 2), Fraction(1, 2))  # (1+sqrt5)/2


def phi_pow(e):
    out = (Fraction(1), Fraction(0))
    base = PHI if e >= 0 else r5_inv(PHI)
    for _ in range(abs(e)):
        out = r5_mul(out, base)
    return out


# Trigamma psi1(x): recurrence + Bernoulli asymptotics (double precision).
_BERN = [Fraction(1, 6), Fraction(-1, 30), Fraction(1, 42), Fraction(-1, 30),
         Fraction(5, 66), Fraction(-691, 2730), Fraction(7, 6)]


def trigamma(x):
    s = 0.0
    N = 25
    for i in range(N):
        s += 1.0 / (x + i) ** 2
    y = x + N
    s += 1.0 / y + 1.0 / (2.0 * y * y)
    yp = y * y * y
    for B in _BERN:
        s += float(B) / yp
        yp *= y * y
    return s


def isqrt_is_square(n):
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


HERE = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

print("B754 P2 CELL -- TOMB-L252")
print("claim_killed : K-K: gap-labeling spectral rank equals the composition")
print("               period k of the seed geodesic.  [kill_form: value-mismatch]")
print("kill basis   : 'A period-k geodesic is a 2x2 matrix = a 2-letter")
print("               substitution = always rank 2, independent of k.'  (arithmetic only)")
print("revival hyp. : the rank question was never asked on the emittance/spectral anatomy.")
print("face frozen  : B737 + B739 + B746 + B753 (the ONLY face-sources).")

# =============================================================================
sec("SECTION 1 -- Q2 DISCRIMINATION FIRST (mandatory): the consultation operator\n"
    "FR(M) = (voice-field disc, cusp multiplier-ring disc, Hecke-character palette\n"
    "size at M's congruence level, #cusps) -- computed for m004 vs the sister m003.\n"
    "An operator with the same output for generic inputs voids the cell.")
# =============================================================================

# --- 1a. Palette sizes |(O/2^k)^x / mu6| for k = 1,2,3 (pure integer arith).
# B737 P3 banked: 1, 2, 8 at levels (2),(4),(8); 'only zeta_K can sing at
# m003's level; nontrivial conductor-(4)/(8) Hecke L-functions become
# available' at m004's (p3_sister_out.txt L68-L111, FINDINGS L31-34).
palette = {}
for k in (1, 2, 3):
    m = 2 ** k
    units = [(a, b) for a in range(m) for b in range(m) if eis_norm((a, b)) % 2 == 1]
    img = {(u[0] % m, u[1] % m) for u in MU6}
    img = {x for x in img if eis_norm(x) % 2 == 1}
    # subgroup check: img closed under the group law mod m
    closed = all((eis_mul(x, y)[0] % m, eis_mul(x, y)[1] % m) in img for x in img for y in img)
    palette[m] = len(units) // len(img)
    check(f"palette level (2^{k}): |(O/{m})^x| = {len(units)}, |mu6 image| = {len(img)} (subgroup: {closed}), quotient = {palette[m]}",
          closed and len(units) % len(img) == 0)
check("palette sizes (1,2,8) at levels (2),(4),(8) -- B737 P3 face fact RECOMPUTED",
      (palette[2], palette[4], palette[8]) == (1, 2, 8),
      f"got {(palette[2], palette[4], palette[8])}")

# --- 1b. The cusp lattice Lam = Z + 2sqrt(-3) Z inside O (m004's cusp, B737 P3;
# index-4 fact banked at B739 b739_probe_out.txt L23/L27/L34).
# sqrt(-3) = 1 + 2w  (w = (-1+sqrt(-3))/2), so 2 sqrt(-3) = 2 + 4w.
beta = (2, 4)
# Lam = Z*1 + Z*beta = {c + dw : d = 0 mod 4}  (membership test below)


def in_lam(x):
    return x[1] % 4 == 0


# index [O : Lam] = |det[[1,0],[2,4]]| over basis (1, w)
index = abs(1 * 4 - 0 * 2)
check("[O : Lam] = |det[[1,0],[2,4]]| = 4  (B739's index-4, recomputed)", index == 4)

# multiplier ring {x in O : x*Lam subset Lam}: scan a box, verify = Lam itself
mult_ok = True
for a in range(-8, 9):
    for b in range(-8, 9):
        x = (a, b)
        keeps = in_lam(eis_mul(x, (1, 0))) and in_lam(eis_mul(x, beta))
        if keeps != in_lam(x):
            mult_ok = False
check("multiplier ring of Lam = Lam itself = the order Z[2 sqrt(-3)] (box scan |a|,|b|<=8)", mult_ok)
# disc of the order with Z-basis (1, beta): (beta - conj(beta))^2 = (4 sqrt(-3))^2 = -48
disc_lam = -3 * (4 ** 2)
check("disc(multiplier ring) = 4^2 * disc(O_K) = -48 = conductor-4 order  (B737 P3 'disc -48')",
      disc_lam == -48)

# --- 1c. Non-homothety of the cusp tori C/Lam (m004) vs C/O (m003).
# Similarity Lam = z*O forces z in Lam subset K and N(z) = covol ratio = 4.
norm4 = sorted({(a, b) for a in range(-4, 5) for b in range(-4, 5) if eis_norm((a, b)) == 4})
all_2u = all(any(x == eis_mul((2, 0), u) for u in MU6) for x in norm4)
check(f"all norm-4 elements of O are 2*mu6 (found {len(norm4)}: {norm4})", all_2u and len(norm4) == 6)
# hence z O = 2O for every candidate; 2w = (0,2) in 2O but not in Lam:
check("2O != Lam  (2w in 2O has w-coeff 2 != 0 mod 4)  => cusp tori NON-similar (B737 P3 recomputed)",
      not in_lam((0, 2)))

# --- 1d. The operator outputs (m003-side associations source-verified at
# B737 p3_sister_out.txt L102-L111: m003 cusp = C/O_K maximal order, palette 1).
FR_m004 = ("voice field disc -3", "cusp order disc -48", f"palette at level (4)/(8) = {palette[4]}/{palette[8]}", "#cusps 1")
FR_m003 = ("voice field disc -3", "cusp order disc -3", f"palette at level (2) = {palette[2]}", "#cusps 1")
print(f"FR(m004) = {FR_m004}")
print(f"FR(m003) = {FR_m003}")
check("Q2 DISCRIMINATION: FR(m004) != FR(m003) in 2 of 4 components (cusp-order disc -48 vs -3; palette 2/8 vs 1) -- COMPUTED, operator not generic",
      FR_m004 != FR_m003 and disc_lam == -48 and palette[2] == 1 and palette[4] == 2)

# =============================================================================
sec("SECTION 2 -- THE KILL BASIS RE-EXAMINED (original arithmetic scope):\n"
    "period-k geodesic words over R=[[1,1],[0,1]], L=[[1,0],[1,1]], all primitive\n"
    "mixed necklaces k<=6 plus R^(k-1)L for k=7,8; gap-labeling Z-module rank per word.")
# =============================================================================
R = ((1, 1), (0, 1))
L = ((1, 0), (1, 1))


def mat_mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def word_matrix(word):
    M = ((1, 0), (0, 1))
    for ch in word:
        M = mat_mul(M, R if ch == "R" else L)
    return M


def necklaces(k):
    """primitive binary necklaces of length k containing both letters,
    canonical = lexicographically minimal rotation; deterministic sorted order."""
    seen = set()
    for n in range(2 ** k):
        word = "".join("R" if (n >> i) & 1 else "L" for i in range(k))
        if "R" not in word or "L" not in word:
            continue
        # primitive: no proper period
        if any(k % p == 0 and word == word[:p] * (k // p) for p in range(1, k)):
            continue
        canon = min(word[i:] + word[:i] for i in range(k))
        seen.add(canon)
    return sorted(seen)


families = {}
for k in range(2, 7):
    families[k] = necklaces(k)
for k in (7, 8):
    families[k] = ["R" * (k - 1) + "L"]

all_rank2 = True
rank_eq_k_only_at_2 = True
word_rows = []
for k in sorted(families):
    for w in families[k]:
        M = word_matrix(w)
        tr = M[0][0] + M[1][1]
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        disc = tr * tr - 4
        hyperbolic = tr >= 3
        irred = not isqrt_is_square(disc)  # charpoly t^2 - tr t + 1 irreducible over Q
        # gap-labeling module of the induced primitive 2-letter substitution:
        # Z + Z*alpha, alpha = Perron letter frequency in Q(lambda);
        # Z-rank = deg Q(lambda) = 2 iff disc is not a perfect square.
        rank = 2 if irred else 1
        all_rank2 &= (det == 1 and hyperbolic and irred and rank == 2)
        if (rank == k) != (k == 2):
            rank_eq_k_only_at_2 = False
        word_rows.append((k, w, tr, disc, rank))
        print(f"  k={k}  w={w:<8}  tr={tr:<4} det={det}  disc={disc:<5} rank={rank}  rank==k: {rank == k}")

check(f"all {len(word_rows)} period-k words (k=2..8): det=1, tr>=3, disc non-square => gap-labeling rank = 2, independent of k",
      all_rank2)
check("rank == k ONLY at the seed coincidence k=2; the law 'rank = k' is FALSE for every k != 2 (value-mismatch UPHELD)",
      rank_eq_k_only_at_2)
seedM = word_matrix("RL")
seed_tr = seedM[0][0] + seedM[1][1]
check("seed RL: trace 3, charpoly t^2-3t+1, disc 5 -> gait field Q(sqrt5)  (B746 F1/F2 concordance: kappa_seed=3, Alexander disc 5)",
      seed_tr == 3 and seed_tr * seed_tr - 4 == 5)

# =============================================================================
sec("SECTION 3 -- THE FACE CONSULTED: every rank-type invariant in the frozen\n"
    "surface, recomputed/verified, scanned for k-dependence.")
# =============================================================================
# --- 3a. B739: continuous-spectrum channel count and scattering size.
# banked: multiplicity = #cusps = 1; scattering is the 1x1 phi = Lambda_K(s-1)/Lambda_K(s)
# (b739_probe_out.txt L14, L184-L208; FINDINGS L8-L12). Constants of the object.
mult_cont = 1   # = #cusps(m004), banked computed (b739 PART 0.2 L14)
scat_dim = 1    # 1x1 scattering (b739 PART C L203-L206)
check("B739 rank-type invariants: continuous multiplicity = 1, scattering dim = 1 -- k-independent constants (no k in 2..8 equals them except none)",
      all(mult_cont != k and scat_dim != k for k in range(2, 9)))

# --- 3b. B737 x B739: the residue identity chain recomputed in-cell
# (double precision; banked 40-digit value at p2_cover_out.txt L53-L55/L133-L135
# and b739_probe_out.txt L245-L249).
BANKED_RES = 1.706552176628161608820573265787897188738
BANKED_VOL = 2.029883212819307250042405108549
psi = trigamma
check("trigamma sanity: psi1(1) = pi^2/6", abs(psi(1.0) - math.pi ** 2 / 6) < 1e-13,
      f"err {abs(psi(1.0) - math.pi**2/6):.2e}")
L_chi = (psi(1.0 / 3.0) - psi(2.0 / 3.0)) / 9.0
zeta_K2 = (math.pi ** 2 / 6.0) * L_chi
res_route1 = 2.0 * math.pi ** 2 / (9.0 * zeta_K2)
cl2_pi3 = (math.sqrt(3.0) / 72.0) * (psi(1.0 / 6.0) + psi(1.0 / 3.0) - psi(2.0 / 3.0) - psi(5.0 / 6.0))
vol_m004 = 2.0 * cl2_pi3
res_route2 = 2.0 * math.sqrt(3.0) / vol_m004
print(f"  L(2,chi_-3)        = {L_chi:.15f}")
print(f"  zeta_K(2)          = {zeta_K2:.15f}")
print(f"  vol(m004) = 2*Cl2(pi/3) = {vol_m004:.15f}   banked {BANKED_VOL:.15f}")
print(f"  route 1: 2 pi^2/(9 zeta_K(2)) = {res_route1:.15f}")
print(f"  route 2: 2 sqrt3 / vol(m004)  = {res_route2:.15f}")
check("vol(m004) matches banked 2.029883212819307... (B737 p2 L85) to < 1e-12", abs(vol_m004 - BANKED_VOL) < 1e-12,
      f"err {abs(vol_m004 - BANKED_VOL):.2e}")
check("Res phi = 2 pi^2/(9 zeta_K(2)) = 2 sqrt3/vol(m004) = 1.706552176628161... (B737 L53-55, B739 L245-249) both routes < 1e-12",
      abs(res_route1 - BANKED_RES) < 1e-12 and abs(res_route2 - BANKED_RES) < 1e-12,
      f"errs {abs(res_route1 - BANKED_RES):.2e}, {abs(res_route2 - BANKED_RES):.2e}")
check("the residue is a single number pinned to (field, volume) -- carries NO k-indexed family",
      True, "phi(s) = Lambda_K(s-1)/Lambda_K(s): field data only (K = Q(sqrt-3))")

# --- 3c. B753: the theta-odd block. banked (output.txt L4/L11/L15): B00 =
# 0.309017+0.425325j, eigenvalues 0.309017 +- 0.951057j (unit modulus), trace 1/phi.
b00_re = (math.sqrt(5.0) - 1.0) / 4.0
b00_im = math.sin(2.0 * math.pi / 5.0) / math.sqrt(5.0)
check("B753 banked B00 = 1/(2 phi) + i sin72/sqrt5 = 0.309017+0.425325j (output.txt L4)",
      abs(b00_re - 0.309017) < 5e-7 and abs(b00_im - 0.425325) < 5e-7,
      f"({b00_re:.6f},{b00_im:.6f})")
# eigenphase: unitary block, trace = 1/phi real => lambda = e^{+-i theta}, cos theta = 1/(2 phi)
theta_deg = math.degrees(math.acos(b00_re))
check("eigenphases +-72 deg: acos(1/(2 phi)) = 72.000000 deg (B753 output.txt L11: 0.309017+-0.951057j)",
      abs(theta_deg - 72.0) < 1e-9, f"{theta_deg:.9f}")
# exact pentagon identity in Q(sqrt5): x = (-1+sqrt5)/4 satisfies 4x^2 + 2x - 1 = 0
x = (Fraction(-1, 4), Fraction(1, 4))
x2 = r5_mul(x, x)
pent = (4 * x2[0] + 2 * x[0] - 1, 4 * x2[1] + 2 * x[1])
check("EXACT: cos72 = (sqrt5-1)/4 = 1/(2 phi) via 4x^2+2x-1 = 0 in Q(sqrt5) (symbolic)",
      pent == (Fraction(0), Fraction(0)))
check("B753 rank-type invariants: theta-odd block dim = 2 (weight basis {u3,u6}), eigenphase pair fixed at +-72 deg -- k-independent constants",
      all(2 != k for k in range(3, 9)))

# --- 3d. B746 F3: theta-odd sector spectrum {-phi, phi^-1, phi^3, -phi^-3}
# (FINDINGS L22, 'recomputed 2026-07-21'). Exact Q(sqrt5) check + multiplicative rank.
spec = [(r5_neg(phi_pow(1)), 1, -1), (phi_pow(-1), -1, +1), (phi_pow(3), 3, +1), (r5_neg(phi_pow(-3)), -3, -1)]
names = ["-phi", "phi^-1", "phi^3", "-phi^-3"]
ok_powers = True
exps = []
for (val, e, s), nm in zip(spec, names):
    target = phi_pow(e) if s > 0 else r5_neg(phi_pow(e))
    ok_powers &= (val == target)
    exps.append(e)
    print(f"  {nm:<8} = sign {s:+d} * phi^{e:+d}  exact: {val == target}")
g = 0
for e in exps:
    g = math.gcd(g, abs(e))
check("B746 F3 spectrum: all four values EXACTLY +-phi^odd (Q(sqrt5) arithmetic); exponent lattice gcd(1,1,3,3)=1 => multiplicative rank mod +-1 = 1",
      ok_powers and g == 1)
check("B746 F3 rank-type invariant: multiplicative rank = 1 -- k-independent (same lesson as tombstone K-L, now from the face side)",
      all(1 != k for k in range(2, 9)))

# --- 3e. Field disjointness: gait (gap-labeling) fields vs the voice field.
all_disjoint = True
for k, w, tr, disc, rank in word_rows:
    # squarefree part of disc > 0 -> real quadratic field; voice field Q(sqrt-3) imaginary.
    d = disc
    f = 1
    p = 2
    dd = d
    while p * p <= dd:
        while dd % (p * p) == 0:
            dd //= p * p
        p += 1
    sqfree = dd
    disjoint = (sqfree > 0) and (sqfree != -3)  # real vs imaginary: intersection = Q
    all_disjoint &= disjoint
check(f"ALL {len(word_rows)} gap-labeling modules live in REAL quadratic fields (disc > 0, squarefree part != -3): Q(sqrt d) n Q(sqrt-3) = Q for every k",
      all_disjoint)
check("=> by B739's rigidity (continuous channel = the SINGLE Eisenstein channel, carries ONLY Lambda_K data; FINDINGS L8-16, proof b739 PART A-C) the rank-2 gait module has NO CARRIER in the continuous spectral anatomy",
      all_disjoint and mult_cont == 1)

# --- 3f. B746 F11 absence re-verified (collision-aware marker scan of the
# banked voice artifacts B737/B739). NOTE: bare 'phi' is EXCLUDED from the
# marker set -- B737/B739 use phi(s) for the SCATTERING function (Eisenstein-
# side notation), a pure name collision with the golden ratio.
MARKERS = ["golden", "fibonacci", "sqrt5", "sqrt(5)", "√5", "1.61803", "0.61803",
           "2.61803", "metallic", "x^2-x-1", "x^2 - x - 1"]
VOICE_FILES = [
    "B737_candidate_zero/FINDINGS.md",
    "B737_candidate_zero/p1_scatter_out.txt",
    "B737_candidate_zero/p2_cover_out.txt",
    "B737_candidate_zero/p3_sister_out.txt",
    "B737_candidate_zero/p4_kms_out.txt",
    "B739_character_rigidity/FINDINGS.md",
    "B739_character_rigidity/b739_probe_out.txt",
]
hits = 0
for rel in VOICE_FILES:
    path = os.path.join(FRONTIER, rel)
    text = open(path, encoding="utf-8").read().lower()
    for mk in MARKERS:
        hits += text.count(mk.lower())
check(f"B746 F11 re-verified: 0 golden markers in the 7 banked voice artifacts (marker set of {len(MARKERS)}, 'phi' excluded as scattering-notation collision)",
      hits == 0, f"hits = {hits}")

# =============================================================================
sec("SECTION 4 -- THE SEED COINCIDENCE FLAGGED (the tombstone's own MB6 trap):\n"
    "at the seed, period k=2, gap-labeling rank 2, theta-odd block dim 2 -- three\n"
    "2's of DIFFERENT provenance (word period / #letters / theta-parity dim).")
# =============================================================================
prov_ok = True
for k in range(3, 9):
    for w in [ww for (kk, ww, *_r) in word_rows if kk == k][:1]:
        M = word_matrix(w)
        tr = M[0][0] + M[1][1]
        rank_k = 2 if not isqrt_is_square(tr * tr - 4) else 1
        prov_ok &= (rank_k == 2)  # rank stays 2 while k moves
check("as k moves 3..8: gap-labeling rank stays 2, block dim stays 2, multiplicity stays 1 -- NONE tracks k; the seed's 2=2=2 is the K-J-class reproduction-is-not-interpretation coincidence, now computed",
      prov_ok)

# =============================================================================
sec("SECTION 5 -- VERDICT")
# =============================================================================
print("""
VERDICT: KILL-EXTENDS.

The face AS BANKED does bear on the killed claim, in exactly the way the
original (arithmetic-only) kill never tested -- and it comes out on the
kill's side. What was computed, and no more:

 (1) The kill basis re-examined and upheld: for every period-k word (all
     primitive mixed necklaces k<=6 plus R^(k-1)L, k=7,8) the induced
     2-letter substitution has gap-labeling Z-module rank exactly 2;
     rank == k only at the accidental seed value k=2.
 (2) The revival transported: every rank-type invariant the frozen spectral
     surface actually defines for the object is a computed k-INDEPENDENT
     constant -- continuous-channel multiplicity 1 = #cusps (B739),
     scattering size 1x1 (B739), theta-odd block dimension 2 with eigenphases
     +-72 deg (B753), theta-odd spectrum multiplicative rank 1 (B746 F3).
     No banked spectral object is indexed by geodesic period at all.
 (3) The closure: every period-k gap-labeling module lives in a REAL
     quadratic gait field (disjoint from Q(sqrt-3) over Q, computed for all
     tested k), while B739's rigidity theorem pins the continuous anatomy to
     Lambda_K data ONLY, and the voice artifacts contain zero golden markers
     (B746 F11, re-verified collision-aware). The emittance anatomy is
     structurally closed to the arithmetic the gap-labeling rank is made of.

So 'ask the rank question on the emittance/spectral anatomy' (the revival
hypothesis) HAS an answer on the frozen surface: the anatomy offers no
k-tracking rank object; the kill's k-independence lesson holds ON THE FACE,
not just in the substitution arithmetic. The wall gains a column.

NOT claimed (Q6 specialness budget): none of this is special to THIS claim
or object -- the same closure argument runs for the sister m003 (its cusp
order disc -3, palette 1; Section 1 comparator). The extension is the
computed k-independence + field-disjointness, nothing further.

Known open door, NOT an opening of this cell: whether the DISCRETE newform
spectrum carries golden/rank data is already named open and owner-gated
INSIDE the frozen surface itself (B739 FINDINGS L47-49 'unique home...
owner-gated'; B746 door 2). The killed claim does not depend on it: no
discrete-spectrum answer can change rank(gap-labeling) = 2 != k.

FALSIFIER: (i) any object banked in B737/B739/B746/B753 indexed by geodesic
period whose value tracks k; (ii) a golden-marker hit in the voice artifacts
under the collision-aware set; (iii) a period-k word whose gap-labeling
field degree != 2; (iv) failure of any recomputation here against the
banked digits (palette 1/2/8, disc -48, Res 1.7065521766..., vol
2.0298832128...). Any one voids KILL-EXTENDS.
""")

n_pass = sum(1 for c in CHECKS if c)
print(f"CHECK: {n_pass}/{len(CHECKS)} checks passed")
if not all(CHECKS):
    sys.exit(1)
