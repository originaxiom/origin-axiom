"""B1703 -- the line census (P-250). Stored: the laws on every order of the first census and of the confirmation (fresh
tau, omega); the large-L check (orders 8, 10 split, 4, 5 coincide at every L). Live: one order-8 line splits d from e
and one order-4 line does not; one order-3 line protects all three sectors."""
import importlib.util, io, contextlib, json, math, pathlib, sys
from fractions import Fraction as Fr
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1703_the_line_census" / "verification"


def law(N):
    return {"d=e": 4 % N == 0 or 5 % N == 0, "u=d": 6 % N == 0, "u=e": 2 % N == 0 or 7 % N == 0,
            "up": 5 % N == 0 or 3 % N == 0, "down": 1 % N == 0 or 3 % N == 0, "lep": 9 % N == 0 or 3 % N == 0}


def test_the_laws_stored():
    c = json.loads((A / "the_confirmation.json").read_text(encoding="utf-8"))
    assert c["A_laws_hold"]
    for part in ("A", "B_omega"):
        for N, e in c[part].items():
            n = int(N)
            for k, v in law(n).items():
                assert (e[k] == e["lines"]) == v and e[k] in (0, e["lines"]), (part, n, k)
            assert (e["all_split"] == e["lines"]) == (n >= 8)
    first = json.loads((A / "the_line_census.json").read_text(encoding="utf-8"))["by_order"]
    for N, e in first.items():
        n = int(N)
        for k in ("d=e", "u=d", "u=e"):
            assert (e[k] == e["lines"]) == law(n)[k] and e[k] in (0, e["lines"])
        for s in ("up", "down", "lep"):
            assert (e["protected"][s] == e["lines"]) == law(n)[s]


def test_large_L_stored():
    rows = json.loads((A / "large_L.json").read_text(encoding="utf-8"))
    for r in rows:
        vals = [r[k] for k in ("canon", "10.0", "100.0", "10000.0", "100000000.0")]
        if r["N"] in (4, 5):
            assert max(vals) < 1e-12
        if r["N"] in (8, 10):
            assert min(vals[1:]) > 1e-3


def test_live():
    argv = sys.argv; sys.argv = ["x"]
    sys.path.insert(0, str(A))
    try:
        spec = importlib.util.spec_from_file_location("b1703", A / "the_line_census.py")
        m = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
    finally:
        sys.argv = argv
    m.TAUS[:] = [complex(0.27, 2.2)]
    m.LINES[:] = [(Fr(1, 8), Fr(3, 8), 8), (Fr(1, 4), Fr(1, 2), 4), (Fr(1, 3), Fr(2, 3), 3)]
    r8, r4, r3 = (m.point((k, 0)) for k in range(3))
    assert not m.same(r8["down"], r8["lep"]) and m.same(r4["down"], r4["lep"])
    assert all(r3[s + "_R1_rel"] < 1e-9 for s in ("up", "down", "lep"))
