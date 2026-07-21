#!/usr/bin/env python3
"""
B749 fork F3 -- THE SILVER SLOPE (sealed campaign, seal v2).

Sibling (sealed in MEASUREMENTS.md): the m=2 once-punctured-torus bundle,
monodromy [[2,1],[1,0]]^2 = [[5,2],[2,1]] = R^2 L^2, trace 6.

Binding measurements (MEASUREMENTS.md F3 block):
  (a) volume + hyperbolicity (snappy)
  (b) trace field: exact minpoly of tr(gamma), algdep-verified with residual guard
      (cc2's lindep lesson: coefficient-size-aware thresholds, exact factornf/nffactor
      confirmation; algdep output FACTORED, irreducible vanishing factor selected)
  (c) arithmeticity (Maclachlan-Reid non-cocompact criterion; B125 predicted YES --
      verified here, not cited)
  (d) H1 / knot-ness (m004 has Z; compute coker(A - I) exactly + snappy cross-check)
  (e) which V4 faces survive (banked V4: being Q(sqrt-3), hearing Q(sqrt5),
      meeting Q(sqrt-15), at the cusp/interface; special prime 3 per B718)

Cross-fork instrument rules (binding): every exact field claim = numeric relation +
exact nf confirmation; every manifold identification = >= 2 independent invariants
(volume + isometry, plus homology here); deterministic (fixed precisions, no clock,
no randomness, no network); CHECK: lines printed for the merge gate.

Verdict criteria (sealed): ROBUST = silver lacks >= 2 of {knot-ness, being-field
analogue's special prime, interface structure}; FRAGILE = comparable full interface.

Tools: python 3.12.1, snappy 3.3.2, cypari, sympy, mpmath (B742 conventions).
"""

import warnings
warnings.filterwarnings("ignore")

import itertools

import cypari
import mpmath
import snappy
import sympy as sp
from snappy.snap import polished_holonomy, polished_tetrahedra_shapes

pari = cypari.pari
pari.set_real_precision(350)
mpmath.mp.dps = 330

BITS_LO, BITS_HI = 700, 1100
DIG_LO, DIG_HI = 210, 331          # floor(bits * log10(2))
GUARD_LO, GUARD_HI = 140, 230      # required -log10(normalized residual)
CHECKS = []


def check(line):
    s = "CHECK: " + line
    print(s)
    CHECKS.append(s)


def note(line):
    print("  " + line)


def pgen(snappy_number):
    """snappy Number -> pari GEN (exact wrapper transfer, no string parsing)."""
    return snappy_number.gen


HEIGHT_CAP = 10 ** 12   # true relations here have height <= 52; LLL fakes at 210+
                        # digits have height ~ 10^(digits/(deg+1)) >> 10^12


def _algdep_candidates(t, maxdeg):
    """Factor the algdep output (cc2 lindep lesson: algdep may return reducible/
    degenerate polys) and yield (irreducible factor, height, -log10 normres)."""
    fac = pari.factor(pari.algdep(t, maxdeg))
    out = []
    for i in range(len(fac[0])):
        f = fac[0][i]
        if pari.poldegree(f) < 1:
            continue
        res = pari.abs(pari.subst(f, "x", t))
        height = sum(abs(int(c)) for c in pari.Vec(f))
        scale = height * max(1, float(pari.abs(t))) ** int(pari.poldegree(f))
        nres = res / pari(scale)
        nexp = float(-pari.log(nres) / pari.log(10)) if nres > 0 else 999.0
        out.append((f, height, nexp))
    return out


def guarded_minpoly(t, maxdeg, digits, guard, label):
    """Coefficient-size-aware acceptance (the cc2 lindep lesson, hardened by the
    S10 sentinel): a candidate minpoly is accepted only if
      (1) it is an irreducible factor of the algdep output,
      (2) height(f) = ||f||_1 <= HEIGHT_CAP  (LLL fakes at D digits have height
          ~ 10^(D/(deg+1)), far above the cap; true small fields stay tiny),
      (3) normalized residual |f(t)|/(||f||_1 * max(1,|t|)^deg) < 10^-guard
          (low-height fakes cannot reach this: best ~ 10^(-deg*log10(cap))).
    Cross-precision stability is asserted by the callers (lo vs hi runs)."""
    cands = [c for c in _algdep_candidates(t, maxdeg) if c[1] <= HEIGHT_CAP]
    if not cands:
        raise RuntimeError(f"no height-admissible algdep factor for {label}")
    best, height, nexp = max(cands, key=lambda c: c[2])
    ok = nexp > guard
    print(f"    [{label}] algdep -> {best}   (height {height}; -log10 normres = "
          f"{nexp:.1f}; guard {guard}; {'PASS' if ok else 'FAIL'})")
    if not ok:
        raise RuntimeError(f"residual guard FAILED for {label}: {nexp:.1f} <= {guard}")
    assert int(pari.polisirreducible(best)) == 1
    return best, nexp


def sentinel_minpoly(t, maxdeg, guard, label):
    """Same acceptance logic, EXPECTED to reject everything (non-vacuity sentinel)."""
    accepted = []
    for f, height, nexp in _algdep_candidates(t, maxdeg):
        if height <= HEIGHT_CAP and nexp > guard:
            accepted.append((f, height, nexp))
        print(f"    [sentinel {label}] candidate height {height:.3e}, -log10 normres "
              f"= {nexp:.1f} (cap 1e12, guard {guard}) -> "
              f"{'ACCEPTED (BAD)' if (height <= HEIGHT_CAP and nexp > guard) else 'rejected'}")
    return not accepted


def nffactor_degrees(nf, polystr):
    f = pari.nffactor(nf, pari(polystr))
    return sorted(int(pari.poldegree(f[0][i])) for i in range(len(f[0])))


def parabolic_translation(a, b, c, d, tol):
    """Translation length of a parabolic SL2 matrix after conjugating its fixed
    point to infinity (exact 2x2 algebra over pari; sign-of-lift insensitive)."""
    if pari.abs(c) < pari("1e-100"):
        return b / a
    p = (a - d) / (2 * c)
    S = ((pari(0), pari(1)), (pari(1), -p))       # z -> 1/(z-p) : p -> infinity
    Si = ((p, pari(1)), (pari(1), pari(0)))       # inverse (up to det -1 scalar)
    def mul(X, Y):
        return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
                (X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
    N = mul(mul(S, ((a, b), (c, d))), Si)
    assert pari.abs(N[1][0]) < tol                # conjugation sanity, precision-aware
    return N[0][1] / N[0][0]


def peripheral_shape(G, digits):
    """Cusp lattice modulus tau = (longitude translation)/(meridian translation)
    from a polished holonomy group (high precision, deterministic)."""
    tol = pari(f"1e-{digits - 25}")
    wm, wl = G.peripheral_curves()[0]
    def ent(mat):
        return (mat[0, 0].gen, mat[0, 1].gen, mat[1, 0].gen, mat[1, 1].gen)
    tm = parabolic_translation(*ent(G(wm)), tol)
    tl = parabolic_translation(*ent(G(wl)), tol)
    return tl / tm


print("=" * 78)
print("B749 / F3 -- THE SILVER SLOPE: the m=2 once-punctured-torus bundle R^2L^2")
print("=" * 78)
print(f"snappy {snappy.__version__}, sympy {sp.__version__}, mpmath {mpmath.__version__}")
print(f"precisions: polished holonomy/shapes at {BITS_LO} and {BITS_HI} bits; "
      f"pari 350 digits; mpmath {mpmath.mp.dps} dps")

# ---------------------------------------------------------------- S1 monodromy
print("\n--- S1: exact monodromy algebra (sympy, exact integer/symbolic) ---")
S = sp.Matrix([[2, 1], [1, 0]])
S2 = S * S
R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
assert S2 == sp.Matrix([[5, 2], [2, 1]])
assert S2 == R * R * L * L
assert S2.trace() == 6 == 2 ** 2 + 2          # B125's tr(M_m^2) = m^2 + 2 at m=2
assert S2.det() == 1
check("monodromy = [[2,1],[1,0]]^2 = [[5,2],[2,1]] = R^2L^2 (exact); tr = 6 = 2^2+2; det = +1")

lam = sp.Rational(3) + 2 * sp.sqrt(2)
ev = sorted(S2.eigenvals().keys(), key=sp.default_sort_key)
assert lam in ev
assert sp.simplify((1 + sp.sqrt(2)) ** 2 - lam) == 0
cf = sp.continued_fraction(1 + sp.sqrt(2))
assert cf == [[2]]                             # purely periodic: [2; 2,2,2,...]
charpoly = sp.expand((sp.symbols('x') - ev[0]) * (sp.symbols('x') - ev[1]))
assert charpoly == sp.symbols('x') ** 2 - 6 * sp.symbols('x') + 1
disc_dil = int(pari.nfdisc("x^2-6*x+1"))
assert disc_dil == 8
check("silver slope CF = [2;(2)] all-2s; dilatation = 3+2*sqrt(2) = (1+sqrt(2))^2; "
      "dilatation field = Q(sqrt2), nfdisc(x^2-6x+1) = 8")

# ------------------------------------------------------- S2 construction + H1
print("\n--- S2: construction, live bundle-string anchor, H1/knot-ness ---")
anchor = snappy.Manifold('b++RL')
m004 = snappy.Manifold('m004')
assert anchor.is_isometric_to(m004)
assert str(anchor.homology()) == "Z"
note(f"anchor b++RL: vol = {anchor.volume()}, H1 = {anchor.homology()}, "
     f"isometric to m004 = True")
check("bundle-string convention verified live: b++RL = m004 (isometric True; H1 = Z; "
      f"vol = {anchor.volume()})")

M = snappy.Manifold('b++RRLL')
from sympy.matrices.normalforms import smith_normal_form
AmI = S2 - sp.eye(2)
snf = smith_normal_form(AmI, domain=sp.ZZ)
assert snf == sp.diag(2, 2)
h1_snappy = str(M.homology())
assert h1_snappy == "Z/2 + Z/2 + Z"
check("H1(silver) = Z + Z/2 + Z/2  [snappy 'Z/2 + Z/2 + Z' == Wang: Z + coker(A-I), "
      "SNF(A-I) = diag(2,2) exact]")
check("knot-ness = NO (a knot complement in S^3 has H1 = Z by Alexander duality; "
      "silver H1 has (Z/2)^2 torsion)  [m004 control: H1 = Z]")

# ---------------------------------------------------- S3 identification (2+ inv)
print("\n--- S3: census identification by TWO+ independent invariants ---")
ident = M.identify()
note(f"identify() -> {ident}")
m136 = snappy.Manifold('m136')
iso1, iso2 = M.is_isometric_to(m136), m136.is_isometric_to(M)
volM, vol136 = snappy.ManifoldHP('b++RRLL').volume(), snappy.ManifoldHP('m136').volume()
voldiff = abs(pgen(volM) - pgen(vol136))
assert iso1 and iso2
assert voldiff < pari("1e-55")
assert str(m136.homology()) == h1_snappy
check(f"identification = m136 (invariant 1: is_isometric_to True both directions; "
      f"invariant 2: |vol diff| = {float(voldiff):.1e} < 1e-55; invariant 3: H1 equal)")

# ------------------------------------------------- S4 hyperbolicity + volume
print("\n--- S4: hyperbolicity + volume ---")
sol = M.solution_type()
assert sol == 'all tetrahedra positively oriented'
check(f"solution_type = '{sol}' (geometric solution; hyperbolic = YES)")

shapes_lo = polished_tetrahedra_shapes(snappy.Manifold('b++RRLL'), bits_prec=BITS_LO)
shapes_hi = polished_tetrahedra_shapes(snappy.Manifold('b++RRLL'), bits_prec=BITS_HI)
exact_shapes = [pari("1+I"), pari("(1+I)/2"), pari("1+I"), pari("I")]
for k, (zlo, zhi, ze) in enumerate(zip(shapes_lo, shapes_hi, exact_shapes)):
    dlo, dhi = abs(pgen(zlo) - ze), abs(pgen(zhi) - ze)
    assert dlo < pari("1e-190") and dhi < pari("1e-300"), (k, dlo, dhi)
note("polished shapes at 700/1100 bits match {1+i, (1+i)/2, 1+i, i} to < 1e-190 / < 1e-300")

# EXACT verification of ALL gluing + completeness equations over Q(i) (sympy):
Iu = sp.I
zs = [1 + Iu, sp.Rational(1, 2) + sp.Rational(1, 2) * Iu, 1 + Iu, Iu]
eqs = M.gluing_equations('rect')
for a_vec, b_vec, c in eqs:
    prod = sp.Integer(1)
    for z, a, b in zip(zs, a_vec, b_vec):
        prod *= z ** int(a) * (1 - z) ** int(b)
    assert sp.simplify(prod - c) == 0, (a_vec, b_vec, c)
assert all(sp.im(z) > 0 for z in zs)
check(f"shapes EXACT = {{1+i, (1+i)/2, 1+i, i}}; all {len(eqs)} gluing+completeness "
      "equations verified EXACTLY over Q(i) (sympy, Gaussian rationals); Im z > 0 all")

# volume: Bloch-Wigner on the EXACT shapes, mpmath 330 dps
def bloch_wigner(z):
    z = mpmath.mpc(z)
    return mpmath.im(mpmath.polylog(2, z)) + mpmath.arg(1 - z) * mpmath.log(abs(z))

vol_bw = sum(bloch_wigner(z) for z in [1 + 1j, 0.5 + 0.5j, 1 + 1j, 1j])
dcat = abs(vol_bw - 4 * mpmath.catalan)
assert dcat < mpmath.mpf(10) ** (-300)
assert abs(float(vol_bw) - M.volume()) < 1e-9
check(f"volume = {mpmath.nstr(vol_bw, 30)} = 4*Catalan exactly to < 1e-300 "
      "(Bloch-Wigner on exact shapes; snappy volume agrees)")

# --------------------------------------- S5 invariant trace field kM (2 routes)
print("\n--- S5: invariant trace field kM -- two independent routes ---")
# Route 1 (exact): shape field. Shapes are EXACTLY {1+i,(1+i)/2,1+i,i} (S4, exact
# gluing verification); z4 = i generates Q(i); all shapes lie in Q(i). By
# Neumann-Reid (cusped: shape field = invariant trace field), kM = Q(i).
disc_kM = int(pari.nfdisc("x^2+1"))
assert disc_kM == -4
note("route 1 (EXACT): shape field = Q(i) [generated by z4 = i; S4 exact]; "
     "Neumann-Reid => kM = Q(i); nfdisc(x^2+1) = -4 -> imaginary quadratic")

# Route 2 (numeric + nf confirmation): traces of squares (elements of Gamma^(2)).
G_lo = polished_holonomy(snappy.Manifold('b++RRLL'), bits_prec=BITS_LO, lift_to_SL2=False)
G_hi = polished_holonomy(snappy.Manifold('b++RRLL'), bits_prec=BITS_HI, lift_to_SL2=False)
assert G_hi.generators() == ['a', 'b', 'c']
for r in G_hi.relators():
    tr_rel = pgen(G_hi(r).trace())
    assert abs(tr_rel - 2) < pari("1e-300")      # relators -> +I : honest SL2 lift
note(f"relators {G_hi.relators()} map to +I (traces = 2): SL(2,C) lift verified")

def ptrace(G, word):
    return pgen(G(word).trace())

Ki = pari.nfinit("y^2+1")
sq_words = ['aa', 'bb', 'cc', 'abab', 'acac', 'bcbc', 'abcabc',
            'aabb', 'aacc', 'bbcc', 'aabbcc']
nonreal_seen = False
for w in sq_words:
    t_lo, t_hi = ptrace(G_lo, w), ptrace(G_hi, w)
    p_lo, _ = guarded_minpoly(t_lo, 8, DIG_LO, GUARD_LO, f"tr({w}) lo")
    p_hi, _ = guarded_minpoly(t_hi, 8, DIG_HI, GUARD_HI, f"tr({w}) hi")
    assert p_lo == p_hi, f"precision instability for tr({w})"
    assert int(pari.pollead(p_hi)) == 1          # monic: algebraic integer
    degs = nffactor_degrees(Ki, str(p_hi))
    assert degs[0] == 1, f"tr({w}) not in Q(i)"  # linear factor over Q(i)
    if abs(pari.imag(t_hi)) > pari("0.5"):
        nonreal_seen = True
assert nonreal_seen
check("kM = Q(i): route 1 shape field EXACT over Q(i) (Neumann-Reid) + route 2 all 11 "
      "traces of squares/square-products have monic Z-minpolys with a linear factor "
      "over Q(i) (nffactor), incl. non-real values; nfdisc = -4 (imaginary quadratic)")
check("kM(silver) = Q(i) (disc -4) != Q(sqrt-3) (disc -3) = kM(m004) -> the silver "
      "sibling is NOT commensurable with the figure-eight (kM is a commensurability "
      "invariant)")

# ------------------------------------------------ S6 trace field (Horowitz basis)
print("\n--- S6: trace field -- exact minpolys of tr(gamma), Horowitz basis ---")
basic = ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
minpolys = {}
all_monic = True
for w in basic:
    t_lo, t_hi = ptrace(G_lo, w), ptrace(G_hi, w)
    p_lo, _ = guarded_minpoly(t_lo, 8, DIG_LO, GUARD_LO, f"tr({w}) lo")
    p_hi, _ = guarded_minpoly(t_hi, 8, DIG_HI, GUARD_HI, f"tr({w}) hi")
    assert p_lo == p_hi, f"precision instability for tr({w})"
    minpolys[w] = p_hi
    if int(pari.pollead(p_hi)) != 1:
        all_monic = False
note("basic-trace minpolys: " + "; ".join(f"tr({w}): {minpolys[w]}" for w in basic))
assert all_monic
check("all 7 Horowitz-basis traces {a,b,c,ab,ac,bc,abc} have MONIC integer minpolys "
      "-> by Horowitz (Z-polynomial trace identities) EVERY trace of Gamma is an "
      "algebraic integer; minpolys: " +
      "; ".join(f"tr({w})={minpolys[w]}" for w in basic))

# the trace field = compositum of the basic-trace fields (exact, pari)
T = pari("x^2+1")
for w in basic:
    if int(pari.poldegree(minpolys[w])) == 1:
        continue
    comps = pari.polcompositum(T, minpolys[w])
    T = pari.polredbest(comps[len(comps) - 1])
T = pari.polredabs(T)
discT = int(pari.nfdisc(T))
assert str(T) == "x^8 + 6*x^4 + 1"
assert discT == 4194304 == 2 ** 22
KT = pari.nfinit("y^8+6*y^4+1")
for w in basic:
    degs = nffactor_degrees(KT, str(minpolys[w]).replace("y", "x"))
    assert degs == [1] * (len(degs)), f"tr({w}) minpoly does not split over T"
assert nffactor_degrees(KT, "x^2+1")[0] == 1      # kM inside T
check("trace field Q(tr Gamma) = octic x^8+6x^4+1 (polredabs), nfdisc = 2^22 = 4194304 "
      "(ramified ONLY at 2); every basic-trace minpoly splits into linear factors over "
      "it (nffactor); contains kM = Q(i)")

# ------------------------------------------------------------ S7 arithmeticity
print("\n--- S7: arithmeticity (Maclachlan-Reid non-cocompact criterion) ---")
# criterion (M-R Thm 8.3.2 as applied by B125): non-cocompact finite-covolume
# Kleinian group is arithmetic <=> kM imaginary quadratic AND all traces are
# algebraic integers. Both VERIFIED above (S5: kM = Q(i), disc -4; S6: monic).
check("ARITHMETIC = YES, verified not cited (kM = Q(i) imaginary quadratic [S5] + all "
      "traces algebraic integers [S6]; M-R non-cocompact criterion) -- B125's silver "
      "prediction independently reproduced; Bianchi class Q(i), distinct from m004's "
      "Q(sqrt-3) class")

# ------------------------------------------- S8 m004 control (same instruments)
print("\n--- S8: m004 control pipeline (the instruments DO see the banked anatomy) ---")
m004_shapes = polished_tetrahedra_shapes(snappy.Manifold('m004'), bits_prec=BITS_HI)
w3 = pari("(1+sqrt(-3))/2")
for z in m004_shapes:
    assert abs(pgen(z) - w3) < pari("1e-300")
zs4 = [sp.Rational(1, 2) + sp.sqrt(3) / 2 * sp.I] * 2
for a_vec, b_vec, c in m004.gluing_equations('rect'):
    prod = sp.Integer(1)
    for z, a, b in zip(zs4, a_vec, b_vec):
        prod *= z ** int(a) * (1 - z) ** int(b)
    assert sp.simplify(prod - c) == 0
G4 = polished_holonomy(snappy.Manifold('m004'), bits_prec=BITS_HI, lift_to_SL2=False)
t4 = ptrace(G4, 'a')
p4, _ = guarded_minpoly(t4, 8, DIG_HI, GUARD_HI, "m004 tr(a)")
assert int(pari.nfdisc(str(p4))) == -3
tau4 = peripheral_shape(G4, DIG_HI)
assert abs(tau4 + pari("2*sqrt(-3)")) < pari("1e-300")   # -2*sqrt(-3): longitude sign
pc4, _ = guarded_minpoly(tau4, 4, DIG_HI, GUARD_HI, "m004 cusp shape")
G4_lo = polished_holonomy(snappy.Manifold('m004'), bits_prec=BITS_LO, lift_to_SL2=False)
pc4_lo, _ = guarded_minpoly(peripheral_shape(G4_lo, DIG_LO), 4, DIG_LO, GUARD_LO,
                            "m004 cusp shape lo")
assert pc4 == pc4_lo                                     # cross-precision stability
assert str(pc4) == "x^2 + 12"
K3 = pari.nfinit("y^2+3")
assert nffactor_degrees(K3, str(pc4)) == [1, 1]
cusp4_hp = snappy.ManifoldHP('m004').cusp_info('shape')[0]
assert abs(pgen(cusp4_hp) - pari("2*sqrt(-3)")) < pari("1e-55")  # snappy convention: +
check("m004 CONTROL: shapes EXACT (1+sqrt(-3))/2 (gluing verified exactly over "
      f"Q(sqrt-3)); tr(a) minpoly {p4} -> nfdisc -3 (being face SEEN); cusp shape = "
      f"2*sqrt(-3) up to orientation (331-digit match; minpoly {pc4} splits linear "
      "over Q(sqrt-3)); H1 = Z (knot). The same instruments that find NOTHING at "
      "silver find the full banked anatomy at m004.")

# ------------------------------------------------------------- S9 the V4 faces
print("\n--- S9: which banked V4 faces survive at silver ---")
# being face Q(sqrt-3):
assert nffactor_degrees(Ki, "x^2+3") == [2]
assert nffactor_degrees(KT, "x^2+3") == [2]
check("being face Q(sqrt-3) = ABSENT (x^2+3 IRREDUCIBLE over kM = Q(i) AND over the "
      "full octic trace field; also forced: trace field disc = 2^22, 3 unramified); "
      "being-ANALOGUE present: kM = Q(i)")

# hearing face Q(sqrt5):
K2 = pari.nfinit("y^2-2")
assert nffactor_degrees(KT, "x^2-5") == [2]
assert nffactor_degrees(K2, "x^2-5") == [2]
check("hearing face Q(sqrt5) = ABSENT (x^2-5 IRREDUCIBLE over the octic trace field "
      "AND over the dilatation field Q(sqrt2)); hearing-ANALOGUE present: dilatation "
      "3+2*sqrt(2), field Q(sqrt2) disc 8")

# meeting face Q(sqrt-15):
assert nffactor_degrees(KT, "x^2+15") == [2]
assert str(minpolys['abc']) == "x^2 + 8"
comp = pari.polredabs(pari.polcompositum("x^2+1", "x^2-2")[0])
assert str(comp) == "x^4 + 1"
gal = pari.polgalois("x^4+1")
assert int(gal[0]) == 4 and int(gal[1]) == 1 and "E(4)" in str(gal[3])
sub_discs = sorted(int(pari.nfdisc(s[0])) for s in pari.nfsubfields("x^4+1")
                   if pari.poldegree(s[0]) == 2)
assert sub_discs == [-8, -4, 8]
check("meeting face Q(sqrt-15) = ABSENT (x^2+15 IRREDUCIBLE over the octic trace "
      "field); meeting-ANALOGUE present: Q(sqrt-2) -- realized as a trace, tr(abc) = "
      "+-2*sqrt(-2) (minpoly x^2+8); silver V4-analogue = Gal(Q(zeta8)/Q) = V4 "
      "[polgalois E(4)], subfield discs {-4, 8, -8} vs banked {-3, 5, -15}")
cls = {d: int(pari.qfbclassno(d)) for d in (-4, 8, -8, -3, 5, -15)}
note(f"context (NON-verdict-bearing): class numbers {cls} -- the object's meeting-face "
     "genus residue h(-15) = 2 (B698) has NO silver counterpart (h(-8) = 1)")

# interface / cusp:
assert M.num_cusps() == 1
tau = peripheral_shape(G_hi, DIG_HI)                       # 331-digit polished cusp modulus
assert abs(tau + pari("I/2")) < pari("1e-300")     # -i/2: longitude-orientation sign
cshape_hp = snappy.ManifoldHP('b++RRLL').cusp_info('shape')[0]
assert abs(pgen(cshape_hp) - pari("I/2")) < pari("1e-55")   # snappy convention: +i/2
pc, _ = guarded_minpoly(tau, 4, DIG_HI, GUARD_HI, "cusp shape")
pc_lo, _ = guarded_minpoly(peripheral_shape(G_lo, DIG_LO), 4, DIG_LO, GUARD_LO, "cusp shape lo")
assert pc == pc_lo                                          # cross-precision stability
assert str(pc) == "4*x^2 + 1"
assert nffactor_degrees(Ki, "4*x^2+1") == [1, 1]
check("interface = PRESENT/CARRIED (1 cusp; cusp shape = i/2 up to orientation "
      "[331-digit match; minpoly 4x^2+1, splits linear over kM = Q(i) via nffactor] "
      "-> cusp field inside kM, imaginary quadratic at the cusp; arithmetic "
      "Bianchi-Q(i) class; full V4-analogue quartet)")

# special prime of the being-field analogue:
ram = int(pari.factor(-disc_kM)[0][len(pari.factor(-disc_kM)[0]) - 1])
assert ram == 2                                   # -4 = -1 * 2^2 -> ramified prime 2
def sl2_facts(p):
    els = [(a, b, c, d) for a, b, c, d in itertools.product(range(p), repeat=4)
           if (a * d - b * c) % p == 1]
    def mul(m, n):
        a, b, c, d = m; e, f, g, h = n
        return ((a * e + b * g) % p, (a * f + b * h) % p,
                (c * e + d * g) % p, (c * f + d * h) % p)
    def inv(m):
        a, b, c, d = m
        return (d % p, (-b) % p, (-c) % p, a % p)
    I2 = (1, 0, 0, 1)
    center = [z for z in els if all(mul(z, x) == mul(x, z) for x in els)]
    invol = [x for x in els if x != I2 and mul(x, x) == I2]
    seen, ncl = set(), 0
    for x in els:
        if x in seen:
            continue
        ncl += 1
        for g in els:
            seen.add(mul(mul(g, x), inv(g)))
    return len(els), len(center), len(invol), ncl
o2, z2, i2, c2 = sl2_facts(2)
o3, z3, i3, c3 = sl2_facts(3)
assert (o2, z2, i2, c2) == (6, 1, 3, 3)
assert (o3, z3, i3, c3) == (24, 2, 1, 7)
check("special prime = ABSENT: ramified prime of kM(silver) = 2 (disc -4); "
      "SL(2,2) computed: order 6, center TRIVIAL, 3 non-central involutions, 3 classes "
      "-> no -I, so NOT a subgroup of SU(2) (every even-order subgroup of SU(2) "
      "contains central -1) -> NOT binary-polyhedral -> NO McKay/ADE node at 2. "
      "Control SL(2,3) computed: order 24, |Z| = 2 (-I), UNIQUE involution, 7 classes "
      "= 7 nodes of affine E6 -- the object's special prime 3 (2T -> E6, B718) has no "
      "silver analogue.")

# ----------------------------------------------------------- S10 sentinel (E20)
print("\n--- S10: non-vacuity sentinels for the algdep guard ---")
# Sentinel value: the volume 4*Catalan (no small-degree/small-height minpoly).
# The sentinels run at EXACTLY the configurations used for verdict-bearing algdeps:
#   (i) 331 digits, maxdeg 8, guard 230;  (ii) 331 digits, maxdeg 4, guard 230;
#   (iii) 210 digits, maxdeg 8, guard 140.
# INSTRUMENT-HARDENING RECORD (pre-verdict, sentinel-driven; both steps kept honest
# in this output): (1) a 63-digit ManifoldHP/deg-8/guard-40 configuration was beaten
# by the sentinel and REMOVED (all cusp shapes now come from 331-digit polished
# holonomy); (2) a residual-only guard was beaten at 331 digits by an LLL fake of
# height ~ 1e37 -- raw LLL residuals are ALWAYS ~ 10^-D; what separates true
# relations is coefficient HEIGHT (true: <= 52 here; fakes: ~ 10^(D/(deg+1))) plus
# cross-precision stability. Hence the acceptance = height cap 1e12 + normalized
# residual + lo/hi stability, and the sentinels below attack that full criterion.
cat_hi = pari("4*Catalan")                                   # at 350-digit precision
cat_lo = pari(f"precision(4*Catalan, {DIG_LO})")
assert sentinel_minpoly(cat_hi, 8, GUARD_HI, "4*Catalan, 331d, deg8")
assert sentinel_minpoly(cat_hi, 4, GUARD_HI, "4*Catalan, 331d, deg4")
assert sentinel_minpoly(cat_lo, 8, GUARD_LO, "4*Catalan, 210d, deg8")
check("sentinel: algdep on 4*Catalan is REJECTED by the full acceptance criterion "
      "(height cap 1e12 + normalized residual guard) in every configuration used for "
      "verdict-bearing claims (331d/deg8, 331d/deg4, 210d/deg8) -> instrument "
      "non-vacuous; two weaker configurations were sentinel-beaten and hardened "
      "BEFORE the verdict (record in S10 comments)")

# ---------------------------------------------------------------- S11 verdict
print("\n--- S11: verdict under the sealed criterion ---")
lacked = ["knot-ness (H1 = Z + (Z/2)^2 != Z)",
          "being-field analogue's special prime (ram prime 2; SL(2,2) not "
          "binary-polyhedral; no McKay/E6 analogue)"]
carried = ["interface structure (1 cusp; cusp field in kM = Q(i) imaginary quadratic; "
           "arithmetic; full V4-analogue {-4, 8, -8} = Gal(Q(zeta8)/Q))"]
print(f"  LACKED  ({len(lacked)}): " + " | ".join(lacked))
print(f"  CARRIED ({len(carried)}): " + " | ".join(carried))
assert len(lacked) >= 2
check("verdict tally: silver LACKS 2 of 3 {knot-ness, special prime} and CARRIES 1 of "
      "3 {interface}; sealed criterion 'ROBUST = lacks >= 2' -> VERDICT = ROBUST")
check("contra-prior flag: prereg expectation was 'F3 half-fragile'; ROBUST is "
      "contra-prior -> EXECUTION_NOTES rule 1 adversarial-skeptic trigger FLAGGED "
      "for the merge gate (the surviving half: arithmeticity + interface-analogue, "
      "exactly the prereg's 'arithmeticity survives' content)")

print("\n" + "=" * 78)
print("F3 VERDICT: ROBUST (earned: every absence is a theorem-grade or "
      "exactly-computed fact where m004 control shows presence)")
print("=" * 78)
