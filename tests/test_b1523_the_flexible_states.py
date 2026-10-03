"""B1523 lock -- THE FLEXIBLE STATES (2026-10-03). sL-10 item 6 at the owner's "all allowed not just m004, choice might be golden",
run as sealed at c13cb636: on every word state to length 12 (758 states, 536 manifolds), is the bundle infinitesimally projectively
rigid rel cusp (so a projective family exists at its hyperbolic point), what is each isometry's sign on the family's line
H^1(M; v), and which rigid states have no isometry that dualises the family.
Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the records: the census (both routes, all 536 manifolds) and the read-out (P1-P9, the counts, the margins);
- live:
  - the enumeration and the kinds (words.py);
  - both routes on the literature's controls (m004, L2R2, R2L): dimensions, signs, slopes, the action on H^1(P; v);
  - Lemma S on m004 (its non-rigid slopes are exactly mu^-1 lam^2, lam, mu lam^2);
  - both routes on the first mirror-broken manifolds;
- X1, after the seal: route F's record in its three passes, and route F live on m004, the first mirror-broken manifold and a
  long golden word;
- hygiene, and the verdict with its registry row.
The census's full rerun (about an hour on four cores) is not locked; its length-6 slice is marked slow."""
import base64
import hashlib
import importlib.util
import json
import re
import sys
import warnings
from pathlib import Path

import mpmath as mp
import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1523_the_flexible_states"
VER = ARC / "verification"
SEALED_SHA = "c61caeb08eb6b794f7123c94a1f213b4f4af8116e0c13a90410603c48d8eb43f"
LOCAL = ("words", "route_r", "route_c", "controls", "census", "read_out", "route_f", "route_f_reach", "route_f_seeded")


def _load(name):
    """this arc's module, with its sibling imports resolved to this arc's files: generic names (census, controls, read_out) exist
    in other arcs, so a module of the same name left in sys.modules by another lock is dropped first"""
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
    """E12 (the b204 pattern): the routes set mp.dps = 60 when they are imported, and tests/conftest.py restores each test's entry
    precision when it ends. A route imported by an earlier test would otherwise run here at 15 digits, where its rank decisions are
    meaningless. The census and the read-out ran as scripts, at the 60 digits their imports set."""
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
    """every file hashed at the seal (the instruments, the read-out and the design-time controls) is byte-identical"""
    lines = [l.split() for l in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    assert len(lines) == 9
    for digest, rel in lines:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == digest, rel
    ctrl = _json("controls.json")
    assert ctrl["all controls pass"] is True and ctrl["failed"] == []
    assert set(k for k in ctrl if re.fullmatch(r"C\d", k)) == {f"C{i}" for i in range(1, 10)}


# ------------------------------------------------------------------------------------------------- live: the words
def test_the_enumeration_and_the_kinds():
    """758 states, 536 manifolds; the kinds by class; 262 without a longitude-inverting isometry, 131 per sign"""
    words = _load("words")
    st, man = words.states(12), words.manifolds(12)
    assert len(st) == 758 and len(man) == 536
    classes = {}
    for m in man.values():
        k = m["kinds"]
        key = "all three" if all(k.values()) else "rev only" if k["rev"] else "swap only" if k["swap"] else \
            "swaprev only" if k["swaprev"] else "none"
        classes[key] = classes.get(key, 0) + 1
    assert classes == {"none": 220, "rev only": 250, "swaprev only": 42, "swap only": 2, "all three": 22}
    no_inv = [m for m in man.values() if not m["a longitude-inverting isometry"]]
    assert len(no_inv) == 262 and sum(1 for m in no_inv if m["sign"] == "+") == 131
    assert sum(len(m["states"]) for m in no_inv) == 482


# ------------------------------------------------------------------------------------------------- live: the controls
def test_both_routes_on_m004():
    """m004 = b++LR: rigid in both routes; sm:B1520's sign table; the cusp lemmas; the fibre boundary rigid, the section not"""
    rr, rc = _load("route_r").record("b++LR"), _load("route_c").record("b++LR")
    for r in (rr, rc):
        assert [r["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1]
    table = {(-1, -1): -1, (-1, 1): -1, (1, -1): 1, (1, 1): 1}
    for x, y in zip(rr["isometries"], rc["isometries"]):
        want = table[(x["cusp map"][0][0], x["cusp map"][1][1])]
        assert abs(x["eps"] - want) < 1e-30 and abs(y["eps"][0] - want) < 1e-30 and abs(y["eps"][1]) < 1e-30
        h = x["on H1(P; v)"]
        if x["det"] == -1:
            assert abs(h["trace"]) < 1e-30 and abs(h["det"] + 1) < 1e-30
    assert rr["cusp"]["slope residual"]["fibre boundary mu"] > 1e-3 and rr["cusp"]["slope residual"]["section lambda"] < 1e-40
    assert rc["slope test"]["fibre boundary mu"] > 1e-4 and rc["slope test"]["section lambda"] < 1e-40


def test_lemma_s_live_on_m004():
    """the non-rigid slopes of m004's class in the box |p| <= 3, 0 <= q <= 3 are exactly mu^-1 lam^2, lam, mu lam^2 (30, 90, 150
    degrees from the fibre boundary): three directions 60 degrees apart, Heusener-Porti's pi/3"""
    box = _load("route_r").record("b++LR", isometries=False)["cusp"]["slope box"]
    zeros = sorted([p, q] for p, q, r, a in box if r < 1e-30)
    assert zeros == [[-1, 2], [0, 1], [1, 2]]
    assert sorted(round(a, 6) for p, q, r, a in box if r < 1e-30) == [30.0, 90.0, 150.0]
    assert all(r > 1e-4 for p, q, r, a in box if [p, q] not in zeros)


# ------------------------------------------------------------------------------------------------- the records
def test_the_census_record():
    """536 manifolds in both routes, none missing, the controls re-read identically; every manifold rigid rel cusp"""
    cen = _json("census.json")
    assert len(cen["manifolds"]) == 536 and cen["missing"] == [] and cen["banked identity (controls re-read)"] is True
    for m in cen["manifolds"]:
        for rt in ("R", "C"):
            assert [m[rt]["H1"][k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1], (m["manifold"], rt)
            assert m[rt]["relator error"] < 1e-35
    assert sum(len(m["states"]) for m in cen["manifolds"]) == 758


def test_the_read_out_record():
    """P1-P9 all held; outcome B; the counts and the margins as banked"""
    r = _json("read_out.json")
    assert all(r["predictions"].values()) and len(r["predictions"]) == 9
    assert r["outcome"].startswith("B:") and r["disagreements"] == [] and r["lemma failures"] == [] and r["lemma S failures"] == []
    c = r["counts"]
    assert (c["manifolds"], c["rigid"], c["rigid with an orientation-reversing isometry"]) == (536, 536, 66)
    assert c["mirror-broken rigid manifolds"] == 262 and c["of them by sign"] == {"+": 131, "-": 131}
    assert c["mirror-broken word states"] == 482
    assert c["mirror-broken by kind"] == {"none": 220, "swaprev only": 42, "swap only": 0, "rev only": 0, "all three": 0}
    assert c["mirror-broken by length"] == {str(n): v for n, v in zip(range(2, 13), [0, 0, 0, 0, 2, 2, 8, 14, 36, 62, 138])}
    assert sorted(c["golden mirror-broken"]) == ["+LLLLRLLLRR", "+LLLLRLRRRLRR", "-LLLLRLLLRR", "-LLLLRLRRRLRR"]
    assert c["fibre boundary rigid"] == 536 and c["fibre boundary not rigid"] == [] and c["longitude rule fails on"] == []
    assert c["section rigid"] == 513 and len(c["section not rigid"]) == 23
    m = r["margins"]
    assert m["v: largest dropped singular value (Fox, route R / C)"][0] < 1e-40 and m["v: smallest kept singular value (Fox, route R / C)"][0] > 1e-8
    assert m["slope residual: smallest counted nonzero / largest counted zero (route R)"][1] < 1e-45


def test_the_non_rigid_slopes_sit_only_on_the_reflective_manifolds():
    """after the run: the box holds a non-rigid slope on exactly the 66 reflective manifolds, all in the coset 30 + 60Z"""
    r = _json("read_out.json")
    with_zero = {k: v for k, v in r["zero slopes in the box, by manifold"].items() if v}
    reflective = {row["manifold"] for row in r["rows"] if row.get("orientation-reversing isometry")}
    assert set(with_zero) == reflective and len(reflective) == 66
    assert all(abs((a - 30.0) % 60.0) < 1e-6 or abs((a - 30.0) % 60.0 - 60.0) < 1e-6 for v in with_zero.values() for p, q, a in v)


# ------------------------------------------------------------------------------------------------- live: the first mirror-broken state
@pytest.mark.parametrize("name", ["b++LLRLRR", "b+-LLRLRR"])
def test_the_first_mirror_broken_state_live(name):
    """+-LLRLRR (length 6, swaprev only): rigid in both routes, its orientation-reversing map keeps the fibre boundary and has
    eps = +1, so no isometry dualises the family"""
    rr, rc = _load("route_r").record(name), _load("route_c").record(name)
    for r in (rr, rc):
        assert [r["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1]
    for x, y in zip(rr["isometries"], rc["isometries"]):
        assert x["cusp map"] == y["cusp map"] and abs(x["eps"] - y["eps"][0]) < 1e-30
        assert x["eps"] > 0, (name, x["cusp map"])            # nothing dualises
    assert any(x["det"] == -1 and not x["inverts the fibre boundary"] for x in rr["isometries"])
    assert rr["cusp"]["slope residual"]["fibre boundary mu"] > 1e-3


@pytest.mark.slow
def test_the_census_slice_to_length_6():
    """the census's own code rerun on the 24 manifolds of length <= 6 (about ten minutes on one core): every dimension and every
    isometry's cusp map and sign agree with census.json in both routes"""
    words, census = _load("words"), _load("census")
    banked = {m["snappy"]: m for m in _json("census.json")["manifolds"]}
    recs = sorted((m for m in words.manifolds(12).values() if m["length"] <= 6), key=lambda m: m["snappy"])
    assert len(recs) == 24
    for rec in recs:
        out, b = census.one(rec), banked[rec["snappy"]]
        assert "error" not in out, (rec["snappy"], out.get("error"))
        for rt in ("R", "C"):
            dims = [out[rt]["H1"][k]["dim"] for k in ("triv", "so", "v")]
            assert dims == [b[rt]["H1"][k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1], (rec["snappy"], rt)
            assert [i["cusp map"] for i in out[rt]["isometries"]] == [i["cusp map"] for i in b[rt]["isometries"]]
            for x, y in zip(out[rt]["isometries"], b[rt]["isometries"]):
                ex, ey = (x["eps"], y["eps"]) if rt == "R" else (x["eps"][0], y["eps"][0])
                assert abs(ex - ey) < 1e-20, (rec["snappy"], rt, x["cusp map"])


# ------------------------------------------------------------------------------------------------- X1: route F (after the seal)
def _fixed_sign_characters(word):
    """how many sign characters of the fibre (Hom(F_2, Z/2), four) the monodromy fixes: the vectors of (Z/2)^2 fixed by the
    word's matrix mod 2"""
    L, R, M = ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((1, 0), (0, 1))
    for c in word:
        A = L if c == "L" else R
        M = tuple(tuple(sum(M[i][k] * A[k][j] for k in range(2)) % 2 for j in range(2)) for i in range(2))
    return sum(all((M[i][0] * v[0] + M[i][1] * v[1] - v[i]) % 2 == 0 for i in range(2))
               for v in ((0, 0), (0, 1), (1, 0), (1, 1)))


def test_route_f_record():
    """X1, written after the seal and disclosed: route F rebuilds each bundle from its word and reads it with its own code, in three
    passes that differ only in how the hyperbolic fixed point is found (the first two with no SnapPy holonomy, on a stratified 118;
    the third seeded from SnapPy's holonomy, on all 536). Every manifold reached agrees with the census on the three dimensions and
    on the fibre boundary, and the seeded and unseeded passes read the same where both reached a manifold."""
    first, second, third = _json("route_f_batch.json"), _json("route_f_reach.json"), _json("route_f_seeded.json")
    assert first["chosen"] == 118 and first["disagree"] == [] and second["disagree"] == [] and third["disagree"] == []
    assert first["agree with the census (dimensions and the fibre boundary)"] == first["reached"] == 60
    assert second["first pass not reached"] == len(first["not reached"]) == 58
    assert second["agree with the census (dimensions and the fibre boundary)"] == second["reached now"] == 6
    still = [
        "+LLLLLRLRRRRR", "+LLLLRLRLRRRR", "+LLLLRLRRRLRR", "+LLLLRLRRRRLR", "+LLLLRRLLRRRR", "+LLLRLLRR", "+LLLRLLRRLRRR",
        "+LLLRLLRRRLRR", "+LLLRLRLR", "+LLLRLRLRLRRR", "+LLLRLRLRRR", "+LLLRLRLRRRLR", "+LLLRLRRRLLRR", "+LLLRLRRRLR",
        "+LLLRRLLRRR", "+LLLRRLRLLRRR", "+LLRLLRLR", "+LLRLLRLRRLRR", "+LLRLLRRLRR", "+LLRLRLRLRLRR", "+LLRLRLRLRR",
        "+LLRLRLRLRRLR", "+LLRLRLRR", "+LLRLRLRRLLRR", "+LLRLRLRRLR", "+LLRLRLRRLRLR", "+LLRLRRLLRR", "+LLRLRRLR", "-LLLLLRLRRRRR",
        "-LLLLRLRLRRRR", "-LLLLRLRRRLRR", "-LLLLRRLLRRRR", "-LLLRLLRR", "-LLLRLLRRLRRR", "-LLLRLLRRRLRR", "-LLLRLRLR",
        "-LLLRLRLRLRRR", "-LLLRLRLRRR", "-LLLRLRLRRRLR", "-LLLRLRRRLLRR", "-LLLRRLLRRR", "-LLLRRLRLLRRR", "-LLRLLRLR",
        "-LLRLLRLRRLRR", "-LLRLRLRLRLRR", "-LLRLRLRLRR", "-LLRLRLRLRRLR", "-LLRLRLRR", "-LLRLRLRRLLRR", "-LLRLRLRRLR",
        "-LLRLRRLLRR", "-LLRLRRLR"
    ]
    assert sorted(second["still not reached"]) == still and len(still) == 52
    assert third["manifolds"] == 536 and third["errors"] == [] and third["not reached"] == []
    assert third["agree with the census (dimensions and the fibre boundary)"] == third["reached"] == 536
    # the seeded pass's first attempt found no seed for +-L3RLRLR2LR2 in the word's own basis (route_f_seeded_run.txt); the
    # fallback added after it reads them through a rotation of the word, the same oriented manifold (route_f_seeded_retry_run.txt)
    assert third["read through a rotation of the word"] == ["+LLLRLRLRRLRR", "-LLLRLRLRRLRR"]
    rot = {d["state"]: d for d in third["records"] if "rotations tried" in d}
    assert sorted(rot) == ["+LLLRLRLRRLRR", "-LLLRLRLRRLRR"]
    assert all(d["rotations tried"][0] == {"rotation": s, "seeds": 0, "matching roots": 0} for s, d in rot.items())
    assert {s: d["rotation read"] for s, d in rot.items()} == {"+LLLRLRLRRLRR": "+LLRLRLRRLRRL", "-LLLRLRLRRLRR": "-LRLRLRRLRRLL"}
    assert third["reached also by a pass without SnapPy's holonomy"] == 66 and third["readings differing from those passes"] == []
    for rec in (second, third):
        assert rec["matching roots whose readings disagree"] == []
    # several roots can match the cusp shape: the representation twisted by a sign character of the fibre that the monodromy fixes
    # is again a fixed point of the trace map, with the same image in PSL(2, C). In the seeded pass, which tries every sign change
    # of its seed, the number of matching roots is that number of characters on every manifold.
    assert all(d["matching roots (up to conjugation)"] == _fixed_sign_characters(d["state"][1:]) for d in third["records"])
    assert {_fixed_sign_characters(w) for w in ("LR", "LLLLRLLR", "LLRLLRR")} == {1, 4, 2}
    for rec in (first, second, third):
        assert rec["smallest fibre-boundary residual among those reached"] > 1e-8


@pytest.mark.parametrize("sign", ["+", "-"])
def test_route_f_live(sign):
    """route F live (its second pass's root search), on m004 and on the first mirror-broken manifold +-LLRLRR: (1, 2, 1) and a
    rigid fibre boundary, with SnapPy's cusp shape used only to pick the hyperbolic fixed point"""
    import snappy
    R = _load("route_f_reach")
    for word in ("LR", "LLRLRR"):
        shape = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
        out = R.record(sign, word, shape)
        assert out["hyperbolic found"] and out["readings agree"], (sign, word)
        assert [out["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1], (sign, word)
        assert out["fibre boundary residual"] > 1e-6 and out["T residual"] < 1e-40, (sign, word)


def test_route_f_seeded_live_on_a_long_golden_word():
    """the seeded pass live on +L4RLR3LR2 (golden, length 12; the unseeded passes missed it): the located point is a fixed point
    of route F's trace map with SnapPy's cusp shape, and route F reads (1, 2, 1) with a rigid fibre boundary"""
    import snappy
    S = _load("route_f_seeded")
    shape = complex(snappy.Manifold("b++LLLLRLRRRLRR").cusp_info("shape")[0])
    out = S.record("+", "LLLLRLRRRLRR", shape)
    assert out["hyperbolic found"] and out["readings agree"]
    assert [out["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1]
    assert out["fibre boundary residual"] > 1e-6 and out["T residual"] < 1e-40


@pytest.mark.slow
def test_route_f_seeded_live_through_a_rotation():
    """the seeded pass's fallback live on +L3RLRLR2LR2 (about two minutes): the word's own basis gives no seed, its first
    rotation does, and route F reads (1, 2, 1) with a rigid fibre boundary"""
    import snappy
    S = _load("route_f_seeded")
    shape = complex(snappy.Manifold("b++LLLRLRLRRLRR").cusp_info("shape")[0])
    out = S.record("+", "LLLRLRLRRLRR", shape)
    assert out["rotations tried"][0]["seeds"] == 0 and out["rotation read"] == "+LLRLRLRRLRRL"
    assert out["hyperbolic found"] and out["readings agree"]
    assert [out["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [1, 2, 1]
    assert out["fibre boundary residual"] > 1e-6 and out["T residual"] < 1e-40


# ------------------------------------------------------------------------------------------------- hygiene and surfaces
def test_hygiene():
    """no vendor word, no private term, no Gate 5-Q word in the arc's text"""
    tokens = [base64.b64decode(t).decode() for t in ("Y2xhdWRl", "YW50aHJvcGlj", "b3B1cw==", "c29ubmV0", "ZmFibGU=")]
    private = bytes([98, 114, 97, 118, 101]).decode()
    for f in list(ARC.glob("*.md")) + list(VER.glob("*.py")) + [ARC / "arc_verdict.json"]:
        t = f.read_text(encoding="utf-8")
        for w in tokens:
            assert not re.search(re.escape(w), t, re.I), (f.name, "vendor word")
        assert private not in t.lower(), f.name
        for w in ("qualia", "aware", "sees"):
            assert not re.search(r"\b" + w + r"\b", t, re.I), (f.name, w)


def test_the_verdict_and_the_registry():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1523" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["prior_work"]["standing"] == "EXTENDS"
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "T-FLEXIBLE-STATES" in reg and "B1523" in reg
