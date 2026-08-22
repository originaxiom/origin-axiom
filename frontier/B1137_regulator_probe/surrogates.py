"""STEP 4 -- matched-null surrogate generator.

Per sec D of the sealed prereg: surrogates are drawn from the SAME measure the criterion uses --
"products of {pi,sqrt3,sqrt5,zeta(3),logphi} and the regulators with random bounded-height
rational coefficients", matched to the real targets' range + digit-precision "type".

Construction (documented choice -- WORKING_RULES rule 4, declare every choice):
  1. Pick k in {2,3,4} basis elements at random from the FULL pruned basis (regulators+constants).
  2. Assign each a random rational coefficient num/den, num in [-9,9]\\{0}, den in [1,9]
     ("bounded-height rational coefficients").
  3. Sum to an EXACT high-precision value S_exact = sum(num_i/den_i * basis_i).
  4. Draw a (digit-class, rel_unc, order-of-magnitude) triple from the EMPIRICAL joint
     distribution of the 18 real PDG targets (this is what "matched range + type" means
     operationally: the surrogate's measured precision and scale mimic a real target's).
  5. Rescale S_exact by a random sign and a power of 10 so its magnitude lands in the chosen
     order-of-magnitude decade, then TRUNCATE to the chosen digit-class -- this is the step that
     makes the null non-trivial: truncation destroys the exact planted relation, so any relation
     PSLQ subsequently reports at full working precision is, by construction, EITHER a numerical
     artifact of under-constrained search OR a coincidental low-precision match -- exactly the
     false-positive phenomenon STEP 4 needs to rate.
  6. Return (S_test, digits, rel_unc) formatted exactly like a real target row, so the IDENTICAL
     grid + gates can run over it.
"""
import random
from mpmath import mp, mpf, nstr

def empirical_target_stats(targets):
    """(digits, rel_unc, order-of-magnitude-decade) triples from the real 18 targets."""
    stats = []
    for t in targets:
        v = abs(float(t['value']))
        decade = 0
        if v > 0:
            import math
            decade = math.floor(math.log10(v))
        stats.append((t['digits'], t['rel_unc'], decade))
    return stats

def make_surrogate(rng, basis_dict, basis_keys, stats, dps):
    old = mp.dps
    mp.dps = dps + 30
    try:
        k = rng.randint(2, 4)
        chosen = rng.sample(basis_keys, k)
        terms = []
        val = mpf(0)
        for key in chosen:
            num = rng.choice([i for i in range(-9, 10) if i != 0])
            den = rng.randint(1, 9)
            c = mpf(num) / mpf(den)
            terms.append((key, num, den))
            val += c * mp.mpf(basis_dict[key])
        digits, rel_unc, decade = stats[rng.randrange(len(stats))]
        if val == 0:
            val = mpf('1e-30')
        cur_decade_f = mp.log(abs(val), 10)
        cur_decade = int(mp.floor(cur_decade_f))
        shift = decade - cur_decade
        val_scaled = val * mpf(10) ** shift
        sign = rng.choice([1, -1])
        val_scaled = abs(val_scaled) * sign
        d_use = max(int(digits), 1)  # PSLQ needs >=1 sig fig to even form a number
        val_str = nstr(val_scaled, d_use, strip_zeros=False)
        val_test = mpf(val_str)
        return {
            'name': f'surrogate[{",".join(f"{n}/{d}*{k}" for k,n,d in terms)}]*1e{shift}',
            'value': val_str,
            'value_mpf': val_test,
            'rel_unc': rel_unc,
            'digits': int(digits),
            'planted_terms': terms,
        }
    finally:
        mp.dps = old

def make_n_surrogates(n, basis_dict, basis_keys, real_targets, dps, seed):
    rng = random.Random(seed)
    stats = empirical_target_stats(real_targets)
    return [make_surrogate(rng, basis_dict, basis_keys, stats, dps) for _ in range(n)]

if __name__ == '__main__':
    import sys, json
    sys.path.insert(0, '.')
    import basis as basismod
    import targets as targetsmod
    b, forms, R = basismod.build_pruned_basis(dps=90)
    real_targets, sha = targetsmod.load_targets()
    surs = make_n_surrogates(8, b, forms['FULL'], real_targets, dps=90, seed=17)
    for s in surs:
        print(f"{s['name'][:70]:70s} value={s['value']:>14s} digits={s['digits']}")
