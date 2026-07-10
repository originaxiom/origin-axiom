"""Locks for B497 (Gate A class 2e: the extended-Bloch class beyond the object's own).

Pure backbone (no SnapPy): the B348 control facts recomputed (the seam identity, the
{+beta, -beta} orbit with the volume magnitude, D == 0 on the fixed field); the child
quartic and octic field facts (irreducibility, disc -283, the octic pair's shared-field
certificates re-verified with sympy resultants where pari-free); banked-JSON integrity
(verdict SEALED with the C-guardrail phrasing, the strata rows, the Ptolemy orbit and
the negated flattening integers, the named TOOL-BLOCKED list).

SnapPy behind importorskip: the live seed control (shapes = z0; z0 AND conj z0 solve the
rect system exactly), the m=2 exact Gaussian solve, one cyclic cover, and the decisive
extended-Bloch computation (the exact N=2 Ptolemy solutions pushed through the offline
Zickert pipeline: the {+c^, -c^} orbit, sum 0, flattening integers negated). Total
runtime well under 60 s.
"""
import importlib.util
import json
import pathlib

import mpmath as mp
import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B497_extended_bloch_galois"

_spec = importlib.util.spec_from_file_location("b497_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

R = json.load(open(_DIR / "b497_extended_bloch.json"))

VOL = 2.0298832128193072


# ---------------- (1) the B348 control, recomputed (pure) ----------------
def test_seam_identity_and_eisenstein_locus():
    z = sp.symbols('z')
    assert sp.simplify(1 - P.Z0 - P.Z0BAR) == 0                 # 1 - z0 = conj(z0)
    assert sp.expand(z * (1 - z) - 1 + (z**2 - z + 1)) == 0     # the locus IS Eisenstein
    assert sp.simplify(1 / P.Z0BAR - P.Z0) == 0                 # the |z|=1 face
    eis = z**2 - z + 1
    assert sp.expand(eis.subs(z, P.Z0)) == 0 and sp.expand(eis.subs(z, P.Z0BAR)) == 0


def test_orbit_sum_zero_and_volume_magnitude():
    d0 = P.bloch_wigner(complex(sp.re(P.Z0), sp.im(P.Z0)))
    d0b = P.bloch_wigner(complex(sp.re(P.Z0BAR), sp.im(P.Z0BAR)))
    assert abs(2 * d0 + 2 * d0b) < mp.mpf(10)**(-25)            # {+beta,-beta}: sum 0
    assert abs(abs(2 * d0) - VOL) < 1e-12                       # member = +-Vol(4_1)
    assert abs(P.bloch_wigner(mp.mpf(2) / 3)) < mp.mpf(10)**(-25)   # D == 0 on fixed field


def test_dneg_orbit_matching_machinery():
    # the seam as a matching: conj of the Eisenstein pair self-pairs (1-z branch);
    # a generic non-real pair does NOT:
    z0 = complex(0.5, 3**0.5 / 2)
    assert P.conj_self_pairs([z0, z0])
    assert not P.conj_self_pairs([complex(0.3, 0.9), complex(0.3, 0.9)])


# ---------------- (2) the child field facts (pure) ----------------
def test_child_quartic_exact():
    x = sp.symbols('x')
    q = x**4 - x - 1
    assert sp.Poly(q, x).is_irreducible
    assert sp.discriminant(q, x) == -283
    assert R["fillings"]["galois"] == "S4"
    assert R["fillings"]["no_quadratic_subfield"] is True


def test_child_octics_banked_and_irreducible():
    x = sp.symbols('x')
    o1 = sp.sympify(R["fillings"]["spun_octic_plus"])
    o2 = sp.sympify(R["fillings"]["spun_octic_minus"])
    assert sp.degree(o1, x) == 8 and sp.degree(o2, x) == 8
    assert sp.Poly(o1, x).is_irreducible and sp.Poly(o2, x).is_irreducible
    assert R["fillings"]["spun_octics_isomorphic"] is True      # ONE abstract field
    assert R["fillings"]["spun_exact_gluing_check"] is True     # exact polmod pass
    assert R["fillings"]["octic_contains_trace_quartic"] is True
    assert R["fillings"]["octic_poldisc_has_283_squared"] is True
    # pari cross-check when cypari is importable (core dep in this repo):
    pari = pytest.importorskip("cypari").pari
    O1 = pari(str(o1).replace('**', '^'))
    O2 = pari(str(o2).replace('**', '^'))
    assert pari.nfisisom(O1, O2) != 0
    assert pari.nfisincl(pari('x^4 - x - 1'), O1) != 0


# ---------------- (3) banked-JSON integrity ----------------
def test_controls_banked_all_pass():
    C = R["controls"]
    assert C["seam_exact"] and C["orbit_sum_zero"] and C["d_vanishes_on_fixed_field"]
    assert abs(C["vol_member"] - VOL) < 1e-12
    assert C["seed_rect_exact"] is True and C["seed_rect_conj_exact"] is True


def test_cover_tower_banked():
    rows = R["covers"]["rows"]
    assert [r["n"] for r in rows] == [2, 3, 4, 5]
    for r in rows:
        assert r["all_shapes_z0"] and r["amphichiral"]
        assert abs(r["vol_over_seed"] - r["n"]) < 1e-8
    assert R["covers"]["field"] == "Q(sqrt-3) all n"


def test_metallic_strata_banked():
    M = R["metallic"]
    assert M["2"]["census"] == "m136" and M["2"]["rect_exact"] is True
    assert M["2"]["conj_self_pairing_exact"] is True and M["2"]["vol_is_4catalan"] is True
    assert M["3"]["census"] == "s464" and "degrees [8]" in M["3"]["field"]
    assert M["4"]["census"] == "t03910" and "degrees [4]" in M["4"]["field"]
    for m in ("1", "2", "3", "4"):
        assert M[m]["amphichiral"] and M[m]["conj_self_pairs_dneg_orbit"]
    # one banked m=4 quartic recomputed irreducible:
    x = sp.symbols('x')
    assert sp.Poly(sp.sympify(M["4"]["min_polys"][1]), x).is_irreducible


def test_extended_bloch_orbit_banked():
    E = R["extended_bloch"]
    assert E["seed_class0"] == "empty"
    assert E["seed_class1_eliminant"] == "c**2 - c + 1"         # the seam roots
    cvp, cvm = E["seed_cvols"]["+"], E["seed_cvols"]["-"]
    assert abs(cvp[0] + cvm[0]) < 1e-9                          # {+c^, -c^}: sum 0
    assert abs(abs(cvp[0]) - VOL) < 1e-9
    assert abs(cvp[1]) < 1e-9 and abs(cvm[1]) < 1e-9            # CS-part 0
    pqp, pqm = E["seed_flattening_pq"]["+"], E["seed_flattening_pq"]["-"]
    assert [[-p, -q] for p, q in pqm] == [list(t) for t in pqp]  # Galois-negated (p,q)
    assert E["seed_pq_galois_negated"] is True
    assert isinstance(E["own_rogers_defect_units_pi2_over_6"], int)   # integer-certified
    # m136: 6 empty, one positive-dimensional, one with 8 points, sum 0:
    vals = list(E["m136_classes"].values())
    assert vals.count("empty") == 6 and vals.count("POSITIVE-DIMENSIONAL") == 1
    pts = [v for v in vals if isinstance(v, dict)]
    assert len(pts) == 1 and pts[0]["n_points"] == 8
    assert sp.factor(sp.sympify(pts[0]["eliminant"])) == sp.factor(
        sp.sympify("c**4 + 2*c**2 + 2"))
    assert abs(E["m136_cv_multiset_sum"]) < 1e-6


def test_verdict_sealed_with_guardrail_and_named_blocks():
    V = R["verdict"]
    assert V["outcome"] == "SEALED"
    assert "computable horizon" in V["phrasing"]
    assert len(V["tool_blocked"]) >= 3                          # named, not silent
    assert any("4 pi^2" in t for t in V["tool_blocked"])
    assert any("K3^ind torsion" in t for t in V["tool_blocked"])
    find = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
    assert "SEALED" in find
    assert "Nothing to `CLAIMS.md`" in find
    assert "TOOL-BLOCKED" in find
    assert "C-guardrail" in find


# ---------------- SnapPy legs (optional dependency) ----------------
def test_snappy_seed_control_exact_gluing():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    z0c = complex(sp.re(P.Z0), sp.im(P.Z0))
    assert all(abs(complex(s) - z0c) < 1e-9 for s in M.tetrahedra_shapes('rect'))
    rows = P.rect_rows(M)
    assert P.rect_check_exact(rows, [P.Z0, P.Z0])
    assert P.rect_check_exact(rows, [P.Z0BAR, P.Z0BAR])


def test_snappy_m136_gaussian_exact_and_self_pairing():
    snappy = pytest.importorskip("snappy")
    B = snappy.Manifold("b++RRLL")
    assert str(B.identify()[0]).startswith("m136")
    sh = [complex(s) for s in B.tetrahedra_shapes('rect')]
    cands = [1 + sp.I, sp.Rational(1, 2) + sp.I / 2, 1 + sp.I, sp.I]
    pool = list(cands)
    exact = []
    for s in sh:
        hit = next(c for c in pool if abs(complex(sp.re(c), sp.im(c)) - s) < 1e-9)
        pool.remove(hit)
        exact.append(hit)
    assert P.rect_check_exact(P.rect_rows(B), exact)            # Gaussian solve, exact
    assert P.conj_self_pairs(sh)                                # the generalized seam


def test_snappy_cover_n2_is_double_class():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    C = [c for c in M.covers(2) if c.cover_info()["type"] == "cyclic"][0]
    z0c = complex(sp.re(P.Z0), sp.im(P.Z0))
    sh = [complex(s) for s in C.tetrahedra_shapes('rect')]
    assert len(sh) == 4 and all(abs(s - z0c) < 1e-9 for s in sh)    # class = 2.beta
    cv = complex(C.complex_volume())
    assert abs(cv.real - 2 * VOL) < 1e-8 and abs(cv.imag) < 1e-9


def test_snappy_ptolemy_orbit_and_flattening_negation():
    snappy = pytest.importorskip("snappy")
    from snappy.ptolemy.coordinates import PtolemyCoordinates
    M = snappy.Manifold("4_1")
    Vs = M.ptolemy_variety(2, obstruction_class='all')
    assert len(Vs) == 2
    pts0, pos0 = P.ptolemy_points_exact(Vs[0])
    assert pts0 == [] and not pos0                              # class 0 empty
    pts1, pos1 = P.ptolemy_points_exact(Vs[1])
    assert not pos1 and len(pts1) == 2                          # the Galois pair
    c = sp.symbols('c')
    assert sp.expand(sp.minimal_polynomial(pts1[0]['c_0101_0'], c)
                     - (c**2 - c + 1)) == 0                     # the seam roots
    sec = eval(Vs[1].py_eval_section())
    out = {}
    for pt in pts1:
        root = complex(sp.N(pt['c_0101_0'], 30))
        pc = PtolemyCoordinates(
            {'1': 1, 'c_0011_0': complex(sp.N(pt['c_0011_0'], 30)), 'c_0101_0': root},
            is_numerical=True, py_eval_section=sec, manifold_thunk=lambda: M)
        cv = complex(pc.complex_volume_numerical())
        fl = pc.flattenings_numerical()
        pq = []
        for tet in (0, 1):
            _, zz, p = fl['z_0000_%d' % tet]
            w1, _, _ = fl['zp_0000_%d' % tet]
            zz = mp.mpc(complex(zz))
            q = round(((complex(w1) + complex(mp.log(1 - zz))) / complex(mp.pi * 1j)).real)
            pq.append((int(p), q))
        out["+" if root.imag > 0 else "-"] = (cv, pq)
    assert abs(out["+"][0].real + out["-"][0].real) < 1e-9      # orbit sum 0
    assert abs(abs(out["+"][0].real) - VOL) < 1e-9
    assert out["+"][1] == [(-p, -q) for (p, q) in out["-"][1]]  # (p,q) Galois-negated
