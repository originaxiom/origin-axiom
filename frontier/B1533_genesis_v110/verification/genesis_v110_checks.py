#!/usr/bin/env python3
"""B1533 -- GENESIS v1.10: the checks run before GENESIS.md is written (sm:B1533; not sealed: each check reads a banked
record, re-derives a fact a record states, or compares texts).

C1  The received texts. Main's v1.9 is main's v1.8 plus exactly the changes main's B1466 lists (main's own amend.py, run on
    main's v1.8, gives main's v1.9 byte for byte); main's v1.8 is main's v1.7 with its version line and one log entry and
    nothing else; each received copy is main's blob (when main's commits are in the clone); the relay asks "Please take v1.9
    as head".
C2  The SM seat's v1.8 lines. sm:B1528's changes, re-applied to main's v1.7, give the seat's v1.8 byte for byte; each of its
    three content changes finds its anchor exactly once in main's v1.9; main's v1.9 has none of their sentences.
C3  The record's Chern-Weil row is B1420's A4 (main): the Dirac index on a closed spin 4-manifold, rank-blind, with the second
    edge stated there (the non-zero values on non-split modules are flat data, counts of twisted classes); it is the only
    verdict row on main naming Chern-Weil; sm:B1531 section 3 scoped GAP6's sentence the same way before main wrote it.
C4  Own code, two routes (sm:B1532's sealed libraries over sm:B1515's routes T and L, read here, nothing edited): on M4 at
    sm:B1515's member nu = (1/3, 0), lam = 1, the non-split W1, its dual and the split V (+) L are representations of the
    level's group (relators checked), of rank five, each with h^1 = 2, and B1297's class index counts +1, -1 and 0 in both
    routes; sm:B1515's banked census row for the member agrees (I(W1) = 1, I(W2) = -1, at both of its primes).
C5  The frames with curvature or a singular point that GENESIS v1.10 names, as banked: sm:B1397 (flux caps), sm:B1502 (no
    rational flux at the cone point), sm:B1503 (positive scalar curvature, the apex index zero), sm:B1351 and sm:B1392 (the
    closed and sealed counts); sm:B1531's reading puts B1397 and B1503 among the negatives of none of the three kinds; GENESIS
    v1.9's GAP3 lets an end flux pay the balance (R41, R80).
C6  Lead L244 (a) on the chirality chain: sm:B1531's reading of the 26 records, recounted from its record: symmetry 8,
    flatness 3, non-uniqueness 3, none 12, nine of the twelve frame arithmetic; main's L244 (a) says a fourth kind refutes
    the taxonomy.
C7  Main's B1465 (read, not re-derived): its four run logs sum to 7 364 rows with 0 non-zero, as its FINDINGS and relay
    state; main's B1465 states the twisted identity as iota~*V ~ V* (x) eps (x) lam^2; main's B1466 table counts -1, +1 and
    0 on the two orders and their sum.
C8  (after writing) GENESIS.md is merge_genesis_v110.py's output byte for byte, with four [v1.10] and four [v1.8] marks;
    undoing the changes gives main's v1.9 exactly; the fork table's statuses are main's v1.9's.
    Before GENESIS.md is written C8 reports "not yet written" and passes (the pre-write log).
Writes genesis_v110_checks.json; prints one line per check. Usage: python3 genesis_v110_checks.py"""
import difflib
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
REC = ARC / "received"
V19M, V18M, V18S = REC / "GENESIS_v1_9_main.md", REC / "GENESIS_v1_8_main.md", REC / "GENESIS_v1_8_sm.md"
RELAY_IN = REC / "CC_TO_SM_AND_CODEX_2026-10-03_THE_COUNT_IS_A_BIT_AND_THE_MIXING_QUARTIC.md"
V17M = ROOT / "frontier" / "B1528_genesis_v18" / "received" / "GENESIS_v1_7_main.md"
SHA = {"v1.9 main": "7eb2df0fee9e32c638b6c872bb4ec07a1f8b93d96c3038153d75508752b5eca2",
       "v1.8 main": "2d652d30c1cb68332d4d8c4c8cd87eba7e3206cb1e4d0e6b815472f7ae02e152",
       "v1.8 sm": "b433054459fe86434c24dffd3745e4d41806e5cadaf910bb83e1c4d207e32423",
       "v1.7 main": "8b8ec814df3ae205a08fe5a7d263aacceb114982335e86518fb7cc19a9948e16",
       "relay": "449d822d60732382b716a5691908dded99050e9173c67a0aa2fb29d70fcb4d6f"}
MAIN_V19, MAIN_V18, SM_V18 = "3f8dc11a", "d2a95da4", "84892ba0"      # main's B1466, main's B1463, sm:B1528's bank
B1466 = "frontier/B1466_the_two_orders_and_the_register_bit"
B1465 = "frontier/B1465_the_mirror_broken_states_at_their_complete_points"
NOT_IN_CLONE = "not checkable: not in this clone"
OUT = {}


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _norm(text):
    return " ".join(text.split())


def git_show(ref_path, binary=False):
    """a blob from a commit of the clone, or None when the commit is not in it"""
    r = subprocess.run(["git", "show", ref_path], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout if binary else r.stdout.decode("utf-8")


def merge():
    return _load("b1533_merge_genesis_v110", HERE / "merge_genesis_v110.py")


# ================================================================================================= C1
def c1():
    for key, p in (("v1.9 main", V19M), ("v1.8 main", V18M), ("v1.8 sm", V18S), ("v1.7 main", V17M), ("relay", RELAY_IN)):
        assert _sha(p) == SHA[key], key
    rec = {"sha-256 of the received texts": SHA}
    blobs = {"v1.9 main": (MAIN_V19 + ":GENESIS.md", V19M), "v1.8 main": (MAIN_V18 + ":GENESIS.md", V18M),
             "v1.8 sm": (SM_V18 + ":GENESIS.md", V18S),
             "relay": (MAIN_V19 + ":docs/handoffs/" + RELAY_IN.name, RELAY_IN)}
    rec["received copy == the blob"] = {}
    for key, (ref, p) in blobs.items():
        b = git_show(ref, binary=True)
        rec["received copy == the blob"][key] = NOT_IN_CLONE if b is None else (b == p.read_bytes())
        assert b is None or b == p.read_bytes(), key
    # main's v1.8 against main's v1.7: the version line and one log entry
    a, b = V17M.read_text(encoding="utf-8").splitlines(), V18M.read_text(encoding="utf-8").splitlines()
    ops = [op for op in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if op[0] != "equal"]
    assert len(ops) == 2, ops
    (t1, i1, i2, j1, j2), (t2, k1, k2, l1, l2) = ops
    assert t1 == "replace" and (i2 - i1, j2 - j1) == (1, 1) and a[i1].startswith("**Version 1.7 ·") and b[j1].startswith("**Version 1.8 ·")
    assert a[i1][len("**Version 1.7"):] == b[j1][len("**Version 1.8"):]
    assert t2 == "insert" and b[l1].startswith("- **v1.8 · 2026-10-03 · main B1463.**") and k1 == len(a)
    rec["main's v1.8 against v1.7"] = {"version line": 1, "log lines added at the end": l2 - l1, "other changes": 0}
    # main's amend.py (B1466) on main's v1.8
    src = git_show(MAIN_V19 + ":" + B1466 + "/adoption/amend.py")
    if src is None:
        rec["main's amend.py on main's v1.8 gives main's v1.9"] = NOT_IN_CLONE
    else:
        ns = {"__file__": str(HERE / "amend.py")}            # main's module computes paths from __file__; build() is not called
        exec(compile(src.split("\ndef build(")[0], "amend.py", "exec"), ns)
        assert ns["SHA_V1_8"] == SHA["v1.8 main"]
        t = V18M.read_text(encoding="utf-8")
        for old, new in ns["CHANGES"]:
            assert t.count(old) == 1
            t = t.replace(old, new)
        same = t == V19M.read_text(encoding="utf-8")
        assert same
        rec["main's amend.py on main's v1.8 gives main's v1.9"] = same
        rec["main's B1466 changes"] = len(ns["CHANGES"])
    relay = RELAY_IN.read_text(encoding="utf-8")
    assert "Please take v1.9 as head." in relay and "GENESIS v1.9" in relay
    rec["the relay asks"] = "Please take v1.9 as head."
    OUT["C1"] = rec
    compared = sum(v is True for v in rec["received copy == the blob"].values())
    amended = rec["main's amend.py on main's v1.8 gives main's v1.9"]
    print(f"C1 PASS: the received texts are main's ({compared} blobs compared); main's v1.8 = v1.7 + version line + "
          f"{l2 - l1} log lines; main's amend.py on v1.8 gives v1.9: {amended}")


# ================================================================================================= C2
def c2():
    m18 = _load("b1528_merge_genesis_v18_c2", ROOT / "frontier" / "B1528_genesis_v18" / "verification" / "merge_genesis_v18.py")
    built = m18.build()
    same = built == V18S.read_text(encoding="utf-8")
    assert same
    v19 = V19M.read_text(encoding="utf-8")
    m = merge()
    anchors = [v19.count(old) for old, _ in m.V18_CONTENT]
    assert anchors == [1, 1, 1], anchors
    assert [o for o, _ in m.V18_CONTENT] == [o for o, _ in m18.CHANGES[2:5]]
    absent = []
    for old, new in m18.CHANGES[2:5]:
        i = 0
        while i < min(len(old), len(new)) and old[i] == new[i]:
            i += 1
        j = 0
        while j < min(len(old), len(new)) - i and old[-1 - j] == new[-1 - j]:
            j += 1
        added = new[i:len(new) - j]                       # what the change inserts, between the common prefix and suffix
        assert len(_norm(added)) > 60
        absent.append(_norm(added)[:60] not in _norm(v19) and _norm(added)[-60:] not in _norm(v19))
    assert all(absent)
    OUT["C2"] = {"sm:B1528's changes on main's v1.7 == the seat's v1.8, byte for byte": same,
                 "content changes carried": 3, "anchors found once in main's v1.9": anchors,
                 "their sentences absent from main's v1.9": absent}
    print("C2 PASS: sm:B1528's changes rebuild the seat's v1.8 byte for byte; its three content changes land once each in "
          "main's v1.9, which carries none of them")


# ================================================================================================= C3
def c3():
    rec = {}
    v19 = V19M.read_text(encoding="utf-8")
    assert _norm("no index built on it can tell 27 from 27̄ (Chern–Weil; the record's Chern–Weil row)") in _norm(v19)
    f = git_show(MAIN_V19 + ":frontier/B1420_the_referees_upgrades/FINDINGS.md")
    if f is None:
        rec["B1420 A4"] = NOT_IN_CLONE
    else:
        fn = _norm(f)
        for s in ("Chern–Weil: a flat bundle has zero curvature ⇒ rational Chern classes vanish ⇒ `ch(V) = rk(V)`",
                  "`ind D_V = rk(V)·(−σ/8)` on a closed spin 4-manifold: **rank-blind**",
                  "the non-zero values on reducible non-split modules are flat data too, so they are not four-dimensional "
                  "Dirac indices either; they are counts of twisted classes"):
            assert _norm(s) in fn, s[:50]
        rec["B1420 A4"] = {"closed spin 4-manifold, rank-blind": True, "the second edge stated": True}
        ledger = git_show(MAIN_V19 + ":docs/views/VERDICT_LEDGER.md")
        rows = [l for l in ledger.splitlines() if l.startswith("| `B") and re.search(r"(?i)chern.weil", l)]
        assert [l.split("|")[1].strip() for l in rows] == ["`B1420`"], rows
        assert "the flat-bundle twisted Dirac index is rank-blind by Chern-Weil + Atiyah-Singer" in rows[0]
        rec["verdict rows on main naming Chern-Weil"] = ["B1420"]
    s = _norm((ROOT / "frontier" / "B1531_the_symmetric_phase" / "FINDINGS.md").read_text(encoding="utf-8"))
    for t in ("Chat 1's Chern–Weil sentence holds where the count is a Fredholm index on a closed or sealed problem (B1351, "
              "B1392), or where there is no flux (B1502).",
              "Non-semisimple flat V against V* evades it"):
        assert _norm(t) in s, t[:40]
    rec["sm:B1531 section 3 scoped it first"] = True
    OUT["C3"] = rec
    print("C3 PASS: the record's Chern-Weil row is B1420's A4 (the Dirac index on a closed spin 4-manifold, rank-blind; the "
          "second edge stated there); the only such verdict row on main; sm:B1531 scoped the sentence the same way")


# ================================================================================================= C4
def c4():
    ver = ROOT / "frontier" / "B1532_three_from_the_cusps" / "verification"
    sys.path.insert(0, str(ver))
    CT = _load("b1532_cover_lib_t", ver / "cover_lib_t.py")
    CL = _load("b1532_cover_lib_l", ver / "cover_lib_l.py")
    b1515 = ROOT / "frontier" / "B1515_the_hyperbolic_point" / "verification"
    rec_t = json.loads((b1515 / "census_t_run.txt").read_text(encoding="utf-8"))
    rec_l = json.loads((b1515 / "census_l_run.txt").read_text(encoding="utf-8"))
    pT, pL = rec_t["primes"]["M4"][0], rec_l["primes"]["M4"][0]
    out = {"level": "M4", "member": "nu = (1/3, 0), lam = 1", "primes": {"T": pT, "L": pL}}
    # route T
    LT = CT.LevelT(4, pT)
    ab = next(a for a in LT.chars if LT.label(a) == "1/3,0")
    m = CT.MemberT(LT, ab)
    assert m.kind == "one"
    W = m.W1(m.c_one)
    mods = {"W1": W, "W1*": W.dual(), "V (+) L": m.W1(m.c_one * LT.dom.convert(0))}
    rows_t = {}
    for name, rep in mods.items():
        assert rep.check(LT.rels), name
        d = LT.ix(rep)
        d2 = LT.ix(CT.T.wedge2_rep(rep))
        rows_t[name] = {"rank": rep.d, "relators hold": True, "h1": d["a1"], "I": d["I"], "I(Lambda^2)": d2["I"],
                        "B1297 data [I, a0, a1, t0, r1, b0, b1, s0, q1]": CT.compact(d)}
    # route L
    LL = CL.LevelL(4, pL)
    abl = next(a for a in LL.chars if LL.label(a) == "1/3,0")
    ml = CL.MemberL(LL, abl)
    assert ml.kind == "one"
    Wl = ml.W1(ml.c_one)
    mods_l = {"W1": Wl, "W1*": Wl.dual(), "V (+) L": ml.W1(LL.F.smul(0, ml.c_one))}
    rows_l = {}
    for name, rep in mods_l.items():
        assert rep.holds(), name
        ix = CL.RL.index(rep)
        ix2 = CL.RL.index(rep.wedge2())
        rows_l[name] = {"rank": rep.d, "relators hold": True, "h1": ix["E"]["h1"], "I": ix["I"], "I(Lambda^2)": ix2["I"],
                        "route L data [I, a0, h1, t0, n, b0, h1*, s0, n*]": CL.lsig(ix)}
    for rows in (rows_t, rows_l):
        assert [rows[k]["I"] for k in ("W1", "W1*", "V (+) L")] == [1, -1, 0], rows
        assert all(rows[k]["rank"] == 5 and rows[k]["h1"] == 2 for k in rows)
    # the banked census row of the member (both of sm:B1515's primes for M4, route T)
    banked = []
    for a in rec_t["A"]:
        if a["level"] == 4 and a["lam"] == "1" and a["char"] == ["1/3", "0"]:
            banked.append({"field": a["field"], "I(W1)": a["row"]["W1"]["c1"]["W1"]["I"], "I(W2)": a["row"]["W2"]["c1"]["I(W2)"]})
    assert len(banked) == 2 and all(b["I(W1)"] == 1 and b["I(W2)"] == -1 for b in banked), banked
    out.update({"route T": rows_t, "route L": rows_l, "sm:B1515's banked rows (route T)": banked,
                "reading": "three flat modules of rank five (one Chern character, ch = rk by Chern-Weil), h^1 = 2 each; "
                           "the class index counts +1, -1, 0"})
    OUT["C4"] = out
    print(f"C4 PASS: on M4 at nu = (1/3, 0) the non-split W1, its dual and V (+) L are flat of rank 5 with h^1 = 2 each and "
          f"count +1, -1, 0 in route T (GF({pT})) and route L (GF({pL})); sm:B1515's banked rows agree")


# ================================================================================================= C5
def c5():
    def verdict(arc):
        d = next(ROOT.glob(f"frontier/{arc}_*"))
        return json.loads((d / "arc_verdict.json").read_text(encoding="utf-8")), d
    v97, _ = verdict("B1397")
    assert v97["verdict"] == "NEGATIVE" and "U(1) flux F of degree n" in v97["claim_one_line"]
    assert "net chirality" in v97["claim_one_line"]
    v02, _ = verdict("B1502")
    assert v02["verdict"] == "PROVED" and "no C-field U(1) and no rational flux at the apex" in v02["claim_one_line"]
    v03, d03 = verdict("B1503")
    assert v03["verdict"] == "PROVED"
    f03 = _norm((d03 / "FINDINGS.md").read_text(encoding="utf-8"))
    assert "positive scalar curvature" in f03 and "(Lichnerowicz)" in f03
    v51, _ = verdict("B1351")
    v92, _ = verdict("B1392")
    assert v51["verdict"] == "PROVED" and v92["verdict"] == "PROVED"
    j = json.loads((ROOT / "frontier" / "B1531_the_symmetric_phase" / "verification" / "symmetric_phase_checks.json")
                   .read_text(encoding="utf-8"))
    curv = j["C2b"]["none of the three, carrying curvature"]
    assert curv == ["B1397", "B1503"]
    v19 = _norm(V19M.read_text(encoding="utf-8"))
    assert "the balance may be paid by flux through an end (R41, R80)" in v19
    OUT["C5"] = {"sm:B1397": v97["verdict"], "sm:B1502": v02["verdict"], "sm:B1503": v03["verdict"],
                 "sm:B1351": v51["verdict"], "sm:B1392": v92["verdict"],
                 "sm:B1531: none of the three kinds, carrying curvature": curv,
                 "GENESIS v1.9 GAP3: an end flux may pay the balance (R41, R80)": True}
    print("C5 PASS: sm:B1397 (flux caps), sm:B1502 (no rational flux at the apex), sm:B1503 (positive scalar curvature), "
          "sm:B1351 and sm:B1392 banked as cited; sm:B1531 puts B1397 and B1503 in none of the three kinds; GAP3's end flux")


# ================================================================================================= C6
def c6():
    j = json.loads((ROOT / "frontier" / "B1531_the_symmetric_phase" / "verification" / "symmetric_phase_checks.json")
                   .read_text(encoding="utf-8"))
    reading = j["C2b"]["reading"]
    assert len(reading) == 26
    tally = {}
    for r in reading.values():
        tally[r["kind"]] = tally.get(r["kind"], 0) + 1
    assert tally == {"S": 8, "F": 3, "U": 3, "none": 12} and tally == j["C2b"]["tally"]
    fa = sum(1 for r in reading.values() if r["kind"] == "none" and r["family"] == "frame-arithmetic")
    assert fa == 9
    rec = {"records": 26, "tally": tally, "frame arithmetic among the twelve": fa}
    leads = git_show(MAIN_V19 + ":docs/OPEN_LEADS.md")
    if leads is None:
        rec["main's L244 (a)"] = NOT_IN_CLONE
    else:
        assert "A fourth kind refutes the taxonomy" in _norm(leads)
        rec["main's L244 (a)"] = "a fourth kind refutes the taxonomy"
    OUT["C6"] = rec
    print("C6 PASS: sm:B1531's 26 records recounted: symmetry 8, flatness 3, non-uniqueness 3, none 12 (nine frame "
          "arithmetic); main's L244 (a): a fourth kind refutes the taxonomy")


# ================================================================================================= C7
def c7():
    rec = {}
    total, nonzero, per = 0, 0, {}
    for st in ("+LLRLRR", "-LLRLRR", "+LLLRLRR", "-LLLRLRR"):
        t = git_show(MAIN_V19 + ":" + B1465 + f"/verification/run_{st}.txt")
        if t is None:
            rec["B1465 run logs"] = NOT_IN_CLONE
            break
        last = t.strip().splitlines()[-1]
        mm = re.fullmatch(r"rows (\d+) nonzero (\d+)", last.strip())
        assert mm, last
        per[st] = int(mm.group(1))
        total += int(mm.group(1))
        nonzero += int(mm.group(2))
    else:
        assert total == 7364 and nonzero == 0
        f = _norm(git_show(MAIN_V19 + ":" + B1465 + "/FINDINGS.md"))
        assert "7 364 indices, all zero, no instrument error." in f
        assert _norm("a twist of the meridian by λ turns the identity into ι̃*V ≅ V* ⊗ ε ⊗ λ²") in f
        rec.update({"rows per state": per, "rows": total, "non-zero": nonzero,
                    "the twisted identity, in main's words": "iota~*V ~ V* (x) eps (x) lam^2"})
    f66 = git_show(MAIN_V19 + ":" + B1466 + "/FINDINGS.md")
    if f66 is None:
        rec["B1466 table"] = NOT_IN_CLONE
    else:
        row = next(l for l in f66.splitlines() if l.startswith("| q₀ = 17 + 12√2, μ = −1 |"))
        cells = [c.strip() for c in row.split("|")[1:-1]]
        assert cells[1].startswith("**−1**") and cells[2].startswith("**+1**") and cells[3] == "0", cells
        rec["B1466 at q0 = 17 + 12 sqrt2: I(W), I(W'), I(A (+) 1)"] = [-1, 1, 0]
    OUT["C7"] = rec
    print(f"C7 PASS: main's B1465 run logs: {total} rows, {nonzero} non-zero; its twisted identity read; main's B1466 counts "
          f"-1, +1, 0 on the two orders and their sum")


# ================================================================================================= C8
def c8():
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.10 ·" not in g:
        OUT["C8"] = {"GENESIS.md": "not yet written (v1.10 absent)"}
        print("C8 PASS: GENESIS.md not yet written (the pre-write run)")
        return
    m = merge()
    built = m.build()
    assert g == built, "GENESIS.md differs from the generator's output"
    marks10, marks8 = g.count("**[v1.10]**"), g.count("**[v1.8]**")
    assert (marks10, marks8) == (4, 4), (marks10, marks8)
    back = g
    for old, new in reversed(m.CHANGES):
        assert back.count(new) == 1, new[:60]
        back = back.replace(new, old)
    v19 = V19M.read_text(encoding="utf-8")
    assert back == v19

    def statuses(text):
        return [l.split("|")[1:4] for l in text.splitlines() if re.match(r"\| FK\d+", l)]
    st = statuses(g)
    assert [r[0] for r in st] == [r[0] for r in statuses(v19)] and [r[2] for r in st] == [r[2] for r in statuses(v19)]
    assert len(st) == 12
    OUT["C8"] = {"GENESIS.md == merge_genesis_v110.build()": True, "[v1.10] marks": marks10, "[v1.8] marks": marks8,
                 "undoing the changes gives main's v1.9": True, "fork statuses as in main's v1.9": True,
                 "sha-256": hashlib.sha256(g.encode("utf-8")).hexdigest()}
    print(f"C8 PASS: GENESIS.md is the generator's output byte for byte ({marks10} [v1.10] and {marks8} [v1.8] marks); "
          f"undoing the {len(m.CHANGES)} changes gives main's v1.9; the fork statuses are main's")


def main():
    c1()
    c2()
    c3()
    c4()
    c5()
    c6()
    c7()
    c8()
    (HERE / "genesis_v110_checks.json").write_text(json.dumps(OUT, indent=1, default=str, ensure_ascii=False) + "\n",
                                                   encoding="utf-8")
    print("ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
