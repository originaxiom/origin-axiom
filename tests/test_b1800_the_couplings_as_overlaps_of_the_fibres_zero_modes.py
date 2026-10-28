"""B1800 -- the couplings as bulk overlaps of flux zero modes.  The committed runs: the closed form with K = (Im tau)^(-1/4)
predicted; the identities Y_pq^2 ~ theta_p theta_q; the referee's q-expansion and independent quadrature."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1800_the_couplings_as_overlaps_of_the_fibres_zero_modes" / "verification"


def test_the_closed_form_and_identities():
    a = (V / "assertions_run.txt").read_text(encoding="utf-8")
    assert "(1) K = (Im tau)^(-1/4) predicted" in a and "assertions exit 0" in a
    c = (V / "closed_form_run.txt").read_text(encoding="utf-8")
    assert "predicted zeros vanish: True" in c and "closed_form exit 0" in c
    worst = float(c.split("worst spread ")[1].split()[0]); assert worst < 1e-12


def test_the_referee():
    r = (V / "referee" / "ref_identities_run.txt").read_text(encoding="utf-8")
    assert "ref_identities exit 0" in r
    for f in ("ref_overlaps_run.txt", "ref_b_test_run.txt", "ref_b_joint_run.txt", "ref_q4_and_count_run.txt"):
        assert (V / "referee" / f).read_text(encoding="utf-8").strip()
