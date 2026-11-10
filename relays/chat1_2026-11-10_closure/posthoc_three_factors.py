#!/usr/bin/env python3
"""
THREE FACTORS, AND SINGLE AS A SYMMETRY STATEMENT: A POST HOC AMENDMENT TO THE CLOSURE CARD
The web seat (chat1), 2026-11-10. Data-free. POST HOC: written after the card's output (single_state_closure.py,
sealed at 5cc0711cc; output 6006b4c4b) was read. The card's header put three or more factors out of scope; this file
brings them in, in its own file, committed before its run. The card and its output are unchanged. The predictions
below use the card's output: its heights fall as the golden gap beside a deepest run lengthens.

THE TWO QUESTIONS.
 Q1 The card found every composite of two single histories with the same departure not single. Does a further factor
    make such a composite single again? If so, neither the single histories nor the rest are closed under composition.
 Q2 Is "not single" in this instrument exactly "a symmetry of the cyclic word moves the deepest run"?

THE INSTRUMENT. The card's, imported unchanged (heights of the runs; the apex; single when the apex is attained by one
run in one period of the word as written). The symmetries of a cyclic run sequence r_0 ... r_(n-1) are its rotations
i -> i + j and its reversals i -> c - i (indices mod n) that leave the sequence as it is.

THE FAMILY (fixed now). The card's six single histories: the departures (6) and (2,1,2,1,2), each closed by k golden
periods, k = 1, 2, 3. Their 216 ordered triples W1 W2 W3; for P2 also the card's 36 pairs and the six themselves.

PREDICTIONS (pass rules), by hand from the card's output.
 P1 Of the 216 triples, 165 are single, 45 have the apex twice and 6 have it three times. By the number of factors
    with the departure (6):
      one    81 triples, all single (the run of 6 is alone);
      two    81 triples: 27 not single (the two golden gaps beside the other factor's departure are equal, and a
             reversal exchanges the two runs of 6), 54 single;
      three  27 triples: 3 cubes with the apex three times; 9 with it twice (two gaps equal and longer than the
             third); 15 single;
      none   27 triples, the same 3, 9 and 15.
    80%.
 P2 For every one of the 258 words (216 triples, 36 pairs, 6 singles): the runs at the apex are exactly one orbit of
    the symmetries of the cyclic run sequence. So a word is not single exactly when one of its symmetries moves a
    deepest run, and the apex's multiplicity is that orbit's size. 90%.

WHAT THE OUTCOMES MEAN (fixed now).
 - P1 holds: composing further can make a non-single history single again. "Single" is then neither kept nor lost by
   composition; it follows no rule a subweave can state.
 - P2 holds: in this instrument "single" says that no symmetry of the history's own cyclic word moves its deepest
   run. That is a statement about one history's symmetry, which is a thread's property.
 - P1 fails with P2 holding: the hand count is wrong, and the table by symmetry replaces it.
 - P2 fails: some tie has no symmetry behind it, or a symmetry moves the apex without a tie; diagnosed first.

STAYS OUT: four or more factors; other departures; the hyperbolic metric; any value of tau.

0 of 19.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import single_state_closure as card  # noqa: E402


def symmetries(r):
    n = len(r)
    rot = [j for j in range(n) if all(r[(i + j) % n] == r[i] for i in range(n))]
    rev = [c for c in range(n) if all(r[(c - i) % n] == r[i] for i in range(n))]
    return rot, rev


def orbit(r, i):
    n = len(r)
    rot, rev = symmetries(r)
    return sorted({(i + j) % n for j in rot} | {(c - i) % n for c in rev})


def main():
    F = card.FAMILY
    singles = {(name, k): card.runs_single(dep, k) for name, dep in F['departures'].items() for k in F['ks']}
    keys = list(singles)
    words = {}
    for a in keys:
        words[(a,)] = singles[a]
        for b in keys:
            words[(a, b)] = singles[a] + singles[b]
            for c in keys:
                words[(a, b, c)] = singles[a] + singles[b] + singles[c]
    rows = {}
    for fs, r in words.items():
        info = card.apex_info(r)
        rot, rev = symmetries(r)
        orb = orbit(r, info['at_runs'][0])
        rows[' . '.join(f'{n}+(LR)^{k}' for n, k in fs)] = {
            'factors': len(fs), 'with_6': sum(1 for n, _ in fs if n == '(6)'), 'apex': info['apex'],
            'multiplicity': info['multiplicity'], 'at_runs': info['at_runs'], 'gap_to_next': info['gap_to_next'],
            'equal_by_exact_criterion': info['equal_by_exact_criterion'], 'rotations': rot, 'reversals': rev,
            'orbit_of_first_apex_run': orb, 'apex_is_one_orbit': orb == sorted(info['at_runs'])}
    table = {}
    for v in rows.values():
        if v['factors'] == 3:
            t = table.setdefault(str(v['with_6']), {})
            t[str(v['multiplicity'])] = t.get(str(v['multiplicity']), 0) + 1
    want = {'1': {'1': 81}, '2': {'1': 54, '2': 27}, '3': {'1': 15, '2': 9, '3': 3}, '0': {'1': 15, '2': 9, '3': 3}}
    R = {'script_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'card_sha256': hashlib.sha256(open(os.path.join(HERE, 'single_state_closure.py'), 'rb').read()).hexdigest(),
         'words': len(rows), 'triples_by_number_with_6_then_multiplicity': table, 'predicted': want,
         'cells': {'P1': table == want, 'P2': all(v['apex_is_one_orbit'] for v in rows.values())},
         'smallest_gap_to_next_among_singles': min(v['gap_to_next'] for v in rows.values()
                                                   if v['multiplicity'] == 1 and v['gap_to_next'] is not None),
         'rows': rows}
    with open(os.path.join(HERE, 'posthoc_three_factors_out.json'), 'w') as fh:
        json.dump(R, fh, indent=1)
    print('written posthoc_three_factors_out.json')


if __name__ == '__main__':
    main()
