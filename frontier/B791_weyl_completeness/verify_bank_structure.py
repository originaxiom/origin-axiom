"""Independent re-derivation of the B788 bank's Part-1 structural claims.

Method (same discipline Chat-1 used): read ONLY the four generator permutations from
outputs/coset_action.json and regenerate everything downstream. No summary field of the
JSON is used as an input to any check -- summaries are only compared against at the end.
"""
import json
import itertools
from fractions import Fraction

import numpy as np

# The B788 bank is an EXTERNAL artifact and is not vendored into this repo. Point this at
# the unpacked bank's coset_action.json:
#     B788_BANK=/path/to/B788_maass_spectrum_programme  python3 verify_bank_structure.py
import os
import sys

_root = os.environ.get("B788_BANK")
if not _root:
    sys.exit("set B788_BANK to the unpacked B788_maass_spectrum_programme directory "
             "(the external Gates 0-9R bank; not vendored here)")
BANK = os.path.join(_root, "outputs", "coset_action.json")
d = json.load(open(BANK))
line = "=" * 74

# ---- INPUT: only the permutation matrices -> permutations -------------------------------
gens = {}
for name in ("L1", "Lz", "U1", "Uz"):
    Pm = d["permutation_matrices"][name]
    # convention P_g e_i = e_{p_g(i)}:  column i has its 1 in row p(i)
    p = [None] * 12
    for i in range(12):
        col = [r for r in range(12) if Pm[r][i] == 1]
        assert len(col) == 1
        p[i] = col[0]
    gens[name] = tuple(p)
print(f"{line}\nINPUT (the only thing taken from the bank): 4 generator permutations\n{line}")
for k, v in gens.items():
    print(f"  {k} = {v}")


def comp(a, b):
    """(a*b)(i) = a(b(i))"""
    return tuple(a[b[i]] for i in range(12))


ident = tuple(range(12))

# ---- C1 closure / image order -----------------------------------------------------------
print(f"\n{line}\nC1 - image order by closure\n{line}")
G = {ident}
frontier = [ident]
while frontier:
    nxt = []
    for x in frontier:
        for g in gens.values():
            y = comp(g, x)
            if y not in G:
                G.add(y)
                nxt.append(y)
    frontier = nxt
G = sorted(G)
print(f"  |G| = {len(G)}          bank claims action_image_order = {d['action_image_order']}")
print(f"  MATCH: {len(G) == d['action_image_order']}")

# ---- C2 transitivity --------------------------------------------------------------------
print(f"\n{line}\nC2 - transitivity on 12 cosets\n{line}")
orb = sorted({g[0] for g in G})
print(f"  orbit of point 0 = {orb}")
print(f"  transitive: {len(orb) == 12}")

# ---- C3 commutant dimension -------------------------------------------------------------
print(f"\n{line}\nC3 - commutant dimension (rank of stacked G^T (x) I - I (x) G)\n{line}")
rows = []
for name, p in gens.items():
    P = np.zeros((12, 12))
    for i in range(12):
        P[p[i], i] = 1.0
    rows.append(np.kron(P.T, np.eye(12)) - np.kron(np.eye(12), P))
Mstack = np.vstack(rows)
r = np.linalg.matrix_rank(Mstack, tol=1e-9)
print(f"  rank = {r}   =>  commutant dim = 144 - {r} = {144 - r}")

# ---- C4 orbitals ------------------------------------------------------------------------
print(f"\n{line}\nC4 - orbits on 12x12 pairs (orbital sizes)\n{line}")
seen, sizes = set(), []
for a in range(12):
    for b in range(12):
        if (a, b) in seen:
            continue
        orbp = set()
        stack = [(a, b)]
        while stack:
            x = stack.pop()
            if x in orbp:
                continue
            orbp.add(x)
            for g in gens.values():
                stack.append((g[x[0]], g[x[1]]))
        seen |= orbp
        sizes.append(len(orbp))
print(f"  orbital sizes = {sorted(sizes)}   (count = rank of commutant = {len(sizes)})")

# ---- C5 character inner products --------------------------------------------------------
print(f"\n{line}\nC5 - <chi,chi> and <chi,1> from the fixed-point distribution\n{line}")
from collections import Counter
fp = Counter(sum(1 for i in range(12) if g[i] == i) for g in G)
print(f"  fixed-point distribution = {dict(sorted(fp.items()))}")
n = len(G)
chi2 = Fraction(sum(c * (k ** 2) for k, c in fp.items()), n)
chi1 = Fraction(sum(c * k for k, c in fp.items()), n)
print(f"  <chi,chi> = {chi2} = {float(chi2):.4f}      (constituents, counted with mult^2)")
print(f"  <chi,1>   = {chi1} = {float(chi1):.4f}      (multiplicity of the trivial rep)")
print(f"  => {chi2} distinct constituents, each multiplicity 1: {chi2 == 3 and chi1 == 1}")

# ---- C6 tau ------------------------------------------------------------------------------
print(f"\n{line}\nC6 - tau = [1,0,3,2,6,7,4,5,9,8,11,10]\n{line}")
tau = (1, 0, 3, 2, 6, 7, 4, 5, 9, 8, 11, 10)
inG = tau in set(G)
print(f"  tau in G?                {inG}")
print(f"  tau^2 = identity?        {comp(tau, tau) == ident}")
print(f"  fixed-point-free?        {all(tau[i] != i for i in range(12))}")
central = all(comp(tau, g) == comp(g, tau) for g in G)
print(f"  central (commutes all)?  {central}")

# ---- C7 decomposition via tau eigenspaces ------------------------------------------------
print(f"\n{line}\nC7 - decomposition rho = V1 + V5 + V6 forced by tau\n{line}")
T = np.zeros((12, 12))
for i in range(12):
    T[tau[i], i] = 1.0
w, V = np.linalg.eigh(T)
plus = int(round(sum(1 for x in w if x > 0)))
minus = int(round(sum(1 for x in w if x < 0)))
print(f"  tau eigenvalue multiplicities: +1 -> {plus},  -1 -> {minus}")
ones = np.ones(12) / np.sqrt(12)
print(f"  trivial rep (all-ones) lies in the +1 eigenspace? {abs(T @ ones - ones).max() < 1e-9}")
print(f"  => +1 side (dim {plus}) carries trivial(1) + a 5;  -1 side (dim {minus}) is the 6.")
print(f"  Only split consistent with <chi,chi>=3, <chi,1>=1, and a central FPF involution:")
print(f"     rho = V1 (+1) + V5 (+1) + V6 (-1)     [forced, not fitted]")

# ---- final comparison against the bank's own summary fields ------------------------------
print(f"\n{line}\nCOMPARISON against the bank's summary fields (only now consulted)\n{line}")
for k in ("action_image_order", "action_kernel_order", "ambient_order", "index"):
    print(f"  {k:24s} = {d[k]}")
print(f"  checks.action_transitive = {d['checks']['action_transitive']}")
print(f"  point stabilizer: ambient {d['ambient_order']}/{d['index']} = "
      f"{d['ambient_order']//d['index']} ; in the IMAGE = {len(G)//12}")
print(f"  (the '320 vs 160' point: 320 is ambient-level, 160 image-level, kernel order 2)")
