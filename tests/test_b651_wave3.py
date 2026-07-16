"""B651 locks — the wave-3 integration."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B651 = os.path.join(HERE, "..", "frontier", "B651_wave3_integration")
PK = os.path.join(B651, "cc2_packets")


def test_key_seals_live():
    seals = {
        "finisher_queue/finisher_queue/f1_jump/JUMP_LAW_THEOREM.md":
            "bda4f00f",
        "finisher_queue/finisher_queue/f2_psl/PSL_THEOREM.md": "4d5d0d71",
        "finisher_queue/finisher_queue/f3_twisted/PREREG_F3.md": "9320e6f9",
    }
    for rel, h8 in seals.items():
        got = hashlib.sha256(
            open(os.path.join(PK, rel), "rb").read()).hexdigest()[:8]
        assert got == h8, rel


def test_witness_corrections_exact():
    import json
    import sympy as sp
    d = json.load(open(os.path.join(HERE, "..", "frontier",
                                    "B649_silver_holonomy",
                                    "entries_L.json")))
    s = sp.sqrt(4 + 4 * sp.sqrt(2))

    def toL(nm, i, j):
        re = sum(sp.Rational(x) * s ** k
                 for k, x in enumerate(d[f"{nm}{i}{j}"][0]))
        im = sum(sp.Rational(x) * s ** k
                 for k, x in enumerate(d[f"{nm}{i}{j}"][1]))
        return re + sp.I * im

    def mat(nm):
        return sp.Matrix(2, 2, lambda i, j: toL(nm, i, j))

    A, B, C = mat("a"), mat("b"), mat("c")
    assert sp.simplify(sp.radsimp((A * B * C).trace() / (A * C).trace())
                       - (1 + sp.I)) == 0
    assert sp.simplify(sp.radsimp((A * A).trace() / B.trace()) - sp.I) == 0


def test_errata_and_noticed_correction_present():
    fnd = open(os.path.join(HERE, "..", "frontier",
                            "B649_silver_holonomy", "FINDINGS.md")).read()
    assert "ERRATA" in fnd and "tr(a²)/tr(b) = i" in fnd
    b646 = open(os.path.join(HERE, "..", "frontier",
                             "B646_wave2_integration", "FINDINGS.md")).read()
    assert "DIED at r = 23" in b646
    el = open(os.path.join(HERE, "..", "docs", "ERROR_LEDGER.md")).read()
    assert "E13" in el and "Stale artifact text" in el
