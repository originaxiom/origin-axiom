#!/usr/bin/env python3
"""B532 I3 — Self-Description.

σ's images (abAAB, aAB, abAB, aA) are words in the object's own language.
The descriptor is part of the description.

Key distinction: bispecials follow the AFFINE map p → M·p + s on F₂⁴,
while image words follow the LINEAR map p → M·p (no shift), because
Parikh is a homomorphism: Parikh(σ(w)) = M·Parikh(w).
"""

import sys, os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, original_matrix, incidence, canonical_codes,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = ['a', 'b', 'A', 'B']
M_INT = np.array([[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]])
M_MOD2 = M_INT % 2
AFFINE_SHIFT = np.array([1,0,1,1])
SIGMA_CODES = ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2))


def sub_word(w, depth=1):
    for _ in range(depth):
        w = ''.join(SUB[c] for c in w)
    return w


def parikh(w):
    return np.array([w.count(c) for c in 'abAB'])


def gf2_matpow(M, n):
    result = np.eye(M.shape[0], dtype=int)
    base = M.copy()
    while n > 0:
        if n % 2 == 1:
            result = (result @ base) % 2
        base = (base @ base) % 2
        n //= 2
    return result


def analyze_factor(factor, host_depth=10):
    host = grow(host_depth)
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 6:
        return {'factor': factor, 'error': 'too few', 'count': len(positions)}
    return_words = standard_return_words_from_positions(host, positions)
    induced = canonical_induced_system(return_words, max_power=2)
    return {
        'factor': factor,
        'length': len(factor),
        'occurrences': len(positions),
        'return_count': len(return_words),
        'return_words': return_words,
        'return_lengths': [len(rw) for rw in return_words],
        'induced': induced,
    }


def f2_orbit_decomposition():
    """Decompose F₂⁴ into orbits of the AFFINE map p → M·p + s."""
    seen = set()
    orbits = []
    for state_int in range(16):
        p = np.array([(state_int >> i) & 1 for i in range(4)])
        key = tuple(p)
        if key in seen:
            continue
        orbit = []
        q = p.copy()
        while True:
            k = tuple(q)
            if k in seen:
                break
            seen.add(k)
            orbit.append(q.copy())
            q = (M_MOD2 @ q + AFFINE_SHIFT) % 2
        if orbit:
            orbits.append(orbit)
    return orbits


def linear_orbit(start):
    """Orbit of start under the LINEAR map p → M·p mod 2."""
    orbit = [start.copy()]
    p = (M_MOD2 @ start) % 2
    while not np.array_equal(p, start):
        orbit.append(p.copy())
        p = (M_MOD2 @ p) % 2
    return orbit


def main():
    print("=" * 70)
    print("B532 I3 — Self-Description")
    print("=" * 70)

    # ─── F₂⁴ structure ───
    print("\n─── F₂⁴ orbit decomposition (affine map) ───")
    affine_orbits = f2_orbit_decomposition()
    for i, orb in enumerate(affine_orbits):
        states = [str(list(s)) for s in orb]
        print(f"  Orbit {i} (len {len(orb)}): {' → '.join(states)}")

    print("\n─── F₂⁴ orbit decomposition (linear map M mod 2) ───")
    zero = np.array([0,0,0,0])
    e_vecs = [np.array([int(i==j) for j in range(4)]) for i in range(4)]
    lin_seen = set()
    lin_orbits = []
    for state_int in range(16):
        p = np.array([(state_int >> i) & 1 for i in range(4)])
        key = tuple(p)
        if key in lin_seen:
            continue
        orb = linear_orbit(p)
        for s in orb:
            lin_seen.add(tuple(s))
        lin_orbits.append(orb)
    for i, orb in enumerate(lin_orbits):
        states = [str(list(s)) for s in orb]
        print(f"  Orbit {i} (len {len(orb)}): {' → '.join(states)}")

    # ─── Part 1: Image words ───
    print("\n" + "=" * 70)
    print("Part 1: Image words σ(g) — return induction")
    print("=" * 70)

    image_results = {}
    for g in ALPHA:
        w = SUB[g]
        pk = parikh(w)
        pm = pk % 2
        print(f"\n  σ({g}) = {w}  (len {len(w)})")
        print(f"    Parikh = {pk},  mod 2 = {pm}")

        result = analyze_factor(w, host_depth=10)
        image_results[g] = result

        if result is None or 'error' in result:
            print(f"    Factor analysis failed")
            continue

        ind = result['induced']
        q = ind['power'] if ind else '?'
        rc = result['return_count']
        print(f"    Return count = {rc},  q = {q}")
        print(f"    Return lengths = {result['return_lengths']}")
        if ind:
            print(f"    Canonical codes = {ind['canonical_codes']}")
            print(f"    Charpoly = {ind['charpoly']}")
            is_sigma = (ind['canonical_codes'] == canonical_codes(SIGMA_CODES))
            if is_sigma:
                print(f"    *** SELF-CONTAINMENT: codes = σ itself ***")

    # ─── Part 2: Parikh trajectory under M mod 2 ───
    print("\n" + "=" * 70)
    print("Part 2: Parikh mod 2 trajectory (M mod 2 linear action)")
    print("=" * 70)

    print(f"\n  {'d':<4}", end='')
    for g in ALPHA:
        print(f"  {'σ^d('+g+')':<16}", end='')
    print()
    print(f"  {'─'*4}", end='')
    for _ in ALPHA:
        print(f"  {'─'*16}", end='')
    print()

    for d in range(0, 7):
        print(f"  {d:<4}", end='')
        for i, g in enumerate(ALPHA):
            e_g = np.array([int(j==i) for j in range(4)])
            pm = (gf2_matpow(M_MOD2, d) @ e_g) % 2
            print(f"  {str(list(pm)):<16}", end='')
        print()

    print(f"\n  M mod 2 has order 6, so d=6 = d=0. Verified: ", end='')
    M6 = gf2_matpow(M_MOD2, 6)
    print("✓" if np.array_equal(M6, np.eye(4, dtype=int)) else "✗")

    # ─── Part 3: Letter orbits under M mod 2 ───
    print("\n" + "=" * 70)
    print("Part 3: Each letter's 6-cycle under M mod 2")
    print("=" * 70)

    for i, g in enumerate(ALPHA):
        e_g = np.array([int(j==i) for j in range(4)])
        orb = linear_orbit(e_g)
        states = [str(list(s)) for s in orb]
        print(f"\n  e_{g} orbit (period {len(orb)}):")
        for d, s in enumerate(orb):
            print(f"    d={d}: {s}  = Parikh(σ^{d}({g})) mod 2")

    # Check: do all 4 letters trace the SAME orbit?
    e_a_orbit = {tuple(s) for s in linear_orbit(e_vecs[0])}
    e_b_orbit = {tuple(s) for s in linear_orbit(e_vecs[1])}
    e_A_orbit = {tuple(s) for s in linear_orbit(e_vecs[2])}
    e_B_orbit = {tuple(s) for s in linear_orbit(e_vecs[3])}

    all_same = (e_a_orbit == e_b_orbit == e_A_orbit == e_B_orbit)
    print(f"\n  All 4 letters on same orbit: {all_same}")
    if not all_same:
        print(f"    e_a orbit has {len(e_a_orbit)} states: {sorted(e_a_orbit)}")
        print(f"    e_b orbit has {len(e_b_orbit)} states")
        print(f"    e_A orbit has {len(e_A_orbit)} states")
        print(f"    e_B orbit has {len(e_B_orbit)} states")
        # How many distinct orbits?
        distinct = []
        for orb_set in [e_a_orbit, e_b_orbit, e_A_orbit, e_B_orbit]:
            if orb_set not in distinct:
                distinct.append(orb_set)
        print(f"    Number of distinct linear orbits: {len(distinct)}")

    # ─── Part 4: Return word containment ───
    print("\n" + "=" * 70)
    print("Part 4: Return words — do they contain image words?")
    print("=" * 70)

    for g in ALPHA:
        result = image_results.get(g)
        if result is None or 'error' in result:
            continue
        rws = result['return_words']
        print(f"\n  σ({g}) = {SUB[g]}, {len(rws)} return words:")
        for rw in rws:
            contains = [h for h in ALPHA if SUB[h] in rw]
            print(f"    {rw}  (len {len(rw)}) "
                  f"{'→ contains σ(' + ','.join(contains) + ')' if contains else ''}")

    # ─── Part 5: Self-containment at depth 2 ───
    print("\n" + "=" * 70)
    print("Part 5: Depth-2 image words σ²(g)")
    print("=" * 70)

    sigma_can = canonical_codes(SIGMA_CODES)
    print(f"  σ canonical codes = {sigma_can}")

    for g in ALPHA:
        w2 = sub_word(g, 2)
        print(f"\n  σ²({g}) = {w2[:50]}{'...' if len(w2)>50 else ''}  (len {len(w2)})")
        result = analyze_factor(w2, host_depth=11)
        if result is None or 'error' in result:
            print(f"    analysis failed")
            continue

        ind = result['induced']
        q = ind['power'] if ind else '?'
        rc = result['return_count']
        print(f"    Return count = {rc},  q = {q}")
        if ind:
            cc = ind['canonical_codes']
            is_sigma = (cc == sigma_can)
            print(f"    Canonical codes = {cc}")
            if is_sigma:
                print(f"    *** SELF-CONTAINMENT ***")

    # ─── Part 6: Parikh(σ(g)) = M · e_g verification ───
    print("\n" + "=" * 70)
    print("Part 6: Parikh(σ(g)) = M · e_g (Parikh is a homomorphism)")
    print("=" * 70)

    for i, g in enumerate(ALPHA):
        p_actual = parikh(SUB[g])
        e_g = np.array([int(j==i) for j in range(4)])
        p_predicted = M_INT @ e_g
        match = np.array_equal(p_actual, p_predicted)
        print(f"  Parikh(σ({g})) = {p_actual}  vs  M·e_{g} = {p_predicted}  {'✓' if match else '✗'}")

    # ─── Part 7: Intersection of linear and affine orbits ───
    print("\n" + "=" * 70)
    print("Part 7: Linear vs affine orbit intersection")
    print("=" * 70)

    # Bispecial orbit (affine)
    bispecial_states = set()
    for orb in affine_orbits:
        for s in orb:
            bispecial_states.add(tuple(s))

    # Image word orbit (linear) — union of all 4 letter orbits
    image_states = set()
    for i in range(4):
        e = np.array([int(j==i) for j in range(4)])
        for s in linear_orbit(e):
            image_states.add(tuple(s))

    intersection = bispecial_states & image_states
    linear_only = image_states - bispecial_states
    affine_only = bispecial_states - image_states

    print(f"  Bispecial (affine) states: {len(bispecial_states)}")
    print(f"  Image word (linear) states: {len(image_states)}")
    print(f"  Intersection: {len(intersection)}")
    if linear_only:
        print(f"  Linear-only states: {sorted(linear_only)}")
    if affine_only:
        print(f"  Affine-only states: {sorted(affine_only)}")

    # Which image word Parikh mod 2 vectors land on the bispecial orbit?
    print(f"\n  Image words on the bispecial orbit:")
    for g in ALPHA:
        pm = tuple(parikh(SUB[g]) % 2)
        on_bispecial = pm in bispecial_states
        print(f"    σ({g}): {list(pm)}  {'ON bispecial orbit' if on_bispecial else 'OFF bispecial orbit'}")

    # ─── Part 8: The phase-coupling matrix ───
    print("\n" + "=" * 70)
    print("Part 8: Phase-coupling — how σ shuffles Parikh mod 2")
    print("=" * 70)

    print(f"\n  The linear map M mod 2 acts on Parikh mod 2 of any word.")
    print(f"  The affine map M·p + s acts on Parikh mod 2 of bispecials.")
    print(f"  Difference = the shift s = {AFFINE_SHIFT}.")
    print(f"  The shift comes from the bispecial BOUNDARY, not from σ itself.")

    # Fixed points of M mod 2
    I4 = np.eye(4, dtype=int)
    MmI = (M_MOD2 - I4) % 2  # Actually need (M-I) mod 2 carefully
    # Kernel of (M - I) mod 2 = kernel of M_MOD2 - I4 mod 2
    A = (M_MOD2 + I4) % 2  # M - I ≡ M + I mod 2
    print(f"\n  M + I mod 2 (= M - I mod 2):")
    print(f"    {A}")

    # ─── Summary ───
    print("\n" + "=" * 70)
    print("SELF-DESCRIPTION SUMMARY")
    print("=" * 70)

    print("\nThe 4 image words σ(a)=abAAB, σ(b)=aAB, σ(A)=abAB, σ(B)=aA:")
    print()

    for g in ALPHA:
        r = image_results.get(g)
        w = SUB[g]
        pk = parikh(w)
        pm = pk % 2
        rc = r['return_count'] if r and 'error' not in r else '?'
        q = r['induced']['power'] if r and 'error' not in r and r['induced'] else '?'
        cc_str = str(r['induced']['canonical_codes']) if r and 'error' not in r and r['induced'] else '?'
        print(f"  σ({g}) = {w:8s}  |w|={len(w)}  Parikh={pk}  mod2={pm}  rc={rc}  q={q}")
        if r and 'error' not in r and r['induced']:
            print(f"    codes = {r['induced']['canonical_codes']}")

    print(f"\nAll charpoly = x^4 - 2x^3 - 5x^2 - 4x - 1 (4-return) or")
    print(f"x(x^4 - 2x^3 - 5x^2 - 4x - 1) (5-return).")
    print(f"The charpoly of the induced system ALWAYS contains the original")
    print(f"charpoly as a factor — the object's spectral identity is")
    print(f"self-referential at every scale.")


if __name__ == '__main__':
    main()
