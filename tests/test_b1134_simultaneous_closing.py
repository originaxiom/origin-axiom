"""B1134 lock -- THE SIMULTANEOUS CLOSING: one conjugation buys so(3,1) + compact su(3),
and all 24 hits are forced into E6(-26)=M(O,C). Verified two-bench (cloud seat's tenth memo
+ this bench's independent re-derivation). Fast tests pin b1134_results.json; the full
independent sweep (~120s) re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1134_simultaneous_closing"
RESULTS = ARC / "b1134_results.json"
CHECKSUM = {6, 2, -14, -26, -78}  # the five real forms of e6 (B1119 classification checksum)


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


def test_histogram_exact():
    d = _load()
    assert d["histogram_color_sig"] == {"4,4": 216, "0,8": 24, "5,3": 240}
    assert d["n_pairs_total"] == 480 == 216 + 240 + 24
    assert d["swappers_with_no_lift"] == 0


def test_all_24_hits_forced_to_E6_minus26():
    d = _load()
    h = d["hits"]
    assert h["n"] == 24
    assert h["chars"] == {"-26": 24}          # ALL hits at character -26 = E6(-26)=M(O,C)
    assert h["double_sigs"] == {"3,3,0": 24}  # ALL double to so(3,1)
    assert h["swaps"] == {"True": 24}         # ALL genuinely swap the triples


def test_clean_bijection_color_to_character():
    d = _load()
    # (4,4)<->+6, (5,3)<->+2, (0,8)<->-26 -- color compactness and the M(O,C) host are ONE fact
    assert d["joint_char_colorsig"] == {"+6|4,4": 216, "-26|0,8": 24, "+2|5,3": 240}


def test_characters_inside_the_classification_checksum():
    d = _load()
    seen = set()
    for k in d["joint_char_colorsig"]:
        seen.add(int(k.split("|")[0]))
    for tally in d["controls"].values():
        for k in tally:
            seen.add(int(k.split("|")[0]))
    assert seen <= CHECKSUM      # no instrument break anywhere
    assert -26 in seen           # the physical form is witnessed


def test_controls_isolate_the_simultaneous_property():
    d = _load()
    c = d["controls"]
    assert c["permute"] == {"+6|4,4|True|3,3,0": 8}   # swaps, but color (4,4) split
    assert c["mixed"] == {"+2|5,3|True|3,3,0": 8}     # swaps, but color (5,3)
    # antipodal has compact color present but NEVER together with the Lorentz swap
    assert not any(k.split("|")[1] == "0,8" and k.split("|")[2] == "True" for k in c["antipodal"])


def test_novelty_fence_20_new_4_overlap():
    d = _load()
    n = d["novelty"]
    assert n["n_distinct_hit_swappers"] == 6
    assert n["overlap_neg_pi_mirror_hits"] == 4    # already inside B1127's swept torsor
    assert n["genuinely_new_hits"] == 20           # outside both prior torsors
    assert n["overlap_neg_pi_mirror_hits"] + n["genuinely_new_hits"] == 24


def test_findings_states_theorem_and_fence():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "SIMULTANEOUS CLOSING" in f
    assert "E₆(−26)" in f and "M(𝕆,ℂ)" in f
    assert "one conjugation" in f
    assert "20 of 24" in f and "4 of 24" in f      # the novelty fence, stated honestly
    assert "Gate 5 untouched" in f


@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="full e6 slot-swapper sweep ~120s; set OA_SLOW=1 to run")
def test_full_sweep_reproduces_OA_SLOW():
    # the genuine reproduction: re-run the independent verifier end-to-end
    r = subprocess.run([sys.executable, str(ARC / "verify_simul_closing.py")],
                       cwd=str(ARC), capture_output=True, text=True, timeout=1200)
    assert r.returncode == 0, r.stderr[-3000:]
    d = _load()
    assert d["histogram_color_sig"] == {"4,4": 216, "0,8": 24, "5,3": 240}
    assert d["hits"]["chars"] == {"-26": 24}
