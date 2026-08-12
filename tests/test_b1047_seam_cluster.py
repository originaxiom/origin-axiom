"""B1047 locks — the seam / level-15 cluster, dispositioned from the bodies.

These lock the DISPOSITION and the MATHEMATICS behind it, not transcript literals (E6).
"""
import glob
import hashlib
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _body(bid):
    return pathlib.Path(glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))[0]
                        ).read_text(encoding="utf-8")


def _vd(bid):
    return json.loads(pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))[0]).read_text())


def _art(bid, name):
    return json.loads(pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{bid}_*" / name))[0]).read_text())


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1047_the_seam_cluster/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 79


def test_the_refuted_law_stays_refuted():
    """The one outcome a consolidation pass must never produce is restoring a refuted claim."""
    assert _vd("B367")["supersedes"] == "B361"
    assert "the local law (B361) is REFUTED at pair (3,4)" in _body("B367")
    lm = re.sub(r"\s+", " ", _read("docs/LAW_MAP.md"))
    # B1047's row may NAME B361 -- it must name it as refuted, and must not restore it.
    assert "B361/B362's" in lm and "is REFUTED at the twelfth pair by B367" in lm


def test_the_doubly_elliptic_arithmetic__recomputed_not_cited():
    """disc(A_m) = m^4+4m^2; the seed is elliptic at p iff disc is a non-residue mod p."""
    def leg(a, p):
        a %= p
        return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)

    def ell(m, p):
        return leg(m ** 4 + 4 * m ** 2, p) == -1

    assert [m for m in range(1, 9) if ell(m, 3) and ell(m, 5)] == [2, 7, 8]
    # the counterexample: (3,4) has no qualifier, (1,3) covers the two primes identically
    assert not (ell(3, 3) and ell(3, 5)) and not (ell(4, 3) and ell(4, 5))
    cover = lambda pr: (any(ell(m, 3) for m in pr), any(ell(m, 5) for m in pr))
    assert cover((1, 3)) == cover((3, 4)) == (True, True)


def test_the_exact_table_makes_3_4_bright_and_1_3_dark():
    s2 = _art("B367", "step0_report.json")["S0_7_sum_s_squared"]
    assert s2["3,4"] == "1/192" and s2["1,3"] == "0" and s2["1,4"] == "0"


def test_the_restored_law_is_the_stratification():
    PF = _art("B393", "product_fields.json")
    dark = {"1,3", "1,4", "3,5"}
    for k, v in PF.items():
        assert (v["s-carrying"] == 0) == (k in dark), (k, v)
        assert v["zero"] == 0, k          # annihilation is field membership, not vanishing
    assert PF["1,4"]["real(x,y)"] == 39 and PF["1,3"]["z-only"] == 24
    assert _art("B410", "b2ii_fullfield.json")["separates"] is True


def test_k1_termwise_is_a_negative_artifact():
    """The rider that must never be dropped: the broken per-side run reads ZERO on the BRIGHT
    controls. If this ever starts agreeing with the full-field run, the erratum needs re-reading."""
    KT, KF = _art("B393", "k1_termwise.json"), _art("B393", "k1_fullfield.json")
    for pair in ("3,4", "2,3"):
        assert KT[pair]["status"] == "bright" and KT[pair]["nonzero_terms"] == 0
        assert KF[pair]["nonzero_terms"] > 0
    assert KT["3,4"]["terms"] != KF["3,4"]["terms"]


def test_b410s_named_generator_is_absent_and_its_json_is_not_a_copy():
    """The provenance defect (L165), with the plan's explanation of it corrected."""
    assert not list(ROOT.glob("**/b2ii_fullfield.py"))
    f410 = glob.glob(str(ROOT / "frontier" / "B410_*" / "b2ii_fullfield.json"))[0]
    f393 = glob.glob(str(ROOT / "frontier" / "B393_*" / "k1_fullfield.json"))[0]
    sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
    assert sha(f410) != sha(f393)          # NOT a byte copy -- a derived summary
    FF, KF = json.loads(open(f410).read()), json.loads(open(f393).read())
    assert all(FF["fullfield_scounts"][k] == KF[k]["nonzero_terms"]
               for k in FF["fullfield_scounts"])


def test_the_dependency_chain_is_present():
    """B393 is not self-contained; a restoration that assumed it was would not re-verify."""
    for p in ("frontier/B358_seam_certification/cyclo_engine.py",
              "frontier/B358_seam_certification/seam_certification.py",
              "frontier/B367_value_map/step0_exact_matrices.py",
              "frontier/B386_crt_closed_form/tensor_gate.py"):
        assert (ROOT / p).is_file(), p


def test_the_cluster_stays_firewalled():
    claims = _read("CLAIMS.md")
    for b in ("B359", "B360", "B361", "B362", "B367", "B393", "B410"):
        assert not re.search(rf"\b{b}\b", claims), b


def test_the_supersessions_backlog_number_matches_the_instrument():
    """B1046 published 21 load-bearing when its own instrument said 26, and its locks pinned the
    dispositions rather than the counts. This is that hole closed."""
    import sys
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import supersession as S
    reg = _read("docs/consolidation/SUPERSESSIONS.md")
    lb = S.load_bearing()
    assert f"{len(lb)} are load-bearing" in reg, len(lb)
    assert f"remaining **{len(S.candidates()) - len(lb)}**" in reg
    assert S.sweep() == []


def test_L165_the_three_promoted_arcs_are_three_different_things():
    """The draft said "none of the 15 sits under a CLAIMS.md promotion". Three do — missed by a
    bare-id grep because CLAIMS.md cites evidence BY PATH. Locked so the distinction survives:
    B156's absent script is one B156 itself refuted, B877 discloses its own gap, and B379 is the
    real one — no code in the arc directory at all."""
    claims = _read("CLAIMS.md")
    for arc in ("B156", "B379", "B877"):
        assert f"frontier/{arc}_" in claims, arc
    assert "over-counts" in re.sub(r"\s+", " ", _body("B156"))
    assert len(list(ROOT.glob("frontier/B156_*/*.py"))) >= 6
    assert "Manifest gap" in _body("B877")
    assert list(ROOT.glob("frontier/B379_*/*.py")) == []
    assert "Reproducer: `reduction_verification.py`" in _body("B379")
    assert not list(ROOT.glob("**/reduction_verification.py"))


def test_law_siblings_coverage_is_measured_not_typed():
    """Step 3: the fingerprint for B1029's row, and the coverage number checked against the file
    rather than remembered. B1046's stale '21' is why this is a lock and not a sentence."""
    import sys
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import law_siblings as LS
    reg = _read("docs/consolidation/LAW_SIBLINGS.md")
    assert "the seam is the ends' class field (B1029)" in LS.FINGERPRINTS
    assert "the seam's darkness is termwise (B1047)" in LS.FINGERPRINTS
    # ANCHORED ON THE ROW, NOT THE CELL SHAPE. A first version demanded the literal "| **150** |"
    # and broke the moment B1048 annotated the cell with its provenance -- a lock that forbids
    # improving the prose is a lock on the wrong thing. What must hold is that the number stated
    # beside each label IS the number the instrument produces.
    def _cell(label):
        rows = [ln for ln in reg.splitlines() if label in ln]
        assert len(rows) == 1, (label, len(rows))
        return rows[0]

    assert f"**{len(LS.FINGERPRINTS)}**" in _cell("fingerprints in `FINGERPRINTS`")
    lm = [ln for ln in _read("docs/LAW_MAP.md").splitlines()
          if ln.startswith("|") and not re.match(r"^\|[\s:-]+\|", ln)]
    five = [ln for ln in lm if ln.count("|") >= 5]
    assert f"**{len(five)}**" in _cell("five-column law tables"), len(five)
    fed = [ln for ln in five if len(set(re.findall(r"\bB\d+\b", ln))) >= 5]
    assert f"**{len(fed)}**" in _cell("the *campaign-fed* rows"), len(fed)
    assert LS.sweep() == []
