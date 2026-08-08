"""B969 locks — L138 fired, verified independently, with its scope limit."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B969_kato_yukie_verify"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_all_three_cubics_carry_mus_signature():
    r = _res()
    assert r["disc_mu"] == 6237
    assert r["mu_squarefree_kernel"] == [7, 11]
    assert r["all_kernels_are_7_11"] is True
    assert len(r["cubics"]) == 3


def test_the_isomorphism_holds_three_for_three():
    r = _res()
    for c in r["cubics"]:
        assert c["mu_factor_degrees"] == [1, 2]
        assert c["isomorphic_to_K"] is True
    assert r["all_isomorphic_to_K"] is True and r["L138_fires"] is True


def test_the_scope_limit_is_stated_up_front():
    """An orbit is not a point -- this must never be quoted without it."""
    r = _res()
    assert "ORBITS" in r["THE_SCOPE_LIMIT"]
    assert "NOT hand the programme a canonical VEV" in r["THE_SCOPE_LIMIT"]
    assert contains(CELL / "FINDINGS.md",
                    "a canonical orbit is not a canonical vev",
                    "within the orbit the choice remains free")


def test_solos_own_correction_is_banked_with_the_result():
    r = _res()
    assert "FAILS" in r["solo_correction_banked"]
    assert "no second canonical triple" in r["solo_correction_banked"]


def test_what_was_not_verified_is_listed():
    r = _res()
    assert len(r["not_verified_here"]) == 2
    assert any("L135" in x for x in r["not_verified_here"])


def test_the_Z6_ledger_row_is_corrected():
    t = (ROOT / "docs" / "SM_SPECIFICATION_LEDGER.md").read_text(encoding="utf-8")
    assert "DELIVERED — the strongest row in this table" in t
    # the Z6 row specifically must no longer say "not addressed";
    # other rows (strong CP, gravity...) legitimately still do.
    z6 = [L for L in t.splitlines() if "global **ℤ₆** form" in L]
    assert len(z6) == 1 and "not addressed" not in z6[0]
