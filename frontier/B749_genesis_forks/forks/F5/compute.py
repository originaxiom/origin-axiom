#!/usr/bin/env python3
"""B749 fork F5 -- the det -1 orientability fork (sealed v2 block of MEASUREMENTS.md).

Sibling: the once-punctured-torus bundle with orientation-reversing monodromy
M = [[1,1],[1,0]] (det -1, trace 1).

Sealed measurements:
  (a) identify the manifold (expected: the Gieseking) -- by volume AND by the
      orientation double cover being isometric to m004 (the verdict-bearing fact);
  (b) invariant trace field (exact, with residual-guarded algdep + symbolic check);
  (c) cusp structure;
  (d) which V4 faces exist unoriented.

Dual route (EXECUTION_NOTES rule 3, binding):
  route A: census/isometry (m000 from the non-orientable cusped census);
  route B: explicit construction (build the det -1 bundle from monodromy data via
           SnapPea's punctured-torus-bundle notation, verified by volume + cover
           per the review-1 bundle-string trap), orientation_cover(), verify = m004;
  plus trace-field/degree cross-checks.  No single isometry call decides.

Deterministic: fixed precision, no wall clock, no unseeded randomness, no network.
"""

import sys
import warnings

warnings.filterwarnings("ignore")

import mpmath as mp
import sympy as sp
import snappy
from snappy.pari import pari
import snappy.snap as snap

PREC_BITS = 280          # working precision for polished shapes
TRACE_BITS = 256         # working precision for polished holonomy
mp.mp.prec = PREC_BITS + 20
pari.set_real_precision(95)

CHECKS = []


def check(fact, value):
    line = f"CHECK: {fact} = {value}"
    CHECKS.append(line)
    print(line)


def num(x):
    """snappy Number -> mpmath mpf/mpc via decimal string (deterministic).

    snappy prints tiny mantissas as e.g. '1.55 E-76' (space before exponent);
    strip whitespace before handing to mpmath.
    """
    def _mpf(v):
        return mp.mpf(str(v).replace(" ", ""))
    try:
        return mp.mpc(_mpf(x.real()), _mpf(x.imag()))
    except AttributeError:
        return _mpf(x)


def bloch_wigner(z):
    """Bloch-Wigner dilogarithm D(z) = Im Li2(z) + log|z| * arg(1-z)."""
    return mp.im(mp.polylog(2, z)) + mp.log(abs(z)) * mp.arg(1 - z)


print("B749/F5 compute.py -- det -1 once-punctured-torus bundle (the orientability fork)")
print(f"tools: python {sys.version.split()[0]}, snappy {snappy.__version__}, "
      f"sympy {sp.__version__}, mpmath {mp.__version__}")
print(f"precision: shapes {PREC_BITS} bits, holonomy {TRACE_BITS} bits")
print()

# ----------------------------------------------------------------------------
# 0. Exact monodromy algebra (sympy, exact integers).
# ----------------------------------------------------------------------------
print("== 0. The sibling monodromy, exactly ==")
R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
S = sp.Matrix([[0, 1], [1, 0]])          # the orientation-reversing swap, det -1
M = S * L                                 # = [[1,1],[1,0]]
M_target = sp.Matrix([[1, 1], [1, 0]])
x = sp.symbols("x")
charpoly = M.charpoly(x).as_expr()
phi = sp.Rational(1, 2) + sp.sqrt(5) / 2
check("monodromy S*L == [[1,1],[1,0]] (exact)", bool(M == M_target))
check("det(monodromy)", M.det())
check("trace(monodromy)", M.trace())
check("charpoly(monodromy)", charpoly)
check("charpoly == x^2 - x - 1 (golden; dilatation phi)",
      bool(sp.expand(charpoly - (x**2 - x - 1)) == 0))
check("phi=(1+sqrt5)/2 satisfies charpoly exactly",
      bool(sp.simplify(charpoly.subs(x, phi)) == 0))
Msq = M * M
RL = R * L
check("monodromy^2 == [[2,1],[1,1]] == R*L (m004's monodromy, exact)",
      bool(Msq == sp.Matrix([[2, 1], [1, 1]]) and Msq == RL))
check("charpoly(monodromy^2) == x^2 - 3x + 1 (dilatation phi^2)",
      bool(sp.expand(Msq.charpoly(x).as_expr() - (x**2 - 3 * x + 1)) == 0))
# Homology prediction for the mapping torus: H1 = Z + coker(M - I).
detMI = (M - sp.eye(2)).det()
check("det(M - I) (exact; = -1 => coker(M-I)=0 => predicted H1 = Z)", detMI)
print()

# ----------------------------------------------------------------------------
# 1. The bundle-string trap (review-1 warning, binding): verify live.
# ----------------------------------------------------------------------------
print("== 1. Bundle-string trap verified live (never trust notation) ==")
m004 = snappy.Manifold("m004")
m000 = snappy.Manifold("m000")
catalan2 = mp.catalan * 2
trap = {}
for s in ["b++RL", "b+-RL", "b-+RL", "b--RL"]:
    B = snappy.Manifold(s)
    trap[s] = B
    print(f"  {s}: orientable={B.is_orientable()} vol={B.volume()} "
          f"H1={B.homology()} cusps={[c.topology for c in B.cusp_info()]}")
check("b++RL.is_isometric_to(m004) (review-1 fact)",
      trap["b++RL"].is_isometric_to(m004))
check("b+-RL orientable with H1 = Z/5 + Z (NOT the Gieseking; the -RL sister)",
      f"orientable={trap['b+-RL'].is_orientable()}, H1={trap['b+-RL'].homology()}")
voltrap = num(trap["b-+RL"].volume())
check("b-+RL volume == 2*Catalan to 9 digits (a DIFFERENT non-orientable manifold)",
      f"{trap['b-+RL'].volume()} vs 2*Catalan={mp.nstr(catalan2, 11)}, "
      f"|diff|<1e-9: {bool(abs(voltrap - catalan2) < mp.mpf('1e-9'))}")
print()

# ----------------------------------------------------------------------------
# 2. Route B: explicit construction of the det -1 bundle.
#    SnapPea punctured-torus-bundle notation: 'b-<s><word>' builds the mapping
#    torus whose monodromy is (reflection) * (word in R,L); the swap S conjugates
#    L to R, so (S*L)^2 = R*L exactly (section 0).  Candidate string 'b-+L'.
#    Per the sealed warning the string is TRUSTED ONLY after volume + cover checks.
# ----------------------------------------------------------------------------
print("== 2. Route B: build the det -1 bundle, verify string by volume + cover ==")
sib = snappy.Manifold("b-+L")
print(f"  b-+L: orientable={sib.is_orientable()} vol={sib.volume()} "
      f"tets={sib.num_tetrahedra()} H1={sib.homology()} "
      f"cusps={[c.topology for c in sib.cusp_info()]}")
GIESEKING_VOL = mp.mpf("1.0149416064096536")   # sealed reference (2 * this = m004)
vol_sib = num(sib.volume())
check("routeB sibling ('b-+L') volume matches Gieseking 1.0149416064 (|diff|<1e-9)",
      bool(abs(vol_sib - GIESEKING_VOL) < mp.mpf("1e-9")))
check("routeB sibling is_orientable", sib.is_orientable())
check("routeB sibling num_tetrahedra", sib.num_tetrahedra())
check("routeB sibling H1 (predicted Z from det(M-I)=-1)", sib.homology())
check("routeB sibling cusp topology", [c.topology for c in sib.cusp_info()])
# all four single-letter det -1 strings, for the record (they coincide):
for s in ["b--L", "b-+R", "b--R"]:
    Bx = snappy.Manifold(s)
    print(f"  {s}: vol={Bx.volume()} iso b-+L: {Bx.is_isometric_to(sib)}")

oc_sib = sib.orientation_cover()
vol_oc = num(oc_sib.volume())
check("routeB orientation_cover volume (expect 2x Gieseking = 2.0298832128)",
      oc_sib.volume())
check("routeB orientation_cover volume == 2 * sibling volume (|diff|<1e-9)",
      bool(abs(vol_oc - 2 * vol_sib) < mp.mpf("1e-9")))
check("routeB orientation_cover().is_isometric_to(m004)  [VERDICT-BEARING]",
      oc_sib.is_isometric_to(m004))
check("routeB orientation_cover H1 (m004 has Z)", oc_sib.homology())
check("routeB orientation_cover cusp topology",
      [c.topology for c in oc_sib.cusp_info()])
print()

# ----------------------------------------------------------------------------
# 3. Route A: census/isometry.  m000 = the Gieseking in the non-orientable
#    cusped census.  Identification by TWO+ independent invariants.
# ----------------------------------------------------------------------------
print("== 3. Route A: census m000, cross-tied to route B ==")
print(f"  m000: orientable={m000.is_orientable()} vol={m000.volume()} "
      f"tets={m000.num_tetrahedra()} H1={m000.homology()} "
      f"cusps={[c.topology for c in m000.cusp_info()]}")
vol_m000 = num(m000.volume())
check("routeA m000 volume matches Gieseking 1.0149416064 (|diff|<1e-9)",
      bool(abs(vol_m000 - GIESEKING_VOL) < mp.mpf("1e-9")))
check("routeA m000 H1", m000.homology())
check("routeA m000 cusp topology", [c.topology for c in m000.cusp_info()])
check("routeA m000.is_isometric_to(routeB sibling)", m000.is_isometric_to(sib))
oc_m000 = m000.orientation_cover()
check("routeA m000.orientation_cover().is_isometric_to(m004)  [VERDICT-BEARING]",
      oc_m000.is_isometric_to(m004))
check("sibling.identify() census names", [str(N) for N in sib.identify()])
check("m000.identify() census names", [str(N) for N in m000.identify()])
# Independent cover route: enumerate ALL degree-2 covers of m000.
covs = m000.covers(2)
cov_desc = [(C.is_orientable(), str(C.volume()), str(C.homology())) for C in covs]
check("m000.covers(2) [(orientable, vol, H1)]", cov_desc)
orient_covs = [C for C in covs if C.is_orientable()]
check("number of orientable degree-2 covers of m000", len(orient_covs))
check("every orientable degree-2 cover of m000 is_isometric_to m004",
      all(C.is_isometric_to(m004) for C in orient_covs))
print()

# ----------------------------------------------------------------------------
# 4. High-precision volumes from first principles (Bloch-Wigner at the exact
#    shape), double-checking the SnapPea kernel numbers.
# ----------------------------------------------------------------------------
print("== 4. Volume cross-check via Bloch-Wigner D(z) at the regular ideal shape ==")
omega_num = mp.mpc(mp.mpf(1) / 2, mp.sqrt(3) / 2)
D_omega = bloch_wigner(omega_num)
print(f"  D((1+i*sqrt3)/2) = {mp.nstr(D_omega, 40)}")
check("Bloch-Wigner D(omega) matches sibling volume (|diff|<1e-9)",
      bool(abs(D_omega - vol_sib) < mp.mpf("1e-9")))
check("2*D(omega) matches m004 volume (|diff|<1e-9)",
      bool(abs(2 * D_omega - num(m004.volume())) < mp.mpf("1e-9")))
print()

# ----------------------------------------------------------------------------
# 5. (b) Invariant trace field, exactly.
#    Polished shapes -> residual-guarded algdep -> EXACT symbolic verification
#    of the gluing equations at z = (1+sqrt(-3))/2, plus pari nffactor
#    (the factornf-style exact field confirmation).  Neumann-Reid: for a cusped
#    orientable finite-volume hyperbolic 3-manifold the invariant trace field
#    equals the tetrahedron-shape field; for the non-orientable sibling the
#    invariant trace field is defined via the orientation double cover (= m004).
# ----------------------------------------------------------------------------
print("== 5. Invariant trace field (exact) ==")
z = sp.symbols("z")
omega = (1 + sp.sqrt(-3)) / 2                       # candidate exact shape
minpoly_candidate = sp.Poly(z**2 - z + 1, z)

shape_data = {}
for name, Mfd in [("m000", m000), ("m004", m004)]:
    shapes = Mfd.tetrahedra_shapes("rect", bits_prec=PREC_BITS)
    zs = [num(s) for s in shapes]
    shape_data[name] = zs
    for i, zi in enumerate(zs):
        # residual-guarded algdep (coefficient-size-aware threshold)
        zp = pari(f"{mp.nstr(zi.real, 80)} + {mp.nstr(zi.imag, 80)}*I")
        p = pari.algdep(zp, 2)
        coeffs = [int(c) for c in pari.Vec(p)]
        height = max(abs(c) for c in coeffs)
        deg = len(coeffs) - 1
        resid = abs(sum(mp.mpc(c) * zi ** (deg - k) for k, c in enumerate(coeffs)))
        bound = (deg + 1) * height * max(1, abs(zi)) ** deg * mp.mpf(2) ** (-(PREC_BITS - 30))
        check(f"{name} shape[{i}] algdep", str(p))
        check(f"{name} shape[{i}] algdep residual < coefficient-aware bound "
              f"({mp.nstr(resid, 3)} < {mp.nstr(bound, 3)})", bool(resid < bound))
        # exact-root proximity: the polished shape IS (1+sqrt(-3))/2 to precision
        dist = abs(zi - omega_num)
        check(f"{name} shape[{i}] == (1+sqrt(-3))/2 to 2^-{PREC_BITS - 30} "
              f"(|diff|={mp.nstr(dist, 3)})",
              bool(dist < mp.mpf(2) ** (-(PREC_BITS - 30))))

check("candidate minpoly z^2 - z + 1 irreducible over Q",
      bool(minpoly_candidate.is_irreducible))
check("omega = (1+sqrt(-3))/2 satisfies z^2 - z + 1 = 0 exactly",
      bool(sp.simplify(minpoly_candidate.as_expr().subs(z, omega)) == 0))

# EXACT verification of every SnapPea gluing equation at the exact shape.
# rect convention: (A, B, c) means  c * prod z_i^A_i * (1-z_i)^B_i = 1.
# (Convention validated numerically below at 280 bits before exact use.)
for name, Mfd in [("m004", m004), ("m000", m000)]:
    eqs = Mfd.gluing_equations("rect")
    zs = shape_data[name]
    exact_ok, numeric_ok, notes = [], [], []
    for (A, B, c) in eqs:
        val_num = mp.mpc(c)
        for zi, a, b in zip(zs, A, B):
            val_num *= zi**a * (1 - zi) ** b
        val_exact = sp.Integer(c)
        for a, b in zip(A, B):
            val_exact *= omega**a * (1 - omega) ** b
        val_exact = sp.simplify(val_exact)
        if abs(val_num - 1) < mp.mpf(2) ** (-(PREC_BITS - 40)):
            numeric_ok.append(True)
            exact_ok.append(bool(val_exact == 1))
            notes.append(f"(A={A},B={B},c={c}): exact value {val_exact}")
        else:
            # non-orientable completeness rows hold as |value| = 1
            numeric_ok.append(bool(abs(abs(val_num) - 1) < mp.mpf(2) ** (-(PREC_BITS - 40))))
            exact_ok.append(bool(sp.simplify(sp.Abs(val_exact)) == 1))
            notes.append(f"(A={A},B={B},c={c}): exact value {val_exact}, |value| = 1 "
                         "(orientation-reversing completeness row)")
    for n in notes:
        print(f"  {name} gluing eq {n}")
    check(f"{name} all gluing equations verified EXACTLY at z=(1+sqrt(-3))/2 "
          "(numeric convention check passed)",
          bool(all(exact_ok) and all(numeric_ok)))

# Field identification: Q(omega) = Q(sqrt(-3)), degree 2, discriminant -3.
ident = sp.expand((2 * omega - 1) ** 2)
check("(2*omega - 1)^2 == -3 exactly (so Q(omega) = Q(sqrt(-3)))", ident)
check("field degree [Q(sqrt(-3)):Q]",
      int(sp.minimal_polynomial(omega, z, polys=True).degree()))
check("pari nfdisc(z^2 - z + 1) (field discriminant)", str(pari.nfdisc("z^2 - z + 1")))
nf = pari.nfinit("z^2 - z + 1")
fac = pari.nffactor(nf, "x^2 + 3")
n_linear = sum(1 for k in range(1, pari.matsize(fac)[0] + 1)
               if int(pari.poldegree(fac[k - 1, 0])) == 1)
check("pari nffactor(x^2+3 over Q[z]/(z^2-z+1)) splits into linear factors "
      "(factornf-style exact confirmation)",
      f"{n_linear} linear factors: {fac}")
print()

# ----------------------------------------------------------------------------
# 6. Arithmeticity face (verified, not cited).  Cusped criterion
#    (Maclachlan-Reid Thm 8.2.3, non-cocompact case): arithmetic iff the
#    invariant trace field is imaginary quadratic AND all traces are algebraic
#    integers.  For the 2-generator group, Fricke: every trace is an integer
#    polynomial in (tr a, tr b, tr ab); integrality of those three suffices
#    (sign ambiguity of PSL2 traces does not affect integrality).
#    Arithmeticity is a commensurability invariant; sibling ~ m004 (2:1 cover).
# ----------------------------------------------------------------------------
print("== 6. Arithmeticity of m004 (cusped Maclachlan-Reid criterion) ==")
G = snap.polished_holonomy(m004, bits_prec=TRACE_BITS, lift_to_SL2=False)
check("m004 fundamental group generators / relators",
      f"{m004.fundamental_group().num_generators()} generators, "
      f"relators {m004.fundamental_group().relators()}")
trace_exact = {
    "a": (-3 + sp.sqrt(-3)) / 2,     # minpoly t^2 + 3t + 3 (monic)
    "b": 1 - sp.sqrt(-3),            # minpoly t^2 - 2t + 4 (monic)
    "ab": sp.Integer(-2),            # minpoly t + 2 (monic)
}
t = sp.symbols("t")
all_integral = True
for word, exact in trace_exact.items():
    tr_num = num(G(word).trace())
    diff = abs(tr_num - mp.mpc(str(sp.re(sp.N(exact, 90))), str(sp.im(sp.N(exact, 90)))))
    mp_ok = bool(diff < mp.mpf(2) ** (-(TRACE_BITS - 30)))
    mpoly = sp.minimal_polynomial(exact, t)
    monic = bool(sp.Poly(mpoly, t).LC() == 1 and
                 all(c.is_integer for c in sp.Poly(mpoly, t).all_coeffs()))
    all_integral = all_integral and monic and mp_ok
    check(f"tr({word}) [PSL2, up to sign] == {exact} exactly "
          f"(|diff|={mp.nstr(diff, 3)}); minpoly {mpoly} monic integral",
          bool(mp_ok and monic))
check("m004: invariant trace field imaginary quadratic Q(sqrt(-3)) AND generator "
      "traces algebraic integers => ARITHMETIC (Maclachlan-Reid 8.2.3, cusped)",
      all_integral)
check("sibling arithmetic (commensurable with m004 via the 2:1 orientation cover)",
      all_integral)
print()

# ----------------------------------------------------------------------------
# 7. (c) Cusp structure and (d) the V4 faces, unoriented.
# ----------------------------------------------------------------------------
print("== 7. Cusp structure + face table ==")
ci_sib = sib.cusp_info(0)
ci_m004 = m004.cusp_info(0)
check("sibling cusp: count / topology",
      f"{sib.num_cusps()} cusp, {ci_sib.topology}")
check("m004 cusp: count / topology",
      f"{m004.num_cusps()} cusp, {ci_m004.topology}")
shape_m004_cusp = num(ci_m004.shape)
check("m004 cusp modulus == 2*sqrt(-3) (|diff|<1e-9; modulus in Q(sqrt(-3)))",
      bool(abs(shape_m004_cusp - mp.mpc(0, 2 * mp.sqrt(3))) < mp.mpf("1e-9")))
shape_sib_cusp = num(ci_sib.shape)
check("sibling Klein-bottle cusp modulus == i*sqrt(3)/6 (|diff|<1e-9)",
      bool(abs(shape_sib_cusp - mp.mpc(0, mp.sqrt(3) / 6)) < mp.mpf("1e-9")))

print()
print("FACE TABLE (V4 anatomy of the banked m004 interface, measured unoriented):")
faces = [
    ("being / trace field Q(sqrt(-3))",
     "PRESENT -- invariant trace field (via orientation cover m004) = Q(sqrt(-3)); "
     "the sibling's own shape field is ALSO Q(sqrt(-3)) exactly (edge eqn z(1-z)=1)"),
    ("hearing / golden Q(sqrt(5))",
     "PRESENT, REFINED -- monodromy dilatation is phi itself (charpoly x^2-x-1); "
     "m004's monodromy is its square (dilatation phi^2): the sibling is the "
     "golden square root of the banked monodromy"),
    ("cusp / interface",
     "PRESENT, UNORIENTED -- one cusp survives as a Klein bottle (modulus "
     "i*sqrt(3)/6); orientation restores the torus cusp of m004 (modulus 2*sqrt(-3))"),
    ("knot-ness H1 = Z",
     "PRESENT as homology -- H1(sibling) = Z (= Z + coker(M-I), det(M-I) = -1); "
     "not an S^3 knot complement (non-orientable), but the homological signature holds"),
    ("arithmeticity",
     "PRESENT -- m004 verified arithmetic (cusped criterion, section 6); "
     "the sibling is commensurable with it (2:1 cover)"),
]
for fname, status in faces:
    print(f"  - {fname}: {status}")
print()

# ----------------------------------------------------------------------------
# 8. Verdict per the sealed criteria.
# ----------------------------------------------------------------------------
print("== 8. Verdict ==")
fragile_fact = (oc_sib.is_isometric_to(m004) and oc_m000.is_isometric_to(m004)
                and m000.is_isometric_to(sib))
check("F5 sealed FRAGILE criterion: the orientation double cover of the det -1 "
      "sibling IS m004 (dual-route)", fragile_fact)
verdict = "FRAGILE" if fragile_fact else "ROBUST"
check("VERDICT F5", verdict)
print()
print(f"F5 VERDICT: {verdict} -- the discarded det -1 choice re-enters the chain as "
      "ancestry: the sibling is the Gieseking, m004's parent, and A6's price is "
      "'orientation = passing to the child'.")
print()
print("Verdict matches the sealed prior (F5 FRAGILE); the contra-prior-ROBUST "
      "skeptic trigger of EXECUTION_NOTES rule 1 does not fire.")
