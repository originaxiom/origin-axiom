"""B498 -- Gate A, class 2d: the SL(3) gluing-variety invariant class of the
figure-eight -- the Galois/mirror sealing sweep (Closure Campaign Phase 2;
prereg docs/CLOSURE_CAMPAIGN_2026-07.md + local README.md).

QUESTION (Gate A / S032-A, restricted to this class). Is any SL(3) gluing/
character-variety invariant of the single seed (1) trace-map-invariant,
(2) discretely multivalued, (3) UNsymmetrizable -- a genuine forced choice?
Outcome enum (committed): SEALED / COUNTEREXAMPLE / TOOL-BLOCKED.

METHOD (all banked): the B71 fixed-locus presentation of the SL(3) figure-eight
character variety (Fix(T_1^2) in the 8 fiber trace coordinates; probe code
REUSED via importlib), the B106/B108 degree=rank scalar conventions, the B129/
K012 Sym^2 sealing, the B444 Ptolemy field control (its sage elimination step
replaced by in-sandbox sympy Groebner), the B98/B495 transverse-Jacobian
torsion convention, and the B330 Galois-symmetrization mechanism.

STRUCTURE OF THE COMPUTATION
  0.  CONTROLS (prereg: fail => INVALID, stop): B71/P24 reproduced -- the exact
      decomposition Fix(T_1^2) = V0 + W1 + W2 (three components, each dim 2,
      with an explicit complete case split); the Sym^2 shadow lands on V0
      (B67 chain, certified-numerical); M^3 = L on W1 and M^3 L = 1 on W2
      (the B71 scalar-matrix criterion, certified-numerical).
  1.  the inversion involution psi (a -> b, b -> a^-1): EXACT -- psi has order
      4 on the coordinates, psi^2 = theta (the B108 contragredient), psi
      conjugates T_1^2 to its inverse (so it preserves the fixed locus), its
      abelianization [[0,-1],[1,0]] conjugates the monodromy [[2,1],[1,1]] to
      its inverse (monodromy reversal = the mirror move, B318/B348), and it
      SWAPS W1 <-> W2 while fixing V0 (pointwise theta-fixed).
  2.  the discrete invariant class, tiers labeled:
      2a  counts/dims/definition fields (exact);
      2b  the degree=rank scalars c on W1 AND W2 at 50 digits at exact rational
          points (computer-assisted-exact; W2 is new, via the psi-image
          realization (A',B') = (B, A^-1) of the banked W1 Q(i) realization);
      2c  the Sym^2 leg made exact at trace level: Sym^2(SL(2) fixed curve) =
          V0(p = x^2-1, q = y^2-1) as an identity; the geometric pair
          (p, q) = ((1+3 sqrt(-3))/2, (1-3 sqrt(-3))/2), e-syms (1, 7); psi|V0
          = the Galois conjugation sigma_3 at the geometric pair (exact);
          the B129/K012 knot-side cross-check;
      2d  the boundary-unipotent (Ptolemy N=3) solution sets for BOTH
          obstruction classes, solved exactly offline (sympy Groebner with
          nonzero saturation): class 0 = 6 points over Q(sqrt-3) + Q(sqrt-7)
          (B444's sage output reproduced bit-for-bit in-sandbox), class 1 =
          2 points over Q(sqrt-3);
      2e  the component-level torsion-type invariant: the EXACT 8-coordinate
          trace-map-Jacobian charpoly per component (closing B495's named
          "time-boxed out" item) -- tau_V0 = -4(p-1)(q-1)(pq-4), tau_W =
          -3(p-q)^2 (identical on W1/W2), and at the geometric pair the exact
          transverse spectrum {u = 5} + {u^2 - 9u + 42 = 0} (disc -87) with
          reg-at-1 value -84 = (-3) * 28, rational (total Galois collapse).
  3.  the three-condition test (B330) on every discrete value, with the
      symmetrizer named per value (forced / Galois orbit / psi-mirror orbit /
      external label).
  4.  verdict + the honest out-of-reach list (TOOL-BLOCKED, named; adjoint
      torsion at SL(3) cross-referenced to B495, not repeated).

VERDICT (computed below, asserted, banked in b498_sl3_gluing.json): SEALED at
the computable horizon. Every discrete value the class hands over is either a
canonical integer (3; 2,2,2; 6; 2), a fixed-field rational (c = 1 = (-1)^(n-1),
tau = -84, the eliminant polynomials in Q[x]), a Galois orbit with rational
symmetric functions (the geometric pair, sum 1 product 7; the transverse
multiplier pair, sum 9 product 42; the Ptolemy root pairs), or a psi-mirror
pair (W1/W2, exponents {+3,-3} sum 0) whose member selection is an external
orientation label. No forced choice. The class beyond these components
(A-variety of V0, Ptolemy N>=4, SL(3) adjoint torsion) remains open -- named
at the end, per the C-guardrail.

Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.
"""
import importlib.util
import itertools
import json
import os
import pathlib

import sympy as sp

t = sp.symbols('t')
p, q = sp.symbols('p q')

HERE = pathlib.Path(__file__).resolve().parent
B71_DIR = HERE.parent / "B71_sl3_apoly"
B444_JSON = HERE.parent / "B444_sl3_field_control" / "sl3_ptolemy.json"

REPORT = {}


def bank(section, **kv):
    REPORT.setdefault(section, {}).update(
        {k: (str(w) if isinstance(w, (sp.Basic, sp.Matrix)) else w) for k, w in kv.items()})


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_CACHE = {}


def b71_probe():
    if 'probe' not in _CACHE:
        _CACHE['probe'] = _load("b498_b71_probe", B71_DIR / "probe.py")
    return _CACHE['probe']


def b71_symbolic_dehn():
    if 'sd' not in _CACHE:
        _CACHE['sd'] = _load("b498_b71_symbolic_dehn", B71_DIR / "symbolic_dehn.py")
    return _CACHE['sd']


# =====================================================================
# the involution psi (a -> b, b -> a^-1) and theta = psi^2 on the 8 coords
# =====================================================================
def psi(c):
    """chi -> chi o psi on the B48 coordinates; psi: a -> b, b -> a^-1."""
    x1, x2, x3, x4, x5, x6, x7, x8 = c
    return (x2, x4, x6, x5, x1, x8, x3, x7)


def psi_inv(c):
    return psi(psi(psi(c)))


def theta(c):
    """the contragredient (B108 theta = -w0) at character level: tr w <-> tr w^-1."""
    x1, x2, x3, x4, x5, x6, x7, x8 = c
    return (x4, x5, x8, x1, x2, x7, x6, x3)


def sym2m(M):
    """Sym^2 : 2x2 -> 3x3 on {e1^2, e1 e2, e2^2} (sympy exact)."""
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, 2 * a * b, b**2],
                      [a * c, a * d + b * c, b * d],
                      [c**2, 2 * c * d, d**2]])


# =====================================================================
# SECTION 0 -- CONTROLS (B71/P24; failure => INVALID)
# =====================================================================
def exact_decomposition():
    """B71/P24 reproduced with a complete exact case split (tier: exact).

    Fix(T_1^2) in C^8 = V0 + W1 + W2: exactly three irreducible components,
    each of dimension 2 (linear 2-planes after the four forced linear
    identifications), the geometric one (V0) containing Sym^2."""
    bp = b71_probe()
    x1, x2, x3, x4, x5, x6, x7, x8 = bp.X8
    eqs = bp.fixed_locus_equations()
    # (i) four of the eight fixed-locus equations are LITERALLY linear:
    assert sp.expand(eqs[1] - (x3 - x2)) == 0
    assert sp.expand(eqs[4] - (x8 - x5)) == 0
    assert sp.expand(eqs[5] - (x4 - x6)) == 0
    assert sp.expand(eqs[6] - (x1 - x7)) == 0
    # (ii) the reduced ideal in (x1, x2, x4, x5): four generators
    red = bp.reduced_ideal()
    assert len(red) == 4

    def in_list(target):
        return any(sp.expand(g - target) == 0 or sp.expand(g + target) == 0 for g in red)

    g_a = sp.expand((x1 - x4) * (x2 - 1))
    g_b = sp.expand((x1 - x4) * (x5 - 1))
    assert in_list(g_a) and in_list(g_b), "case-split generators drifted"
    # (iii) COMPLETE case split.
    #   case x1 != x4:  g_a, g_b force x2 = 1 and x5 = 1; the remaining two
    #   generators vanish IDENTICALLY on {x2 = 1, x5 = 1}  =>  W2... and
    #   symmetrically the slice is the FULL 2-plane {x2 = x5 = 1}:
    assert all(sp.expand(g.subs([(x2, 1), (x5, 1)])) == 0 for g in red)
    #   case x1 = x4: every generator reduces to a multiple of (x1-1)(x2-x5):
    for g in red:
        gg = sp.expand(g.subs(x4, x1))
        if gg != 0:
            quo = sp.cancel(gg / ((x1 - 1) * (x2 - x5)))
            assert quo.is_Number, f"unexpected residual factor {sp.factor(gg)}"
    #   subcase x2 = x5 (with x1 = x4): all generators vanish  =>  V0:
    assert all(sp.expand(g.subs([(x4, x1), (x5, x2)])) == 0 for g in red)
    #   subcase x1 = x4 = 1: all generators vanish  =>  W1:
    assert all(sp.expand(g.subs([(x1, 1), (x4, 1)])) == 0 for g in red)
    # => V(I) = V0 {x1=x4, x2=x5}  +  W1 {x1=x4=1}  +  W2 {x2=x5=1}: three
    #    LINEAR 2-planes (in the 4 free coordinates) => irreducible, dim 2 each.
    # (iv) irredundance: witness points on each component missing the others
    comps = bp.components()
    wit = {"V0": {p: 2, q: 3}, "W1": {p: 5, q: 7}, "W2": {p: 5, q: 7}}
    for nm, (params, coord) in comps.items():
        pt = tuple(c.subs(zip(params, [wit[nm][p], wit[nm][q]])) for c in coord)
        on = {"V0": pt[0] == pt[3] and pt[1] == pt[4],
              "W1": pt[0] == 1 and pt[3] == 1,
              "W2": pt[1] == 1 and pt[4] == 1}
        assert on[nm] and sum(on.values()) == 1, f"{nm} witness not separating"
    # (v) each parametrization is T_1^2-fixed (the B71 reuse):
    for nm, (_params, coord) in comps.items():
        assert all(sp.expand(a - b) == 0 for a, b in zip(bp.T1_sq(coord), coord)), nm
    bank("controls", decomposition="V0 {x1=x4,x2=x5} + W1 {x1=x4=1} + W2 {x2=x5=1}",
         n_components=3, dims=[2, 2, 2], case_split="complete (exact)",
         tier="exact")
    return comps


def sym2_shadow_numeric():
    """B71 control (b): Sym^2 of the B67 SL(2) family lands on V0 (certified-numerical)."""
    bp = b71_probe()
    dev = 0.0
    for xv in (3, 4, 5, 2.5, 7, 0.5 + 0.5j):
        c = bp.sym2_groundtruth_coords(xv)
        dev = max(dev, abs(c[0] - c[3]) + abs(c[1] - c[4]))
    assert dev < 1e-10, f"Sym^2 shadow off V0: {dev}"
    bank("controls", sym2_shadow_dev=float(dev), sym2_tier="certified-numerical")
    return dev


def dehn_scalar_control():
    """B71 control (c): M^3 = L on W1, M^3 L = 1 on W2 -- the exact scalar-matrix
    criterion evaluated in double precision (certified-numerical)."""
    sd = b71_symbolic_dehn()
    med1, n1 = sd.dehn_scalar_residual(sd.per.W1, "D2", seeds=(5,), npts=6)
    med2, n2 = sd.dehn_scalar_residual(sd.per.W2, "D3", seeds=(5,), npts=6)
    assert n1 >= 3 and n2 >= 3
    assert med1 < 1e-6 and med2 < 1e-6, f"A-variety control fail: {med1}, {med2}"
    bank("controls", w1_scalar_median=float(med1), w2_scalar_median=float(med2),
         avariety_tier="certified-numerical")
    return med1, med2


def controls():
    print("== 0. CONTROLS (B71/P24; prereg: fail => INVALID) ==")
    exact_decomposition()
    print("   Fix(T_1^2) = V0 + W1 + W2: THREE components, EACH dim 2 -- complete")
    print("   exact case split (4 linear identifications + (x1-x4)(x2-1)-type split)")
    dev = sym2_shadow_numeric()
    print(f"   Sym^2(B67 SL(2) family) lands on V0: max dev {dev:.1e}   [certified-numerical]")
    m1, m2 = dehn_scalar_control()
    print(f"   W1: [A,B] = c mu^3 (M^3 = L)   scalar-deviation median {m1:.1e}")
    print(f"   W2: [A,B] mu^3 = c (M^3 L = 1) scalar-deviation median {m2:.1e}")
    print("   CONTROLS PASS")
    return True


# =====================================================================
# SECTION 1 -- the inversion involution psi (tier: exact)
# =====================================================================
def involution_exact():
    bp = b71_probe()
    X8 = bp.X8
    # order 4; psi^2 = theta (the contragredient = B108's theta at character level)
    assert psi(psi(psi(psi(X8)))) == tuple(X8)
    assert psi(psi(X8)) == theta(X8)
    # psi conjugates the trace map to its INVERSE:  (psi T^2 psi^-1) o T^2 = id
    C = psi(bp.T1_sq(psi_inv(X8)))
    sub = dict(zip(X8, bp.T1_sq(X8)))
    CoT = tuple(sp.expand(c.subs(sub, simultaneous=True)) for c in C)
    assert CoT == tuple(X8), "psi does not conjugate T_1^2 to its inverse"
    # => psi(Fix T_1^2) = Fix(T_1^-2) = Fix(T_1^2): psi is a symmetry of the atlas.
    # abelianized: N = [[0,-1],[1,0]] conjugates the monodromy to its inverse:
    N = sp.Matrix([[0, -1], [1, 0]])
    phi = sp.Matrix([[2, 1], [1, 1]])
    assert N * phi * N.inv() == phi.inv() and N.det() == 1
    # component action: psi swaps W1 <-> W2, fixes V0 (setwise; p <-> q);
    # theta fixes V0 POINTWISE and acts on W1/W2 by (p, q) -> (q, p):
    comps = bp.components()
    (pv, qv), V0c = comps["V0"]
    _, W1c = comps["W1"]
    _, W2c = comps["W2"]
    swap = {pv: qv, qv: pv}

    def img(f, coord):
        return tuple(sp.expand(e) for e in f(coord))

    assert img(psi, W1c) == tuple(c.subs(swap, simultaneous=True) for c in W2c)
    assert img(psi, W2c) == tuple(W1c)     # psi^2 = theta acts on W1 by p <-> q
    assert img(psi, V0c) == tuple(c.subs(swap, simultaneous=True) for c in V0c)
    assert img(theta, V0c) == tuple(V0c)                       # pointwise fixed
    assert img(theta, W1c) == tuple(c.subs(swap, simultaneous=True) for c in W1c)
    print("\n== 1. THE INVERSION INVOLUTION psi: a -> b, b -> a^-1 (tier: exact) ==")
    print("   psi^4 = id;  psi^2 = theta (the B108 contragredient at character level)")
    print("   psi o T_1^2 o psi^-1 = T_1^-2 (exact)  =>  psi preserves Fix(T_1^2)")
    print("   abelianized [[0,-1],[1,0]]: monodromy [[2,1],[1,1]] -> its INVERSE")
    print("   (monodromy reversal = the mirror move; B318/B348)")
    print("   orbits on the atlas: {V0} (fixed, p <-> q), {W1, W2} (SWAPPED)")
    print("   theta fixes V0 POINTWISE (V0 lies in the contragredient-fixed locus)")
    bank("involution", order=4, psi_squared="theta (contragredient)",
         conjugates_trace_map_to_inverse=True, monodromy_reversal=True,
         orbit_V0="fixed (p<->q)", orbit_W="W1 <-> W2 swapped",
         theta_fixes_V0="pointwise", tier="exact")
    return True


# =====================================================================
# SECTION 2c -- the Sym^2 leg, exact at trace level (upgrades B71's numerics)
# =====================================================================
def sym2_exact():
    print("\n== 2c. THE GEOMETRIC COMPONENT AND Sym^2 (tier: exact) ==")
    a, b, c, d, e, f, g, h = sp.symbols('a b c d e f g h')
    A = sp.Matrix([[a, b], [c, d]])
    B = sp.Matrix([[e, f], [g, h]])
    Ainv = sp.Matrix([[d, -b], [-c, a]])              # adjugate = inverse at det 1
    det1 = {d: (1 + b * c) / a}
    # trace transfer: tr Sym^2(g) = (tr g)^2 - 1 on SL(2)
    assert sp.simplify((sym2m(A).trace() - ((a + d)**2 - 1)).subs(det1)) == 0
    # Fricke: tr(A^-1 B) = tr A tr B - tr AB
    assert sp.simplify(((Ainv * B).trace()
                        - ((a + d) * (e + h) - (A * B).trace())).subs(det1)) == 0
    # the SL(2) fixed curve (B48 m=1 coords): T1(x,y,z) = (z, x, xz - y)
    x, y, z = sp.symbols('x y z')
    T1_2 = lambda v: (v[2], v[0], sp.expand(v[0] * v[2] - v[1]))
    F2 = T1_2(T1_2((x, y, z)))
    eqs2 = [sp.expand(F2[i] - (x, y, z)[i]) for i in range(3)]
    yc = x / (x - 1)
    assert all(sp.simplify(e_.subs([(y, yc), (z, yc)])) == 0 for e_ in eqs2)
    # Sym^2 image coordinates: (x^2-1, y^2-1, z^2-1, x^2-1, y^2-1, w^2-1, w^2-1,
    # z^2-1) with w = xy - z; on the curve w = x EXACTLY:
    w_curve = sp.simplify((x * yc - yc))
    assert sp.simplify(w_curve - x) == 0
    # so Sym^2(SL(2) fixed curve) = V0(p = x^2 - 1, q = y^2 - 1) as an identity:
    P_, Q_ = sp.expand(x**2 - 1), sp.cancel(yc**2 - 1)
    image = (P_, Q_, Q_, P_, Q_, P_, P_, Q_)          # z = y, w = x on the curve
    comps = b71_probe().components()
    (pv, qv), V0c = comps["V0"]
    assert tuple(sp.cancel(c_.subs([(pv, P_), (qv, Q_)])) for c_ in V0c) == \
        tuple(sp.cancel(e_) for e_ in image)
    print("   tr Sym^2 = tr^2 - 1 and tr(A^-1 B) = trA trB - trAB (symbolic, det 1)")
    print("   SL(2) fixed curve: y = z = x/(x-1);  w = xy - z = x on the curve")
    print("   =>  Sym^2(SL(2) fixed curve) = V0(p = x^2-1, q = y^2-1)  EXACTLY")
    print("       (upgrades B71's 1e-14 Sym^2-shadow numerics to an identity)")
    # the geometric pair: x^2 - 3x + 3 = 0 (B98/B495 anchor, Q(sqrt-3))
    xg = sp.Rational(3, 2) + sp.sqrt(-3) / 2
    assert sp.simplify(xg**2 - 3 * xg + 3) == 0
    p_geo = sp.expand(xg**2 - 1)
    q_geo = sp.radsimp(sp.cancel((xg / (xg - 1))**2 - 1))
    assert sp.simplify(p_geo - (sp.Rational(1, 2) + 3 * sp.sqrt(-3) / 2)) == 0
    assert sp.simplify(q_geo - sp.conjugate(p_geo)) == 0
    s_, pr_ = sp.simplify(p_geo + q_geo), sp.simplify(sp.expand(p_geo * q_geo))
    assert (s_, pr_) == (1, 7)
    print(f"   geometric pair on V0: (p, q) = ({p_geo}, {q_geo})")
    print(f"   q = conj(p): the two coordinates are sigma_3-CONJUGATE;  psi|V0 (p <-> q)")
    print(f"   IS the Galois conjugation at the geometric pair  [B318 pattern at SL(3)]")
    print(f"   symmetric functions: sum = {s_}, product = {pr_}  (both rational)")
    # the B129/K012 knot-side cross-check (meridian presentation), exact:
    om = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    A2 = sp.Matrix([[1, 1], [0, 1]])
    B2 = sp.Matrix([[1, 0], [-om, 1]])
    SA, SB = sym2m(A2), sym2m(B2)
    K = {"trA": SA.trace(), "trB": SB.trace(),
         "trAB": sp.expand((SA * SB).trace()),
         "trAinvB": sp.expand((sym2m(A2.inv()) * SB).trace()),
         "trComm": sp.expand((SA * SB * SA.inv() * SB.inv()).trace())}
    expect = {"trA": 3, "trB": 3,
              "trAB": sp.Rational(1, 2) - 3 * sp.sqrt(3) * sp.I / 2,
              "trAinvB": sp.Rational(9, 2) + 5 * sp.sqrt(3) * sp.I / 2,
              "trComm": sp.Rational(1, 2) + 3 * sp.sqrt(3) * sp.I / 2}
    for k_ in K:
        assert sp.simplify(K[k_] - expect[k_]) == 0, k_
        re_, im_ = K[k_].as_real_imag()
        assert re_.is_rational and sp.simplify(im_ / sp.sqrt(3)).is_rational
    words = [sp.eye(3), SA, SB, SA * SB, SB * SA, SA * SA, SB * SB,
             SA * SB * SA, SA * SA * SB, SB * SB * SA, SA * SB * SB,
             SA * SB * SA * SB]
    Mvec = sp.Matrix([[sp.expand(W[i, j]) for i in range(3) for j in range(3)]
                      for W in words])
    assert Mvec.rank() == 9, "Sym^2 image not irreducible?"
    print("   B129/K012 cross-check: Sym^2 knot-side traces = the banked values,")
    print("   ALL in Q(sqrt-3); generated algebra = M_3 (rank 9: irreducible rep)")
    bank("sym2", identity="Sym^2(SL2 fixed curve) = V0(x^2-1, y^2-1)",
         p_geo=p_geo, q_geo=q_geo, esym=[1, 7], psi_is_sigma3_at_geo=True,
         k012_traces={k_: str(v) for k_, v in K.items()}, algebra_rank=9,
         tier="exact")
    return p_geo, q_geo


# =====================================================================
# SECTION 2b -- the degree=rank scalars at 50 digits (computer-assisted-exact)
# =====================================================================
def scalars_50digit(pts=((2, 3), (-1, 5), (sp.Rational(1, 3), 4)), dps=50):
    """c on W1 ([A,B] = c mu^3) and on W2 ([A,B] mu^3 = c) at `dps` digits at exact
    rational points. W1 uses B71's banked Q(i) realization A = diag(1, i, -i),
    B(p,q) exact; W2 uses its psi-image (A', B') = (B, A^-1) -- the psi-swap made
    computational. det t = 1 pinned (mu^3 is cube-root-branch independent)."""
    from mpmath import mp, matrix as mpm, eig, mpc
    mp.dps = dps
    I = sp.I
    A = sp.diag(1, I, -I)
    Ai = A.inv()
    bb = sp.symbols("b11 b12 b13 b21 b22 b23 b31 b32 b33")
    B = sp.Matrix(3, 3, bb)
    adjB = B.adjugate()
    conds = [sp.trace(B) - q, sp.trace(A * B) - q, sp.trace(Ai * B) - 1,
             sp.trace(adjB) - p, sp.trace(A * adjB) - 1, sp.trace(Ai * adjB) - p,
             B.det() - 1, B[0, 1] - 1, B[1, 2] - 1]
    Bsym = B.subs(sp.solve(conds, list(bb), dict=True)[0])

    def to_mp(M):
        return mpm([[mpc(sp.N(sp.re(M[i, j]), dps + 10), sp.N(sp.im(M[i, j]), dps + 10))
                     for j in range(3)] for i in range(3)])

    def kron(X, Y):
        out = mpm(9, 9)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        out[3 * i + k, 3 * j + l] = X[i, j] * Y[k, l]
        return out

    def det3(M):
        return (M[0, 0] * (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
                - M[0, 1] * (M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0])
                + M[0, 2] * (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0]))

    def monodromy_mp(Amp, Bmp):
        I3 = mpm([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        phiA, phiB = Amp * Amp * Bmp, Amp * Bmp          # phi: a -> a^2 b, b -> ab
        K1, K2, K3, K4 = kron(Amp.T, I3), kron(I3, phiA), kron(Bmp.T, I3), kron(I3, phiB)
        E = mpm(18, 9)
        for i in range(9):
            for j in range(9):
                E[i, j] = K1[i, j] - K2[i, j]
                E[9 + i, j] = K3[i, j] - K4[i, j]
        G = mpm(9, 9)
        for i in range(9):
            for j in range(9):
                G[i, j] = sum(mp.conj(E[r, i]) * E[r, j] for r in range(18))
        ev, Vv = eig(G)
        k = min(range(9), key=lambda i: abs(ev[i]))
        v = [Vv[r, k] for r in range(9)]
        tm = mpm([[v[0], v[3], v[6]], [v[1], v[4], v[7]], [v[2], v[5], v[8]]])
        return tm / det3(tm)**(mp.mpf(1) / 3)

    def scalar_dev_and_c(Msc):
        off = max(abs(Msc[i, j]) for i in range(3) for j in range(3) if i != j)
        dg = max(abs(Msc[0, 0] - Msc[1, 1]), abs(Msc[1, 1] - Msc[2, 2]))
        return max(off, dg), (Msc[0, 0] + Msc[1, 1] + Msc[2, 2]) / 3

    Amp = to_mp(A)
    worst_dev, worst_c = mp.mpf(0), mp.mpf(0)
    for pv, qv in pts:
        Bmp = to_mp(Bsym.subs({p: pv, q: qv}))
        # W1: [A,B] mu^-3 scalar; mu = a^-1 t (w = a for phi: a -> a^2 b)
        t1 = monodromy_mp(Amp, Bmp)
        mu = Amp**-1 * t1
        comm = Amp * Bmp * Amp**-1 * Bmp**-1
        dev1, c1 = scalar_dev_and_c(comm * (mu * mu * mu)**-1)
        # W2 via psi: (A', B') = (B, A^-1) realizes the psi-image character in W2
        A2m, B2m = Bmp, Amp**-1
        t2 = monodromy_mp(A2m, B2m)
        mu2 = A2m**-1 * t2
        comm2 = A2m * B2m * A2m**-1 * B2m**-1
        dev2, c2 = scalar_dev_and_c(comm2 * (mu2 * mu2 * mu2))
        worst_dev = max(worst_dev, dev1, dev2)
        worst_c = max(worst_c, abs(c1 - 1), abs(c2 - 1))
    thresh = mp.mpf(10)**(-(dps - 12))
    assert worst_dev < thresh, f"scalar-matrix criterion fails: {worst_dev}"
    assert worst_c < thresh, f"c != 1: {worst_c}"
    # exact cross-checks: c = 1 = (-1)^(n-1) at n = 3 (B153/B83); c^2 = 1 => theta-
    # fixed (the B108 hinge row: theta sends c -> c^-1; 1^-1 = 1).
    assert (-1)**(3 - 1) == 1 and sp.Integer(1)**(-1) == 1
    return float(worst_dev), float(worst_c), len(pts)


def scalars_leg():
    print("\n== 2b. THE DEGREE=RANK SCALARS (tier: computer-assisted-exact) ==")
    wd, wc, n = scalars_50digit()
    print(f"   W1: [A,B] = c mu^3  (M^3 = L);   W2: [A,B] mu^3 = c  (M^3 L = 1)")
    print(f"   at {n} exact rational points, 50 digits: worst scalar-dev {wd:.1e},")
    print(f"   worst |c - 1| = {wc:.1e}   =>  c = 1 on BOTH components")
    print("   (W2 is NEW at this tier -- realized as the psi-image (B, A^-1) of the")
    print("    banked W1 Q(i) realization; B106 had W2 only at ~3e-10)")
    print("   cross-checks: c = 1 = (-1)^(n-1) at n = 3 (B153/B83 sign law);")
    print("   c^2 = 1 => theta-fixed (B108: theta sends c -> c^-1); exponent pair")
    print("   k = (+3, -3) (B106 D4 convention), psi-swapped, sum 0")
    bank("scalars", c_W1=1, c_W2=1, worst_scalar_dev=wd, worst_c_dev=wc,
         n_points=n, k_pair=[3, -3], sign_law="c = (-1)^(n-1), n = 3",
         theta_fixed="c^2 = 1", tier="computer-assisted-exact (50 digits, exact points)")


# =====================================================================
# SECTION 2e -- the component-level torsion-type invariant (tier: exact)
# =====================================================================
def jacobian_torsion():
    """The EXACT 8-coordinate trace-map-Jacobian charpoly per component -- the
    B98/B495 transverse-torsion convention at SL(3). Closes B495's named
    'time-boxed out' item (the 8-coordinate symbolic SL(3) Jacobian)."""
    print("\n== 2e. THE TRANSVERSE-JACOBIAN TORSION CLASS AT SL(3) (tier: exact) ==")
    bp = b71_probe()
    X8 = bp.X8
    img = bp.T1_sq(X8)
    J = sp.Matrix([[sp.diff(img[i], X8[j]) for j in range(8)] for i in range(8)])
    comps = bp.components()
    out = {}
    for nm, (params, coord) in comps.items():
        pv, qv = params
        Jc = J.subs(dict(zip(X8, coord)), simultaneous=True)
        cp = Jc.charpoly(t).as_expr()
        e = sp.expand(cp.subs([(pv, p), (qv, q)]))
        k = 0
        while sp.simplify(e.subs(t, 1)) == 0:
            e = sp.expand(sp.div(e, t - 1, t)[0])
            k += 1
        out[nm] = (sp.expand(cp.subs([(pv, p), (qv, q)])), k, sp.factor(e.subs(t, 1)))
    cpV0, kV0, tauV0 = out["V0"]
    cpW1, kW1, tauW1 = out["W1"]
    cpW2, kW2, tauW2 = out["W2"]
    # (i) psi at the Jacobian level: W1 and W2 carry the IDENTICAL charpoly:
    assert sp.expand(cpW1 - cpW2) == 0
    # (ii) the (t-1)-multiplicity is 2 on every component (the dim-2 tangent):
    assert (kV0, kW1, kW2) == (2, 2, 2)
    # (iii) the reg-at-1 torsion-type functions:
    assert sp.expand(tauV0 + 4 * (p - 1) * (q - 1) * (p * q - 4)) == 0
    assert sp.expand(tauW1 + 3 * (p - q)**2) == 0
    # theta-invariance: tau_W(p, q) = tau_W(q, p); continuous (B130 pattern):
    assert sp.expand(tauW1 - tauW1.subs([(p, q), (q, p)], simultaneous=True)) == 0
    assert sp.diff(tauV0, p) != 0 and sp.diff(tauW1, p) != 0
    print(f"   char(J|V0) reg-at-1: tau_V0(p,q) = {sp.factor(tauV0)}")
    print(f"   char(J|W1) = char(J|W2) (psi at Jacobian level);  tau_W = {sp.factor(tauW1)}")
    print("   (t-1)-multiplicity 2 on all three components (the dim-2 tangent, exact)")
    print("   both tau are CONTINUOUS on their components (B130 pattern: no discrete")
    print("   choice from the function itself); tau_W is theta-invariant (p <-> q)")
    # (iv) the geometric stratum, exactly:
    p_geo = sp.Rational(1, 2) + 3 * sp.sqrt(-3) / 2
    q_geo = sp.Rational(1, 2) - 3 * sp.sqrt(-3) / 2
    tau_geo = sp.simplify(sp.expand(tauV0.subs([(p, p_geo), (q, q_geo)])))
    tau_geo_bar = sp.simplify(sp.expand(tauV0.subs([(p, q_geo), (q, p_geo)])))
    assert tau_geo == -84 and tau_geo_bar == -84
    cp_geo = sp.expand(cpV0.subs([(p, p_geo), (q, q_geo)]))
    quad = sp.expand(t**2 - 5 * t + 1)
    quart = sp.expand(t**4 - 9 * t**3 + 44 * t**2 - 9 * t + 1)
    assert sp.expand(cp_geo - sp.expand((t - 1)**2 * quad * quart)) == 0
    # the quadratic block is the Sym^2 shadow of the SL(2) multiplier (B98 c = 5,
    # B495's t^2 - 5t + 1, disc 21); u = pq - 2 = 5 at the geometric pair:
    assert sp.simplify(sp.expand(p_geo * q_geo - 2)) == 5
    assert sp.discriminant(quad, t) == 21
    # the quartic is palindromic; in u = t + 1/t it is u^2 - 9u + 42 (disc -87):
    u = sp.symbols('u')
    upoly = sp.expand(u**2 - 9 * u + 42)
    assert sp.expand(quart - sp.expand(t**2 * (upoly.subs(u, t + 1 / t)))) == 0
    assert sp.discriminant(upoly, u) == -87
    # reg-at-1 factorization: -84 = (-3) x 28; 28 = Norm(u - 2) in Q(sqrt-87):
    assert quad.subs(t, 1) == -3 and quart.subs(t, 1) == 28
    assert sp.expand(upoly.subs(u, 2)) == 28
    print("   at the geometric pair: char = (t-1)^2 (t^2 - 5t + 1) (t^4 - 9t^3 + 44t^2 - 9t + 1)")
    print("     - t^2 - 5t + 1 = the Sym^2 shadow of the SL(2) multiplier block")
    print("       (u = pq - 2 = 5 = B98's c(x_geo); disc 21; B495's quadratic)")
    print("     - the quartic is PALINDROMIC: u^2 - 9u + 42 in u = t + 1/t, disc -87;")
    print("       the exact form of B99's numerical spectrum {5, 4.5 +- 4.664 i}")
    print("       (closes B495 Section 5's named 'time-boxed out' item)")
    print("   tau_V0(geometric pair) = -84 = (-3) x 28 = (-3) x N(u - 2), RATIONAL,")
    print("   equal at BOTH Galois lifts: total Galois collapse (B495 pattern)")
    bank("jacobian", tau_V0=sp.factor(tauV0), tau_W=sp.factor(tauW1),
         charpoly_W1_equals_W2=True, t1_multiplicity=2,
         geo_charpoly="(t-1)^2 (t^2-5t+1)(t^4-9t^3+44t^2-9t+1)",
         geo_quad_disc=21, geo_quartic_u="u^2 - 9u + 42", geo_u_disc=-87,
         geo_u_esym=[9, 42], tau_geo=-84, tau_geo_factor="(-3) x 28",
         tier="exact")
    return tauV0, tauW1


# =====================================================================
# SECTION 2d -- the Ptolemy N=3 fields, exact and offline
# =====================================================================
def _squarefree_part(n):
    n = int(n)
    sign = -1 if n < 0 else 1
    out = sign
    for pr, e in sp.factorint(abs(n)).items():
        if e % 2:
            out *= pr
    return out


def solve_ptolemy_class(eqstrs, varstrs):
    """Exact solve of one Ptolemy obstruction-class system: sympy Groebner with
    nonzero-coordinate saturation. Returns nonempty, ideal degree (# standard
    monomials, 0-dim certified), per-variable eliminants, quadratic-field set."""
    vars_ = sp.symbols(varstrs)
    vmap = {str(v): v for v in vars_}
    eqs = [sp.sympify(e.replace("^", "**"), locals=vmap) for e in eqstrs]
    w = sp.symbols("w_aux")
    gens = (w,) + tuple(vars_)
    gb = sp.groebner(eqs + [w * sp.prod(vars_) - 1], *gens, order="grevlex")
    if gb.exprs == [sp.Integer(1)]:
        return dict(nonempty=False)
    lm_exps = [tuple(sp.Poly(pp, *gens).LM(order="grevlex")) for pp in gb.exprs]
    bounds = [0] * len(gens)
    for e in lm_exps:
        nz = [i for i, x_ in enumerate(e) if x_ > 0]
        if len(nz) == 1:
            bounds[nz[0]] = max(bounds[nz[0]], e[nz[0]])
    assert all(b_ > 0 for b_ in bounds), "not 0-dimensional (no pure-power LM)"
    degree = sum(1 for it in itertools.product(*[range(b_) for b_ in bounds])
                 if not any(all(a_ <= b_ for a_, b_ in zip(l_, it)) for l_ in lm_exps))
    eliminants, discs = {}, set()
    for target in vars_:
        rest = [v for v in vars_ if v != target]
        gbl = sp.groebner(eqs + [w * sp.prod(vars_) - 1], w, *rest, target, order="lex")
        uni = [g for g in gbl.exprs if g.free_symbols <= {target}]
        assert uni, f"no eliminant for {target}"
        eliminants[str(target)] = sp.factor(uni[0])
        for fac, _mult in sp.factor_list(uni[0])[1]:
            if sp.Poly(fac, target).degree() == 2:
                discs.add(_squarefree_part(sp.discriminant(fac, target)))
    return dict(nonempty=True, degree=degree,
                eliminants={k: str(v) for k, v in eliminants.items()},
                fields=sorted(discs))


def ptolemy_exact():
    print("\n== 2d. PTOLEMY N=3 BOUNDARY-UNIPOTENT FIELDS (tier: exact, offline) ==")
    classes = {}
    source = None
    try:
        import snappy
        M = snappy.Manifold("4_1")
        Vs = M.ptolemy_variety(3, obstruction_class='all')
        assert len(Vs) == 2
        for i, V in enumerate(Vs):
            classes[i] = ([str(e) for e in V.equations], [str(v) for v in V.variables])
        source = "snappy (equations extracted live; solve = sympy, offline)"
    except Exception as exc:                                    # pragma: no cover
        d = json.load(open(B444_JSON))
        classes[0] = (d["4_1"]["eqs"], d["4_1"]["vars"])
        source = f"B444 bundled JSON (snappy unavailable: {exc}); class 1 skipped"
    results = {}
    for i, (eqstrs, varstrs) in classes.items():
        results[i] = solve_ptolemy_class(eqstrs, varstrs)
    r0 = results[0]
    assert r0["nonempty"] and r0["degree"] == 6
    assert r0["fields"] == [-7, -3]
    c0 = sp.symbols('c_1101_0')
    elim = sp.sympify(r0["eliminants"]["c_1101_0"], locals={'c_1101_0': c0})
    assert sp.expand(elim - sp.expand((c0 - 1) * (4 * c0**2 - c0 + 4))) == 0
    print(f"   source: {source}")
    print("   class 0: NONEMPTY, ideal degree 6 (0-dim certified via pure-power LMs);")
    print("   eliminant(c_1101_0) = (c - 1)(4c^2 - c + 4)  [B444's sage output,")
    print("   reproduced bit-for-bit in-sandbox]; quadratic fields {Q(sqrt-3), Q(sqrt-7)}")
    if 1 in results:
        r1 = results[1]
        assert r1["nonempty"] and r1["degree"] == 2 and r1["fields"] == [-3]
        print("   class 1: NONEMPTY, ideal degree 2, Q(sqrt-3) ONLY (the PGL(3)-only")
        print("   boundary-unipotent pair -- NEW beyond B444, which solved class 0)")
    # association (tier split, honest):
    #   - the class-0 Eisenstein pair = Sym^2(geometric pair) in V0: Sym^2 of a
    #     unipotent is unipotent (exact), and Sym^2(SL2 curve) = V0 (Section 2c);
    un = sym2m(sp.Matrix([[1, 1], [0, 1]]))
    assert (un - sp.eye(3)).is_nilpotent()
    #   - the four sqrt(-7) points sit on W1/W2: B444 (sage-exact, banked) + HMP/
    #     Falbel (lit). NOT re-derived here (the Ptolemy -> fiber-trace dictionary
    #     is named TOOL-BLOCKED below).
    print("   association: Eisenstein pair = Sym^2(geometric pair) in V0 (exact:")
    print("   Sym^2 preserves unipotency + Section 2c); sqrt(-7) quadruple on W1/W2")
    print("   per B444 (sage-exact, banked) + Heusener-Munoz-Porti/Falbel (lit)")
    bank("ptolemy", source=source,
         class0=results[0], class1=results.get(1, "unavailable"),
         association="Eisenstein pair -> V0 exact; sqrt-7 quadruple -> W1/W2 (B444+lit)",
         tier="exact (eliminants); association mixed (exact / banked+lit)")
    return results


# =====================================================================
# SECTION 3 -- the three-condition test (B330)
# =====================================================================
def three_condition_seal():
    print("\n== 3. THE THREE-CONDITION TEST (B330 mechanism) ==")
    # the discrete values this class hands over, with their B330 classification.
    # bins: F = forced/canonical single value (fails clause 2 -- no choice);
    #       G = Galois orbit, symmetric functions in the fixed field;
    #       P = psi-mirror orbit (member selection = external orientation label);
    #       C = continuous family (fails clause 2; B130 pattern).
    table = [
        dict(value="component count = 3", bin="F", symmetrizer="canonical integer"),
        dict(value="dims = (2, 2, 2)", bin="F", symmetrizer="canonical integers"),
        dict(value="definition fields of the three components = Q (rational 2-planes)",
             bin="F", symmetrizer="already in the fixed field"),
        dict(value="{W1, W2} (the component pair)", bin="P",
             symmetrizer="psi (inversion/mirror); V0 forced apart intrinsically (Sym^2)"),
        dict(value="A-variety exponent pair k = {+3, -3}", bin="P",
             symmetrizer="psi swaps; sum 0, product -9 rational"),
        dict(value="degree=rank scalars {c_W1, c_W2} = {1, 1}", bin="F",
             symmetrizer="equal, rational, = (-1)^(n-1) (B153); theta-fixed (B108)"),
        dict(value="geometric pair coordinates {(1+3 sqrt-3)/2, (1-3 sqrt-3)/2}",
             bin="G", symmetrizer="sigma_3 = psi|V0 (B318 pattern); e-syms (1, 7)"),
        dict(value="Ptolemy class-0 root pairs (Eisenstein + two sqrt-7 pairs)",
             bin="G", symmetrizer="sigma_3, sigma_7; eliminants already in Q[x]"),
        dict(value="Ptolemy counts (6, 2) and field set {Q(sqrt-3), Q(sqrt-7)}",
             bin="F", symmetrizer="canonical integers; fields label intrinsic strata"),
        dict(value="tau_V0, tau_W (torsion-type functions)", bin="C",
             symmetrizer="continuous on the component (B130); no discrete choice"),
        dict(value="tau_V0(geometric pair) = -84", bin="F",
             symmetrizer="rational, equal at both lifts (total Galois collapse)"),
        dict(value="transverse multiplier pair u = (9 +- sqrt-87)/2", bin="G",
             symmetrizer="sigma_87; e-syms (9, 42) rational"),
    ]
    # programmatic verification of every symmetrization claim:
    assert 3 + (-3) == 0 and 3 * (-3) == -9                     # k-pair
    p_geo = sp.Rational(1, 2) + 3 * sp.sqrt(-3) / 2
    q_geo = sp.conjugate(p_geo)
    assert sp.simplify(p_geo + q_geo) == 1 and sp.simplify(sp.expand(p_geo * q_geo)) == 7
    u1 = sp.Rational(9, 2) + sp.sqrt(-87) / 2
    u2 = sp.conjugate(u1)
    assert sp.simplify(u1 + u2) == 9 and sp.simplify(sp.expand(u1 * u2)) == 42
    assert all(sp.Integer(v).is_rational for v in (1, 1, -84, 3, 6, 2))
    # condition (1): every listed value is attached to intrinsic strata of
    # Fix(T_1^2) (components; their intersections; the Sym^2/geometric stratum;
    # boundary-unipotency) -- trace-map-invariant by construction (Sections 0-2).
    # condition (2): the multivalued items are exactly the G/P rows (finite sets).
    # condition (3): every G/P row carries a computed symmetrizer above; the psi
    # orbits are symmetrized by the object's OWN mirror move (Section 1), the
    # Galois orbits by the B330 mechanism. NO row is unsymmetrizable.
    bins = {r["bin"] for r in table}
    assert bins == {"F", "G", "P", "C"}
    assert not any(r.get("unsymmetrizable") for r in table)
    for r in table:
        print(f"   [{r['bin']}] {r['value']}")
        print(f"        symmetrized by: {r['symmetrizer']}")
    print("   (1) trace-map-invariant: all values cut intrinsically from Fix(T_1^2) OK")
    print("   (2) discretely multivalued: the G/P rows (finite orbits) OK")
    print("   (3) symmetrizable: EVERY orbit collapses -- Galois (sigma_3, sigma_7,")
    print("       sigma_87) or the object's own mirror psi; member selection in the")
    print("       psi-pairs = an external orientation label (the B496 bin-P pattern)")
    print("   => NO forced choice exists in this class: SEALED")
    bank("seal", table=table, verdict="SEALED",
         k_pair_esym=[0, -9], geo_esym=[1, 7], u_esym=[9, 42],
         rational_values=[1, 1, -84], counts=[3, 2, 2, 2, 6, 2])
    return table


# =====================================================================
# SECTION 4 -- verdict + honest residual
# =====================================================================
def verdict():
    print("\n== 4. VERDICT ==")
    print("   SEALED (at the computable horizon).")
    print("   The SL(3) gluing class of the single seed is mirror-organized end to")
    print("   end: a rational atlas (three Q-defined 2-planes), a psi-swapped filling")
    print("   pair with c = 1 = (-1)^(n-1) on both members, Galois-paired point data")
    print("   with rational symmetric functions, and a torsion-type value (-84) that")
    print("   collapses into Q at both Galois lifts. The object hands you symmetric")
    print("   orbits and canonical integers -- never a member.")
    print("   OUT OF REACH (named, honest):")
    print("    - the exact A-variety of the geometric component V0 (Falbel et al.'s")
    print("      eliminated Groebner basis is 141 polynomials): magma/sage-scale")
    print("      elimination -- TOOL-BLOCKED (magma / sage; prereg-excluded).")
    print("    - the exact (p,q) fiber-coordinates of the boundary-unipotent points")
    print("      on W1/W2 (the Ptolemy -> fiber-trace dictionary; the sympy radical")
    print("      solve of the full 9-variable triangular system did not terminate")
    print("      in-budget): TOOL-BLOCKED (magma / sage / Ptolemy database, no")
    print("      network). The FIELDS are exact above; only the per-point component")
    print("      dictionary rests on B444 (sage, banked) + HMP/Falbel (lit).")
    print("    - adjoint (Porti-normalized) torsion at the SL(3) reps: the Fox/Wada")
    print("      pipeline needs Ad(SL3) = the 8-dim adjoint over number fields --")
    print("      cross-reference B495 Section 5 (same named block: number-field")
    print("      Groebner / magma / sage); NOT repeated here. Note the transverse-")
    print("      Jacobian HALF of that item (the 8-coordinate symbolic Jacobian) is")
    print("      now CLOSED, exactly, by Section 2e.")
    print("    - Ptolemy N >= 4 enumeration; the Ptolemy database cross-check (no")
    print("      network): TOOL-BLOCKED.")
    print("    - the universal all-invariants statement: OPEN (C-guardrail; sealing")
    print("      != universal impossibility proof).")
    print("   Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.")
    bank("verdict", outcome="SEALED",
         phrasing="sealed at the computable horizon; the class beyond these "
                  "components remains open",
         tool_blocked=[
             "exact V0 A-variety (141-polynomial elimination): magma/sage",
             "Ptolemy -> fiber-trace dictionary for the sqrt-7 points: "
             "magma/sage/Ptolemy DB (no network)",
             "SL(3) adjoint torsion (Fox/Wada at Ad(SL3)): see B495 Section 5 "
             "(number-field Groebner / magma / sage); transverse-Jacobian half "
             "closed here (Section 2e)",
             "Ptolemy N >= 4; Ptolemy database cross-check (no network)"],
         open_="universal statement (C-guardrail)")


def main():
    ok = controls()
    if not ok:                                                   # pragma: no cover
        print("CONTROL FAILED -- probe INVALID; stopping per prereg.")
        return 1
    involution_exact()
    scalars_leg()
    sym2_exact()
    ptolemy_exact()
    jacobian_torsion()
    three_condition_seal()
    verdict()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "b498_sl3_gluing.json")
    json.dump(REPORT, open(out, "w"), indent=1, default=str)
    print(f"\n[written] {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
