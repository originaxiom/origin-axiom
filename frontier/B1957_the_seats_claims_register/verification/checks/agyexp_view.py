"""B1957: agy-exp's view on selection and the dictionary (relays/AGY-EXP_VIEW_ON_SELECTION_AND_DICTIONARY.md, committed
2026-11-15 13:39 +0100), the exact statements it marks as established, computed by main (2026-11-18; data-free).
 V1  the bigraded exterior algebra of C^3 + C^2 with Q6 = 3q - 2p: the six summands of even total degree, their
     dimensions and charges, against the record's charges (B1936's table); the sum of dimensions; the Higgs's summand;
     the duality (p, q) -> (3 - p, 2 - q); the generator's trace on C^5.
 V2  the pairs of even summands that pair with the Higgs's summand into the top form, by wedge (p sum 3, q sum 1) and
     by contraction (p sum 3, q sum 3), and their charge sums.
 V3  for T_m = [[m, 1], [1, 0]]: det(T_m - 1) and det(-T_m^2 - 1) as polynomials in m."""
import itertools, math, pathlib, re, sympy as sp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
Q6 = lambda p, q: 3 * q - 2 * p; dim = lambda p, q: math.comb(3, p) * math.comb(2, q)
even = [(p, q) for p in range(4) for q in range(3) if (p + q) % 2 == 0]
table = {pq: (dim(*pq), Q6(*pq)) for pq in even}
src = (next((ROOT / "frontier").glob("B1936_*")) / "verification/degrees.py").read_text()
Y6 = eval(re.search(r"^Y6 = (\{.*\})$", src, re.M).group(1)); record = sorted(v for k, v in Y6.items() if k != "H")
mult = {1: 6, -4: 3, 2: 3, -3: 2, 6: 1, 0: 1}
print("V1: even summands (p, q): (dimension, Q6) = %s; total dimension %d; their charges %s against the record's %s: %s; dimensions by charge as the record's multiplets (6, 3, 3, 2, 1, 1): %s; the Higgs's summand (0, 1): dimension %d, Q6 = %d against the record's %d; duality negates Q6 on all twelve summands: %s; trace of the generator on C^5: %d"
      % (table, sum(d for d, _ in table.values()), sorted(c for _, c in table.values()), record, sorted(c for _, c in table.values()) == record, all(mult[c] == d for d, c in table.values()), dim(0, 1), Q6(0, 1), Y6["H"],
         all(Q6(3 - p, 2 - q) == -Q6(p, q) for p in range(4) for q in range(3)), 3 * (-2) + 2 * 3))
wedge = [(a, b) for a, b in itertools.combinations_with_replacement(even, 2) if a[0] + b[0] == 3 and a[1] + b[1] == 1]
contr = [(a, b) for a, b in itertools.combinations_with_replacement(even, 2) if a[0] + b[0] == 3 and a[1] + b[1] == 3]
print("V2: by wedge with the Higgs: %s, charge sums with +3: %s; by contraction: %s, charge sums with -3: %s"
      % (wedge, [Q6(*a) + Q6(*b) + 3 for a, b in wedge], contr, [Q6(*a) + Q6(*b) - 3 for a, b in contr]))
m = sp.symbols("m"); Tm = sp.Matrix([[m, 1], [1, 0]])
print("V3: det(T_m - 1) = %s; det(-T_m^2 - 1) = %s; at m = 1: %s and %s" % (sp.expand((Tm - sp.eye(2)).det()), sp.expand((-Tm ** 2 - sp.eye(2)).det()), (Tm - sp.eye(2)).det().subs(m, 1), (-Tm ** 2 - sp.eye(2)).det().subs(m, 1)))
