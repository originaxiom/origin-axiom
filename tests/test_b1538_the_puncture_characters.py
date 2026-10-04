"""B1538 -- THE PUNCTURE CHARACTERS: the seal's lock (sealed; no outcome read).

  - seal integrity: every file of ARTIFACT_HASHES.txt hashes as sealed;
  - the controls K0-K12 recorded in controls.json all hold, with K10's structure (Proposition H's ten covers, the two golden
    ones, and the identity class of each silver state), K11's manifest (80 covers, 108 chunks, the seal's totals) and K12's
    fourth-root certificate (40 covers);
  - the read-out's logic on synthetic rows (P4-P6, the Part F branches, the audit lane's R87 coverage cases, and
    Proposition H's P9-P11);
  - route W reproduces the figure-eight's Burau/Alexander identity (control K7) at two roots of unity;
  - the population's structure on m004 and m003: 5 and 9 covers, b1 = #cusps (Lemma 2), the puncture-trivial subgroup of
    order |det(M - 1)| (Lemma 3), free rank #cusps - 1.
sm:B1536's route_r resets PARI's stack when imported, so nothing here imports punct_four (or controls.py, which does).
Instruments are imported inside the tests: sm:B1527's cusp_lib sets mpmath's precision when imported."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1538_the_puncture_characters"
V = ARC / "verification"


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, V / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _lib():
    if str(V) not in sys.path:
        sys.path.insert(0, str(V))
    import punct_covers as F
    import punct_transfer as T
    import punct_wang as W
    return F, T, W


def test_seal_integrity():
    lines = [ln for ln in (ARC / "ARTIFACT_HASHES.txt").read_text().splitlines() if ln.strip() and not ln.startswith("#")]
    assert len(lines) >= 11
    for ln in lines:
        h, name = ln.split(None, 1)
        assert hashlib.sha256((ARC / name).read_bytes()).hexdigest() == h, name


def test_controls_recorded():
    c = json.loads((V / "controls.json").read_text())
    assert c["all hold"] is True
    for k in ("K0", "K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "K11", "K12"):
        assert c[k]["holds"] is True, k
    assert c["K1"]["rows"] == 541 and c["K2"]["covers"] == 80 and len(c["K9"]["cases"]) == 26
    assert c["K12"]["covers"] == 40 and c["K12"]["failure count"] == 0
    h = c["K10"]
    assert h["count"] == 10 and h["golden covers"] == ["m003.D4.2-0-2.w0", "m004.D4.2-0-2.w0"]
    assert h["identity covers"] == ["m135.D4.2-0-2.w0", "m136.D4.2-0-2.w3"]
    assert all(v["m"] == 2 and all(v["checks"].values()) for v in h["covers"].values())
    m = c["K11"]
    assert len(m["manifest"]) == 80 and m["chunks"] == 108
    assert m["totals"] == {"m004": [5, 583, 201], "m003": [9, 39695, 7313], "m136": [29, 807820, 210524],
                           "m135": [37, 1558524, 444950]}


def test_read_out_logic():
    RO = _load("read_out", "b1538_read_out_lock")

    def cover(state, hits, chunks=1):
        return {"cover": state + ".x", "chunk": 0, "chunks": chunks, "state": state, "read": True, "puncture orbits": 4,
                "puncture characters": 8, "hits": hits, "route P": {"reads": 5, "disagree": []},
                "route T": {"reads": len(hits), "skipped": 0, "disagree": []}}

    def man(*cids, chunks=1):
        return {c: {"chunks": chunks, "puncture orbits": 4} for c in cids}

    def hit(n):
        return {"n": n, "zeta": [1], "m": 2, "s": [1, 2], "h1": n, "trivial cusps": 0}
    chi = {"zeta": [1], "m": 2, "s": [1, 2], "n": 2}
    q = lambda s: None  # noqa: E731
    ident = {"identity holds": True}
    p = RO.evaluate(ident, [cover("m003", [])], None, say=q, manifest=man("m003.x"))["predictions"]
    assert (p["P4"], p["P5"], p["P6"], p["P8"]) == (False, True, True, True)
    p = RO.evaluate(ident, [cover("m004", [hit(1)])], None, say=q, manifest=man("m004.x"))["predictions"]
    assert (p["P4"], p["P5"], p["P6"]) == (True, True, False)
    # the audit lane's R87: a missing cover, or a candidate with an empty Part F, certifies nothing
    out = RO.evaluate(ident, [cover("m003", [])], None, say=q, manifest=man("m003.x", "m135.x"))
    assert out["every cover read"] is False and (out["predictions"]["P4"], out["predictions"]["P8"]) == (None, None)
    p = RO.evaluate(ident, [cover("m135", [hit(2)])], [], say=q, manifest=man("m135.x"))["predictions"]
    assert (p["P7"], p["P8"]) == (None, None)
    head = {"kind": "candidate", "cover": "m135.x", "chi": chi, "planned": 1}
    both = {"kind": "reading", "cover": "m135.x", "chi": chi, "nu": {"zeta": [1], "m": 8, "s": [1, 8]}, "member": True,
            "h1 R": 1, "h1 P4": 1, "R": {"capW": 2, "capL2": 2}, "P4": {"capW": 2, "capL2": 2}}
    p = RO.evaluate(ident, [cover("m135", [hit(2)])], [head, both], say=q, manifest=man("m135.x"))["predictions"]
    assert (p["P5"], p["P7"], p["P8"]) == (False, False, False)
    p = RO.evaluate(ident, [cover("m135", [hit(2)])], None, say=q, manifest=man("m135.x"))["predictions"]
    assert p["P7"] is None and p["P8"] is None
    # Proposition H: the sum of n at zeta_H is 4; at most 2 at one s where tau moves Q8; even where tau fixes it
    gold = {"m004.x": {"ez": [1, 1], "m": 2, "golden": True, "acts on Q8 as the identity": False}}
    fixed = {"m135.x": {"ez": [1, 1], "m": 2, "golden": False, "acts on Q8 as the identity": True}}

    def qh(n, s):
        return {"n": n, "zeta": [1, 1], "m": 2, "s": s, "h1": n, "trivial cusps": 0}
    p = RO.evaluate(ident, [cover("m004", [qh(2, [1, 6]), qh(1, [1, 3]), qh(1, [2, 3])])], None, say=q, hcov=gold,
                    manifest=man("m004.x"))["predictions"]
    assert (p["P9"], p["P10"], p["P11"]) == (True, True, None)
    p = RO.evaluate(ident, [cover("m004", [qh(3, [1, 6]), qh(1, [1, 3])])], None, say=q, hcov=gold,
                    manifest=man("m004.x"))["predictions"]
    assert (p["P9"], p["P10"]) == (True, False)
    p = RO.evaluate(ident, [cover("m135", [qh(2, [0, 1]), qh(1, [1, 4])])], None, say=q, hcov=fixed,
                    manifest=man("m135.x"))["predictions"]
    assert (p["P9"], p["P10"], p["P11"]) == (False, None, False)
    p = RO.evaluate(ident, [cover("m004", [qh(4, [0, 1])], chunks=2)], None, say=q, hcov=gold,
                    manifest=man("m004.x", chunks=2))["predictions"]
    assert (p["P9"], p["P10"], p["P11"]) == (None, None, None)


def test_route_w_burau_identity():
    F, T, W = _lib()
    from cypari import pari as P
    s1 = {"a": "abA", "b": "a", "c": "c"}
    s2i = {"a": "a", "b": "c", "c": "Cbc"}
    img = {g: g for g in "abc"}
    for step in (s2i, s1, s2i, s1):
        img = {g: F.substitute(img[g], step) for g in "abc"}
    idx = {"a": 0, "b": 1, "c": 2}
    images = [[(idx[c.lower()], 1 if c.islower() else -1) for c in img[g]] for g in "abc"]
    for m in (7, 12):
        Jb, _ = W.jbar(W.fox_jacobian(images, [1, 1, 1], m), [1, 1, 1], m)
        z = P.Mod(P("y"), P.polcyclo(m, "y"))
        ratio = P.subst(P.charpoly(Jb, "x"), "x", 1) / ((1 + z + z ** 2) * (z ** 2 - 3 * z + 1))
        assert ratio ** (2 * m) == 1, m


def test_structure_m004_m003():
    F, T, W = _lib()
    for sw, ncov, det in (("+LR", 5, 1), ("-LR", 9, 5)):
        st = F.State(sw)
        cv = F.covers(st, 12)
        assert len(cv) == ncov
        for lat, w in cv:
            C = F.Cover(st, lat, w)
            assert C.free_rank == len(C.cusps) - 1
            pt, _ = C.puncture_trivial()
            assert len(pt) == det
            r = T.read(C, [0] * C.n, 0, 1)
            assert r["b1"] == r["cusps"] == len(C.cusps)
