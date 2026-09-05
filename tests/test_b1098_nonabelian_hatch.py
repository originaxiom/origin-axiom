"""B1098 lock: the hatch's verdict rows — the stored A2 triple verified live + the table."""
import json
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]

def test_saturation_and_the_two_landings():
    rows = json.load(open(ROOT / "frontier/B1098_nonabelian_hatch/b1098_results.json"))
    assert len(rows) == 20                                   # saturation vs the cited count
    dims = sorted((r["dim_c"] for r in rows), reverse=True)
    assert dims[:4] == [35, 22, 16, 14]                       # a5, b3+u1, a2+a2, g2
    a2row = next(r for r in rows if r["dim_c"] == 16)
    assert (a2row["rank_c"], a2row["center_dim"], a2row["dim_ss"], a2row["rank_ss"]) == (4, 0, 16, 4)
    a1row = next(r for r in rows if r["dim_c"] == 35)
    assert (a1row["rank_c"], a1row["dim_ss"]) == (5, 35)
    b3row = next(r for r in rows if r["dim_c"] == 22)
    assert (b3row["rank_c"], b3row["center_dim"], b3row["dim_ss"], b3row["rank_ss"]) == (4, 1, 21, 3)

@pytest.mark.slow
def test_a2_triple_relations_and_centralizer_live():
    import os
    from fractions import Fraction as F
    import sympy as sp
    vendored = ROOT / "frontier/B1148_carrier_harvest/verification/certificates/twisted_double.py"
    cert = os.environ.get("B1098_CERT_PATH", str(vendored))
    if not os.path.exists(cert):
        pytest.skip("cert machinery path not provided in this environment")
    # B1240 vendored the closure; its relative imports need the actual filename.
    # Keep the original mathematical assertions, not a record-only replacement.
    G = {"__file__": str(Path(cert).resolve()), "__name__": "b1098_certificate_prefix"}
    src = open(cert).read()
    cut = src.index(chr(112) + 'rint(" IDENTITY double')
    exec(compile(src[:cut], cert, "exec"), G)
    br, DIM = G["br"], G["DIM"]
    d = json.load(open(ROOT / "frontier/B1098_nonabelian_hatch/b1098_a2_triple.json"))
    de = lambda v: [F(a, b) for a, b in v]
    X, H, Y = de(d["X"]), de(d["H"]), de(d["Y"])
    HX = br(H, X); HY = br(H, Y); XY = br(X, Y)
    assert all(HX[i] == F(2) * X[i] for i in range(DIM))
    assert all(HY[i] == F(-2) * Y[i] for i in range(DIM))
    assert all(XY[i] == H[i] for i in range(DIM))
    def adm(Z):
        out = []
        for i in range(DIM):
            e = [F(0)] * DIM; e[i] = F(1)
            out.append([sp.Rational(c.numerator, c.denominator) for c in br(Z, e)])
        return sp.Matrix(out).T
    S = sp.Matrix.vstack(adm(X), adm(H), adm(Y))
    assert len(S.nullspace()) == 16 == d["dim_c"]
