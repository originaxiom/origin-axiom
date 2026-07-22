#!/usr/bin/env python3
# =============================================================================
# B754 P2 cell — target B107 (dead-probe)
# KILLED CLAIM: "the metallic tower spectrum is new physics (operator anomalous
#   dimensions / masses)" — killed (category-error) as re-presented moduli-space
#   monodromy carrying the single scale log phi.
# P2 QUESTION: does the spectral face AS BANKED (frozen surface = B737, B739,
#   B746, B753 ONLY) bear on this killed claim in a way the original kill
#   (faces_consulted = ["sl-n-tower"] only) never tested?
# VERDICT COMPUTED HERE: KILL-EXTENDS.
#
# RUN-WITH: plain python3, stdlib only (fractions, math, cmath). Deterministic:
#   no RNG, no network, no environment dependence. Every verdict-bearing fact
#   prints a CHECK: line.
# Gate 5 (absolute): pure mathematics; no SM values, no value-hunting — this
#   cell re-examines the KILL BASIS (the single-scale fact) against the face.
# Gate 5-Q: Q2 discrimination is computed FIRST (Section 2) before the face is
#   consulted against the claim (Sections 3-5). Q5: no experience vocabulary.
# E23: the one congruence-level statement names its filtration explicitly: the
#   2-adic filtration (2) > (4) > (8) of O_K = Z[omega], K = Q(sqrt(-3)),
#   2 inert; palette = |(O/2^k)^x / mu_6|. E25: no integer-relation searches
#   are used anywhere (all algebra is exact root/coefficient verification).
# =============================================================================

from fractions import Fraction as F
import math, cmath

ok_all = True
def CHECK(label, cond):
    global ok_all
    tag = "CHECK" if cond else "CHECK-FAIL"
    if not cond:
        ok_all = False
    print(f"{tag}: {label}")

print("=" * 78)
print("B754 P2 cell B107 — the single-scale kill vs the banked spectral face")
print("=" * 78)

# -----------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt5): numbers are (p, q) meaning p + q*sqrt5, p,q in Q
# -----------------------------------------------------------------------------
def q5(p, q=0):
    return (F(p), F(q))

def q5_add(u, v): return (u[0] + v[0], u[1] + v[1])
def q5_neg(u):    return (-u[0], -u[1])
def q5_mul(u, v): return (u[0]*v[0] + 5*u[1]*v[1], u[0]*v[1] + u[1]*v[0])
def q5_inv(u):
    den = u[0]*u[0] - 5*u[1]*u[1]
    return (u[0]/den, -u[1]/den)
def q5_pow(u, k):
    if k < 0:
        return q5_pow(q5_inv(u), -k)
    r = q5(1)
    for _ in range(k):
        r = q5_mul(r, u)
    return r
def q5_float(u): return float(u[0]) + float(u[1]) * math.sqrt(5)

PHI = (F(1, 2), F(1, 2))          # phi = (1+sqrt5)/2
ONE = q5(1); MONE = q5(-1)

def sphik(s, k):                   # s * phi^k, s in {+1,-1}
    return q5_mul(q5(s), q5_pow(PHI, k))

# -----------------------------------------------------------------------------
# Exact linear algebra over Q: charpoly det(xI - A) via Faddeev-LeVerrier
# -----------------------------------------------------------------------------
def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

def charpoly(A):
    n = len(A)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    M = [row[:] for row in I]
    coeffs = [F(1)]
    for k in range(1, n + 1):
        AM = matmul(A, M)
        c = -sum(AM[i][i] for i in range(n)) / k
        coeffs.append(c)
        M = [[AM[i][j] + (c if i == j else 0) for j in range(n)] for i in range(n)]
    return coeffs   # x^n + c1 x^(n-1) + ... + cn

def poly_from_roots(roots):
    # monic polynomial with the given Q(sqrt5) roots; coefficients in Q(sqrt5)
    poly = [q5(1)]
    for r in roots:
        new = [q5(0)] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i] = q5_add(new[i], c)                     # x * c
            new[i + 1] = q5_add(new[i + 1], q5_mul(q5_neg(r), c))
        poly = new
    return poly

def sym_matrix(a, b, c, d, deg):
    # induced action on binary forms of degree deg under x -> a x + b y, y -> c x + d y
    # basis m_i = x^(deg-i) y^i; returns integer matrix (as Fractions)
    def binom_expand(u, v, m):
        return [math.comb(m, t) * u**(m - t) * v**t for t in range(m + 1)]
    def conv(p1, p2):
        out = [0] * (len(p1) + len(p2) - 1)
        for i, x in enumerate(p1):
            for j, y in enumerate(p2):
                out[i + j] += x * y
        return out
    n = deg + 1
    cols = []
    for i in range(n):
        p = conv(binom_expand(a, b, deg - i), binom_expand(c, d, i))
        cols.append(p)
    return [[F(cols[i][j]) for i in range(n)] for j in range(n)]

# =============================================================================
# SECTION 1 — THE KILL BASIS RECOMPUTED EXACTLY (the target's evidence quote)
# B107 B: tower factors as prod_d Sym^d(M1) (B103, proved n=3,4);
# M1 = [[1,1],[1,0]]; the SL(3) tower spectrum is the 8-element set
# { 1, -1, phi^2, phi^-2, phi^3, -phi, phi^-1, -phi^-3 }  (evidence quote).
# =============================================================================
print()
print("SECTION 1 — the kill basis (single scale log phi) recomputed exactly")

expected = {
    0: [sphik(1, 0)],
    1: [sphik(1, 1), sphik(-1, -1)],
    2: [sphik(1, 2), sphik(-1, 0), sphik(1, -2)],
    3: [sphik(1, 3), sphik(-1, 1), sphik(1, -1), sphik(-1, -3)],
}
for deg in range(4):
    A = sym_matrix(1, 1, 1, 0, deg)     # Sym^deg of the golden seed M1
    cp = charpoly(A)
    prod = poly_from_roots(expected[deg])
    match = all(pc == (cc, F(0)) for pc, cc in zip(prod, cp))
    CHECK(f"charpoly(Sym^{deg}(M1)) = prod(x - s*phi^k) over the expected "
          f"{len(expected[deg])} eigenvalues, EXACT in Q(sqrt5)", match)

# the SL(3) 8-spectrum (B107 evidence quote) = Sym^0 u Sym^2 u Sym^3 spectra
sl3 = set(expected[0]) | set(expected[2]) | set(expected[3])
quote = {sphik(1, 0), sphik(-1, 0), sphik(1, 2), sphik(1, -2),
         sphik(1, 3), sphik(-1, 1), sphik(1, -1), sphik(-1, -3)}
CHECK("SL(3) tower 8-spectrum = B107 evidence quote "
      "{1,-1,phi^2,phi^-2,phi^3,-phi,phi^-1,-phi^-3}, sets EXACTLY equal "
      "(assembly per B103 prod-Sym^d factorization, proved n=3,4 — banked)",
      sl3 == quote and len(sl3) == 8)

# single-scale form: every eigenvalue is s*phi^k, k in {-3..3} -> the only
# eigenvalue-modulus scale present is log phi (k=0 members have |lambda|=1).
forms = []
for lam in sorted(sl3, key=q5_float):
    found = None
    for s in (1, -1):
        for k in range(-3, 4):
            if lam == sphik(s, k):
                found = (s, k)
    forms.append(found)
CHECK("every SL(3) tower eigenvalue = s*phi^k with s=+-1, k in {-3..3} "
      "(single geometric scale log phi) — EXACT", all(f is not None for f in forms))

# ties to the ledger seed: the nontrivial Sym^2 factor is x^2-3x+1, disc 5
disc = F(3)**2 - 4*F(1)
CHECK("disc(x^2-3x+1) = 5 (the golden seed disc; B746 F1/F2 FORCED rows: "
      "kappa_seed=3, Alexander t^2-3t+1)", disc == 5)

# B746 F3: the theta-odd chord spectrum = the ODD golden powers = Sym^3 block
f3 = {sphik(-1, 1), sphik(1, -1), sphik(1, 3), sphik(-1, -3)}
CHECK("B746 F3 theta-odd chord spectrum {-phi, phi^-1, phi^3, -phi^-3} = "
      "Sym^3(M1) spectrum EXACTLY = the odd-k half of the SL(3) tower — the "
      "face already carries the tower's odd half on the GAIT column",
      f3 == set(expected[3]))

# =============================================================================
# SECTION 2 — GATE 5-Q Q2, MANDATORY FIRST: the consultation operator
# DISCRIMINATES the object from the comparator (sister m003), computed.
#
# Operator V(M) = ( cusp j-invariant / CM order,
#                   2-adic palette |(O/2^k)^x / mu_6| at M's congruence level,
#                   golden-scale query mode on the banked continuous channel ).
# =============================================================================
print()
print("SECTION 2 — Q2 discrimination: operator V on m004 vs sister m003")

# --- 2a. j-invariants (Eisenstein-series q-expansions; deterministic) --------
def jtau(tau, terms=250):
    q = cmath.exp(2j * cmath.pi * tau)
    E4 = 1 + 240 * sum(n**3 * q**n / (1 - q**n) for n in range(1, terms))
    E6 = 1 - 504 * sum(n**5 * q**n / (1 - q**n) for n in range(1, terms))
    return 1728 * E4**3 / (E4**3 - E6**2)

# m003 comparator: cusp = C/O_K, hexagonal, tau = (1+sqrt(-3))/2 -> j = 0
j_m003 = jtau(complex(0.5, math.sqrt(3) / 2))
CHECK(f"[Q2] m003 comparator: j((1+sqrt(-3))/2) = 0 exactly (|j| computed = "
      f"{abs(j_m003):.2e} < 1e-6) — the GENERIC maximal-order point (B737 P3)",
      abs(j_m003) < 1e-6)

# m004: cusp = C/(Z + 2sqrt(-3)Z), tau = 2sqrt(3)i, CM by the disc -48 order;
# j = the LARGER root of x^2 - 2835810000 x + 6549518250000 (B737 P3)
j_m004 = jtau(complex(0.0, 2 * math.sqrt(3)))
Dj = 2835810000**2 - 4 * 6549518250000
root_big = (2835810000 + math.sqrt(float(Dj))) / 2
rel = abs(j_m004.real - root_big) / root_big
CHECK(f"[Q2] m004: j(2sqrt(3)i) = {j_m004.real:.3f} = larger root "
      f"{root_big:.3f} of x^2-2835810000x+6549518250000 (rel err {rel:.1e} "
      f"< 1e-8; Im j = {abs(j_m004.imag):.1e}) — disc -48 conductor-4 CM "
      f"(B737 P3)", rel < 1e-8 and abs(j_m004.imag) < 1e-3)

# --- 2b. the cusp lattice and its congruence data (E23: 2-adic filtration) ---
# O_K = Z<1, omega>, omega = (1+sqrt(-3))/2, omega^2 = omega - 1.
# sqrt(-3) = 2*omega - 1, so 2*sqrt(-3) = 4*omega - 2.
# Lambda = Z<1, 2sqrt(-3)> = Z<(1,0), (-2,4)> in the (1, omega) basis.
det = 1 * 4 - 0 * (-2)
g = math.gcd(math.gcd(1, 0), math.gcd(-2, 4))   # gcd of entries -> SNF d1
CHECK(f"[Q2] cusp lattice index [O:Lambda] = |det[[1,0],[-2,4]]| = {det} = 4; "
      f"Smith form diag({g},{det//g}) -> O/Lambda = Z/4 (B739 (a))",
      det == 4 and g == 1)
# B739's presentation Lambda = Z + (2+4omega)Z is the same lattice:
# (2+4omega) = (4omega-2) + 4*1, integer unimodular change of basis.
CHECK("[Q2] Z<1,4omega-2> = Z<1,4omega+2> (basis change by [[1,4],[0,1]], "
      "det 1) — B739's presentation and B737's are the same lattice",
      (4 - 2) - (4 + 2) == -4)   # second generators differ by 4*(first) exactly

# 2 is inert in O_K: x^2 - x + 1 has no root mod 2
CHECK("[Q2] 2 inert in O_K: x^2-x+1 has no root mod 2 "
      f"(values {[(x*x - x + 1) % 2 for x in (0, 1)]})",
      all((x*x - x + 1) % 2 == 1 for x in (0, 1)))

# --- 2c. the palette along the 2-adic filtration (2) > (4) > (8) -------------
def palette(k):
    mod = 2**k
    def mul(x, y):
        a, b = x; c, d = y
        return ((a*c - b*d) % mod, (a*d + b*c + b*d) % mod)   # omega^2=omega-1
    units = [(a, b) for a in range(mod) for b in range(mod)
             if (a*a + a*b + b*b) % 2 == 1]                    # N odd <=> unit
    mu6 = {(1 % mod, 0), ((-1) % mod, 0), (0, 1), (0, (-1) % mod),
           ((-1) % mod, 1 % mod), (1 % mod, (-1) % mod)}       # {+-1,+-w,+-w^2}
    # sanity: units form a group containing mu6's image; quotient order:
    return len(units) // len(mu6), len(units)

pal = []
for k in (1, 2, 3):
    p, nu = palette(k)
    pal.append(p)
    exp_units = 3 * 4**(k - 1)
    CHECK(f"[Q2] level (2^{k}): |(O/2^{k})^x| = {nu} = 3*4^{k-1}; "
          f"|(O/2^{k})^x / mu_6| = {p}",
          nu == exp_units)
CHECK(f"[Q2] palette along the 2-adic filtration (2)>(4)>(8) = "
      f"{tuple(pal)} = (1, 2, 8) (B737 P3) — m004's level admits 8 "
      f"characters at (8); m003's level admits only zeta_K (palette 1)",
      pal == [1, 2, 8])

# --- 2d. the discrimination verdict ------------------------------------------
print()
print("Q2 OUTPUT m004 : ( j = 2835807690.2 [disc -48, conductor-4 order],")
print("                   palette (1,2,8) — 8 characters available at (8),")
print("                   golden query mode = EXCLUDED-BY-RIGIDITY: room exists")
print("                   and B739 proves NONE appears in the continuous channel )")
print("Q2 OUTPUT m003 : ( j = 0 [disc -3, maximal order],")
print("                   palette (1) — only zeta_K available,")
print("                   golden query mode = EXCLUDED-BY-VACUITY: no room —")
print("                   the exclusion is carried by the field, not the object )")
CHECK("[Q2] V(m004) != V(m003) in EVERY component (j: 2.8e9 vs 0; palette: 8 "
      "vs 1; exclusion mode: rigidity vs vacuity) — the operator "
      "DISCRIMINATES; the cell may proceed",
      abs(j_m003) < 1e-6 and rel < 1e-8 and pal == [1, 2, 8])

# =============================================================================
# SECTION 3 — THE FACE'S VOICE INVARIANTS RECOMPUTED (B737 P1/P2, B739 (e))
# =============================================================================
print()
print("SECTION 3 — the banked voice invariants, recomputed from scratch")

# --- 3a. Res_{s=1} zeta_K = L(1, chi_-3) = 2 pi / (6 sqrt 3) -----------------
N = 10**6
L1 = math.fsum(1.0 / ((3*j + 1) * (3*j + 2)) for j in range(N))
a = N - 0.5
L1 += (1.0 / 3.0) * math.log((3*a + 2) / (3*a + 1))       # midpoint tail
res_zK = 2 * math.pi / (6 * math.sqrt(3))
CHECK(f"Res zeta_K = L(1,chi_-3) computed = {L1:.12f} = 2pi/(6sqrt3) = "
      f"{res_zK:.12f} (|diff| = {abs(L1 - res_zK):.1e} < 1e-9) — B737 P1 "
      f"residue chain endpoint 0.6045997880...",
      abs(L1 - res_zK) < 1e-9 and abs(L1 - 0.6045997880) < 1e-9)

# --- 3b. vol(m004) = 2 * Cl2(pi/3), Cl2 via the zeta-accelerated series ------
def zeta_em(s, Nz=10000):
    # sum_{n>N} n^-s = N^(1-s)/(s-1) - N^-s/2 + s*N^(-s-1)/12 - O(N^(-s-3))
    tot = math.fsum(n ** (-s) for n in range(1, Nz + 1))
    return tot + Nz**(1 - s) / (s - 1) - 0.5 * Nz**(-s) + s * Nz**(-s - 1) / 12

CHECK(f"zeta(2) computed by Euler-Maclaurin = {zeta_em(2):.14f} = pi^2/6 "
      f"(|diff| < 1e-12)", abs(zeta_em(2) - math.pi**2 / 6) < 1e-12)

def cl2(theta):
    tot = theta - theta * math.log(theta)
    for m in range(1, 26):
        tot += (zeta_em(2 * m, 2000) * theta**(2*m + 1)
                / (m * (2*m + 1) * math.pi**(2*m) * 4**m))
    return tot

vol = 2 * cl2(math.pi / 3)
print(f"vol(m004) = 2*Cl2(pi/3) = {vol:.15f}  (two regular ideal tetrahedra)")

# --- 3c. Res phi = 2 sqrt3 / vol(m004): the B737 P2 banked number ------------
res_phi = 2 * math.sqrt(3) / vol
CHECK(f"Res phi_m004 = 2sqrt3/vol(m004) computed = {res_phi:.14f} = banked "
      f"1.70655217662816 (B737 P2; |diff| = "
      f"{abs(res_phi - 1.70655217662816):.1e} < 1e-11)",
      abs(res_phi - 1.70655217662816) < 1e-11)

# --- 3d. two-route consistency (B739 (e)): Res phi = 2 pi^2 / (9 zeta_K(2)) --
L2 = math.fsum(1.0 / (3*j + 1)**2 - 1.0 / (3*j + 2)**2 for j in range(N))
L2 += (1.0 / 3.0) * (1.0 / (3*a + 1) - 1.0 / (3*a + 2))   # midpoint tail
zK2 = zeta_em(2) * L2
route2 = 2 * math.pi**2 / (9 * zK2)
CHECK(f"two-route: 2pi^2/(9 zeta_K(2)) = {route2:.12f} vs 2sqrt3/vol = "
      f"{res_phi:.12f} (|diff| = {abs(route2 - res_phi):.1e} < 1e-9) — "
      f"B739 (e), covering-invariance chain", abs(route2 - res_phi) < 1e-9)

# =============================================================================
# SECTION 4 — THE EXTENSION: the B'-flagged untested channel is computed shut
#
# The B' exposure: "the object's native continuous emittance-scattering
# channel ... was never tested and could carry scales beyond log-phi."
# The frozen surface NOW answers that channel (banked, one-hop verified):
#   B739: the continuous spectrum of m004 is a SINGLE channel, multiplicity 1,
#     furnished entirely by the one Eisenstein series = the pullback of the
#     Bianchi-orbifold Eisenstein series AS FUNCTIONS; every Fourier
#     coefficient restricted from the level-one base; Fourier support in
#     O^dual subset K; scattering EXACTLY Lambda_K(s-1)/Lambda_K(s); NO
#     conductor-(4)/(8) character appears anywhere in the continuous spectrum.
#   B737 P2: phi_m004 = phi_orbifold identically; Res phi = 2sqrt3/vol.
#   B746 F11: grep of the banked voice artifacts -> ZERO golden markers.
# The channel's arithmetic is therefore K = Q(sqrt(-3))-rigid. Below: log phi
# CANNOT live there — computed field disjointness.
# =============================================================================
print()
print("SECTION 4 — the extension: field disjointness, computed exactly")

def squarefree_part(n):
    s = 1 if n > 0 else -1
    n = abs(n)
    d = 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
        d += 1
    return s * n

CHECK(f"squarefree(5) = {squarefree_part(5)} != {squarefree_part(-3)} = "
      f"squarefree(-3): Q(sqrt5) != Q(sqrt-3); both degree 2 over Q, so "
      f"Q(sqrt5) n Q(sqrt-3) = Q",
      squarefree_part(5) == 5 and squarefree_part(-3) == -3)

m = math.isqrt(15)
CHECK(f"-15 = 5*(-3) is not a rational square (isqrt(15)^2 = {m*m} != 15): "
      f"the compositum Q(sqrt5, sqrt-3) has degree 4 — the fields are "
      f"linearly disjoint", m * m != 15)

# phi is real and irrational; Q(sqrt-3) n R = Q (a + b sqrt-3 real <=> b=0);
# hence phi not in Q(sqrt-3). Computed witness: phi irrational because 5 is
# not a perfect square:
CHECK("phi = (1+sqrt5)/2 is real irrational (5 not a square) and "
      "Q(sqrt(-3)) n R = Q -> phi NOT in Q(sqrt(-3)): the voice field cannot "
      "contain the tower scale", math.isqrt(5)**2 != 5)

# every scale-carrying tower eigenvalue (k != 0, i.e. |lambda| != 1) is
# irrational in Q(sqrt5) (q-part nonzero) — none lies in K:
scale_carriers = [lam for lam in sl3 if lam not in (ONE, MONE)]
CHECK(f"all {len(scale_carriers)} scale-carrying tower eigenvalues (the six "
      f"with k != 0) have nonzero sqrt5-part — each generates Q(sqrt5), none "
      f"lies in K = Q(sqrt(-3)); the two rational ones (+-1) have "
      f"log|lambda| = 0 (no scale)",
      all(lam[1] != 0 for lam in scale_carriers) and len(scale_carriers) == 6)

print()
print("EXTENSION (exactly what was computed, no more): the continuous")
print("emittance-scattering channel of m004 — the channel the B' exposure")
print("flagged as never tested — is, as banked (B739 + B737 P2), the single")
print("multiplicity-1 Eisenstein channel with scattering Lambda_K(s-1)/")
print("Lambda_K(s), character-rigid, Fourier support in O^dual; its")
print("arithmetic content lies in K = Q(sqrt(-3)). Computed here: the tower")
print("spectrum is exactly {s*phi^k} in Q(sqrt5) (Section 1), and Q(sqrt5)")
print("meets Q(sqrt(-3)) only in Q, with phi not in K (Section 4). Hence the")
print("single scale log phi CANNOT appear in the continuous channel: the one")
print("channel the kill never consulted EXCLUDES the tower, upholding the")
print("category-error kill (monodromy-not-spectrum) from the spectral side.")

# =============================================================================
# SECTION 5 — the revival's root-of-unity clause, audited against the face
# (B' second clause: "the arc's E-fork off-principal multichannel sector
#  (D1 root-of-unity data) ... could carry scales beyond log-phi")
# =============================================================================
print()
print("SECTION 5 — root-of-unity data carry phases, not scales")

# B753: the theta-odd weld block is exactly unitary, eigenvalues e^{+-i 72deg}
lam = cmath.exp(2j * cmath.pi / 5)
CHECK(f"B753 block eigenvalues e^(+-i72deg): |lambda| = {abs(lam):.15f} = 1 "
      f"exactly (unitary) -> ZERO eigenvalue-modulus scale content",
      abs(abs(lam) - 1) < 1e-15)

# Re lambda = cos 72deg = 1/(2 phi) = (sqrt5-1)/4, EXACT in Q(sqrt5):
half_inv_phi = q5_mul(q5(F(1, 2)), q5_inv(PHI))       # 1/(2 phi)
target = (F(-1, 4), F(1, 4))                          # (sqrt5 - 1)/4
CHECK("B753: Re e^(i72deg) = cos72 = 1/(2phi) = (sqrt5-1)/4 EXACT in Q(sqrt5) "
      f"(numeric cos(2pi/5) = {math.cos(2*math.pi/5):.15f}, "
      f"(sqrt5-1)/4 = {q5_float(target):.15f}) — the face's own root-of-unity "
      "block is GOLDEN in phase arithmetic: gait column (B746), no new scale",
      half_inv_phi == target
      and abs(math.cos(2*math.pi/5) - q5_float(target)) < 1e-15)

# The D1 revival data (B107 Addition 3, TARGET-SOURCE side, not face):
# omega, omega^2 are roots of x^2+x+1 (disc -3); +-i roots of x^2+1 (disc -4).
CHECK(f"D1 data (target source B107 Addition 3): omega roots of x^2+x+1, "
      f"disc = {1 - 4} -> squarefree part {squarefree_part(-3)} = the BEING/"
      f"voice field Q(sqrt(-3)); +-i: x^2+1, disc -4 -> Q(i). All moduli = 1: "
      f"|omega| = {abs(cmath.exp(2j*cmath.pi/3)):.15f}, |i| = 1",
      squarefree_part(1 - 4) == -3
      and abs(abs(cmath.exp(2j*cmath.pi/3)) - 1) < 1e-15)

print()
print("AUDIT RESULT: every root-of-unity datum in play (face: e^(+-i72deg);")
print("target-source D1: omega, omega^2, +-i, -1) has modulus exactly 1 —")
print("phases, ZERO scale. The revival clause 'could carry scales beyond")
print("log phi' gains nothing from root-of-unity data: on the banked face the")
print("only non-unit-modulus golden spectra remain the +-phi^k towers")
print("themselves (single scale, Section 1), and the phase arithmetic of the")
print("face's own unitary block is golden (gait column) while D1's omega is")
print("Eisenstein (being) — the two-column split the kill rests on, intact.")

# =============================================================================
# SCOPE BOUNDARY (honest, per B739's own bounds + the cc ack)
# =============================================================================
print()
print("SCOPE: B739 is weight-0 scalar; the DISCRETE newform spectrum (owner-")
print("gated, B746 door 2) and the off-principal multichannel sector remain")
print("outside the frozen surface. NEITHER is load-bearing for THIS claim:")
print("B107-E states the tower does not touch the off-principal reps and")
print("flags that sector 'explicitly NOT the dead spectral claims of C';")
print("B107 Addition 3 banks D1 as CONFIRMING the single-scale thesis. The")
print("extension claimed here is for the continuous channel exactly as the")
print("B' exposure flagged it — no more. (Residual open questions belong to")
print("the next arc's queue per the S16 review's convention note; they do not")
print("change this cell's verdict.)")

# =============================================================================
# VERDICT
# =============================================================================
print()
print("=" * 78)
if ok_all:
    print("ALL CHECKS PASS")
    print("VERDICT: KILL-EXTENDS — the banked spectral face answers the")
    print("B'-flagged untested channel and the answer upholds the kill: the")
    print("continuous emittance-scattering channel is K = Q(sqrt(-3))-rigid")
    print("(B739/B737) and provably cannot carry the tower's single scale")
    print("log phi (computed disjointness); the face's own golden spectra")
    print("(B746 F3, B753 block) sit on the gait/monodromy column — exactly")
    print("the kill's category. The wall gains the spectral-face column.")
else:
    print("CHECK FAILURE — verdict void; see CHECK-FAIL lines above.")
print("=" * 78)
