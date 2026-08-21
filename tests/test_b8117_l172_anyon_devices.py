"""B8117 -- locks L172's negative and the route it closes."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8117_l172_anyon_devices")
R = json.load(open(os.path.join(ARC, "results.json")))
PROSE = open(os.path.join(ARC, "FINDINGS.md")).read()


def test_the_answer_is_that_no_native_device_exists():
    assert "there is no Fibonacci-anyon device" in R["answer_one_line"]
    assert "DIGITAL SIMULATION" in R["answer_one_line"]


import re


def _identifiers(cite):
    """arXiv numbers and journal DOIs -- the tokens that survive markdown formatting.

    Journal volume/page pairs are deliberately NOT matched: the prose bolds the volume
    ('**112**, 140504'), so matching them would couple the lock to formatting rather than
    to the citation. Every source here carries an arXiv number or a DOI, so nothing escapes.
    """
    return re.findall(r"\d{4}\.\d{4,5}|s\d{5}-\d{3}-\d{5}-\w", cite)


def test_every_evidence_row_carries_a_cite_and_a_decisive_clause():
    assert len(R["evidence"]) == 4
    for e in R["evidence"]:
        assert e["cite"] and e["decisive_clause"]
        ids = _identifiers(e["cite"])
        assert ids, f"no machine-checkable identifier in {e['cite']}"
        for i in ids:
            assert i in PROSE, f"identifier {i} missing from FINDINGS.md"


def test_the_universality_result_is_S3_not_fibonacci():
    e = next(x for x in R["evidence"] if "s41586-026-10709-y" in x["cite"])
    assert "S_3" in e["what"] and "FUSION AS A COMPUTATIONAL PRIMITIVE" in e["what"]
    assert "NOT Fibonacci" in e["decisive_clause"]


def test_compilation_runs_unitary_to_braid_not_the_reverse():
    e = next(x for x in R["evidence"] if "1310.4150" in x["cite"])
    assert "OUTPUT of a compiler" in e["decisive_clause"]
    assert "never a measurement" in e["decisive_clause"]


def test_the_boundary_is_simulation_versus_realization_not_precision():
    c = R["class_named"]
    assert "SIMULATION vs REALIZATION" in c
    assert "not a precision boundary" in c


def test_it_closes_the_anyon_route_to_L179_and_names_the_survivor():
    b = R["composes_with_b8111"]
    assert "0.101910213188" in b
    assert "ANYON-DEVICE ROUTE TO L179 IS CLOSED" in b
    assert "B8094" in b  # the surviving route is named, not merely implied


def test_the_unfound_citation_is_recorded_not_dropped():
    assert "Parzanchevski-Sarnak" in R["not_found"]
    assert "NOT cited" in R["not_found"]
