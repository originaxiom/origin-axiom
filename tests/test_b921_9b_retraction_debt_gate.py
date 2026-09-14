"""B921-9b lock -- the retraction-debt gate: every RETRACTED arc is NAMED in docs/RETRACTIONS.md.

The gap this gate closes is L143's, on a second surface: `retraction-sweep` polices the CONTENT
of rows that exist and is RIGHT to be green while seven rows are simply missing. These tests pin
(1) the check finds all twelve RETRACTED arcs from the verdict files, (2) the real ledger is
clean, (3) the check FAILS on a ledger with the rows stripped -- the failure path exercised
against a real-shaped file, because a check that cannot fail is not a check (MB12), (4) a bare
mention without a retraction verb does NOT discharge a debt, and (5) the id boundary is exact,
so B437 is not discharged by a row about B4370.
"""
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "checks" / "retraction_debt.py"


def _mod():
    spec = importlib.util.spec_from_file_location("retraction_debt", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_twelve_retracted_arcs_are_found_from_the_verdict_files():
    arcs = _mod().retracted_arcs()
    # the count is the corpus's own: gate_supersession_backlinks' docstring says "the 12
    # RETRACTED arcs are a separate, deliberate act". The seven this lead wrote rows for:
    for i in ["B58", "B192", "B216", "B702", "B731", "B780", "B1181"]:
        assert i in arcs, f"{i} is RETRACTED but the check does not see it"
    # and the five that already had rows
    for i in ["B90", "B225", "B437", "B519", "B964"]:
        assert i in arcs
    assert not any(k.startswith("<unparsed:") for k in arcs), sorted(arcs)


def test_the_real_ledger_is_clean():
    r = subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "12 of 12" in r.stdout, r.stdout


def test_the_check_fails_when_the_rows_are_stripped(tmp_path):
    # MB12: the failure path, against a real-shaped file. The ledger's first 12 lines are its
    # preamble and table header -- every row removed, no arc registered.
    stripped = tmp_path / "RETRACTIONS.md"
    src = (ROOT / "docs" / "RETRACTIONS.md").read_text(encoding="utf-8").splitlines()[:12]
    stripped.write_text("\n".join(src) + "\n", encoding="utf-8")
    env = dict(os.environ, OA_RETRACTIONS_LEDGER=str(stripped))
    r = subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True, env=env)
    assert r.returncode == 1, "the check passed a ledger with every row removed"
    assert "12 UNREGISTERED" in r.stdout, r.stdout


def test_a_bare_mention_without_a_retraction_verb_does_not_discharge_the_debt():
    reg = _mod().registered
    # this is what stops "see B731 for the index table" from counting as a registration
    assert "B731" not in reg("| see B731 for the level-by-level index table |")
    assert "B731" in reg("| B731's headline | ... | RETRACTED -- the index jumps at level (8) |")
    # the corpus's other retraction verbs, each taken from a row already in the ledger
    for verb in ["REFUTED", "WITHDRAWN", "CORRECTED", "OVERTURNED", "NEGATED",
                 "RELABELED", "DISSOLVED", "SUPERSEDED", "REPLACED", "VACUOUS"]:
        assert "B999" in reg(f"| B999 | x | {verb} -- y | z |"), verb


def test_the_arc_id_boundary_is_exact():
    reg = _mod().registered
    # B437 must match inside a path, and must NOT be discharged by a longer id
    assert "B437" in reg("RETRACTED -- frontier/B437_child_abelian_book/FINDINGS.md")
    assert "B437" not in reg("RETRACTED -- the B4370 row")
    assert "B4370" not in reg("RETRACTED -- the B437 row")
