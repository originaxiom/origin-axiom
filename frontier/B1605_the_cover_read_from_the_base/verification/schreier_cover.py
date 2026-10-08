#!/usr/bin/env python3
"""B1605 -- THE COVER READ FROM THE BASE.  B1604 found the stacked index noise on forced covers whose SnapPy presentation
has relators of hundreds of letters (the four's relator residual up to 6e2 at 40 digits).  Here the forced cover is never
triangulated: its fundamental group is presented by Reidemeister-Schreier from the thread's own presentation and the
permutation action on the sheets -- Schreier generators t_i g t_{i.g}^-1 (short words in the base generators), one
rewritten base relator per sheet (each of the base relator's length), the cusps as the stabiliser sublattices of the
base cusp group on the sheets -- and its holonomy is the thread's polished holonomy (SnapPy's Newton-refined shapes at
any precision) evaluated on those words.  Then B1492's stacked instrument runs unchanged at the chosen precision, with
the Euler constraint (T-NO-INDEX-IN-THREE) and the four's relator residual as acceptance.

Validated against B1602 on the clean covers (+LR: 24 members (1, 0, 1); -LR: 6 members (4, 0, 4)) and against B1601's
cover invariants (cusps, volume ratio, homology via the abelianised presentation).

    python3 schreier_cover.py THREAD [bits] [dps]   -> schreier_<thread>.json: the four at every sign character of the
                                                       forced kernel(s): residual, chi, members (h1, r1, n), readings"""
import sys, json, pathlib, itertools, time
import snappy, snappy.snap as snap
import sympy as sp
from snappy import pari
from mpmath import mp, mpf, mpc, matrix, eye
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1602_the_forced_cover_on_every_thread" / "verification"))
import forced_every as FE
MC, RM = FE.MC, FE.RM
pari.allocatemem(2 ** 30, silent=True)
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def reduce_word(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


class Schreier:
    """the cover of a thread by the permutation action perms[g] (right action on sheets 0..d-1) of its generators"""

    def __init__(self, G, perms_by_gen):
        self.gens = list(G.generators()); self.rels = list(G.relators()); self.per = G.peripheral_curves()
        self.act = {g: list(p) for g, p in perms_by_gen.items()}
        self.d = len(next(iter(self.act.values())))
        inv = {g: [0] * self.d for g in self.gens}
        for g in self.gens:
            for i, j in enumerate(self.act[g]):
                inv[g][j] = i
        self.act_inv = inv
        # Schreier transversal by BFS from sheet 0
        self.trans = {0: ""}; frontier = [0]; tree = set()
        while frontier:
            i = frontier.pop(0)
            for g in self.gens:
                for letter, j in ((g, self.act[g][i]), (g.upper(), self.act_inv[g][i])):
                    if j not in self.trans:
                        self.trans[j] = self.trans[i] + letter; tree.add((i, letter)); frontier.append(j)
        assert len(self.trans) == self.d, "the action is not transitive"
        # Schreier generators s_{i,g} = t_i g t_{i.g}^-1 for every (i, g); tree edges are trivial
        self.sgens = {}; names = []
        for i in range(self.d):
            for g in self.gens:
                j = self.act[g][i]
                if (i, g) in tree or (j, g.upper()) in tree:
                    self.sgens[(i, g)] = None
                else:
                    name = LETTERS[len(names)]; names.append(name); self.sgens[(i, g)] = name
        self.names = names
        self.sword = {(i, g): reduce_word(self.trans[i] + g + inv_word(self.trans[self.act[g][i]])) for i in range(self.d) for g in self.gens}

    def step(self, i, letter):
        """from sheet i read one base letter: the Schreier letter emitted (or '') and the next sheet"""
        if letter.islower():
            g = letter; j = self.act[g][i]; s = self.sgens[(i, g)]
            return (s or ""), j
        g = letter.lower(); j = self.act_inv[g][i]; s = self.sgens[(j, g)]
        return ((s.upper()) if s else ""), j

    def rewrite(self, w, i):
        out = []; cur = i
        for c in w:
            s, cur = self.step(cur, c); out.append(s)
        return reduce_word("".join(out)), cur

    def presentation(self):
        rels = []
        for r in self.rels:
            for i in range(self.d):
                w, j = self.rewrite(r, i); assert j == i
                if w:
                    rels.append(w)
        return self.names, rels

    def cusps(self):
        """for each orbit of the base cusp group on the sheets: a basis of the stabiliser sublattice of one sheet,
        rewritten from that sheet -- the cusp's peripheral pair on the cover"""
        out = []
        for (mu, lam) in self.per:
            pm = [self.rewrite(mu, i)[1] for i in range(self.d)]; pl = [self.rewrite(lam, i)[1] for i in range(self.d)]
            seen = set()
            for i in range(self.d):
                if i in seen:
                    continue
                orbit = {i}; fr = [i]
                while fr:
                    x = fr.pop()
                    for y in (pm[x], pl[x]):
                        if y not in orbit:
                            orbit.add(y); fr.append(y)
                seen |= orbit; k = len(orbit)
                # the stabiliser lattice of i: {(a, b): mu^a lam^b fixes i}; a basis by brute force in a box
                def img(a, b):
                    x = i
                    for _ in range(abs(a)):
                        x = pm[x] if a > 0 else pm.index(x)
                    for _ in range(abs(b)):
                        x = pl[x] if b > 0 else pl.index(x)
                    return x
                cands = [(a, b) for a in range(-k, k + 1) for b in range(-k, k + 1) if (a, b) != (0, 0) and img(a, b) == i]
                basis = None
                for v1, v2 in itertools.combinations(sorted(cands, key=lambda v: (abs(v[0]) + abs(v[1]), v)), 2):
                    if abs(v1[0] * v2[1] - v1[1] * v2[0]) == k:
                        basis = (v1, v2); break
                assert basis, (i, k, cands[:10])
                def word(a, b):
                    return (mu if a > 0 else inv_word(mu)) * abs(a) + (lam if b > 0 else inv_word(lam)) * abs(b)
                w1, _ = self.rewrite(word(*basis[0]), i); w2, _ = self.rewrite(word(*basis[1]), i)
                out.append((w1, w2, k, basis))
        return out


def holonomy(M, bits):
    """the thread's polished holonomy in PSL(2, C) (SnapPy's SL(2) lift fails on threads with torsion in H1; the four is
    blind to the lift's sign), each matrix normalised to determinant one"""
    Gp = snap.polished_holonomy(M, bits_prec=bits, lift_to_SL2=False)
    assert list(Gp.generators()) == list(M.fundamental_group().generators())
    rho = {}
    for g in Gp.generators():
        A = Gp.SL2C(g) if hasattr(Gp, "SL2C") else Gp.matrices()[g]
        B = matrix([[mpc(mpf(str(A[i, j].real())), mpf(str(A[i, j].imag()))) for j in range(2)] for i in range(2)])
        rho[g] = B / mp.sqrt(B[0, 0] * B[1, 1] - B[0, 1] * B[1, 0])
    return rho


def site_from_schreier(M, S, rho_base, dps):
    names, rels = S.presentation(); cusps = S.cusps()
    site = RM.Room.__new__(RM.Room); site.name = M.name() + "~schreier"; site.M = None
    site.gens = names; site.rels = rels; site.cusps = [(c[0], c[1]) for c in cusps]; site.m = len(cusps)
    site.rho = {}
    for (i, g), nm in S.sgens.items():
        if nm:
            site.rho[nm] = MC.word(S.sword[(i, g)], rho_base)
    return site, cusps


def run(name, bits=500, dps=100):
    t0 = time.time()
    M = snappy.Manifold(name); G, eps, label, group, good, ks = FE.forced(M)
    MC.mp.dps = dps; MC.TOL = mpf(10) ** (-(dps // 2))
    rho_base = holonomy(M, bits)
    res_base = max(min(mp.norm(MC.word(r, rho_base) - eye(2)), mp.norm(MC.word(r, rho_base) + eye(2))) for r in G.relators())
    out = {"thread": name, "deck": label, "bits": bits, "dps": dps, "tolerance": MC.mp.nstr(MC.TOL, 2), "base_residual": mp.nstr(res_base, 3), "covers": []}
    for img in ks:
        perms = {g: [group.index(FE.mul(group[i], img[g])) for i in range(len(group))] for g in G.generators()}
        S = Schreier(G, perms); site, cusps = site_from_schreier(M, S, rho_base, dps)
        F = site.four({g: mpc(1) for g in site.gens}); res4 = max(mp.norm(MC.word(r, F) - eye(4)) for r in site.rels)
        # homology of the cover from the abelianised presentation (a check against SnapPy's cover)
        A = sp.Matrix([[sum((1 if ch == g else -1 if ch == g.upper() else 0) for ch in r) for g in site.gens] for r in site.rels])
        b1 = len(site.gens) - A.rank()
        cov = {"generators": len(site.gens), "relators": len(site.rels), "max_relator_length": max(len(r) for r in site.rels), "cusps": site.m,
               "cusp_orbit_sizes": [c[2] for c in cusps], "b1": b1, "four_residual": mp.nstr(res4, 3), "members": [], "chi_fails": 0, "sign_characters": 0}
        for vals, nu in RM.sign_characters(site):
            V = site.four(nu); c = site.counts(V); dcount = site.counts(MC.dual(V))
            chi = c["a0"] - c["a1"] + dcount["n"] + dcount["t0_sum"] - dcount["a0"]
            cov["sign_characters"] += 1
            if chi != 0:
                cov["chi_fails"] += 1
            if c["n"] > 0:
                row = {"nu": list(vals), "h1": c["a1"], "r1": c["r1"], "n": c["n"], "t0": c["t0"], "chi": chi, "readings": []}
                interior, other = site.classes(V)
                for z, dead in interior:
                    W = site.extension(V, z); I1 = site.index(W); L2 = {g: MC.ext2(W[g]) for g in site.gens}; I2 = site.index(L2)
                    row["readings"].append({"dead_on_cusps": dead, "I_W1": I1["I"], "I_L2W1": I2["I"]})
                cov["members"].append(row)
        cov["member_count"] = len(cov["members"]); cov["structures"] = sorted({(m["h1"], m["r1"], m["n"]) for m in cov["members"]})
        cov["kinds"] = sorted({(r["I_W1"], r["I_L2W1"]) for m in cov["members"] for r in m["readings"]})
        out["covers"].append(cov)
    out["s"] = round(time.time() - t0, 1)
    (HERE / f"schreier_{name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps({k: (v if k != "covers" else [{kk: vv for kk, vv in c.items() if kk != "members"} for c in v]) for k, v in out.items()}, default=str), flush=True)
    return out


if __name__ == "__main__":
    name = sys.argv[1]; bits = int(sys.argv[2]) if len(sys.argv) > 2 else 500; dps = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    run(name, bits, dps)
