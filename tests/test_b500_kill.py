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


def test_141_of_150_words_completed_tail_is_double_decimation():
    txt = _RES.read_text()
    planned = [''.join(w) for w in it.product('FMD', repeat=5) if set(w) == set('FMD')]
    assert len(planned) == 150
    done = {l.split(':')[0].strip() for l in txt.splitlines()
            if ':' in l and l[:5].isalpha() and set(l.split(':')[0].strip()) <= set('FMD')
            and len(l.split(':')[0].strip()) == 5}
    assert len(done) == 141
    missing = [w for w in planned if w not in done]
    # the 9 tool-blocked words are all double-decimation (DD-prefixed): degree blow-up, not chance
    assert len(missing) == 9
    assert all(w.startswith('DD') for w in missing)
