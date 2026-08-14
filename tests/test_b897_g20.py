"""B897 locks. Before results land, exactly one lock is meaningful: the seal.

The results locks are appended at banking; the sealed criteria are evaluated
verbatim in FINDINGS.md.
"""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B897_27_under_g20")
SEALED_SHA = "e293f095349b33ec0d29a9ff44755e779ec8eb7ebb9f394876b14979b60db205"


def test_prereg_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _res():
    import json
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_gates_and_agreement_at_both_primes():
    r = _res()
    for p in ("p1", "p2"):
        assert r[p]["g_dim"] == 20
        assert r[p]["derived_dim"] == 19
        assert r[p]["z_color_dim"] == 11
        assert r[p]["split"] == {"8": 8, "3": 3}
        assert r[p]["tiles_27"] is True
        assert len(r[p]["blocks"]) == 3
        assert all(b["dim"] == 9 for b in r[p]["blocks"])
    assert r["primes_agree"] is True


def test_outcome_a_blocks_present_at_both_primes():
    r = _res()
    for p in ("p1", "p2"):
        blocks = r[p]["blocks"]
        # the (3_c, 3_f) block: both Casimirs nonzero, su(2)' single-valued
        b33 = [b for b in blocks if b["c"] != 0 and b["f"] != 0]
        assert len(b33) == 1 and len(b33[0]["w"]) == 1
        # the (1_c, 3_f) block: color trivial, flavor acts, w-split 3 + 6
        b13 = [b for b in blocks if b["c"] == 0 and b["f"] != 0]
        assert len(b13) == 1
        assert sorted(d for _, d in b13[0]["w"]) == [3, 6]


def test_casimirs_lift_to_the_same_rationals():
    r = _res()
    for p in ("p1", "p2"):
        q = int(r[p]["prime"])
        cvals = {b["c"] for b in r[p]["blocks"]} - {0}
        fvals = {b["f"] for b in r[p]["blocks"]} - {0}
        assert cvals == fvals == {4 * pow(9, -1, q) % q}   # C_c = C_f = 4/9
        wnz = {w for b in r[p]["blocks"] for w, _ in b["w"]} - {0}
        assert wnz == {3 * pow(8, -1, q) % q}              # C_w = 3/8
