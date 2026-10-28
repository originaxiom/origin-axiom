"""B1791 -- Im tau is not found forced in B1656's frame.  The rho' Higgs's Petersson peak is line- and Re tau-independent at
2.8406 and moves with the eta power (a convention); the strength-type functionals rise monotonically on the committed scan."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1791_im_tau_not_forced_in_the_frame" / "verification"


def test_the_rho_prime_peak_is_one_height_set_by_a_convention():
    run = (V / "referee" / "fine_eta_run.txt").read_text(encoding="utf-8")
    peaks = [float(x) for x in re.findall(r"eta\^6 dR  \(weight 4.5\) Re tau [0-9.]+: Petersson-norm maximum at Im tau = ([0-9.]+)", run)]
    assert len(peaks) == 5 and all(abs(p - 2.8406) < 1e-4 for p in peaks)          # the same height at every Re tau
    fam = {int(m): float(y) for m, y in re.findall(r"m = +(\d+): max at Im tau = ([0-9.]+)", run)}
    assert abs(fam[5] - 3.8175) < 1e-3 and abs(fam[6] - 2.8406) < 1e-3 and abs(fam[7] - 2.3092) < 1e-3
    assert not any(2.96 <= y <= 3.11 for y in fam.values())                       # no integer power lands in the strip


def test_the_strength_type_functionals_rise():
    s = json.loads((V / "functionals_summary.json").read_text(encoding="utf-8"))
    assert len(s) == 324
    for key in ("F3_frob_S", "F4_nuc_S", "F5_smax_S", "F3_frob_St", "F4_nuc_St", "F5_smax_St"):
        series = [v for k, v in s.items() if k.endswith("|" + key)]
        assert len(series) == 27 and all(v["trend"] == "up" and not v["extrema"] for v in series), key
    assert sum(1 for v in s.values() if v["extrema"]) == 4                          # the draft's four shallow, line-specific extrema
