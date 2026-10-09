"""B1625 -- the SM seat's corrections to B1620 are on every surface: TM2 under T(x)T, P10 under T-bar(x)T, GENESIS v1.36 (amend
--check), the theorem row, the write-up; and B1620's stored fits really fix (1/3,1/3,1/3) under T(x)T."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = ROOT / "frontier" / "B1625_the_seats_corrections_to_b1620_taken"


def test_the_stored_fits_are_tm2_under_t_tensor_t():
    d = json.loads(ROOT.joinpath("frontier", "B1620_the_breaking_the_weave_allows", "verification", "post_seal_tensors.json").read_text())
    fams = d["T_x_T"]["pmns_fits_below_4"]
    assert fams and all(sorted(round(x, 4) for x in f["block_sums"]) == [0.3333] * 3 + [0.6667] * 3 for f in fams)


def test_every_surface_carries_the_correction():
    g = ROOT.joinpath("GENESIS.md").read_text(encoding="utf-8")
    assert int(g.split("**Version 1.")[1].split()[0]) >= 36 and "[v1.36] Corrected (B1625" in g and "[v1.36] The weave's own surface" in g
    assert subprocess.run([sys.executable, str(ARC / "adoption" / "amend.py"), "--check"]).returncode == 0
    assert "**Under T ⊗ T the family is TM2**" in ROOT.joinpath("docs", "FALSIFIER_REGISTER.md").read_text(encoding="utf-8")
    assert "T ⊗ T (TM2 only)" in ROOT.joinpath("docs", "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    w = ROOT.joinpath("docs", "THE_DERIVED_STRUCTURE_FOR_REVIEW.md").read_text(encoding="utf-8")
    assert "TM2 only under T ⊗ T" in w and "exactly symmetric at every τ" not in w
    assert ROOT.joinpath("frontier", "B1620_the_breaking_the_weave_allows", "ADDENDUM_2026-10-09_the_seats_corrections.md").exists()
