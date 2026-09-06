"""B1280 — the chirality probe: (fast) the theta-odd pairing law -- the object's inversion acts on the six deformation
classes H^1(M; Sym^n rho_0), n in {2, 8, 10, 14, 16, 22}, by exactly the E_6 outer automorphism's signs (+, -, +, +, -, +),
exactly over two primes, so N(27) = 0 on the whole E_6 deformation germ; (fast) the exact identities behind the W1/W2
theorem at generic points (lambda = mu^(+-3) with c = 1; tr Phi^-1 = 2 tr mu^-1; det Phi^-1 = 1; the transpose sheet
has the same eight traces and a different ninth); (slow) the full W1/W2 probe: the cusp-fixed curve K, the
repeated-eigenvalue points, Wang = Fox, max |N| = 0."""
import sys
from pathlib import Path
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "frontier" / "B1280_the_chirality_probe" / "verification"))


def test_the_inversion_is_the_e6_outer_automorphism_on_the_deformation_germ(capsys):
    import theta_odd_pairing as P
    verdict, agree, h1_ok = P.main()
    text = capsys.readouterr().out
    assert agree and h1_ok
    assert verdict['iota'] == ([1, -1, 1, 1, -1, 1], True)
    assert verdict['iota.tau'] == ([1, -1, 1, 1, -1, 1], True)
    assert verdict['tau'] == ([1, 1, 1, 1, 1, 1], False)          # the period-2 swap acts trivially on the germ
    assert "the two primes agree on every row: True" in text


def test_the_geometric_point_is_the_unique_paired_sl2_point(capsys):
    import mod4_criterion_other_sl2 as Q
    r = Q.main()
    text = capsys.readouterr().out
    assert r["E6 (principal; the geometric point)"]['ok'] is True
    assert [k for k, v in r.items() if v['ok']] == ["E6 (principal; the geometric point)"]
    sub = r["E6(a1) (subregular; B1256's I-25 point)"]
    assert sub['summands'] == [2, 4, 6, 8, 10, 10, 14, 16] and sub['dim'] == 70
    assert sub['options'][0][1:3] == ([2, 6, 10, 14], [4, 8, 10, 16]) and sub['options'][0][5] == [10]   # the V10 of the 42 unpaired
    assert "exactly ONE direction is unpaired: the V10 of the 42" in text


def test_the_w1_w2_identities_at_generic_points():
    import chirality_probe_w1w2 as X
    from frontier.B71_sl3_apoly import peripheral as per
    rng = np.random.default_rng(3)
    done = 0
    for name, fn, sgn in (("W1", per.W1, -3), ("W2", per.W2, 3)):
        while True:
            p, q = complex(*rng.standard_normal(2)), complex(*rng.standard_normal(2))
            out = per.realize(fn(p, q))
            if out is None:
                continue
            A, B = out
            T, res, w = per.monodromy(A, B, with_conjugator=True)
            if T is None or not np.allclose(w, A):
                continue
            d = X.analyse_point(A, B, T)
            S = d['lam'] @ np.linalg.matrix_power(d['mu'], sgn)
            c = np.trace(S) / 3
            assert abs(c - 1) < 1e-8 and np.max(np.abs(S - c * np.eye(3))) < 1e-6          # lambda = mu^(+-3), c = 1
            assert abs(np.trace(d['H']) - 2 * np.trace(np.linalg.inv(d['mu']))) < 1e-6      # tr Phi^-1 = 2 tr mu^-1
            assert abs(np.linalg.det(d['H']) - 1) < 1e-6                                     # det Phi^-1 = 1
            assert np.max(np.abs(X.traces8(A, B) - X.traces8(A.T, B.T))) < 1e-9             # the transpose sheet: same eight traces
            lam = d['lam']
            assert abs(np.trace(lam) - np.trace(np.linalg.inv(lam))) > 1e-3                  # ... and a different ninth, off K
            assert all(v == 0 for v in d['N'].values())                                      # N = 0 off K (no cusp-fixed vectors)
            assert all(h == (0, 0) for h in d['h0'].values())
            done += 1
            break
    assert done == 2


@pytest.mark.slow
def test_the_w1_w2_probe_finds_no_net_chirality(capsys):
    import chirality_probe_w1w2 as X
    out = X.main()
    text = capsys.readouterr().out
    assert out['ok_a'] and out['ok_b']
    assert out['maxN'] == 0 and len(out['results']) > 0
    assert all(r[7] == r[8] for r in out['results'])                                         # Wang = Fox at every repeated-eigenvalue point
    assert all(r[5] == r[6] for r in out['results'])                                         # equal Jordan data on V and V*
    assert "two characters off K: True" in text
