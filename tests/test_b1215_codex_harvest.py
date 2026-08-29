"""B1215 — the codex transcript harvest. Locks the theorem's scope, the wrappers' honesty, and the
fence on a conditional lead."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1215_codex_transcript_harvest"


def _res():
    return json.loads((ARC / "b1215_results.json").read_text(encoding="utf-8"))


def test_no_wrapper_claims_success_without_gating_on_its_own_output():
    """Codex's flag, made permanent. A wrapper that asserts REPRODUCES on the process exiting 0
    rather than on the computation asserting something is a reproducer that cannot fail."""
    ungated = []
    for f in ROOT.glob("frontier/*/verification/reproduce.sh"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        if "echo REPRODUCES" in t and not any(k in t for k in ("grep -q", "&&", "assert", "[ ")):
            ungated.append(str(f.relative_to(ROOT)))
    assert not ungated, f"wrappers printing REPRODUCES with no gate: {ungated}"


def test_the_reproducer_that_reproduces_nothing_says_so():
    """B1175 cannot re-run its certificates -- they live on another seat's branch. It must not
    claim to. RECORD is the true word; REPRODUCES was not."""
    t = (ROOT / "frontier" / "B1175_charter_close_harvest" / "verification" /
         "reproduce.sh").read_text(encoding="utf-8")
    assert "RE-RUNS NOTHING" in t, "the correction must be stated in the file"
    assert "RECORD" in t
    assert "echo \"REPRODUCES\"" not in t and "echo REPRODUCES" not in t


def test_r022_does_not_refute_the_registered_v4_theorem():
    """The scope boundary. R022's negative is branch-vs-being-x-hearing; B1182 is the sqrt(-3)
    internal pair. If these are ever conflated, a registered theorem reads as refuted."""
    r = _res()["leg_1_r022_vs_b1182"]
    assert r["resolution"].startswith("NO CONFLICT")
    assert "being x hearing" in r["r022_negative_is_about"]
    assert "sqrt(-3)-internal" in r["b1182_theorem_is_about"]
    assert "C4'" in r["settled_by"]
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "T-V4-TORSOR-IDENT" in reg, "the theorem must still be registered"


def test_the_tail_selection_rule_is_derived_not_copied():
    """The invariant that makes codex's correction right: the rule tracks the A-character."""
    p = subprocess.run([sys.executable, str(ARC / "verification" / "tail_selection.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert p.returncode == 0, p.stderr[-300:]
    assert "VERIFIED" in p.stdout
    r = _res()["leg_3_tail_selection"]
    assert r["reproduces_spec_rule_for_A7"] == 8 and r["gives_for_A11"] == 4
    assert r["repeated_vanishing_by_skewness"] == [2, 2]


def test_the_conditional_stays_conditional():
    """The lead is worth carrying and easy to over-read. The A_11 premise is NOT established, and
    the effect on B1208's fork is evidence against one branch, not a decision."""
    r = _res()["leg_3_tail_selection"]
    assert "undetermined at" in r["fenced"]
    assert r["conditional_effect_on_b1208_fork"].startswith("evidence AGAINST")
    assert "does not decide" in r["conditional_effect_on_b1208_fork"]
