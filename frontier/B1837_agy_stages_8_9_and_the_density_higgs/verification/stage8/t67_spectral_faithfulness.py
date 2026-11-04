"""S302 check of the lane's Theorem 67 ('Spectral Faithfulness'), exact arithmetic, main's laws only:
(1) the mod-5 chiral-transpose orbits of the sector charges (up (1,-4), down (1,2), lepton (-3,6));
(2) the criterion 'the self-transpose orbit and the transpose pair get distinct exponents' evaluated with BOTH of main's
    exponent laws:
      (i)  the channel-class gaps of the channel-exponent law (LAW_MAP's B1832 S300 row; B1836 slope_gaps_exact.py), and
      (ii) B1788's closed form of the second-generation exponent e(m2/m3) = 1/2 - (||2 q_L a|| + ||2 q_R a||)/2 on DR;
    on the lane's domain {1/5, 2/5} and on main's B1836 domain (N | 4 or 5, a in (0, 1/2]);
(3) the steepness lemma: (||4a|| - ||8a||)/2 > 0 iff ||4a|| > 1/3, its maximum 1/4 and where, on all reduced slopes with
    denominator <= 60; and that e_up - e_down from B1788's closed form equals (||4a|| - ||8a||)/2.
No held-out quantity enters (within-sector exponents only)."""
from fractions import Fraction as F
from math import gcd

def nn(x):
    x = x - (x.numerator // x.denominator); return min(x, 1 - x)
CH = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}

def chan_gaps(al):                                     # B1836 slope_gaps_exact.py, verbatim law
    out = {}
    for s, (ql, qr) in CH.items():
        e = {(a, b): nn(ql * al + F(a, 2)) ** 2 + nn(qr * al + F(b, 2)) ** 2 - F(1, 8) for a in (0, 1) for b in (0, 1)}
        out[s] = abs(min(e[0, 0], e[1, 1]) - min(e[0, 1], e[1, 0]))
    return out

def e1788(al):                                         # B1788 closed form, m2/m3 exponent on DR
    return {s: F(1, 2) - (nn(2 * ql * al) + nn(2 * qr * al)) / 2 for s, (ql, qr) in CH.items()}

# (1) orbits mod 5
m5 = {s: (ql % 5, qr % 5) for s, (ql, qr) in CH.items()}
print("charges mod 5:", m5, "; up self-transpose:", m5["up"] == m5["up"][::-1],
      "; down/lepton transposes:", m5["down"] == m5["lep"][::-1])
m4 = {s: (ql % 4, qr % 4) for s, (ql, qr) in CH.items()}
print("charges mod 4 (for main's wider domain):", m4)

def faithful(ex):                                      # orbit O_self = {up}, O_pair = {down, lep}
    return ex["up"] != ex["down"] or ex["up"] != ex["lep"]

for name, law in (("channel-class gaps (LAW_MAP / B1836)", chan_gaps), ("B1788 e(m2/m3) on DR", e1788)):
    for dom_name, dom in (("lane {1/5, 2/5}", [F(1, 5), F(2, 5)]), ("main N|4 or 5 in (0,1/2]", [F(1, 2), F(1, 4), F(1, 5), F(2, 5)])):
        rows = {str(a): {k: str(v) for k, v in law(a).items()} for a in dom}
        print("%-38s %-26s values %s -> 'faithful': %s" % (name, dom_name, rows, [str(a) for a in dom if faithful(law(a))]))

# (3) the steepness lemma and its identity with B1788
sl = [F(p, N) for N in range(2, 61) for p in range(1, N) if gcd(p, N) == 1 and F(p, N) < F(1, 2)]
bad_lemma = [a for a in sl if ((nn(4 * a) - nn(8 * a)) / 2 > 0) != (nn(4 * a) > F(1, 3))]
bad_ident = [a for a in sl if e1788(a)["up"] - e1788(a)["down"] != (nn(4 * a) - nn(8 * a)) / 2]
gmax = max((nn(4 * a) - nn(8 * a)) / 2 for a in sl)
print("slopes in (0,1/2), N<=60:", len(sl), "; lemma failures:", len(bad_lemma), "; B1788 identity failures:", len(bad_ident),
      "; max gap", gmax, "at", [str(a) for a in sl if (nn(4 * a) - nn(8 * a)) / 2 == gmax],
      "; fraction with up steeper:", F(sum(1 for a in sl if nn(4 * a) > F(1, 3)), len(sl)))
