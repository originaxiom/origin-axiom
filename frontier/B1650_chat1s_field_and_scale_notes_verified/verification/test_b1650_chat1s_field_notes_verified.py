"""B1650 -- chat1's field notes verified on main.  The stored recheck and reproduction record; live: O6's identity
sum_r R_r^2 wp(z_r) = 0 with the record's pairing at one tau, and the bite -- a permuted pairing does not vanish."""
import json, pathlib
import mpmath as mp
A = pathlib.Path(__file__).resolve().parents[1]


def test_stored():
    d = json.load(open(A / "verification" / "main_recheck.json"))
    assert all(r["record_pairing_rel"] < 1e-25 for r in d["O6_sum_R2_wp"]) and d["C5b_max_rel"] < 1e-12
    assert d["Ad_minus1_is_identity_on_M"]
    rec = json.load(open(A / "verification" / "reproduction_record.json"))
    ident = {r["output"]: r["byte_identical"] for r in rec["runs"]}
    assert ident["checks_2.json"] and ident["condensate_in_M.json"]
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_live_o6_and_bite():
    mp.mp.dps = 25
    t = mp.mpc(0.21, 1.13); q = mp.exp(1j * mp.pi * t); th = lambda n, z: mp.jtheta(n, z, q)
    d = mp.pi * th(2, 0) * th(3, 0) * th(4, 0)
    R2 = [(-th(2, 0) ** 2 / d) ** 2, (-th(4, 0) ** 2 / d) ** 2, (1j * th(3, 0) ** 2 / d) ** 2]
    g = lambda z: mp.diff(lambda w: mp.log(th(1, mp.pi * w)), z, 2)
    G = [g(mp.mpf(1) / 2), g(t / 2), g((1 + t) / 2)]
    scale = sum(abs(R2[r] * G[r]) for r in range(3))
    assert abs(sum(R2[r] * G[r] for r in range(3))) / scale < 1e-18                 # the record's pairing
    assert abs(R2[0] * G[1] + R2[1] * G[0] + R2[2] * G[2]) / scale > 1e-2             # the bite: swapping i and j fails


def test_scale_stored():
    d = json.load(open(A / "verification" / "main_scale_recheck.json"))
    assert abs(d["LLR_CS_over_pi2"] + 1 / 24) < 1e-12 and d["mirror_max_dvol"] < 1e-9 and d["mirror_max_cs_sum_mod"] < 1e-9
    assert all(x[1] < 1e-9 for x in d["swap_symmetric_in_sample"]) and d["L25R25_vol"] < d["two_v8"]
    assert max(d["hitchin_residual_sign_+1"]) < 1e-12 and max(d["hitchin_residual_sign_-1"]) > 1e-3   # the sign is controlled
