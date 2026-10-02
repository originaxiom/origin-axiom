"""B1515 lock -- THE HYPERBOLIC POINT (2026-10-02). The owner's "go" after B1514: can one configuration carry both halves of a
generation?  A 5bar' needs torus cohomology of Lambda^2 W, which on m004's harmonic family happens only at q = 1.  Sealed at
b36f6d8e before any index at q = 1 was computed; run by two routes that share no code (the owner's rule NO NEGATIVE FROM A BUG):
route T (census_t.py on B1511's tower_lib) and route L (census_l.py on B1513's audit backends, the interior dimension from one
joint system).  PROVED by the sealed rule: P5 fails at 24 order-8 members of M6, which carry (I(W1), I(Lambda^2 W1)) = (+1, -1),
a 10bar' and a 5bar' (anomaly -2); no member through level 6 is generation-shaped.
Locked here:
- the seal's digest and markers;
- the controls' record (S1-S7, K1-K6, C);
- both routes' records: Part 0, the table of FINDINGS Section 3, the D-checks, the predictions, the members with both, the agreement
  on all 3048 keys and the disjoint primes; the sign pattern in both records;
- the post-run record (a)-(d);
- live: the torus table on one level (exact); one member of each kind on M4 and M6 by both routes at a recorded prime; the 'both'
  member (1/8, 1/2) exactly over Q(zeta_8); Wang's kernel at the four orbits;
- route L's independence from route T's code (AST);
- the kill-graph entry, the verdict, the findings' load-bearing sentences, and hygiene.
The sealed runs (13 and 7 minutes) are not rerun; the controls' rerun is marked slow."""
import ast
import functools
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1515_the_hyperbolic_point"
VER = ARC / "verification"
SEALED_SHA = "5644a92c4c13d17f4663e74b16e9e0fafa8c86a16b2ce895e8b16871faf411db"
PREDICTIONS = {
    "P1 every lam = 1 member is simple": False,
    "P2 population B is empty": True,
    "P3 off the deck coincidence, simple case (b): I(W1) = 0": True,
    "P4 I(Lambda^2 W1) = 0 at every member (every class read)": False,
    "P4 mechanism: Lambda_A meets pi_A in 0 at every simple member": True,
    "P5 no member carries both a non-zero I(W1) and a non-zero I(Lambda^2 W1)": False,
}
BOTH_REPS = [("1/8", "1/2"), ("1/8", "5/8"), ("1/8", "7/8"), ("1/4", "3/8")]


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
    return {name: _load(name) for name in ("route_l", "route_t", "census_t", "census_l", "post_run_checks")}


@functools.lru_cache(maxsize=None)
def _record(name):
    return json.loads((VER / f"{name}_run.txt").read_text(encoding="utf-8"))


def _primary(d):
    return d["c1"] if len(d) == 1 else d["generic"]


def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_controls_record():
    """S1-S7, K1-K6 and C as recorded before the seal"""
    c = _record("controls")
    assert all(c["summary"].values()) and len(c["summary"]) == 9
    assert c["S1"]["signature (+, -)"] == [3, 1] and c["S1"]["invariant symmetric forms (dimension)"] == 1
    for lev in range(1, 7):
        s = c["S2-S6"][f"M{lev}"]
        assert s["torus table (dim of invariants)"]["W1 [z1 + k z2]"] == [1, "never drops"]
        assert s["torus table (dim of invariants)"]["L2W1* [z1 + k z2]"] == [3, "never drops"]
        assert s["dim pi_A"] == 2 and all(s["T-deck: m acts trivially on H^1(P)"].values())
    assert c["S7"]["Q(1, s)"] == "-(s - 1)**2*(s**2 - 6*s + 1)"
    assert len(c["K6"]["route T"]) == 6 and len(c["K6"]["route L"]) == 6


def test_route_T_record():
    """Part 0 passed; 1023 full readings and 5115 member tests; every D-check holds; the predictions as banked; the table of
    FINDINGS Section 3"""
    r = _record("census_t")
    assert r["Part 0"]["passed"] is True and len(r["A"]) == 1023 and len(r["B"]) == 5115
    assert all(r["C"]["D"].values()) and len(r["C"]["D"]) == 14
    assert r["C"]["P"] == PREDICTIONS
    both = r["C"]["members with both"]
    assert len(both) == 192 and {(m["level"], m["I(W1)"], m["I(L2W1)"]) for m in both} == {(6, 1, -1)}
    assert len({tuple(m["char"]) for m in both}) == 24
    tab = r["C"]["table (one prime per level)"]
    assert [tab[f"M{n}"]["members (lam = 1)"] for n in range(1, 7)] == [1, 5, 16, 45, 121, 320]
    m6 = tab["M6"]["distribution"]
    assert m6["case b, simple False, coincident True: (I(W1), I(L2W1)) = (1, -1)"] == 24
    assert m6["case b, simple True, coincident True: (I(W1), I(L2W1)) = (1, 0)"] == 24
    assert m6["case b, simple False, coincident False: (I(W1), I(L2W1)) = (0, 0)"] == 100
    assert tab["M5"]["distribution"]["case b, simple True, coincident True: (I(W1), I(L2W1)) = (1, 0)"] == 20
    assert tab["M4"]["distribution"]["case b, simple True, coincident True: (I(W1), I(L2W1)) = (1, 0)"] == 8
    assert not r["C"]["population B members"]


def test_route_L_record_and_the_agreement():
    """route L's Part 0 and its own checks; the comparison: all 3048 keys agree, primes disjoint; the class dependence at the 24"""
    r = _record("census_l")
    assert r["Part 0"]["passed"] is True and len(r["A"]) == 1531 and len(r["B"]) == 7655
    C = r["C"]
    for k in ("route L: every field reads the same", "route L: readings constant on deck orbits", "route L: pieces have index 0",
              "route L: indices vanish off mu_4 (W) and off mu_2 u mu_3 (Lambda^2 W)", "route L: mirror I(W2) = -I(W1), I(L2W2) = -I(L2W1)"):
        assert C[k] is True, k
    assert C["route L: P4 I(Lambda^2 W1) = 0 at every member"] is False and C["route L: P5 no member with both"] is False
    assert not C["route L: population B members"]
    comp = C["comparison with route T"]
    assert comp["agree everywhere"] is True and comp["keys read by both"] == 3048 and not comp["disagreements"]
    assert comp["primes disjoint"] is True
    tchars = {tuple(m["char"]) for m in _record("census_t")["C"]["members with both"]}
    assert {tuple(m["char"]) for m in C["route L: members with both"]} == tchars
    cnt = Counter((c, v["W1"]["I"], v["L2W1"]["I"]) for x in r["A"] if x["level"] == 6 and tuple(x["char"]) in tchars
                  for c, v in x["row"]["W1"].items())
    assert cnt == Counter({("c1", 0, -1): 72, ("c2", 1, -1): 72, ("c1+c2", 1, -1): 72, ("generic", 1, -1): 72})


@pytest.mark.parametrize("name, key", [("census_t", "T"), ("census_l", "L")])
def test_the_sign_pattern(name, key):
    """at every member, class and field: I(W1) in {0, 1}, I(Lambda^2 W1) in {0, -1}; never equal and non-zero"""
    r = _record(name)
    seen = set()
    for x in r["A"] + r["B"]:
        if "pieces" not in x["row"]:
            continue
        for v in x["row"]["W1"].values():
            seen.add((v["W1"]["I"], v["L2W1"]["I"]))
    assert seen <= {(0, 0), (1, 0), (1, -1), (0, -1)} and (1, -1) in seen
    assert not [s for s in seen if s[0] == s[1] != 0]


def test_the_post_run_record():
    """(a) exact over Q(zeta_8); (b) both routes' interior classes on M6; (c) the Lambda^2 count; (d) Wang"""
    p = _record("post_run_checks")
    assert all(p["summary"].values()) and len(p["summary"]) == 4
    a = p["(a) exact over Q(zeta_8)"]
    assert [tuple(r["char"]) for r in a if r["kind"] == "both"] == BOTH_REPS
    for r in a:
        if r["kind"] == "both":
            assert r["W1"]["boundary-type (fixed combination)"]["W1"]["I"] == 1
            assert r["W1"]["boundary-type (fixed combination)"]["L2W1"]["I"] == -1
            assert (r["W1"]["interior class c_int"]["W1"]["I"], r["W1"]["interior class c_int"]["L2W1"]["I"]) == (0, -1)
    b = p["(b) interior classes on M6"]
    assert b["distribution of n over the 320 characters"] == {"0": 292, "1": 24, "2": 4}
    assert p["(d) Wang: the fibre monodromy's kernel = h^1(V) at every character of M6"]["distribution of dim ker(S^(6) - 1)"] == \
        {"1": 292, "2": 24, "3": 4}
    c = p["(c) the Lambda^2 count at a 'both' member"]
    assert (c["a1(Lambda^2 W1)"], c["r1(Lambda^2 W1)"], c["s0(Lambda^2 W1)"], c["I(Lambda^2 W1)"]) == (4, 4, 3, -1)


def test_the_torus_table_live():
    """Lemma 1 on M6, exactly: (t0, s0) = (1, 2) for W1 and (2, 3) for Lambda^2 W1 at the chart's generic class and at z2"""
    K = _load("controls")
    import random
    s = K.s_torus(6, random.Random(1515))
    t = s["torus table (dim of invariants)"]
    assert (t["W1 [z1 + k z2]"], t["W1* [z1 + k z2]"], t["L2W1 [z1 + k z2]"], t["L2W1* [z1 + k z2]"]) == \
        ([1, "never drops"], [2, "never drops"], [2, "never drops"], [3, "never drops"])
    assert s["T1: every cocycle of P in rho1 is valued in e-perp"] and s["dim pi_A"] == 2


def test_both_routes_live():
    """a deck-coincident simple member of M4 and the 'both' member (1/8, 1/2) of M6, by both routes at recorded primes"""
    M = _modules()
    RT, RL = M["route_t"], M["route_l"]
    rT, rL = _record("census_t"), _record("census_l")
    for n, ch, expect in ((4, ("0", "1/3"), (1, 0)), (6, ("1/8", "1/2"), (1, -1))):
        lev = RT.Level(n)
        p = rT["primes"][f"M{n}"][0]
        A = RT.Arith("gf", lev.K, p=p)
        ab = tuple(int(Fr(c) * lev.N) for c in ch)
        row = RT.read_member(lev, A, RT.T.rs_rho(lev.cov, A.field), ab, 0)
        w = _primary(row["W1"])
        assert (w["W1"]["I"], w["L2W1"]["I"]) == expect
        rec = next(x for x in rT["A"] if x["level"] == n and x["field"] == f"GF({p})" and tuple(x["char"]) == ch)
        assert _primary(rec["row"]["W1"])["W1"] == w["W1"] and _primary(rec["row"]["W1"])["L2W1"] == w["L2W1"]
        pL = rL["primes"][f"M{n}"][0]
        F = RL.ModP(pL, "")
        U = RL.Units(F, RL.lcm(RL.fibre_characters(n)[1], 12))
        rowL = RL.read_member(F, U, n, RL.rho1(F, n), (Fr(ch[0]), Fr(ch[1])), Fr(0))
        wl = _primary(rowL["W1"])
        assert (wl["W1"]["I"], wl["L2W1"]["I"]) == expect


def test_the_both_member_exactly():
    """(1/8, 1/2) over Q(zeta_8): h1(V) = h1(V_eta) = h1(V (x) L) = 2 and (I(W1), I(Lambda^2 W1)) = (+1, -1) at the fixed combination"""
    P = _modules()["post_run_checks"]
    T, RT = P.T, P.RT
    E = P.ExactK8()
    lev = E.lev
    ex = lev.exponents((5, 20), 0)
    V, Veta, VL, L = E.twisted(ex, 1), E.twisted(ex, 5), E.twisted(ex, -3), E.line(ex, -4)
    assert [T.h1_classes(m, lev.rels)[1] for m in (V, Veta, VL)] == [2, 2, 2]
    cls, _ = T.h1_classes(Veta, lev.rels)
    W = RT.ext_with_line(V, RT.class_trials(cls)[-1][1], L, lev.cov["gens"])
    assert T.index(W, lev.rels, lev.mu, lev.lam)["I"] == 1
    assert T.index(T.wedge2_rep(W), lev.rels, lev.mu, lev.lam)["I"] == -1


def test_wang_live():
    """the fibre monodromy's kernel at q = 1: 2 at the four orbit representatives, 1 at a simple order-8 character"""
    T = _modules()["route_t"].T
    lev = _modules()["route_t"].Level(6)
    p = _record("census_t")["primes"]["M6"][0]
    field = T.Field("gf", p=p, r=1, iota=T.gf_root_of_unity(p, 4))
    fm = T.FibreMonodromy(field)
    for ch, k in [(c, 2) for c in BOTH_REPS] + [(("1/8", "0"), 1)]:
        ab = tuple(int(Fr(c) * lev.N) for c in ch)
        S, B = fm.level(ab, lev.N, 6)
        assert T.kernel_dims_on_H1(S, B, field.dom.one, maxpow=1)[0] == k, ch


def test_route_L_shares_no_code_with_route_T():
    """route L imports nothing of route T, B1511's tower_lib or B1374's index_lib: route_l.py loads only B1513's independent audit
    (by path), and census_l.py only route_l.py (route T's record is read as data for the comparison)"""
    allowed = {"route_l.py": {"importlib.util", "fractions", "math", "pathlib", "sympy"},
               "census_l.py": {"json", "sys", "time", "fractions", "pathlib", "sympy", "route_l"}}
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
        if fname == "route_l.py":
            assert len(specs) == 1 and "B1513_the_triplets_higgs_sector/verification/independent_audit.py" in specs[0]
        else:
            assert not specs
        for bad in ("route_t", "census_t", "tower_lib", "index_lib", "controls", "post_run_checks"):
            assert not re.search(rf"^\s*(import|from)\s+{bad}\b", src, re.M), (fname, bad)


@pytest.mark.slow
def test_the_controls_rerun():
    """S1-S7, K1-K6 and C pass again"""
    rec = _load("controls").main()
    assert all(rec["summary"].values())


def test_the_kill_graph_entry():
    """the no-go content (no generation-shaped member at q = 1 through level 6) is routed with content (B1207's A3)"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1515"]
    assert len(rec) == 1
    r = rec[0]
    assert r["fact_computed"] is True and r["routed_from"] == "sm-branch-2026-10-02-banking"
    assert r["kill_form"].startswith("wrong-partner-five") and len(r["hatch"]) > 80
    assert "tests/test_b1515_the_hyperbolic_point.py" in r["note"] and "B833" in r["depth_note"]


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED by the sealed rule, creates no law, keeps 0 of 19; the findings carry the answer, the predictions,
    the post-run checks, the disclosure and the leads; the owner's private term is absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1515" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["identifications"] == []
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    for needle in ("**Verdict:** PROVED, by the sealed rule", "**Both halves, on one background, with opposite signs** (P5 NO)",
                   "**one 10̄′ and one 5̄′**", "The SU(5)′ cubic anomaly I(Λ²W) − I(W) is **−2**",
                   "**No member through level 6 has I(W₁) = I(Λ²W₁) ≠ 0.**", "| P5 | no member carries both",
                   "**(a) Exactness.**", "**(d) A third method.**", "**A sealed-text slip** (ERROR_LEDGER)",
                   "1. **The sign law.**", SEALED_SHA, "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for path in list(ARC.glob("*.md")) + list(VER.glob("*.py")) + [ARC / "arc_verdict.json"]:
        assert term not in path.read_text(encoding="utf-8").lower(), path
