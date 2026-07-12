#!/usr/bin/env python3
"""B532 I4 — The Derivation DAG.

Among the 28+ computed layers of the object, which derive from which?
Build the explicit derivation graph. Source nodes = irreducible kernel.

Each edge is a DEMONSTRATED computation (not a claim).
Extra inputs needed by the observer are listed explicitly.
"""

import json

LAYERS = {
    # ── Source nodes ──
    'sigma': {
        'name': 'σ (the substitution)',
        'desc': 'a→abAAB, b→aAB, A→abAB, B→aA on F₄',
        'derived_from': [],
        'extra_input': None,
        'movement': 'B530 definition',
    },

    # ── Level 1: immediate from σ ──
    'M': {
        'name': 'M (incidence matrix)',
        'desc': '4×4 integer matrix M_ij = count of letter i in σ(j)',
        'derived_from': ['sigma'],
        'extra_input': None,
        'movement': 'B530.I',
    },
    'grammar': {
        'name': 'Grammar (7/16 adjacencies)',
        'desc': 'Allowed letter pairs extracted from σ-images',
        'derived_from': ['sigma'],
        'extra_input': None,
        'movement': 'B530.III',
    },
    'swap_s': {
        'name': 'Swap symmetry s',
        'desc': 'Letter permutation preserving the grammar',
        'derived_from': ['sigma'],
        'extra_input': None,
        'movement': 'B530.XI',
    },
    'symplectic_D': {
        'name': 'Symplectic form D',
        'desc': 'det(M)=-1, orientation-reversing; the chirality',
        'derived_from': ['sigma'],
        'extra_input': None,
        'movement': 'B530.XII',
    },

    # ── Level 2: from M ──
    'charpoly': {
        'name': 'Characteristic polynomial',
        'desc': 'x⁴-2x³-5x²-4x-1, irreducible over Q',
        'derived_from': ['M'],
        'extra_input': None,
        'movement': 'B530.I',
    },
    'perron_eigvec': {
        'name': 'Perron eigenvector (frequencies)',
        'desc': '(φ, 1, φ√φ, √φ)/S — the letter frequencies',
        'derived_from': ['M'],
        'extra_input': None,
        'movement': 'B530.II',
    },
    'perron_eigval': {
        'name': 'Perron eigenvalue β',
        'desc': 'β = φ(1+√φ) = 3.6762… (growth rate)',
        'derived_from': ['M'],
        'extra_input': None,
        'movement': 'B530.I',
    },
    'M_mod2': {
        'name': 'M mod 2 (F₂⁴ structure)',
        'desc': 'Order 6, two linear orbits, nilpotent C=M²+M+I',
        'derived_from': ['M'],
        'extra_input': None,
        'movement': 'B530.XXXVI',
    },
    'disc_galois': {
        'name': 'Discriminant and Galois group',
        'desc': 'disc=-400, Gal=D₄, three independent fields',
        'derived_from': ['charpoly'],
        'extra_input': None,
        'movement': 'B530.IX',
    },

    # ── Level 3: from frequencies ──
    'gap_labels': {
        'name': 'Gap labels (IDS values)',
        'desc': 'freq(a), freq(a)+freq(b), 1-freq(B) — Bellissard',
        'derived_from': ['perron_eigvec'],
        'extra_input': None,
        'movement': 'B530.XXXII',
    },
    'decider_courier': {
        'name': 'Decider/courier roles',
        'desc': '{a,A} deciders (weight β), {b,B} couriers (weight β/φ)',
        'derived_from': ['grammar', 'perron_eigvec'],
        'extra_input': None,
        'movement': 'B530.IV',
    },
    'golden_section': {
        'name': 'Golden section of body',
        'desc': 'deciders:couriers = φ:1 (the golden ratio)',
        'derived_from': ['perron_eigvec', 'decider_courier'],
        'extra_input': None,
        'movement': 'B530.II',
    },
    'entropy': {
        'name': 'Topological entropy h = log β',
        'desc': 'h = 1.3022… = log(φ(1+√φ))',
        'derived_from': ['perron_eigval'],
        'extra_input': None,
        'movement': 'B530.XVII',
    },

    # ── Level 3: from M + σ ──
    'spectral_type': {
        'name': 'Pure discrete spectrum (Pisot)',
        'desc': 'β Pisot + strong coincidence → pure discrete',
        'derived_from': ['charpoly', 'sigma'],
        'extra_input': None,
        'movement': 'B530.VII',
    },
    'rauzy_fractal': {
        'name': 'Rauzy fractal',
        'desc': 'Fractal tile in contracting hyperplane, dim≈2.35',
        'derived_from': ['M', 'sigma'],
        'extra_input': None,
        'movement': 'B530.XIX',
    },
    'return_induction': {
        'name': 'Return-word induction engine',
        'desc': 'Canonical induced substitution for each factor',
        'derived_from': ['sigma'],
        'extra_input': None,
        'movement': 'B530.XXXIV',
    },

    # ── Level 4: from induction engine ──
    'seven_types': {
        'name': '7 canonical induced types',
        'desc': 'All factors at depth 8 fall into 7 conjugacy types',
        'derived_from': ['return_induction'],
        'extra_input': None,
        'movement': 'B530.XXXV',
    },
    'six_phase_clock': {
        'name': 'Six-phase clock (period 6 = 2×3)',
        'desc': 'Period-2 spectral (λ₂<0) × period-3 combinatorial (F₂)',
        'derived_from': ['M_mod2', 'return_induction'],
        'extra_input': None,
        'movement': 'B530.XXXVI',
    },
    'self_containment': {
        'name': 'Self-containment of σ(a)',
        'desc': 'Return induction of "abAAB" has canonical codes = σ',
        'derived_from': ['return_induction'],
        'extra_input': None,
        'movement': 'B532.I3',
    },

    # ── Level 4: from I2 ──
    'projection_algebra': {
        'name': 'Projection algebra (I2)',
        'desc': 'σ irreducibly 4-letter; {aA}|{bB}→φ, {ab}|{AB}→1/√φ',
        'derived_from': ['sigma', 'perron_eigvec'],
        'extra_input': None,
        'movement': 'B532.I2',
    },

    # ── Level 4: from I3 ──
    'two_linear_orbits': {
        'name': 'Two linear orbits on F₂⁴',
        'desc': '{a,b} and {A,B} disjoint 6-cycles, offset 4',
        'derived_from': ['M_mod2'],
        'extra_input': None,
        'movement': 'B532.I3',
    },

    # ── Level 4: from I1 ──
    'period3_absent': {
        'name': 'Period-3 ABSENT from spectrum',
        'desc': 'Complex eigenvalue period ≈ 2.54 (irrational)',
        'derived_from': ['charpoly', 'six_phase_clock'],
        'extra_input': None,
        'movement': 'B532.I1B',
    },

    # ── Requires SL₂C (observer input) ──
    'char_variety': {
        'name': 'Character variety X(F₄, SL₂C)',
        'desc': 'Representation space of F₄ into SL₂C',
        'derived_from': ['sigma'],
        'extra_input': 'SL₂C structure (the observer\'s gauge)',
        'movement': 'B530.XXI',
    },
    'trace_map': {
        'name': '9D trace map',
        'desc': 'Volume-preserving, non-integrable dynamics on X',
        'derived_from': ['char_variety', 'sigma'],
        'extra_input': 'SL₂C structure',
        'movement': 'B530.XXII',
    },
    'fp_variety': {
        'name': 'σ*-fixed point variety',
        'desc': 'Two components: generic isolated + trace-zero family',
        'derived_from': ['trace_map'],
        'extra_input': 'SL₂C structure',
        'movement': 'B532.I1A',
    },

    # ── Requires potential V (observer input) ──
    'schrodinger': {
        'name': 'Schrödinger operator',
        'desc': 'H_V on ℓ²(Z) with potential V(n) from the word',
        'derived_from': ['sigma'],
        'extra_input': 'Potential function V (observer\'s measurement)',
        'movement': 'B530.XXVIII',
    },
    'gap_widths': {
        'name': 'Gap-opening slopes',
        'desc': 's₁≈0.191, s₂≈0.152; gap-3 period-2 oscillation',
        'derived_from': ['schrodinger', 'gap_labels'],
        'extra_input': 'Potential function V',
        'movement': 'B531.T1',
    },

    # ── GL(4,Z) conjugacy (from I3b) ──
    'gl4z_conjugacy': {
        'name': 'GL(4,Z) conjugacy class',
        'desc': 'Pair substitution is GL(4,Z)-conjugate to σ',
        'derived_from': ['M'],
        'extra_input': None,
        'movement': 'B532.I3b',
    },
}


def build_dag():
    """Build and analyze the DAG."""
    # Compute depths (longest path from a source)
    depths = {}
    def get_depth(key):
        if key in depths:
            return depths[key]
        parents = LAYERS[key]['derived_from']
        if not parents:
            depths[key] = 0
            return 0
        d = 1 + max(get_depth(p) for p in parents)
        depths[key] = d
        return d

    for key in LAYERS:
        get_depth(key)

    return depths


def main():
    depths = build_dag()

    print("=" * 78)
    print("B532 I4 — THE DERIVATION DAG")
    print("=" * 78)

    # ── The DAG by depth ──
    max_depth = max(depths.values())
    for d in range(max_depth + 1):
        nodes = [(k, v) for k, v in LAYERS.items() if depths[k] == d]
        print(f"\n{'─'*78}")
        print(f"DEPTH {d}" + (" — SOURCE" if d == 0 else ""))
        print(f"{'─'*78}")
        for key, layer in sorted(nodes, key=lambda x: x[0]):
            parents = layer['derived_from']
            extra = layer['extra_input']
            parent_str = ', '.join(parents) if parents else '(none — source)'
            extra_str = f'  [OBSERVER INPUT: {extra}]' if extra else ''
            print(f"\n  {layer['name']}")
            print(f"    ← {parent_str}{extra_str}")
            print(f"    {layer['desc']}")

    # ── Source nodes (the kernel) ──
    print(f"\n{'='*78}")
    print("THE IRREDUCIBLE KERNEL")
    print(f"{'='*78}")

    sources = [k for k, v in LAYERS.items() if not v['derived_from']]
    print(f"\n  Source nodes: {sources}")
    print(f"  The kernel is: σ (the substitution itself)")
    print(f"  Everything else derives from σ by pure computation,")
    print(f"  EXCEPT layers requiring observer inputs.")

    # ── Observer inputs ──
    print(f"\n{'='*78}")
    print("OBSERVER INPUTS (what the observer must bring)")
    print(f"{'='*78}")

    observer_layers = [(k, v) for k, v in LAYERS.items() if v['extra_input']]
    observer_inputs = set(v['extra_input'] for _, v in observer_layers)
    for inp in sorted(observer_inputs):
        layers_needing = [k for k, v in LAYERS.items() if v['extra_input'] == inp]
        print(f"\n  {inp}:")
        for k in layers_needing:
            print(f"    → {LAYERS[k]['name']}")

    # ── Statistics ──
    print(f"\n{'='*78}")
    print("STATISTICS")
    print(f"{'='*78}")

    n_total = len(LAYERS)
    n_intrinsic = sum(1 for v in LAYERS.values() if v['extra_input'] is None)
    n_observer = n_total - n_intrinsic
    n_sources = len(sources)

    print(f"\n  Total layers: {n_total}")
    print(f"  Intrinsic (from σ alone): {n_intrinsic}")
    print(f"  Observer-dependent: {n_observer}")
    print(f"  Source nodes: {n_sources}")
    print(f"  Max depth: {max_depth}")
    print(f"  Observer inputs needed: {len(observer_inputs)}")

    # ── What σ is STRICTLY MORE than ──
    print(f"\n{'='*78}")
    print("WHAT σ IS STRICTLY MORE THAN")
    print(f"{'='*78}")
    print(f"""
  The charpoly x⁴-2x³-5x²-4x-1 does NOT determine σ:
  - Many substitutions share this charpoly
  - The GL(4,Z) conjugacy class is strictly smaller (the pair substitution
    is conjugate, with the same combinatorial invariants)
  - But even the GL(4,Z) class may not be unique to σ

  σ carries STRICTLY MORE than M:
  - The grammar (7/16) is not determined by M alone
  - The Rauzy fractal shape depends on the specific images
  - The strong-coincidence property depends on the images
  - The self-containment (σ(a) → σ) depends on the specific words
  - The projection algebra (which partitions are Pisot) depends on σ

  σ carries STRICTLY MORE than the grammar:
  - The grammar is a CONSEQUENCE of the images, not vice versa
  - Many substitutions can produce the same 7/16 grammar
  - The specific image lengths (5,3,4,2) are not determined by the grammar

  The irreducible kernel is: THE FOUR WORDS (abAAB, aAB, abAB, aA).
  Not the matrix. Not the polynomial. Not the grammar. The words.
""")

    # ── The prediction form ──
    print(f"{'='*78}")
    print("THE PREDICTION FORM")
    print(f"{'='*78}")
    print(f"""
  Given σ (the four words), EVERYTHING intrinsic is forced:
  - M, frequencies, growth rate, entropy
  - grammar, deciders/couriers, golden section
  - spectral type, gap labels, Rauzy fractal
  - F₂⁴ structure, six-phase clock, 7 types
  - projection algebra, self-containment
  - GL(4,Z) conjugacy class

  Given σ + SL₂C, the representation theory is forced:
  - character variety, trace map, fixed points

  Given σ + V, the spectrum is forced:
  - gap widths, slopes, period-2 oscillation

  THE OBSERVER BRINGS: SL₂C (choice of gauge) and V (choice of coupling).
  EVERYTHING ELSE is forced by the four words.
""")

    # ── Export DAG as adjacency list ──
    print(f"{'='*78}")
    print("DAG EDGES (for reference)")
    print(f"{'='*78}")
    for key in sorted(LAYERS.keys()):
        layer = LAYERS[key]
        for parent in layer['derived_from']:
            extra = f'  [{layer["extra_input"]}]' if layer['extra_input'] else ''
            print(f"  {parent:25s} → {key}{extra}")


if __name__ == '__main__':
    main()
