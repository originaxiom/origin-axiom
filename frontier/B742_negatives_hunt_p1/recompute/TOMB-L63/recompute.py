#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B739 Stage-B recompute — TOMB-L63 (speculations/TOMBSTONES.md:L63)

BANKED KILL (umbrella, Chat-2 "Standard-theory-kills"): five quantum-tower /
knot-invariant observations "are the ambient theory's definitions doing the
work, mistaken for framework-specific bridges."  kill_form = category-error;
fact_basis = asserted (umbrella carries no computation of its own).

THE DISCRIMINATING FACT (E19, identified before computing):
  Each of the five member observations is derivable from AMBIENT quantum-
  topology definitions alone (unitarity; finite-order level-k modular images;
  the known 4_1 volume conjecture; divisibility arithmetic of the level-k
  phase lattice; the standard semiclassical asymptotics), with ZERO
  framework-specific input, AND the same phenomena hold for non-framework
  objects.  If true, the "framework-specific bridge" reading is a category
  error and the kill stands.  Negation direction (kill fails): some member
  phenomenon actually discriminates the framework object (golden / metallic
  monodromy) from generic ambient objects.

DECLARED CONVENTIONS (E1 — the original arc "Chat-2" left these implicit):
  C1. "Quantum tower" operator := the SU(2)_k Reshetikhin-Turaev / WZW torus
      representation of SL(2,Z), dim k+1:
        S_ab = sqrt(2/(k+2)) sin(pi (a+1)(b+1)/(k+2)),  a,b = 0..k
        T_ab = delta_ab exp(2 pi i (h_a - c/24)),
        h_a = a(a+2)/(4(k+2)),  c = 3k/(k+2)
      (the ambient Chern-Simons quantization; nothing framework-specific).
  C2. Figure-eight (the golden m=1 seed of TOMBSTONES' metallic family) :=
      the once-punctured-torus bundle with monodromy
        M = R L = [[2,1],[1,1]],  R=[[1,1],[0,1]]=T,  L=[[1,0],[1,1]]=S T^-1 S^-1
      so the quantum monodromy is  U_k = T_q S_q T_q^-1 S_q^-1  (projective
      phase irrelevant to |lambda| and only shifts all eigenphases equally).
      Classical eigenvalues phi^{+-2}, phi the golden ratio (tombstone's
      "|lambda| = phi^k" with k=2).
  C3. Kashaev convention — taken from the ONE-HOP citation the member-3 kill
      leans on (S027 SCOPE block, speculations/S027_metallic_quantum_modularity.md):
        J_N(4_1) = sum_{j=0}^{N-1} |(q)_j|^2,  q = e^{2 pi i/N},
        (2 pi/N) log J_N(4_1) -> vol(4_1) = 2.0299  (monotone, from above)
      vol(4_1) recomputed here two independent ambient ways:
        (a) 2 * Im Li_2(e^{i pi/3})   (Bloch-Wigner of the tetrahedron shape)
        (b) 6 * Lobachevsky(pi/3),  Lob(t) = -int_0^t log|2 sin u| du
  C4. z0 := e^{i pi/3} = (1+i sqrt3)/2, the regular-ideal-tetrahedron shape
      parameter of 4_1 (root of z^2 - z + 1); arg z0 = pi/3.  "Phases at
      level k" is read THREE declared ways (the arc did not fix one):
        (a) the lattice UNIT 2 pi/(k+2);  (b) membership of pi/3 in the
        lattice { m pi/(k+2) };  (c) the actual eigenphases of U_k.
  C5. Root-of-unity detection: rational reconstruction of eigenphase/(2 pi)
      with denominator <= 20000, then exact-power verification
      |lambda^q - 1| < 1e-18 at working precision dps = 40.
  C6. Determinism: no wall-clock, no randomness anywhere.  The "generic
      unitary" control is U = expm(i H), H_jk = 1/(1+j+k) (fixed Hilbert
      matrix), dimension 6.

GATE 5: every quantity below is mathematics (matrices over cyclotomic fields,
hyperbolic volume, divisibility).  No SM quantities.
"""

from fractions import Fraction
import mpmath as mp

mp.mp.dps = 40
PI = mp.pi
TOL = mp.mpf(10) ** (-18)

LINE = "-" * 78


def su2k_modular_data(k):
    """Ambient SU(2)_k torus modular data (C1)."""
    K = k + 2
    dim = k + 1
    S = mp.matrix(dim, dim)
    for a in range(dim):
        for b in range(dim):
            S[a, b] = mp.sqrt(mp.mpf(2) / K) * mp.sin(PI * (a + 1) * (b + 1) / K)
    c = mp.mpf(3) * k / K
    T = mp.matrix(dim, dim)
    for a in range(dim):
        h_a = mp.mpf(a) * (a + 2) / (4 * K)
        T[a, a] = mp.e ** (2j * PI * (h_a - c / 24))
    return S, T


def herm_conj(A):
    n, m = A.rows, A.cols
    B = mp.matrix(m, n)
    for i in range(n):
        for j in range(m):
            B[j, i] = mp.conj(A[i, j])
    return B


def unitarity_defect(A):
    n = A.rows
    D = A * herm_conj(A)
    return max(abs(D[i, j] - (1 if i == j else 0)) for i in range(n) for j in range(n))


def eigvals(A):
    return mp.eig(A, left=False, right=False)


def quantum_monodromy(k, word):
    """rho_k(word) with word a string over {'R','L'} (C2)."""
    S, T = su2k_modular_data(k)
    Sinv = herm_conj(S)   # S unitary
    Tinv = herm_conj(T)
    R_q = T
    L_q = S * Tinv * Sinv
    U = mp.eye(k + 1)
    for ch in word:
        U = U * (R_q if ch == "R" else L_q)
    return U


def root_of_unity_order(lam, maxden=20000):
    """C5: return q if lam is verified as a primitive q-th root of unity, else None."""
    ph = mp.arg(lam) / (2 * PI)          # in (-1/2, 1/2]
    fr = Fraction(float(ph)).limit_denominator(maxden)
    q = fr.denominator
    if abs(lam ** q - 1) < TOL:
        return q
    return None


def kashaev_J(N):
    """C3: J_N(4_1) = sum_{j=0}^{N-1} |(q)_j|^2, q = e^{2 pi i/N}."""
    q = mp.e ** (2j * PI / N)
    total = mp.mpf(1)          # j = 0 term: empty product = 1
    prod = mp.mpf(1)
    for m_ in range(1, N):
        prod *= abs(1 - q ** m_) ** 2
        total += prod
    return total


print("TOMB-L63 recompute — umbrella 'Standard-theory-kills' (five members)")
print("Discriminating fact: all five observations derive from AMBIENT definitions")
print("alone and hold for non-framework objects (=> 'bridge' reading = category error).")
print(LINE)

# ---------------------------------------------------------------- MEMBER 1
print("MEMBER 1: quantum |lambda| = 1 is UNITARITY; classical |lambda| = phi^2 != 1")
# classical side, exact
phi = (1 + mp.sqrt(5)) / 2
Mcl = mp.matrix([[2, 1], [1, 1]])
lam_cl = eigvals(Mcl)
lam_cl_abs = sorted(abs(x) for x in lam_cl)
print(f"  classical M = RL = [[2,1],[1,1]]  eigenvalue moduli = "
      f"{[mp.nstr(x, 12) for x in lam_cl_abs]}")
print(f"  phi^2  = {mp.nstr(phi**2, 12)}   phi^-2 = {mp.nstr(phi**-2, 12)}")
match_phi = max(abs(lam_cl_abs[1] - phi ** 2), abs(lam_cl_abs[0] - phi ** -2))
print(f"  |moduli - phi^{{+-2}}| = {mp.nstr(match_phi, 3)}  (tombstone's phi^k, k=2)")
# symplectic but not unitary
J2 = mp.matrix([[0, 1], [-1, 0]])
sympl = max(abs((Mcl * J2 * Mcl.T)[i, j] - J2[i, j]) for i in range(2) for j in range(2))
notU = max(abs((Mcl * Mcl.T)[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
print(f"  M J M^T = J defect {mp.nstr(sympl, 3)} (symplectomorphism: YES);"
      f"  M M^T - I max = {mp.nstr(notU, 3)} (unitary: NO)")
# quantum side
print("  quantum U_k = rho_k(RL) (C1/C2):  k : unitarity defect | max ||lam|-1|")
m1_max = mp.mpf(0)
U_by_k = {}
for k in range(1, 9):
    U = quantum_monodromy(k, "RL")
    U_by_k[k] = U
    ud = unitarity_defect(U)
    dev = max(abs(abs(l) - 1) for l in eigvals(U))
    m1_max = max(m1_max, dev)
    print(f"    k={k}:  {mp.nstr(ud, 3)}  |  {mp.nstr(dev, 3)}")
# genericity controls (kill-fails direction): non-framework objects
W = quantum_monodromy(4, "RLL")          # sister monodromy RL^2 (trace 4, not metallic m=1)
devW = max(abs(abs(l) - 1) for l in eigvals(W))
H = mp.matrix(6, 6)
for i in range(6):
    for j in range(6):
        H[i, j] = mp.mpf(1) / (1 + i + j)
G = mp.expm(1j * H)                       # generic deterministic unitary (C6)
devG = max(abs(abs(l) - 1) for l in eigvals(G))
print(f"  controls: sister RL^2 at k=4 max ||lam|-1| = {mp.nstr(devW, 3)};"
      f"  generic expm(iH) = {mp.nstr(devG, 3)}")
m1_ok = m1_max < TOL and devW < TOL and devG < TOL and match_phi < mp.mpf(10) ** -30
print(f"  => |lambda|=1 is a property of EVERY unitary (ambient), classical phi^2"
      f"  is the non-unitary symplectic side.  MEMBER 1 AMBIENT: {m1_ok}")
print(LINE)

# ---------------------------------------------------------------- MEMBER 2
print("MEMBER 2: finite-k eigenvalues are roots of unity (ambient finite image)")
m2_ok = True
orders_by_k = {}
for k in range(1, 9):
    lams = eigvals(U_by_k[k])
    orders = []
    for l in lams:
        q = root_of_unity_order(l)
        if q is None:
            m2_ok = False
            orders.append("FAIL")
        else:
            orders.append(q)
    orders_by_k[k] = orders
    print(f"    k={k}: eigenvalue orders (lam^q = 1 verified to {mp.nstr(TOL,2)}): {orders}")
# sister object: same ambient mechanism, no framework input
lamsW = eigvals(W)
ordW = [root_of_unity_order(l) for l in lamsW]
print(f"    sister RL^2, k=4: orders {ordW}")
# precision finding on the banked WORDING: 'defined over q => roots of unity by
# construction' is NOT the operative mechanism -- counterexamples both ways:
lam_top = max(lam_cl, key=lambda x: abs(x))
q_cl = root_of_unity_order(lam_top)
lamsG = eigvals(G)
ordG = [root_of_unity_order(l) for l in lamsG]
print(f"    counterexample A: classical M has entries in Z subset Z[zeta_6], yet")
print(f"      eigenvalue phi^2 root-of-unity order = {q_cl}  (None = not a root of unity)")
print(f"    counterexample B: generic UNITARY expm(iH): orders {ordG}")
print("      -> unitarity alone does not give roots of unity either; the ambient")
print("         mechanism is the FINITE IMAGE of the level-k SL(2,Z) representation")
print("         (congruence-subgroup property) -- still ambient, zero framework input.")
m2_ok = m2_ok and all(o is not None for o in ordW) and q_cl is None and all(o is None for o in ordG)
print(f"  MEMBER 2 AMBIENT (with wording refined, kill unchanged): {m2_ok}")
print(LINE)

# ---------------------------------------------------------------- MEMBER 3
print("MEMBER 3: Kashaev -> volume is the KNOWN volume conjecture for 4_1")
V_bw = 2 * mp.im(mp.polylog(2, mp.e ** (1j * PI / 3)))
lob = -mp.quad(lambda t: mp.log(abs(2 * mp.sin(t))), [0, PI / 3])
V_lob = 6 * lob
print(f"  vol(4_1) ambient (a) 2 Im Li2(z0)   = {mp.nstr(V_bw, 25)}")
print(f"  vol(4_1) ambient (b) 6 Lob(pi/3)    = {mp.nstr(V_lob, 25)}")
print(f"  |(a)-(b)| = {mp.nstr(abs(V_bw - V_lob), 3)}")
print("  Kashaev sum per S027's declared convention (one-hop citation):")
Ns = [100, 200, 400, 800, 1600]
vN = {}
dN = {}
for N in Ns:
    JN = kashaev_J(N)
    vN[N] = 2 * PI * mp.log(JN) / N
    dN[N] = 2 * PI * (mp.log(JN) - mp.mpf(3) / 2 * mp.log(N)) / N
    print(f"    N={N:5d}:  (2pi/N) log J_N = {mp.nstr(vN[N], 12)}"
          f"   [minus (3/2)log N corr: {mp.nstr(dN[N], 12)}]")
mono_above = all(vN[Ns[i]] > vN[Ns[i + 1]] for i in range(len(Ns) - 1)) and vN[Ns[-1]] > V_bw
rich = {}
for i in range(len(Ns) - 1):
    rich[Ns[i + 1]] = 2 * dN[Ns[i + 1]] - dN[Ns[i]]
err_final = abs(rich[1600] - V_bw)
print(f"  S027's 'monotone, from above' toward vol: {mono_above}")
print(f"  Richardson (2 d_2N - d_N) at N=1600: {mp.nstr(rich[1600], 12)}"
      f"   |diff from vol| = {mp.nstr(err_final, 3)}")
m3_ok = mono_above and err_final < mp.mpf(1) / 10000 and abs(V_bw - V_lob) < TOL
print(f"  => the growth rate IS the ambient hyperbolic volume (Kashaev 1997 /")
print(f"     proven for 4_1) -- a known-result check, not a discovered bridge.")
print(f"  MEMBER 3 AMBIENT: {m3_ok}")
print(LINE)

# ---------------------------------------------------------------- MEMBER 4
print("MEMBER 4: z0 / k=4 phase match is divisibility arithmetic in (k+2)")
z0 = (1 + 1j * mp.sqrt(3)) / 2
print(f"  z0 = (1+i sqrt3)/2;  |z0^2 - z0 + 1| = {mp.nstr(abs(z0**2 - z0 + 1), 3)}"
      f"  (tetrahedron shape);  arg z0 = pi/3: "
      f"{mp.nstr(abs(mp.arg(z0) - PI/3), 3)}")
ks = list(range(1, 13))
# reading (a): lattice unit 2pi/(k+2) equals pi/3  <=>  k+2 = 6
ka = [k for k in ks if k + 2 == 6]
# reading (b): pi/3 in { m pi/(k+2) : m in Z }  <=>  3 | (k+2)
kb = [k for k in ks if (k + 2) % 3 == 0]
# reading (c): pi/3 (mod 2pi) among actual eigenphases of U_k
kc = []
for k in ks:
    U = U_by_k.get(k) or quantum_monodromy(k, "RL")
    phases = [mp.arg(l) for l in eigvals(U)]
    if any(min(abs(p - PI / 3), abs(p + PI / 3)) < mp.mpf(10) ** -25 for p in phases):
        kc.append(k)
print(f"  (a) unit 2pi/(k+2) = pi/3      : k in {ka}   (k=4 unique: k+2 = 6 = 2*3)")
print(f"  (b) pi/3 in lattice m*pi/(k+2) : k in {kb}   (<=> 3 | (k+2) -- not unique!)")
print(f"  (c) pi/3 among eigenphases U_k : k in {kc}")
print("  NOTE (precision on the banked wording): the bullet's 'at all other k they")
print("  are multiples of pi/(k+2) != pi/3' holds only under reading (a) (the lattice")
print("  UNIT); under (b) the match recurs at every k = 1 (mod 3).  Either way the")
print("  match is pure divisibility in (k+2) -- ambient arithmetic; non-uniqueness")
print("  STRENGTHENS 'coincidence, not deep'.  No framework input anywhere.")
m4_ok = (ka == [4]) and (kb == [1, 4, 7, 10]) and abs(z0 ** 2 - z0 + 1) < TOL
print(f"  MEMBER 4 AMBIENT: {m4_ok}")
print(LINE)

# ---------------------------------------------------------------- MEMBER 5
print("MEMBER 5: 'three regimes' = the standard asymptotic/semiclassical structure")
# (i) finite k: cyclotomic -- orders from MEMBER 2 => lam in Q(zeta_q)
all_cyc = all(all(isinstance(o, int) for o in orders_by_k[k]) for k in orders_by_k)
ords4 = orders_by_k[4]
print(f"  (i)  finite k: every U_k eigenvalue verified a root of unity (MEMBER 2);")
print(f"       e.g. k=4 orders {ords4} -> all in cyclotomic fields Q(zeta_q).  {all_cyc}")
# (ii) k->infty / classical: algebraic irrational phi^2, min poly x^2-3x+1
import sympy as sp
x = sp.symbols("x")
mp_cl = sp.minimal_polynomial(sp.Rational(3, 2) + sp.sqrt(5) / 2, x)
print(f"  (ii) classical: lambda = (3+sqrt5)/2 = phi^2, minimal polynomial {mp_cl};")
print(f"       algebraic of degree 2 in Q(sqrt5), |lambda| != 1, NOT a root of unity")
print(f"       (order = {q_cl}); log-growth 2 log phi = {mp.nstr(2*mp.log(phi), 12)}")
# (iii) growth coefficient of the quantum invariant = V/(2 pi), V the volume.
# PSLQ at HIGH precision (a dps-40 run returns precision-floor spurious
# relations); any candidate must survive residual re-evaluation at dps 200.
with mp.workdps(120):
    V_hi = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))
    vec = [mp.mpf(1)] + [V_hi ** i for i in range(1, 7)]
    rel = mp.pslq(vec, maxcoeff=10 ** 8, maxsteps=10 ** 6)
if rel is None:
    genuine = False
    resid = None
else:
    with mp.workdps(200):
        V_vh = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))
        resid = abs(sum(rel[i] * V_vh ** i for i in range(7)))
    genuine = resid < mp.mpf(10) ** -150
print(f"  (iii) coefficient regime: growth rate recomputed above -> V/(2pi),")
print(f"       V = {mp.nstr(V_bw, 20)};  PSLQ (dps 120) on [1, V, ..., V^6],")
print(f"       maxcoeff 1e8: {rel}" +
      ("" if rel is None else f";  residual at dps 200 = {mp.nstr(resid, 3)}"
       f" -> genuine: {genuine}"))
print("       (no surviving relation -> no small algebraic relation, consistent")
print("       with the 'transcendental coefficient' label; finite check, not proof.)")
m5_iii_ok = (rel is None) or (not genuine)
m5_ok = all_cyc and (q_cl is None) and m5_iii_ok and sp.expand(mp_cl - (x**2 - 3*x + 1)) == 0
print("  All three regime NUMBERS come out of the ambient construction (cyclotomic")
print("  from finite level-k images; phi^2 from the classical monodromy; V from")
print("  hyperbolic geometry) -- an interpretation ON the standard asymptotics.")
print(f"  MEMBER 5 AMBIENT: {m5_ok}")
print(LINE)

# ---------------------------------------------------------------- VERDICT
print("UMBRELLA SYNTHESIS (both E19 directions)")
oks = [m1_ok, m2_ok, m3_ok, m4_ok, m5_ok]
print(f"  direction 1 (kill true?): members ambient-derived = {oks}")
print("  direction 2 (kill false?): does ANY phenomenon discriminate the framework")
print("  object?  |lambda|=1: no (holds for sister RL^2 and generic expm(iH)).")
print("  roots of unity: no (holds for sister RL^2; fails for BOTH non-TQFT")
print("  controls => mechanism is the ambient finite image, not the golden seed).")
print("  volume growth: the known 4_1 result.  pi/3 match: recurs at k=1,7,10")
print("  under the lattice reading => not a k=4 fingerprint.  regimes: standard.")
verdict = "RECONFIRMED" if all(oks) else "CHECK FAILED -- see members above"
print(f"  VERDICT: {verdict}")
