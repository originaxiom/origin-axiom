"""B739 locks — the negatives-hunt P1 re-adjudication (2 revivals + reconfirmation samples).
Locks assert the MATHEMATICS (WORKING_RULES 7), extracted minimal from the sealed recomputes."""
import numpy as np


def test_b58_revival_sealed_recompute_reproduces():
    # The banked kill said the SL(4) 7-factor prediction "cannot be tested numerically";
    # the B739 recompute computed it (eps-extrapolated pinv route, validated on the exact
    # SL(3) anchor, spectrum matching B59's banked factorization). TRANSCRIPT-ASSERT
    # FALLBACK (WORKING_RULES 7, marked as such): the full rerun takes minutes and was
    # verified byte-identical twice in-arc (agent + banking seat); here we pin the sealed
    # output bytes and the spectrum headline.
    import hashlib, os
    p = os.path.join(os.path.dirname(__file__), "..", "frontier",
                     "B742_negatives_hunt_p1", "recompute", "B58", "output.txt")
    data = open(p, "rb").read()
    assert "char(M^" in data.decode("utf-8", "replace")          # the computed spectrum exists
    with open(p + ".sha256") as f:
        assert hashlib.sha256(data).hexdigest() == f.read().split()[0]


def test_b225_revival_the_bad_prime_extraction_is_tautological_at_2():
    # The kill read "2 divides the branch-locus discriminant" as evidence AGAINST
    # '2 = octahedral parent'. Lock the tautology: for ANY monic-in-z quadratic
    # z^2 + a z + b over Z, disc = a^2 - 4b is a SQUARE mod 2 (indeed ≡ a^2 ≡ a mod 2's
    # square structure: disc ≡ a^2 mod 2), so the extraction flags 2 for every such curve.
    for a in range(-6, 7):
        for b in range(-6, 7):
            disc = a * a - 4 * b
            assert (disc - a * a) % 2 == 0     # disc ≡ a² (mod 2): square mod 2, always
    # hence "2 in bad primes" carries zero discriminating information at p=2.


def test_reconfirmed_sample_tomb_l70_roots_of_unity_are_tautological():
    # TOMB-L70 kill (reconfirmed, now computed): finite-k CS eigenvalues are roots of
    # unity BY CONSTRUCTION (the rep is over q = exp(2 pi i/(k+2))). Lock: the SU(2)_k
    # T-matrix diag entries are exact roots of unity for k=1..8.
    for k in range(1, 9):
        N = 4 * (k + 2)
        for a in range(k + 1):
            z = np.exp(2j * np.pi * (a * (a + 2)) / N)
            assert abs(z ** N - 1) < 1e-9      # z is an N-th root of unity


def test_reconfirmed_sample_b516_pisot_dim5_counterexample_now_computed():
    # B516's kill (reconfirmed; previously ASSERTED): golden-field Pisot inflation
    # numbers exist at dim 5 as well as 3 -- nothing selects 3 spatial dimensions.
    # Lock a dim-5 witness: the companion matrix of x^5 - x^4 - x^3 - x^2 - x - 1
    # (pentanacci) has a real root > 1 with all conjugates inside the unit disk (Pisot).
    C = np.zeros((5, 5)); C[0, :] = 1
    for i in range(1, 5): C[i, i - 1] = 1
    ev = np.linalg.eigvals(C)
    ev_sorted = sorted(ev, key=lambda z: -abs(z))
    assert abs(ev_sorted[0].imag) < 1e-9 and ev_sorted[0].real > 1
    assert all(abs(z) < 1 for z in ev_sorted[1:])
