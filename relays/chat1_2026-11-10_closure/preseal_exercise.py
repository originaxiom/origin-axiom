#!/usr/bin/env python3
"""
THE CLOSURE CARD'S PRE-SEAL EXERCISE, KEPT (data-free)
The web seat (chat1), 2026-11-10. Committed AFTER the card's run and its review, so that what was seen before the seal
is on record.

The card's header says its functions "were exercised once on two unrelated departures, (3) and (3,1,3), to see that the
code runs". The review found that this understates it: the exercise ran the whole card on that family and printed its
cells. The family has the card's two shapes, a single run and a palindromic departure. This file is that scratch
script as it was run before the seal, with only the import path made relative. Its printed output was not saved then;
the run kept beside this file was made after the review, with the sealed script unchanged.

What it printed before the seal, as the seat's log has it: the cells (C0 and C5 true; C1 to C4 false, since (3) does
not keep the line and (3,1,3) is itself a mirror pair); 16 composites, 4 single and 12 not; for a square the half
rotation, found; for a composite of (3) closed by 1 and by 2 periods one reversal, with det g = -1, the relation
g W^-1 g^-1 = W true and the two departures exchanged; the four apexes.

0 of 19.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import single_state_closure as m  # noqa: E402

F = {'departures': {'(3)': [3], '(3,1,3)': [3, 1, 3]}, 'ks': (1, 2),
     'controls': {'(4)': ([4], '2.618034', 1)},
     'generators': {'L^3 R (LR)^1': [3, 1, 1, 1]}, 'deepest': 3}
R = m.card(F)
print(json.dumps(R['cells']), R['counts'])
k = next(iter(R['C4_symmetries']))
print(k, {a: b for a, b in R['C4_symmetries'][k].items() if a != 'word'})
ks = [x for x in R['C4_symmetries'] if R['C4_symmetries'][x]['kind'] == 'reversal']
print(ks[0], R['C4_symmetries'][ks[0]]['reversals'])
print({a: (b['apex'], b['multiplicity']) for a, b in R['C1'].items()})
