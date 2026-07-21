"""B739 Stage B recompute — TOMB-L267 (umbrella: the CM/arithmetic cluster of 2026-06-11).

Banked claim killed (umbrella): the two identifications of that review session + audit are dead —
  K-N: |disc_CM| = kappa_m  (the CM discriminant equals the commutator/monodromy parameter m^2+2)
  K-O: the golden "trace leak"  tr rho_{SU(2)_3}(seed) = -1/phi  as a DISTINGUISHED signal.
The math underneath is fine; the identifications are the kills.

Discriminating facts re-derived here (compute-not-cite, E19):
  (K-N)  kappa_m = tr(R^m L^m) = m^2 + 2 exactly (symbolic);  the silver (m=2) CM field is Q(i)
         with |disc| = 4 != 6 = kappa_2, while the golden (m=1) "3 = 3" is a shared integer only;
         m = 3..6 have NO imaginary-quadratic shape field at all (no CM disc exists), so the
         revival kill condition ("a metallic m>=2 with |disc_CM| = kappa_m") has empty support.
  (K-O)  in the finite image (order 2880) of the SU(2)_3 modular representation, the seed's
         trace class is POPULATED, not a singleton: 1350/2880 elements have nonzero trace and
         384/2880 have golden-magnitude (|phi^{+-1}|) trace; the seed value -1/phi itself
         recomputes exactly (the "math fine" half), and RRL / RLL have trace 0 (the banked
         per-element table).

Declared conventions (E1):
  - Metallic family: R = [[1,1],[0,1]], L = [[1,0],[1,1]]; the m-th metallic once-punctured-torus
    bundle is the SnapPy bundle 'b++' + 'R'*m + 'L'*m (B125/B147 convention); m=1 = figure-eight.
  - kappa_m := tr(R^m L^m) = m^2+2, the banked B148 identity (the tombstone's own in-line value
    kappa_2 = m^2+2 = 6); "commutator parameter" per the Fricke convention kappa = x^2+y^2+z^2-xyz-2
    = tr[A,B] pinned in B148/V137.
  - CM field / disc_CM: the invariant trace field kM, computed as the SHAPE field (Neumann-Reid:
    equal for cusped M) via high-precision tetrahedra shapes + pari.algdep — exactly the
    B125/B147 method — with an added residual guard (candidate minimal polynomial must vanish
    at the shape to ~1e-30; B147 guard discipline).  disc = poldisc of the reduced quadratic.
  - SU(2)_3 modular rep: verbatim B210 (k=3, n=k+2=5; S_ab = sqrt(2/5) sin(pi (a+1)(b+1)/5);
    T = diag(exp(2 pi i (h_a - c/24))), h_a = a(a+2)/20, c = 3k/(k+2) = 9/5); image = BFS closure
    of <S,T> with 5-decimal rounding keys (B210's own key convention).
  - Seed word into the rep (undeclared in the banked record, declared here): SL(2,Z) generators
    S = [[0,-1],[1,0]], T = [[1,1],[0,1]]; R = T and L = S T^-1 S^-1 (verified below as an exact
    2x2 integer identity), so rho(R) = T_rep, rho(L) = S_rep T_rep^-1 S_rep^-1, seed = rho(R)rho(L).
  - Tolerances: trace zero/golden tests at 1e-6 (trace values are separated by O(0.1); see the
    distinct-|trace| table printed below); algdep residual gate 1e-30 at 220-bit shapes.

Deterministic: no wall-clock, no randomness, no network. SnapPy census lookups are local.
Gate 5: pure mathematics (number fields, modular representations); no SM quantities.
"""
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import sympy as sp
import mpmath as mp
import snappy
import cypari

pari = cypari.pari
pari.set_real_precision(70)
mp.mp.dps = 60

PHI = (1 + 5 ** 0.5) / 2

print("=" * 78)
print("TOMB-L267 recompute — the CM/arithmetic cluster (K-N + K-O)")
print("=" * 78)

# ---------------------------------------------------------------------------
# Part 1 (K-N, arithmetic side): kappa_m = tr(R^m L^m) = m^2 + 2, exact/symbolic.
# ---------------------------------------------------------------------------
print("\n[1] kappa_m = tr(R^m L^m), symbolic (sympy):")
m = sp.symbols("m", positive=True, integer=True)
R2 = sp.Matrix([[1, 1], [0, 1]])
L2 = sp.Matrix([[1, 0], [1, 1]])
Rm = sp.Matrix([[1, m], [0, 1]])          # R^m exactly
Lm = sp.Matrix([[1, 0], [m, 1]])          # L^m exactly
assert sp.simplify(R2 ** 3 - sp.Matrix([[1, 3], [0, 1]])) == sp.zeros(2, 2)  # sanity: R^m form
tr_sym = sp.expand((Rm * Lm).trace())
print("    tr(R^m L^m) =", tr_sym)
assert tr_sym == m ** 2 + 2
kappa = {mm: mm ** 2 + 2 for mm in (1, 2, 3, 4, 5, 6)}
for mm in (1, 2):
    Mnum = (R2 ** mm) * (L2 ** mm)
    assert Mnum.trace() == kappa[mm] and Mnum.det() == 1
print("    kappa_1 =", kappa[1], "  kappa_2 =", kappa[2])

# ---------------------------------------------------------------------------
# Part 2 (K-N, CM side): shape fields of the metallic bundles (B125/B147 method).
# ---------------------------------------------------------------------------
print("\n[2] CM / invariant trace fields via shape field + algdep (residual-guarded):")

RESIDUAL_GATE = mp.mpf(10) ** -30
HEIGHT_GATE = 10 ** 6   # genuine shape-field quadratics here have single-digit coefficients;
                        # algdep can always fabricate a ~30-digit-coefficient "fit" at finite
                        # precision (observed at m=4), so a height gate is required for the
                        # test to DISCRIMINATE (B147 guard discipline).

def shape_minpoly_deg2(z_real_str, z_imag_str):
    """pari.algdep degree-2 candidate + residual + coefficient height at the shape."""
    zc = pari.complex(z_real_str, z_imag_str)
    cand = pari.algdep(zc, 2)
    zm = mp.mpc(mp.mpf(z_real_str), mp.mpf(z_imag_str))
    coeffs = [mp.mpf(str(cand.polcoef(d))) for d in range(int(cand.poldegree()) + 1)]
    res = abs(sum(c * zm ** d for d, c in enumerate(coeffs)))
    height = max(abs(int(cand.polcoef(d))) for d in range(int(cand.poldegree()) + 1))
    return cand, res, height

def bundle_shapes(word):
    M = snappy.Manifold(word)
    shapes = M.tetrahedra_shapes(part="rect", bits_prec=220)
    # SnapPy number strings may carry a spaced exponent ("... e-78"); normalize for mpmath/pari
    return M, [(str(z.real()).replace(" ", ""), str(z.imag()).replace(" ", "")) for z in shapes]

disc_CM = {}
for mm, expect_field in ((1, "golden"), (2, "silver")):
    word = "b++" + "R" * mm + "L" * mm
    M, shapes = bundle_shapes(word)
    idents = [str(x) for x in M.identify()]
    print(f"    m={mm} {word}: identify -> {idents}; vol = {M.volume()}")
    minpolys = set()
    quad_ok = True
    for zr, zi in shapes:
        cand, res, height = shape_minpoly_deg2(zr, zi)
        ok = res < RESIDUAL_GATE and height <= HEIGHT_GATE
        quad_ok &= ok
        minpolys.add(str(cand))
        print(f"      shape ~ {zr[:12]} + {zi[:12]} i : minpoly {cand}  "
              f"(residual {mp.nstr(res, 3)}, height {height}, quad_fit={ok})")
    assert quad_ok, f"m={mm}: a shape failed its quadratic fit"
    # the shape field is the compositum; both metallic CM members are single quadratic fields
    field_polys = sorted(minpolys)
    # reduced field disc: the fundamental discriminant of each quadratic's disc
    red = {int(pari(f"coredisc(poldisc({p}))")) for p in field_polys}
    assert len(red) == 1, f"m={mm}: shapes span more than one quadratic field: {field_polys} discs {red}"
    disc_CM[mm] = red.pop()
    print(f"      => shape field = invariant trace field: fundamental disc = {disc_CM[mm]}")

assert disc_CM[1] == -3, "golden CM field must be Q(sqrt-3)"
assert disc_CM[2] == -4, "silver CM field must be Q(i)"

# supporting (banked NUMERICAL in B147 addendum): silver volume = 4*Catalan
vol_silver = mp.mpf(str(snappy.Manifold("b++RRLL").volume()))
print(f"    silver vol - 4*Catalan = {mp.nstr(vol_silver - 4 * mp.catalan, 5)}  (|.| < 1e-9)")
assert abs(vol_silver - 4 * mp.catalan) < mp.mpf("1e-9")

print("\n[2b] m=3..6: no imaginary-quadratic shape field (no CM disc exists):")
for mm in (3, 4, 5, 6):
    word = "b++" + "R" * mm + "L" * mm
    M, shapes = bundle_shapes(word)
    worst = None
    any_nonquad = False
    for zr, zi in shapes:
        cand, res, height = shape_minpoly_deg2(zr, zi)
        if res > RESIDUAL_GATE or height > HEIGHT_GATE:
            any_nonquad = True
            worst = (res, height)
            break
    assert any_nonquad, f"m={mm}: unexpectedly all shapes genuinely quadratic"
    print(f"    m={mm} {word}: a shape REFUSES every honest degree<=2 fit "
          f"(best candidate residual {mp.nstr(worst[0], 3)}, coeff height {worst[1]:.2e}) "
          f"-> kM degree > 2, not CM")

print("\n[K-N verdict data]")
print(f"    golden m=1: |disc_CM| = {abs(disc_CM[1])}  vs kappa_1 = {kappa[1]}  ->  EQUAL (the shared integer)")
print(f"    silver m=2: |disc_CM| = {abs(disc_CM[2])}  vs kappa_2 = {kappa[2]}  ->  {abs(disc_CM[2])} != {kappa[2]}  (the kill)")
print("    m>=3: no CM discriminant exists (kM not imaginary quadratic) -> revival condition empty")
assert abs(disc_CM[1]) == kappa[1]           # 3 = 3 at m=1 (the coincidence)
assert abs(disc_CM[2]) != kappa[2]           # 4 != 6 at m=2 (the discriminating fact)

# ---------------------------------------------------------------------------
# Part 3 (K-O): the SU(2)_3 modular image, the seed trace, and the class count.
# ---------------------------------------------------------------------------
print("\n[3] SU(2)_3 modular representation (B210 conventions verbatim):")
k = 3
n = k + 2
a = np.arange(4)
S_rep = np.sqrt(2 / n) * np.sin(np.pi * np.outer(a + 1, a + 1) / n)
h = a * (a + 2) / (4 * n)
T_rep = np.diag(np.exp(2j * np.pi * (h - (3 * k / (k + 2)) / 24)))

# exact 2x2 integer identity behind the word convention: L = S T^-1 S^-1 in SL(2,Z)
Sz = sp.Matrix([[0, -1], [1, 0]])
Tz = sp.Matrix([[1, 1], [0, 1]])
assert Sz * Tz ** -1 * Sz ** -1 == sp.Matrix([[1, 0], [1, 1]])   # = L
assert Tz == sp.Matrix([[1, 1], [0, 1]])                          # = R

I4 = np.eye(4)

def key(Mx):
    return tuple(np.round(Mx.flatten(), 5))

seen = {key(I4): I4}
frontier = [I4]
while frontier:
    nf = []
    for Mx in frontier:
        for g in (S_rep, T_rep):
            P = Mx @ g
            kk = key(P)
            if kk not in seen:
                seen[kk] = P
                nf.append(P)
    frontier = nf
order = len(seen)
print(f"    |<S,T>| = {order}   (banked: 2880; 2I would be 120)")
assert order == 2880

S_inv = np.linalg.inv(S_rep)
T_inv = np.linalg.inv(T_rep)
rho_R = T_rep
rho_L = S_rep @ T_inv @ S_inv
seed = rho_R @ rho_L
tr_seed = np.trace(seed)
print(f"    tr rho(RL) = {tr_seed:.15f}")
print(f"    -1/phi     = {-1 / PHI:.15f}")
assert abs(tr_seed - (-1 / PHI)) < 1e-12    # the 'math fine' half: the seed trace IS -1/phi

TOL = 1e-6
traces = [np.trace(Mx) for Mx in seen.values()]
nonzero = sum(1 for t in traces if abs(t) > TOL)
goldenmag = sum(1 for t in traces if abs(abs(t) - PHI) < TOL or abs(abs(t) - 1 / PHI) < TOL)
print(f"    nonzero-trace elements       : {nonzero}/{order} = {nonzero/order:.5f}  (banked 1350/2880 ~ 47%)")
print(f"    golden-magnitude |phi^(+-1)| : {goldenmag}/{order} = {goldenmag/order:.5f}  (banked 384/2880 ~ 13%)")
assert nonzero == 1350
assert goldenmag == 384

# banked per-element table spot-checks: RRL and RLL have trace exactly 0
for wname, word in (("RRL", "RRL"), ("RLL", "RLL")):
    Mx = I4.copy()
    for c in word:
        Mx = Mx @ (rho_R if c == "R" else rho_L)
    t = np.trace(Mx)
    print(f"    tr rho({wname}) = {abs(t):.2e}  (banked: exactly 0)")
    assert abs(t) < TOL

# the trace-value landscape (supporting: the seed's class is populated, not a singleton)
from collections import Counter
mag_hist = Counter(round(float(abs(t)), 6) for t in traces)
print("    distinct |trace| values (value: count):")
for v in sorted(mag_hist):
    print(f"      {v:>9.6f} : {mag_hist[v]}")
seed_mag_class = mag_hist[round(1 / PHI, 6)]
print(f"    elements sharing the seed's |trace| = 1/phi magnitude: {seed_mag_class} (a populated class)")
assert seed_mag_class > 1

print("\n[K-O verdict data]")
print(f"    order {order}; nonzero {nonzero} ({nonzero/order:.1%}); golden-magnitude {goldenmag} ({goldenmag/order:.1%});")
print(f"    seed trace -1/phi reproduced; RRL/RLL trace 0 reproduced; seed class populated -> no distinguished signal.")

# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("VERDICT: RECONFIRMED")
print("  K-N: |disc_CM(silver)| = 4 != 6 = kappa_2 = m^2+2 (m=2); golden 3=3 is m=1-only;")
print("       m=3..6 possess no CM discriminant (shape field degree > 2). Identification dead.")
print("  K-O: image order 2880; 1350 nonzero-trace (46.9%), 384 golden-magnitude (13.3%);")
print("       seed trace -1/phi exact but its class is populated. No distinguished signal.")
print("  The umbrella kill (math fine, identification dead) recomputes true in both branches.")
print("=" * 78)
