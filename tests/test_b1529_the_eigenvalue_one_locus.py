"""B1529 lock -- THE EIGENVALUE-ONE LOCUS (2026-10-03). sL-10 item 9: the class index where the cusp acquires the eigenvalue
one, near the hyperbolic point of every word state to length 12 and of m004's levels M2-M6. Sealed at 44cdb4a6, run as sealed;
PROVED, with a kill record. Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the census record (census_records.json, the 541 records of the git-ignored census.jsonl): the sealed census reader re-run on
  it in a temporary directory reproduces read_out.json's census part; P1 (SR for Lambda^2 at all 47,333 base points), P2's one
  failing word state (m135 = -LLRR, two characters), P3 (the levels reproduce sm:B1515), I = 0 everywhere;
- the crossing records: the sealed crossing reader re-run on them reproduces read_out.json's crossing part (196 brackets, 143
  located; P4 fails on the location rate alone, P5 and P6 hold); the sign changes through a pole of b on +-L3RLR2 (22 of 40
  per sign, X1's own test), none located, every pole-free bracket located;
- the read-out: 5 of 7 (P2 and P4 failed);
- the post-run records: the controls re-run, m135 by routes Fox and W, m135 in exact arithmetic, the coverage pass (37 of 57
  located, the 20 left all on -L4RLR3LR2) and the post-run read re-run on the records (180 of the 200 first-order
  crossings, no failure);
- live: m135 in exact arithmetic over Q(zeta_8) (two characters); the census's own reading of m135 (census.one);
  sm:B1527's X1 crossing counts with the pole test (the correction applied to B1527's FINDINGS);
- hygiene, and the verdict with its registry row, its kill record and its ledger rows."""
import base64
import hashlib
import importlib.util
import json
import re
import shutil
import sys
import warnings
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1529_the_eigenvalue_one_locus"
VER = ARC / "verification"
B1527 = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"
SEALED_SHA = "0d25e63811f62d0ae408acee484648dd8d7712fb61ce2b4ddd0e5e0ca5f88089"
LOCAL = ("fibre_lib", "controls", "census", "crossings", "read_out", "post_run_poles", "post_run_coverage", "post_run_read",
         "post_run_fox", "post_run_exact_m135", "post_run_records")
B1527_NAMES = ("cusp_lib", "family_lib", "scan_lib", "wang_lib", "run", "post_run_x1", "post_run_x1c")
TEN = ["pLR", "mLR", "pLLRLRR", "mLLRLRR", "pLLLRLRR", "mLLLRLRR", "pLLLLRLLLRR", "mLLLLRLLLRR", "pLLLLRLRRRLRR",
       "mLLLLRLRRRLRR"]


def _purge():
    """this arc's generic module names (and sm:B1527's, which fibre_lib loads by bare name) may be held in sys.modules by
    another arc's lock; drop any that do not come from the expected directory"""
    for names, d in ((LOCAL, VER), (B1527_NAMES, B1527)):
        for n in names:
            mod = sys.modules.get(n)
            if mod is not None and Path(str(getattr(mod, "__file__", ""))).resolve().parent != d.resolve():
                del sys.modules[n]


def _load(name, here=None):
    """this arc's module (optionally with its HERE pointed at a temporary directory, for the readers)"""
    warnings.filterwarnings("ignore")
    _purge()
    for d in (B1527, VER):
        if str(d) in sys.path:
            sys.path.remove(str(d))
        sys.path.insert(0, str(d))
    if name in sys.modules and here is None:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    if here is not None:
        mod.HERE = here
    return mod


def _json(name):
    return json.loads((VER / name).read_text(encoding="utf-8"))


@pytest.fixture(autouse=True)
def _mp_dps_60():
    """E12 (the b204 pattern): the arc's modules work at 60 digits; tests/conftest.py restores the entry precision after"""
    saved = mp.mp.dps
    mp.mp.dps = 60
    yield
    mp.mp.dps = saved


@pytest.fixture()
def reader_dir(tmp_path):
    """a temporary directory with census.jsonl rebuilt from census_records.json and the ten crossing records copied"""
    recs = _json("census_records.json")["records"]
    (tmp_path / "census.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    for n in TEN:
        f = VER / f"crossings_{n}.json"
        if f.exists():
            shutil.copy(f, tmp_path / f.name)
    return tmp_path


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, rel = line.split(None, 1)
        assert hashlib.sha256((ARC / rel.strip()).read_bytes()).hexdigest() == digest, rel


# ------------------------------------------------------------------------------------------------- the census
def test_the_census_record():
    """541 manifolds (536 word states, M2-M6), no error; on the bench, census.jsonl is the file the record was made from"""
    doc = _json("census_records.json")
    recs = doc["records"]
    assert len(recs) == 541 and len({r["state"] for r in recs}) == 541
    assert sum(1 for r in recs if r["level"]) == 5 and not any("error" in r for r in recs)
    src = VER / "census.jsonl"
    if src.exists():
        assert hashlib.sha256(src.read_bytes()).hexdigest() == doc["sha256 of the source"]


def test_the_census_reading(reader_dir):
    """read_out.census(), the sealed reader, on the record: P1, P3 and G's census part hold, P2 fails on -LLRR alone; as
    read_out.json banked"""
    ro = _load("read_out", here=reader_dir)
    c = ro.census()
    banked = _json("read_out.json")["census"]
    for P in ("P1", "P2", "P3"):
        assert c[P]["holds"] == banked[P]["holds"], P
    assert c["P1"]["holds"] and c["P3"]["holds"] and not c["P2"]["holds"]
    assert c["P2"]["failing word states"] == ["-LLRR"]
    assert c["P1"]["base points"] == 47333 and c["P2"]["base points"] == 46826
    assert c["G (census part)"]["golden word states"] == 14 and c["G (census part)"]["P1 and P2 hold on all of them"]
    assert all(c["P3"]["checks"].values())


def test_the_census_numbers():
    """the four's base condition fails at m135's (0, 1/2) and (1/2, 0) and M6's 28 (24 of order 8 with h1 = 2, 4 of order 5
    with h1 = 3); its SR fails at 42 base points (m135 6, M4 8, M6 28); Lambda^2's SR and base condition hold everywhere"""
    recs = {r["state"]: r for r in _json("census_records.json")["records"]}
    base, sr = {}, {}
    for st, r in recs.items():
        assert set(r["L2"]["(h1, h1*, t0, s0) values"]) == {"(2, 2, 2, 2)"} and not r["L2"]["SR fails at"], st
        assert set(r["4"]["I values"]) == {"0"} and set(r["L2"]["I values"]) == {"0"}, st
        if r["4"]["base condition fails at"]:
            base[st] = r["4"]["base condition fails at"]
        if r["4"]["SR fails at"]:
            sr[st] = len(r["4"]["SR fails at"])
    assert set(base) == {"-LLRR", "+" + "LR" * 6}
    assert sorted((tuple(p["u"]), tuple(p["(h1, h1*, t0, s0)"])) for p in base["-LLRR"]) == [
        (("0", "1/2"), (2, 2, 1, 1)), (("1/2", "0"), (2, 2, 1, 1))]
    assert len(base["+" + "LR" * 6]) == 28
    assert sr == {"-LLRR": 6, "+" + "LR" * 4: 8, "+" + "LR" * 6: 28}


@pytest.mark.slow
def test_the_census_reads_m135_live():
    """census.one, the sealed census's own function, on -LLRR: the record's readings, both modules"""
    census = _load("census")
    rec = census.one(("-LLRR", None))
    banked = next(r for r in _json("census_records.json")["records"] if r["state"] == "-LLRR")
    for m in ("4", "L2"):
        for key in ("(h1, h1*, t0, s0) values", "am(C; 1) values", "I values", "base condition fails at"):
            assert rec[m][key] == banked[m][key], (m, key)


# ------------------------------------------------------------------------------------------------- the crossings
def test_the_crossing_reading(reader_dir):
    """read_out.crossings(), the sealed reader, on the ten records: as read_out.json banked"""
    ro = _load("read_out", here=reader_dir)
    x = ro.crossings()
    banked = _json("read_out.json")["crossings"]
    assert x == json.loads(json.dumps(banked)) or {k: x[k] for k in ("P4", "P5", "P6", "brackets", "located", "missing")} == \
        {k: banked[k] for k in ("P4", "P5", "P6", "brackets", "located", "missing")}
    assert (x["brackets"], x["located"], x["missing"]) == (196, 143, [])
    assert x["P4"] is False and x["P5"] is True and x["P6"] is True and x["G (crossing part)"] is True
    assert all(not st["structure fails"] and not st["index fails"] and not st["mechanism fails"]
               for st in x["states"].values())
    assert sum(st["rows T"] for st in x["states"].values()) == 9562
    assert sum(st["rows Fox/W"] for st in x["states"].values()) == 1406
    assert x["states"]["-LLLLRLRRRLRR"]["located"] == 0 and x["states"]["+LLLLRLRRRLRR"]["located"] == 15


def test_the_read_out():
    p = _json("read_out.json")["predictions"]
    assert p == {"P1": True, "P2": False, "P3": True, "P4": False, "P5": True, "P6": True, "G": True}
    assert sum(p.values()) == 5


def test_the_pole_brackets():
    """X1's pole test on +-L3RLR2: 22 of 40 brackets per sign are sign changes through a pole of b; none was located, and every
    pole-free bracket was (post_run_poles' records are the sealed reader's input there)"""
    PP = _load("post_run_poles")
    for name in ("pLLLRLRR", "mLLLRLRR"):
        tagged = PP.brackets_with_poles(name)
        rec = _json(f"crossings_{name}.json")
        assert len(tagged) == len(rec["crossings"]) == 40 and sum(b["pole"] for b in tagged) == 22
        for b, c in zip(tagged, rec["crossings"]):
            assert ("read" in c) == (not b["pole"]), (name, b["between"])


def test_the_coverage_record():
    """post_run_coverage: twenty first-order crossings per ring; 57 targets (48 missed, 9 failed), 37 located (32 route F, 5
    route S), the 20 not located all on -L4RLR3LR2"""
    PC = _load("post_run_coverage")
    d = _json("post_run_coverage.json")
    s = d["summary"]
    assert (s["targets"], s["located"], s["by route"]) == (57, 37, {"F": 32, "S": 5, "null": 20})
    assert {k: v["targets"] - v["located"] for k, v in s["by state"].items() if v["targets"] != v["located"]} == \
        {"-LLLLRLRRRLRR": 20}
    kinds = {}
    for e in d["entries"]:
        kinds[e["target"]] = kinds.get(e["target"], 0) + 1
    assert kinds == {"missed": 48, "failed": 9}
    for alpha1 in (0.0, 12.5, 37.0):
        pred = PC.predicted(alpha1)
        assert len(pred) == 20 and sorted({k for k, _, _ in pred}) == ["E1", "E2", "E3", "E4"]


def test_the_post_run_read(reader_dir):
    """post_run_read.main, re-run on the records in a temporary directory, reproduces post_run_read.json: 180 of the 200
    first-order crossings located, each matched once, no structure, index or mechanism failure"""
    shutil.copy(VER / "post_run_coverage.json", reader_dir / "post_run_coverage.json")
    _load("read_out", here=reader_dir)
    pr = _load("post_run_read", here=reader_dir)
    pr.main()
    got = json.loads((reader_dir / "post_run_read.json").read_text(encoding="utf-8"))
    banked = _json("post_run_read.json")
    assert got == banked
    t = banked["totals"]
    assert (t["first-order crossings"], t["located"], t["rows T"], t["rows Fox/W"]) == (200, 180, 11640, 1640)
    assert t["structure fails"] == t["index fails"] == t["mechanism fails"] == t["unmatched"] == t["found twice"] == 0
    assert banked["agrees with read_out on the sealed records"] is True
    assert all(v is True for k, v in banked["after the run"].items() if k != "located / first-order")


# ------------------------------------------------------------------------------------------------- m135
def test_m135_by_routes_fox_and_w():
    s = _json("post_run_fox.json")["states"]
    assert list(s) == ["-LLRR"]
    r = s["-LLRR"]
    assert r["the three routes agree"] and r["every Fox identity holds"] and r["I = 0 on every row (both routes)"]
    assert r["interior classes n(V) at the failures"] == {"0/1/2": [1, 1], "1/2/0": [1, 1]}


def test_m135_exact_record():
    d = _json("post_run_exact_m135.json")
    assert d["every row agrees with the census"] and len(d["rows"]) == 8
    assert all(v is True for k, v in d["exact checks"].items() if not k.startswith("traces"))
    assert d["exact checks"]["traces of the four (a, b, t, ab, abt)"] == ["2 sqrt2", "2 sqrt2", "4", "4", "4"]
    rows = {tuple(r["u"]): r for r in d["rows"]}
    for u in (("0", "1/2"), ("1/2", "0")):
        assert rows[u]["(h1, h1*, t0, s0)"] == [2, 2, 1, 1] and rows[u]["n(V), n(V*)"] == [1, 1]
    four_root = ["1", "-4", "6", "-4", "1"]
    assert sum(1 for r in d["rows"] if r["chi_C (highest first)"] == four_root) == 6


def test_m135_exact_live():
    """the exact route, live: the holonomy read in PGL(2, Q(i)) and the four's readings at u = (0, 1/2) and (0, 0)"""
    E = _load("post_run_exact_m135")
    FL = _load("fibre_lib").load_b1527("family_lib")
    G, img = FL.word_group(E.SIGN, E.WORD)
    g2 = E.exact_sl2()
    W = {g: E.four(g2[g]) for g in "abt"}
    for u, want in (((0, 1, 2), (2, 2, 1, 1)), ((0, 0, 1), (1, 1, 1, 1))):
        nua, nub = E.root_of_unity(Fraction(u[0], u[2])), E.root_of_unity(Fraction(u[1], u[2]))
        lam = (nua * nub).inv()
        nu = {"a": nua, "b": nub, "t": lam}
        rho = {g: E.scal(W[g], nu[g]) for g in "abt"}
        rhod = {g: E.transpose(E.minv(rho[g])) for g in "abt"}
        V, Vd = E.readings(rho, G.rels, G.cusp), E.readings(rhod, G.rels, G.cusp)
        assert (V["h1"], Vd["h1"], V["t0"], Vd["t0"]) == want


# ------------------------------------------------------------------------------------------------- sm:B1527's X1 count
def test_b1527_x1_count_with_the_pole_test():
    """X1's banked crossing count, with X1's own test for a sign change of b through a pole: 12, 12, 12, 12, 14, 14, 12, 12, 12
    and 8 genuine sign changes (the 30 on +-L3RLR2 counted 16 through a pole); B1527's FINDINGS carries the correction"""
    want = [12, 12, 12, 12, 14, 14, 12, 12, 12, 8]
    got = []
    for name in TEN:
        x = json.loads((B1527 / f"x1_{name}.json").read_text(encoding="utf-8"))
        a = x["a"]
        grid = {round(g["alpha0"], 6) % 360: g for g in x["grid"]}
        n = 0
        for c in x["eigenvalue-one crossings"]:
            g, h = grid[round(c["between"][0], 6) % 360], grid[round(c["between"][1], 6) % 360]
            pole = (g["b"] > 0) != (h["b"] > 0) and not (abs(g["b"]) < 10 * a and abs(h["b"]) < 10 * a)
            n += not pole
        got.append(n)
    assert got == want
    txt = (ROOT / "frontier" / "B1527_the_cusp_decides" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "12, 12, 12, 12, 14, 14, 12, 12, 12 and 8" in txt and "8 to 14" in txt and "8 to 30" in txt


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
    assert v["id"] == "B1529" and v["verdict"] == "PROVED" and v["creates_law"] is True
    assert v["prior_work"]["standing"] == "EXTENDS" and v["scope"]["frame"] == "F-HE" and v["scope"]["reach"] == "class"
    assert "T-THE-EIGENVALUE-ONE-LOCUS" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "B1529 VERDICT: PROVED" in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Seen first" in f and "sweep" in f and "literature" in f and "\u27e8TBD" not in f and "{{" not in f
    assert "5 of 7" in f


def test_the_kill_record():
    """Theorem N and Lemma K's no-go is in the kill graph within its scope"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1529"]
    assert len(rec) == 1 and rec[0]["kill_form"].startswith("the-interior-polynomial-decides")
    sc = rec[0]["scope"]
    assert sc["frame"] == "F-HE" and sc["reach"] == "class" and rec[0]["fact_computed"] is True
    assert "536" in sc["object"] and "M2-M6" in sc["object"] and "item 10" in rec[0]["hatch"]

