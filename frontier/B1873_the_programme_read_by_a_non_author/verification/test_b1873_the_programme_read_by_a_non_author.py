"""B1873 -- the recount is what the script prints, and the four repairs are in force in the programme as built.
The refusals themselves are planted and fired in B1861's own lock (test_the_joins_the_seals_rule_needs_and_each_refusal_can_fire)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = json.loads((ROOT / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
PK = {w["id"]: w for w in P["packages"]}


def _up(i, seen=None):
    seen = set() if seen is None else seen
    for x in PK[i]["needs_all"]:
        if x not in seen:
            seen.add(x)
            _up(x, seen)
    return seen


def test_the_recount_runs_and_says_what_the_findings_quote():
    out = subprocess.run([sys.executable, "-B", str(HERE / "read_checks.py")], capture_output=True, text=True, check=True, timeout=300).stdout
    for s in ("every one is in a package upstream of the sealed card: True", "the sealed card now waits on the suite and on the comparison's own instruments: True",
              "packages marked started while a need has not started: 0", "every finding names what it bears on: True",
              "the script the foundation cites for the live price exits 1"):
        assert s in out, s
    sealed = (HERE / "read_checks_run.txt").read_text(encoding="utf-8")
    # 8 at the read; 9 since the owner named the orientation's condition on 2026-11-11 (B1879), which the run now prints
    # The count of debts joined to nothing was typed here (64 at the read, then 65, 66, 67): a pin on a live value, edited each time
    # a debt was registered.  What it stood for is asserted instead: the run's three counts agree
    import re as _re
    m = _re.search(r"debts on the map: (\d+); joined to a node by an edge: (\d+); joined to nothing: (\d+)", sealed)
    assert m and int(m.group(3)) == int(m.group(1)) - int(m.group(2))
    assert "an exit with no objection on the page: 9" in sealed


def test_the_four_repairs_are_in_force():
    F = P["findings"]
    assert sorted(P["bears_on"]) == sorted(F) and all(P["bears_on"][k] for k in F)
    repo = [k for k, b in P["bears_on"].items() if "REPOSITORY" in b]
    up = _up("WP-5.3")
    assert repo and all(F[k]["wp"] in up for k in repo)
    assert {"WP-0.2", "WP-0.5"} <= set(PK["WP-5.3"]["needs"])
    assert not [(w, x) for w in PK for x in PK[w]["needs_all"] if not PK[w]["status"].startswith("NOT STARTED") and PK[x]["status"].startswith("NOT STARTED")]
    fixed = [k for k, f in F.items() if f["state"] == "FIXED"]
    # "fixed" is main's word and the re-audit's verdict is a field apart: a fixed finding either carries that seat's acceptance,
    # or is listed as fixed and not yet re-audited.  (When this lock was written all eight fixed ones were accepted; main has
    # fixed more since, and those are shown as not yet read by that seat, never as accepted.)
    unread = P["stats"]["fixed_and_not_yet_re_audited"]
    assert fixed and sorted(k for k in fixed if k not in P["accepted"]) == sorted(unread)
    assert all(P["accepted"][k].startswith("accepted") for k in fixed if k in P["accepted"])
    # eight when this lock was written; eleven after the seat's fourth re-audit read B1878's two and accepted E3 (B1880)
    # 2026-11-11: the line pinned eleven, and the seat's sixth re-audit accepted a twelfth (E5).  What it holds now is the rule:
    # every finding marked fixed has a re-audit's acceptance, and none is fixed and unread.
    assert len([k for k in fixed if k in P["accepted"]]) == len(fixed) >= 11 and unread == []
    assert F["E3"]["state"] == "FIXED" and F["X3"]["wp"] == "WP-0.12" and F["X4"]["wp"] == "WP-0.11"
    # the control: a finding about the repository filed in a package the card does not wait on would be seen here
    outside = [w for w in PK if w not in up and w != "WP-5.3" and not w.startswith(("WP-5.4", "WP-6"))]
    assert not any(F[k]["wp"] in outside for k in repo)


def test_what_is_owed_is_said_and_registered():
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "**owed**: 64 of 81 are joined to nothing", "Both halves of the", "Nothing here is a result about the mathematics"):
        assert s in f, s
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    assert "| P-773 |" in reg
