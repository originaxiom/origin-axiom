"""B1007 — locks for a failed instrument attempt and the correction it forced.

WHAT THIS ARC IS
----------------
B1007 tried to build an arbitrary-precision Maass solver, failed its own validation gate,
claimed a cost overturn that was FALSE, and then discovered that a working sealed arb-based
25-digit solver had been on main since B922. Banked NEGATIVE.

The most valuable lock here is test_the_working_solver_is_on_main: this session lost nine arcs
to the same failure — grepping claims instead of reading code — and the specific form it took
here was rebuilding an instrument the repo already had. A test that ASSERTS THE INSTRUMENT
EXISTS is the cheapest thing that stops the next seat repeating it, because the false belief
("we have no high-precision solver") now fails a test rather than merely being wrong.
"""
from __future__ import annotations

import json
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1007_arb_maass"
WORKING = ROOT / "frontier" / "B878_maass_upper_window" / "branch_cell9_rung1_v2.py"


def test_the_working_solver_is_on_main():
    """THE LOCK THAT MATTERS. A sealed, arb-based, 25-digit Maass solver is in this repo.

    B1007 was written because this seat believed the programme had no such instrument and that
    building one was the next step. It was wrong: the script behind B922's 58.1-hour run is on
    main, carries B922's own seal hash, and drives arb directly. Anyone who again concludes
    "we need to build a high-precision solver" must first explain why this file is not one.
    """
    assert WORKING.is_file(), (
        f"{WORKING.relative_to(ROOT)} is the 25-digit solver behind B922. If it moved, update "
        "this lock — do not delete it and do not rebuild the instrument.")
    src = WORKING.read_text()
    assert "169e9042" in src, "the working solver must carry B922's seal hash"
    assert "import flint" in src, "the 58.1h run used arb — this is what refutes B1007's draft"
    assert "bessel_k" in src and "acb_mat" in src, (
        "both primitives B1007 claimed to 'discover' are already used here")


def test_B798_stands_and_the_cost_claim_is_withdrawn():
    """B798's law AND its cost estimate both stand. B1007 withdrew its challenge to them.

    B798 priced the 100-digit run at 4-5 orders of magnitude 'on a different numerical stack
    (arb/mpmath Bessel, mp linear algebra)' — it NAMED arb. The two-term cost model is the
    content: modes scale ~linearly with precision, and the dense solve is cubic in modes.
    B1007's draft measured only per-operation precision cost at FIXED mode count, which is the
    one term that was never the problem.
    """
    b798 = (ROOT / "frontier" / "B798_falsifier_power_box" / "FINDINGS.md").read_text()
    assert "arb/mpmath Bessel" in b798, (
        "B798's own text names the arb stack; this is what makes B1007's draft claim false")
    claim = json.loads((ARC / "arc_verdict.json").read_text())["claim_one_line"]
    assert "WITHDRAWN" in claim and "B798 STANDS" in claim
    assert "HELD THE MODE COUNT FIXED" in claim, (
        "the arc must keep naming its own error, not merely record that it erred")


def test_the_verdict_is_negative_and_the_gate_stayed_shut():
    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["verdict"] == "NEGATIVE"
    assert verdict["instrument"] is True
    findings = (ARC / "FINDINGS.md").read_text()
    assert "4.9000853730625213014795758" in findings, (
        "the gate's target must stay quoted so the failure is checkable")
    assert "ninth instance" in findings.lower(), (
        "the failure mode is the arc's main content; it must not be softened away")


# --- the one surviving positive observation, and the exact geometry ------------------

flint = pytest.importorskip("flint", reason="python-flint (arb) not installed on this bench")


def test_the_91_moves_are_exact_integer_pairs_over_Z_omega():
    """The geometry port is correct — and redundant with the working solver's own machinery.

    Locked anyway because it is cheap and because a wrong entry here would silently invalidate
    the one architectural point B1007 got right: every move is integral, so a float-chosen
    move can be applied exactly.
    """
    moves = json.loads((ARC / "moves_eisenstein.json").read_text())
    assert len(moves) == 91
    for k, M in enumerate(moves):
        for i in range(2):
            for j in range(2):
                a, b = M[i][j]
                assert isinstance(a, int) and isinstance(b, int), (
                    f"move {k} entry ({i},{j}) is not an exact integer pair")


def test_the_dual_lattice_is_skewed_at_small_M():
    """THE ONE GENUINELY NEW OBSERVATION, and it is a warning about method.

    Lam* = Z + (i/(2 sqrt3))Z and 1/(2 sqrt3) ~ 0.289, so ordering by |mu| pulls in many n
    before a second m: at M = 30 the m-range is still only {-1, 0, 1}. This is a CONSEQUENCE
    of choosing modes by COUNT — the working solver takes all |mu| <= R_cut instead, with
    R_cut set by where K_ir dies. Locked so the count-based shortcut is not retried.
    """
    import sys
    sys.path.insert(0, str(ARC))
    import arb_maass  # noqa: E402
    ms = {m for m, _ in arb_maass.dual_lattice(30)}
    assert ms <= {-1, 0, 1}, f"expected the skew to persist at M=30, got m-range {sorted(ms)}"
