# The read-only referee's gluing check for TWO THREE-GENERATION FLUXES, copied unchanged below this header, committed
# before its run here. It enumerates, by Nikulin's gluing criterion, the primitive embeddings into the even lattice of
# signature (2, 2) and det 5 (Lambda_A, unique in its genus) of every even negative-definite binary lattice of det <= 36
# with two independent norm -6 vectors.   python3 -B referee_glue_check.py > referee_glue_check_out.txt
"""Which even negative-definite binary N (two independent norm -6 vectors, det <= 36) embed primitively in an even
lattice of signature (2,2) and det 5 (unique in its genus: Lambda_A)?  Nikulin: N primitive with complement T
(positive definite, rank 2) iff there is an isotropic graph H of an injective gamma: H_N -> A_T with
det N det T = 5 |H|^2.  Exhaustive over T and gamma."""
from fractions import Fraction as F
import itertools, math

def forms_with_two_norm6(maxdet=36, R=8):
    out = []
    for a in range(2, 40, 2):
        for c in range(a, 80, 2):
            for b in range(0, a // 2 + 1):
                d = a * c - b * b
                if d <= 0 or d > maxdet: continue
                vs = [(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1) if a*x*x + 2*b*x*y + c*y*y == 6]
                if any(p[0]*q[1] - p[1]*q[0] for p, q in itertools.combinations(vs, 2)):
                    out.append(((a, b, c), len(vs)))
    return out

def even_pos_forms(det):
    out = []
    for a in range(2, int((4 * det / 3) ** 0.5) + 2, 2):
        for b in range(0, a // 2 + 1):
            if (det + b * b) % a: continue
            c = (det + b * b) // a
            if c >= a and c % 2 == 0: out.append((a, b, c))
    return out

def disc(Gm):
    a, b, c = Gm[0][0], Gm[0][1], Gm[1][1]
    d = a * c - b * b
    inv = [[F(c, d), F(-b, d)], [F(-b, d), F(a, d)]]
    els = set()
    for y1 in range(abs(d)):
        for y2 in range(abs(d)):
            x = (inv[0][0] * y1 + inv[0][1] * y2, inv[1][0] * y1 + inv[1][1] * y2)
            els.add((x[0] % 1, x[1] % 1))
    els = sorted(els)
    def bil(x, y): return x[0]*a*y[0] + x[0]*b*y[1] + x[1]*b*y[0] + x[1]*c*y[1]
    def add(x, y): return ((x[0] + y[0]) % 1, (x[1] + y[1]) % 1)
    def mul(n, x): return ((n * x[0]) % 1, (n * x[1]) % 1)
    return els, bil, add, mul

def order(x, mul):
    n = 1
    while mul(n, x) != (0, 0): n += 1
    return n

def embeds(Nf):
    """Nf positive form (a,b,c); N = Nf(-1)."""
    a, b, c = Nf
    GN = [[-a, -b], [-b, -c]]
    dN = a * c - b * b
    AN, bN, addN, mulN = disc(GN)
    qN = lambda x: bN(x, x) % 2
    found = []
    for h in range(1, dN + 1):
        if dN % h or (5 * h * h) % dN: continue
        dT = 5 * h * h // dN
        for Tf in even_pos_forms(dT):
            AT, bT, addT, mulT = disc([[Tf[0], Tf[1]], [Tf[1], Tf[2]]])
            qT = lambda y: bT(y, y) % 2
            # subgroups of A_N of order h, by generating pairs
            seen = set()
            for x1, x2 in itertools.product(AN, repeat=2):
                o1, o2 = order(x1, mulN), order(x2, mulN)
                sub = frozenset(addN(mulN(i, x1), mulN(j, x2)) for i in range(o1) for j in range(o2))
                if len(sub) != h or sub in seen: continue
                seen.add(sub)
                rel = [(i, j) for i in range(o1) for j in range(o2) if addN(mulN(i, x1), mulN(j, x2)) == (0, 0)]
                for y1, y2 in itertools.product(AT, repeat=2):
                    if (qN(x1) + qT(y1)) % 2 or (qN(x2) + qT(y2)) % 2 or (bN(x1, x2) + bT(y1, y2)) % 1: continue
                    if any(addT(mulT(i, y1), mulT(j, y2)) != (0, 0) for i, j in rel): continue
                    img = set(addT(mulT(i, y1), mulT(j, y2)) for i in range(o1) for j in range(o2))
                    if len(img) != h: continue  # injective
                    found.append((h, Tf))
                    break
                if found and found[-1][1] == Tf and found[-1][0] == h: break
    return found

for f, nv in forms_with_two_norm6():
    det = f[0] * f[2] - f[1] ** 2
    print(f, "det", det, "norm-6 vectors", nv, "-> primitive embeddings (h, T):", sorted(set(embeds(f))))
