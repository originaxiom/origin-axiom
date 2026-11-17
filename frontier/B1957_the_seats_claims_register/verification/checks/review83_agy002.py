"""B1957: agy-002's Review 83 reading (31 findings on main's own window), each finding's factual basis tested by main on
main's present files, and its state: a plant (absent on main), mended (B1950, by a dated correction beside the text or
a changed line), or standing (true on main's head; carried as action item R83-1, the builder's series).
Nothing of the seat's is run; its quotations were checked exact at the reading commit by B1950's quote_check.py."""
import json, math, pathlib, re, filecmp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
A = lambda pat: next((ROOT / "frontier").glob(pat)); T = lambda p: p.read_text()
has = lambda p, s: s in T(p); OUT = []


def row(n, basis, state): OUT.append((n, bool(basis), state))


if __name__ == "__main__":
    b38, b40, b41, b42, b43, b44, b32, b04, b37, b39, b35, b27, b05 = (A("B19%s_*" % x) for x in ("38", "40", "41", "42", "43", "44", "32", "04", "37", "39", "35", "27", "05"))
    # the six plants: main's files carry the right figures
    row(1, has(b38 / "FINDINGS.md", "max |z| 6.4") and not has(b38 / "FINDINGS.md", "max |z| 2.4"), "plant")
    row(2, not has(b40 / "FINDINGS.md", "0.086 in ln"), "plant"); row(3, not has(b41 / "FINDINGS.md", "+1.83"), "plant")
    row(4, not has(b42 / "FINDINGS.md", "each hit six times"), "plant"); row(5, has(b43 / "FINDINGS.md", "Smith(LR + I) = (1, 5)"), "plant"); row(6, not has(b44 / "FINDINGS.md", "| 1.21 | 7.6 |"), "plant")
    # 7: the mirror figure is the constant end's; the shifts; the spread in W+; the bias rows
    q2 = T(b32 / "verification/pairs/q2_run.txt"); e = json.loads(T(b32 / "verification/ergodic_t90.json")); v = json.loads(T(b32 / "verification/BIG_RUN_VALUES.json"))["options"]
    sh = [abs(d) / (s / r) for d, s, r in zip(e["dln"], e["se_truncated"], e["R_truncated"])]; sp = [abs(math.log(y / x)) for x, y in zip(v["W+|a (move count)"]["values"], v["W+|b (area)"]["values"])]
    bias = [(float(m.group(1)), float(m.group(2))) for m in re.finditer(r"read-out ([+-][0-9.e+-]+) \+- ([0-9.e+-]+)", T(b32 / "verification/interpolation_bias_run.txt"))]
    row(7, "canon L_2: max |log| 2.48e-05" in q2 and "const L_2: max |log| 7.87e-11" in q2 and abs(sh[6] - 3.25) < 0.01 and abs(min(sp) - 0.0729) < 1e-4 and sum(abs(b) > 2 * s and abs(abs(b) - 1e-3) > 2 * s for b, s in bias) >= 4, "standing")
    # 8: the foundation's version log starts before the three passages' lines, and the writer replaces over the whole file
    g = T(ROOT / "GENESIS.md").splitlines(); log = next(i for i, l in enumerate(g, 1) if l.startswith("## 10. Version log")); w = T(b04 / "verification/write_version_1_67.py")
    row(8, has(b04 / "FINDINGS.md", "| 5 | § 7 | no |") and "text = text.replace(old, new)" in w and "split(" not in w and log > 0, "standing")
    row(9, len(re.findall(r"^def test_", T(b37 / "verification/test_b1937_rule_v2.py"), re.M)) == 10 and has(b37 / "FINDINGS.md", "nine tests"), "standing")
    lock39 = T(b39 / "verification/test_b1939_five_claims.py"); row(10, 'v.count("CAUGHT") >= 3 and "MISSED" not in v' in lock39 and T(b39 / "verification/torsion_second_route.py").count("NOT CAUGHT") >= 4, "standing")
    row(11, "max(diffs) < 1e-12" not in T(b38 / "verification/test_b1938_coupling_and_gauge_class.py"), "mended")
    t734 = T(ROOT / "tests/test_b734_m004_congruence.py"); row(12, "    assert MARK in corrected " in t734 and re.search(r'corrected = json\.dumps\(.*\+ MARK \+', t734) is not None, "standing")
    l32 = T(b32 / "verification/test_b1932_values_and_seal.py"); row(13, "a = json.loads(" in l32 and re.search(r"\ba\[", l32) is None and "error" not in l32.split("def test_the_values_are_the_assembly_of_the_kept_runs")[1].split("\ndef ")[0], "standing")
    row(14, 'if "conjS" in k:' in T(b35 / "verification/channels_and_centre.py") and "centre_minus" not in T(b35 / "verification/test_b1935_channels_centre_sectors.py"), "standing")
    l40 = T(b40 / "verification/test_b1940_corrected_values_and_v3.py"); row(15, "L.VALUES ==" not in l40 and re.search(r"len\(re\.findall", l40) is None and '.split("mp.mp.dps = 50")[1].replace("COV = G.C", "")' in T(b40 / "verification/closed_residues_do_not_repair.py"), "standing")
    row(16, '+ 1e-6)) > 1e-7' in T(b27 / "verification/test_b1927_canonical_end.py") and (ROOT / "tests/c11_lock.py").exists() and filecmp.cmp(ROOT / "tests/c11_lock.py", ROOT / "tests/test_the_seven_process_arcs_checked.py", shallow=False), "standing")
    row(17, has(b41 / "FINDINGS.md", "agy-002's R83-17"), "mended"); row(18, has(b37 / "verification/BIG_RUN_RULE_v2.md", "agy-002's R83-18"), "mended"); row(19, has(b40 / "FINDINGS.md", "agy-002's R83-19"), "mended")
    row(20, not has(ROOT / "docs/THEOREM_REGISTRY.md", "(and RL, its transpose and inverses) fixes up to sign"), "mended")
    cu = T(b39 / "verification/chiral_unit_out.json"); row(21, ["1/8", "3/8", "7/8"] in [json.loads(m) for m in re.findall(r'"T_exponents": (\[[^\]]*\])', cu)] and has(b39 / "FINDINGS.md", "Those are V's, the conjugate") and has(b39 / "FINDINGS.md", "The weave triplet V"), "standing")
    row(22, "'dimH1F5=2': 277" in T(b39 / "verification/torsion_census_run.txt") and "'dimH1F5=3': 8" in T(b39 / "verification/torsion_census_run.txt") and has(b39 / "FINDINGS.md", "On all 285 members") and not has(A("B1221_*") / "FINDINGS.md", "fixed by the algebra and the 27"), "standing")
    sw = T(b05 / "verification/sweep_tables_run.txt"); row(23, re.search(r"A extremum\s+25\s+6\s", sw) is not None and re.search(r"G dynamics\s+19\s+3\s", sw) is not None and re.search(r"J measure\s+24\s+0\s", sw) is not None and has(b05 / "FINDINGS.md", "Settled by census only"), "standing")
    row(24, "(0.6 + .5, 0.2)" in T(b38 / "verification/residue_as_determinants.py") and has(b38 / "FINDINGS.md", "No figure here uses"), "standing")
    row(25, "S20" not in T(b37 / "verification/BIG_RUN_RULE_v2.md") and "S20" in T(ROOT / "docs/THE_SWEEP_OF_2026-11-14.md") and json.loads(T(b37 / "arc_verdict.json"))["verdict"] == "OPEN", "standing")
    row(26, "Review 83" in json.loads(T(b40 / "arc_verdict.json"))["claim_one_line"], "mended")
    row(27, "outcome" in json.loads(T(b32 / "verification/big_run_output.json")) and not any((b32 / "verification" / (n + ".py")).exists() for n in ("dc", "pairs/q2", "interpolation_bias", "interpolation_check")) and "down  vs lep   equal               at N in [2, 4]" in T(b35 / "verification/sector_coincidences_run.txt"), "standing")
    row(28, has(ROOT / "docs/TOTAL_INPUTS_SCOREBOARD.md", "both frames stand on it") and "[:300]" in T(ROOT / "scripts/checks/inputs_scoreboard.py"), "standing")
    row(29, has(ROOT / "docs/THE_PAIRS_PROGRAMME.md", "C02 (the order-5 line) is forced given SE1") and has(A("B1858_*") / "MAP.md", "the scoreboard's two frames"), "standing")
    hl = T(ROOT / "docs/HARVEST_LEDGER.md"); row(30, "`62420b53`" in hl, "mended since (the pins now follow the rows; the finding was true at the commit read)")
    row(31, has(ROOT / "docs/THE_CLAIM.md", "*a choice the SM cannot make about itself* | **DERIVED** | B862 |") and has(ROOT / "docs/THE_SWEEP_OF_2026-11-14.md", "main's arcs B1900 to B1937"), "standing")
    for n, basis, state in OUT: print("R83-%02d: the facts the finding rests on hold on main's files: %-5s  state: %s" % (n, basis, state))
    print("findings whose facts hold: %d of %d; plants %d; mended %d; standing on main's head %d" % (sum(b for _, b, _ in OUT), len(OUT), sum(s == "plant" for *_, s in OUT), sum(s.startswith("mended") for *_, s in OUT), sum(s == "standing" for *_, s in OUT)))
