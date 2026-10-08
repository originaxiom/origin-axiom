"""B1620 -- THE BREAKING THE WEAVE ALLOWS: the sealed instrument unchanged and its cells as banked; the post-seal checks
(abelian iff three distinct masses; no family below four reaches the CKM; two for the PMNS; the residuals containing the
inner automorphisms give permutations under all three tensors); B1618's odd-weight addendum."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1620_the_breaking_the_weave_allows"
V = ARC / "verification"
PHI6 = ((1 + 5 ** 0.5) / 2) ** 6


def test_sealed_and_part_A():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at aa28a42e6: ")
    assert hashlib.sha256(open(V / "breaking_the_weave_allows.py", "rb").read()).hexdigest() == first.split()[4]
    A = json.load(open(V / "breaking_the_weave_allows.json"))["A"]
    assert A["number_of_subgroups"] == 68 and A["number_of_conjugacy_classes"] == 26
    assert A["subgroup_classes_allowing_three_distinct_masses"] == 20 and A["max_order_with_three_distinct_masses"] == 16
    assert all(c["free_complex_mass_couplings"] >= 3 for c in A["classes"] if c["three_distinct_masses"])


def test_part_B_the_rule_outside_the_weave():
    B = json.load(open(V / "breaking_the_weave_allows.json"))["B"]
    assert all(abs(f - 0.25) < 1e-3 for f in B["B1_class_frequencies"].values())
    ch = B["B2_characters"]
    assert ch["(-1)^(A+B)"]["max_abs_partial_sum"] <= 1                       # the clock's parity: word-blind, bounded
    for k in ("(-1)^A", "(-1)^B"):
        assert ch[k]["max_abs_partial_sum"] >= 12                            # the letter-reading walks grow
        r = ch[k]["ratios_of_successive_record_positions"]
        assert abs(r[-1] * r[-2] - PHI6) < 1e-2                              # two records per factor phi^6
    a = ch["(-1)^A"]["record_values_and_first_positions"]; b = ch["(-1)^B"]["record_values_and_first_positions"]
    assert abs(b["11"] / a["11"] - (1 + 5 ** 0.5) / 2) < 1e-4                # the b-walk is the a-walk inflated by phi
    cyc = [tuple(v) for _, v in sorted(B["B3_class_at_fibonacci_lengths"].items(), key=lambda kv: int(kv[0]))]
    assert set(cyc) == {(1, 0), (1, 1), (0, 1)} and all(cyc[i] == cyc[i + 3] for i in range(len(cyc) - 3))


def test_post_seal_pairs_and_inner():
    d = json.load(open(V / "post_seal_pairs.json"))
    assert d["P1"]["sum_of_characters_iff_abelian"] and d["P1"]["abelian"] == 57
    assert d["P3"]["ckm_min_family_dim_reaching_data"] == 4 and not d["P3"]["ckm_block_passes_below_4"]
    assert d["P3"]["pmns_min_family_dim_reaching_data"] == 2
    assert d["P4"]["fixed_patterns_include_B1612s"]
    inner = json.load(open(V / "post_seal_inner.json"))
    assert inner["I1"]["order_K"] == 4 and inner["I1"]["T_on_K_piece_dims"] == [1, 1, 1]
    for t in ("Tbar_x_T", "T_x_T", "Sym2_T"):
        assert inner[t]["family_dims"] == [0] and inner[t]["every_pattern_a_permutation"]


def test_post_seal_three_tensors():
    d = json.load(open(V / "post_seal_tensors.json"))
    expect = {"Tbar_x_T": (57, 4, 2), "T_x_T": (24, 4, 2), "Sym2_T": (16, 4, 4)}
    for t, (nv, ck, pm) in expect.items():
        v = d[t]
        assert v["P1"]["viable_subgroups"] == nv and v["P1"]["viable_all_abelian"] and v["block_sums_shared_by_family"]
        assert v["ckm_min_family_dim_reaching_data"] == ck and not v["ckm_fits_below_4"]   # the 13 unreduced, every tensor
        assert v["pmns_min_family_dim_reaching_data"] == pm
    assert 3 not in d["Sym2_T"]["P1"]["viable_orders"]                       # no order-3 residual: no TM1 under Sym^2 T
    # bite: the tally holds fixed families (dimension 0) and full ones (4), so the rank can fail both ways
    tally = d["Tbar_x_T"]["tally_(family_dim,ckm_block,pmns_block)"]
    assert tally["(0, False, False)"] > 0 and tally["(4, True, True)"] > 0


def test_b1618_odd_weight_addendum():
    o = json.load(open(ROOT / "frontier" / "B1618_the_weighted_cell_at_omega" / "verification" / "post_seal_odd_weight.json"))
    assert o["inner_fixed_dim_in_Sym2T"] == 3 and o["every_omega_spectrum_degenerate_or_zero"]
    assert [c["iota_eigenvalue"] for c in o["cells"]] == [[-1.0, 0.0]] and o["cells"][0]["dim"] == 3


def test_genesis_v1_35_tau_omega_retired_and_the_write_up():
    import subprocess, sys
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 35                    # a lower bound (E86): later amendments may follow
    assert "τ = ω RETIRED AS TESTED" in g and "THE BREAKING THE WEAVE ALLOWS (B1620, PROVED)" in g
    r = subprocess.run([sys.executable, str(ARC / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    w = open(ROOT / "docs" / "THE_DERIVED_STRUCTURE_FOR_REVIEW.md", encoding="utf-8").read()
    assert "0 of 19" in w and "reduces none of the 13" in w and "P10" in w
