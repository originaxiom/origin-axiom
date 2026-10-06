"""Second seal (PREREGISTRATION_2_ORBIT_LAW.md): levels 1-2 on the sample, level 3 on four new roots."""
import sys, json, math, itertools
import first_background as F
def canon(w):
    sw = w.translate(str.maketrans('LR', 'RL'))
    return min(min(x[i:] + x[:i] for i in range(len(x))) for x in (w, sw, w[::-1], sw[::-1]))
words = sorted({canon(''.join(t)) for k in range(2, 7) for t in itertools.product('LR', repeat=k)
                if 'L' in t and 'R' in t}, key=lambda s: (len(s), s))
prod = lambda t: math.prod(t) if t else 1
sample = [sg + w for w in words for sg in ('', 'I') if prod(F.torsion(F.mono(sg + w), 2)[0]) <= 200]
L3 = ['LLR', 'ILLR', 'LLLR', 'ILLLR']
if __name__ == '__main__':
    print('sample', len(sample), sample, flush=True)
    jobs = [(r, n) for r in sample for n in (1, 2)] + [(r, 3) for r in L3]
    out = []
    for r, n in jobs:
        F.ROOTS[r] = r
        res = F.run(r, n); out.append(res)
        print(r, n, res['torsion'], 'firing', res['firing'], 'bg', res['generation_backgrounds'], 'lifted', res['lifted'],
              'orbits', res['backgrounds_by_orbit_size'], 'differ', res['differing_at_other_primes'], flush=True)
        json.dump(out, open('orbit_law.json', 'w'), indent=1)
