"""B496 -- Gate A, class 2b: the Chern-Simons / eta class of the figure-eight beyond
the banked CS = 0 -- the Galois/mirror-orbit sealing sweep (Closure Campaign Phase 2;
prereg docs/CLOSURE_CAMPAIGN_2026-07.md + local README.md).

QUESTION (Gate A / S032-A, restricted to this class). Is any CS-type invariant of the
single seed (1) trace-map-invariant, (2) discretely multivalued, (3) UNsymmetrizable --
a genuine forced choice? Outcome enum (committed): SEALED / COUNTEREXAMPLE / TOOL-BLOCKED.

METHOD (all banked): the B330 Galois-symmetrization mechanism; the B348 {+beta, -beta}
self-symmetrization with amphichirality killing the orientation sign; B151's lattice
statement (complex volume in C/4pi^2 Z, SL2; SnapPy normalization cs = CS/(2 pi^2),
defined mod 1/2 cusped / mod 1 closed, complex_volume mod i pi^2); B127's K-A metallic
CS = 0 computation (reused shape); B489's cyclic-cover tower (H1 torsion |L(2n)-2|);
B432's filling-chirality sample + CS-initialization method; B434's forced +-5 slope and
the Meyerhoff child.

TIER HONESTY (stated up front, unlike the all-exact B495): CS is an analytic invariant;
SnapPy gives certified-NUMERICAL values (double + quad-double ManifoldHP + SnapPea's
accuracy estimate). Two upgrades to EXACT are available in-sandbox and used:
  * the 2-torsion elimination: orientation reversal negates cs (the classical fact:
    the Chern-Simons functional is orientation-odd), so an AMPHICHIRAL manifold has
    2 cs = 0, i.e. cs in the finite set {0, 1/4} (cusped, mod 1/2) / {0, 1/2} (closed,
    mod 1); a machine-zero (or machine-1/4) numeric then pins the exact member, because
    the alternative is at distance 1/4 >> every error bound. Amphichirality itself is
    a combinatorial certificate (canonical-cell symmetry group, full + amphicheiral).
  * exact rational recognition at the flat (Seifert) fillings, residuals < 1e-12.
Everything else (the chiral child pair, the generic B432 sample) stays certified
numerical and is labeled so. sage/magma are excluded by prereg: the verified-interval
tier (complex_volume(verified_modulo_2_torsion=True)) is named TOOL-BLOCKED, as are
eta (no SnapPy API -- checked, not skipped silently), the exact number-field CS of the
chiral fillings (extended-Ptolemy/GTZ needs the Ptolemy DB or sage/magma), and the
graph-manifold CS/eta at the toroidal slopes +-4.

STRUCTURE OF THE COMPUTATION
  A.  exact arithmetic (sympy/mpmath, no SnapPy): the 2-torsion fixed-point sets;
      the Lucas torsion law |det(A^n - I)| = |L(2n) - 2| for the cover tower (B489);
      the child trace-field quartic x^4 - x - 1 (disc -283, S4, no quadratic
      subfield -- B434); the independent dilogarithm volume anchor 2 Im Li2(e^{i pi/3}).
  0.  CONTROLS (prereg: fail => INVALID, stop): cs(4_1) = 0 exactly (HP machine zero;
      complex volume = Vol + 0 i; GTZ form c_hat = i(Vol + i CS) = i 2.0298...);
      the sister m003 cs = 1/4 (P9); the metallic family cs == 0 for m = 1..6 (the
      B127 K-A computation) against the census mix control (m003, m004, m006).
  1.  the cusped strata (seed, sister, metallic m = 1..6, cyclic covers n = 1..5, 8):
      presentation invariance, amphichirality certificates, and the 2-torsion
      elimination => EXACT values {0 x 13, 1/4}.
  2.  the filling interface: the exceptional set {0, +-1, +-2, +-3} (flat: exact
      rationals 0, +-1/84, +-1/40, +-1/24), the toroidal wall +-4 (CS undefined,
      raises -- recorded), the forced child pair 4_1(+-5, 1) = Meyerhoff +- mirror
      (cs = +-0.07703818026377..., sum 0 mod 1, chiral by TWO certificates), and the
      eta exposure scan (negative => TOOL-BLOCKED, named).
  3.  the mirror-pairing law on the whole banked B432 sample: cs(p,-q) = -cs(p,q)
      mod 1, 31/31, and the banked values match 31/31.
  4.  the three conditions + the seal: every value mirror-FIXED (2-torsion, forced by
      amphichirality), a mirror +- PAIR with sum 0 (the B348 {+beta,-beta} pattern;
      member = orientation/slope-sign = external input), or an input-LABELED generic
      value still obeying the pairing law. No clause-(3) forced choice.

VERDICT (computed below, asserted, banked in b496_cs_eta.json): SEALED at the
computable horizon; the class beyond these strata (eta, exact chiral CS, toroidal
graph pieces, the universal statement) remains open -- named, per the C-guardrail.

Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.
"""
import json
import math
import os
from fractions import Fraction

import mpmath as mp
import sympy as sp

try:
    import snappy
    HAVE_SNAPPY = True
except Exception:                                                # pragma: no cover
    snappy = None
    HAVE_SNAPPY = False

MACHINE = 1e-12          # double-precision machine-zero bar (observed <= 4e-15)
HP_ZERO = 1e-50          # quad-double machine-zero bar (observed <= 7e-64)
NUM = 1e-9               # certified-numerical agreement bar
REPORT = {}


def bank(section, **kv):
    REPORT.setdefault(section, {}).update(
        {k: (str(w) if isinstance(w, (sp.Basic, sp.Matrix, Fraction)) else w)
         for k, w in kv.items()})


def mod_dist(x, modulus):
    """distance from 0 in R/(modulus)Z."""
    d = x % modulus
    return min(d, modulus - d)


def filled(p, q, hp=False):
    """4_1(p,q) with the closed-CS initialization done on the cusp (the B432 method)."""
    M = (snappy.ManifoldHP if hp else snappy.Manifold)("4_1")
    M.chern_simons()                     # initialize SnapPea's CS internals (cusped)
    M.dehn_fill((p, q))
    return M


def fcs(M):
    return float(M.chern_simons())


# =====================================================================
# SECTION A -- exact arithmetic (sympy/mpmath; no SnapPy; tier: exact)
# =====================================================================
def exact_backbone():
    print("== A. EXACT BACKBONE (tier: exact; no SnapPy) ==")
    # (a) the 2-torsion lemma's fixed-point sets, exactly. Orientation reversal
    #     negates the Chern-Simons invariant (the CS functional is orientation-odd;
    #     classical). Amphichiral  =>  cs = -cs in R/(mod)Z  =>  2 cs = 0:
    fixed_cusped = sorted(sp.Rational(k, 4) for k in range(2)
                          if (2 * sp.Rational(k, 4)) % sp.Rational(1, 2) == 0)
    fixed_closed = sorted(sp.Rational(k, 2) for k in range(2)
                          if (2 * sp.Rational(k, 2)) % 1 == 0)
    assert fixed_cusped == [0, sp.Rational(1, 4)]      # 2-torsion of R/(1/2)Z
    assert fixed_closed == [0, sp.Rational(1, 2)]      # 2-torsion of R/Z
    print("   2-torsion (mirror-fixed) sets: cusped {0, 1/4} mod 1/2; closed {0, 1/2} mod 1")

    # (b) the cover-tower torsion law (B489, exact): A = [[2,1],[1,1]] = the RL cat
    #     map; |H1 torsion of the n-fold cyclic cover| = |det(A^n - I)| = |L(2n) - 2|.
    A = sp.Matrix([[2, 1], [1, 1]])
    lucas = {n: int((A**n).trace()) for n in (1, 2, 3, 4, 5, 8)}
    tors = {n: int(abs((A**n - sp.eye(2)).det())) for n in (1, 2, 3, 4, 5, 8)}
    assert lucas == {1: 3, 2: 7, 3: 18, 4: 47, 5: 123, 8: 2207}    # L(2n)
    assert tors == {1: 1, 2: 5, 3: 16, 4: 45, 5: 121, 8: 2205}     # |L(2n) - 2|
    assert all(tors[n] == abs(lucas[n] - 2) for n in tors)
    print(f"   Lucas tower: trace(A^n) = L(2n) = {lucas}; |det(A^n - I)| = {tors}")

    # (c) the child trace-field quartic (B434, exact): x^4 - x - 1.
    x = sp.Symbol('x')
    P = x**4 - x - 1
    d = sp.discriminant(P, x)
    assert d == -283 and sp.isprime(283)
    assert sp.Poly(P, x).is_irreducible
    R3 = x**3 + 4 * x - 1                 # resolvent cubic of x^4 + px + q, p=q=-1
    assert sp.Poly(R3, x).is_irreducible
    # disc nonsquare + irreducible resolvent => Galois S4 => NO quadratic subfield:
    assert not sp.sqrt(sp.Abs(d)).is_integer
    print(f"   child quartic x^4 - x - 1: disc {d} (prime), resolvent cubic irreducible")
    print("   => Galois S4 => no quadratic subfield (neither sqrt5 nor sqrt-3): B434")

    # (d) the independent volume anchor (P9/B348 pattern; no SnapPy, no constant):
    mp.mp.dps = 30
    vol_dilog = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))
    assert abs(vol_dilog - mp.mpf("2.029883212819307250042405108549")) < mp.mpf("1e-27")
    print(f"   dilogarithm volume anchor 2 Im Li2(e^(i pi/3)) = {mp.nstr(vol_dilog, 20)}")

    # (e) the banked P9 constants (the probe must agree with them, not restate them):
    from origin_axiom.constants import CS_FIG8, CS_SISTER, VOL_FIG8
    assert CS_FIG8 == 0.0 and CS_SISTER == 0.25
    assert abs(VOL_FIG8 - float(vol_dilog)) < 1e-9
    bank("exact", fixed_cusped=[str(v) for v in fixed_cusped],
         fixed_closed=[str(v) for v in fixed_closed], lucas=lucas, torsion=tors,
         child_quartic="x**4 - x - 1", child_disc=-283, child_galois="S4",
         vol_dilog=float(vol_dilog))
    return float(vol_dilog)


# =====================================================================
# SECTION 0 -- CONTROLS (prereg: failure => INVALID; SnapPy)
# =====================================================================
def controls(vol_anchor):
    print("\n== 0. CONTROLS (banked anchors; fail => INVALID) ==")
    # (a) the seed: cs(4_1) = 0 exactly, complex volume = Vol + 0 i.
    M = snappy.Manifold("4_1")
    cs0 = fcs(M)
    cv = M.complex_volume()
    vol, csu = float(cv.real()), float(cv.imag())
    MH = snappy.ManifoldHP("4_1")
    cs0_hp = float(MH.chern_simons())
    assert abs(cs0) < MACHINE and abs(cs0_hp) < HP_ZERO, f"CONTROL FAIL cs(4_1) {cs0}"
    assert abs(csu) < NUM, f"CONTROL FAIL cv imag {csu}"
    assert abs(vol - vol_anchor) < 1e-6
    # GTZ form (B151): c_hat = i (Vol + i CS) in C/4pi^2 Z => c_hat = i 2.0298...,
    # CS part 0 (Re c_hat = -CS_unnormalized):
    c_hat = complex(0, 1) * complex(vol, csu)
    assert abs(c_hat.real) < NUM and abs(c_hat.imag - vol_anchor) < 1e-6
    sg = M.symmetry_group()
    assert sg.is_full_group() and sg.is_amphicheiral()
    print(f"   seed 4_1: cs = {cs0:+.1e} (HP {cs0_hp:+.1e}); cv = {vol:.10f} + {csu:+.1e} i")
    print(f"             GTZ c_hat = i(Vol + i CS) = {c_hat.real:+.1e} + i {c_hat.imag:.10f}")
    print(f"             symmetry group {sg} (full, amphicheiral)   [certified numerical")
    print("              + exact-by-elimination: amphichiral => cs in {0, 1/4}; 0 pinned]")

    # (b) the sister m003 (P9): cs = 1/4 -- the OTHER 2-torsion point.
    S = snappy.Manifold("m003")
    csS = fcs(S)
    csS_hp = float(snappy.ManifoldHP("m003").chern_simons())
    assert abs(csS - 0.25) < NUM and abs(csS_hp - 0.25) < HP_ZERO, \
        f"CONTROL FAIL cs(m003) {csS}"
    cvS = S.complex_volume()
    assert abs(float(cvS.imag()) - math.pi**2 / 2) < NUM      # = 2 pi^2 * (1/4)
    assert abs(float(cvS.real()) - vol_anchor) < 1e-6          # shares the volume (P9)
    sgS = S.symmetry_group()
    assert sgS.is_full_group() and sgS.is_amphicheiral()
    print(f"   sister m003: cs = {csS:.10f} = 1/4 exactly (HP resid {csS_hp - 0.25:+.1e});")
    print(f"             cv imag = pi^2/2 = {float(cvS.imag()):.9f}; symmetry {sgS} amphicheiral")

    # (c) the metallic family (B127 K-A, the reused computation): cs == 0, m = 1..6,
    #     against the census MIX control (the zero is discriminating, not universal).
    metallic = {}
    for m_ in range(1, 7):
        W = snappy.Manifold("b++" + "R" * m_ + "L" * m_)
        metallic[m_] = (fcs(W), abs(float(W.complex_volume().imag())))
    assert all(abs(c) < MACHINE and i < NUM for c, i in metallic.values()), \
        f"CONTROL FAIL metallic {metallic}"
    census = {nm: fcs(snappy.Manifold(nm)) for nm in ("m003", "m004", "m006")}
    assert abs(census["m003"] - 0.25) < NUM and abs(census["m004"]) < MACHINE
    assert abs(census["m006"]) > 0.05                          # generic nonzero member
    print(f"   metallic m=1..6: cs all machine zero {[f'{c:+.0e}' for c, _ in metallic.values()]}")
    print(f"   census mix control: m003 {census['m003']:.4f}, m004 {census['m004']:+.0e}, "
          f"m006 {census['m006']:+.6f} (nonzero) -- the family zero is discriminating")
    bank("controls", seed_cs=cs0, seed_cs_hp=repr(cs0_hp), seed_vol=vol,
         gtz_chat=[c_hat.real, c_hat.imag], sister_cs=csS,
         sister_cv_imag=float(cvS.imag()),
         metallic_cs={k: v[0] for k, v in metallic.items()}, census_mix=census,
         all_pass=True)
    return True


# =====================================================================
# SECTION 1 -- the cusped strata: forced 2-torsion values (exact by elimination)
# =====================================================================
def cusped_strata():
    print("\n== 1. THE CUSPED STRATA (2-torsion elimination => tier: exact) ==")
    rows = []

    def certify(tag, M, expect, note=""):
        """amphichirality certificate + machine-pin => the exact 2-torsion member."""
        c = fcs(M)
        sg = M.symmetry_group()
        amph = bool(sg.is_full_group() and sg.is_amphicheiral())
        assert amph, f"{tag}: amphichirality certificate failed"
        # amphichiral => cs in {0, 1/4} mod 1/2; the numeric pins the member exactly:
        d0, d4 = mod_dist(c, 0.5), mod_dist(c - 0.25, 0.5)
        val = 0 if d0 < 1e-6 else (Fraction(1, 4) if d4 < 1e-6 else None)
        assert val is not None and abs(float(val) - expect) < 1e-9, f"{tag}: cs = {c}"
        rows.append(dict(stratum=tag, cs_exact=str(val), cs_numeric=c,
                         symmetry=str(sg), amphicheiral=amph,
                         tier="exact (2-torsion elimination)", note=note))
        return val

    # presentation invariance of the seed (condition-1 exhibit): three descriptions,
    # one isometry class, one value; retriangulation-stable; reversal fixes it.
    names = ["4_1", "m004", "b++RL"]
    Ms = {nm: snappy.Manifold(nm) for nm in names}
    assert Ms["4_1"].is_isometric_to(Ms["m004"]) and Ms["4_1"].is_isometric_to(Ms["b++RL"])
    cs3 = {nm: fcs(M) for nm, M in Ms.items()}
    assert all(abs(c) < MACHINE for c in cs3.values())
    Rnd = snappy.Manifold("4_1")
    Rnd.randomize()
    assert abs(fcs(Rnd)) < MACHINE
    Rev = snappy.Manifold("4_1")
    Rev.reverse_orientation()
    assert abs(fcs(Rev)) < MACHINE                    # 0 is mirror-FIXED
    RevS = snappy.Manifold("m003")
    RevS.reverse_orientation()
    assert mod_dist(fcs(RevS) - 0.25, 0.5) < NUM      # -1/4 = 1/4 mod 1/2: FIXED
    print(f"   presentation invariance: 4_1 = m004 = b++RL (isometric), cs {cs3};")
    print("   randomize-stable; orientation reversal FIXES 0 and FIXES 1/4 (mod 1/2)")

    # the strata:
    certify("seed 4_1", Ms["4_1"], 0.0, "P9; the D4 amphichiral seed")
    certify("sister m003", snappy.Manifold("m003"), 0.25,
            "P9; same volume, the OTHER 2-torsion point; mirror-fixed")
    for m_ in range(1, 7):
        certify(f"metallic m={m_} (b++{'R'*m_}{'L'*m_})",
                snappy.Manifold("b++" + "R" * m_ + "L" * m_), 0.0,
                "B127 M-2/K-A: R^m L^m palindromic under reverse+swap")

    # the cyclic cover tower (B489): canonical (n=2 IS the unique degree-2 cover),
    # H1 torsion = |L(2n) - 2| (matches Section A exactly), vol = n Vol(4_1):
    seed_vol = float(snappy.Manifold("4_1").volume())
    cov2 = snappy.Manifold("4_1").covers(2)
    assert len(cov2) == 1 and snappy.Manifold("b++RLRL").is_isometric_to(cov2[0])
    tor_expect = {1: 1, 2: 5, 3: 16, 4: 45, 5: 121, 8: 2205}
    for n in (1, 2, 3, 4, 5, 8):
        C = snappy.Manifold("b++" + "RL" * n)
        ed = C.homology().elementary_divisors()
        tor = 1
        for e in ed:
            tor *= e if e else 1
        assert tor == tor_expect[n], f"cover n={n} torsion {tor}"
        assert abs(float(C.volume()) - n * seed_vol) < 1e-8
        certify(f"cyclic cover n={n} (b++{'RL'*n})", C, 0.0,
                f"B489 tower; H1 torsion {tor} = |L({2*n})-2|; vol = {n} Vol")
    print(f"   cover tower n=1..5,8: unique-cover certificate (n=2), torsion "
          f"{list(tor_expect.values())}, vol = n Vol, cs = 0 each")

    vals = [row["cs_exact"] for row in rows]
    assert vals.count("0") == 13 and vals.count("1/4") == 1 and len(vals) == 14
    print("   CUSPED VALUE MULTISET (exact): {0 x 13, 1/4} -- every member 2-torsion,")
    print("   i.e. mirror-FIXED: the cusped class collapses onto the fixed subgroup")
    bank("cusped", rows=rows, multiset={"0": 13, "1/4": 1},
         presentation_invariance=True, unique_degree2_cover=True)
    return rows


# =====================================================================
# SECTION 2 -- the filling interface: exceptional set + the forced child + eta
# =====================================================================
def filling_interface():
    print("\n== 2. THE FILLING INTERFACE (tier: certified numerical + recognitions) ==")
    rows = []
    # the exceptional set {0, +-1, +-2, +-3}: flat solutions, EXACT rationals;
    # the wall +-4: degenerate, CS undefined (raises).
    expect = {0: Fraction(0), 1: Fraction(1, 84), 2: Fraction(1, 40), 3: Fraction(1, 24)}
    for p in (0, 1, 2, 3):
        for sgn in ((1,) if p == 0 else (1, -1)):
            M = filled(sgn * p, 1)
            st = str(M.solution_type())
            assert "flat" in st, f"4_1({sgn*p},1) solution type {st}"
            c, acc = M.chern_simons(accuracy=True)
            c = float(c)
            frac = Fraction(c).limit_denominator(100)
            assert frac == sgn * expect[p] and abs(c - float(frac)) < MACHINE
            assert acc >= 8
            rows.append(dict(slope=f"({sgn*p},1)", type=st, cs_exact=str(frac),
                             cs_numeric=c, accuracy=int(acc),
                             tier="certified numerical + exact rational recognition"))
    got = {r["slope"]: r["cs_exact"] for r in rows}
    print(f"   exceptional flat fillings: {got}")
    print("   => Seifert-type rationals in mirror pairs +-{1/84, 1/40, 1/24}; Sol point 0")
    M4 = filled(4, 1)
    st4 = str(M4.solution_type())
    assert "degenerate" in st4
    raised = False
    try:
        M4.chern_simons()
    except Exception as exc:
        raised = True
        wall = f"{type(exc).__name__}: {exc}"
    assert raised
    print(f"   toroidal wall 4_1(+-4,1): [{st4}] chern_simons RAISES ({wall})")
    print("   => graph-manifold CS/eta: TOOL-BLOCKED (Kirk-Klassen/Ouyang calculus;")
    print("      not in SnapPy, sage/magma excluded by prereg)")

    # the forced child pair 4_1(+-5,1) = Meyerhoff +- mirror (B434):
    K = filled(5, 1)
    assert "positively oriented" in str(K.solution_type())
    cK, accK = K.chern_simons(accuracy=True)
    cK = float(cK)
    cK_hp = float(filled(5, 1, hp=True).chern_simons())
    cKm = fcs(filled(-5, 1))
    cKm2 = fcs(filled(5, -1))
    assert abs(cK - 0.07703818) < 1e-7                      # the banked B434 value
    assert abs(cK - cK_hp) < 1e-11 and accK >= 8
    assert mod_dist(cK + cKm, 1.0) < NUM                    # mirror pair: sum = 0 mod 1
    assert mod_dist(cK + cKm2, 1.0) < NUM                   # (p,-q) = the same mirror
    Mey = snappy.Manifold("m003(-2,3)")
    assert K.is_isometric_to(Mey)                           # the B434 identification
    KR = filled(5, 1)
    KR.reverse_orientation()
    assert mod_dist(fcs(KR) + cK, 1.0) < NUM                # reversal NEGATES (chiral)
    # chirality, TWO certificates: cs outside the closed 2-torsion set {0, 1/2};
    # and the canonical symmetry group is NOT amphicheiral:
    assert min(mod_dist(cK, 1.0), mod_dist(cK - 0.5, 1.0)) > 0.07
    sgK = K.symmetry_group()
    assert sgK.is_full_group() and not sgK.is_amphicheiral()
    # anti-recognition: the value leaves the rational/2-torsion world (B434's "new
    # arithmetic" surfacing in the CS class): no small-denominator rational nearby:
    best = Fraction(cK_hp).limit_denominator(1000)
    assert abs(cK_hp - float(best)) > 1e-9
    print(f"   forced child 4_1(5,1) = Meyerhoff (= m003(-2,3), isometry-verified):")
    print(f"     cs = +{cK_hp:.17f} (HP; SnapPea accuracy {accK} digits)")
    print(f"     mirror 4_1(-5,1): cs = {cKm:+.12f}; pair sum mod 1 = "
          f"{mod_dist(cK + cKm, 1.0):.1e}")
    print(f"     chiral by TWO certificates: cs distance {min(mod_dist(cK,1.0), mod_dist(cK-0.5,1.0)):.3f}"
          f" from {{0, 1/2}}; symmetry {sgK} NOT amphicheiral")
    print(f"     anti-recognition: best fraction q<=1000 off by "
          f"{abs(cK_hp - float(best)):.1e} (not rational-small); field label "
          f"x^4 - x - 1, disc -283 (Section A) = EXTERNAL-input arithmetic")
    # independent code-path agreement: complex_volume (Zickert-flavored path) vs
    # chern_simons (SnapPea closed algorithm) on the child:
    cvK = K.complex_volume()
    assert mod_dist(float(cvK.imag()) - 2 * math.pi**2 * cK, math.pi**2) < 1e-6
    print(f"     cv cross-path: cv imag {float(cvK.imag()):.9f} = 2 pi^2 cs mod pi^2  OK")

    # eta: the honest exposure scan (prereg: say so, do not skip silently):
    eta_api = sorted(a for a in set(dir(snappy.Manifold("4_1"))) |
                     set(dir(snappy.ManifoldHP("4_1")))
                     if "eta" in a.lower() and "attr" not in a.lower())
    assert eta_api == []
    print("   eta invariant: SnapPy 3.3.x exposes NO eta/rho API (dir() scan over")
    print("   Manifold + ManifoldHP: empty) => eta sub-item TOOL-BLOCKED (named:")
    print("   APS eta needs Meyerhoff-Ruberman/Ouyang machinery or sage -- excluded)")
    bank("interface", exceptional=rows, toroidal_wall=dict(slope="(+-4,1)", type=st4,
                                                           cs="undefined (raises)"),
         child=dict(cs_hp=repr(cK_hp), cs=cK, mirror_cs=cKm, accuracy=int(accK),
                    pair_sum_mod1=mod_dist(cK + cKm, 1.0),
                    meyerhoff_identified=True, symmetry=str(sgK), amphicheiral=False,
                    anti_recognition_q1000=abs(cK_hp - float(best)),
                    tier="certified numerical (HP)"),
         eta_api_scan=eta_api, eta="TOOL-BLOCKED (no SnapPy API; sage/magma excluded)")
    return cK_hp, cKm


# =====================================================================
# SECTION 3 -- the mirror-pairing law across the B432 sample
# =====================================================================
def mirror_law():
    print("\n== 3. THE MIRROR-PAIRING LAW (B432 sample; tier: certified numerical) ==")
    here = os.path.dirname(os.path.abspath(__file__))
    b432 = json.load(open(os.path.join(here, "..", "B432_filling_chirality",
                                       "filling_chirality.json")))
    rows = b432["rows"]
    assert len(rows) == 31 and b432["n_chiral"] == 31
    worst_law, worst_match, checked = 0.0, 0.0, 0
    for row in rows:
        p, q = row["p"], row["q"]
        c1, c2 = fcs(filled(p, q)), fcs(filled(p, -q))
        worst_law = max(worst_law, mod_dist(c1 + c2, 1.0))
        worst_match = max(worst_match, abs((c1 % 1.0) - row["cs"]))
        checked += 1
    assert checked == 31 and worst_law < NUM and worst_match < 1e-6
    # the law's mechanism: mirror(4_1(p,q)) = mirror(4_1)(p,-q) = 4_1(p,-q) BECAUSE
    # the seed is amphichiral -- the seed's own symmetry organizes every chiral child
    # into a +- pair. Volume is mirror-even (spot check):
    v1, v2 = float(filled(3, 4).volume()), float(filled(3, -4).volume())
    assert abs(v1 - v2) < NUM
    print(f"   31/31 banked slopes: cs recomputed, banked match (worst {worst_match:.1e});")
    print(f"   LAW cs(p,-q) = -cs(p,q) mod 1: 31/31 (worst deviation {worst_law:.1e});")
    print(f"   volume mirror-even (spot: {v1:.9f} vs {v2:.9f})")
    print("   => the amphichiral seed organizes the ENTIRE sampled filled class into")
    print("      {+c, -c} mirror orbits; the member selection = the slope sign = input")
    bank("mirror_law", n=31, law_pass=31, worst_law=worst_law,
         banked_match_worst=worst_match, mechanism="mirror(4_1(p,q)) = 4_1(p,-q)")
    return worst_law


# =====================================================================
# SECTION 4 -- the three conditions + the seal
# =====================================================================
def galois_seal(child_cs):
    print("\n== 4. THE THREE CONDITIONS + THE SEAL ==")
    # the assembled forced-value table (exact members where elimination applies):
    F = Fraction
    cusped_fixed = [F(0)] * 13 + [F(1, 4)]                     # seed+sister+metallic+covers
    flat_pairs = [F(1, 84), F(-1, 84), F(1, 40), F(-1, 40), F(1, 24), F(-1, 24)]
    sol_point = [F(0)]                                          # 4_1(0,1)
    child_pair = [child_cs, -child_cs]                          # numerical pair, mod 1

    # (1) trace-map / presentation invariance: computed in Section 1 (three
    #     descriptions of the seed isometric with one value; randomize-stable;
    #     child = m003(-2,3) cross-identified). CS carries NO presentation gauge
    #     (a topological invariant of the oriented manifold) -- and each stratum is
    #     cut intrinsically: the seed; its unique same-volume sister; its canonical
    #     cyclic covers; the K010 metallic monodromy family; the boundary +-5 of the
    #     maximal exceptional set (B434); the exceptional set itself.
    cond1 = bool(REPORT["cusped"]["presentation_invariance"])

    # (2) discretely multivalued: the class takes values in the DISCRETE lattice
    #     quotients R/(1/2)Z (cusped) and R/Z (closed) -- B151's "complex number mod
    #     a lattice" -- and the forced value set assembled above is FINITE:
    forced_set = sorted(set(cusped_fixed + flat_pairs + sol_point), key=float)
    assert len(forced_set) == 8                                # {0,1/4,+-1/84,+-1/40,+-1/24}
    cond2 = len(forced_set) > 1

    # (3) symmetrizable -- the exhaustive three-bin classification under the mirror
    #     involution sigma: cs -> -cs (realized GEOMETRICALLY by the seed's own
    #     amphichirality, B318/B348; = complex conjugation on the geometric solution):
    #     bin F (mirror-FIXED, forced): every cusped value is 2-torsion: sigma-fixed.
    binF = all(mod_dist(2 * float(v), 0.5) < 1e-15 for v in cusped_fixed)
    #     bin P (mirror +- PAIRS, sum 0): the flat rationals and the child pair --
    #     the B348 {+beta, -beta} pattern; the pair is forced, the member is the
    #     orientation / slope sign = external input (B432/B434):
    binP_flat = (sorted(flat_pairs) == sorted(-v for v in flat_pairs)
                 and sum(flat_pairs) == 0)
    binP_child = mod_dist(sum(child_pair), 1.0) < NUM
    #     bin L (input-LABELED): the generic B432 sample -- 31 slope-labeled values,
    #     each still obeying the pairing law (Section 3): the label carries the choice.
    binL = REPORT["mirror_law"]["law_pass"] == 31
    assert cond1 and cond2 and binF and binP_flat and binP_child and binL
    # the FULL multiset (cusped mod 1/2; filled mod 1) is sigma-invariant:
    inv_cusped = sorted(v % F(1, 2) for v in cusped_fixed) == \
        sorted((-v) % F(1, 2) for v in cusped_fixed)
    filled_vals = flat_pairs + sol_point
    inv_filled = sorted(v % 1 for v in filled_vals) == \
        sorted((-v) % 1 for v in filled_vals)
    assert inv_cusped and inv_filled
    print(f"   (1) trace-map-invariant: presentation/triangulation/name-independent "
          f"(computed): {cond1}")
    print(f"   (2) discretely multivalued: lattice quotients; forced set (8 values): "
          f"{[str(v) for v in forced_set]}")
    print("   (3) symmetrizable -- every value lands in exactly one bin:")
    print(f"       bin F mirror-FIXED (2-torsion, forced by amphichirality): "
          f"{{0 x 13, 1/4}}: {binF}")
    print(f"       bin P mirror +-PAIRS (sum 0; member = orientation = input): "
          f"+-{{1/84, 1/40, 1/24}} and +-{abs(child_cs):.10f}: "
          f"{binP_flat and binP_child}")
    print(f"       bin L input-LABELED (generic slopes; still +- paired): 31/31: {binL}")
    print("   full multiset sigma-invariant (cusped mod 1/2, filled mod 1): "
          f"{inv_cusped and inv_filled}")
    print("   NO value is trace-map-invariant + discrete + UNsymmetrizable.")
    bank("seal", forced_set=[str(v) for v in forced_set],
         cusped_multiset_fixed=binF, pairs_sum_zero=bool(binP_flat and binP_child),
         input_labeled_pass=binL, multiset_sigma_invariant=bool(inv_cusped and inv_filled),
         verdict="SEALED")


def verdict():
    print("\n== 5. VERDICT ==")
    print("   SEALED (at the computable horizon).")
    print("   Every CS-type value the object produces across the banked strata is")
    print("   either mirror-FIXED 2-torsion forced by amphichirality (the cusped class:")
    print("   0 thirteen times, and the sister's 1/4 -- both fixed points), a mirror")
    print("   +-PAIR with sum 0 whose member selection is the orientation / slope-sign")
    print("   external input (the exceptional rationals +-{1/84, 1/40, 1/24} and the")
    print("   Meyerhoff child pair +-0.0770381802...), or an input-labeled generic value")
    print("   still obeying the pairing law (31/31). The object hands you the symmetric")
    print("   orbit, never a member -- the B348 {+beta, -beta} pattern landing in the")
    print("   CS class. No clause-(3) forced choice exists in this class.")
    print("   OUT OF REACH (named, honest):")
    print("    - eta / APS rho: NO SnapPy API (scan negative); Meyerhoff-Ruberman /")
    print("      Ouyang / Kirk-Klassen machinery or sage: TOOL-BLOCKED.")
    print("    - exact number-field CS of the CHIRAL fillings (extended-Ptolemy / GTZ")
    print("      exact tier): Ptolemy database (network) or magma/sage: TOOL-BLOCKED.")
    print("    - graph-manifold CS/eta at the toroidal wall 4_1(+-4,1): TOOL-BLOCKED.")
    print("    - verified-interval CS (verified_modulo_2_torsion): needs SageMath;")
    print("      the numeric tier here is certified-numerical (HP + accuracy), with")
    print("      exact values only where 2-torsion elimination / recognition applies.")
    print("    - the universal all-invariants statement: OPEN (C-guardrail; sealing !=")
    print("      universal impossibility proof).")
    print("   Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.")
    bank("verdict", outcome="SEALED",
         phrasing="sealed at the computable horizon; the class beyond these strata "
                  "remains open",
         out_of_reach=["eta/APS rho (no SnapPy API; sage/specialist: TOOL-BLOCKED)",
                       "exact chiral CS via extended-Ptolemy/GTZ (Ptolemy DB or "
                       "magma/sage: TOOL-BLOCKED)",
                       "toroidal +-4 graph CS/eta (TOOL-BLOCKED)",
                       "verified-interval CS (sage: named)",
                       "universal statement (open)"])


def main():
    vol_anchor = exact_backbone()
    if not HAVE_SNAPPY:                                          # pragma: no cover
        print("\nSnapPy unavailable: the value sweep did not run (controls not")
        print("executed; exact backbone only). Rerun with snappy installed.")
        bank("verdict", outcome="NOT-RUN (snappy unavailable)")
        return 0
    if not controls(vol_anchor):                                 # pragma: no cover
        print("CONTROL FAILED -- probe INVALID; stopping per prereg.")
        return 1
    cusped_strata()
    child_cs, _ = filling_interface()
    mirror_law()
    galois_seal(child_cs)
    verdict()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b496_cs_eta.json")
    json.dump(REPORT, open(out, "w"), indent=1, default=str)
    print(f"\n[written] {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
