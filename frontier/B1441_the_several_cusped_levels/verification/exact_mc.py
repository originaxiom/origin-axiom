#!/usr/bin/env python3
"""The class index on several cusps in exact arithmetic over Q(zeta_N): a second implementation of B1333's formulas
(own cyclotomic field, own linear algebra), for the rank-two modules of B1441 with |I| >= 2.

n(V) = a_1 - r_1,  a_1 = dim Z^1 - (d - a_0),  r_1 = rank(res Z^1 + B^1(dM)) - rank B^1(dM),  B^1(dM) = (+)_i B^1(T_i);
I = n(V) - n(V*).
"""
import sys, json, itertools, pathlib, warnings, random
warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1435_the_interaction_census" / "verification"))
sys.path.insert(0, str(HERE))
from exact_couplings import Cyc, nullspace, rank
import several_cusps as sc

def mm(A, B): return [[sum((A[i][l] * B[l][j] for l in range(1, len(B))), A[i][0] * B[0][j]) for j in range(len(B[0]))] for i in range(len(A))]
def inv_tri(A):                                              # inverse of an upper- or lower-triangular 2x2, or a 1x1
    if len(A) == 1: return [[A[0][0].inv()]]
    d = (A[0][0] * A[1][1] - A[0][1] * A[1][0]).inv()
    return [[A[1][1] * d, -A[0][1] * d], [-A[1][0] * d, A[0][0] * d]]

class Rep:
    def __init__(self, F, gens, mats):
        self.F, self.gens, self.d = F, gens, len(mats[gens[0]]); self.M = dict(mats); self.Mi = {g: inv_tri(mats[g]) for g in gens}
        self.I = [[F.const(int(i == j)) for j in range(self.d)] for i in range(self.d)]
    def word(self, w):
        R = self.I
        for ch in w: R = mm(R, self.M[ch] if ch.islower() else self.Mi[ch.lower()])
        return R
    def fox(self, w, gen):
        d = self.d; res = [[self.F.const(0)] * d for _ in range(d)]; pre = self.I
        for ch in w:
            g = ch.lower()
            if ch.islower():
                if g == gen: res = [[res[i][j] + pre[i][j] for j in range(d)] for i in range(d)]
                pre = mm(pre, self.M[g])
            else:
                pre = mm(pre, self.Mi[g])
                if g == gen: res = [[res[i][j] - pre[i][j] for j in range(d)] for i in range(d)]
        return res
    def dual(self):
        return Rep(self.F, self.gens, {g: [[self.Mi[g][j][i] for j in range(self.d)] for i in range(self.d)] for g in self.gens})

def analyse(V, rels, per):
    F, d, gens = V.F, V.d, V.gens; g = len(gens)
    inv_rows = [[V.M[x][i][j] - V.I[i][j] for j in range(d)] for x in gens for i in range(d)]
    a0 = d - rank(inv_rows, d, F)
    J = []
    for r in rels:
        bl = [V.fox(r, x) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    rkJ, Z = nullspace(J, g * d, F); a1 = len(Z) - (d - a0)
    c = len(per); R = []; Bt = []; t0s = []
    for i, (mu, lam) in enumerate(per):
        A = V.word(mu); Bm = V.word(lam)
        Am = [[A[x][y] - V.I[x][y] for y in range(d)] for x in range(d)]; Bmm = [[Bm[x][y] - V.I[x][y] for y in range(d)] for x in range(d)]
        t0s.append(d - rank(Am + Bmm, d, F))
        for k in range(d):
            row = [F.const(0)] * (2 * c * d)
            for r_ in range(d): row[2 * i * d + r_] = Am[r_][k]; row[2 * i * d + d + r_] = Bmm[r_][k]
            Bt.append(row)
    foxp = [[(V.fox(mu, x), V.fox(lam, x)) for x in gens] for (mu, lam) in per]
    for v in Z:
        z = [v[j * d:(j + 1) * d] for j in range(g)]; row = []
        for i in range(c):
            for which in (0, 1):
                out = [F.const(0)] * d
                for j in range(g):
                    Fm = foxp[i][j][which]
                    for a in range(d):
                        for b in range(d): out[a] = out[a] + Fm[a][b] * z[j][b]
                row += out
        R.append(row)
    nz = lambda rows: [r for r in rows if any(not q.iszero() for q in r)]
    rB = rank(nz(Bt), 2 * c * d, F) if nz(Bt) else 0
    r1 = (rank(nz(R + Bt), 2 * c * d, F) if nz(R + Bt) else 0) - rB
    return dict(a0=a0, a1=a1, r1=r1, n=a1 - r1, t0s=t0s)

def classes_exact(F, gens, rels, exps):
    V1 = Rep(F, gens, {g: [[F.zeta(exps[i])]] for i, g in enumerate(gens)})
    J = [[V1.fox(r, g)[0][0] for g in gens] for r in rels]
    rk, Z = nullspace(J, len(gens), F)
    b = [F.zeta(e) - 1 for e in exps]; cur = [b] if any(not q.iszero() for q in b) else []; r0 = rank(cur, len(gens), F) if cur else 0; out = []
    for zc in Z:
        r2 = rank(cur + [zc], len(gens), F)
        if r2 > r0: cur.append(zc); r0 = r2; out.append(zc)
    return out

def index_exact(F, gens, rels, per, lc, al, ct):
    N = F.N; be = [(a - b) % N for a, b in zip(al, lc)]
    mats = {g: [[F.zeta(al[i]), ct[i] * F.zeta(be[i])], [F.const(0), F.zeta(be[i])]] for i, g in enumerate(gens)}
    V = Rep(F, gens, mats)
    for r in rels:
        W = V.word(r); assert all((W[i][j] - V.I[i][j]).iszero() for i in range(2) for j in range(2)), "not a representation"
    A = analyse(V, rels, per); B = analyse(V.dual(), rels, per)
    return A["n"] - B["n"], A, B

def verify(tag, nm, d, i, N, witnesses, limit=6, seed=1):
    C = sc.get(nm, d, i); gens, rels, per = sc.group_data(C); b1, tors, Nt = sc.homology(gens, rels); N = max(Nt, 2) if N is None else N
    F = Cyc(N); rnd = random.Random(seed); out = []
    for w in witnesses[:limit]:
        lc, al = w["l"], w["alpha"]; H = classes_exact(F, gens, rels, lc); assert len(H) == w["h1_l"], ("h1 differs", len(H), w["h1_l"])
        combos = [[int(a == b) for b in range(len(H))] for a in range(len(H))]
        if len(H) > 1: combos += [[rnd.randrange(1, 9) for _ in H] for _ in range(3)]
        vals = []
        for co in combos:
            ct = [sum((H[m][j] * co[m] for m in range(1, len(H))), H[0][j] * co[0]) for j in range(len(gens))]
            I, A, B = index_exact(F, gens, rels, per, lc, al, ct); vals.append((I, A["n"], B["n"], A["a1"], A["r1"], A["t0s"], B["t0s"]))
        out.append(dict(l=lc, alpha=al, h1_l=len(H), prime_field_I=w["I"], exact=[dict(I=v[0], n=v[1], n_dual=v[2], a1=v[3], r1=v[4], t0s=v[5], t0s_dual=v[6]) for v in vals]))
        print(tag, "l", lc, "alpha", al, "h1(l)", len(H), "prime-field I", w["I"], "exact I over the classes tried:", [v[0] for v in vals], flush=True)
    return out


if __name__ == "__main__":                                   # verify every carrier of |I| >= 2 in the run's records
    import glob, re
    rows = []
    for f in sorted(glob.glob(str(HERE / "several_cusps_*.json"))):
        if re.fullmatch(r"several_cusps_\d+\.json", pathlib.Path(f).name): rows += json.load(open(f))
    car = [r for r in rows if "skipped" not in r and r["max_abs_I"] >= 2]; out = []
    for r in sorted(car, key=lambda r: (r["characters"], r["tag"])):
        N = r["N"] if (r["degree"] is None and r["tag"].endswith("N=12")) else None
        v = verify(r["tag"], r["root"], r["degree"], r["index_in_snappy_list"], N, r["witnesses"], limit=4)
        out.append(dict(tag=r["tag"], cusps=r["cusps"], N=r["N"], field="Q(zeta_%d)" % r["N"], witnesses=v,
                        exact_max_abs_I=max(abs(e["I"]) for w in v for e in w["exact"])))
        json.dump(out, open(HERE.parent / "exact_several.json", "w"), indent=1)
    print("carriers verified:", len(out), "; all exact max |I| equal to the prime-field one:", all(o["exact_max_abs_I"] >= 2 for o in out))
