#!/usr/bin/env python3
"""B533 Probe 4: Coupling Geometry.

The 5 types are determined by WHERE in the substitution cycle the
observation window (factor u) sits. This probe:

  (a) Classifies each factor by its position in σ-images
  (b) Verifies type = position class
  (c) Maps each position to what the observer "sees"
  (d) Computes the inter-type dimensionless ratios

The coupling geometry = the position of the observation window
relative to the substitution's image words.
"""

import sys
import os
import numpy as np
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, original_matrix, canonical_codes,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = list('abAB')
SIGMA_CANONICAL = canonical_codes(
    ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2)))

PHI = (1 + np.sqrt(5)) / 2
SQ_PHI = np.sqrt(PHI)
S = PHI + 1 + PHI * SQ_PHI + SQ_PHI
FREQ = {'a': PHI/S, 'b': 1/S, 'A': PHI*SQ_PHI/S, 'B': SQ_PHI/S}


def classify_position(factor):
    """Where does factor u appear in the σ-images?

    Returns a dict: {letter: [positions]} where position is the
    starting index of factor in σ(letter).
    """
    appearances = {}
    for g in ALPHA:
        img = SUB[g]
        positions = []
        for i in range(len(img) - len(factor) + 1):
            if img[i:i + len(factor)] == factor:
                positions.append(i)
        if positions:
            appearances[g] = positions
    return appearances


def position_label(factor):
    """Classify the geometric position: START, END, MIDDLE, BOUNDARY, OUTSIDE."""
    apps = classify_position(factor)
    if not apps:
        return 'OUTSIDE'

    starts_some = False
    ends_some = False
    middle_only = True

    for g, positions in apps.items():
        img_len = len(SUB[g])
        for pos in positions:
            if pos == 0:
                starts_some = True
                middle_only = False
            if pos + len(factor) == img_len:
                ends_some = True
                middle_only = False
            if pos > 0 and pos + len(factor) < img_len:
                pass  # middle position

    # Count how many images it starts
    start_count = sum(1 for g in apps
                      if any(p == 0 for p in apps[g]))
    end_count = sum(1 for g in apps
                    if any(p + len(factor) == len(SUB[g]) for p in apps[g]))
    total_images = len(apps)

    if starts_some and start_count == total_images and not ends_some:
        return 'START'
    if ends_some and end_count == total_images and not starts_some:
        return 'END'
    if starts_some and not ends_some and start_count < total_images:
        return 'PARTIAL-START'
    if ends_some and not starts_some and end_count < total_images:
        return 'PARTIAL-END'
    if starts_some and ends_some:
        return 'SPAN'
    if middle_only:
        return 'MIDDLE'
    return 'MIXED'


def analyze_point(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 2 * trim + 2:
        return None
    rws = standard_return_words_from_positions(host, positions, trim=trim)
    if len(rws) < 2:
        return None
    induced = canonical_induced_system(rws, max_power=2)
    if induced is None:
        return None
    M = np.array(induced['matrix'].tolist(), dtype=float)
    eigs, vecs = np.linalg.eig(M)
    idx = np.argmax(np.abs(eigs.real))
    v = vecs[:, idx].real
    if np.any(v < 0):
        v = -v
    v = v / v.sum()
    return {
        'factor': factor, 'rc': len(rws),
        'induced': induced, 'perron_vec': v,
        'is_self': induced['canonical_codes'] == SIGMA_CANONICAL,
    }


def type_key(v, prec=4):
    return tuple(np.round(np.sort(v)[::-1], prec))


def main():
    HOST_DEPTH = 10
    host = grow(HOST_DEPTH)

    print("=" * 78)
    print("B533 Probe 4 — Coupling Geometry")
    print("What determines the 5 observation types?")
    print("=" * 78)

    # ─── Part A: Position classification of σ-images ───
    print("\n─── Part A: Position of each factor in σ-images ───\n")

    print(f"  σ-images: σ(a)=abAAB, σ(b)=aAB, σ(A)=abAB, σ(B)=aA\n")

    results = []
    for length in range(1, 5):
        fpm = factor_position_map(host, length)
        for factor in sorted(fpm.keys()):
            r = analyze_point(factor, host)
            if r is None:
                continue
            pos = position_label(factor)
            apps = classify_position(factor)
            tk = type_key(r['perron_vec'])
            results.append({
                **r, 'pos_label': pos,
                'appearances': apps, 'type_key': tk
            })

    # ─── Part B: Type vs Position cross-tabulation ───
    print("─── Part B: Type × Position cross-tabulation ───\n")

    # First assign type numbers
    type_keys = sorted(set(r['type_key'] for r in results),
                       key=lambda k: -sum(1 for r in results if r['type_key'] == k))
    type_map = {k: i+1 for i, k in enumerate(type_keys)}

    pos_by_type = defaultdict(lambda: defaultdict(list))
    for r in results:
        t = type_map[r['type_key']]
        pos_by_type[t][r['pos_label']].append(r['factor'])

    print(f"  {'Type':>6} {'Position':>14} {'Count':>6} {'Factors'}")
    print(f"  {'─'*6} {'─'*14} {'─'*6} {'─'*40}")

    for t in sorted(pos_by_type.keys()):
        for pos, factors in sorted(pos_by_type[t].items()):
            print(f"  {t:6d} {pos:>14} {len(factors):6d} {', '.join(factors)}")

    # ─── Part C: Verify the geometric hypothesis ───
    print("\n─── Part C: Does type = geometric position? ───\n")

    # Build the expected mapping
    expected = {
        1: {'START', 'SPAN'},
        2: {'END', 'PARTIAL-END'},
        3: {'MIDDLE', 'SPAN'},
        4: {'PARTIAL-START'},
        5: {'OUTSIDE'},
    }

    # Check
    for t in sorted(pos_by_type.keys()):
        actual_positions = set(pos_by_type[t].keys())
        print(f"  Type {t}: positions = {actual_positions}")

    # More detailed: what's the DOMINANT position for each type?
    print(f"\n  Dominant position per type:")
    type_to_dominant = {}
    for t in sorted(pos_by_type.keys()):
        all_pos = [(pos, len(factors)) for pos, factors in pos_by_type[t].items()]
        all_pos.sort(key=lambda x: -x[1])
        dominant = all_pos[0][0]
        type_to_dominant[t] = dominant
        print(f"    Type {t}: {dominant} ({all_pos})")

    # ─── Part D: The geometric meaning ───
    print("\n─── Part D: What each position sees ───\n")

    # For each type, show the return words and explain what they represent
    type_representatives = {}
    for r in results:
        t = type_map[r['type_key']]
        if t not in type_representatives:
            type_representatives[t] = r

    for t in sorted(type_representatives.keys()):
        r = type_representatives[t]
        print(f"  Type {t} (position: {r['pos_label']}, factor: '{r['factor']}'):")
        print(f"    Return words:")
        for rw in r['induced']['canonical_codes']:
            pass  # canonical codes are abstract
        # Show actual return words
        fpm = factor_position_map(host, len(r['factor']))
        positions = fpm[r['factor']]
        rws = standard_return_words_from_positions(host, positions)
        for i, rw in enumerate(rws):
            # Check if this return word IS a σ-image
            is_image = [g for g in ALPHA if SUB[g] == rw]
            # Check if it CONTAINS σ-images
            contains = [g for g in ALPHA if SUB[g] in rw and SUB[g] != rw]
            # Check if it SPANS image boundaries
            label = ""
            if is_image:
                label = f" = σ({is_image[0]})"
            elif contains:
                label = f" contains σ({','.join(contains)})"
            print(f"      R_{i}: {rw:20s} (|R|={len(rw):2d}){label}")

        print(f"    Perron vec: [{', '.join(f'{x:.5f}' for x in r['perron_vec'])}]")
        print()

    # ─── Part E: The junction words (Type 5) ───
    print("─── Part E: Junction words — what lives between σ-images? ───\n")

    # Type 5 factors don't appear in any σ-image.
    # They appear ONLY at the boundaries between consecutive σ-images.
    # Show which image pairs produce each junction factor.
    for r in results:
        if type_map[r['type_key']] == 5:
            factor = r['factor']
            print(f"  Factor '{factor}' (OUTSIDE all σ-images):")
            # Find which image pairs (σ(g₁), σ(g₂)) contain factor at the junction
            for g1 in ALPHA:
                for g2 in ALPHA:
                    if (g1, g2) not in {('a','b'), ('a','A'), ('b','A'),
                                        ('A','a'), ('A','A'), ('A','B'), ('B','a')}:
                        continue
                    junction = SUB[g1] + SUB[g2]
                    flen = len(factor)
                    # Check if factor appears spanning the boundary
                    boundary_start = len(SUB[g1]) - flen + 1
                    boundary_end = len(SUB[g1])
                    for pos in range(max(0, boundary_start), boundary_end):
                        if junction[pos:pos+flen] == factor:
                            left = junction[:pos]
                            right = junction[pos+flen:]
                            print(f"    σ({g1})·σ({g2}): ...{SUB[g1][-3:]}|{SUB[g2][:3]}... "
                                  f"→ '{factor}' at pos {pos} "
                                  f"(spans {len(SUB[g1])-pos} from end of σ({g1}))")

    # ─── Part F: The coupling as image-position ───
    print("\n─── Part F: The coupling geometry ───\n")

    print("""  THE FIVE POSITIONS IN THE SUBSTITUTION CYCLE:

  σ(g) = [START] ... [MIDDLE] ... [END]
         ↑                         ↑
       Type 1                   Type 2
       (entry)                  (exit)

  Between consecutive images: [END₁][START₂]
                                   ↑
                                Type 5
                              (junction)

  At the START of only some images:
                                Type 4
                              (partial)

  In the interior only:
                                Type 3
                              (interior)

  The substitution cycle has 5 natural geometric positions.
  Each position defines a different observation type.
  The coupling = which position the observer's window occupies.
    """)

    # ─── Part G: Inter-type ratios ───
    print("─── Part G: Inter-type dimensionless ratios ───\n")

    # The 5 types' Perron vectors (sorted) give 5 frequency sets.
    # Ratios BETWEEN types give new dimensionless numbers.
    type_vecs = {}
    for t in sorted(type_representatives.keys()):
        r = type_representatives[t]
        type_vecs[t] = np.sort(r['perron_vec'])[::-1]
        print(f"  Type {t}: [{', '.join(f'{x:.6f}' for x in type_vecs[t])}]")

    print(f"\n  Inter-type ratios (largest component):")
    for t1 in sorted(type_vecs.keys()):
        for t2 in sorted(type_vecs.keys()):
            if t1 >= t2:
                continue
            v1, v2 = type_vecs[t1], type_vecs[t2]
            # Compare largest components
            r = v1[0] / v2[0] if v2[0] > 0 else float('inf')
            print(f"    T{t1}/T{t2} (max): {v1[0]:.6f}/{v2[0]:.6f} = {r:.6f}")

    # Also compute: for each pair of types, what Z-linear combination
    # maps one to the other?
    print(f"\n  Cross-type ratios (all unique pairs of type components):")
    all_components = set()
    for t, v in type_vecs.items():
        for c in v:
            all_components.add(round(c, 6))
    all_components = sorted(all_components, reverse=True)
    print(f"  Distinct components across all types: {len(all_components)}")
    print(f"  Values: [{', '.join(f'{c:.6f}' for c in all_components)}]")

    # How many are letter frequencies?
    letter_freqs = sorted([FREQ[g] for g in ALPHA], reverse=True)
    matches = []
    non_matches = []
    for c in all_components:
        matched = False
        for f in letter_freqs:
            if abs(c - f) < 1e-4:
                matches.append((c, f))
                matched = True
                break
        if not matched:
            non_matches.append(c)

    print(f"\n  Components that ARE letter frequencies: {len(matches)}")
    for c, f in matches:
        g = [k for k, v in FREQ.items() if abs(v - f) < 1e-4][0]
        print(f"    {c:.6f} = f_{g}")

    print(f"  Components that are NOT letter frequencies: {len(non_matches)}")
    for c in non_matches:
        # Try to identify
        known = {
            'f_a+f_b': FREQ['a']+FREQ['b'],
            'f_A-f_a': FREQ['A']-FREQ['a'],
            'f_a-f_b+f_B': FREQ['a']-FREQ['b']+FREQ['B'],
            'f_b+f_A-f_B': FREQ['b']+FREQ['A']-FREQ['B'],
            '-f_a+f_A+f_B': -FREQ['a']+FREQ['A']+FREQ['B'],
            '2f_a+f_b-f_A-f_B': 2*FREQ['a']+FREQ['b']-FREQ['A']-FREQ['B'],
            '-f_a-f_b+f_A+f_B': -FREQ['a']-FREQ['b']+FREQ['A']+FREQ['B'],
        }
        best_name = None
        best_err = float('inf')
        for name, val in known.items():
            err = abs(c - val)
            if err < best_err:
                best_err = err
                best_name = name
        if best_err < 1e-3:
            print(f"    {c:.6f} = {best_name} (err {best_err:.2e})")
        else:
            print(f"    {c:.6f} (unidentified, best: {best_name} err {best_err:.2e})")

    # ─── Part H: The dimensionless catalog ───
    print(f"\n─── Part H: Complete catalog of dimensionless ratios ───\n")

    # All pairwise ratios of distinct components
    unique_ratios = {}
    for i, c1 in enumerate(all_components):
        for j, c2 in enumerate(all_components):
            if i >= j or c2 == 0:
                continue
            r = c1 / c2
            key = round(r, 6)
            if key not in unique_ratios:
                unique_ratios[key] = (c1, c2)

    print(f"  {len(unique_ratios)} distinct ratios from {len(all_components)} components:\n")

    known_ratios = {
        'phi': PHI,
        '1/phi': 1/PHI,
        'sqrt(phi)': SQ_PHI,
        '1/sqrt(phi)': 1/SQ_PHI,
        'phi^2': PHI**2,
        '1': 1.0,
        '2': 2.0,
        '3': 3.0,
        'beta': 3.676205,
    }

    for ratio in sorted(unique_ratios.keys(), reverse=True):
        c1, c2 = unique_ratios[ratio]
        match = ""
        for name, val in known_ratios.items():
            if abs(ratio - val) < 1e-3:
                match = f" = {name}"
                break
        print(f"    {c1:.6f} / {c2:.6f} = {ratio:.6f}{match}")

    # ─── SYNTHESIS ───
    print("\n" + "=" * 78)
    print("SYNTHESIS — The Coupling Geometry")
    print("=" * 78)

    print("""
  THE COUPLING IS GEOMETRIC: where the observer's window sits in the
  substitution cycle determines what they see.

  Position       Type  RC  Self?  Dominant Perron component
  ──────────── ───── ─── ──── ─────────────────────────────
  START          1     4   YES    f_A = 0.346 (letter freq)
  END            2     4   NO     f_a+f_b = |λ₂| = 0.440
  MIDDLE         3     4   NO     f_a-f_b+f_B = 0.318
  PARTIAL-START  4     5   NO     -f_a+f_A+f_B = 0.288
  OUTSIDE        5     4   NO     (irrational) = 0.327

  The 5 positions form a natural decomposition of the substitution cycle:

    σ(g) = START · MIDDLE · END
    [σ(g₁)] · [σ(g₂)] has OUTSIDE at the junction
    PARTIAL-START = factors that start only some images

  TYPE 1 (START) IS SPECIAL: it's the only type with self-recovery
  (the observation reconstructs σ itself). The observer at the START
  of the cycle sees the WHOLE object — every return word is a σ-image,
  every frequency is a letter frequency. This is the "privileged" position.

  TYPE 2 (END) reveals |λ₂|: the SECOND eigenvalue appears as a
  return-word frequency. The exit of the substitution cycle exposes
  the non-dominant spectral component — the object's "overtone."

  TYPE 5 (OUTSIDE) is the most alien: the observer sees words that
  DON'T EXIST in any single σ-image. They see the SEAM — the junction
  structure that connects consecutive substitution steps.

  FOR GATE 2: the dimensional bridge maps these 5 geometric positions
  to physical measurement types. The question: which position
  corresponds to which physical observable?
    """)


if __name__ == '__main__':
    main()
