"""B74 (Path C, V56) -- locking test for the higher-spin / W_N literal-match result.

Locks the two NON-TRIVIAL symbolic facts that make the grading a literal shared object, and the
DIVERGENCE of the full spectra (so the honest negative cannot silently drift into a claimed match):
  - W_N charge conjugation C=-X^T grades the spin-s Casimir tr(X^s) by (-1)^s (sl(3,4,5), generic X);
  - the Dickson grading L_s(-m)=(-1)^s L_s(m) is the SAME involution on the metallic invariants;
  - on the overlap of W_n spins {2..n} and rank-n Dickson positive powers the gradings coincide,
    AND the Dickson tower carries extras (neg powers / sign sectors / multiplicities) with no W_n
    counterpart -- i.e. NOT a full spectral bijection for n>=4.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b74_hsg", _ROOT / "frontier" / "B74_higher_spin_grading" / "probe.py")
hsg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hsg)


def test_wn_charge_conjugation_grades_casimirs_by_sign():
    """The W_N grading: tr((-X^T)^s) = (-1)^s tr(X^s) for a generic traceless X, sl(3),(4),(5)."""
    for n in (3, 4, 5):
        chk = hsg.casimir_conjugation_check(n)
        assert all(chk.values()), (n, chk)


def test_dickson_parity_is_the_same_involution():
    """The Dickson grading: L_s(-m) = (-1)^s L_s(m), s=1..6 -- -w0 on the metallic invariants."""
    dp = hsg.dickson_parity_check(6)
    assert all(dp.values()), dp


def test_grading_matches_on_overlap_but_spectrum_diverges():
    """On the overlap the two gradings coincide (literal shared object); for n>=4 the Dickson tower
    has extras (no full bijection) -- the honest negative is locked."""
    # n=3: clean bijection {2,3}={2,3}, no positive extras
    c3 = hsg.compare(3)
    assert c3["grading_match"] and c3["overlap"] == [2, 3] and c3["extras"] == []
    # n=4,5: gradings agree on overlap, but the spectra DIVERGE (extras present)
    for n in (4, 5):
        c = hsg.compare(n)
        assert c["grading_match"], (n, "grading must agree on overlap")
        assert set(c["spins"]).issubset(set(c["powers"])), (n, "W_n spins embed in Dickson powers")
        diverges = bool(c["extras"]) or bool(c["extra_mult"]) or bool(c["neg_powers"]) or bool(c["sign_sectors"])
        assert diverges, (n, "n>=4 must NOT be a clean bijection -- extras expected")
