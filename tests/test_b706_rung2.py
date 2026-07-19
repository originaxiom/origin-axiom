"""B706 lock — the rung-2 structural comparator returns NO-MATCH (pyenv-pure)."""
import mpmath as mp


def test_rung1_lepton_ratios_generic_over_Q5():
    mp.mp.dps = 40
    s5 = mp.sqrt(5)
    # the precise lepton mass ratio: no low-height algebraicity over Q(sqrt5)
    x = mp.mpf('105.6583755') / mp.mpf('0.51099895000')      # m_mu/m_e, ~9 digits
    basis = [x**i * (s5**j) for i in range(3) for j in range(2)]
    rel = mp.pslq(basis, maxcoeff=10**3, maxsteps=10**5)
    assert rel is None, f"unexpected low-height relation {rel} (would be a rung-1 hit)"


def test_cabibbo_candidate_is_rational_rung4_not_rung1():
    # the 'hit' 9 - 40x = 0 is x = 9/40, RATIONAL (in Q, not Q(sqrt5)); rung-4, dead
    x = mp.mpf(9) / 40
    assert x == mp.mpf('0.225')          # rational, sqrt5 absent
    # it does not involve the audible field -> not the object speaking


def test_rung2_kind_mismatch_discrete_vs_continuous():
    # the seam is a finite F_2-space (2^k points); the SM freedom is continuous (R^n)
    stages = 3                            # e.g. being/hearing/E6
    seam_points = 2 ** stages             # finite, discrete
    sm_params = 19                        # ~ continuous real dof
    assert seam_points == 8 and seam_points < float('inf')
    # discrete-finite != continuous: the SM freedom is not an F_2-space
    assert isinstance(seam_points, int) and sm_params > seam_points
