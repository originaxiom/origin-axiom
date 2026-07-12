#!/usr/bin/env python3
"""B535 C1: does the coupling census saturate? (Durand guarantees YES; find where.)

For every factor u of length 1..8 of the fixed point (host depth 11):
return-word induction -> Perron type (sorted rounded vector) + canonical codes.
Track cumulative distinct counts per length.
"""
import sys
import os
import numpy as np
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, canonical_codes,
)

SIGMA_CANONICAL = canonical_codes(((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2)))


def analyze(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 2 * trim + 2:
        return None
    rws = standard_return_words_from_positions(host, positions, trim=trim)
    if len(rws) < 2:
        return None
    ind = canonical_induced_system(rws, max_power=2)
    if ind is None:
        return None
    M = np.array(ind['matrix'].tolist(), dtype=float)
    eigs, vecs = np.linalg.eig(M)
    idx = np.argmax(np.abs(eigs.real))
    v = vecs[:, idx].real
    if np.any(v < 0):
        v = -v
    v = v / v.sum()
    return {
        'perron_key': tuple(np.round(np.sort(v)[::-1], 4)),
        'codes': ind['canonical_codes'],
        'rc': len(rws),
        'is_self': ind['canonical_codes'] == SIGMA_CANONICAL,
    }


def main():
    host = grow(11)
    print(f"host length: {len(host)}")
    print(f"\n{'len':>4} {'factors':>8} {'analyzed':>9} {'new-P':>6} {'cum-P':>6} "
          f"{'new-C':>6} {'cum-C':>6} {'self':>5}")
    print("  " + "-" * 55)

    perron_types = {}
    code_types = {}
    census = []
    for L in range(1, 9):
        fpm = factor_position_map(host, L)
        n_analyzed = n_self = 0
        new_p = new_c = 0
        for u in sorted(fpm.keys()):
            r = analyze(u, host)
            if r is None:
                continue
            n_analyzed += 1
            n_self += r['is_self']
            if r['perron_key'] not in perron_types:
                perron_types[r['perron_key']] = (L, u)
                new_p += 1
            if r['codes'] not in code_types:
                code_types[r['codes']] = (L, u)
                new_c += 1
            census.append((L, u, r['perron_key'], r['rc']))
        print(f"{L:>4} {len(fpm):>8} {n_analyzed:>9} {new_p:>6} "
              f"{len(perron_types):>6} {new_c:>6} {len(code_types):>6} {n_self:>5}")

    print(f"\nPERRON TYPES: {len(perron_types)} total")
    for key, (L, u) in sorted(perron_types.items(), key=lambda kv: kv[1][0]):
        n_pts = sum(1 for c in census if c[2] == key)
        print(f"  first at len {L} ('{u}'), rc={len(key)}, {n_pts} points: "
              f"[{', '.join(f'{x:.4f}' for x in key)}]")

    print(f"\nCANONICAL INDUCED SYSTEMS: {len(code_types)} total")
    for codes, (L, u) in sorted(code_types.items(), key=lambda kv: kv[1][0]):
        star = " = SIGMA (self)" if codes == SIGMA_CANONICAL else ""
        print(f"  first at len {L} ('{u}'): {codes}{star}")

    # saturation lengths
    sat_p = max(L for key, (L, u) in perron_types.items())
    sat_c = max(L for codes, (L, u) in code_types.items())
    print(f"\nSATURATION: last new Perron type at length {sat_p}; "
          f"last new canonical system at length {sat_c}")
    print(f"(Durand's theorem guarantees finiteness; lengths {max(sat_p,sat_c)+1}..8 "
          f"produced nothing new)" if max(sat_p, sat_c) < 8 else
          "(WARNING: new types at max length — census NOT saturated, extend)")


if __name__ == '__main__':
    main()
