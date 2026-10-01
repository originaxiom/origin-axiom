"""B1507 -- the physics seat's R64 and R68 (2026-09-06; seat reports, not banked) on this bench, with B1270's exact icosian E8
(its Q(sqrt5) quaternion helpers, frontier/B1270_e6_from_the_two_faces/verification) and an own enumeration.
R64: an order-3 unit g acts on E8 (the icosians) by left multiplication as the A2 family rotation on Z[g] times an order-3 isometry
     of E6 = Z[g]^perp that fixes no vector -- the regular order-3 class of W(E6), whose lift (the principal order-3 element) has
     centraliser A2^3: the trinification.  So B1271's family triplet and B521's 'trinification within one 27' are the two factors
     of one element.
R68: of E6's 40 trinification subsystems A2^3, exactly 4 are stable under left multiplication by g, 4 under right, 1 under both;
     right multiplication permutes the 4 left frames as a 3-cycle and a fixed point; the two-sided frame is mirror-invariant.
     (R65's 85 -> 40 is main's B1306 FINDINGS_C; R68's addendum maps the selected frame to B1264's labelling (1,0,2,2,0,2).)
Counts are invariant under conjugating g in 2I (all 20 order-3 units are conjugate); two different units are run."""
import importlib.util
import itertools
import os
import random
from collections import Counter
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
B1270 = os.path.join(HERE, "..", "..", "B1270_e6_from_the_two_faces", "verification", "e6_from_the_two_faces.py")
_spec = importlib.util.spec_from_file_location("b1270_two_faces", B1270)
B = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(B)
Q5, qmul, qconj, bil, key = B.Q5, B.qmul, B.qconj, B.bil, B.key


def setup():
    units = B.unit_icosians(); roots = B.e8_roots(units)
    one = (Q5(1), Q5(0), Q5(0), Q5(0))
    order3 = [u for u in units if u[0] == Q5(F(-1, 2))]
    return units, roots, one, order3


def analyse(roots, one, g):
    E6 = [r for r in roots if bil(r, one) == 0 and bil(r, g) == 0]
    idx = {key(r): i for i, r in enumerate(E6)}
    L = [idx[key(qmul(g, r))] for r in E6]; R = [idx[key(qmul(r, g))] for r in E6]
    C = [idx.get(key(qconj(r))) for r in E6]
    orbits = {frozenset({i, L[i], L[L[i]]}) for i in range(len(E6))}
    G = [[bil(a, b) for b in E6] for a in E6]
    neg = [idx[key(tuple(-x for x in r))] for r in E6]
    A2s = set()
    for i in range(len(E6)):
        for j in range(i + 1, len(E6)):
            if G[i][j] == -1:
                s = idx[key(tuple(x + y for x, y in zip(E6[i], E6[j])))]
                A2s.add(frozenset([i, j, s, neg[i], neg[j], neg[s]]))
    A2s = list(A2s)
    orth = [[all(G[p][q] == 0 for p in P for q in Q) for Q in A2s] for P in A2s]
    frames = set()
    for a in range(len(A2s)):
        for b in range(a + 1, len(A2s)):
            if orth[a][b]:
                for c in range(b + 1, len(A2s)):
                    if orth[a][c] and orth[b][c]:
                        frames.add(frozenset(A2s[a] | A2s[b] | A2s[c]))
    frames = list(frames)
    stable = lambda Fr, m: all(m[x] in Fr for x in Fr)
    left = [Fr for Fr in frames if stable(Fr, L)]; right = [Fr for Fr in frames if stable(Fr, R)]
    both = [Fr for Fr in left if Fr in right]
    perm = [left.index(frozenset(R[x] for x in Fr)) if frozenset(R[x] for x in Fr) in left else None for Fr in left]
    cycle_type = sorted(Counter(len(c) for c in _cycles(perm)).items()) if None not in perm else None
    return dict(e6_roots=len(E6), fixed_roots=sum(1 for i in range(len(E6)) if L[i] == i), free_orbits=len(orbits),
                pairing_r_gr=sorted({G[i][L[i]] for i in range(len(E6))}), a2=len(A2s), frames=len(frames), left=len(left),
                right=len(right), both=len(both), right_on_left_cycle_type=cycle_type,
                two_sided_mirror_invariant=[all(C[x] is not None and C[x] in Fr for x in Fr) for Fr in both]), E6


def _cycles(perm):
    seen, out = set(), []
    for i in range(len(perm)):
        if i in seen:
            continue
        c, j = [], i
        while j not in seen:
            seen.add(j); c.append(j); j = perm[j]
        out.append(c)
    return out


def principal_order3(E6):
    """the regular order-3 class lifts to the principal element exp(2 pi i rho^v / 3): its centraliser's roots are those of height
    0 mod 3 for a base of E6; count them and their simple components"""
    import sympy as sp
    rng = random.Random(5)
    while True:
        h = [Q5(F(rng.randint(-50, 50), 7), F(rng.randint(-50, 50), 11)) for _ in range(4)]
        ht = lambda r: sum((x * y).x + (x * y).y * 2.2360679774997896 for x, y in zip(r, h))
        if all(abs(ht(r)) > 1e-9 for r in E6):
            break
    pos = [r for r in E6 if ht(r) > 0]
    pk = {key(p) for p in pos}
    simple = [r for r in pos if not any(key(tuple(a - b for a, b in zip(r, s))) in pk for s in pos if key(s) != key(r))]
    Cm = sp.Matrix([[bil(a, b) for b in simple] for a in simple]); Si = Cm.inv()
    heights = []
    for r in pos:
        co = Si * sp.Matrix([bil(r, s) for s in simple])
        assert all(c.is_integer and c >= 0 for c in co)
        heights.append(int(sum(co)))
    zero3 = [r for r, t in zip(pos, heights) if t % 3 == 0]
    Z = zero3 + [tuple(-x for x in r) for r in zero3]
    comps, seen = [], set()
    for r in Z:
        if key(r) in seen:
            continue
        stack, cc = [r], set()
        while stack:
            x = stack.pop()
            if key(x) in cc:
                continue
            cc.add(key(x)); stack += [y for y in Z if bil(x, y) != 0 and key(y) not in cc]
        seen |= cc; comps.append(len(cc))
    return dict(simple=len(simple), heights=dict(sorted(Counter(heights).items())), height_0_mod_3_positive=len(zero3),
                centraliser_dim=2 * len(zero3) + 6, components=sorted(comps))


def main():
    units, roots, one, order3 = setup()
    out = dict(e8_roots=len(roots), unit_icosians=len(units), order3_units=len(order3))
    first = None
    for label, g in (("unit_0", order3[0]), ("unit_7", order3[7])):
        res, E6 = analyse(roots, one, g)
        out[label] = res
        first = first or E6
    out["principal_order3"] = principal_order3(first)
    return out


if __name__ == "__main__":
    for k, v in main().items():
        print(k, "=", v)
