"""B1237 -- the physics-seat harvest, second ring (R31-R38 + the W-D synthesis), every correction
recomputed here. These locks pin the corrections where they LIVE (the corrected arcs' own files),
which is the E53 lesson the cell exists for: a correction that reaches only the log is not banked.
"""
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1237_physics_seat_r31_r38_harvest"
VER = ARC / "verification"


def _verdict(d):
    return json.loads((ROOT / "frontier" / d / "arc_verdict.json").read_text(encoding="utf-8"))


def test_the_cell_is_sealed_and_declares_no_identification():
    d = _verdict("B1237_physics_seat_r31_r38_harvest")
    assert d["verdict"] == "PROVED" and d["identifications"] == []
    assert "SILVER IS ARITHMETIC" in d["claim_one_line"]
    assert (ARC / "FINDINGS.md").is_file() and (VER / "reproduce.sh").is_file()


def test_c42_witness_recomputes_from_committed_b1236():
    """The 3/8 traces from B1236's committed multiplet content -- no HANDOFF6_RUN, no cw.py."""
    br = ROOT / "frontier" / "B1236_a1_landing_exact" / "verification" / "a1_su6_branching.py"
    r = subprocess.run([sys.executable, str(VER / "traces_from_b1236.py"), str(br)],
                       capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Tr(T3^2) = 3  Tr(Y^2) = 5  Tr(T3.Y) = 0" in r.stdout
    assert "C42 WITNESSED FROM COMMITTED B1236: True" in r.stdout


def test_b919_runner_is_recorded_as_unreproducible_from_the_repo():
    d = _verdict("B919_weinberg_traces")
    assert d["verdict"] == "PROVED"
    assert "cw.py" in (d.get("note") or "") and "B1237" in (d.get("note") or "")
    assert (ROOT / "frontier" / "B919_weinberg_traces" / "ADDENDUM_2026-09-02_B1237.md").is_file()


def test_silver_arithmetic_is_banked_in_the_output_and_in_both_arcs():
    out = (VER / "silver_arithmetic.txt").read_text(encoding="utf-8")
    assert "SILVER ARITHMETIC (invariant field Q(i), integral invariant traces, Bianchi volume ratio 12): True" in out
    assert "Vol(m136) = 3.66386237670887606021841405972953644309659749712668853706599" in out
    for arc in ("B1062_bridge_cell", "B258_two_ended_unification"):
        d = _verdict(arc)
        assert d["verdict"] == "PROVED"
        assert "arithmetic" in (d.get("note") or "").lower() and "B1237" in (d.get("note") or "")
        assert (ROOT / "frontier" / arc / "ADDENDUM_2026-09-02_B1237.md").is_file()
    assert _verdict("B1062_bridge_cell")["claim_one_line"].startswith("CORRECTED 2026-09-02 (B1237)")


def test_e53_at_verdict_file_grain_is_propagated():
    b361 = _verdict("B361_seam_local_law")
    assert b361["superseded_by"] == "B367" and b361["claim_one_line"].startswith("SUPERSEDED")
    assert b361["verdict"] == "PROVED"                      # the 8-pair fact holds; RETRACTED is for one's own headline (B818)
    b259 = _verdict("B259_gravity_brick_wall_map")
    assert "B980" in (b259.get("note") or "") and "wall #5" in (b259.get("note") or "")
    b892 = _verdict("B892_second_measurement")
    assert "12" in (b892.get("note") or "") and "B950" in (b892.get("note") or "")
    for arc in ("B361_seam_local_law", "B259_gravity_brick_wall_map", "B892_second_measurement"):
        assert (ROOT / "frontier" / arc / "ADDENDUM_2026-09-02_B1237.md").is_file()


def test_three_negatives_numbers_corrected_verdicts_unchanged():
    for arc, frag in (("B850_length_spectrum_type", "m004 | **12**"),
                      ("B333_compositum_seam", "**122**"),
                      ("B213_higgs_side_periods", "2-isogenous to 40a1, not 40a1")):
        assert _verdict(arc)["verdict"] == "NEGATIVE"
        assert frag in (ROOT / "frontier" / arc / "ADDENDUM_2026-09-02_B1237.md").read_text(encoding="utf-8")
    assert "h=2 list: [-15, -20, -24, -35, -40, -51, -52, -88, -91, -115, -123, -148, -187, -232, -235, -267]" in \
        (VER / "b333_fundamental_discriminants.txt").read_text(encoding="utf-8")
    assert "Phi's member is in the class: True | isomorphic to 40a1: False" in \
        (VER / "b213_isogeny_class.txt").read_text(encoding="utf-8")


def test_kill_graph_carries_the_two_e55_rows():
    k = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    ids = {e["id"] for e in k}
    assert {"B258-silver-inference", "B1062-V2-axis"} <= ids


def test_ledgers_carry_e55_l197_and_the_c42_pointer():
    err = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "| E55" in err and "invariant trace field" in err
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "## L197" in leads and "REPRODUCES" in leads
    tl = (ROOT / "docs" / "THEOREM_LEDGER.md").read_text(encoding="utf-8")
    c42 = tl[tl.index("**C42 ["):]
    c42 = c42[:c42.index("**C43 [")] if "**C43 [" in c42 else c42[:1200]
    assert "B1237" in c42 and "traces_from_b1236.py" in c42
