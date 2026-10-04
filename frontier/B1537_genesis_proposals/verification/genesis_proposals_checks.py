#!/usr/bin/env python3
"""B1537 checks -- main's GENESIS v1.10 taken as head; the SM seat's page changes as proposals P1-P9 to it.

  C1  received/GENESIS_v1_10_main.md is main's v1.10 as on origin/main (B1467), by sha-256 and by `git show`.
  C2  received/GENESIS_v1_10_sm.md is the SM seat's own v1.10 (sm:B1533): its generator's output, byte for byte.
  C3  main's v1.10 lacks P1-P4's content (the six-gaps heading, GAP6's scope, FK9's sm:B1527 and Part H lines, the frontier's
      item-8 line), and each of P1-P4's texts is the seat's v1.10 text with only the version mark replaced.
  C4  every proposal applies once; the proposed text is main's v1.10 plus nine marked insertions, and removing them gives
      main's v1.10 back; the marks [sm P1]-[sm P9] each occur, none twice in a heading or row they do not own.
  C5  P5-P8's facts against the banked records they cite (sm:B1530, sm:B1532, sm:B1534, sm:B1535; sm:B1536's seal row).
  C6  GENESIS.md at the repository root is main's v1.10, byte for byte (after it is written).
  C7  Gate 5-Q's three words, vendor words and the private term: absent from the proposed text and this arc's files.

    python3 genesis_proposals_checks.py --prewrite   (before GENESIS.md is written: C6 expects the seat's v1.10)
    python3 genesis_proposals_checks.py [--record]   ->  genesis_proposals_checks.json (after: C6 expects main's v1.10)"""
import base64
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import merge_proposals as MP  # noqa: E402


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def c1():
    main_txt = (ARC / "received" / "GENESIS_v1_10_main.md").read_bytes()
    git = subprocess.run(["git", "-C", str(ROOT), "show", "origin/main:GENESIS.md"], capture_output=True, check=True).stdout
    return {"sha-256": sha(main_txt), "equals origin/main's GENESIS.md": main_txt == git,
            "equals the pinned sha": sha(main_txt) == MP.SHA_MAIN_V110}


def c2():
    seat = (ARC / "received" / "GENESIS_v1_10_sm.md").read_text(encoding="utf-8")
    gen = load("b1533_merge", ROOT / "frontier" / "B1533_genesis_v110" / "verification" / "merge_genesis_v110.py")
    return {"sha-256": sha(seat.encode()), "equals sm:B1533's generator output": seat == gen.build()}


def c3():
    mn = (ARC / "received" / "GENESIS_v1_10_main.md").read_text(encoding="utf-8")
    seat = (ARC / "received" / "GENESIS_v1_10_sm.md").read_text(encoding="utf-8")
    gap6, fk9, front = MP.carried()
    out = {
        "main lacks 'Six gaps'": "**Six gaps**" not in mn and "**Five gaps**" in mn,
        "main lacks GAP6's scope": "Its scope, from the record (sm:B1531" not in mn,
        "main lacks FK9's sm:B1527 line": "Answered near the hyperbolic point (sm:B1527" not in mn,
        "main lacks FK9's Part H line": "7 364 indices, all zero" not in mn,
        "main lacks the frontier's item-8 line": "answered near the hyperbolic point in finite volume (sm:B1527)" not in mn,
        "P2 is the seat's text": gap6.replace("**[sm P2]**", "**[v1.10]**", 1) in seat,
        "P3 is the seat's text": fk9.replace("**[sm P3]**", "**[v1.8]**", 1).replace("**[sm P3]**", "**[v1.10]**", 1) in seat,
        "P4 is the seat's text": front.replace("**[sm P4]**", "**[v1.8]**", 1) in seat,
        "the seat's v1.10 heading": "**Six gaps**, none of which work on one state can close:" in seat,
    }
    return out


def c4():
    mn = (ARC / "received" / "GENESIS_v1_10_main.md").read_text(encoding="utf-8")
    prop = MP.build()
    undone = prop
    for old, new in reversed(MP.changes()):
        assert undone.count(new) == 1
        undone = undone.replace(new, old, 1)
    marks = {f"[sm P{i}]": prop.count(f"**[sm P{i}]**") for i in range(1, 10)}
    return {"proposals": len(MP.changes()), "every anchor once in main's v1.10": all(mn.count(o) == 1 for o, _ in MP.changes()),
            "undoing the proposals gives main's v1.10": undone == mn, "marks": marks,
            "each mark occurs (P3 twice: its sm:B1527 and Part H lines)":
                marks == {**{f"[sm P{i}]": 1 for i in range(1, 10)}, "[sm P3]": 2},
            "written file reproduces": (ARC / "proposed" / "GENESIS_v1_10_with_proposals.md").exists() and
                (ARC / "proposed" / "GENESIS_v1_10_with_proposals.md").read_text(encoding="utf-8") == prop}


def c5():
    fr = ROOT / "frontier"
    b1532 = json.loads((fr / "B1532_three_from_the_cusps" / "verification" / "read_out.json").read_text())
    tw = json.loads((fr / "B1532_three_from_the_cusps" / "verification" / "post_run_twists.json").read_text())
    v1532 = json.loads((fr / "B1532_three_from_the_cusps" / "arc_verdict.json").read_text())
    v1534 = json.loads((fr / "B1534_the_silver_covers" / "arc_verdict.json").read_text())
    v1530 = json.loads((fr / "B1530_the_interior_extensions" / "arc_verdict.json").read_text())
    ro1535 = json.loads((fr / "B1535_the_cap" / "verification" / "read_out.json").read_text())
    v1535 = json.loads((fr / "B1535_the_cap" / "arc_verdict.json").read_text())
    seal = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    census = {r: b1532["census"][r] for r in ("T", "L")}
    return {
        "sm:B1532 NEGATIVE": v1532["verdict"] == "NEGATIVE",
        "sm:B1532: 68,596 counts per route, none generation-shaped":
            all(c["generation-shaped"] in ([], 0) for c in census.values()) and
            "The census reads 68,596 counts in each route" in (fr / "B1532_three_from_the_cusps" / "FINDINGS.md").read_text(encoding="utf-8"),
        "sm:B1532 after the run: kappa^5 = 1 adds none": all(tw[r]["generation-shaped"] == [] for r in ("T", "L")),
        "sm:B1534 NEGATIVE": v1534["verdict"] == "NEGATIVE",
        "sm:B1530 PROVED (one generation on m135 and m136)": v1530["verdict"] == "PROVED",
        "sm:B1535 PROVED": v1535["verdict"] == "PROVED" and ro1535["predictions"]["P2 Theorem C at every reading"] and
            ro1535["predictions"]["P3 the routes agree"] and ro1535["predictions"]["P8 Lemma W census"],
        "sm:B1535: the only generation-shaped value is (-1, -1)": ro1535["generation-shaped readings"] == {"(-1, -1)": 36},
        "sm:B1536 sealed (its SEAL_LEDGER row)": "B1536 THE FINITE COVERS" in seal and
            "frontier/B1536_the_finite_covers/PREREGISTRATION.md" in seal,
    }


def c6():
    g = ROOT / "GENESIS.md"
    mn = (ARC / "received" / "GENESIS_v1_10_main.md").read_bytes()
    seat = (ARC / "received" / "GENESIS_v1_10_sm.md").read_bytes()
    cur = g.read_bytes()
    return {"GENESIS.md == main's v1.10": cur == mn, "GENESIS.md == the seat's v1.10 (before writing)": cur == seat,
            "sha-256": sha(cur)}


def c7():
    words = [base64.b64decode(x).decode() for x in ("cXVhbGlh", "YXdhcmU=", "c2Vlcw==", "Y2xhdWRl", "YW50aHJvcGlj", "b3B1cw==",
                                                     "c29ubmV0", "ZmFibGU=")]
    words.append(bytes([98, 114, 97, 118, 101]).decode())
    texts = {"proposed": MP.build()}
    for p in sorted(ARC.rglob("*")):
        if p.is_file() and p.suffix in (".md", ".py", ".json", ".txt") and "received" not in p.parts:
            texts[str(p.relative_to(ARC))] = p.read_text(encoding="utf-8", errors="ignore")
    hits = [(k, w[:2]) for k, t in texts.items() for w in words if re.search(r"\b" + re.escape(w) + r"\b", t.lower())]
    return {"files checked": len(texts), "hits": hits}


def main():
    out = {}
    checks = {"C1": c1, "C2": c2, "C3": c3, "C4": c4, "C5": c5, "C6": c6, "C7": c7}
    passed = {}
    for name, f in checks.items():
        r = f()
        out[name] = r
        if name == "C7":
            ok = r["hits"] == []
        elif name in ("C1", "C2"):
            ok = all(v for k, v in r.items() if k != "sha-256")
        elif name == "C4":
            ok = all(v for k, v in r.items() if k not in ("proposals", "marks"))
        elif name == "C6":
            if "--prewrite" in sys.argv:
                ok = r["GENESIS.md == the seat's v1.10 (before writing)"]
                print("C6 (before writing): GENESIS.md is still the seat's v1.10" if ok else "C6: unexpected GENESIS.md")
            else:
                ok = r["GENESIS.md == main's v1.10"]
        else:
            ok = all(r.values())
        passed[name] = ok
        print(f"{name} {'PASS' if ok else 'FAIL'}", flush=True)
    out["passed"] = passed
    out["all pass"] = all(passed.values())
    print(("before GENESIS.md is written: " if "--prewrite" in sys.argv else "after GENESIS.md was written: ") +
          ("ALL PASS" if out["all pass"] else "NOT ALL PASS"))
    if "--record" in sys.argv:
        (HERE / "genesis_proposals_checks.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    return out


if __name__ == "__main__":
    main()
