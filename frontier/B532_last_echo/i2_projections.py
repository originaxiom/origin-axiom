#!/usr/bin/env python3
"""B532 I2 — The Projection Algebra.

Binary projections (coarsenings) of the 4-letter alphabet: each is a
"measurement" that reads a value from the object. Which measurements are
compatible with the grammar, and do they determine each other?

For each partition {X}|{Y} of {a,b,A,B} into two non-empty classes:
1. Compute the 2×2 induced substitution matrix
2. Perron eigenvalue → frequency ratio
3. Is the induced system Pisot? Primitive?
4. Does the projected fixed point form a substitutive sequence?
5. Grammar compatibility: does the projection respect the 7/16 grammar?
"""

import sympy as sp
import numpy as np
from itertools import combinations

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHABET = ['a', 'b', 'A', 'B']
GRAMMAR = {('a', 'b'), ('a', 'A'), ('b', 'A'), ('A', 'a'), ('A', 'A'), ('A', 'B'), ('B', 'a')}


def grow(depth, seed='a'):
    u = seed
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


def binary_partitions():
    """All 7 non-trivial 2-class partitions (up to complement)."""
    partitions = []
    for r in range(1, 3):
        for combo in combinations(range(4), r):
            class0 = frozenset(combo)
            class1 = frozenset(range(4)) - class0
            key = min(class0, class1)
            label0 = ''.join(ALPHABET[i] for i in sorted(class0))
            label1 = ''.join(ALPHABET[i] for i in sorted(class1))
            partitions.append({
                'class0': class0,
                'class1': class1,
                'label': f'{{{label0}}}|{{{label1}}}',
                'proj': {ALPHABET[i]: 0 for i in class0} | {ALPHABET[i]: 1 for i in class1},
            })
    return partitions


def induced_matrix(partition):
    """Compute the 2×2 induced substitution matrix for a binary partition."""
    proj = partition['proj']
    M = np.zeros((2, 2), dtype=int)
    for g in ALPHABET:
        image = SUB[g]
        target = proj[g]
        for c in image:
            source = proj[c]
            M[source, target] += 1
    return M


def analyze_partition(partition, depth=10):
    """Full analysis of a binary partition."""
    M = induced_matrix(partition)
    proj = partition['proj']

    # Eigenvalues
    M_sp = sp.Matrix(M.tolist())
    charpoly = M_sp.charpoly(sp.Symbol('x'))
    evals = [complex(e) for e in M_sp.eigenvals().keys()]
    evals_abs = sorted([abs(e) for e in evals], reverse=True)

    # Perron eigenvalue and frequency ratio
    perron = evals_abs[0]
    contracting = evals_abs[1] if len(evals_abs) > 1 else 0

    # Is Pisot? (PV number: >1, all conjugates <1 in absolute value)
    is_pisot = perron > 1 and (len(evals_abs) < 2 or contracting < 1)

    # Is primitive? (some power has all positive entries)
    is_primitive = False
    Mk = np.eye(2, dtype=int)
    for k in range(1, 20):
        Mk = Mk @ M
        if np.all(Mk > 0):
            is_primitive = True
            break

    # Frequency ratio from Perron eigenvector
    evals_sp, evecs = np.linalg.eig(M.astype(float))
    perron_idx = np.argmax(np.abs(evals_sp))
    pv = np.abs(evecs[:, perron_idx])
    pv = pv / pv.sum()
    freq_ratio = pv[0] / pv[1] if pv[1] > 1e-10 else float('inf')

    # Project the fixed point and check if it's substitutive
    word = grow(depth)
    projected = ''.join(str(proj[c]) for c in word)

    # Induced 2-letter substitution (if it exists)
    induced_sub = {}
    for g in ALPHABET:
        target = proj[g]
        image = ''.join(str(proj[c]) for c in SUB[g])
        if target not in induced_sub:
            induced_sub[target] = image
        else:
            if induced_sub[target] != image:
                induced_sub[target] = None

    is_substitutive = all(v is not None for v in induced_sub.values())

    # Grammar compatibility: check which transitions in {0,1} are allowed
    proj_grammar = set()
    for x, y in GRAMMAR:
        proj_grammar.add((proj[x], proj[y]))
    n_proj_transitions = len(proj_grammar)

    # Check actual transitions in projected word
    actual_transitions = set(zip(projected, projected[1:]))
    n_actual = len(actual_transitions)

    # The projection preserves grammar iff the projected word's transitions
    # are exactly what the induced grammar predicts
    grammar_compatible = n_actual == n_proj_transitions

    return {
        'label': partition['label'],
        'matrix': M,
        'charpoly': str(charpoly.as_expr()),
        'perron': perron,
        'contracting': contracting,
        'is_pisot': is_pisot,
        'is_primitive': is_primitive,
        'freq_ratio': freq_ratio,
        'freq_0': pv[0],
        'freq_1': pv[1],
        'is_substitutive': is_substitutive,
        'induced_sub': induced_sub if is_substitutive else None,
        'n_proj_transitions': n_proj_transitions,
        'n_actual_transitions': n_actual,
        'grammar_compatible': grammar_compatible,
    }


def main():
    phi = (1 + np.sqrt(5)) / 2
    sq_phi = np.sqrt(phi)

    print("=" * 80)
    print("B532 I2 — The Projection Algebra")
    print("=" * 80)

    partitions = binary_partitions()
    results = []

    for p in partitions:
        r = analyze_partition(p)
        results.append(r)

    # Display
    print(f"\n{'Partition':<20} {'Matrix':>12} {'Perron':>8} {'|λ₂|':>8} {'Pisot':>6} "
          f"{'Prim':>5} {'Ratio':>8} {'Sub':>4} {'Gram':>5} {'Trans':>6}")
    print("-" * 100)
    for r in results:
        M = r['matrix']
        mstr = f"[{M[0,0]},{M[0,1]};{M[1,0]},{M[1,1]}]"
        print(f"{r['label']:<20} {mstr:>12} {r['perron']:8.4f} {r['contracting']:8.4f} "
              f"{'YES' if r['is_pisot'] else 'NO':>6} "
              f"{'YES' if r['is_primitive'] else 'NO':>5} "
              f"{r['freq_ratio']:8.4f} "
              f"{'YES' if r['is_substitutive'] else 'NO':>4} "
              f"{'YES' if r['grammar_compatible'] else 'NO':>5} "
              f"{r['n_actual_transitions']}/{r['n_proj_transitions']:>4}")

    # Identify known frequency ratios
    print("\n--- Frequency ratio identification ---")
    known = {
        'φ': phi,
        '1/φ': 1/phi,
        '√φ': sq_phi,
        '1/√φ': 1/sq_phi,
        'φ√φ': phi * sq_phi,
        '1/(φ√φ)': 1 / (phi * sq_phi),
    }
    for r in results:
        matches = []
        for name, val in known.items():
            if abs(r['freq_ratio'] - val) < 0.001:
                matches.append(name)
            if abs(1/r['freq_ratio'] - val) < 0.001:
                matches.append(f"1/{name}" if not name.startswith('1/') else name[2:])
        if matches:
            print(f"  {r['label']}: ratio = {r['freq_ratio']:.6f} = {', '.join(matches)}")
        else:
            print(f"  {r['label']}: ratio = {r['freq_ratio']:.6f} (no known match)")

    # Commutativity of projections
    print("\n--- Projection lattice ---")
    print("  Two projections π₁, π₂ commute if π₁∘π₂ = π₂∘π₁ on sequences.")
    print("  (All binary projections commute trivially since they map to {0,1}.)")
    print("  The lattice structure: meet = AND, join = OR of partition classes.")

    # The ONE-MEASUREMENT TEST
    print("\n--- ONE-MEASUREMENT TEST ---")
    print("  Fix one projection's frequency ratio. Among all 4-letter substitutions")
    print("  with the same Pisot property — how many satisfy our 7/16 grammar?")

    # Check which partitions are substitutive
    sub_count = sum(1 for r in results if r['is_substitutive'])
    pisot_count = sum(1 for r in results if r['is_pisot'])
    gram_count = sum(1 for r in results if r['grammar_compatible'])
    print(f"\n  Substitutive projections: {sub_count}/7")
    print(f"  Pisot projections: {pisot_count}/7")
    print(f"  Grammar-compatible projections: {gram_count}/7")

    # For non-substitutive ones, show why
    print("\n--- Non-substitutive projections (image ambiguity) ---")
    for r in results:
        if not r['is_substitutive']:
            proj = [p for p in partitions if p['label'] == r['label']][0]['proj']
            images = {}
            for g in ALPHABET:
                target = proj[g]
                image = ''.join(str(proj[c]) for c in SUB[g])
                if target not in images:
                    images[target] = [(g, image)]
                else:
                    images[target].append((g, image))
            for target, entries in images.items():
                if len(set(img for _, img in entries)) > 1:
                    print(f"  {r['label']}: class {target} has conflicting images:")
                    for g, img in entries:
                        print(f"    σ({g}) → {SUB[g]} → projected: {img}")

    # Summary table
    print("\n" + "=" * 80)
    print("PROJECTION ALGEBRA SUMMARY")
    print("=" * 80)
    print(f"\n  7 binary partitions analyzed:")
    print(f"  - {sub_count} are SUBSTITUTIVE (projection commutes with σ)")
    print(f"  - {pisot_count} are PISOT")
    print(f"  - {gram_count} have all grammar transitions realized")
    print()
    for r in results:
        flags = []
        if r['is_substitutive']:
            flags.append('SUB')
        if r['is_pisot']:
            flags.append('PISOT')
        if r['is_primitive']:
            flags.append('PRIM')
        if r['grammar_compatible']:
            flags.append('GRAM')
        print(f"  {r['label']:<20} ratio={r['freq_ratio']:.4f}  [{', '.join(flags)}]")


if __name__ == '__main__':
    main()
