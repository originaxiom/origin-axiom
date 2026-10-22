"""B1707 -- W111 on main (P-211). Live: the moves keep the boundary class (g = 2); the Heisenberg character H(3) at g = 2
is fixed by every move on random words; at g = 2 the all-minus Pauli representation is broken by mu' alone, and at g = 1
the all-minus one (Q8) is fixed. Stored: the search's tallies; the extraspecial table."""
import importlib.util, io, contextlib, json, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1707_w111_on_main" / "verification"


def _src():
    s = (A / "the_surface_route.py").read_text(encoding="utf-8")
    return s[:s.index("# (a) SL(2, C) characters fixed")] + s[s.index("# (b), (c): the Heisenberg"):s.index("heis = {}")]


def test_live():
    ns = {"__file__": str(A / "the_surface_route.py")}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(_src(), "b1707_partial", "exec"), ns)
    assert all(ns["out"]["boundary_kept"][2].values())
    X, Z = ns["clock_shift"](3); img = {}
    for k in range(2): img[("a", k)] = ns["kron_at"](X, k, 2, 3); img[("b", k)] = ns["kron_at"](Z, k, 2, 3)
    assert ns["fixed"](img, 2, nwords=60) == {}
    PX = np.array([[0, 1], [1, 0]], dtype=complex); PZ = np.array([[1, 0], [0, -1]], dtype=complex)
    q2 = {}
    for k in range(2): q2[("a", k)] = 1j * ns["kron_at"](PX, k, 2, 2); q2[("b", k)] = 1j * ns["kron_at"](PZ, k, 2, 2)
    assert sorted(ns["fixed"](q2, 2, nwords=120)) == ["mu'"]
    q1 = {("a", 0): 1j * PX, ("b", 0): 1j * PZ}
    assert ns["fixed"](q1, 1, nwords=120) == {}


def test_stored():
    d = json.loads((A / "the_surface_route.json").read_text(encoding="utf-8"))
    a2 = d["a_search"]["2"]
    assert a2["converged"] > 0 and a2["trivial_or_traces_2"] == a2["converged"] and not a2["other"]
    assert d["a_search"]["1"]["quaternion_handles"] > 0
    assert [k for k, v in d["c_extraspecial"].items() if v["fixed"]] == ["g=1 squares --"]
    assert all(v == {} for v in d["b_heisenberg_moves_breaking"].values())
