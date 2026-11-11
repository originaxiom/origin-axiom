#!/usr/bin/env python3
"""
THE READ-OUT AS A VALUE, NOT A PLACE: WHAT A COMPOSITE READS
The web seat (chat1), 2026-11-11. Data-free. This header is the sealed rule. It was committed and pushed, with this
script's sha256, before any run of this script on any family. Nothing was run before the seal: the functions it
imports are the closure card's (relays/chat1_2026-11-10_closure/single_state_closure.py, sealed 5cc0711cc, unchanged),
and the code below was not executed, not even on other inputs.

WHY. The closure card (8718d4677; main's B1875) showed that "one state, one place" is not kept when histories are
composed. Its numbers suggest something it did not test: two copies of one departure tie exactly, so both places read
the same value; and a composite of different departures has its apex at the deepest one. If so, what all allowed
histories read together is a value, and it composes as a greatest. P-717 lists "ONE departure (not several)" as a
choice; this card asks whether, for the read value, it is one.

KIND. A weave question (what do all allowed histories read together), put to a thread instrument on a chosen clock:
B1857's flat-fibre model, where the lightest state sits at the apex and reads its height, exactly in the limit of
small fibre area. Nothing is computed on the hyperbolic metric. No coupling, no frame output, no data. The heights are
the instrument's own; none is compared with any value of tau on record.

THE INSTRUMENT. The closure card's: the height of run i of a cyclic run sequence is H_i = (r_i + x_i + y_i)/2, with
x_i and y_i the continued fractions read forward and backward; the apex is the greatest. The OWN VALUE of a departure
is its apex height when closed by 60 golden periods. The OFFSET of a run is (x_i - y_i)/2: the shift of the apex's
real part from that of the departure read alone, which is palindromic.

THE FAMILY (fixed now).
 - Departures: the single runs (6) and (11), and (2,1,2,1,2). D_g is D closed by g golden periods, runs D + [1]*(2g+1).
 - Gaps: k = 1, 2, 4, 8, 16. A composite of m factors at k has gaps k, k+1, ..., k+m-1, all different.
 - Same departure: m = 2, 3, 4 copies of each of the three departures.
 - Different departures: (6)(11); (6)(2,1,2,1,2); (11)(2,1,2,1,2); (6)(6)(11); (11)(6)(2,1,2,1,2).
 - Single runs n = 6, 11, 16, 21, 26, each as L^n R (LR)^3; and n = 7 as a control that must fail.

HAND WORK BEFORE THIS CARD (disclosed).
 H1 A run's height depends on its neighbours only through the two continued fractions, and a golden gap of g periods
    hides what lies beyond it up to a factor phi^-(4g) roughly. So every copy of a departure tends to the departure's
    own value as the gaps lengthen, and so does the offset to 0. Two copies with gaps k and k + 1 have their two
    continued fractions exchanged, so they tie exactly (the closure card's C2); three or four do not.
 H2 A single run of n in a long golden ground has own value (n + 2/phi)/2 = (n - 1)/2 + sqrt(5)/2.
 H3 L^5 = 1 mod 5, so L^n R (LR)^k keeps LR's line exactly when n = 1 mod 5; then it is a power of LR mod 5.
 H4 In B1857's model the lightest level falls as the height rises (dE0/dq > 0, q = 4 pi^2/(A H)).

CELLS, PREDICTIONS, PRIORS (pass rules).
 V0 The own values of (6) and (2,1,2,1,2) are B1857's 3.618034 and 1.723607 to 1e-6. 99%.
 V1 Same departure, for each of the 9 pairs (D, m): at every k the apex is at one of the m copies of D's deepest run;
    the greatest distance of those m heights from D's own value, and their greatest offset, each fall strictly from
    k = 1 through 16 and are below 1e-12 at k = 16; ln(distance at 8 / distance at 16)/8 is within 5% of 4 ln phi;
    and the spread of the m heights is zero at every k for m = 2 (the closure card's exact tie), and for m = 3, 4
    falls strictly from k = 1 through 16 and is below 1e-12 at k = 16. 93%.
 V2 Different departures, for each of the 5 composites: at every k the apex is unique and sits at a run of the
    deepest departure present (11 if there is one, else 6); its distance from that departure's own value falls
    strictly from k = 1 through 16 and is below 1e-12 at 16. 93%.
 V3 The runs n = 6, 11, 16, 21, 26 each keep the line as rows and as columns; their own values equal
    (n - 1)/2 + sqrt(5)/2 to 1e-40 and increase with n. The control n = 7 does not keep the line. 98%.

WHAT THE OUTCOMES MEAN (fixed now).
 - V1 and V2 hold: in this instrument, in the limit of long golden gaps, a history reads the own value of its deepest
   departure, and copies of a departure do not change the value. For the read value, "one departure, not several" is
   then not a separate choice: several departures of one kind read what one reads.
 - V3 holds as well: the allowed departures have no greatest own value. So over all allowed histories the read value
   has no greatest, and by H4 the lightest state of the whole does not exist in this instrument: its infimum is the
   cusp. What is missing is a bound on the departure, or an order with a least member. That is P-717's second choice
   (the length), and the weight of B1872 and B1876, said in this instrument.
 - V1 fails (the copies do not converge): copies change the value, and "one, not several" stays a choice.
 - V2 fails: a composite does not read its deepest departure, and the greatest law is withdrawn.
 - V3 fails: diagnosed first.
 - Any cell fails: the failure is the finding.

STAYS OUT: the hyperbolic metric; the order of departures by any action (length, volume); which departure is least;
any comparison of a height with a value of tau on record; the tick's histories with an odd number of runs.

0 of 19.
"""
import hashlib
import json
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'chat1_2026-11-10_closure'))
import single_state_closure as card  # noqa: E402

mp.mp.dps = 60
PHI = (1 + mp.sqrt(5)) / 2
DEPS = {'(6)': [6], '(11)': [11], '(2,1,2,1,2)': [2, 1, 2, 1, 2]}
DEEP = {'(6)': 0, '(11)': 0, '(2,1,2,1,2)': 2}          # the index of the deepest run inside the departure
KS = (1, 2, 4, 8, 16)


def own_value(dep):
    return max(card.heights(card.runs_single(dep, 60)))


def build(names, k):
    """Runs of the composite, and for each factor the index of its departure's deepest run."""
    runs, deep = [], []
    for j, name in enumerate(names):
        deep.append(len(runs) + DEEP[name])
        runs += DEPS[name] + [1] * (2 * (k + j) + 1)
    return runs, deep


def offsets(r, idx):
    out = []
    for i in idx:
        x = card.cf_tail(card.fwd(r, i))
        y = card.cf_tail(card.bwd(r, i))
        out.append(abs(x - y) / 2)
    return out


def strictly_falling(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def main():
    R = {'script_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'card_sha256': hashlib.sha256(open(os.path.join(HERE, '..', 'chat1_2026-11-10_closure', 'single_state_closure.py'), 'rb').read()).hexdigest()}
    own = {name: own_value(dep) for name, dep in DEPS.items()}
    R['own_values'] = {name: mp.nstr(v, 20) for name, v in own.items()}
    R['V0'] = {'(6)': bool(abs(own['(6)'] - mp.mpf('3.618034')) < mp.mpf('1e-6')),
               '(2,1,2,1,2)': bool(abs(own['(2,1,2,1,2)'] - mp.mpf('1.723607')) < mp.mpf('1e-6'))}
    # ---- V1
    v1 = {}
    for name in DEPS:
        for m in (2, 3, 4):
            rows = []
            for k in KS:
                r, deep = build([name] * m, k)
                H = card.heights(r)
                top = max(H)
                at = [i for i, h in enumerate(H) if abs(h - top) < card.TOL]
                hs = [H[i] for i in deep]
                rows.append({'k': k, 'apex_at_a_copy': all(i in deep for i in at), 'spread': max(hs) - min(hs),
                             'distance': max(abs(h - own[name]) for h in hs), 'offset': max(offsets(r, deep))})
            rate = mp.log(rows[3]['distance'] / rows[4]['distance']) / 8
            if m == 2:
                spread_ok = all(x['spread'] < card.TOL for x in rows)
            else:
                spread_ok = strictly_falling([x['spread'] for x in rows]) and rows[-1]['spread'] < mp.mpf('1e-12')
            ok = (all(x['apex_at_a_copy'] for x in rows) and spread_ok
                  and all(strictly_falling([x[q] for x in rows]) and rows[-1][q] < mp.mpf('1e-12')
                          for q in ('distance', 'offset'))
                  and abs(rate / (4 * mp.log(PHI)) - 1) < mp.mpf('0.05'))
            v1[f'{name} x {m}'] = {'rows': [{a: (mp.nstr(b, 8) if isinstance(b, mp.mpf) else b) for a, b in x.items()} for x in rows],
                                   'rate': mp.nstr(rate, 10), 'four_ln_phi': mp.nstr(4 * mp.log(PHI), 10), 'holds': bool(ok)}
    R['V1'] = v1
    # ---- V2
    v2 = {}
    for names in (['(6)', '(11)'], ['(6)', '(2,1,2,1,2)'], ['(11)', '(2,1,2,1,2)'], ['(6)', '(6)', '(11)'],
                  ['(11)', '(6)', '(2,1,2,1,2)']):
        deepest = '(11)' if '(11)' in names else '(6)'
        rows = []
        for k in KS:
            r, deep = build(names, k)
            H = card.heights(r)
            top = max(H)
            at = [i for i, h in enumerate(H) if abs(h - top) < card.TOL]
            allowed = [d for d, n in zip(deep, names) if n == deepest]
            rows.append({'k': k, 'unique': len(at) == 1, 'at_the_deepest_departure': at[0] in allowed,
                         'distance': abs(top - own[deepest])})
        ok = (all(x['unique'] and x['at_the_deepest_departure'] for x in rows)
              and strictly_falling([x['distance'] for x in rows]) and rows[-1]['distance'] < mp.mpf('1e-12'))
        v2[' '.join(names)] = {'deepest': deepest,
                               'rows': [{a: (mp.nstr(b, 8) if isinstance(b, mp.mpf) else b) for a, b in x.items()} for x in rows],
                               'holds': bool(ok)}
    R['V2'] = v2
    # ---- V3
    v3, vals = {}, []
    for n in (6, 11, 16, 21, 26, 7):
        w = 'L' * n + 'R' + 'LR' * 3
        line = card.keeps_line(card.mat(w))
        val = own_value([n])
        formula = mp.mpf(n - 1) / 2 + mp.sqrt(5) / 2
        v3[str(n)] = {'keeps_line_columns': line['column'], 'keeps_line_rows': line['row'], 'own_value': mp.nstr(val, 20),
                      'equals_formula_to_1e-40': bool(abs(val - formula) < mp.mpf('1e-40'))}
        if n != 7:
            vals.append(val)
    R['V3'] = v3
    R['cells'] = {
        'V0': all(R['V0'].values()),
        'V1': len(v1) == 9 and all(x['holds'] for x in v1.values()),
        'V2': len(v2) == 5 and all(x['holds'] for x in v2.values()),
        'V3': (all(v3[str(n)]['keeps_line_columns'] and v3[str(n)]['keeps_line_rows'] and v3[str(n)]['equals_formula_to_1e-40']
                   for n in (6, 11, 16, 21, 26)) and strictly_falling([-v for v in vals])
               and not (v3['7']['keeps_line_columns'] or v3['7']['keeps_line_rows'])),
    }
    with open(os.path.join(HERE, 'out_value_not_place.json'), 'w') as fh:
        json.dump(R, fh, indent=1)
    print('written out_value_not_place.json')


if __name__ == '__main__':
    main()
