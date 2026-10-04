"""B1532 lock -- THREE FROM THE CUSPS (2026-10-04). sL-7: sm:B1515's frame pulled back to every finite abelian cover of m004's
levels M2-M6, at every lambda = 1 member and every class. Sealed at 97fdce6d, run as sealed; NEGATIVE: no cover carries a
generation-shaped count, so none carries three; the W counts never go below -1, and where they reach -1 the Lambda^2 count
is -2 or -4. Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the run's records: Part 0 in both routes, the terms (kept compressed; their sha-256 before compression), the read-out
  reproduced by read_out.py itself in a temporary directory from the compressed terms, and the first read-out's printout
  (P1 pending route C, nothing else different);
- the census's shape behind the verdict, recomputed from the terms;
- route C (route_c_run.json) and the post-run check of the members at kappa^5 = 1 (post_run_twists.json);
- live: one member of M2 read again in both routes, at every twist;
- hygiene, the verdict, its registry row and its kill record."""
import base64
import gzip
import hashlib
import importlib.util
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1532_three_from_the_cusps"
VER = ARC / "verification"
SEALED_SHA = "f7ff13be181b89100dca0ce52affd6e09edf0eb3529d6f96f65d52f7acecfbf0"
LOCAL = ("read_out", "run_terms", "cover_lib_t", "cover_lib_l", "route_c", "run_route_c", "controls", "adjudicate",
         "post_run_twists")


def _load(name):
    """this arc's module, its sibling imports resolved to this arc's files (generic names such as read_out and controls exist
    in other arcs, so a module of the same name left in sys.modules by another lock is dropped first)"""
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


@pytest.fixture(scope="module")
def run_dir(tmp_path_factory):
    """a temporary copy of the run's inputs to the read-out, the terms decompressed"""
    d = tmp_path_factory.mktemp("b1532_run")
    for route in ("T", "L"):
        with gzip.open(VER / f"terms_{route}.jsonl.gz", "rb") as src, open(d / f"terms_{route}.jsonl", "wb") as dst:
            shutil.copyfileobj(src, dst)
        shutil.copy(VER / f"part0_{route}.json", d / f"part0_{route}.json")
    shutil.copy(VER / "route_c_run.json", d / "route_c_run.json")
    return d


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt and "Lemma S" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    """every file in ARTIFACT_HASHES.txt hashes as sealed"""
    rows = [ln.split() for ln in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines()
            if ln and not ln.startswith("#")]
    assert len(rows) == 15
    for sha, rel in rows:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == sha, rel


# ------------------------------------------------------------------------------------------------- the run's records
def test_part0_in_both_routes():
    """the banked identity: all 507 chi = 1 terms equal sm:B1515's census rows, in each route"""
    for route in ("T", "L"):
        p0 = _json(f"part0_{route}.json")
        assert p0 == {"agree": 507, "differ": [], "passed": True}


def test_the_terms_are_the_run_s(run_dir):
    """the compressed terms decompress to the files the read-out read (their sha-256 recorded at banking)"""
    want = dict(reversed(ln.split()) for ln in (VER / "terms_sha256.txt").read_text().splitlines() if ln.strip())
    for route in ("T", "L"):
        got = hashlib.sha256((run_dir / f"terms_{route}.jsonl").read_bytes()).hexdigest()
        assert got == want[f"terms_{route}.jsonl"]


def test_the_read_out_is_reproduced(run_dir):
    """read_out.py itself, on the decompressed terms in a temporary directory, gives read_out.json (all but the timing)"""
    ro = _load("read_out")
    saved = sys.argv
    try:
        sys.argv = ["read_out.py", "--dir", str(run_dir)]
        out = ro.main()
    finally:
        sys.argv = saved
    out = json.loads(json.dumps(out, default=str))
    banked = _json("read_out.json")
    for d in (out, banked):
        d.pop("seconds")
    assert out == banked
    p = banked["predictions"]
    assert [p[k] for k in sorted(p)] == [True, True, True, False, False, False, True, True, False]
    assert banked["checks"] == {"D5": 0} and banked["censuses agree"] is True
    assert all(banked["census"][r]["generation-shaped"] == [] for r in ("T", "L"))


def test_the_first_read_out_differs_only_in_p1():
    """the read-out ran first before route C (as sealed): its printout differs from the recorded one only in P1 and timing"""
    first = (VER / "read_out_first_run.txt").read_text().splitlines()
    second = (VER / "read_out_log.txt").read_text().splitlines()
    assert len(first) == len(second)
    diff = [(a, b) for a, b in zip(first, second) if a != b]
    assert diff and all(("P1 route C = route T" in a and "route_c_run.json missing" in a and b.endswith("true,"))
                        or ("seconds" in a and "seconds" in b) for a, b in diff)


def test_the_census_shape(run_dir):
    """recomputed from route T's terms: 68,596 counts; Lambda^2 = 0 on M2-M5; every Lambda^2 count <= 0; every W count >= -1,
    and -1 only at the interior class of the 120 two-class members on covers containing nu^4, where Lambda^2 is -2 or -4;
    hence no generation-shaped count"""
    ro = _load("read_out")
    R = ro.Route("T", ro.load(run_dir / "terms_T.jsonl"))
    subs = {n: ro.subgroups(sorted(R.chars[n])) for n in R.levels}
    hist, shaped = R.census(subs)
    assert sum(hist.values()) == 68596 and shaped == []
    assert all(l == 0 for (n, c, w, l) in hist if n < 6)
    assert all(l <= 0 and w >= -1 for (n, c, w, l) in hist)
    neg = Counter({(n, c, l): v for (n, c, w, l), v in hist.items() if w == -1})
    assert neg == Counter({(6, "int", -2): 720, (6, "int", -4): 624})
    # the only negative W terms: the interior class at chi = nu^4, at all 120 two-class members
    negs = [(nu, chi) for (n, nu, chi), r in R.rows.items() if r["kind"] == "two" and r["int"][0][0] < 0]
    assert len(negs) == 120 and all(chi == ro.scale(nu, 4) for nu, chi in negs)
    assert all(t[0][0] >= 0 for r in R.rows.values()
               for t in ([r["c"]] if r["kind"] == "one" else [r["gen"][1]] + [x for _, _, x in r["special"]]))


# ------------------------------------------------------------------------------------------------- the other records
def test_route_c_as_banked():
    rc = _json("route_c_run.json")
    assert rc["readings"] == 264 and rc["all agree"] is True
    assert all(r["agree"] and r["route C"] == r["route T sum"] for r in rc["rows"])
    assert Counter(r["n"] for r in rc["rows"]) == Counter({2: 10, 3: 88, 4: 48, 5: 10, 6: 108})


def test_the_members_at_kappa5_as_banked():
    """post-run (disclosed): the members nu0 eps at kappa^5 = 1 on every finite abelian cover, from the sealed terms"""
    t = _json("post_run_twists.json")
    assert t["identity (the code at x1 = 0 reproduces the sealed census)"] == {"T": True, "L": True}
    assert t["routes agree"] is True
    for route in ("T", "L"):
        r = t[route]
        assert r["counts read"] == 110956 and r["generation-shaped"] == []
        assert r["shifted (B0, coset) pairs by level"] == {"2": 4, "3": 0, "4": 24, "5": 0, "6": 148}
        assert r["smallest W count"] == -1 and r["smallest Lambda^2 count"] == -24


# ------------------------------------------------------------------------------------------------- live
def test_one_member_of_m2_live_in_both_routes(run_dir):
    """route T and route L, live at sm:B1515's first primes: one member of M2 at all five twists, equal to the terms read"""
    ro = _load("read_out")
    rt = _load("run_terms")
    for route in ("T", "L"):
        stored = ro.load(run_dir / f"terms_{route}.jsonl")
        ps = rt.primes(route)
        L, chars, make, one = rt.level(route, 2, ps[2])
        ab = chars[1]
        n, lab, rows = rt.read_member(route, 2, ps[2], ab)
        assert len(rows) == 5
        for row in rows:
            assert row["c"] == stored[(2, lab, row["chi"])]["c"], (route, lab, row["chi"])


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
    assert v["id"] == "B1532" and v["verdict"] == "NEGATIVE"
    assert v["prior_work"]["standing"] == "EXTENDS" and v["scope"]["frame"] == "F-HE"
    assert "B1532" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Seen first" in f and "sweep" in f and "literature" in f and "{{" not in f


def test_the_kill_record():
    """the negative is in the kill graph with its population in its scope"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1532"]
    assert len(rec) == 1 and rec[0]["kill_form"].startswith("the-sides-never-meet")
    sc = rec[0]["scope"]
    assert sc["frame"] == "F-HE" and sc["reach"] == "class" and rec[0]["fact_computed"] is True
    assert "abelian" in sc["object"] and "lambda = 1" in sc["object"]
