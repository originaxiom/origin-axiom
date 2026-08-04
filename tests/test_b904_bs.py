"""B904 locks: the Barton-Sudbery capstone — stage gates + a phi spot-verification."""
import json
import os
import pickle
from fractions import Fraction as F

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B904_barton_sudbery")


def _j(name):
    with open(os.path.join(ARC, name)) as f:
        return json.load(f)


def test_stage1_triality_dims():
    d = _j("stage1_dims.json")
    assert d["dim_soN"] == 28
    assert d["dim_tri"] == 28


def test_stage2_derived_products_unique():
    p = _j("stage2b_products.json")
    assert p["(1,2)->(3)"] == ["xy"]
    assert p["(2,3)->(1)"] == ["y_cx"]
    assert p["(3,1)->(2)"] == ["cy_x"]


def test_stage3_jacobi_zero_failures():
    r = _j("stage2c_results.json")
    assert r["fit"] == "OK"
    assert r["jacobi_failures"] == 0
    assert r["scalars"]["mu0"] == r["scalars"]["mu1"] == r["scalars"]["mu2"] == "-24"
    assert r["scalars"]["nu0"] == r["scalars"]["nu1"] == r["scalars"]["nu2"] == "-12"


def test_stage4_roots_and_e6():
    r = _j("stage4_roots.json")
    assert r["n_roots"] == 72
    assert r["dims"].count(1) == 72 and 6 in r["dims"]
    c = _j("stage4b_cartan.json")
    assert c["n_pos"] == 36 and c["n_simple"] == 6
    assert c["e6_permutation"] is not None


def test_phi_is_a_verified_isomorphism():
    r = _j("stage4c_results.json")
    assert r["mismatches"] == 0
    assert r["verdict"] == "ISOMORPHISM"
    # the banked phi exists and is 78x78
    PHI = pickle.load(open(os.path.join(ARC, "stage4c_phi.pkl"), "rb"))
    assert len(PHI) == 78 and all(len(row) == 78 for row in PHI)


def test_phi_spot_homomorphism_recheck():
    """Independent recheck of phi([a,b]) = [phi a, phi b] on fixed pairs,
    with both bracket tensors loaded from the banked artifacts."""
    import sympy as sp
    from collections import defaultdict
    RAW = pickle.load(open(os.path.join(ARC, "stage2c_tensor.pkl"), "rb"))
    NBR = defaultdict(dict)
    for kstr, d in RAW.items():
        key = eval(kstr)
        if len(key) == 2:
            for kk, vv in d.items():
                NBR[key][int(kk)] = F(vv)
        else:
            NBR[(key[0], key[1])][key[2]] = F(d)

    def nbr(a, b):
        if a == b: return {}
        if a < b: return NBR.get((a, b), {})
        return {k: -v for k, v in NBR.get((b, a), {}).items()}

    import io, contextlib
    frame_path = os.path.join(os.path.dirname(ARC), "B854_centralizer_exact",
                              "e6_centralizer.py")
    scope = {"__file__": frame_path}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(open(frame_path).read(), "b854", "exec"), scope)
    BB = scope["BB"]
    PHI = [[F(sp.Rational(x).p, sp.Rational(x).q) for x in row]
           for row in pickle.load(open(os.path.join(ARC, "stage4c_phi.pkl"), "rb"))]
    DIM = 78

    def phicol(v):
        return [PHI[k][v] for k in range(DIM)]

    def brv_bd(u, v):
        out = [F(0)]*DIM
        for i, cu in enumerate(u):
            if not cu: continue
            for j, cv in enumerate(v):
                if not cv: continue
                w = BB[i][j]
                for k, c in enumerate(w):
                    if c:
                        r = sp.Rational(c)
                        out[k] += cu*cv*F(r.p, r.q)
        return out

    pairs = [(0, 30), (5, 46), (28, 62), (30, 46), (46, 62), (62, 30),
             (30, 31), (46, 47), (62, 63), (0, 5), (12, 70), (28, 29),
             (3, 40), (17, 55), (25, 77)]
    for (a, b) in pairs:
        lhs_vec = nbr(a, b)
        lhs = [F(0)]*DIM
        for i, c in lhs_vec.items():
            col = phicol(i)
            for k in range(DIM):
                lhs[k] += c*col[k]
        rhs = brv_bd(phicol(a), phicol(b))
        assert lhs == rhs, (a, b)
