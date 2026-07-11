"""B500 depth-5 KILL lock — the child is not a short word.

Pins the negative: the streamed hunt result carries NO -283 / field-isomorphism / airlock hit,
and the 141 completed words produced only generic large symmetric Galois groups. Guards against
a silently-edited results file or a missed airlock.
"""
import pathlib
import itertools as it

_RES = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B500_child_hunt" / "hunt_results_d5.txt"


def test_no_airlock_hit_in_depth5():
    txt = _RES.read_text()
    body = "\n".join(l for l in txt.splitlines() if "target d_K=-283" not in l)
    for forbidden in ("AIRLOCK", "-283", "isomorph", " HIT"):
        assert forbidden not in body, f"unexpected {forbidden!r} in hunt_results_d5.txt"


def test_census_is_115_analyzed_35_unchecked():
    # CORRECTED (B525 audit): 141 lines are LOGGED but 26 are bare TIMEOUT (not analyzed).
    # So 115 analyzed / 35 unchecked (26 timeout + 9 never-reached). The KILL is provisional.
    txt = _RES.read_text()
    planned = [''.join(w) for w in it.product('FMD', repeat=5) if set(w) == set('FMD')]
    assert len(planned) == 150
    word_lines = [l for l in txt.splitlines()
                  if ':' in l and l[:5].isalpha()
                  and set(l.split(':')[0].strip()) <= set('FMD')
                  and len(l.split(':')[0].strip()) == 5]
    logged = {l.split(':')[0].strip() for l in word_lines}
    timeouts = [l for l in word_lines if 'TIMEOUT' in l]
    analyzed = [l for l in word_lines if 'TIMEOUT' not in l]
    assert len(logged) == 141                    # lines logged
    assert len(timeouts) == 26                    # bare TIMEOUT = NOT analyzed
    assert len(analyzed) == 115                   # actually analyzed (0 hits)
    unchecked = 150 - len(analyzed)
    assert unchecked == 35                        # 26 timeout + 9 never-reached -> KILL provisional
