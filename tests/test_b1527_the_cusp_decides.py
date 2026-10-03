"""B1527 lock -- THE CUSP DECIDES (2026-10-03). sL-10 item 8: the class index on the projective deformations of the word states
near their hyperbolic point, run as sealed at 4f802f15. PROVED, with a kill record; as sealed one prediction of eight held (P1)
and the read-out returns outcome C, because the sealed scan found type-one points only on +LR (an instrument defect, E31).
Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the records: the run's ten manifolds and the read-out (P1-P8) exactly as banked;
- the post-run records (disclosed in FINDINGS section 4): the diagnosis of the scan's budget; X1's six frames on nine manifolds
  and X1c's two on the tenth, exactly 60 degrees apart, with the lines of FINDINGS section 0; X2's index rows at 100 digits
  (I = 0 on 1,656 rows, route W agreeing on its 240, the sealed margin bar met, the nullities 4 and 5); the soft singular
  value's scaling with a (post_run_soft_run.txt);
- the points exported for main's L242 (e): sixty, no reading in the file, each frame as banked, and each a representation
  (the relators and the cusp's commutator read live from the exported matrices);
- live:
  - the slice's closed form against mpmath (C1);
  - the positive control: sm:B1509's I(W1) = -1 and I(W2) = +1, transported to +LR, in both routes (C4);
  - Part H on the first mirror-broken manifold (+LLRLRR) at the cusp-trivial twist and at 1.7, both modules, both routes;
  - Lemma E's identity on every one of those readings;
  - Part A's step in exact arithmetic (part_a_lemma.py: the slice's a- and b-directions lie in v);
- hygiene, and the verdict with its registry row and its kill record.
The full run and the post-run checks (hours on four cores) are not locked; one type-one point is rebuilt and polished live in a
slow test."""
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
ARC = ROOT / "frontier" / "B1527_the_cusp_decides"
VER = ARC / "verification"
SEALED_SHA = "ebb8c34ed282f30c0ca9ee02292b0b39445c010bda426faefe7bbbd545339bce"
LOCAL = ("cusp_lib", "family_lib", "scan_lib", "wang_lib", "controls", "run", "read_out", "post_run_x1",
         "part_a_lemma")


def _load(name):
    """this arc's module, with its sibling imports resolved to this arc's files: generic names (run, controls, read_out) exist in
    other arcs, so a module of the same name left in sys.modules by another lock is dropped first"""
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
    """E12 (the b204 pattern): cusp_lib sets mp.dps = 60 when it is imported, and tests/conftest.py restores each test's entry
    precision when it ends. A module imported by an earlier test would otherwise run here at 15 digits."""
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


# ------------------------------------------------------------------------------------------------- the records
def test_the_run_covers_the_ten_manifolds():
    run = _load("run")
    for sign, word in run.MANIFOLDS:
        rec = _json("run_" + run.name_of(sign, word) + ".json")
        assert rec["manifold"] == sign + word
        assert rec["H"]["rows"], sign + word


def test_the_read_out_is_as_banked():
    """read_out.py's readers, applied in memory to the run records, reproduce read_out.json's per-manifold verdicts (nothing is
    written)"""
    ro = _load("read_out")
    run = _load("run")
    banked = _json("read_out.json")
    assert banked["manifolds"] == 10 and banked["missing"] == []
    for sign, word in run.MANIFOLDS:
        rec = _json("run_" + run.name_of(sign, word) + ".json")
        row = banked["rows"][sign + word]
        for P, f in (("P1", ro.p1), ("P2", ro.p2), ("P4", ro.p4), ("P5", ro.p5), ("P6", ro.p6), ("P7", ro.p7)):
            assert f(rec)["holds"] == row[P]["holds"], (sign + word, P)
        if sign + word in ro.REFLECTIVE:
            assert ro.p3(rec)["holds"] == row["P3"]["holds"], (sign + word, "P3")


# ------------------------------------------------------------------------------------------------- live
def test_the_slice_closed_form():
    S = _load("scan_lib")
    assert S.selftest() < 1e-13


def test_the_positive_control_both_routes():
    """sm:B1509's exact extension indices at q = 17 + 12 sqrt2, mu = -1, transported to +LR: I(W1) = -1 and I(W1[A*]) = -1
    (so I(W2) = +1) in route Fox and in route W, with every identity"""
    L = _load("cusp_lib")
    FL = _load("family_lib")
    WL = _load("wang_lib")
    controls_src = (VER / "controls.py").read_text(encoding="utf-8")
    assert "def transport(mod)" in controls_src
    G, img = FL.word_group("+", "LR")
    q = 17 + 12 * mp.sqrt(2)
    B = L.ballas(q)
    A = L.Module({g: -B.M[g] for g in ("m", "n")})

    def transport(mod):
        m, n = mod.M["m"], mod.M["n"]
        mi = mp.inverse(m)
        ni = mp.inverse(n)
        return L.Module({"a": n * mi, "b": m * ni * m * n * mi * mi, "t": m})
    for base in (A, A.dual()):
        z, _ = L.cocycle_generator(L.BALLAS, base)
        W = transport(L.extension(base, z))
        fox = L.class_index(G, W)
        wang = WL.index_wang(img, G.cusp, {g: W.M[g] for g in "abt"})
        assert fox["I"] == wang["I"] == -1
        assert all(fox["checks"].values())


def test_part_h_on_the_first_mirror_broken_state():
    """Part H on +LLRLRR: the trivial character at the cusp-trivial twist (t0 = s0 = 1 for the four, 2 for Lambda^2) and at 1.7
    (acyclic), I = 0 in both routes, Lemma E holding"""
    L = _load("cusp_lib")
    FL = _load("family_lib")
    WL = _load("wang_lib")
    G, img = FL.word_group("+", "LLRLRR")
    A2, B2, T2, _ = FL.hyperbolic_sl2("+", "LLRLRR")
    rho = FL.paraboloid_module(FL.to_cusp_frame(A2, B2, T2, "+", 0))
    for lam, t0 in ((mp.mpf(1), (1, 2)), (mp.mpf("1.7"), (0, 0))):
        for wedge, want in ((False, t0[0]), (True, t0[1])):
            mats = {g: (lam if g == "t" else 1) * (L.wedge2(rho.M[g]) if wedge else rho.M[g]) for g in "abt"}
            fox = L.class_index(G, L.Module(mats))
            wang = WL.index_wang(img, G.cusp, mats)
            assert fox["I"] == wang["I"] == 0
            assert fox["V"]["t0"] == fox["V*"]["t0"] == want
            assert all(fox["checks"].values())


def test_part_a_step_exactly():
    """the step Part A states in one line: at a = b = 0 the slice's a- and b-directions are Q-symmetric (they lie in v), with
    D_a = X(E22 - I/4) + (X^2/2)(E12 - E24) - (X^3/3)E14, zero exactly when X = 0 (sympy, and a central difference of expm)"""
    P = _load("part_a_lemma")
    assert P.main() == 0


# ------------------------------------------------------------------------------------------------- the post-run records
def _frames(name):
    x1 = _json("x1_" + name + ".json")
    out = [p for p in x1["points"] if p.get("point")]
    if name == "mLLLLRLRRRLRR":
        x1c = _json("x1c_" + name + ".json")
        out += [{"alpha": r["alpha"], "beta": r["beta"], "point": None} for r in x1c["new points"]]
    return out


LINES = {"LR": 0.0, "LLRLRR": 0.0, "LLLRLRR": 8.2555, "LLLLRLLLRR": 20.1143, "LLLLRLRRRLRR": 0.95}


def test_the_diagnosis():
    """the sealed solver (80 iterations) from seeds off +LR's frames: 74 iterations from 0.32 degrees at 300, more than 80
    everywhere else off the frame"""
    d = _json("post_run_diagnosis.json")
    it = {(p["frame"], p["offset (deg)"]): p["iterations"] for p in d["probes"]}
    assert all(p["converged"] for p in d["probes"])
    assert it[(300.0, 0.32)] <= 80 < it[(0.0, 0.32)]
    assert min(it[(f, o)] for f in (300.0, 0.0) for o in (1.0, 2.5)) > 80
    assert it[(300.0, 0.0)] == it[(0.0, 0.0)] == 7


def test_six_frames_sixty_degrees_apart_on_all_ten():
    """X1 (and X1c on -L4RLR3LR2): six type-one frames, at alpha_1 + 60 k, and three lines beta, on every manifold"""
    run = _load("run")
    for sign, word in run.MANIFOLDS:
        name = run.name_of(sign, word)
        pts = _frames(name)
        assert len(pts) == 6, name
        a1 = LINES[word]
        for p in pts:
            off = (p["alpha"] - a1) % 60.0
            assert min(off, 60.0 - off) < 1e-3, (name, p["alpha"])
            b = (p["beta"] - a1 - 30.0) % 60.0
            assert min(b, 60.0 - b) < 1e-3, (name, p["beta"])
        assert len({round(p["alpha"] % 360.0) % 360 for p in pts}) == 6, name


def test_the_type_one_points_at_100_digits():
    """X2: every type-one point polished at 100 digits; every index row I = 0 with an acyclic cusp, a0 = b0 = 0, every
    identity, route W agreeing, the sealed margin bar met; the rows agree with the 60-digit ones; nullities 4 and 5"""
    s = _json("x2.json")
    tot = s["totals"]
    assert all(v != "missing" for v in s["manifolds"].values())
    assert tot["points"] == 60
    assert tot["rows with I != 0"] == 0 and tot["rows differing from 60 digits"] == 0
    assert tot["rows failing an identity"] == 0 and tot["rows with a non-acyclic cusp"] == 0
    assert tot["rows with a0 or b0 != 0"] == 0
    assert tot["rows meeting the sealed margin bar (kept > 1e-20, dropped < 1e-40)"] == tot["rows"] == 1656
    assert tot["route W rows"] == 240
    assert tot["points with nullities 4 and 5 (100 digits)"] == 60
    run = _load("run")
    w = 0
    for sign, word in run.MANIFOLDS:
        for p in _json("x2_" + run.name_of(sign, word) + ".json")["points"]:
            assert p["nullity, type one (100 digits)"]["nullity"] == 4 and p["nullity, b free (100 digits)"]["nullity"] == 5
            for r in p["index rows"]:
                if "W" in r:
                    w += 1
                    assert r["W"]["I"] == r["I"] == 0
                    assert (r["W"]["h1(V)"], r["W"]["h1(V*)"], r["W"]["t0"]) == (r["V"]["h1"], r["V*"]["h1"], r["V"]["t0"])
    assert w == 240


def test_the_soft_value_scales_with_a():
    """post_run_soft.py: the type-one Jacobian's soft singular value at a = 1e-5, 4e-5 and 1.6e-4 on +LR and +LLLRLRR, in the
    ratios 1 : 4 : 16, with the nullity 4 at every reading"""
    lines = [ln for ln in (VER / "post_run_soft_run.txt").read_text(encoding="utf-8").splitlines() if " a = " in ln]
    assert len(lines) == 6
    for ln, want in zip(lines, (1.0, 4.0, 16.0) * 2):
        assert "nullity 4," in ln
        ratio = float(re.search(r"ratio to a = 1e-5: ([0-9.]+)", ln).group(1))
        assert abs(ratio - want) < 2e-3 * want, ln


def test_the_points_for_main():
    """points_for_l242e.json: the sixty type-one points with no reading in the file, each frame as banked, and each a
    representation: the bundle relators and the cusp's commutator read from the exported matrices at 60 digits"""
    L = _load("cusp_lib")
    doc = _json("points_for_l242e.json")
    raw = (VER / "points_for_l242e.json").read_text(encoding="utf-8")
    for key in ('"I"', '"index rows"', "eigenvalue", "margin", "nullity", '"h1', '"t0"'):
        assert key not in raw, key
    run = _load("run")
    assert list(doc["manifolds"]) == [sg + wd for sg, wd in run.MANIFOLDS]
    n = 0
    for name, m in doc["manifolds"].items():
        assert len(m["points"]) == 6, name
        G = L.Group(m["generators"], m["relators"], tuple(m["cusp words"]), name)
        for p in m["points"]:
            n += 1
            assert p["frame agrees (1e-3 deg)"] and float(p["polished |F|"]) < 1e-48, (name, p["frame alpha (deg)"])
            mats = {g: mp.matrix([[mp.mpf(x) for x in row] for row in p["matrices"][g]]) for g in "abt"}
            mod = L.Module(mats)
            for rel in G.rels:
                assert mp.mnorm(mod.word(rel) - mp.eye(4), 1) < mp.mpf(10) ** -40, (name, rel)
            l, t = G.cusp
            assert mp.mnorm(mod.word(l + t + L.inv_word(l) + L.inv_word(t)) - mp.eye(4), 1) < mp.mpf(10) ** -40, name
    assert n == 60


@pytest.mark.slow
def test_a_type_one_point_live():
    """+LLRLRR's type-one point at the frame 60 degrees, rebuilt as X1 builds it and polished at 60 digits: rho(l) has no
    eigenvalue 1, the cusp is acyclic and I = 0 for the trivial character at lambda = 1 (Part A, Lemma C)"""
    import numpy as np
    run = _load("run")
    FL = _load("family_lib")
    L = _load("cusp_lib")
    S = _load("scan_lib")
    saved = (run.A_SCAN, FL.solve_type_one)
    try:
        X1 = _load("post_run_x1")
        P = X1.Pinned("+", "LLRLRR")
        rec = P.solve(np.radians(60.0))
        assert rec["converged"]
        u1, f1, _ = X1.gauss_newton(lambda v: S.residual(v, X1.A, rec["W"], False).real,
                                    lambda v: S.jacobian(v, X1.A, rec["W"], False), rec["u"][:52], 0.3 * rec["threshold"])
        G, img = FL.word_group("+", "LLRLRR")
        U = mp.matrix([mp.mpf(x) for x in u1])
        Up, fp, _, _ = X1.polish_gn(U, mp.mpf(X1.A), G, img, tol=mp.mpf(10) ** -48, maxit=40)
        assert fp < mp.mpf(10) ** -40
        mats, (Xl, Yl, _, _) = FL.unpack(Up)
        assert abs(float(mp.degrees(mp.atan2(Yl, Xl))) - 60.0) < 1e-3
        mod = L.Module(mats)
        ev = FL.eig_sorted(mod.word("abAB"))
        assert min(abs(e - 1) for e in ev) > mp.mpf(10) ** -6
        out = L.class_index(G, mod)
        assert out["I"] == 0 and out["V"]["t0"] == 0 and out["V*"]["t0"] == 0 and out["V"]["h1(Delta)"] == 0
        assert all(out["checks"].values())
    finally:
        run.A_SCAN, FL.solve_type_one = saved


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
    assert v["id"] == "B1527"
    assert v["verdict"] == "PROVED"
    assert "B1527" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r["id"] == "B1527"]
    assert len(rec) == 1 and rec[0]["scope"]["frame"] == "F-HE" and rec[0]["fact_computed"] is True
