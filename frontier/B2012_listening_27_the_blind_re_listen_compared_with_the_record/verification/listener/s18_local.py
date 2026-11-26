# s18_local.py -- integer leaves with no integer point in the box |coords|<=240 (from s04): are they excluded by a
# congruence (X_k(Z/n) empty for some n in the list) or do they have points mod every n tested?
import re, numpy as np
nopts = []
for l in open('s04_integer_orbits.out'):
    m = re.search(r'k=\s*(-?\d+)\s+orbits\(with a point of height<=30\)=\s*(\d+)', l)
    if int(m.group(2)) == 0: nopts.append(int(m.group(1)))
mods = [4, 8, 16, 32, 64, 9, 27, 81, 243, 5, 25, 125, 7, 49, 11, 13]
present = {}
for n in mods:
    r = np.arange(n, dtype=np.int64)
    X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
    present[n] = set(np.unique((X*X + Y*Y + Z*Z - X*Y*Z) % n).tolist())
print("k values mod 4 attained:", sorted(present[4]), " mod 8:", sorted(present[8]), " mod 9:", sorted(present[9]), " mod 27 missing:", sorted(set(range(27)) - present[27]))
print("mod 16 missing:", sorted(set(range(16)) - present[16]), " mod 32 missing:", sorted(set(range(32)) - present[32]), " mod 81 missing:", sorted(set(range(81)) - present[81]))
unexpl = []
for kv in nopts:
    obs = [n for n in mods if (kv % n) not in present[n]]
    if not obs: unexpl.append(kv)
    else: pass
print("k in [-60,130] with no integer point in the box:", len(nopts))
print("  of these, excluded by some modulus in", mods, ":", len(nopts) - len(unexpl))
print("  with points modulo every listed modulus (no congruence obstruction found):", unexpl)
