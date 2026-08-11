"""B1040 locks — the isomonodromy cluster, re-verified before restoration.

These do NOT exec `verify.py` (it shells out to B169's flow reproducer). They independently
recompute the symbolic core and read the banked `results.json` for the numerical half.
If any breaks, the restored LAW_MAP row is wrong and must move with it.
"""
import json
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_R = json.loads((_ROOT / "frontier" / "B1040_isomonodromy_restored" / "results.json")
                .read_text(encoding="utf-8"))

_x, _y, _z = sp.symbols("x y z")
_t = sp.symbols("t1 t2 t3 t4")
_PX, _PY, _PZ = _t[0]*_t[1] + _t[2]*_t[3], _t[0]*_t[3] + _t[1]*_t[2], _t[0]*_t[2] + _t[1]*_t[3]
_P0 = 4 - sum(v**2 for v in _t) - _t[0]*_t[1]*_t[2]*_t[3]
_PHI = _x**2 + _y**2 + _z**2 + _x*_y*_z - _PX*_x - _PY*_y - _PZ*_z - _P0
_KAPPA = _x**2 + _y**2 + _z**2 - _x*_y*_z - 2

_VIETA = {
    "s_x": lambda v: (_PX - v[1]*v[2] - v[0], v[1], v[2]),
    "s_y": lambda v: (v[0], _PY - v[0]*v[2] - v[1], v[2]),
    "s_z": lambda v: (v[0], v[1], _PZ - v[0]*v[1] - v[2]),
}


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_vieta_involutions_preserve_the_cubic_in_all_seven_variables():
    """The four boundary traces stay FREE — this is the cubic as a family, not one fibre."""
    for nm, s in _VIETA.items():
        im = s((_x, _y, _z))
        assert sp.expand(sp.Matrix(s(im)) - sp.Matrix([_x, _y, _z])) == sp.zeros(3, 1), nm
        assert sp.expand(_PHI.subs({_x: im[0], _y: im[1], _z: im[2]},
                                   simultaneous=True) - _PHI) == 0, nm


def test_the_composite_is_not_an_involution_so_the_dynamics_is_not_vacuous():
    """Three involutions generating only involutions would be a finite group — no Painlevé-VI."""
    a = _VIETA["s_y"](_VIETA["s_x"]((_x, _y, _z)))
    b = _VIETA["s_y"](_VIETA["s_x"](a))
    assert sp.expand(sp.Matrix(b) - sp.Matrix([_x, _y, _z])) != sp.zeros(3, 1)


def test_the_bridge_to_the_OPT_void_fibre_at_kappa_equals_2():
    phi0 = sp.expand(_PHI.subs({v: 0 for v in _t}))
    assert sp.expand(phi0 - (_x**2 + _y**2 + _z**2 + _x*_y*_z - 4)) == 0
    assert sp.expand(phi0.subs(_z, -_z) - (_KAPPA - 2)) == 0


def test_dim_two_Fricke_cubics_are_exactly_the_seed_and_the_four_punctured_sphere():
    """B164 carries this by CITATION; a repo-wide search for 6g-6 finds two hits, neither a
    computation. Classical (Fricke; Cantat-Loray) — a verification, not a discovery."""
    got = [(g, n) for g in range(0, 41) for n in range(0, 81)
           if 6*g - 6 + 2*n == 2 and 2*g - 2 + n > 0]
    assert sorted(got) == [(0, 4), (1, 1)]


def test_the_class_s_cubic_and_kappa_are_one_equation():
    """a,b,c = -tr A, -tr B, -tr AB in a^2+b^2+c^2+abc = 2+lam+1/lam gives kappa = lam + 1/lam."""
    lam = sp.Symbol("lam")
    assert sp.expand(((-_x)**2 + (-_y)**2 + (-_z)**2 + (-_x)*(-_y)*(-_z)) - (_KAPPA + 2)) == 0
    assert sp.solve(sp.Eq(lam + 1/lam, -2), lam) == [-1]


def test_the_metallic_degree_holds_symbolically_in_m():
    """The arcs check m = 1,2,3; the law needs every m."""
    m = sp.Symbol("m", positive=True)
    lam_m = (m + sp.sqrt(m**2 + 4)) / 2
    assert sp.simplify(lam_m**2 - m*lam_m - 1) == 0
    assert sp.simplify(sp.expand((lam_m**2)**2 - (m**2 + 2)*lam_m**2 + 1)) == 0
    assert sp.simplify(sp.radsimp(lam_m.subs(m, 1)**2) - (3 + sp.sqrt(5))/2) == 0
    assert sp.simplify(sp.radsimp(lam_m.subs(m, 3)**2) - (11 + 3*sp.sqrt(13))/2) == 0


def test_the_flow_is_scale_free__the_check_B169_never_runs():
    """B169's two P3 checks pass `True` literally. This is its one formalisable sub-claim."""
    s, c, ti = sp.symbols("s c t_i")
    rhs = 1/(s - ti)
    assert sp.simplify(rhs.subs({s: c*s, ti: c*ti}) - rhs/c) == 0


def test_the_flow_result_travels_with_its_control_or_it_is_not_evidence():
    """RK4 at h=0.01 has O(h^4) truncation, so 4e-10 alone proves nothing — the CONTRAST does."""
    a = _R["checks"]["P2_the_Schlesinger_flow_preserves_every_local_conjugacy_class"]
    b = _R["checks"]["P2b_AND_the_control_fires__which_is_what_makes_it_evidence"]
    assert a["pass"] and b["pass"]
    assert float(a["drift"]) < 1e-8 < 1.0 < float(b["control"])


def test_the_restoration_landed_with_all_three_scope_corrections():
    lawmap = (_ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "THE PAINLEVÉ-VI PARTNER IS FORCED BY A DIMENSION COUNT" in lawmap
    assert "not a discovery" in lawmap          # the (g,n) count is classical
    assert "no Picard lattice" in lawmap        # the [exact] tag is on the algebra only
    assert "superseded by B169" in lawmap       # B164's C4
    assert "POSTULATED" in lawmap               # the relocation verdict's tier
    assert "non-Schlesinger control" in lawmap  # the number's licence
    for b in ("B164", "B169", "B150"):
        assert b in lawmap, b


def test_what_is_carried_by_citation_is_named_not_implied():
    cb = _R["carried_by_citation"]
    assert any("Cantat-Loray" in v for v in cb.values())
    assert any("RHYME" in v for v in cb.values())
    assert any("NEEDS-SPECIALIST" in v for v in cb.values())
