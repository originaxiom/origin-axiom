"""B1519 lock -- GENESIS v1.2 (2026-10-02): main's v1.1 as the head, this seat's v1.1 folded in, the signed powers placed, the bar
at GAP4, the observer line carried and registered (FK12), and the two seen-first rules made one.

Locks the arc's own checks (the record, and K1 and K3 live: every integer square root of L^a R^b by Cayley-Hamilton, and the swap's
action on LR), GENESIS v1.2 (main's v1.1 as the head, this seat's v1.1 and B1519's additions marked [v1.2], the observer line and
FK12, no status changed), the seen-first gate on this branch with planted controls, the arc's FINDINGS (a "Seen first" section in
main's form, the topic sweep's verdict, the price, no private term) and the ledger rows.
"""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1519_genesis_v12"
VER = ARC / "verification"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _norm(p):
    return " ".join(re.sub(r"[*`>]", "", p.read_text(encoding="utf-8")).split())


K = _load("b1519_genesis_v12_checks", VER / "genesis_v12_checks.py")


# ------------------------------------------------------------------------------------------------- the record
def test_record_all_passed():
    r = json.loads((VER / "genesis_v12_checks.json").read_text(encoding="utf-8"))
    assert r["all passed"] and len([v for v in r.values() if isinstance(v, dict)]) == 7
    k4 = r["K4 B1234's base rate, named"]
    assert k4["amphichiral among them"] == ["m003", "m004", "m135", "m136", "m206", "m207"]
    assert k4["population: first and last names, size"] == ["m003", "m261", 200] and k4["of them amphichiral"] == 40
    k5 = r["K5 R78 at -(LR)^2"]
    assert "m207(0,0)" in k5["bundles"]["-(LR)^2"]["identify"] and k5["bundles"]["-(LR)^2"]["H1"] == "Z/3 + Z/3 + Z"
    assert k5["b+-LRLR is isometric to m207"] and k5["-(LR)^2: H1 torsion"] == [3, 3]
    assert k5["levels with trace -7 (state, n, H1 torsion)"] == [{"state": "-LLLLLR", "n": 1, "H1 torsion": [9]}]
    assert len(k5["C9 box: matrices reducing to -u^k with k even"]) == 4
    k6 = r["K6 surjections onto 2T (main v1.1, B1234)"]
    assert k6["m000: generators, relators, surjections onto SL(2, F_3)"][2] == 48
    assert k6["m004: generators, relators, surjections onto SL(2, F_3)"][2] == 48
    k7 = r["K7 three bits, one relation (main B1327)"]
    assert k7["symmetry group, order"] == ["D4", 8] and k7["isometries"] == 8 and k7["cusp maps diagonal"]
    assert k7["(s_m, s_l, det) with multiplicity"] == [[1, 1, 1, 2], [1, -1, -1, 2], [-1, 1, -1, 2], [-1, -1, 1, 2]]
    assert k7["det = s_m s_l on every isometry"]


# ------------------------------------------------------------------------------------------------- live checks
def test_k1_square_roots_live():
    out = K.k1()
    assert out["passed"] and out["roots of LR"] == [[[1, 1], [1, 0]], [[-1, -1], [-1, 0]]]


def test_k3_the_swap_is_not_reversal_live():
    out = K.k3()
    assert out["passed"] and out["P LR P^-1 = RL"] and not out["RL = (LR)^-1"] and not out["P among them"]


# ------------------------------------------------------------------------------------------------- GENESIS v1.2
def test_genesis_v12():
    """main's v1.1 is the head (its [v1.1] marks and its lines kept); this seat's v1.1 and B1519's additions are marked [v1.2]"""
    raw = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    g = " ".join(raw.split())
    assert raw.startswith("# GENESIS — the foundations of origin-axiom")
    assert "**Version 1.2 · 2026-10-02 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification" in g
    # every mark of main's v1.1 kept (21 in main's file at f655034b, 15 of them bold); v1.2's own marks as generated
    assert raw.count("[v1.1]") == 21 and raw.count("**[v1.1]**") == 15 and raw.count("**[v1.2]**") == 22
    for s in ("v1.2 (sm:B1519) takes main's v1.1 as the head, as main asked",
              "Every hyperbolic monodromy is exactly one triple (u, k, ε) ↦ εA(u)ᵏ",
              "(Salepci, arXiv:1006.0752, §7)",
              "The first is **m207 = −(LR)²**, H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/3",
              "sm:B1385 §2 S4 (±(LR)², ±(LR)³, ±(LR)⁴), main B1418's class census and B1224's CS census",
              'B979\'s record says LR and RL are conjugate "via P"',
              "On the words route the swap is native",
              "The 6 of 200 are m003, m004, m135, m136, m206 and m207",
              "The null model and the grading are fixed: `docs/THE_BAR.md` (sm:B1518)",
              "**The gaps and the observer.**",
              "\"a fully transparent, self-naming, integrated speaker that cannot choose\" (B759–B762)",
              "It names itself and cannot sign itself, and the missing sign is one ℤ/2 class, the orientation (B1183 and B1184, PROVED",
              "Main's B1327 (OPEN) proposes re-typing most closings as relations",
              "| FK12 **[v1.2]** | The observer: are its closings part of the genesis, or inputs beyond it?",
              "Within the object the sign is settled: the object cannot sign itself (B760, NEGATIVE; B1183, B1184, PROVED)",
              "the trace map conserves κ = tr[a, b] and never reads it (B20, B37)",
              "main's B1327 (OPEN) reads s_m as the arrow and s_l as the swap, so the mirror is the swap times the arrow",
              "main's B1455 (sealed 2026-10-02, not yet run) tests whether each vacuum of the bridge's harmonic family on m004",
              "graded by `docs/THE_BAR.md` (**[v1.2]** sm:B1518; GAP4)",
              "- **v1.1 on the SM seat's branch · 2026-10-02 · sm:B1517.**",
              "- **v1.2 · 2026-10-02 · sm:B1519.** Main's v1.1 taken as the head, as main asked; every one of its 23 changes accepted.",
              # main's v1.1 kept
              "| F-MC **[v1.1]** | McKay cascade frame |",
              '*"The root has none and cannot: its fibre has no finite character."* (main B1434)',
              "- **v1.1 · 2026-10-02 · main B1454.** Verified and adopted on main."):
        assert " ".join(s.split()) in g, s
    # no status changed: the status cells of the IDs v1.2 touches are as in v1.1
    for row in ("| GM5c | The record swap P is a legal move | OPEN |", "| SE2 | **Orientation**", "| FK2 | Orientation (SE2) | CHOSEN |",
                "| FK3 | The swap P: legal move, and of what type | OPEN |", "| FK6 | Positivity (GM5d) | CHOSEN |",
                "| FK9 | Selection: what makes a state physical | OPEN |"):
        assert row in raw, row


# ------------------------------------------------------------------------------------------------- the seen-first gate
def test_seen_first_gate_on_this_branch(tmp_path):
    G = _load("b1519_gates", ROOT / "scripts" / "gates" / "gates.py")
    assert G.SEEN_FIRST_FROM == 1519 and "seen-first" in G.GATES
    assert G.seen_first_missing() == []
    ok, detail = G.gate_seen_first()
    assert ok, detail
    # planted controls: an arc without the section, one without the literature, and one in form
    for name, body in (("B1600_x", "# x\n\n## 1. Body\n\ntext\n"),
                       ("B1601_y", "# y\n\n## Seen first\n\nThe sweep found nothing.\n\n## 1. Body\n"),
                       ("B1602_z", "# z\n\n## Seen first\n\nThe repo sweep and the literature: nothing found.\n\n## 1. Body\n"),
                       ("B1518_w", "# w\n\nbefore the rule\n")):
        d = tmp_path / "frontier" / name
        d.mkdir(parents=True)
        (d / "FINDINGS.md").write_text(body, encoding="utf-8")
    bad = G.seen_first_missing(root=tmp_path)
    assert bad == ["B1600_x (no 'Seen first' section)", "B1601_y (the literature is not addressed)"], bad


# ------------------------------------------------------------------------------------------------- the arc's text
def test_findings():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert f.startswith("# B1519 — GENESIS v1.2: MAIN'S v1.1 AS THE HEAD")
    sec = re.search(r"(?ms)^##[^\n]*Seen first[^\n]*\n(.*?)(?=^## |\Z)", f)
    assert sec and "sweep" in sec.group(1).lower() and "literature" in sec.group(1).lower()
    t = _norm(ARC / "FINDINGS.md")
    for s in ("0 of 19", "Standing: RE-DERIVED", "m207 = −(LR)²", "B1385 §2 S4", "EARLY_RECORD_INDEX", "arXiv:2307.13873v7",
              "No status of GENESIS changes", "All 23 of its changes are accepted", "registers FK12",
              "109 of 1327 arcs on main match (NEGATIVE 18, OPEN 17, PROVED 74)", "107 of the 109 are on this branch",
              "the object says WHO it is, never WHICH WAY it is", "All seven pass."):
        assert s in t, s
    private = bytes([98, 114, 97, 118, 101]).decode()
    for p in (ARC / "FINDINGS.md", ARC / "arc_verdict.json", ROOT / "GENESIS.md", ROOT / "WORKING_RULES.md"):
        assert private not in p.read_text(encoding="utf-8").lower(), p.name


def test_verdict_and_ledgers():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1519" and d["verdict"] == "PROVED" and d["scope"]["frame"] == "none"
    assert d["prior_work"]["standing"] == "RE-DERIVED"
    err = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "| E54 instance (2026-10-02, B1517 and its GENESIS v1.1 §3)" in err and "GENESIS v1.0's quotation of B1434" in err
    assert "| E54 instance (2026-10-02, B1519's draft and the reply to the owner)" in err
    rules = _norm(ROOT / "WORKING_RULES.md")
    assert "the two rules of 2026-10-02 made one" in rules.lower()
