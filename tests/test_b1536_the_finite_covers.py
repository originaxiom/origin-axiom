"""B1536 lock -- THE FINITE COVERS (2026-10-04). sL-10 item 16, sm:B1535's Corollary C3, second place: sm:B1515's frame on
every connected finite cover of degree <= 12 of m004 and m003 and on their Q8 towers (m = 1, 2, 3, 4, 6, 9, 12, 18), at every
pulled-back character of finite order and every class. Sealed at 9c28d076 (addendum eeb20c44), run as sealed; NEGATIVE: no
member has both caps >= 3 (the largest min(capW, capL2) is 1 on m004 and 2 on m003, at the trivial character of sixteen
degree-10 covers), and no count read is generation-shaped. Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt), and the banked identity;
- the run as banked: the four records (run_<route>_<state>.jsonl.gz) against run_sha256.txt, complete against the population;
- the read-out (read_out.json), reproduced in memory by read_out.py itself on decompressed copies in a temporary directory;
- the post-run tables (post_run_rooms.json), reproduced the same way;
- live: the supplies at the trivial character of m003's d10.4, a cover with room for two, in both routes;
- hygiene, the verdict, the findings, and the kill record."""
import base64
import gzip
import hashlib
import importlib.util
import json
import re
import shutil
import sys
import warnings
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1536_the_finite_covers"
VER = ARC / "verification"
SEALED_SHA = "eb1a17947bfab6c7ade94fda5046246fdc0e657bcd42e3cd6ba220a349f96d0d"
ADDENDUM_SHA = "6f40e363f9bcfb540c597414283c42f47d3572e2c95d22c5b5264e7addc2ffab"
RECORDS = [f"run_{r}_{s}" for s in ("m004", "m003") for r in ("N", "R")]
LOCAL = ("cover_lib", "gf", "route_n", "route_r", "population", "run", "read_out", "identity", "post_run_rooms",
         "read_out_selftest")


def _load(name):
    """this arc's module, its sibling imports resolved to this arc's files: generic names (read_out, identity, run) exist
    in other arcs, so a module of the same name left in sys.modules by another lock is dropped first (E12)"""
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


def _records_to(d):
    """decompress the banked records into directory d (the raw .jsonl files are not tracked)"""
    for name in RECORDS:
        with gzip.open(VER / f"{name}.jsonl.gz", "rb") as src, open(d / f"{name}.jsonl", "wb") as dst:
            shutil.copyfileobj(src, dst)


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    assert hashlib.sha256((ARC / "PREREGISTRATION_ADDENDUM.md").read_bytes()).hexdigest() == ADDENDUM_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt and "Lemma G" in txt and "Proposition Q" in txt
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    assert SEALED_SHA in ledger and ADDENDUM_SHA in ledger


def test_the_sealed_files_are_unchanged():
    """every file in ARTIFACT_HASHES.txt hashes as sealed (29 files, the amended control_k1.py and the addendum included)"""
    rows = [ln.split() for ln in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines()
            if ln and not ln.startswith("#")]
    assert len(rows) == 29
    for sha, rel in rows:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == sha, rel


def test_the_banked_identity():
    """identity.py, run before run.py read anything, found every control reproduced and every sealed file as sealed"""
    ident = _json("identity.json")
    assert ident["identity holds"] is True


# ------------------------------------------------------------------------------------------------- the run as banked
def test_the_records_are_the_runs():
    """the banked records decompress to the raw records whose sha-256 was taken at the bank; each holds its population"""
    want = dict(reversed(ln.split()) for ln in (VER / "run_sha256.txt").read_text().splitlines() if ln.strip())
    sizes = {"m004": (184, 8148), "m003": (156, 35100)}
    for name in RECORDS:
        raw = gzip.open(VER / f"{name}.jsonl.gz", "rb").read()
        assert hashlib.sha256(raw).hexdigest() == want[f"{name}.jsonl"], name
        rows = [json.loads(x) for x in raw.decode().splitlines() if x.strip()]
        done = [r for r in rows if r.get("done")]
        assert (len(done), len(rows) - len(done)) == sizes[name[-4:]], name


def test_the_read_out_is_reproduced(tmp_path, monkeypatch):
    """read_out.py itself, on decompressed copies in a temporary directory, gives read_out.json (it does not write there)"""
    _records_to(tmp_path)
    ro = _load("read_out")
    monkeypatch.setattr(sys, "argv", ["read_out.py", "--dir", str(tmp_path)])
    out = ro.main()
    assert json.loads(json.dumps(out, default=str)) == _json("read_out.json")


def test_the_read_out_as_banked():
    """complete; the routes agree; NEGATIVE's conditions (P1, P2, P8, P10) hold; 8 of 10 predictions, P4 and P6 failing"""
    r = _json("read_out.json")
    assert r["complete"] is True and r["agreement"]["disagreements"] == {}
    assert r["agreement"]["compared"] == {"rows": 43248, "Part P": 1228, "Part O strata": 176}
    assert r["predictions"] == {"P1": True, "P2": True, "P3": True, "P4": False, "P5": True, "P6": False, "P7": True,
                                "P8": True, "P9": True, "P10": True}
    assert r["three"] == [] and r["generation-shaped"] == [] and r["open strata"] == []
    assert r["generation-shaped at the pulled-back class (either route)"] == []
    assert r["failed readings (number)"] == 0 and r["(N, nu) with both caps >= 3"] == 0
    assert r["the Q8 tower's n(1) at kappa = 1"]["m004"] == {"Q8.m18": 4, "Q8.m12": 4, "Q8.m9": 0, "Q8.m6": 4, "Q8.m4": 0,
                                                             "Q8.m3": 0, "Q8.m2": 0, "Q8.m1": 0}
    assert r["the Q8 tower's n(1) at kappa = 1"]["m003"] == {"Q8.m18": 0, "Q8.m12": 4, "Q8.m9": 0, "Q8.m6": 0, "Q8.m4": 0,
                                                             "Q8.m3": 0, "Q8.m2": 0, "Q8.m1": 0}
    assert all(v == 0 for st in ("m004", "m003") for v in r["the Q8 tower's n(rho) at kappa = 1"][st].values())
    caps = {st: r["per state"][st]["caps"] for st in ("m004", "m003")}
    assert max(min(eval(c)) for c in caps["m004"]) == 1 and max(min(eval(c)) for c in caps["m003"]) == 2
    assert caps["m003"]["(2, 2)"] == 16 and caps["m003"]["(1, 4)"] == 12


def test_the_post_run_tables_are_reproduced(tmp_path, monkeypatch):
    """post_run_rooms.py, written after the read-out and disclosed, reproduces post_run_rooms.json from the banked records"""
    _records_to(tmp_path)
    pr = _load("post_run_rooms")
    monkeypatch.setattr(pr, "HERE", tmp_path)
    pr.main()
    assert json.loads((tmp_path / "post_run_rooms.json").read_text()) == _json("post_run_rooms.json")
    d = _json("post_run_rooms.json")
    assert d["m004"]["routes give the same caps"] is True and d["m003"]["routes give the same caps"] is True
    room = [b for b in d["m003"]["members with min(caps) >= 2 or capL2 >= 3"] if b["caps"] == [2, 2]]
    assert len(room) == 16 and all(b["degree"] == 10 and not b["abelian"] and b["u"] == ["0", "0"] and b["kappa"] == "0"
                                   for b in room)
    assert all(not x["abelian"] for st in ("m004", "m003") for x in d[st]["trivial character supplies"])


# ------------------------------------------------------------------------------------------------- live
def test_live_room_for_two_on_m003_d10_4():
    """routes N and R, live: at the trivial character of m003's d10.4 (degree 10, three cusps, non-abelian) the supplies
    are n(L) = 1 and n((VL)*) = 2, so capW = capL2 = 2, and both equal the banked row"""
    CL, POP, gf, N, R = (_load(m) for m in ("cover_lib", "population", "gf", "route_n", "route_r"))
    st = CL.state("m003")
    perms = dict(POP.covers(st))["d10.4"]
    cus, L, Nroot, chars = POP.characters(st, perms)
    assert len(perms["a"]) == 10 and len(cus) == 3
    banked = {}
    for route in "NR":
        for line in gzip.open(VER / f"run_{route}_m003.jsonl.gz", "rt"):
            r = json.loads(line)
            if r.get("cover") == "d10.4" and not r.get("done") and r["u"] == ["0", "0"] and r["kappa"] == "0":
                banked[route] = r["S"]
    for route in "NR":
        p = gf.primes_1_mod(Nroot, N.P_BOUND if route == "N" else 1 << 31, 1)[0]
        B = N.Base(st, gf.GF(p, Nroot))
        chi = B.character((Fraction(0), Fraction(0)), Fraction(0))
        if route == "N":
            sup = N.supplies(B, N.perm_arrays(st["G"], perms), chi)
        else:
            sup = R.supplies(R.PCover(st["G"], perms), B.rho, chi, p)
        assert (sup["n(L)"], sup["n((VL)*)"], sup["capW"], sup["capL2"]) == (1, 2, 2, 2), route
        assert sup == banked[route], route


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


def test_the_verdict_and_the_findings():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1536" and v["verdict"] == "NEGATIVE"
    assert v["prior_work"]["standing"] == "EXTENDS" and v["scope"]["frame"] == "F-HE" and v["scope"]["reach"] == "class"
    assert "|" not in v["claim_one_line"] and "0 of 19" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Seen first" in f and "sweep" in f and "literature" in f and "{{" not in f
    assert "**Verdict: NEGATIVE**" in f and "8 of 10 predictions held" in f
    assert "sixteen" in f and "(2, 2)" in f and "the four is the bottleneck" in f.lower()


def test_the_kill_record():
    """the negative is in the kill graph with its population in its scope"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1536"]
    assert len(rec) == 1 and rec[0]["kill_form"].startswith("capped-by-the-supplies")
    sc = rec[0]["scope"]
    assert sc["frame"] == "F-HE" and sc["reach"] == "class" and rec[0]["fact_computed"] is True
    assert "degree <= 12" in sc["object"] and "Q8 towers" in sc["object"]
