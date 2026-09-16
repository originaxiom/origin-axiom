"""B1415 locks: (1) the Burnside count for a symplectic 2T on K3 with Nikulin's numbers has exactly the two solutions of rank 19;
(2) Kac's order-3 inner classes of E6 modulo the S3 diagram symmetry: five of exact order 3 plus the identity, none the Standard Model;
(3) E6 root-system facts behind sm:B1364: the SM-singlet roots are exactly +-beta, 30 roots are orthogonal to beta, 8 of them are SM roots."""
import itertools, subprocess, sys, os
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1415_the_sm_seats_closing_arcs_harvested", "verification")


def test_burnside_k3_two_solutions():
    r = subprocess.run([sys.executable, os.path.join(V, "burnside_k3.py")], capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, r.stderr[-500:]
    assert "number of solutions: 2" in r.stdout
    assert "2xA2 + 1xA5 + 1xD4 + 1xE6  rank 19" in r.stdout and "2xA2 + 1xA3 + 2xE6  rank 19" in r.stdout


def test_kac_order3_classes():
    r = subprocess.run([sys.executable, os.path.join(V, "kac_s3.py")], capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, r.stderr[-500:]
    assert "order 3: Kac solutions 20; exact order 17; S3-classes exact 5, all 6" in r.stdout
    assert "['A1+A4+1u(1)', 'A2+A2+A2', 'A5+1u(1)', 'D4+2u(1)', 'D5+1u(1)']" in r.stdout
    assert "order 4: Kac solutions 42; exact order 33; S3-classes exact 8, all 11" in r.stdout


def test_e6_sm_centraliser_counts():
    s3 = np.sqrt(3); roots = []
    for i, j in itertools.combinations(range(5), 2):
        for a in (1, -1):
            for b in (1, -1):
                v = np.zeros(6); v[i] = a; v[j] = b; roots.append(v)
    for signs in itertools.product((1, -1), repeat=5):
        v = np.array([0.5 * s for s in signs] + [0.0]); neg = sum(1 for s in signs if s < 0)
        v[5] = s3 / 2 if neg % 2 == 0 else -s3 / 2; roots.append(v)
    R = np.array(roots); assert len(R) == 72 and np.allclose((R ** 2).sum(1), 2)
    su3 = [r for r in R if r[5] == 0 and abs(r[:3]).sum() == 2 and abs(r[3:5]).sum() == 0 and r[:3].sum() == 0]
    su2 = [r for r in R if r[5] == 0 and abs(r[3:5]).sum() == 2 and abs(r[:3]).sum() == 0 and r[3:5].sum() == 0]
    Y = np.array([-1 / 3, -1 / 3, -1 / 3, 1 / 2, 1 / 2, 0]); SM = su3 + su2
    assert len(su3) == 6 and len(su2) == 2
    sing = [r for r in R if all(abs(r @ s) < 1e-9 for s in SM) and abs(r @ Y) < 1e-9]
    assert len(sing) == 2 and np.allclose(sing[0], -sing[1])
    beta = sing[0] if sing[0][5] > 0 else sing[1]
    perp = [r for r in R if abs(r @ beta) < 1e-9]
    assert len(perp) == 30
    assert sum(1 for r in perp if any(np.allclose(r, s) for s in SM)) == 8
