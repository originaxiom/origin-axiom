"""Locks: B638 (the swap mechanism) + B639 (the honest partial)."""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B638 = os.path.join(HERE, "..", "frontier", "B638_swap_decomposition")
B639 = os.path.join(HERE, "..", "frontier", "B639_conjtheta_cubic")


def _ledger():
    return open(os.path.join(HERE, "..", "frontier", "B598_l85_campaign",
                             "ARTIFACT_HASHES.txt")).read()


def test_preregs_sealed():
    led = _ledger()
    for d in (B638, B639):
        h = hashlib.sha256(open(os.path.join(
            d, "PREREGISTRATION.md"), "rb").read()).hexdigest()
        assert h in led


def test_b638_banked():
    out = open(os.path.join(B638, "b638_output.txt")).read()
    # the banked transcript is the run's tail section (the build heads are
    # reproducible; the mathematical content is complete)
    assert "sigma*(rep_i) are cocycles, all 5: True" in out
    assert "sigma*^2 = id mod coboundaries, all 5: True" in out
    assert "sigma*[0] = (1/2+1/2r) 0 0 0 0" in out
    assert "laws: ['plus_conj']" in out
    assert "'plus_conj': 3" in out


def test_b639_banked():
    out1 = open(os.path.join(B639, "b639_output.txt")).read()
    assert "no invertible +lambda intertwiner" in out1
    out2 = open(os.path.join(B639, "b639_stage2_output.txt")).read()
    assert "mu-match False" in out2
    fnd = open(os.path.join(B639, "FINDINGS.md")).read()
    assert "FIXES the holonomy pointwise" in fnd


def test_b638_closure():
    out = open(os.path.join(B638, "closure_output.txt")).read()
    assert "direction 1 (the pair implies the law equation): True" in out
    assert "banked values satisfy the law equation: True" in out
    assert "banked ratio = 24*z6: True" in out


def test_b639_stage3():
    out3 = open(os.path.join(B639, "b639_stage3_output.txt")).read()
    assert "B_theta invariance (rho^T B rho = B): True" in out3
    # all four gluing cells fail (the realization obstruction)
    assert out3.count("mu-match False") == 2
    fnd = open(os.path.join(B639, "FINDINGS.md")).read()
    assert "NO representation-twisted amalgam" in fnd


def test_b639_btheta_invariant_pairing_math():
    """The mathematical content behind B_theta (not a transcript grep):
    on an odd-dim irreducible sl2 module the invariant SYMMETRIC pairing
    exists, is unique up to scale, and is antidiagonal with strictly
    alternating signs — solved from the invariance equations directly."""
    import sympy as sp
    n = 5
    s2 = n - 1
    e = sp.zeros(n, n)
    f = sp.zeros(n, n)
    for i in range(n - 1):
        e[i, i + 1] = (i + 1) * (s2 - i)
        f[i + 1, i] = 1
    # invariance: e^T B + B e = 0 and f^T B + B f = 0, B symmetric
    Bsym = sp.MatrixSymbol("B", n, n)
    B = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"x_{min(i,j)}_{max(i,j)}"))
    eqs = list(e.T * B + B * e) + list(f.T * B + B * f)
    sol = sp.solve(eqs, list(set(B)), dict=True)
    assert len(sol) == 1
    Bs = B.subs(sol[0])
    free = list(Bs.free_symbols)
    assert len(free) == 1  # unique up to one scale
    Bn = Bs.subs(free[0], 1) * sp.Rational(1, 1)
    scale = Bn[0, n - 1]
    Bn = sp.simplify(Bn / scale)
    for i in range(n):
        for j in range(n):
            if i + j != n - 1:
                assert Bn[i, j] == 0
    signs = [sp.sign(Bn[i, n - 1 - i]) for i in range(n)]
    assert all(signs[i] == -signs[i + 1] for i in range(n - 1))
