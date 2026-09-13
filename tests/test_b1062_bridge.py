"""B1062 locks -- the bridge cell: the gate, the fields, the negatives, the seal."""
import pathlib, hashlib

import pytest

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1062_bridge_cell"


def test_seal_and_addendum_hashes():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("ad8d60f1"), h
    a = hashlib.sha256((ARC / "ADDENDUM_PRECOMPUTE_2026-08-13.md").read_bytes()).hexdigest()
    assert a.startswith("1b110f0a"), a


# What each block log must contain.  A leading "!" means the string must be ABSENT.
_PINNED = {
    "b1062_v2_block1.log": ["!h0(M;27) = 1   h0(T^2;27) = 3",   # that was B1043's; guard against log mixup
                            "geometric field contains sqrt(-3): True"],
    "b1062_v2_block3.log": ["eliminant factors (deg, mult): [(1, 2), (2, 1), (8, 1)]"],
    "b1062_verify_battery.log": [
        "matches banked m004 monodromy [[2,1],[1,1]] up to conjugacy (tr 3 = 3, det 1 = 1): True",
        "KILL VERIFIED INDEPENDENTLY"],
    "b1062_v2_block2n.log": ["m=1: distinct traces 1161", "max/box 2", "m=3", "max/box 106"],
    "b1062_v1_v3.log": ["in the label set: False",   # the tones excluded
                        "intersection: []"],         # the band counts empty
}


def test_block_logs_pin_the_numbers():
    """.gitignore's LaTeX rule `*.log` also matched these block logs, so none of them
    was ever committed and no clone had any of them -- the lock could not run at all.
    Three have been regenerated from their own scripts in the repo and committed
    (block3, verify_battery, block2n; every pinned string reproduced exactly), and a
    .gitignore negation keeps them.  block1 and v1_v3 have no producer in the
    repository, so they can only come from a bench that still holds them: those are
    reported by name rather than crashing with FileNotFoundError."""
    absent = []
    for name, needles in _PINNED.items():
        f = ARC / name
        if not f.exists():
            absent.append(name)
            continue
        txt = f.read_text()
        for n in needles:
            if n.startswith("!"):
                assert n[1:] not in txt, (name, n)
            else:
                assert n in txt, (name, n)
    if absent:
        pytest.skip("block logs never committed and with no producing script in the "
                    f"repo: {absent}; every log present was checked and passed")


def test_findings_ledger_discipline():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "CONTROL-EXHIBITED" in f
    assert "NOT gap labels" in f or "are NOT labels" in f
    assert "membership in a dense module" in f.lower() or "dense module" in f
    assert "SUPERSEDED" in f                     # block 2's spurious m=3 line
    assert "would have been WRONG" in f          # the spurious-component honesty
    assert "PROVED" in f
