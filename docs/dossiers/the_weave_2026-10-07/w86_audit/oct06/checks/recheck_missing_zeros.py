"""Audit: the zero cells that the first-level table rests on but recheck_zeros.py did not include, rerun with the plain
instrument (first_background.run unchanged: long presentation, no orbit cache) at primes from 20000 up."""
import sys, json
sys.path.insert(0, sys.argv[1])
import first_background as F
CELLS = [('ILRLR', 1), ('LLLRR', 1), ('ILLLRR', 1), ('LLRLR', 1), ('LLLLLR', 1), ('ILLLLLR', 1), ('LLLLRR', 1), ('ILLLLRR', 1),
         ('LLLRLR', 1), ('ILLR', 1), ('ILLR', 2), ('LLLLR', 1), ('LLLLR', 2), ('ILLLLR', 1), ('ILLLLR', 2)]
out = []
for name, n in CELLS:
    F.ROOTS[name] = name
    r = F.run(name, n, pstart=20000); out.append(r)
    print(name, n, r['primes'], r['torsion'], 'firing', r['firing'], 'bg', r['generation_backgrounds'], 'differ', r['differing_at_other_primes'], r['seconds'], 's', flush=True)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
