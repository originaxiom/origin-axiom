"""B643 locks — the flip-breaking verdict."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B643 = os.path.join(HERE, "..", "frontier", "B643_flip_symmetry")


def test_step1_conjugator():
    out = open(os.path.join(B643, "b643_output.txt")).read()
    assert "conjugator search: ('', 'lam_inv')" in out
    assert "phi(mu) = mu: True" in out


def test_no_global_sl2_companion():
    out = open(os.path.join(B643, "b643_output.txt")).read()
    # Q is a nontrivial unipotent, not +-I
    assert "SL2 global-companion Q" in out and "'(0+1r)'" in out
    # only the derived convention acts on rep0
    assert "A(derived: W=V^-1): tau*(rep0) cocycle = True" in out
    assert "B(no-inverse: W=V): tau*(rep0) cocycle = False" in out


def test_both_families_singular_on_sym0():
    out = open(os.path.join(B643, "b643_output.txt")).read()
    assert out.count("d = ((0), (0), (1))   [blocks Sym16, Sym8, Sym0]") >= 2
    assert out.count("invertible member: False") >= 2
    assert "conjugator: ('aBAb', 1, -1)" in out
    assert "det(normalized U_phib) = (1)" in out
    fnd = open(os.path.join(B643, "FINDINGS.md")).read()
    assert "The chord breaks both amphichiral flip classes" in fnd


def test_f1_naive_obstruction_line():
    """The prereg's F1 verdict (the naive flip fails BOTH J-conventions)
    is asserted from the banked output, per the /loop banking directive."""
    out = open(os.path.join(B643, "b643_output.txt")).read()
    assert "F1 FAIL: the flip does not act on the double in either" in out
    assert "tau*(rep0) cocycle (J-choice A): False" in out
    assert "tau*(rep0) cocycle (J-choice B): False" in out


def test_artifact_hashes_sealed_line():
    hh = open(os.path.join(B643, "ARTIFACT_HASHES.txt")).read()
    assert hh.splitlines()
    assert ("76d64ba0f0f506960d4e90b893813f3e9cc0b5d587173815b0294e2b69f68db3"
            "  PREREGISTRATION.md") in hh
    import hashlib
    got = hashlib.sha256(
        open(os.path.join(B643, "PREREGISTRATION.md"), "rb").read()
    ).hexdigest()
    assert got == "76d64ba0f0f506960d4e90b893813f3e9cc0b5d587173815b0294e2b69f68db3"
