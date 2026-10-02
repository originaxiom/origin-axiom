"""B1514 lock -- THE DECOUPLING LAW (2026-10-02). B1513's leads 1 and 2: is "a chiral state does not couple to a Higgs class of
its background" a law of B1509's harmonic frame?  Tested on B1511's case (b), the opposite-sign 10bar' on M4, M5 and M6 (18
groups, 184 members); sealed at a0badfa3 before any Higgs class, coupling or joining form at a case-(b) member was computed;
PROVED.  Run by two routes that share no code (the owner's rule NO NEGATIVE FROM A BUG): route T, the relative triple product
(census.py on law_lib.py), and route L, the lifting criterion (independent_route.py on lift_route.py).
Locked here:
- the seal's digest and markers;
- the controls' record (K1-K6, 803 checks);
- both routes' records: Part 0, the readings table of FINDINGS Section 3, Part B's form counts, Part C's predictions and checks,
  the agreement, and the disjoint primes;
- the post-run records (a)-(d) and (e), case (a) through level 6;
- live:
  - the first member of every group by both routes at a recorded prime-root, equal to the recorded rows;
  - the joining forms at one M4 orbit by both routes: the own triple carries one form, the wedge form; cross triples that pass the
    character test carry none;
  - the character test on all 34 orbits (12, 20 and 18 passing cross triples per orbit of four, five and six);
  - W2's chiral 10' decoupled and the interior 10' at w = 7 coupled to itself, by both routes;
  - case (a): B1509's join pulled back to M_4 decoupled and the +-i control on M_5 non-zero, by both routes; the factorisation
    behind the transfer argument;
- route L's independence from route T's code (AST);
- the kill-graph entry, the verdict, the findings' load-bearing sentences, and hygiene.
The sealed runs (about 40 minutes each) are not rerun; the controls' rerun (about two minutes) is marked slow."""
import ast
import functools
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1514_the_decoupling_law"
VER = ARC / "verification"
SEALED_SHA = "12aa1edd7819cf9d7848d2b34e55420d631e11825c890cbf626848651e08c014"

PREDICTIONS = {
    "P1 the twisted Higgs bulk Lambda^2 V is acyclic at every member": True,
    "P2 the Higgs content reads as Lemma 4 (M4 none; M5 h1(V); M6 one)": True,
    "P3 the 10bar' coupling to every 5bar'_H vanishes at every member": True,
    "P4 the 10' coupling is non-zero at some member with a Higgs class": True,
    "P5 some cross triple carries a joining form": False,
    "P6 every cross coupling through a joining form vanishes": True,
    "P7 no chiral state through level 6 couples to a Higgs class (with B1513)": True,
}
# (h0, h1, h2 of Lambda^2 V; h1 of V (x) L, Lambda^2 W1, Lambda^2 W1*, W1, W1*; interior classes of W1, W1*;
#  the 10bar' coupling zero; the 10' coupling zero): FINDINGS Section 3's table
SIMPLE = (0, 0, 0, 1, 1, 1, 1, 2, 1, 0, True, False)
TABLE = {"M4": (0, 0, 0, 0, 0, 0, 1, 2, 1, 0, True, True), "M5 lam = 1": (0, 0, 0, 2, 2, 2, 2, 3, 2, 1, True, False)}


def _load(name):
    if str(VER) not in sys.path:
        sys.path.insert(0, str(VER))
    spec = importlib.util.spec_from_file_location(name, VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@functools.lru_cache(maxsize=None)
def _modules():
    """this arc's modules, loaded by path in dependency order so that their plain imports resolve to this arc's files"""
    mods = {}
    for name in ("law_lib", "lift_route", "census", "independent_route", "post_run_checks", "case_a_levels"):
        mods[name] = _load(name)
    return mods


@functools.lru_cache(maxsize=None)
def _record(name):
    return json.loads((VER / f"{name}_run.txt").read_text(encoding="utf-8"))


def _bools(d):
    if isinstance(d, dict):
        return [b for v in d.values() for b in _bools(v)]
    if isinstance(d, list):
        return [b for v in d for b in _bools(v)]
    return [d] if isinstance(d, bool) else []


def _prime_root(arithmetic):
    m = re.match(r"GF\((\d+)\), q = (\d+)$", arithmetic)
    return (int(m.group(1)), int(m.group(2))) if m else None


def _signature(row):
    h = row["h"]
    k10b = next(k for k in row if k.startswith("10bar'"))
    k10 = next(k for k in row if k.startswith("10' "))
    return (h["L2V"]["h0"], h["L2V"]["h1"], h["L2V"]["h2"], h["VL"]["h1"], h["L2W"]["h1"], h["L2W*"]["h1"], h["W1"]["h1"],
            h["W1*"]["h1"], row["interior"]["W1"], row["interior"]["W1*"], row[k10b]["zero"], row[k10]["zero"])


def _expected(population):
    if population.startswith("M4"):
        return TABLE["M4"]
    if population.startswith("M5") and population.endswith("lam = 1"):
        return TABLE["M5 lam = 1"]
    return SIMPLE


def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_controls_record():
    """K1-K6 as recorded before the seal: every one of the 803 checks holds"""
    c = _record("controls")
    b = _bools(c)
    assert len(b) == 803 and all(b)
    assert c["K1"] == {"members per prime-root": 184, "pass": True, "populations": 18, "routes read the same populations": True}
    assert [c["K2"][f"level {n}"]["cells"] for n in (4, 5, 6)] == [199, 492, 1259]
    assert c["K5"]["triplet (banked zero), route T"] == [True] * 3 and c["K5"]["triplet (banked zero), route L"] == [True] * 3
    assert all((r["dim End"], r["dim Hom(L2 rho, rho)"], r["dim Hom(rho rho, rho)"]) == (1, 0, 0) for r in c["K6"]["rows"])


@pytest.mark.parametrize("route, readings, nD", [("census", 1120, 8), ("independent_route", 1672, 9)])
def test_each_routes_record(route, readings, nD):
    """Part 0 passed; every reading falls on its row of FINDINGS Section 3's table, with the control fired, the cusp acyclic and
    the forms symmetric; the predictions and the D-checks as banked"""
    r = _record(route)
    assert r["0_banked_identity"]["pass"] is True
    rows = [(blk["population"], row) for blk in r["A"] for row in blk["rows"]]
    assert len(rows) == r["C"]["readings"] == readings
    assert len({pop for pop, _ in rows}) == 18
    for pop, row in rows:
        assert _signature(row) == _expected(pop), (pop, row["member"])
        assert row["cusp acyclic"] is True and next(v for k, v in row.items() if k.startswith("control")) is True
        for k in row:
            if k.startswith("10"):
                assert row[k]["symmetric"] is True and row[k].get("blocks ok", True) is True
    exact = [blk for blk in r["A"] if blk["arithmetic"].startswith("exact")]
    assert len(exact) == 2 and all(blk["population"].startswith("M4") and len(blk["rows"]) == 4 for blk in exact)
    assert r["C"]["predictions"] == PREDICTIONS
    assert len(r["C"]["D"]) == nD and all(v is True for v in r["C"]["D"].values())
    assert r["C"]["cross couplings computed"] == 0


@pytest.mark.parametrize("route", ["census", "independent_route"])
def test_each_routes_joining_forms(route):
    """Part B: the 184 own triples carry exactly one form; none of the 5 400 cross triples carries any"""
    r = _record(route)
    own = cross = 0
    assert len(r["B"]) == 18
    for g in r["B"]:
        for o in g["orbits"].values():
            assert o["cross couplings"] == {}
            if "own: the wedge form lies in the form space" in o:
                assert all(o["own: the wedge form lies in the form space"])
            for t, dim in o["triples"].items():
                i, j, k = map(int, t.split(","))
                if i == j == k:
                    own += 1
                    assert dim == 1, t
                else:
                    cross += 1
                    assert dim == 0, t
    assert (own, cross) == (184, 5400)


def test_the_routes_agree_on_disjoint_primes():
    """route L's comparison with route T's record passes on all 18 groups; the routes used 9 and 19 primes, none shared"""
    agr = _record("independent_route")["C"]["agreement with route T"]
    assert agr["pass"] is True and agr["predictions agree"] is True
    groups = {k: v for k, v in agr.items() if isinstance(v, dict)}
    assert len(groups) == 18 and all(v["same readings"] and v["route L"] == v["route T"] for v in groups.values())
    primes = [{pr[0] for blk in _record(r)["A"] if (pr := _prime_root(blk["arithmetic"]))} for r in ("census", "independent_route")]
    assert (len(primes[0]), len(primes[1])) == (9, 19) and not primes[0] & primes[1]


def test_the_post_run_record():
    """(a) the interior 10' at w = 7 couples, to itself too; (b) H^1(V) -> H^1(W1) an isomorphism; (c) W2's chiral 10' decoupled;
    (d) where the non-zero 10' couplings sit; both routes wherever both ran"""
    p = _record("post_run_checks")
    s = p["summary"]
    assert s["(a) the interior 10' at w = 7 couples (both routes)"] == [True, True] and s["(a) routes agree"]
    assert s["(a) the self-coupling B(f_int, f_int): route T, any 5'_H"] == [True, True] and s["(a) the self-coupling: routes agree"]
    assert s["(b) H^1(V) -> H^1(W1) is an isomorphism at every group"]
    assert s["(c) W2's chiral 10' decouples at every group (both routes)"] and s["(c) routes agree on W2"]
    assert sorted(p["a"]) == ["M5 [12, 19] lam = 1", "M5 [15, 18] lam = 1"]
    for v in p["a"].values():
        assert v["route T"]["interior 10' classes"] == 1 and v["route T"]["Higgs"] == 2
        assert v["route T"]["self-coupling B(f_int, f_int) non-zero, per 5'_H"] == [[True, True]]
        assert v["route L"]["self-class [f_int ^ f_int] non-zero in H^2(Lambda^2 W1*)"] == [True]
    assert len(p["b"]) == 18
    for pop, v in p["b"].items():
        n = 2 if pop.startswith("M5") and pop.endswith("lam = 1") else 1
        assert (v["h1(V)"], v["rank of H^1(V) -> H^1(W1)"], v["h1(W1)"], v["isomorphism"]) == (n, n, n, True), pop
    assert len(p["c"]) == 18
    for pop, v in p["c"].items():
        w7 = pop.startswith("M5") and pop.endswith("lam = 1")
        higgs = 0 if pop.startswith("M4") else (2 if w7 else 1)
        assert v["route T"] == {"Higgs 5'_H of W2": higgs, "h1(W2)": 3 if w7 else 2, "h1(W2*)": 2 if w7 else 1,
                                "the 10' coupling of W2 is zero": True}, pop
        assert v["route L"] == {"h1(W2)": 3 if w7 else 2, "h1(W2*)": 2 if w7 else 1, "the 10' coupling of W2 is zero": True}, pop
    for pop, v in p["d"].items():
        w7 = pop.startswith("M5") and pop.endswith("lam = 1")
        if pop.startswith("M4"):
            assert v == [{"10' coupling zero": True, "Higgs": 0, "interior 10'": 0}]
        else:
            assert v == [{"10' coupling zero": False, "Higgs": 2 if w7 else 1, "interior 10'": 1 if w7 else 0}], pop


def test_the_case_a_record():
    """post-run (e): the join pulled back to M_1..M_6 and the triplet on M_6 have one 5'_H and a zero 10' coupling on all of
    H^1(W*), by both routes on disjoint primes; the +-i control pulled back to M_5 is non-zero by both"""
    r = _record("case_a_levels")
    s = r["summary"]
    assert s["case (a) through level 6: one 5'_H, the 10' coupling zero on all of H^1(W*), both routes"] is True
    assert s["positive control on M_5 non-zero, both routes"] is True
    assert s["readings (zeros), route T / route L"] == [36, 36] and s["levels of the join read"] == [1, 2, 3, 4, 5, 6]
    pT, pL = map(set, s["primes, route T / route L"])
    assert (len(pT), len(pL)) == (9, 13) and not pT & pL
    rows = r["join pulled back to M_n"] + r["triplet on M_6"]
    assert all(x["h1(V)"] == 1 and x["h1(Lambda^2 W)"] == 1 and x["h1(W*)"] == 2 for x in rows)
    assert all(x["coupling zero on all of H^1(W*)"] and x["interior 10'"] == 1 for x in rows if x["route"] == "T")
    assert all(x["B == 0 on H^1(W*)"] and x["mu-type pairing == 0"] and x["cross terms [a_i ^ e f0] zero"] and x["blocks check"]
               for x in rows if x["route"] == "L")
    ctl = r["control: +-i point pulled back to M_5"]
    assert len(ctl) == 8 and all(not x.get("coupling zero on all of H^1(W*)", False) and not x.get("B == 0 on H^1(W*)", False)
                                 for x in ctl)


def test_the_case_a_transfer_factorisation():
    """at the join's q (q^2 - 34 q + 1 = 0), B1509's Q = -q (s + 1)^2 (s^2 - 10 s + 1): no root on the unit circle but -1"""
    import sympy as sp
    q, s = sp.symbols("q s")
    Q = -q * s ** 4 + 8 * q * s ** 3 + (q ** 2 - 16 * q + 1) * s ** 2 + 8 * q * s - q
    assert sp.rem(sp.expand(Q + q * (s + 1) ** 2 * (s ** 2 - 10 * s + 1)), q ** 2 - 34 * q + 1, q) == 0
    assert all(abs(abs(complex(x)) - 1) > 0.5 for x in sp.solve(s ** 2 - 10 * s + 1, s))


def test_case_a_live():
    """live, both routes: B1509's join pulled back to M_4 decouples; B1510's +-i point pulled back to M_5 does not"""
    M = _modules()
    CA, LT, LR = M["case_a_levels"], M["law_lib"], M["lift_route"]
    H, T, IA = LT.H, LT.T, LR.IA
    r = _record("case_a_levels")
    G = H.FibredGroup(4)
    C, z, _ = G.fundamental()
    row = next(x for x in r["join pulled back to M_n"] if x["route"] == "T" and x["level"] == 4)
    field = T.Field("gf", p=row["p"], r=row["q"])
    one = field.dom.one
    got = CA.route_T(G, C, z, field, {"x": one, "y": one, "t": one})
    assert got == {k: v for k, v in row.items() if k not in ("route", "level", "p", "q")}
    row = next(x for x in r["join pulled back to M_n"] if x["route"] == "L" and x["level"] == 4)
    got = CA.route_L(IA.ModP(row["p"], "lock"), row["q"], 4, (1, 1, 1), "join M4")
    assert got == {k: v for k, v in row.items() if k not in ("route", "level", "p", "q")} and got["B == 0 on H^1(W*)"]
    ctl = next(x for x in r["control: +-i point pulled back to M_5"] if x["route"] == "L")
    F = IA.ModP(ctl["p"], "lock")
    got = CA.route_L(F, ctl["q"], 5, (1, 1, IA.sqrt_m1(ctl["p"])), "control M5")
    assert got["h1(V)"] == 1 and got["B == 0 on H^1(W*)"] is False


def test_both_routes_live_at_every_group():
    """live: the first member of every group, by both routes, at each route's first recorded prime-root, equals the recorded
    row (dimensions, interior classes, control, both couplings)"""
    M = _modules()
    LT, CT, IR = M["law_lib"], M["census"], M["independent_route"]
    H, T, LR, IA = LT.H, LT.T, IR.LR, IR.LR.IA
    first = {}
    for route in ("census", "independent_route"):
        for blk in _record(route)["A"]:
            pr = _prime_root(blk["arithmetic"])
            if pr and (route, blk["population"]) not in first:
                first[(route, blk["population"])] = (pr, blk["rows"][0])
    groups = {}
    for pop in LT.populations():
        n, ab = pop["level"], next(iter(pop["orbits"].values()))[0]
        if n not in groups:
            G = H.FibredGroup(n)
            groups[n] = (G,) + G.fundamental()[:2]
        G, C, z = groups[n]
        (p, r), rec = first[("census", pop["label"])]
        field = T.Field("gf", p=p, r=r, iota=T.gf_root_of_unity(p, 4) if "i" in pop["lam"] else None)
        row, _ = CT.read_member(G, C, z, field, H.rho_mats(G, field), ab, pop["N"], LT.lam_value(field, pop["lam"]))
        assert json.loads(json.dumps(row)) == rec, ("route T", pop["label"])
        (p, r), rec = first[("independent_route", pop["label"])]
        F = IA.ModP(p, "lock")
        iota = IA.sqrt_m1(p) if "i" in pop["lam"] else None
        (_, _), Nr = LR.reduce_char(ab, pop["N"])
        row, _ = IR.read_member(F, IA.mn_mats(F, r), n, ab, pop["N"], IR.lam_residue(pop["lam"], p, iota), LR.root_of_unity(p, Nr))
        assert json.loads(json.dumps(row)) == rec, ("route L", pop["label"])


def _passes(vk, vi, vj, N):
    """the character test for an invariant on a graded piece of Lambda^2 W_k* (x) W_i (x) W_j (the t-part always passes inside
    a group): nu_i nu_j = nu_k^2 (the wedge piece), or nu_k^3 nu_i = nu_j^4, or nu_k^3 nu_j = nu_i^4 (the line pieces)"""
    zero = lambda *terms: all(sum(c * v[s] for c, v in terms) % N == 0 for s in range(2))  # noqa: E731
    return zero((1, vi), (1, vj), (-2, vk)) or zero((3, vk), (1, vi), (-4, vj)) or zero((3, vk), (-4, vi), (1, vj))


def test_the_character_test_on_every_orbit():
    """live: every one of the 34 orbits has cross triples that pass the character test (12, 20 and 18 per orbit of four, five
    and six), so the characters alone do not decide P5; the form solvers did (none of 5 400)"""
    LT = _modules()["law_lib"]
    counts = []
    for pop in LT.populations():
        for orb in pop["orbits"].values():
            n = len(orb)
            c = sum(_passes(orb[k], orb[i], orb[j], pop["N"]) for k in range(n) for i in range(n) for j in range(n)
                    if not i == j == k)
            counts.append((n, c))
    assert len(counts) == 34 and sorted(set(counts)) == [(4, 12), (5, 20), (6, 18)]


def test_the_joining_forms_live():
    """live, at an M4 orbit by both routes: the own triple carries one form, which is the wedge form (route T); the first two
    cross triples that pass the character test carry none"""
    M = _modules()
    LT, CT, LR = M["law_lib"], M["census"], M["lift_route"]
    H, T, IA = LT.H, LT.T, LR.IA
    pop = next(p for p in LT.populations() if p["label"] == "M4 orbit [0, 5]")
    orb = pop["orbits"]["[0, 5]"]
    crosses = [(k, i, j) for k in range(4) for i in range(4) for j in range(4)
               if not i == j == k and _passes(orb[k], orb[i], orb[j], 15)][:2]
    assert len(crosses) == 2
    bT = next(b for b in _record("census")["B"] if b["population"] == pop["label"])
    G = H.FibredGroup(4)
    field = T.Field("gf", p=bT["p"], r=bT["q"])
    rho = H.rho_mats(G, field)
    W = [LT.Member(G, field, rho, ab, 15, field.dom.one).W1 for ab in orb]
    dim, basis = LT.form_space(W[0], W[0], W[0], bT["p"])
    assert dim == 1 and CT.flint_rank([CT.wedge_vector()] + basis, bT["p"]) == 1
    assert all(LT.form_space(W[k], W[i], W[j], bT["p"])[0] == 0 for (k, i, j) in crosses)
    bL = next(b for b in _record("independent_route")["B"] if b["population"] == pop["label"])
    F = IA.ModP(bL["p"], "lock")
    mn = IA.mn_mats(F, bL["q"])
    WL = [LR.Member(F, mn, 4, ab, 15, 1, LR.root_of_unity(bL["p"], LR.reduce_char(ab, 15)[1])).W1 for ab in orb]
    assert LR.form_space(WL[0], WL[0], WL[0])[0] == 1
    assert all(LR.form_space(WL[k], WL[i], WL[j])[0] == 0 for (k, i, j) in crosses)


def test_the_post_run_checks_live():
    """live, both routes: at M5's double point the interior 10' couples to itself; at an M6 group W2's chiral 10' does not couple
    to W2's 5'_H"""
    M = _modules()
    LT, LR, PR = M["law_lib"], M["lift_route"], M["post_run_checks"]
    H, T, IA = LT.H, LT.T, LR.IA
    pops = {p["label"]: p for p in LT.populations()}
    rec = _record("post_run_checks")
    for label, part in (("M5 [12, 19] lam = 1", "a"), ("M6 [32, 34] lam = -1", "c")):
        pop, n = pops[label], pops[label]["level"]
        p, r = rec[part][label]["p"], rec[part][label]["q"]
        G = H.FibredGroup(n)
        C, z, _ = G.fundamental()
        iota = T.gf_root_of_unity(p, 4) if "i" in pop["lam"] else None
        field = T.Field("gf", p=p, r=r, iota=iota)
        ab = next(iter(pop["orbits"].values()))[0]
        mT = LT.Member(G, field, H.rho_mats(G, field), ab, pop["N"], LT.lam_value(field, pop["lam"]))
        F = IA.ModP(p, "lock")
        lamL = {"1": 1, "-1": p - 1}[pop["lam"]]
        mL = LR.Member(F, IA.mn_mats(F, r), n, ab, pop["N"], lamL, LR.root_of_unity(p, LR.reduce_char(ab, pop["N"])[1]))
        if part == "a":
            t, l = PR.interior_10_T(G, C, z, mT), PR.interior_10_L(mL)
            assert t["self-coupling B(f_int, f_int) non-zero, per 5'_H"] == [[True, True]]
            assert l["self-class [f_int ^ f_int] non-zero in H^2(Lambda^2 W1*)"] == [True]
        else:
            assert PR.w2_coupling_T(G, C, z, mT) == rec["c"][label]["route T"]
            assert PR.w2_coupling_L(mL) == rec["c"][label]["route L"]


def test_route_L_shares_no_code_with_route_T():
    """route L imports nothing of route T, B1513's higgs_lib or B1511's tower_lib: lift_route.py loads only B1513's independent
    audit (by path), and independent_route.py only lift_route.py (route T's record is read as data for the comparison)"""
    allowed = {"lift_route.py": {"importlib.util", "json", "math", "pathlib", "numpy", "sympy"},
               "independent_route.py": {"json", "sys", "time", "pathlib", "numpy", "sympy", "lift_route"}}
    for fname, ok in allowed.items():
        src = (VER / fname).read_text(encoding="utf-8")
        tree = ast.parse(src)
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names |= {a.name for a in node.names}
            elif isinstance(node, ast.ImportFrom):
                names.add(node.module or "")
        assert names <= ok, (fname, names - ok)
        calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
        named = {n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, "id", "") for n in calls}
        assert not named & {"import_module", "__import__"}, fname
        specs = [ast.get_source_segment(src, n) for n in calls
                 if isinstance(n.func, ast.Attribute) and n.func.attr == "spec_from_file_location"]
        if fname == "lift_route.py":
            assert len(specs) == 1 and "B1513_the_triplets_higgs_sector/verification/independent_audit.py" in specs[0]
        else:
            assert not specs
        for bad in ("law_lib", "higgs_lib", "tower_lib", "census", "extension_index", "post_run_checks", "controls"):
            assert not re.search(rf"^\s*(import|from)\s+{bad}\b", src, re.M), (fname, bad)


@pytest.mark.slow
def test_the_controls_rerun():
    """K1-K6 (about two minutes) pass again"""
    for name in ("law_lib", "lift_route"):
        _load(name)
    K = _load("controls")
    rec = K.main()
    assert rec["all pass"] is True and len(_bools(rec)) == 803 and all(_bools(rec))


def test_the_kill_graph_entry():
    """the no-go content is routed with content (B1207's A3), as for B1509-B1511's PROVED arcs"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1514"]
    assert len(rec) == 1
    r = rec[0]
    assert r["fact_computed"] is True and r["routed_from"] == "sm-branch-2026-10-02-banking"
    assert r["kill_form"].startswith("subbundle-decoupling") and len(r["hatch"]) > 80
    assert "tests/test_b1514_the_decoupling_law.py" in r["note"] and "B833" in r["depth_note"]


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED and creates a law (registry row present), keeps 0 of 19; the findings carry the answer, the
    predictions, the lemmas, the post-run checks and the leads; the owner's private term is absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1514" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["identifications"] == []
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    assert "B1514" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "THE DECOUPLING LAW (B1514)" in (ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**Verdict:** PROVED", "**The answer (both routes).**", "**The twisted Higgs bulk is acyclic at every member**",
                   "**The chiral 10̄′ couples to none of them** (P3 YES)", "**No form joins two members of an orbit** (P5 NO)",
                   "| P5 | some cross triple carries a joining form (50%) | **NO**: 0 of 5 400 |",
                   "**Lemma 3 (the sub-wedge lemma).**", "B(f_int, f_int) ≠ 0", "the analogue in this frame is not proved",
                   "**Post-run check (a) extended after its first run.**", "**(e) Case (a) through level 6**",
                   "**A bug in post-run (e), caught before banking.**", SEALED_SHA, "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for path in list(ARC.glob("*.md")) + list(VER.glob("*.py")) + [ARC / "arc_verdict.json"]:
        assert term not in path.read_text(encoding="utf-8").lower(), path
