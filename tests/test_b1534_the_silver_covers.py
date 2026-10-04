"""B1534 lock -- THE SILVER COVERS (2026-10-04). sL-10 item 11: sm:B1515's frame pulled back to every finite abelian cover of
m135 = -LLRR and m136 = +LLRR, at every member (every twist, Lemma Q), every class and every subgroup of the contributing
group. Sealed at 1f58d161, run as sealed; NEGATIVE: no cover carries three generations at a pulled-back member, in either
order; the only generation-shaped count is (-1, -1); the 5bar' side is capped at two. Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the banked identity (the controls re-run after the seal, identical but the timings);
- the run as banked (terms.json): the 144 terms in both routes, the pencils, every count recomputed from the terms, and the
  structure behind the verdict (Lambda^2 terms only at the non-simple members' non-simple twists);
- route C (route_c.json), the read-out (read_out.json, reproduced in memory by read_out.py itself in a temporary
  directory), K10 (members_every_twist.json) and the post-run route S (post_run_s.json);
- live: m136's kappa = -1 member's terms at chi = 1 and chi = (1/2, 1/2; 0) in exact arithmetic over Q(zeta_24);
- hygiene, the verdict, its registry row and its kill record."""
import base64
import hashlib
import importlib.util
import itertools
import json
import re
import shutil
import sys
import warnings
from collections import Counter
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1534_the_silver_covers"
VER = ARC / "verification"
SEALED_SHA = "0423e1f1cc40e62185da0ade839d0aac1e98a2561990adb887dccdd1ed6ffe97"
LOCAL = ("silver_lib", "silver_n", "read_out", "controls", "run_terms", "run_route_c", "members_every_twist", "identity",
         "post_run_s")


def _load(name):
    """this arc's module, its sibling imports resolved to this arc's files: generic names (read_out, controls, identity)
    exist in other arcs, so a module of the same name left in sys.modules by another lock is dropped first"""
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


@pytest.fixture(autouse=True)
def _mp_dps_60():
    """E12 (the b204 pattern): the numerical routes set mp.dps = 60 when imported; restore the entry precision after"""
    saved = mp.mp.dps
    mp.mp.dps = 60
    yield
    mp.mp.dps = saved


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt and "Lemma Q" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    """every file in ARTIFACT_HASHES.txt hashes as sealed"""
    rows = [ln.split() for ln in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines()
            if ln and not ln.startswith("#")]
    assert len(rows) == 12
    for sha, rel in rows:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == sha, rel


def test_the_banked_identity():
    """the controls, re-run unchanged after the seal, reproduce the sealed outputs in every field but the timings"""
    ident = _load("identity")
    for sealed, rerun in (("controls.json", "controls_rerun.json"),
                          ("members_every_twist.json", "members_every_twist_rerun.json")):
        assert ident.diff(ident.strip(_json(sealed)), ident.strip(_json(rerun))) == []
    c = _json("controls.json")
    assert c["all hold"] is True and all(c[f"K{i}"]["holds"] for i in range(10))


# ------------------------------------------------------------------------------------------------- the run as banked
def _terms():
    return _json("terms.json")


def test_the_population_and_the_routes():
    """14 members (m135: 8 at kappa = 1; m136: 4 at kappa = 1, 2 at kappa = 1/2 turn); 144 terms; routes E and N agree on
    every term and every pencil, every identity holding"""
    T = _terms()
    st135, st136 = T["states"]["-LLRR"], T["states"]["+LLRR"]
    assert len(st135["members"]) == 8 and all(m["kappa"] == "0" for m in st135["members"])
    assert Counter(m["kappa"] for m in st136["members"]) == Counter({"0": 4, "1/2": 2})
    n = 0
    for st in (st135, st136):
        for m in st["members"]:
            assert m["agree"] is True
            for cname, d in m["terms"].items():
                for ck, t in d.items():
                    n += 1
                    rn = m["route N"][cname][ck]
                    assert rn["checks"] is True and all(list(x) == t for x in rn["T"])
            for p in m["pencils"].values():
                assert p["agree"] is True and p["generic rank (E)"] == p["generic rank (N)"]
    assert n == 144
    assert sum(len(m["pencils"]) for st in (st135, st136) for m in st["members"]) == 64


def _subgroups(keys):
    """every subgroup of the contributing group, rebuilt here from the character keys '(w0, w1; k)'"""
    def parse(k):
        inner = k.strip("()")
        w, kk = inner.split(";")
        a, b = (Fraction(x.strip()) for x in w.split(","))
        return (a, b, Fraction(kk.strip()))
    els = {parse(k): k for k in keys}
    zero = (Fraction(0), Fraction(0), Fraction(0))

    def add(x, y):
        return tuple((p + q) % 1 for p, q in zip(x, y))

    def closure(gs):
        H, fr = {zero}, [zero]
        while fr:
            new = []
            for h in fr:
                for g in gs:
                    z = add(h, g)
                    if z not in H:
                        H.add(z)
                        new.append(z)
            fr = new
        return frozenset(H)
    out = {closure(gs) for r in range(4) for gs in itertools.combinations(sorted(els), r)}
    assert all(H <= set(els) for H in out)
    return [sorted(els[h] for h in H) for H in out]


def test_every_count_recomputed_from_the_terms():
    """each stored count is the sum of its subgroup's terms, every subgroup of C_nu is present (8, 5 or 16 of them), and the
    counts that occur are exactly the eight sealed in FINDINGS section 0"""
    T = _terms()
    seen = Counter()
    for st in T["states"].values():
        for m in st["members"]:
            subs = _subgroups(m["contributing"])
            assert len(subs) == {8: 16 if m["kappa"] == "1/2" else 8, 4: 5}[len(m["contributing"])]
            for cname, rows in m["counts"].items():
                assert sorted(tuple(r["H"]) for r in rows) == sorted(tuple(H) for H in subs)
                for r in rows:
                    w = sum(m["terms"][cname][h][0] for h in r["H"])
                    l2 = sum(m["terms"][cname][h][1] for h in r["H"])
                    assert [w, l2] == r["count"]
                    seen[tuple(r["count"])] += 1
    assert seen == Counter({(-1, -2): 20, (-1, -1): 28, (0, -2): 20, (0, -1): 12, (0, 0): 42, (1, 0): 30, (3, 0): 8,
                            (5, 0): 4})


def test_the_five_bar_side_is_capped():
    """a Lambda^2 term is non-zero only at the non-simple members (m135's u1, u2; m136's kappa = -1 members), at the twists
    chi = 1 and chi = (1/2, 1/2), where it is -1 (0 at the special class); so every count's Lambda^2 part lies in
    {0, -1, -2} and the only generation-shaped count is (-1, -1)"""
    T = _terms()
    for state, st in T["states"].items():
        for m in st["members"]:
            nonsimple = (state == "-LLRR" and tuple(m["u"]) in {("0", "1/2"), ("1/2", "0")}) or m["kappa"] == "1/2"
            for cname, d in m["terms"].items():
                for ck, (w, l2) in d.items():
                    if l2 != 0:
                        assert nonsimple and ck in ("(0, 0; 0)", "(1/2, 1/2; 0)") and l2 == -1, (state, m["u"], cname, ck)
                    assert w in (-1, 0, 1)
                    if w == -1:
                        assert cname in ("c_int", "the class") and ck == "(0, 0; 0)" and nonsimple
                    if w == 1:
                        assert not nonsimple
            for rows in m["counts"].values():
                for r in rows:
                    assert r["count"][1] in (0, -1, -2)
                    if r["count"][0] == r["count"][1] != 0:
                        assert r["count"] == [-1, -1]


def test_the_special_classes():
    """one special class per two-class member of m135, s = -sqrt2/30 at u1 and +sqrt2/30 at u2, found only by the (L2E)*
    pencil at chi = 1 and chi = (1/2, 1/2), where every term reads (0, 0); no conjugate pair"""
    T = _terms()
    for m in T["states"]["-LLRR"]["members"]:
        if m["h1"] != 2:
            assert not m["pencils"]
            continue
        sp = [c for c in m["classes"] if c.startswith("special")]
        assert len(sp) == 1 and not any(c.startswith("conjugate") for c in m["classes"])
        target = (-1 if m["u"] == ["0", "1/2"] else 1) * mp.sqrt(2) / 30
        val = mp.mpf(re.findall(r"[-+]?\d*\.\d+", m["classes"][sp[0]][1])[0])      # the real part, as recorded
        assert abs(val - target) < mp.mpf(10) ** -50
        assert all(tuple(t) == (0, 0) for t in m["terms"][sp[0]].values())
        hits = {k for k, p in m["pencils"].items() if p["special (E)"]}
        assert hits == {"(0, 0; 0) (L2E)*", "(1/2, 1/2; 0) (L2E)*"}


# ------------------------------------------------------------------------------------------------- the other records
def test_route_c_as_banked():
    """route C, the permutation module never split into characters, agrees with the sum of route E's terms on every cover
    it read (each member's first subgroup of order min(4, |C|), at the interior or one class and at c_g1)"""
    rc = _json("route_c.json")
    assert rc["agree"] is True and len(rc["rows"]) == 16
    assert all(r["route C"] == r["sum of route E's terms"] and r["|A|"] == 4 for r in rc["rows"])


def test_the_read_out_is_reproduced(tmp_path):
    """read_out.py itself, run in a temporary directory on copies of terms.json and route_c.json, gives read_out.json"""
    ro = _load("read_out")
    for f in ("terms.json", "route_c.json"):
        shutil.copy(VER / f, tmp_path / f)
    saved = ro.HERE
    try:
        ro.HERE = tmp_path
        ro.main()
    finally:
        ro.HERE = saved
    assert json.loads((tmp_path / "read_out.json").read_text()) == _json("read_out.json")
    r = _json("read_out.json")
    assert r["predictions"] == {"P1": True, "P2": False, "P3": True, "P4": True, "P5": True, "P6": True, "P7": True,
                                "P8": True}
    assert r["verdict"].startswith("NEGATIVE") and r["three"] == []


def test_k10_and_lemma_q():
    """K10: the fibre operator's unit-circle eigenvalues are 1 at every u and -1 at m136's u1, u2 only; routes T and E agree
    at all 288 points of mu_24"""
    k = _json("members_every_twist.json")
    assert k["holds"] is True
    m135, m136 = k["states"]["-LLRR"], k["states"]["+LLRR"]
    assert m135["u with eigenvalue -1"] == [] and sorted(m136["u with eigenvalue -1"]) == [["0", "1/2"], ["1/2", "0"]]
    for s in (m135, m136):
        assert s["other roots on the unit circle"] == [] and s["routes T and E disagree on mu_24 at"] == []
        assert mp.mpf(s["nearest other root to the circle"]) > mp.mpf("0.5")
    assert m135["comparisons"] + m136["comparisons"] == 288


def test_route_s_as_banked():
    """post-run route S (SnapPy's presentation, cusp and holonomy; its own classes, pencils and special classes) agrees
    with route E's member profiles, term multisets and counts on both states"""
    s = _json("post_run_s.json")
    assert s["all agree"] is True
    for state in ("-LLRR", "+LLRR"):
        c = s["comparisons"][state]
        assert c["profiles agree with route E"] and c["identity checks"] and c["Lemma Z' off C (0, 0)"]
        assert c["three (route S)"] == [] and c["generation-shaped counts (route S)"] == [[-1, -1]]


# ------------------------------------------------------------------------------------------------- live, exact
def test_m136_kappa_minus_one_member_live_exactly():
    """route E, live: at m136's kappa = -1 member u = (0, 1/2), the term at chi = 1 is (-1, -1) and at chi = (1/2, 1/2; 0) is
    (0, -1), exactly over Q(zeta_24)"""
    SL = _load("silver_lib")
    st = SL.setup("+LLRR")
    m = next(x for x in SL.members(st) if x["u"] == (Fraction(0), Fraction(1, 2)) and x["kappa"] == Fraction(1, 2))
    c = m["classes"]["the class"]
    T1, _ = SL.term(st, m, c, SL.char(st, (0, 0), 0))
    T2, _ = SL.term(st, m, c, SL.char(st, (Fraction(1, 2), Fraction(1, 2)), 0))
    assert T1 == (-1, -1) and T2 == (0, -1)


# ------------------------------------------------------------------------------------------------- hygiene and verdict
def test_hygiene():
    """no vendor word or the private term in the arc; the Gate 5-Q words stay out"""
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
    assert v["id"] == "B1534" and v["verdict"] == "NEGATIVE"
    assert v["prior_work"]["standing"] == "EXTENDS" and v["scope"]["frame"] == "F-HE"
    assert "B1534" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Seen first" in f and "sweep" in f and "literature" in f and "{{" not in f


def test_the_kill_record():
    """the negative is in the kill graph with its population in its scope"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1534"]
    assert len(rec) == 1 and rec[0]["kill_form"].startswith("the-five-bar-side-is-capped")
    sc = rec[0]["scope"]
    assert sc["frame"] == "F-HE" and sc["reach"] == "class" and rec[0]["fact_computed"] is True
    assert "abelian" in sc["object"] and "every twist" in sc["object"]
