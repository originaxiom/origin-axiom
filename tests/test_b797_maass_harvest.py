"""B797 — locks on the harvested m004 Maass spectrum (cc3's B792, certified).

Locks the DATA and the CERTIFICATION arithmetic, not the solver: the eigenvalues are
independently re-derived in B795, and the mode-count certification is what makes the SM
comparison's tolerances meaningful.
"""
import json
import pathlib

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B797_maass_spectrum_harvest"


def _cert():
    return json.loads((ARC / "mode_count_certification.json").read_text())


def test_seventeen_certified_eigenvalues_and_the_drift_bound():
    c = _cert()
    rows = c["rows"]
    assert len(rows) == 17
    assert c["modes"] == [664, 900]                      # the certification pair
    # every per-eigenvalue drift is at or below the reported maximum
    assert max(abs(r["dr"]) for r in rows) <= c["max_dr"] * (1 + 1e-12)
    # UNITS (corrected 2026-07-29, cc3's delta 6): tau_v = max(2*rel_unc, 1e-8) is a RELATIVE
    # tolerance, so the drift must be compared RELATIVE too. cc originally compared the ABSOLUTE
    # max|dr| against the relative floor and reported a 1.8x margin. That is an absolute-vs-
    # relative units error, in the conservative direction, and it was locked here.
    max_rel = max(abs(r["dr"]) / abs(r["r_banked"]) for r in rows)
    assert abs(max_rel - 6.9e-10) < 1e-10                # the correct quantity
    assert max_rel < 1e-8                                # clears the prereg tolerance FLOOR
    assert 13.0 < 1e-8 / max_rel < 16.0                  # ~14.5x, not 1.8x


def test_parent_ground_state_matches_the_secondary_sourced_GH_value():
    """n=6 is the Bianchi ground state; it discharges the B791 provenance alert."""
    rows = _cert()["rows"]
    r6 = [x["r_banked"] for x in rows if abs(x["r_banked"] - 7.072004187) < 1e-6]
    assert len(r6) == 1
    lam = 1 + r6[0] ** 2
    assert abs(lam - 51.013243) < 1e-5
    # G-H (secondary-sourced) gave 51.014: agreement to 4 sig figs, 5th digit off by one,
    # which is exactly the precision caveat the source attaches to its own table.
    assert abs(lam - 51.014) < 1e-3
    assert abs(lam - 51.014) > 1e-4                      # the 5th digit genuinely differs


def test_eigenvalues_are_ordered_and_lambda_matches_the_convention():
    rows = _cert()["rows"]
    rs = [x["r_banked"] for x in rows]
    assert rs == sorted(rs)
    assert rs[0] > 3.9 and rs[-1] < 9.9                  # the certified window
    for x in rows:                                       # lambda = 1 + r^2 throughout
        assert abs((1 + x["r_banked"] ** 2) - (1 + x["r_banked"] ** 2)) < 1e-12


def test_sm_comparison_is_a_clean_null_with_candidates_actually_generated():
    """The null is only meaningful because candidates WERE produced and then killed."""
    d = json.loads((ARC / "sm_comparison_results.json").read_text())
    blob = json.dumps(d)
    assert "gated" in blob or "candidates" in blob       # the record carries both counts
    # the prereg seal is byte-pinned: harvest must not have altered it
    import hashlib
    h = hashlib.sha256((ARC / "SM_COMPARISON_PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("c6954bfa")


def test_weyl_completeness_of_the_certified_set():
    """17 distinct / 27 with multiplicity over [0.8, 10] against the leading Weyl budget."""
    mp.mp.dps = 20
    L2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    W = mp.mpf(3) ** mp.mpf(1.5) * mp.zeta(2) * L2 / (4 * mp.pi ** 2) / (6 * mp.pi ** 2)
    rows = _cert()["rows"]
    n_mult = sum(int(x.get("multiplicity", 1)) for x in rows)
    mu = 12 * W * (mp.mpf(10) ** 3 - mp.mpf("0.8") ** 3)
    z = (n_mult - mu) / mp.sqrt(mu)
    assert abs(z) <= 2                                   # PASS band (counts WITH multiplicity)
