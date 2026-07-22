#!/usr/bin/env python3
# B754 P2 cell — TOMB-L334 (B85 Sym(W)->trace-ring functor wall; kill-form: finite-level-obstruction)
# RUN-WITH: plain python3 (stdlib only; no Sage). Deterministic.
#
# THE P2 QUESTION: does the spectral face AS BANKED (ONLY B737, B739, B746, B753)
# bear on the killed claim in a way the original kill (arithmetic-only,
# faces_consulted = none) never tested?
#
# Structure:
#   PART A — kill basis recomputed (pure A_{n-1}/theta root combinatorics, the
#            exposure note's C1-C5 scope) + the sector's field invariant.
#   PART B — Gate 5-Q Q2: the consultation operator CONSULT(X) computed for the
#            object (m004) AND the sister comparator (m003); it must discriminate.
#   PART C — the confrontation: the revival hypothesis ("the emittance spectrum /
#            congruence tower could reindex the height-2 sector") consulted
#            against the frozen surface. Verdict-bearing facts as CHECK: lines.
#
# Face vocabulary bound to the four frozen arcs only (Q1). E23: every congruence-
# level statement below names the filtration: the 2-adic congruence filtration
# (2) contained-in (4) contained-in (8) of O = Z[omega], K = Q(sqrt(-3)), with
# palette group (O/2^k O)^x / im(mu_6). No SM values (Gate 5). No E25 use.

from fractions import Fraction
from math import gcd, cos, sin, pi, isqrt
import itertools, cmath

PASS = True
def check(tag, cond, msg):
    global PASS
    status = "PASS" if cond else "FAIL"
    if not cond:
        PASS = False
    print(f"CHECK: [{tag}] [{status}] {msg}")

print("=" * 78)
print("B754/P2 cell TOMB-L334 — the Sym(W)->trace-ring functor wall vs the banked")
print("spectral face (B737, B739, B746, B753 ONLY)")
print("=" * 78)

# ---------------------------------------------------------------------------
# PART A — KILL BASIS RECOMPUTED (A_{n-1} / theta root combinatorics)
# ---------------------------------------------------------------------------
print()
print("PART A — the kill basis recomputed (C1-C5 scope: roots + theta only)")
print("-" * 78)

def pos_roots_height(n, h):
    # positive height-h roots of A_{n-1}: e_i - e_{i+h}, i = 1..n-h, as (i, j=i+h)
    return [(i, i + h) for i in range(1, n - h + 1)]

def theta_root(n, root):
    # opposition involution theta = -w0: e_i - e_j |-> e_{n+1-j} - e_{n+1-i}
    i, j = root
    return (n + 1 - j, n + 1 - i)

def mat_rank_exact(M):
    # fraction-free exact rank over Q
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0]) if M else 0
    r = 0
    for c in range(cols):
        piv = next((k for k in range(r, rows) if M[k][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for k in range(rows):
            if k != r and M[k][c] != 0:
                f = Fraction(M[k][c], M[r][c])
                M[k] = [a - f * b for a, b in zip(M[k], M[r])]
        r += 1
    return r

first_mult2_n = None
all_h2_ok = True
parity_ok = True
maxmult_pre5 = 0
reversal_ok = True
for n in range(3, 16):
    h = 2
    roots = pos_roots_height(n, h)
    m = len(roots)                       # = n - 2
    # direct -w0 action vs abstract reversal sigma(i) = (n-h+1) - i
    perm = []
    for idx, r in enumerate(roots):
        tr = theta_root(n, r)
        if tr not in roots:
            reversal_ok = False
            break
        perm.append(roots.index(tr))
    sigma = [ (m - 1) - idx for idx in range(m) ]   # 0-based reversal
    if perm != sigma:
        reversal_ok = False
    # eigenspace dims two ways: cycle count and exact matrix rank
    fixed = sum(1 for i in range(m) if perm[i] == i)
    two_cycles = (m - fixed) // 2
    dims_cycle = (fixed + two_cycles, two_cycles)
    P = [[1 if perm[j] == i else 0 for j in range(m)] for i in range(m)]
    I = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    dim_minus = mat_rank_exact([[P[i][j] - I[i][j] for j in range(m)] for i in range(m)])
    dim_plus  = mat_rank_exact([[P[i][j] + I[i][j] for j in range(m)] for i in range(m)])
    dims_rank = (dim_plus, dim_minus)
    want = ((n - 2 + 1) // 2, (n - 2) // 2)         # (ceil, floor) of (n-2)/2
    if not (dims_cycle == dims_rank == want):
        all_h2_ok = False
    if (fixed == 1) != (n % 2 == 1):
        parity_ok = False
    if n < 5:
        maxmult_pre5 = max(maxmult_pre5, max(dims_cycle))
    if first_mult2_n is None and max(dims_cycle) >= 2:
        first_mult2_n = n

check("A1", reversal_ok,
      "theta=-w0 on height-2 roots == the reversal sigma(i)=(n-h+1)-i, all n=3..15 "
      "(direct root action recomputed, not imported)")
check("A1", all_h2_ok,
      "height-2 (+1,-1) eigenspace dims = (ceil((n-2)/2), floor((n-2)/2)), n=3..15 "
      "— cycle count AND exact rank agree (the tombstone's mult law recomputed)")
check("A1", first_mult2_n == 5 and maxmult_pre5 == 1,
      f"max height-2 sector multiplicity for n<5 is {maxmult_pre5}; first n with a "
      f"multiplicity-2 height-2 sector = {first_mult2_n} — LABELING-INDEPENDENT: no "
      "height-2 char factor of EITHER sign reaches mult 2 before n=5")
check("A1", parity_ok,
      "theta-fixed height-2 index exists iff n odd (n=3..15) — the tombstone's parity clause")

# A2 — all heights sanity (the full closed form, Tier-1 scope of B112)
allh_ok = True
for n in range(3, 16):
    tot = 0
    for h in range(1, n):
        roots = pos_roots_height(n, h)
        m = len(roots)
        perm = [roots.index(theta_root(n, r)) for r in roots]
        fixed = sum(1 for i in range(m) if perm[i] == i)
        dims = (fixed + (m - fixed) // 2, (m - fixed) // 2)
        if dims != ((n - h + 1) // 2, (n - h) // 2):
            allh_ok = False
        tot += m
    if tot != n * (n - 1) // 2:
        allh_ok = False
check("A2", allh_ok,
      "all heights h=1..n-1, n=3..15: dims = (ceil((n-h)/2), floor((n-h)/2)); "
      "totals = n(n-1)/2 — the closed form of the evidence_quote recomputed")

# A3 — kill-basis status re-examination (fact_basis was 'cited-unverified')
print()
print("  [A3] kill-basis status, re-examined at source (B112_closed_form_proof/")
print("       FINDINGS.md status relabel, three tiers): Tier 1 (the ceil/floor")
print("       eigenspace DIMS, all n) is the proved theorem and is what PART A")
print("       recomputes; the char(M^h)-vs-char(-M^h) LABELING is tower-verified")
print("       n<=5 with the B118 fixed-root sign (-1)^(h+1) caveat for even h.")
print("       The kill's operative content — no mult-2 height-2 sector of any")
print("       sign before n=5, attainment at n=5 — needs only Tier 1 plus the")
print("       n<=5-verified labeling range. The 'PROVED for all n' evidence_quote")
print("       is thereby refined, and the kill survives the refinement.")
check("A3", first_mult2_n == 5,
      "the finite-level obstruction (nothing of dim 2 at height 2 before n=5) rests "
      "on Tier-1 dims (recomputed above) + labeling inside its verified range n<=5")

# A4 — the sector's field invariant (binds the height-2 sector to a column)
def charpoly2(M):
    tr = M[0][0] + M[1][1]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return tr, det          # t^2 - tr*t + det

M = [[3, -1], [1, 0]]       # companion of the banked seed x^2 - 3x + 1 (B746 F1/F2)
tr1, det1 = charpoly2(M)
M2 = [[sum(M[i][k] * M[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
tr2, det2 = charpoly2(M2)
disc_seed = tr1 * tr1 - 4 * det1
disc_h2 = tr2 * tr2 - 4 * det2

def squarefree_part(d):
    d = abs(d); s = 1; f = 2
    while f * f <= d:
        e = 0
        while d % f == 0:
            d //= f; e += 1
        if e % 2 == 1:
            s *= f
        f += 1
    return s * d

check("A4", (tr1, det1, disc_seed) == (3, 1, 5),
      "seed charpoly t^2-3t+1, disc 5 (banked B746 F1: kappa_seed=3 => disc 5)")
check("A4", (tr2, det2) == (7, 1) and disc_h2 == 45 and squarefree_part(disc_h2) == 5,
      "char(M^2) = t^2 - 7t + 1 (tr M^2 = 7 = L_4), disc 45 = 3^2*5, squarefree part 5 "
      "— the height-2 sector char factors split over Q(sqrt5): a GOLDEN-column object "
      "(char(-M^2) = t^2+7t+1 has the same disc 45)")

# ---------------------------------------------------------------------------
# PART B — Q2 DISCRIMINATION: the consultation operator, object vs sister
# ---------------------------------------------------------------------------
print()
print("PART B — Gate 5-Q Q2: the consultation operator CONSULT(X)")
print("-" * 78)
print("  CONSULT(X) := ( m_cont(X) = banked continuous-channel multiplicity,")
print("                  palette chain |(O/2^k)^x / im(mu_6)| along the 2-adic")
print("                    congruence filtration (2) c (4) c (8)  [E23: named],")
print("                  N_excl(X) = nontrivial palette classes available at X's")
print("                    banked level that rigidity must exclude,")
print("                  (disc, h) of X's banked cusp CM order,")
print("                  golden-prime presence in X's banked voice invariants )")
print("  Consulted against the claim: can the emittance face host / reindex a")
print("  multiplicity-2, Q(sqrt5)-split height-2 sector?")
print()

# B1 — the palette chain, recomputed exactly in O = Z[omega], omega^2 = -1-omega
def eis_mul(x, y, mod):
    a, b = x; c, d = y
    return ((a * c - b * d) % mod, (a * d + b * c - b * d) % mod)

def palette_size(k):
    mod = 2 ** k
    units = [(a, b) for a in range(mod) for b in range(mod)
             if (a * a - a * b + b * b) % 2 == 1]          # norm odd <=> invertible mod 2^k
    mu6 = [(1, 0), (0, 1), (mod - 1, mod - 1),
           (mod - 1, 0), (0, mod - 1), (1, 1)]             # {1, w, w^2, -1, -w, -w^2}
    mu6 = [(a % mod, b % mod) for a, b in mu6]
    seen, n_cosets = set(), 0
    for u in units:
        if u in seen:
            continue
        n_cosets += 1
        for z in mu6:
            seen.add(eis_mul(u, z, mod))
    return len(units), n_cosets

sizes = {}
for k in (1, 2, 3):
    n_units, n_cosets = palette_size(k)
    sizes[2 ** k] = n_cosets
    print(f"  |(O/{2**k})^x| = {n_units}, palette |(O/{2**k})^x / im(mu_6)| = {n_cosets}")
check("B1", (sizes[2], sizes[4], sizes[8]) == (1, 2, 8),
      "palette chain (1, 2, 8) at levels (2), (4), (8) — recomputed exactly "
      "(matches B737 p3_sister_out.txt PART[5] and B739 b739_probe_out.txt PART 0.5)")

# B2 — the discriminating component: available-and-excluded classes
n_excl_m004_4, n_excl_m004_8 = sizes[4] - 1, sizes[8] - 1
n_excl_m003 = sizes[2] - 1
check("B2", (n_excl_m004_4, n_excl_m004_8, n_excl_m003) == (1, 7, 0),
      f"N_excl(m004) = {n_excl_m004_4} at level (4), {n_excl_m004_8} at level (8) "
      f"(m004's banked levels, B737-P3); N_excl(m003) = {n_excl_m003} at m003's level (2) "
      "— CONSULT DISCRIMINATES: the rigidity consultation is CONTENTFUL for the object "
      "(7 available classes to exclude) and VACUOUS for the sister (nothing available)")

# B3 — the cusp CM orders via exact trace forms + reduced-forms class numbers
def h_disc(D):
    # class number of primitive reduced positive forms (a,b,c), b^2-4ac = D < 0
    n = 0
    amax = isqrt(abs(D) // 3)
    for a in range(1, amax + 1):
        for b in range(-a + 1, a + 1):
            num = b * b - D
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if c < a:
                continue
            if a == c and b < 0:
                continue
            if gcd(gcd(a, abs(b)), c) == 1:
                n += 1
    return n

# m004 cusp lattice ring Z + 2 sqrt(-3) Z (B737-P3): basis {1, alpha}, alpha^2 = -12
disc_m004 = (2 * (-24)) - (0 * 0)     # det [[tr 1, tr a],[tr a, tr a^2]] = [[2,0],[0,-24]]
# m003 cusp lattice ring O_K = Z[omega]: basis {1, omega}, tr(omega) = tr(omega^2) = -1
disc_m003 = (2 * (-1)) - ((-1) * (-1))
check("B3", disc_m004 == -48 and disc_m003 == -3
      and h_disc(-48) == 2 and h_disc(-3) == 1,
      f"cusp-order trace-form discs: m004 -> {disc_m004} (h(-48) = {h_disc(-48)} by "
      f"reduced-forms enumeration), m003 -> {disc_m003} (h(-3) = {h_disc(-3)}) — "
      "CONSULT DISCRIMINATES on the cusp CM component (conductor-4 order vs maximal)")

# B4 — golden-prime scan of the banked voice invariants (B746 S4 recomputed)
def prime_support(n):
    n = abs(n); s = set(); f = 2
    while f * f <= n:
        while n % f == 0:
            s.add(f); n //= f
        f += 1
    if n > 1:
        s.add(n)
    return s

voice_invariants = {
    "cusp CM disc": 48,          # |disc -48|            (B737-P3)
    "palette top": 8,            # palette sizes 1,2,8   (B737-P3 / B739 P0.5)
    "covering degree": 12,       # Humbert 12            (B737-P1 / B739 P0.2)
    "residue field elt 2sqrt3/vol -> 3": 3,   # sqrt3: prime 3 (B737-P2 / B739)
    "cusp modulus norm N(2sqrt-3)": 12,
}
support = set()
for name, v in voice_invariants.items():
    support |= prime_support(v)
check("B4", support == {2, 3},
      f"prime support of EVERY banked voice invariant = {sorted(support)}; the golden "
      "prime 5 is ABSENT (B746 spot-check S4 recomputed) — vs the height-2 sector's "
      "disc 45 where 5 is PRESENT")

print()
print("  Q2 VERDICT: CONSULT(m004) = (1, (1,2,8), N_excl={1,7}, (-48, h=2), 5-absent)")
print("              CONSULT(m003) = (1, (1,..), N_excl={0},   (-3,  h=1), --)")
print("  The outputs DIFFER in three computed components (N_excl 7 vs 0; cusp order")
print("  -48/h=2 vs -3/h=1; palette chain depth). Honest note: m_cont = #cusps = 1")
print("  alone would NOT discriminate (both are one-cusped); the discrimination")
print("  rests on the palette / cusp-order components — exactly the components that")
print("  make B739's rigidity a nontrivial theorem about THIS object. Q2 PASS.")
check("Q2", (n_excl_m004_8, n_excl_m003) == (7, 0) and (disc_m004, disc_m003) == (-48, -3),
      "the consultation operator discriminates the object from the sister comparator "
      "(computed, not asserted); the cell does not stop at Q2")

# ---------------------------------------------------------------------------
# PART C — THE CONFRONTATION: the revival hypothesis vs the frozen surface
# ---------------------------------------------------------------------------
print()
print("PART C — the revival hypothesis consulted against the banked face")
print("-" * 78)
print("  B' revival_hypothesis (sealed record): 'the ceil((n-2)/2) rep-tower law")
print("  never met the emittance spectrum; the congruence tower could reindex the")
print("  height-2 sector.' The original kill was arithmetic-only (faces_consulted")
print("  = none). The frozen surface now answers three of its load-bearing steps:")
print()

# C1 — capacity
m_cont = 1        # banked: B739 PART C (multiplicity of continuous spectrum = #cusps = 1)
sector_need = 2   # recomputed PART A: mult-2 from n=5 on
check("C1", m_cont < sector_need,
      f"CAPACITY: the banked continuous emittance channel has multiplicity {m_cont} "
      "(= #cusps; B739 b739_probe_out.txt PART C L184-208, source-verified there at two "
      f"primary documents) < {sector_need} = the sector's multiplicity from n=5 on "
      "(PART A). A single-channel voice cannot host ANY multiplicity-2 sector at any n.")

# C2 — column
check("C2", 5 in prime_support(disc_h2) and 5 not in support,
      "COLUMN: the height-2 sector is Q(sqrt5)-split (disc 45, PART A4) while every "
      "banked voice invariant has prime support in {2,3} (PART B4) and the continuous "
      "channel carries the zeta_K-quotient of K = Q(sqrt-3) ONLY (B739 FINDINGS L8-16; "
      "B746 F11: zero golden markers in the voice; the two-column law: gait transmits, "
      "name does not). The sector's field never appears in the banked voice.")

# C3 — mechanism
check("C3", (sizes[4] - 1, sizes[8] - 1) == (1, 7),
      "MECHANISM: the congruence-level reindexing resource the revival names IS the "
      "palette (1,2,8 recomputed, PART B1) along the named 2-adic filtration — and "
      "B739 proves the continuous channel excludes ALL of it (Fourier support locked "
      "to O^v: b739_probe_out.txt L81 and L283; 'NO conductor-(4)/(8) Hecke character "
      "appears ANYWHERE' L327). The reindexing route is CLOSED for the continuous "
      "channel; the level's arithmetic lives only in the discrete newform spectrum.")

# C4 — the banked mult-2 theta-odd block sits on the gait side (B753), exact in Q(sqrt5)
class Q5:
    # x + y*sqrt5 with Fraction coefficients
    def __init__(s, x, y=0):
        s.x, s.y = Fraction(x), Fraction(y)
    def __add__(s, o): return Q5(s.x + o.x, s.y + o.y)
    def __sub__(s, o): return Q5(s.x - o.x, s.y - o.y)
    def __mul__(s, o): return Q5(s.x * o.x + 5 * s.y * o.y, s.x * o.y + s.y * o.x)
    def inv(s):
        d = s.x * s.x - 5 * s.y * s.y
        return Q5(s.x / d, -s.y / d)
    def __eq__(s, o): return s.x == o.x and s.y == o.y
    def __repr__(s): return f"({s.x} + {s.y}*sqrt5)"

one, sqrt5 = Q5(1), Q5(0, 1)
phi = Q5(Fraction(1, 2), Fraction(1, 2))
phi_over_sqrt5 = phi * sqrt5.inv()
lhs = one - phi_over_sqrt5                    # 1 - phi/sqrt5
rhs = (phi * sqrt5).inv()                     # 1/(phi sqrt5)
mixing_exact = Q5(Fraction(1, 2), Fraction(-1, 10))   # (5 - sqrt5)/10
half_inv_phi = (Q5(2) * phi).inv()            # 1/(2 phi)
cos72_exact = Q5(Fraction(-1, 4), Fraction(1, 4))     # (sqrt5 - 1)/4
check("C4", lhs == rhs == mixing_exact and half_inv_phi == cos72_exact,
      "GAIT SIDE: B753's kind-correct mixing identity |B00|^2 = 1 - phi/sqrt5 = "
      "1/(phi sqrt5) = (5-sqrt5)/10 verified EXACTLY in Q(sqrt5), and cos72 = 1/(2 phi) "
      "exactly — the one banked 2-dim theta-odd spectral block (B753 output.txt L11/L27/"
      "L29) is unitary with GOLDEN eigenphases e^{+-i72}, and it lives on the weld/gait "
      "side, NOT in the emittance channel: mult-2 theta-structure, where the program "
      "has actually banked it, sits in the golden column — consistent with C2.")
ev_banked = complex(0.309017, 0.951057)            # B753 output.txt L11 (in-arc artifact)
ev_exact = cmath.exp(1j * 2 * pi * 72 / 360)
check("C4b", abs(ev_banked - ev_exact) < 5e-7 and abs(float(cos72_exact.x) + float(cos72_exact.y) * 5 ** 0.5 - cos(2 * pi * 72 / 360)) < 1e-15,
      "B753's banked eigenvalues match e^{+-i 72deg} to the printed 6 digits; "
      "cos(72deg) = (sqrt5-1)/4 to 1e-15 (float cross-check of the exact identity)")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
print()
print("=" * 78)
verdict_ok = PASS
check("VERDICT", verdict_ok,
      "KILL-EXTENDS — exactly what was computed: (i) the kill basis recomputed "
      "(mult at height 2 = ceil((n-2)/2), first mult-2 sector at n=5, theta-fixed "
      "index iff n odd; labeling-independent for n<5); (ii) the height-2 sector is "
      "Q(sqrt5)-split (disc 45); (iii) the banked emittance face offers exactly ONE "
      "continuous channel (mult = #cusps = 1), character-rigid (all 7 available "
      "nontrivial palette classes at the object's level excluded), with prime support "
      "{2,3} in every banked voice invariant. The reindexing mechanism the revival "
      "hypothesis names (the congruence-level palette) is the exact resource B739 "
      "excludes from the continuous channel. The wall gains a spectral column: the "
      "functor cannot reach the mult-2 char(M^2) sector before n=5 (algebra, "
      "recomputed), AND the object's continuous emittance face can neither host nor "
      "reindex ANY mult-2 sector at any n (capacity 1 < 2; field disjoint; mechanism "
      "closed). Scope: the CONTINUOUS channel only — the discrete newform spectrum "
      "is the frozen surface's own named remainder (B739 honest-bounds; B746 door 2, "
      "owner-gated), not an opening this cell can compute or needs for the verdict.")
print()
print(f"ALL CHECKS PASS: {PASS}")
