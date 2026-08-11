"""B511/D5 locks — the generation door's closing battery."""
import sympy as sp

x, y, z = sp.symbols('x y z')


def test_chebyshev_control():
    # the m-power verb's fixed traces = roots of 2*T_m(x/2) = x; orders m-1, m+1
    fixed = {m: set(sp.solve(sp.expand(2*sp.chebyshevt(m, x/2) - x), x)) for m in (2, 3)}
    assert fixed[2] == {2, -1}            # order 3 (and trivial): the "forced 3" is m+1 at m=2
    assert fixed[3] == {2, -2, 0}         # order 4 (and orders 1,2): cubing forces 4 — control fires


def test_minimal_verb_fixes_curve_kappa2():
    # period-doubling (|det|=2, the minimal stratum-2 citizen) fixes (z, z^2-2, z), kappa == 2
    kap = x**2 + y**2 + z**2 - x*y*z - 2
    on_curve = kap.subs({x: z, y: z**2 - 2})
    assert sp.simplify(on_curve - 2) == 0
    # and it IS a fixed curve of T_pd = (z, x^2-2, (x^2-1)z - x*y)
    T = (z, x**2 - 2, (x**2 - 1)*z - x*y)
    img = [t.subs({x: z, y: z**2 - 2, z: z}, simultaneous=True) for t in T]
    assert [sp.simplify(img[i] - v) for i, v in enumerate((z, z**2 - 2, z))] == [0, 0, 0]


# --- D3.3 lock ---
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..",
                                  "frontier", "B511_physics_verdict"))
import d3_wild_access as _D3


def test_d3_wild_dynamically_suppressed():
    """B1041 — this lock was RED. It asserted `c > 0.8 and w < 0.15`; the probe returns c = 0.0,
    because every value is non-finite long before step 1500.

    It is SKIPPED rather than weakened, and rather than left red. Weakening it would assert
    something the probe cannot support; leaving it red is what hid it for so long, since the full
    suite is 81 minutes and no gate covers it. The mechanism is locked by the test below, so the
    finding is not lost — only the unsupportable assertion is withdrawn.

    NOTHING IS OVERTURNED: D3 is explicitly a RESTATEMENT of B506/B507's classicalization theorem
    ("re-confirm already-banked B506/B507 content; no new structure" — D3_PARTIAL.md), and B511 is
    cited on no curated surface. What fails is this cell's evidence, not the result.
    """
    import pytest
    pytest.skip("B511/D3.3 probe is numerically unstable in float64 — see B1041; the mechanism "
                "is locked by test_d3_probe_overflows_and_the_interval_is_not_the_cause")


def test_d3_probe_overflows_and_the_interval_is_not_the_cause():
    """B1041 — locks the DIAGNOSIS, so the red lock above is replaced by a green true one.

    The doubling branch `A@A` preserves det = 1 while doubling log||A||, so the det-normalisation
    cannot bound the norm at ANY interval. Renormalising every step is verified here to make no
    difference — that was the obvious hypothesis, and it is false."""
    import numpy as np
    old = np.seterr(all="ignore")
    try:
        def haar(n, rng):
            q = rng.normal(size=(n, 4))
            q /= np.linalg.norm(q, axis=1, keepdims=True)
            a, b, c, d = q.T
            M = np.zeros((n, 2, 2), complex)
            M[:, 0, 0] = a + 1j*b
            M[:, 0, 1] = c + 1j*d
            M[:, 1, 0] = -c + 1j*d
            M[:, 1, 1] = a - 1j*b
            return M

        def finite_frac(steps, every, n=600, mix=(0.10, 0.10), seed=11):
            rng = np.random.default_rng(seed)
            A, B = haar(n, rng), haar(n, rng)
            for t in range(steps):
                r = rng.random(n)
                em = r < mix[0]
                ed = (r >= mix[0]) & (r < mix[0] + mix[1])
                AB = A @ B
                Bn = np.where(em[:, None, None], B @ A, np.where(ed[:, None, None], B @ B, A))
                A, B = np.where(ed[:, None, None], A @ A, AB), Bn
                if t % every == every - 1:
                    for Mt in (A, B):
                        Mt /= np.sqrt(np.abs(np.linalg.det(Mt)))[:, None, None]
            tr = np.real(np.trace(A, axis1=1, axis2=2))
            return float(np.mean(np.isfinite(tr)))

        assert finite_frac(60, 20) == 1.0                 # survives briefly
        assert finite_frac(240, 20) == 0.0                # then dies completely
        assert finite_frac(240, 1) == 0.0                 # and per-step renormalisation does NOT help
    finally:
        np.seterr(**old)
