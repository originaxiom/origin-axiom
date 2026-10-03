"""B1530 lock -- THE INTERIOR EXTENSIONS (2026-10-03). sL-10 item 10 (a): B1515's rank-five extensions at the hyperbolic point of
every word state to length 12 and of m004's levels M2-M6. Sealed at 1d359734, run as sealed; PROVED: m135's interior class
(kappa = 1) and m136's kappa = -1 classes are generation-shaped, one class on the two states' common double cover; the golden
form G fails. Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- Part A as banked (run_a.json): the eight characters of m135, both routes, class by class, and the mechanism;
- the census as banked (census_bc.json): no error, the routes agreeing, its level rows reproducing the sealed dry run; the
  read-out (read_out.json) reproduced in memory by read_out.py's own readers;
- the post-run records (disclosed in FINDINGS section 4): route S on m135 and m136, the kappa = -1 members in routes N and W,
  m136 exactly, the common double cover exactly;
- live: m136's kappa = -1 member and the common double cover in exact arithmetic over Q(zeta_24); m135's member in route E
  (slow);
- hygiene, and the verdict with its registry row."""
import base64
import hashlib
import importlib.util
import json
import re
import sys
import warnings
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1530_the_interior_extensions"
VER = ARC / "verification"
SEALED_SHA = "f39d185d006e0fc4095f50258f996412f8217d71a160f5d486601b574d8ac90a"
LOCAL = ("exact_lib", "exact_states", "route_n", "census_lib", "run_a", "census_bc", "read_out", "controls", "post_run_s",
         "post_run_b", "post_run_e136", "post_run_cover")


def _load(name):
    """this arc's module, its sibling imports resolved to this arc's files: generic names (read_out, controls) exist in other
    arcs, so a module of the same name left in sys.modules by another lock is dropped first"""
    warnings.filterwarnings("ignore")
    if str(VER) in sys.path:
        sys.path.remove(str(VER))
    sys.path.insert(0, str(VER))
    for other in LOCAL:
        mod = sys.modules.get(other)
        if mod is not None and Path(str(getattr(mod, "__file__", ""))).resolve().parent != VER.resolve():
            del sys.modules[other]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _json(name):
    return json.loads((VER / name).read_text(encoding="utf-8"))


def _pair(r):
    return (r["I(W)"], r["I(L2W)"])


@pytest.fixture(autouse=True)
def _mp_dps_60():
    """E12 (the b204 pattern): the numerical routes set mp.dps = 60 when imported, and tests/conftest.py restores each test's
    entry precision when it ends. A module imported by an earlier test would otherwise run here at 15 digits."""
    saved = mp.mp.dps
    mp.mp.dps = 60
    yield
    mp.mp.dps = saved


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    """every file the seal hashed is byte-identical (ARTIFACT_HASHES.txt)"""
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, rel = line.split(None, 1)
        assert hashlib.sha256((ARC / rel.strip()).read_bytes()).hexdigest() == digest, rel


# ------------------------------------------------------------------------------------------------- Part A
def test_part_a_as_banked():
    """m135's eight characters at kappa = 1: the routes agree everywhere; at u = (0, 1/2) and (1/2, 0) W1 reads (-1, -1) at
    the interior class in both routes (and at route N's own interior class), (0, -1) at every boundary-type class, W2 the
    negatives; the six simple members read (0, 0); the mechanism as FINDINGS section 0 states it"""
    A = _json("run_a.json")
    assert A["state"] == "-LLRR" and A["characters"] == 8 and A["routes agree everywhere"]
    nonsimple = [r for r in A["rows"] if not r["route E"]["simple"]]
    simple = [r for r in A["rows"] if r["route E"]["simple"]]
    assert sorted(tuple(r["u"]) for r in nonsimple) == [("0", "1/2"), ("1/2", "0")]
    assert len(simple) == 6
    for r in nonsimple:
        E, N = r["route E"], r["route N"]
        assert r["routes agree"]
        assert E["h1"] == {"V": 2, "V_eta": 2, "V (x) L": 2} and E["n"]["V_eta"] == 1 == N["interior"]
        assert _pair(E["W1"]["c_int"]) == _pair(N["W1"]["c_int"]) == (-1, -1)
        assert _pair(N["W1"]["route N's own interior class"]) == (-1, -1)
        for k in ("c_b", "c_b + c_int", "c_b - c_int", "c_b + 2 c_int"):
            assert _pair(E["W1"][k]) == _pair(N["W1"][k]) == (0, -1), k
        assert _pair(E["W2"]["c'_int"]) == (1, 1)
        assert _pair(E["W2"]["c'_b"]) == _pair(E["W2"]["c'_b + c'_int"]) == (0, 1)
        m = E["mechanism (route E)"]
        assert m["Jordan type of S0 on C at 1"] == [2, 2]
        assert m["x cup c_int = 0"] is True and m["x cup c_b = 0"] is True
        assert m["mu (the lift of c_int) in Lambda_A"] is False and m["dim Lambda_A"] == 2 and m["c_int lifts"] is True
        assert m["mu a P-coboundary"] is False and m["bit at c_b: e ^ c|_P in Lambda_A"] is False
    for r in simple:
        E, N = r["route E"], r["route N"]
        assert r["routes agree"] and E["h1"] == {"V": 1, "V_eta": 1, "V (x) L": 1}
        assert _pair(E["W1"]["the class"]) == _pair(N["W1"]["the class"]) == (0, 0) == _pair(E["W2"]["the class"])
        assert "route N's own interior class" not in N["W1"]


# ------------------------------------------------------------------------------------------------- the census and the read-out
def test_the_census_as_banked():
    """census_bc.json: the 541 rows without error; routes T and G agree everywhere they both read; rank and pairing agree in
    Part C"""
    C = _json("census_bc.json")
    assert C["manifolds"] == 541 and C["errors"] == []
    assert C["B"]["disagreements"] == [] and C["C"]["rank and pairing disagree"] == []
    states = {r["state"] for r in C["records"]}
    assert len(states) == 541 and {"-LLRR", "+LLRR"} <= states
    # Part B: route G reads h1 = 1 at kappa = -1 at exactly m136's two characters, route T agreeing at every comparison
    assert C["B"]["route G at kappa = -1, all characters"] == {"0": 47331, "1": 2}
    assert C["B"]["route G checks"] == 51677 and C["B"]["H0(F) != 0"] == []
    minus = sorted((h[0], h[2], h[3]) for h in C["B"]["route T: characters with h1 >= 1 at kappa != 1"] if h[4] == "-1")
    assert minus == [("+LLRR", "0", "1/2"), ("+LLRR", "1/2", "0")]
    others = {h[4] for h in C["B"]["route T: characters with h1 >= 1 at kappa != 1"] if h[4] != "-1"}
    assert others == {"omega", "omega^2"}
    # Part C: the meet is 0 at every chi, by rank and by pairing, with dimensions (2, 2)
    assert C["C"]["characters"] == 31489
    assert C["C"]["meet != 0 (rank)"] == [] and C["C"]["meet != 0 (pairing)"] == [] and C["C"]["dims not (2, 2)"] == []


def test_the_levels_reproduce_the_dry_run():
    """the census's rows on M2-M6 equal the sealed dry run's in every reading (seconds aside)"""
    C = {r["state"]: r for r in _json("census_bc.json")["records"]}
    D = _json("dry_run_bc.json")
    for r in D["records"]:
        c = C[r["state"]]
        assert c["D"] == r["D"]
        for key in ("route T: h1 >= 1 at", "route G at kappa = -1", "disagreements", "H0(F) != 0 at", "route G checks"):
            assert c["B"][key] == r["B"][key], (r["state"], key)
        for key in ("characters", "meet != 0 (rank)", "meet != 0 (pairing)", "dims not (2, 2)", "rank and pairing disagree"):
            assert c["C"][key] == r["C"][key], (r["state"], key)


def test_the_read_out_is_reproduced():
    """read_out.py's readers, applied in memory to run_a.json and census_bc.json, give read_out.json's predictions (nothing is
    written)"""
    ro = _load("read_out")
    A, BC = _json("run_a.json"), _json("census_bc.json")
    banked = _json("read_out.json")
    _, a_p, _ = ro.part_a(A)
    _, bc_p, members = ro.part_bc(BC)
    for k, v in {**a_p, **bc_p}.items():
        assert banked["predictions"][k] == v, k
    assert banked["verdict"].startswith("PROVED")
    assert banked["predictions"]["P2"] is True and banked["predictions"]["G"] is False
    assert banked["predictions"]["P6"] is False
    # the kappa = -1 members the read-out finds (by their fifth powers) are the ones post_run_b.py read
    hits = {(m[0], m[2], m[3]) for m in members["-1"]}
    read = {(r["state"], *r["nu^5 (the hit)"]) for r in _json("post_run_b.json")["rows"]}
    assert hits == read and ("+LLRR", "0", "1/2") in hits


# ------------------------------------------------------------------------------------------------- the post-run records
def test_route_s_records():
    """route S (SnapPy's presentation and holonomy, every character of order dividing 12): every comparison agrees; two
    generation-shaped readings on each state, at kappa = 1 on m135 and kappa = -1 on m136"""
    for tag, kappa, ident in (("mLLRR", "1", "m135"), ("pLLRR", "-1", "m136")):
        d = _json(f"post_run_s_{tag}.json")
        assert d["all comparisons agree"] and d["all checks"]
        assert any(x.startswith(ident) for x in d["SnapPy"]["identify"])
        gs = d["generation-shaped readings"]
        assert len(gs) == 2 and all(g[1] == kappa and tuple(g[3]) == (-1, -1) for g in gs)


def test_the_kappa_minus_one_members():
    """post_run_b.json: every member read in routes N and W at every basis class and the sum; all agree; all case (a)"""
    d = _json("post_run_b.json")
    assert d["routes agree everywhere"] and d["read"] == d["members"] >= 2
    assert "+LLRR" in d["states with members"]
    for r in d["rows"]:
        assert r["case"] == "(a)" and r["routes agree"] and r["interior"] == r["h1(V_eta)"]
        for v in r["readings"].values():
            assert v["route N"] == v["route W"]


def test_m136_exactly_as_banked():
    d = _json("post_run_e136.json")
    rows = {(tuple(r["u"]), r["kappa"]): r for r in d["rows"]}
    for u in (("0", "1/2"), ("1/2", "0")):
        r = rows[(u, "-1")]
        assert r["h1"] == {"V": 1, "V_eta": 1, "V (x) L": 1} and r["n (interior)"]["V_eta"] == 1
        assert _pair(r["W1"]["basis 0"]) == (-1, -1) and _pair(r["W2"]["basis 0"]) == (1, 1)
        assert r["mechanism"]["x cup basis 0 = 0"] is True
    for u in (("0", "0"), ("1/2", "1/2")):
        assert rows[(u, "-1")]["h1"]["V_eta"] == 0
    for u in (("0", "0"), ("0", "1/2"), ("1/2", "0"), ("1/2", "1/2")):
        assert _pair(rows[(u, "1")]["W1"]["basis 0"]) == (0, 0)


def test_the_common_double_cover_as_banked():
    d = _json("post_run_cover.json")
    assert d["Gamma_2"] == "+LLRRLLRR" and d["D"] == 32
    for r in d["rows"]:
        if r["nu(t_2)"] == "1":
            assert (r["h1"], r["interior"]) == (2, 1)
            assert tuple(r["W1"]["c_int"]) == (-1, -1) and tuple(r["W1"]["c_b"]) == (0, -1)
        else:
            assert r["h1"] == 0


# ------------------------------------------------------------------------------------------------- live
def test_m136_member_live_exactly():
    """m136 = +LLRR at u = (0, 1/2), kappa = -1: the exact four (sm:B1529's reader with sign +), h^1(V_eta) = 1, every class
    interior, W1 reads (-1, -1) and W2 (+1, +1), every identity asserted by exact_lib"""
    P = _load("post_run_e136")
    E = _load("exact_lib")
    S = _load("exact_states")
    sl2, _ = P.m136_sl2()
    G, img, chars, D = S.group("+", "LLRR")
    rho = S.four_module(sl2)
    assert rho.check(G.rels)
    ch = S.nu("+", (Fraction(0), Fraction(1, 2)), Fraction(1, 2))
    V = rho.twist(ch)
    CE = E.Cohomology(G, rho.twist(S.power_char(ch, 5)))
    assert CE.h1 == 1 and CE.n == 1
    W1 = E.extension(V, CE.reps[0], None)
    assert W1.check(G.rels)
    assert E.class_index(G, W1)["I"] == -1 and E.class_index(G, W1.wedge2())["I"] == -1
    CEd = E.Cohomology(G, rho.twist(S.power_char(ch, 5)).dual())
    W2s = E.extension(V.dual(), CEd.reps[0], None)
    assert E.class_index(G, W2s)["I"] == -1 and E.class_index(G, W2s.wedge2())["I"] == -1     # W2 reads (+1, +1)


def test_the_common_double_cover_live_exactly():
    """+LLRRLLRR with m136's exact four and t -> t^2, at u = (0, 1/2) and nu(t_2) = 1: h^1 = 2 with one interior class,
    which reads (-1, -1)"""
    P = _load("post_run_e136")
    E = _load("exact_lib")
    S = _load("exact_states")
    m136, _ = P.m136_sl2()
    G, img, chars, D = S.group("+", "LLRRLLRR")
    rho = S.four_module({"a": m136["a"], "b": m136["b"], "t": E.mmul(m136["t"], m136["t"])})
    assert rho.check(G.rels)
    V = rho.twist(S.nu("+", (Fraction(0), Fraction(1, 2)), 0))
    CV = E.Cohomology(G, V)
    assert (CV.h1, CV.n) == (2, 1)
    c = CV.combine(CV.interior()[0])
    W1 = E.extension(V, c, None)
    assert E.class_index(G, W1)["I"] == -1 and E.class_index(G, W1.wedge2())["I"] == -1


@pytest.mark.slow
def test_m135_member_live_route_e():
    """m135 at u = (0, 1/2): route E's reading of Part A, rebuilt (run_a.route_e): (-1, -1) at c_int, (0, -1) at c_b, mu
    outside Lambda_A"""
    R = _load("run_a")
    S = _load("exact_states")
    G, img, chars, D = S.group("-", "LLRR")
    rho = S.four_module(S.m135_sl2())
    row, classes, _ = R.route_e(G, img, "-", rho, (Fraction(0), Fraction(1, 2)))
    assert _pair(row["W1"]["c_int"]) == (-1, -1) and _pair(row["W1"]["c_b"]) == (0, -1)
    assert row["mechanism (route E)"]["mu (the lift of c_int) in Lambda_A"] is False


# ------------------------------------------------------------------------------------------------- hygiene
def test_hygiene():
    """no vendor word or the private term in the arc; the Gate 5-Q words stay out (Q5)"""
    words = [base64.b64decode(x).decode() for x in ("Y2xhdWRl", "YW50aHJvcGlj", "b3B1cw==", "c29ubmV0", "ZmFibGU=")]
    words.append(bytes([98, 114, 97, 118, 101]).decode())
    words += [base64.b64decode(x).decode() for x in ("cXVhbGlh", "YXdhcmU=", "c2Vlcw==")]
    for p in sorted(ARC.rglob("*")):
        if p.is_file() and p.suffix in (".md", ".py", ".txt"):
            t = p.read_text(encoding="utf-8", errors="ignore").lower()
            for w in words:
                assert not re.search(r"\b" + re.escape(w) + r"\b", t), (p.name, w[:2])


def test_the_verdict_and_its_row():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1530" and v["verdict"] == "PROVED"
    assert v["prior_work"]["standing"] == "EXTENDS" and v["scope"]["frame"] == "F-HE"
    assert "B1530" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")


def test_the_kill_record_and_the_withdrawn_bound():
    """the no-go half is in the kill graph (G, the golden form, refuted by the silver counterexamples), and FINDINGS section 7
    withdraws the one-sided two-generation bound rather than stating it"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1530"]
    assert len(rec) == 1 and rec[0]["kill_form"].startswith("silver-not-golden")
    assert rec[0]["scope"]["frame"] == "F-HE" and rec[0]["fact_computed"] is True
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    sec7 = f[f.index("## 7."):f.index("## Files")]
    assert "A bound withdrawn" in sec7 and "So the count on any such cover is at most two generations" not in f
    assert "Seen first" in f and "sweep" in f and "literature" in f
