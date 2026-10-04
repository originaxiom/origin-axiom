"""B1535 lock -- THE CAP (2026-10-04). sL-10 item 14, first half: at a finite-order member of sm:B1515's frame on any finite
cover, I(Lambda^2 W1) lies in [-n(nu^3 rho), 0] and I(W1) >= -b0 - n(nu^4), at every class and in either order (Theorem C), and
the line has no interior class on a once-punctured-torus bundle with Anosov monodromy or a finite abelian cover of one at
puncture-trivial characters (Lemma W). Sealed at b410afeb, run as sealed; PROVED (P2, P3, P8 hold). Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the banked identity (identity.json);
- the run's records: Part M's rows (kept compressed; their sha-256 before compression), the read-out reproduced by read_out.py
  itself in a temporary directory, and Part W's census;
- Theorem C's caps at every reading, recomputed from the rows; the one generation-shaped value;
- live: one pair (nu, B) of m135 read again by part_m.run in both routes, equal to the rows;
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
ARC = ROOT / "frontier" / "B1535_the_cap"
VER = ARC / "verification"
SEALED_SHA = "c0803c0c9c72eac9e8cfe3c0980db2b75f3aa9bce1fcea3c59c7c47b5a902104"
LOCAL = ("read_out", "part_m", "part_w", "mixed_lib", "rs_lib", "cap_lib", "controls", "control_k1", "identity",
         "check_b1532")


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
    """a temporary copy of the read-out's inputs, Part M's rows decompressed"""
    d = tmp_path_factory.mktemp("b1535_run")
    with gzip.open(VER / "part_m.jsonl.gz", "rb") as src, open(d / "part_m.jsonl", "wb") as dst:
        shutil.copyfileobj(src, dst)
    shutil.copy(VER / "part_w.json", d / "part_w.json")
    return d


@pytest.fixture(scope="module")
def rows(run_dir):
    return [json.loads(x) for x in (run_dir / "part_m.jsonl").read_text().splitlines() if x.strip()]


def T(r):
    return (r["I(W)"], r["I(L2W)"])


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt and "Theorem C (the cap)" in txt and "Lemma W" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    """every file in ARTIFACT_HASHES.txt hashes as sealed"""
    rows_ = [ln.split() for ln in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    assert len(rows_) == 17
    for sha, rel in rows_:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == sha, rel


def test_the_banked_identity():
    ident = _json("identity.json")
    assert ident["identity holds"] is True and ident["controls differences"] == 0 and ident["hash mismatches"] == []
    assert ident["k1 holds (144 terms)"] is True and ident["sealed files checked"] == 17


# ------------------------------------------------------------------------------------------------- the run's records
def test_the_rows_are_the_run_s(run_dir):
    """the compressed rows decompress to the file the read-out read (its sha-256 recorded at banking)"""
    want = (VER / "part_m_sha256.txt").read_text().split()[0]
    assert hashlib.sha256((run_dir / "part_m.jsonl").read_bytes()).hexdigest() == want


def test_the_read_out_is_reproduced(run_dir):
    """read_out.py itself, on the decompressed rows in a temporary directory, gives read_out.json"""
    ro = _load("read_out")
    out = json.loads(json.dumps(ro.main(d=run_dir), default=str))
    assert out == _json("read_out.json")
    p = out["predictions"]
    assert [p[k] for k in sorted(p)] == [True, True, True, True, False, False, True, True, True]
    assert out["verdict rule (section 9)"].endswith(": they do")
    assert out["generation-shaped readings"] == {"(-1, -1)": 36}


def test_part_w_as_banked():
    w = _json("part_w.json")
    assert w["rows"] == 541 and w["Lemma W holds"] is True
    assert w["n != 0 (X)"] == 0 and w["n != 0 (S)"] == 0 and w["mu != tau"] == 0 and w["order | 12 counts agree"] is True
    assert w["route X characters"] == 567996 and w["route S characters"] == 41724
    assert len(_json("part_w_rows.json")) == 541


def test_the_caps_at_every_reading(rows):
    """recomputed from the rows: 776 readings; Theorem C's checks in every route; b0 = 1 and n(nu^4) = 0 everywhere, so
    W >= -1; Lambda^2 >= -n(nu^3 rho*) >= -2; the routes agree; the only generation-shaped value is (-1, -1)"""
    assert len(rows) == 776
    assert Counter(len(r["B"]) for r in rows) == Counter({2: 260, 4: 360, 8: 156})
    for r in rows:
        a, b = r["RS p1"], r["RS p2"]
        assert a["all"] and b["all"] and r.get("Ind", {"all": True})["all"]
        assert a["b0"] == 1 and a["n(L)"] == 0 and T(a)[0] >= -1
        assert -a["n((VL)*)"] <= T(a)[1] <= 0 and a["n((VL)*)"] <= 2
        assert all(a[k] == b[k] for k in ("I(W)", "I(L2W)", "k", "b0", "n((VL)*)", "n(V)", "n(L)", "rk d1"))
        if "Ind" in r:
            assert all(r["Ind"][k] == a[k] for k in ("I(W)", "I(L2W)", "k", "b0", "n((VL)*)", "n(V)", "n(L)", "rk d1"))
        if "banked" in r:
            assert list(T(a)) == r["banked"]
    shaped = Counter(T(r["RS p1"]) for r in rows if T(r["RS p1"])[0] == T(r["RS p1"])[1] != 0)
    assert shaped == Counter({(-1, -1): 36})
    assert sum(1 for r in rows if "Ind" in r) == 140


def test_p6_is_one_special_class(rows):
    """P6 fails at exactly one pair: m136, nu = (1/2, 0; 1/2), order 4, where the first hashed class has the smaller rank"""
    gen = {}
    for r in rows:
        if r["class"].startswith("mixed-generic"):
            gen.setdefault((r["state"], tuple(r["nu"]), json.dumps(r["B"])), []).append(r["RS p1"])
    differ = [(k, v) for k, v in gen.items() if len({T(x) for x in v}) > 1]
    assert len(gen) == 102 and len(differ) == 1
    (state, nu, B), (g1, g2) = differ[0]
    assert state == "+LLRR" and nu == ("1/2", "0", "1/2") and len(json.loads(B)) == 4
    assert (T(g1), g1["rk d1"]["L2*"]) == ((0, -1), 3) and (T(g2), g2["rk d1"]["L2*"]) == ((0, -2), 4)


def test_the_blind_prediction_for_b1532():
    c = _json("check_b1532.json")
    assert c.get("holds") is True


# ------------------------------------------------------------------------------------------------- live
def test_one_pair_live(rows):
    """part_m.run, live, at m135's first pair (nu = 0, order 2): every class equal to the rows, in both routes"""
    pm = _load("part_m")
    st = pm.SL.setup("-LLRR")
    mems, pop = pm.population(st)
    m, B = pop[0]
    nu = pm.lab_of(m["u"], m["kappa"])
    live = pm.run(selection={("-LLRR", nu, B)}, log=lambda s: None)
    nu_s, B_s = [str(v) for v in nu], [[str(v) for v in x] for x in B]
    banked = [r for r in rows if r["state"] == "-LLRR" and r["nu"] == nu_s and r["B"] == B_s]
    assert len(live) == len(banked) >= 6
    for a, b in zip(live, banked):
        assert json.loads(json.dumps(a, default=str)) == b


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
    assert v["id"] == "B1535" and v["verdict"] == "PROVED"
    assert v["prior_work"]["standing"] == "EXTENDS" and v["scope"]["frame"] == "F-HE"
    assert "T-THE-CAP" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Seen first" in f and "sweep" in f and "literature" in f and "{{" not in f


def test_the_kill_record():
    """Corollary C1 is in the kill graph as a negative within its scope (the seal's section 9)"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1535"]
    assert len(rec) == 1 and rec[0]["kill_form"].startswith("capped-by-the-supplies")
    sc = rec[0]["scope"]
    assert sc["frame"] == "F-HE" and sc["reach"] == "class" and rec[0]["fact_computed"] is True
    assert "abelian" in sc["object"] and "m135" in sc["object"] and "m136" in sc["object"]
