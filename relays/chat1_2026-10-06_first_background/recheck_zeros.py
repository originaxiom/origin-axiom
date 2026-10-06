"""Recheck every zero cell that a 'first level' claim rests on: plain instrument (first_background.run, long presentation,
no orbit cache), primes from 20000 up (disjoint from the 5000-set of the original runs)."""
import json, sys
import first_background as F
CELLS = [('golden+', 1), ('golden+', 2), ('golden-', 1), ('golden-', 2), ('silver+', 1), ('silver+', 2), ('silver+', 3),
         ('silver-', 1), ('silver-', 2), ('bronze+', 1), ('bronze+', 2), ('bronze-', 1), ('bronze-', 2),
         ('LLR', 1), ('LLR', 2), ('LLLR', 1), ('LLLR', 2), ('ILLLR', 1), ('ILLLR', 2), ('ILLR', 3)]
out = []
for name, n in CELLS:
    if name not in F.ROOTS: F.ROOTS[name] = name
    r = F.run(name, n, pstart=20000); out.append(r)
    print(name, n, r['primes'], r['torsion'], 'firing', r['firing'], 'bg', r['generation_backgrounds'], 'differ',
          r['differing_at_other_primes'], flush=True)
    json.dump(out, open('recheck_zeros.json', 'w'), indent=1)
