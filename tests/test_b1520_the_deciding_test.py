"""B1520 lock -- THE DECIDING TEST ON THE BRIDGE'S VACUA (2026-10-02). The owner's selection-rule handoff (section 4), made exact by
main's B1455 and run independently here: is every vacuum mu (x) rho_q of m004's Ballas family fixed by a count-odd map? Sealed at
dda82524 before the population ran; outcome A, the registered kill; NEGATIVE.
Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the records: the symmetries, both routes (controls and the 32 decisions), the follow-up, the read-out, the post-run checks, the lift;
- live:
  - the witness D.theta by route 2's Theorem T (all 768 traces equal) and D.id's exact locus {1};
  - the witness and the twist by the post-run solver at a rational point that no sealed run used;
  - the follow-up at one prime-root pair: I(W1) = -1, a bare image -1, a dualised image +1;
  - the E8 lift's two facts;
- the kill-graph entry, the verdict, the findings' load-bearing sentences, and hygiene.
The two routes' full reruns (17 s and 27 s) are marked slow."""
import hashlib
import importlib.util
import json
import re
import sys
from fractions import Fraction as Fr
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1520_the_deciding_test"
VER = ARC / "verification"
SEALED_SHA = "5d55ef5632cae081ed734b057f0f1aebb817a42041dac9cd65bacefd692f0ed7"
FIXERS = {"id", "s", "tau.theta", "tau.s.theta", "D.theta", "D.s.theta", "D.tau.id", "D.tau.s"}


def _load(name):
    if str(VER) not in sys.path:
        sys.path.insert(0, str(VER))
    spec = importlib.util.spec_from_file_location(f"b1520_{name}", VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"b1520_{name}"] = mod
    spec.loader.exec_module(mod)
    return mod


def _json(name):
    return json.loads((VER / name).read_text(encoding="utf-8"))


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    """every file hashed at the seal (the instruments and the design-time outputs) is byte-identical"""
    lines = [l.split() for l in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    assert len(lines) == 12
    for digest, rel in lines:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == digest, rel


# ------------------------------------------------------------------------------------------------- the records
def test_the_symmetries_record():
    sym = _json("symmetries.json")
    reps = sym["representatives"]
    assert sym["passed"] and sym["S2 SnapPy"] == {"group": "D4", "order": 8, "amphichiral": True}
    assert set(reps) == {"id", "theta", "s", "s.theta", "tau.id", "tau.theta", "tau.s", "tau.s.theta"}
    for k, v in reps.items():
        assert v["automorphism"] is True and v["endomorphism (R -> 1)"] is True, k
        assert v["orientation"] == ("reversed" if k.startswith("tau") else "kept"), k
        assert v["on H1"] == (-1 if k.endswith("theta") else 1), k
    simple = sym["main B1455's eight simple maps"]
    assert sum(1 for v in simple.values() if v["automorphism"]) == 4
    assert all(v["orientation"] == "kept" for v in simple.values() if v["automorphism"])


def test_the_two_routes_record():
    r1, r2 = _json("route_intertwiner.json"), _json("route_traceform.json")
    assert r1["controls"]["controls passed"] and r2["controls"]["controls passed"]
    assert r2["positive roots of det Gram"] == []
    assert len(r1["table"]) == len(r2["table"]) == 16
    for key in r1["table"]:
        fix = key in FIXERS
        a, b = r1["table"][key], r2["table"][key]
        assert a["to rho_q"]["isomorphic for every q > 0"] is fix and a["to rho_{1/q}"]["isomorphic for every q > 0"] is (not fix), key
        assert b["to rho_q"]["all Theorem-T traces equal"] is fix and b["to rho_{1/q}"]["all Theorem-T traces equal"] is (not fix), key
        good = a["to rho_q"] if fix else a["to rho_{1/q}"]
        assert good["dim over Q(q)"] == 1 and good["X verified"] and good["positive zeros of det X"] == [], key
        assert b["to rho_q"]["conjugate exactly at q > 0"] == ("every q > 0" if fix else ["1"]), key
        assert b["to rho_{1/q}"]["conjugate exactly at q > 0"] == (["1"] if fix else "every q > 0"), key
    assert r1["table"]["D.theta"]["to rho_q"]["det X"] == "-16*q**3*(q**2 + q + 1)"
    assert r1["table"]["D.id"]["to rho_{1/q}"]["det X"] == "-16*q*(q**2 + q + 1)"


def test_the_followup_and_the_read_out():
    fol, dec = _json("followup_index.json"), _json("decide.json")
    assert fol["BANKED IDENTITY: I(W1) = -1 at all six prime-root pairs (B1509)"] is True
    assert fol["every bare image -1 and every dualised image +1"] is True and len(fol["maps"]) == 16 and len(fol["rows"]) == 6
    assert dec["registered outcome"] == "A" and dec["predictions true"] == 6 and all(dec["predictions"].values())
    assert dec["the two routes agree on all 32 decisions"] and dec["every control and banked identity passed"]
    assert set(dec["stabiliser of a vacuum q != 1 (maps fixing every q)"]) == FIXERS
    assert dec["count-odd maps fixing every vacuum, every twist mu"] == ["D.theta", "D.s.theta"]
    assert dec["of these, orientation kept (Lemma G's charge conjugation needs one)"] == ["D.theta", "D.s.theta"]
    assert dec["maps leaving the family"] == [] and dec["P2: rho_q* vs rho_q conjugate exactly at q > 0"] == ["1"]


def test_the_post_run_record():
    pr = _json("post_run_check.json")
    assert pr["passed"] is True
    assert pr["X1 third route at rational points (own Fraction elimination)"]["all 224 decisions as sealed"] is True
    assert len(pr["X1 third route at rational points (own Fraction elimination)"]["rows"]) == 112
    assert pr["X2 the witness D.theta against R47 F14's J"]["all points"] is True
    assert pr["X3 the twist computed (Lemma Tw)"]["all 48 as Lemma Tw"] is True and len(pr["X3 the twist computed (Lemma Tw)"]["rows"]) == 48
    rows = pr["X4 the stabiliser of a vacuum, all sixteen maps"]["rows"]
    generic = [r for r in rows if r["q"] != "1" and r["mu"] not in ("-1", "1")]
    assert len(generic) == 2
    for r in generic:
        assert r["stabiliser"] == ["D.s.theta", "D.theta", "id", "s"] and r["orientation-reversing members"] == []
    assert [r["order"] for r in rows] == [4, 4, 8, 8, 16]


def test_the_lift_record():
    lift = _json("lift_e8.json")
    assert lift["passed"] and lift["E1 steps (= number of positive roots)"] == 120 and lift["E1 w0 = -1"]
    assert lift["E2 both blocks A4, orthogonal"]


# ------------------------------------------------------------------------------------------------- live
def test_live_witness_by_route_two():
    """Theorem T: D.theta's image of rho_q has all 768 traces of rho_q (conjugate at every q > 0); D.id's are equal exactly at q = 1"""
    R2 = _load("route_traceform")
    rho = R2.ballas()
    basis = _json("route_traceform.json")["basis words"]
    reps = {k: {"m": v["m"], "n": v["n"]} for k, v in _json("symmetries.json")["representatives"].items()}
    assert R2.compare(R2.pulled_back(rho, reps["theta"], True), rho, basis)[0] is True
    eq, _, locus = R2.compare(R2.pulled_back(rho, reps["id"], True), rho, basis)
    assert eq is False and locus == ["1"]
    assert R2.Rep(rho).trace("nMNmmNMn") == R2.L({1: 3, -3: 1})          # B1510 Lemma R, banked


def test_live_witness_and_twist_at_a_new_point():
    """at q = 3/2 (used by no sealed run): D.theta and D.s.theta fix mu (x) rho_q for mu = 4; D.tau.id fixes rho_q but sends the
    twist to mu^-1; theta pairs q with 1/q"""
    X = _load("post_run_check")
    q, mu = Fr(3, 2), Fr(4)
    rho, rho_inv = X.ballas(q), X.ballas(1 / q)
    reps = {k: {"m": v["m"], "n": v["n"]} for k, v in _json("symmetries.json")["representatives"].items()}
    tw = {g: [[mu * x for x in r] for r in rho[g]] for g in ("m", "n")}
    tw_inv = {g: [[x / mu for x in r] for r in rho[g]] for g in ("m", "n")}

    def iso(S, T):
        B = X.intertwiners(S, T)
        return len(B) == 1 and X.det(B[0]) != 0

    for name in ("theta", "s.theta"):
        assert iso(X.image(tw, reps[name], True), tw) and not iso(X.image(tw, reps[name], True), tw_inv), name
    assert iso(X.image(tw, reps["tau.id"], True), tw_inv) and not iso(X.image(tw, reps["tau.id"], True), tw)
    assert iso(X.image(rho, reps["theta"], False), rho_inv) and not iso(X.image(rho, reps["theta"], False), rho)


def test_live_followup_at_one_pair():
    """p = 1009, one root of 2: I(W1) = -1 (B1509), a bare image -1 (tau, orientation-reversing), a dualised image +1 (D.theta)"""
    FI = _load("followup_index")
    EX, IL = FI.EX, FI.IL
    p = 1009
    F = IL.GF(p)
    q0 = (17 + 12 * F.sqrt(2)) % p
    A = IL.Rep(F, ["m", "n"], EX.modp_rep(F, q0, p - 1))
    W1 = EX.modp_ext(F, A, EX.modp_cocycle(F, A))
    assert IL.index(W1, [FI.R], FI.MU, FI.LAM)[0] == -1
    reps = FI.representatives()
    assert IL.index(FI.transformed(F, W1, reps["tau.id"], False), [FI.R], FI.MU, FI.LAM)[0] == -1
    assert IL.index(FI.transformed(F, W1, reps["theta"], True), [FI.R], FI.MU, FI.LAM)[0] == 1


def test_live_lift():
    E = _load("lift_e8")
    W0, steps, _ = E.longest_element(E.cartan())
    assert steps == 120 and W0 == [[-1 if r == c else 0 for c in range(8)] for r in range(8)]


@pytest.mark.slow
def test_the_two_routes_rerun():
    """the sealed routes rerun in full reproduce the recorded 32 decisions"""
    R1, R2 = _load("route_intertwiner"), _load("route_traceform")
    t1 = R1.run()
    rho, basis, _ = R2.setup()
    t2 = R2.run(rho, basis)
    for key in t1:
        fix = key in FIXERS
        assert t1[key]["to rho_q"]["isomorphic for every q > 0"] is fix and t2[key]["to rho_q"]["all Theorem-T traces equal"] is fix


# ------------------------------------------------------------------------------------------------- the record
def test_the_kill_graph_entry():
    """the NEGATIVE is routed with content (B1207's A3), with its scope"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1520"]
    assert len(rec) == 1
    r = rec[0]
    assert r["fact_computed"] is True and r["routed_from"] == "sm-branch-2026-10-02-banking"
    assert r["kill_form"].startswith("symmetry-cannot-select") and len(r["hatch"]) > 80
    assert "tests/test_b1520_the_deciding_test.py" in r["note"]
    assert r["scope"]["frame"] == "F-HE" and r["scope"]["reach"] == "single"


def test_findings_verdict_and_hygiene():
    """the verdict is NEGATIVE, creates no law, keeps 0 of 19; the findings carry the answer, the predictions, the checks and the
    scope; the owner's private term and vendor words are absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1520" and v["verdict"] == "NEGATIVE" and v["creates_law"] is False and v["identifications"] == []
    assert v["prior_work"]["standing"] == "RE-DERIVED" and "b1520-tmp" not in v["prior_work"]["repo"]["heads"]
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**Verdict: NEGATIVE — outcome A, the registered kill.**", "## Seen first (the repo sweep and the literature)",
                   "| generic: (q, μ) = (2, 3), (1/3, −2) | id, s, D.θ, D.sθ | 4 | **none** | D.θ, D.sθ |",
                   "**All 224 decisions are as sealed.**", "**All 48 cases are as Lemma Tw says.**",
                   "| P5 | outcome A with witness D.θ, banked NEGATIVE | 93% | **YES** (D.θ and D.sθ) |",
                   "**The routes agree on all 32 decisions.**", "**Standing: RE-DERIVED.**", "**creates_law is false**",
                   "`dda82524`", "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    vendor = re.compile(r"\b(" + "|".join(__import__("base64").b64decode(b).decode() for b in
                                         (b"Y2xhdWRl", b"YW50aHJvcGlj", b"b3B1cw==", b"c29ubmV0", b"ZmFibGU=")) + r")\b", re.I)
    for path in list(ARC.glob("*.md")) + list(VER.glob("*.py")) + [ARC / "arc_verdict.json"]:
        text = path.read_text(encoding="utf-8")
        assert term not in text.lower(), path
        assert not vendor.search(text), path
