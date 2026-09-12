"""B1338 - the widened already-banked surfaces are wired and non-vacuous.

B1202's instrument is MANDATORY before writing MISSING/OPEN, and it could not read the ledgers
or the SCHEDULED artifacts that live only at other commits -- which is where the record's
rediscoveries live. These assert the new surfaces exist and actually fire, and that the DEFAULT
path is unchanged so B1202's own controls keep measuring what they measured.
"""
import pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECK = ROOT / "scripts" / "checks" / "already_banked.py"


def _run(args):
    return subprocess.run([sys.executable, str(CHECK)] + args,
                          capture_output=True, cwd=ROOT).stdout.decode("utf-8", "ignore")


def test_wide_flag_exists_and_reports_both_surfaces():
    out = _run(["--wide", "three", "generations", "not", "derived"])
    assert "--wide:" in out, "the --wide surfaces are not wired in"


def test_wide_finds_the_consolidation_that_was_rediscovered():
    """memo 152 answers 'what exactly we do not have'; proposing that consolidation afresh
    is the rediscovery this surface exists to stop."""
    out = _run(["--wide", "what", "exactly", "we", "do", "not", "have", "chain"])
    assert "memo 152" in out, "the SCHEDULED/ledger surface did not surface memo 152"


def test_default_path_unchanged_for_b1202_negative_controls():
    """Without --wide the instrument must still be SILENT on B1202's declared blind regions,
    or B1202's own controls stop measuring what they measured."""
    # B1202's own control always passes --exclude=B1202: a self-documenting instrument
    # matches its own test phrases, and excluding it is what that flag is for.
    out = _run(["--exclude=B1202", "inflation", "reheating", "e-folds", "primordial"])
    assert "a MISSING/OPEN claim is admissible" in out, (
        "default behaviour changed: B1202's negative control no longer clean")
