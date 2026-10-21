"""B1692 -- the cusp with a twisted line per sector (P-169, part 1). Live: B1653's residue coupling with the covariant
Higgs DR reproduces B1691's 18 |q|^(1/2) at Im tau = 4; at Im tau = 10 the line alpha = 5/48 splits the sectors as
(2, 1, 4) times the line-free value and the half-period line gives (2, 2, 2); the bite: the up sector read with the down
quarks' charge (-4 -> 2) changes its factor. Stored: the 484-line census at Im tau = 14 (spread <= 4, no beta dependence)
and the finite-Im tau census (spread 3.01, 3.60, 3.92)."""
import importlib.util, io, contextlib, json, pathlib, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1692_the_cusp_with_a_twisted_line_per_sector" / "verification"
sys.path.insert(0, str(A))
B1691 = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(B1691))


def _mods():
    import b1653_funcs as F
    spec = importlib.util.spec_from_file_location("te_lock", B1691 / "the_exponents.py")
    te = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(te)
    return F, te


def _m2m3(F, A_, t, alpha, left, right, N=192):
    mp = F.mp
    w = alpha * t
    M = F.res_bil(F.twist_of(F.SIXY[left] * w, t), F.twist_of(F.SIXY[right] * w, t), t, N=N)
    Y = F.coupling(A_[0] * F.QI + A_[1] * F.QJ + A_[2] * F.QK, M)
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True)
    return s[1] / s[0]


def test_two_codes_and_the_split_live_with_the_bite():
    F, te = _mods(); mp = F.mp; mp.mp.dps = 30
    t = mp.mpc(0, 4); a = [te.ev(c, t) for c in te.B[1]]
    assert abs(_m2m3(F, a, t, 0, "Q", "u") / mp.exp(-mp.pi * 4) - 18) < 1e-3
    t = mp.mpc(0, 10); a = [te.ev(c, t) for c in te.B[1]]
    base = _m2m3(F, a, t, 0, "Q", "u")
    al = mp.mpf(5) / 48
    c = [_m2m3(F, a, t, al, L, R) / base for L, R in (("Q", "u"), ("Q", "d"), ("L", "e"))]
    assert abs(c[0] - 2) < 1e-3 and abs(c[1] - 1) < 1e-2 and abs(c[2] - 4) < 1e-2
    h = [_m2m3(F, a, t, mp.mpf(1) / 2, L, R) / base for L, R in (("Q", "u"), ("Q", "d"), ("L", "e"))]
    assert all(abs(x - 2) < 1e-6 for x in h)
    assert abs(_m2m3(F, a, t, al, "Q", "d") / base - c[0]) > 0.5                     # the bite: the charge matters


def test_the_censuses_stored():
    r = json.loads((A / "line_census.json").read_text(encoding="utf-8"))
    assert len(r) == 484 and max(max(v) / min(v) for _, _, v in r) < 4 + 1e-6 and min(min(v) for _, _, v in r) > 1 - 1e-6
    by_j = {}
    for j, b, v in r: by_j.setdefault(j, set()).add(tuple(round(x, 6) for x in v))
    assert all(len(s) == 1 for s in by_j.values())                                     # beta never matters
    f = json.loads((A / "finite_census.json").read_text(encoding="utf-8"))
    for y, cap in ((1.5, 3.02), (2, 3.61), (3, 3.93)):
        assert max(max(v) / min(v) for j, yy, n, v in f if yy == y) < cap
