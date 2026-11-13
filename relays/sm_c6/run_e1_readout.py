#!/usr/bin/env python3
"""SM-C6 E1, the owed step 3: the read-out on the whole (B1881, B1895), through main's own instrument, imported unchanged
from a checkout of main (first argument): heights(runs) and keeps_line_seat/keeps_line_main of
frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py.
Question (card relays/cards/SM_C6_E1_the-based-count.md, step 3): does the read-out keep the letters' order (a word
against its reverse), and is there an input through which the pieces' order can reach it?
Only equalities and counts are recorded; no height value is written or compared with anything.
Plant P: a read-out weighted to the forward reading, (r_i + 2 x_i + y_i)/2, must tell some word from its reverse.
    python3 run_e1_readout.py MAIN_CHECKOUT [out.json]"""
import sys, json, inspect, itertools, importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
F = MAIN / "frontier" / "B1881_the_whole_and_the_value_verified" / "verification" / "whole_and_value_on_main.py"
spec = importlib.util.spec_from_file_location("whole", F); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
mp = W.mp
mp.mp.dps = 50
EPS = mp.mpf(10) ** -40


def rev_word(runs):
    """the reverse word as a run sequence that starts with an L-run (even length: reverse, then rotate by one)"""
    r = list(reversed(runs))
    return r[1:] + r[:1]


def plant_heights(runs):
    n = len(runs); out = []
    for i in range(n):
        fwd = [runs[(i + 1 + k) % n] for k in range(n)]
        bwd = [runs[(i - 1 - k) % n] for k in range(n)]
        out.append((runs[i] + 2 / W.cf_value(fwd) + 1 / W.cf_value(bwd)) / 2)
    return out


def same_multiset(a, b):
    a, b = sorted(a), sorted(b)
    return all(abs(x - y) < EPS for x, y in zip(a, b))


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "e1_readout_results.json"
    seqs = [list(s) for n in (2, 4, 6) for s in itertools.product(range(1, 6), repeat=n)]
    c = {"sequences": len(seqs), "palindromic_up_to_rotation": 0, "heights_same_as_reverse": 0, "apex_same_as_reverse": 0,
         "keeps_line_same_as_reverse_seat": 0, "keeps_line_same_as_reverse_main": 0, "keeps_line_seat_eq_main": 0,
         "keeps_line_constant_on_letter_keeping_rotations": 0, "plant_tells_some_word_from_its_reverse": 0}
    for s in seqs:
        r = rev_word(s)
        rots = [s[i:] + s[:i] for i in range(0, len(s), 2)]
        c["palindromic_up_to_rotation"] += r in rots
        hs, hr = W.heights(s), W.heights(r)
        c["heights_same_as_reverse"] += same_multiset(hs, hr)
        c["apex_same_as_reverse"] += abs(max(hs) - max(hr)) < EPS
        c["keeps_line_same_as_reverse_seat"] += W.keeps_line_seat(s) == W.keeps_line_seat(r)
        c["keeps_line_same_as_reverse_main"] += W.keeps_line_main(s) == W.keeps_line_main(r)
        c["keeps_line_seat_eq_main"] += W.keeps_line_seat(s) == W.keeps_line_main(s)
        c["keeps_line_constant_on_letter_keeping_rotations"] += len({W.keeps_line_seat(x) for x in rots}) == 1
        c["plant_tells_some_word_from_its_reverse"] += not same_multiset(plant_heights(s), plant_heights(r))
    sig = {name: str(inspect.signature(getattr(W, name))) for name in ("heights", "keeps_line_seat", "keeps_line_main")}
    res = {"instrument": "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py (main)",
           "counts": c, "signatures": sig,
           "pieces_order_input": "none: every function of the read-out takes a run sequence only; no module or count enters",
           "summary": {"letters_order_dropped_by_heights": c["heights_same_as_reverse"] == c["sequences"],
                       "line_keeping_reversal_invariant_seat": c["keeps_line_same_as_reverse_seat"] == c["sequences"],
                       "plant_fires": c["plant_tells_some_word_from_its_reverse"] > 0}}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
