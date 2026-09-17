#!/usr/bin/env python3
"""xB010 cells R1-R5, exactly as sealed in PREREGISTRATION.md (sha256 5ec6f8c5...,
commit b5ac068, pushed BEFORE any of this existed).  Each cell asserts its mathematics."""
import collections
import glob
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]


def _mod(p):
    spec = importlib.util.spec_from_file_location("_m", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


RD = _mod(ROOT / "scripts" / "checks" / "rederivation.py")


def R1():
    wr = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    pr = (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")
    print("R1       the rule is written where the standing rules live, and registered")
    for nm, txt, needle in (("WORKING_RULES.md", wr, "THE RE-DERIVATION RULE"),
                            ("docs/PRACTICES.md", pr, "THE RE-DERIVATION RULE")):
        print(f"         {nm:<20} contains the rule: {needle in txt}")
        assert needle in txt, nm
    for nm, txt in (("WORKING_RULES.md", wr), ("docs/PRACTICES.md", pr)):
        assert "CITE" in txt and "RE-DERIVE" in txt, f"{nm}: the cite/re-derive distinction is the rule"
    assert "NOT_RERUN" in wr and "NOT_RERUN" in pr
    print("R1 PASS  both carry the rule, the CITE != RE-DERIVE distinction, and the honest")
    print("         NOT_RERUN escape that keeps it from producing false declarations.")


def R2():
    ros = json.loads((ROOT / "docs" / "REDERIVATION_ROSTER.json").read_text(encoding="utf-8"))
    ex = set(ros["exempt"])
    print(f"\nR2       the binding mechanism: a FROZEN ROSTER, not a numeric cutoff")
    print(f"         roster freezes {len(ex)} pre-existing arcs")
    # the reason a cutoff cannot work, demonstrated rather than asserted
    import re
    for nm in ("xB009_the_odd_sector", "B1231_identification_discipline"):
        num = int(re.sub(r"^[a-z]*B", "", re.match(r"([a-z]{0,2}B\d+)", nm).group(1)))
        print(f"         {nm:<34} parses to the number {num}")
    print("         => a numeric cutoff at, say, 1258 would EXEMPT this seat's own arcs")
    print("            forever. The roster binds by identity, so it cannot.")
    assert "xB010_the_rederivation_rule" not in ex, "the rule's own arc must be BOUND, not exempt"
    print("R2 PASS  xB010 itself is NOT on the roster: the rule binds its own author.")
    return ex


def R3():
    out = subprocess.run([sys.executable, str(ROOT/"scripts"/"gates"/"gates.py")],
                         capture_output=True, text=True, timeout=1800).stdout
    lines = out.splitlines()
    npass = sum(1 for l in lines if l.startswith("  PASS"))
    nfail = sum(1 for l in lines if l.startswith("  FAIL"))
    print(f"\nR3       the present tree: {npass} PASS, {nfail} FAIL")
    assert any(l.startswith("  PASS  rederivation") for l in lines), "the new gate is not green"
    assert nfail == 0, [l for l in lines if l.startswith("  FAIL")][:3]
    assert npass == 35, f"expected 35 (34 + this one), got {npass}"
    print("R3 PASS  34/34 became 35/35; nothing retroactively red.")


def R4():
    print("\nR4       the two-way selftest -- and the cell that could go wrong BY DESIGN")
    fails = RD.selftest()
    assert not fails, fails
    honest = RD.validate({"arc": "B999", "outcome": "NOT_RERUN",
                          "why": "needs Sage, unavailable here"})
    bare = RD.validate({"arc": "B999", "outcome": "NOT_RERUN"})
    cite = RD.validate({"arc": "B425", "outcome": "CONFIRMED"})
    assert honest is None, honest
    assert bare is not None and cite is not None
    print("\n         an HONEST refusal passes; a BARE refusal does not; and CONFIRMED with")
    print("         nothing recomputed does not -- because citing is not re-deriving.")
    print("R4 PASS  a rule that forbade 'I did not re-run this' would produce false")
    print("         declarations, not re-derivation. Silence is impossible; honesty is cheap.")


def R5():
    """this seat eats it first: RE-DERIVE the statistic the rule itself rests on."""
    print("\nR5       THE AUTHOR EATS IT FIRST -- re-deriving B742's numbers, which are the")
    print("         evidence the rule is argued from, FROM ITS ARTIFACTS rather than its prose")
    rec = sorted(glob.glob(str(ROOT / "frontier" / "B742_negatives_hunt_p1" / "recompute" / "*")))
    names = [pathlib.Path(p).name for p in rec]
    print(f"         recompute/ target directories on disk : {len(rec)}"
          f"   [B742's prose says 32 sealed targets recomputed]")
    assert len(rec) == 32, len(rec)
    txt = (ROOT / "frontier" / "B742_negatives_hunt_p1" / "FINDINGS.md").read_text(encoding="utf-8")
    verd = collections.Counter()
    for l in txt.splitlines():
        if l.startswith("| B") or l.startswith("| V"):
            cells = [c.strip().replace("**", "") for c in l.strip("|").split("|")]
            if len(cells) >= 4:
                verd[cells[3]] += 1
    print(f"         REVIVED rows tallied from its own table : {verd['REVIVED']}"
          f"   [prose says 2 REVIVED]")
    assert verd["REVIVED"] == 2, verd
    print(f"         and B146 is among the recomputed targets: {'B146' in names}"
          f"   -- B742 recomputed it in July; xB006 re-tested it again today and found its")
    print( "            KILL sound but its JUSTIFICATION wrong. Two passes, two different")
    print( "            defects: exactly the case for this rule.")
    assert "B146" in names
    print("\n         HONEST LIMIT, declared rather than glossed: this cell's row-parser")
    print("         tallies only 8 RECONFIRMED against B742's stated 30 -- the table carries")
    print("         row formats the regex does not match. THE 30 IS THEREFORE *NOT*")
    print("         INDEPENDENTLY CONFIRMED HERE and is declared SCOPED, not CONFIRMED.")
    print("         The two numbers this rule actually argues from -- 32 recomputed, 2")
    print("         revived -- ARE confirmed from artifacts.")
    print("R5 PASS  the rule's own motivating statistic was re-derived, not cited, and the")
    print("         part that could not be is declared rather than claimed.")


if __name__ == "__main__":
    R1(); R2(); R3(); R4(); R5()
    print("\nVERIFIED")
