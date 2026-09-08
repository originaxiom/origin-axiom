#!/usr/bin/env python3
"""B1302's vacuum census on Y_15's survival patterns (from the structural line count): the odd-alphabet closing keeps
the colour triplet everywhere, so no configuration should go below two light triplet pairs (as on Y_9)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / 'B1302_the_one_triplet_vacua' / 'verification'))
import odd_alphabet_lines as O
import one_triplet_vacua as V
r = O.run(HERE / 'support_mt_Y15.json', 'Y_15')
out = V.analyse(r['patterns'], 'Y_15')
print(f"\nY_15: minimal light triplet pairs over all configurations with a light doublet pair: {out['minT']}; patterns {out['n_patterns']}")
print("SELFTEST:", "PASS" if out['minT'] == 2 and out['n_patterns'] == 67 else "FAIL")
