r"""R12 — THE ELIGIBILITY SCREEN: which targets can a quantized emitter ever hit?

WHY THIS EXISTS
---------------
Four sealed crossings, four failures. The first three had named METHODOLOGICAL
defects (B915 assumed interpolation, B925 wrong hemisphere, B929 missing
normalisation) and R1-R11 were built to fix them. They worked: B1027 was
methodologically clean -- sealed before data contact, prior MISS declared and
held, ZERO anchors consumed, all eleven requirements cited.

It missed at 11.4 sigma and 38.0 sigma.

When a clean crossing fails that hard, the remaining defect is not in HOW
crossings are run. It is in WHICH TARGETS ARE ELIGIBLE.

THE CONSTRAINT, ALREADY PROVED AND NEVER APPLIED TO TARGET SELECTION
--------------------------------------------------------------------
chat1's resolution bound: any FORCED value = Re chi_V(M)/dim V -- a CHARACTER
value of a finite group. B1011 makes the set explicit. The object's dimensionless
outputs are QUANTIZED to eight values. SM parameters are generic reals.

Screening the two numeric targets that were actually run:
  B929  |V_us| = 0.2265  -> nearest forced value 0.25,   gap 10.4%
  B1027 cos d13 = 0.3616 -> nearest forced value 0.4045, gap 11.9%
NEITHER was in the set. BOTH were run anyway. Nothing in R1-R11 checks this.

AND THE BASE RATE MAKES NEAR-MISSES WORTHLESS
----------------------------------------------
With 8 values in [0,1], a RANDOM target lands within 5% of one 52% of the time;
within 3%, 35%; within 1%, 13%. Mean gap 6.3%. So "close" is the default, and a
margin reported without this number overstates itself by construction.

THE DESIGNER FREEDOM, DECLARED BEFORE LOOKING
----------------------------------------------
Each parameter must be mapped into [0,1] to be compared. THE CHOICE OF MAP IS A
FREEDOM, and trying several rebuilds the look-elsewhere problem one level up. So
ONE canonical map per TYPE is fixed here, in advance:

  angle theta            -> cos(theta)          (B1027's own convention)
  mixing-matrix element  -> |V| directly        (already in [0,1])
  ratio r                -> r if r<=1 else 1/r  (no other folding)
  everything else        -> EXCLUDED, not mapped

Any other map is a SECOND trial and must be priced as one. This file tries
exactly one map per parameter and reports the whole list, not a selection.

GATE 5-Q. This is a SCREENING INSTRUMENT. It asserts no physical claim, selects
no crossing, and nothing here goes to CLAIMS.md. Measured values are inputs to a
filter, not outputs of a derivation.
"""
import math
import random

PHI = (1 + 5 ** 0.5) / 2

# B1011's banked theta-even forced value set -- the coupling channel's.
FORCED = sorted({0.0, 0.25, 1 / (4 * PHI), 0.5, 1 / (2 * PHI),
                 PHI / 4, PHI / 2, 1.0})

# (name, measured value, 1-sigma, map type). Values are standard PDG/NuFIT
# figures used ONLY as filter inputs.
TARGETS = [
    ('|V_us|',              0.2243,  0.0008, 'elt'),
    ('|V_cb|',              0.0410,  0.0014, 'elt'),
    ('|V_ub|',              0.00382, 0.00020, 'elt'),
    ('|V_td|',              0.0086,  0.0002, 'elt'),
    ('quark delta_13 (deg)', 68.8,    4.5,   'angle'),
    ('theta_12 PMNS (deg)',  33.4,    0.8,   'angle'),
    ('theta_23 PMNS (deg)',  49.0,    1.3,   'angle'),
    ('theta_13 PMNS (deg)',   8.57,   0.12,  'angle'),
    ('delta_CP PMNS (deg)',  197.0,   40.0,  'angle'),
    ('sin^2 theta_W',        0.23122, 0.00004, 'ratio'),
    ('m_u/m_d',              0.47,    0.05,  'ratio'),
    ('m_s/m_d',             19.5,     2.5,   'ratio'),
    ('m_e/m_mu',             0.00484, 0.00001, 'ratio'),
    ('m_mu/m_tau',           0.0595,  0.0001, 'ratio'),
]


def canonical_map(v, kind):
    """ONE map per type, fixed before looking. Returns None if not mappable."""
    if kind == 'angle':
        return abs(math.cos(math.radians(v)))
    if kind == 'elt':
        return v if 0 <= v <= 1 else None
    if kind == 'ratio':
        return v if v <= 1 else 1 / v
    return None


def gap(x):
    return min(abs(x - f) for f in FORCED)


def base_rate(n=200000, seed=12):
    """P(a uniform random target lands within d of some forced value)."""
    rng = random.Random(seed)
    ds = sorted(gap(rng.random()) for _ in range(n))
    return ds


def main():
    print('R12 — THE ELIGIBILITY SCREEN')
    print('=' * 74)
    print(f'  forced set ({len(FORCED)} values): {[round(f, 4) for f in FORCED]}')

    ds = base_rate()
    n = len(ds)
    p = lambda d: sum(1 for x in ds if x < d) / n
    print(f'\n  BASE RATE — a RANDOM target lands within:')
    for d in (0.01, 0.03, 0.05, 0.10):
        print(f'    {d*100:>4.0f}%  of a forced value : {100*p(d):5.1f}% of the time')
    print(f'    mean gap for a random target : {sum(ds)/n:.4f}')

    print(f'\n  THE WHOLE LIST — one declared map each, no selection:\n')
    print(f'  {"target":22}{"mapped":>9}{"nearest":>9}{"gap":>8}{"gap<1sig?":>11}'
          f'{"P(random does better)":>22}')
    rows = []
    for name, v, sig, kind in TARGETS:
        x = canonical_map(v, kind)
        if x is None:
            print(f'  {name:22}{"EXCLUDED -- no declared map for this type":>50}')
            continue
        g = gap(x)
        near = min(FORCED, key=lambda f: abs(x - f))
        # propagate 1-sigma through the same declared map
        if kind == 'angle':
            xs = abs(math.cos(math.radians(v + sig)))
            smap = abs(xs - x)
        elif kind == 'ratio' and v > 1:
            smap = abs(1 / (v + sig) - x)
        else:
            smap = sig
        elig = g <= smap
        better = p(g)
        rows.append((name, g, elig, better))
        print(f'  {name:22}{x:9.4f}{near:9.4f}{g:8.4f}'
              f'{("YES" if elig else "no"):>11}{100*better:>21.1f}%')

    elig = [r for r in rows if r[2]]
    print(f'\n{"=" * 74}')
    print(f'  ELIGIBLE (gap within the target\'s own 1-sigma): {len(elig)} of {len(rows)}')
    for name, g, _, better in elig:
        print(f'    {name}   gap {g:.5f}   but a random target does better '
              f'{100*better:.1f}% of the time')
    if not elig:
        print('    NONE.')
    print(f'\n  READ THIS CORRECTLY:')
    print(f'  * eligibility is NECESSARY, never sufficient — the base-rate column')
    print(f'    is why. A small gap against 8 quantized values is cheap.')
    print(f'  * the whole list is printed. Choosing a target AFTER reading it is')
    print(f'    post-hoc selection (E29) and must be priced as such.')
    print(f'  * ONE map per type was fixed before looking. Any other map is a')
    print(f'    SECOND trial and multiplies the look-elsewhere budget.')
    print(f'  * FORCED is the COUPLING channel\'s set (B1011). R10/B1016 require a')
    print(f'    crossing to declare its channel; this screen applies PER CHANNEL,')
    print(f'    and cc3 holds only this one.')
    print('=' * 74)


if __name__ == '__main__':
    main()
