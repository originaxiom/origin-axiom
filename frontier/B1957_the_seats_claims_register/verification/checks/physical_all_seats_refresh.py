"""B1957: the physical lane's package 'all seats refresh' (2026-11-15), its review of every branch and its priorities
note: the arithmetic it checks by hand, on main.  Nothing of any seat's is run.
 W0  custody (needs the seats' branches fetched): the head its coverage table names for each branch is a commit of that
     branch.
 W1  the Weil split: with the parity P = diag(1, 1, 1, -1, -1), (1 - 5P)/2 = diag(-2, -2, -2, 3, 3); the even exterior
     algebra's sixteen states and their charges; the four anomaly sums vanish.
 W2  for eigenvalues a (three times) and b (twice): the mixed and gravitational anomalies are 3a + 2b, 3a + 2b and
     8(3a + 2b), and the cubic one 4(3a + 2b)(9a^2 + 6ab + 5b^2); shifted by -(3a + 2b)/2 at a = b = 1 the charges are
     -5/2, -1/2, 3/2 with multiplicities 1, 10, 5 and vanishing linear and cubic sums.
 W3  the one-loop eliminant: with b = (4N/3 + 1/10, 4N/3 - 43/6, 4N/3 - 11) and c = (23/6, -111/10, 109/15): sum c = 0
     and c.b = 0 for every N.
 W4  the charge arithmetic: (-3, 6) = (2, 1) modulo 5; 6 = 0 mod 3 and 1 mod 5; (6, 12) exchanged is (-3, 6) modulo 15;
     no c modulo 10 has (c, 2c) = (7, 6) or (6, 7); -15 w is integral on the 15-torsion.
 W5  the projector: the integral of exp(2 pi i x/5) over [0, 1] is not zero; the finite sum over (Z/N)^2 of
     exp(2 pi i <v, z>/N), divided by N^2, is 1 when v = 0 modulo N and 0 otherwise."""
import functools, itertools, cmath, math, subprocess
from fractions import Fraction as Fr
import sympy as sp
print = functools.partial(print, flush=True)

def content(a, b):
    """the even exterior algebra of C^3 + C^2 with charges a, b: (multiplicity, charge, colour triplets?, weak doublets?)"""
    out = []
    for k3 in range(4):
        for k2 in range(3):
            if (k3 + k2) % 2: continue
            out.append((math.comb(3, k3) * math.comb(2, k2), k3 * a + k2 * b, k3 in (1, 2), k2 == 1, math.comb(3, k3), math.comb(2, k2)))
    return out

if __name__ == "__main__":
    tab = subprocess.run(["git", "show", "8d5c91032:reports/physical_bridge_2026_09_05/all_seats_refresh_2026_11_15/COVERAGE.md"], capture_output=True).stdout.decode()
    rows = [l.split("|") for l in tab.split("\n") if l.startswith("| `origin/")]
    if rows:
        okh = sum(subprocess.run(["git", "merge-base", "--is-ancestor", r[2].strip().strip("`"), r[1].strip().strip("`")], capture_output=True).returncode == 0 for r in rows)
        print("W0: the coverage table: %d branches; the head named is a commit of that branch for %d" % (len(rows), okh))
    else: print("W0: the lane's branch is not fetched here; custody not checked")
    P = sp.diag(1, 1, 1, -1, -1); Y6 = (sp.eye(5) - 5 * P) / 2; C = content(-2, 3)
    lin = sum(m * q for m, q, *_ in C); cub = sum(m * q ** 3 for m, q, *_ in C); su3 = sum(Fr(1, 2) * q * d2 for m, q, t3, t2, d3, d2 in C if t3); su2 = sum(Fr(1, 2) * q * d3 for m, q, t3, t2, d3, d2 in C if t2)
    print("W1: (1 - 5P)/2 = diag%s; the even exterior algebra: %d states, (multiplicity, charge): %s; linear, cubic, SU(3)^2 and SU(2)^2 sums: %s, %s, %s, %s" % (tuple(Y6[i, i] for i in range(5)), sum(m for m, *_ in C), [(m, q) for m, q, *_ in C], lin, cub, su3, su2))
    a, b = sp.symbols("a b"); Cs = content(a, b)
    A3 = sp.expand(sum(sp.Rational(1, 2) * q * d2 for m, q, t3, t2, d3, d2 in Cs if t3)); A2 = sp.expand(sum(sp.Rational(1, 2) * q * d3 for m, q, t3, t2, d3, d2 in Cs if t2)); Ag = sp.factor(sum(m * q for m, q, *_ in Cs)); Ac = sp.factor(sum(m * q ** 3 for m, q, *_ in Cs))
    sh = [(m, q.subs({a: 1, b: 1}) - sp.Rational(5, 2)) for m, q, *_ in Cs]; byq = {}
    for m, q in sh: byq[q] = byq.get(q, 0) + m
    print("W2: SU(3)^2: %s; SU(2)^2: %s; gravitational: %s; cubic: %s; shifted at a = b = 1: %s, linear sum %s, cubic sum %s" % (A3, A2, Ag, Ac, {str(k): v for k, v in sorted(byq.items())}, sum(m * q for m, q in sh), sum(m * q ** 3 for m, q in sh)))
    N = sp.symbols("N"); bb = (sp.Rational(4, 3) * N + sp.Rational(1, 10), sp.Rational(4, 3) * N - sp.Rational(43, 6), sp.Rational(4, 3) * N - 11); cc = (sp.Rational(23, 6), -sp.Rational(111, 10), sp.Rational(109, 15))
    print("W3: sum c = %s; c.b = %s; at N = 3 the slopes are %s" % (sum(cc), sp.simplify(sum(x * y for x, y in zip(cc, bb))), [x.subs(N, 3) for x in bb]))
    lvl10 = [c for c in range(10) if (c % 10, 2 * c % 10) in ((7, 6), (6, 7))]
    print("W4: (-3, 6) mod 5 = %s; 6 mod 3 and mod 5: %s; (6, 12) exchanged mod 15: %s, and (-3, 6) mod 15: %s; solutions at level 10: %s; -15 w integral on the 15-torsion: %s" % (((-3) % 5, 6 % 5), (6 % 3, 6 % 5), (12 % 15, 6 % 15), ((-3) % 15, 6 % 15), lvl10, all((-15 * Fr(p, 15)).denominator == 1 for p in range(15))))
    integ = (cmath.exp(2j * math.pi / 5) - 1) / (2j * math.pi / 5); Nn = 5; proj = lambda v: abs(sum(cmath.exp(2j * math.pi * (v[0] * z0 + v[1] * z1) / Nn) for z0 in range(Nn) for z1 in range(Nn)) / Nn ** 2)
    print("W5: the integral has modulus %.4f; the finite sum at v = (0, 0), (5, 10), (1, 0), (2, 3): %s" % (abs(integ), [round(proj(v), 12) for v in ((0, 0), (5, 10), (1, 0), (2, 3))]))
