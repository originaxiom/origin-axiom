#!/usr/bin/env python3
"""B1506 -- THE LEVEL, built as sealed (PREREGISTRATION.md, sha256 664f8192..., committed at 58e3f28f before this file).

sL-5: is a count taken on a cover or on its quotient?  The root m004 is the base of every cover the tower generates, and its deck
Z/n acts on every level M_n.  B1374's index engine (index_lib.py) on the Standard-Model frame's doublet modules: a background is a
flat E6 connection with holonomy in the image of SL(2)_beta x U(1)_Y x U(1)_gamma; sector s (Q, u^c, e^c, d^c, L, nu^c; charges
(s_Y, s_gamma) = (1,3), (-4,3), (6,3), (2,1), (-3,1), (0,-5)) is the non-split extension of beta_s by alpha_s with extension character
lam = alpha_s / beta_s.  Backgrounds are parametrised here by (lam, kappa, psi_Y): alpha_s = s_Y psi_Y + s_gamma kappa +
((1 - s_gamma)/2) lam (additive exponents), which covers the backgrounds that do not lift to SL(2)_beta x U(1)^2 (lam not a square).

Presentations.
  RS  B1384's Reidemeister-Schreier cover of pi_1(m004) = <a, b | abABaBAbaB> (two meridians): z = a^n, y_k = a^k b a^-(k+1),
      y_(n-1) = a^(n-1) b; meridian z; the root deck tau = conjugation by a (rs_conj).
  MT  B1381's mapping torus of phi^n, phi = (a -> ab, b -> bab) (fixes [a,b]); meridian t, longitude abAB; tau = (phi, phi, t).

Parts (python3 the_level.py [part ...]; no argument runs all and writes the_level.json):
  A  covers of m004 (SnapPy)                 B  presentations and the deck (MT automorphism; RS closed form; B1378's word map)
  C  the loci lemma (exact on MT M1..M4, numerical on M5, M6)
  D  the complete census on RS M1..M6 (and MT M1..M4 for s961's second presentation): loci, firing modules, generation-shaped
     backgrounds, lifts, root-deck orbits; B1375's counts recovered from the lift data
  E  pullbacks keep the index (MT: M1 -> M2..M6, M2 -> M4, M6, M3 -> M6, every candidate)
  F  the M6 triplet: the seed's root-deck orbit, the four descents to s961 (D1-D3), the root object's counts by level (D5)
  H  the s961 / M6 correspondence (D6, P7)"""
import sys, os, json, math, time, itertools, importlib.util, warnings
from collections import Counter, defaultdict
warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
_spec = importlib.util.spec_from_file_location(
    "b1374_index_lib", os.path.join(ROOT, "frontier", "B1374_the_class_index_in_the_sm_frame", "verification", "index_lib.py"))
IL = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(IL)

SECTORS = [("Q", 1, 3), ("u^c", -4, 3), ("e^c", 6, 3), ("d^c", 2, 1), ("L", -3, 1), ("nu^c", 0, -5)]
CHARGED = 5
PRIMES_DEFAULT = 3


# ============================================================================================ words
def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def red(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def subst(img, w):
    return "".join(img[c] if c.islower() else inv(img[c.lower()]) for c in w)


def lcm(*xs):
    out = 1
    for x in xs:
        out = out * x // math.gcd(out, x)
    return out


def primes_for(N, k=PRIMES_DEFAULT, start=400):
    out = []
    p = (start // N + 1) * N + 1
    while len(out) < k:
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            out.append(p)
        p += N
    return out


def smith(gens, rels):
    from sympy import Matrix
    from sympy.matrices.normalforms import smith_normal_decomp
    E = Matrix([[IL.abelian_exponents(r, gens)[g] for g in gens] for r in rels])
    return smith_normal_decomp(E)


def h1_of(gens, rels):
    S, _, _ = smith(gens, rels)
    diag = [abs(int(S[i, i])) for i in range(min(S.shape))]
    return [d for d in diag if d > 1], len(gens) - sum(1 for d in diag if d)


def characters(gens, rels, N):
    """every character pi -> Z/N (exponent tuples in the order of gens), via Smith's decomposition"""
    from sympy import Matrix
    S, U, V = smith(gens, rels)
    ranges = []
    for i in range(len(gens)):
        s = abs(int(S[i, i])) if i < min(S.shape) else 0
        if s:
            step = N // math.gcd(s, N)
            ranges.append([k * step % N for k in range(N // step)])
        else:
            ranges.append(list(range(N)))
    Vl = [[int(V[i, j]) for j in range(V.shape[1])] for i in range(V.shape[0])]
    out = []
    for kp in itertools.product(*ranges):
        out.append(tuple(sum(Vl[i][j] * kp[j] for j in range(len(kp))) % N for i in range(len(gens))))
    return out


# ============================================================================================ the two presentations
PHI = {"a": "ab", "b": "bab"}                  # fixes [a,b] = abAB exactly; abelianization [[1,1],[1,2]] (trace 3: m004)
MT_GENS = ["a", "b", "t"]
MT_MU, MT_LAM = "t", "abAB"


def apply(phi, w):
    return red("".join(phi[c] if c.islower() else inv(phi[c.lower()]) for c in w))


def phi_power(n):
    img = {"a": "a", "b": "b"}
    for _ in range(n):
        img = {g: apply(PHI, img[g]) for g in "ab"}
    return img


def mt_level(n):
    P = phi_power(n)
    return ["taT" + inv(P["a"]), "tbT" + inv(P["b"])]


RS_RELATOR = "abABaBAbaB"
RS_LONGITUDE = "bABaaBAb"
RS_LETTERS = "cdefghijk"


def rs_cover(n):
    """Reidemeister-Schreier for the n-fold cyclic cover (a, b -> 1 in Z/n), transversal a^k (B1384's rs_cover, rebuilt)"""
    gens = ["z"] + [RS_LETTERS[k] for k in range(n)]
    words = {"z": "a" * n}
    for k in range(n):
        words[RS_LETTERS[k]] = "a" * k + "b" + ("A" * (k + 1) if k < n - 1 else "")

    def rewrite(w, k=0):
        out = []
        for ch in w:
            if ch == "a":
                if k == n - 1:
                    out.append("z")
                k = (k + 1) % n
            elif ch == "A":
                if k == 0:
                    out.append("Z")
                k = (k - 1) % n
            elif ch == "b":
                out.append(RS_LETTERS[k]); k = (k + 1) % n
            elif ch == "B":
                k = (k - 1) % n; out.append(RS_LETTERS[k].upper())
        return "".join(out), k

    rels = []
    for k in range(n):
        r, kk = rewrite(RS_RELATOR, k)
        assert kk == k
        rels.append(r)
    lam, k2 = rewrite(RS_LONGITUDE)
    assert k2 == 0
    return gens, words, rewrite, rels, "z", lam


def rs_conj(n, j):
    """tau^j on the RS generators: g -> a^j g a^-j rewritten from coset 0"""
    gens, words, rewrite, rels, mu, lam = rs_cover(n)
    out = {}
    for g in gens:
        w, k = rewrite("a" * j + words[g] + "A" * j)
        assert k == 0
        out[g] = red(w)
    return out


def rs_closed_form(n):
    L = RS_LETTERS
    out = {"z": "z"}
    for k in range(n):
        if k < n - 2:
            out[L[k]] = L[k + 1]
        elif k == n - 2:
            out[L[k]] = L[n - 1] + "Z"
        else:
            out[L[k]] = "z" + L[0]
    return out


class Pres:
    """a level of the tower in one presentation, with its characters and the root deck on them"""

    def __init__(self, kind, n, N=None):
        self.kind, self.n = kind, n
        if kind == "RS":
            self.gens, self.words, self.rewrite, self.rels, self.mu, self.lam = rs_cover(n)
            self.deck_img = rs_conj(n, 1)
        else:
            self.gens, self.rels, self.mu, self.lam = list(MT_GENS), mt_level(n), MT_MU, MT_LAM
            self.deck_img = {"a": PHI["a"], "b": PHI["b"], "t": "t"}
            self.words = None
        self.tors, self.free = h1_of(self.gens, self.rels)
        self.e = lcm(*self.tors) if self.tors else 1
        self.N = N or lcm(12, self.e)
        self.chars = characters(self.gens, self.rels, self.N)
        self.cset = set(self.chars)
        assert len(self.cset) == len(self.chars)
        G = self.gens
        self.D = [[IL.abelian_exponents(self.deck_img[g], G)[h] for h in G] for g in G]
        self.mu_ex = [IL.abelian_exponents(self.mu, G)[h] for h in G]
        self.lam_ex = [IL.abelian_exponents(self.lam, G)[h] for h in G]
        self.squares = set(tuple(2 * x % self.N for x in c) for c in self.chars)
        self.sqrt = defaultdict(list)
        self.fifth = defaultdict(list)
        for c in self.chars:
            self.sqrt[tuple(2 * x % self.N for x in c)].append(c)
            self.fifth[tuple(5 * x % self.N for x in c)].append(c)

    def val(self, c, ex):
        return sum(a * b for a, b in zip(ex, c)) % self.N

    def pull(self, c, k=1):
        for _ in range(k):
            c = tuple(sum(self.D[i][j] * c[j] for j in range(len(c))) % self.N for i in range(len(c)))
        return c

    def add(self, *cs, coeffs=None):
        coeffs = coeffs or [1] * len(cs)
        return tuple(sum(k * c[i] for k, c in zip(coeffs, cs)) % self.N for i in range(len(self.gens)))


def ext_rep(F, z, gens, alpha, beta, coc, N):
    """the extension [[alpha, c beta], [0, beta]] (c a cocycle for alpha/beta, index_lib's left convention)"""
    return {g: [[pow(z, a % N, F.p), coc[g] * pow(z, b % N, F.p) % F.p], [0, pow(z, b % N, F.p)]]
            for g, a, b in zip(gens, alpha, beta)}


# ============================================================================================ the census
class Census:
    """every finite-order locus lam (square or not), every T5-candidate module (alpha trivial on the cusp; beta = alpha - lam),
    the index over three primes; then the generation-shaped backgrounds in (lam, kappa, psi_Y) coordinates"""

    def __init__(self, P, primes=None, verbose=True):
        t0 = time.time()
        self.P = P
        N = P.N
        self.primes = primes or primes_for(N)
        self.fields = []
        for p in self.primes:
            F = IL.GF(p)
            self.fields.append((F, F.root_of_unity(N)))
        # loci: h^1(lam) >= 1 at every prime; the cocycle per prime
        self.loci = {}
        bad_t1 = []
        for c in P.chars:
            cocs = []
            for (F, z) in self.fields:
                val = {g: pow(z, x, F.p) for g, x in zip(P.gens, c)}
                h1, coc = IL.h1_and_cocycle(F, P.gens, P.rels, P.mu, P.lam, val)
                if coc is None:
                    break
                assert h1 == 1, ("B1381: h^1 <= 1", P.kind, P.n, c, h1)
                cocs.append(coc)
            else:
                self.loci[c] = cocs
                if P.val(c, P.mu_ex) or P.val(c, P.lam_ex):
                    bad_t1.append(c)
        self.t1_exceptions = bad_t1                               # T1: every locus trivial on the cusp
        self.cand_alpha = [a for a in P.chars if P.val(a, P.mu_ex) == 0 and P.val(a, P.lam_ex) == 0]
        self.I = {}
        self.rechecked = self.differ = 0
        for lam in self.loci:
            for a in self.cand_alpha:
                b = P.add(a, lam, coeffs=[1, -1])
                I0 = self.index(lam, a, b, 0)
                self.I[(lam, a)] = I0
                if I0:
                    self.rechecked += 1
                    if any(self.index(lam, a, b, q) != I0 for q in range(1, len(self.fields))):
                        self.differ += 1
        self.firing = {k: v for k, v in self.I.items() if v}
        self.time = time.time() - t0
        if verbose:
            print(f"  {P.kind} M_{P.n}: H1 torsion {P.tors}, N = {N}, |Hom| = {len(P.chars)}, loci {len(self.loci)} "
                  f"(non-square {sum(1 for l in self.loci if l not in P.squares)}), candidates {len(self.I)}, firing "
                  f"{len(self.firing)} (non-square {sum(1 for (l, a) in self.firing if l not in P.squares)}), rechecked "
                  f"{self.rechecked}, differing {self.differ} ({self.time:.0f} s)", flush=True)

    def module(self, lam, a, q=0):
        P = self.P
        F, z = self.fields[q]
        b = P.add(a, lam, coeffs=[1, -1])
        return IL.Rep(F, P.gens, ext_rep(F, z, P.gens, a, b, self.loci[lam][q], P.N))

    def index(self, lam, a, b, q):
        V = self.module(lam, a, q)
        assert V.check_relators(self.P.rels)
        return IL.index(V, self.P.rels, self.P.mu, self.P.lam)[0]

    def alphas(self, lam, kappa, psiY):
        P = self.P
        return tuple(P.add(psiY, kappa, lam, coeffs=[sy, sg, (1 - sg) // 2]) for (_, sy, sg) in SECTORS)

    def generation_shaped(self):
        """classes (lam, six alphas) -> the six counts; the five charged sectors equal and non-zero"""
        P = self.P
        fifth = P.fifth
        by_lam = defaultdict(dict)
        for (lam, a), I in self.firing.items():
            by_lam[lam][a] = I
        classes = {}
        for lam, fire in by_lam.items():
            for ad, Id in fire.items():
                for aL, IL_ in fire.items():
                    if Id != IL_:
                        continue
                    w = P.add(ad, aL, coeffs=[1, -1])
                    for y in fifth.get(w, []):
                        kappa = P.add(ad, y, coeffs=[1, -2])
                        als = self.alphas(lam, kappa, y)
                        assert als[3] == ad and als[4] == aL
                        Is = tuple(self.I.get((lam, a), 0) for a in als)
                        if all(Is[i] == Is[0] != 0 for i in range(CHARGED)):
                            key = (lam, als)
                            assert classes.get(key, Is) == Is
                            classes[key] = Is
        return classes

    def deck_class(self, key, k=1):
        lam, als = key
        return (self.P.pull(lam, k), tuple(self.P.pull(a, k) for a in als))

    def orbit(self, key):
        for k in range(1, self.P.n + 1):
            if self.deck_class(key, k) == key:
                return k
        raise AssertionError("tau^n must fix every class")

    def lift_data(self, key):
        """B1375's lift data (chi != 0, psi_Y, psi_gamma) of a class: 2 chi = lam, chi + s_Y psi_Y + s_g psi_g = alpha_s"""
        P = self.P
        lam, als = key
        n = 0
        roots = [c for c in P.sqrt.get(lam, []) if any(c)]
        ys = P.fifth.get(P.add(als[3], als[4], coeffs=[1, -1]), [])
        for chi in roots:
            for y in ys:
                g = P.add(als[3], chi, y, coeffs=[1, -1, -2])
                if all(P.add(chi, y, g, coeffs=[1, sy, sg]) == als[i] for i, (_, sy, sg) in enumerate(SECTORS)):
                    n += 1
        return n


def census_summary(C, with_lifts=False):
    P = C.P
    mods = C.firing
    orb_m = Counter()
    for (lam, a) in mods:
        for k in range(1, P.n + 1):
            if (P.pull(lam, k), P.pull(a, k)) == (lam, a):
                orb_m[k] += 1
                break
    inv_ok = all(C.I.get((P.pull(lam), P.pull(a))) == I for (lam, a), I in mods.items())
    classes = C.generation_shaped()
    orb = Counter(C.orbit(k) for k in classes)
    lifted = [k for k in classes if k[0] in P.squares]
    row = dict(presentation=P.kind, n=P.n, H1_torsion=P.tors, N=P.N, primes=C.primes, hom=len(P.chars), loci=len(C.loci),
               loci_non_square=sum(1 for l in C.loci if l not in P.squares), t1_exceptions=len(C.t1_exceptions),
               candidates=len(C.I), firing=len(mods), firing_non_square=sum(1 for (l, a) in mods if l not in P.squares),
               non_square_loci_firing=len(set(l for (l, a) in mods if l not in P.squares)),
               index_values=dict(Counter(mods.values())), rechecked=C.rechecked, differing=C.differ,
               module_orbit_sizes={str(k): v for k, v in sorted(orb_m.items())}, deck_invariant_index=inv_ok,
               generation_shaped=len(classes), generation_shaped_lifted=len(lifted),
               generation_shaped_not_lifted=len(classes) - len(lifted),
               background_orbit_sizes={str(k): v for k, v in sorted(orb.items())},
               background_signs=dict(Counter(Is[0] for Is in classes.values())),
               background_nu_counts=dict(Counter(Is[5] for Is in classes.values())),
               background_max_abs=max([abs(x) for Is in classes.values() for x in Is[:CHARGED]], default=0),
               seconds=round(C.time, 1))
    if with_lifts and lifted:
        row["lift_data_total"] = sum(C.lift_data(k) for k in lifted)
    return row, classes


# ============================================================================================ A. the covers of m004
def part_a(dmax=6):
    import snappy
    M = snappy.Manifold("m004")
    rows = []
    for d in range(2, dmax + 1):
        covs = M.covers(d)
        kinds = Counter(c.cover_info()["type"] for c in covs)
        cyc = [c for c in covs if c.cover_info()["type"] == "cyclic"]
        rows.append(dict(degree=d, covers=len(covs), types=dict(kinds), cyclic_H1=[str(c.homology()) for c in cyc],
                         cyclic_name=[str(c.identify()[0]) if c.identify() else "" for c in cyc]))
    F = IL.GF(601)
    rep = IL.Rep(F, ["a", "b"], {"a": [[F.p - 1]], "b": [[F.p - 1]]})
    dfa = rep.fox(RS_RELATOR)["a"][0][0]
    det = min(dfa % F.p, (-dfa) % F.p)
    return dict(covers=rows, det_4_1=det,
                unique_2_and_3=all(r["covers"] == 1 and r["types"] == {"cyclic": 1} for r in rows if r["degree"] in (2, 3)),
                regular_noncyclic_up_to_dmax=sum(r["types"].get("regular", 0) for r in rows))


# ============================================================================================ B. presentations and the deck
def mt_tau_of(word):
    img = {"a": PHI["a"], "b": PHI["b"], "t": "t"}
    return red(subst(img, word))


def mt_formal_identity(n):
    P = phi_power(n)
    Q = phi_power(n + 1)
    return all(red("".join(P[c] if c.islower() else inv(P[c.lower()]) for c in PHI[g])) == Q[g] for g in "ab")


B1378_TAU = {"z": "z", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "zcZ"}
B1378_TAU2 = {"z": "z", "c": "e", "d": "f", "e": "g", "f": "h", "g": "zcZ", "h": "zdZ"}


def geometric_rs(F, n):
    w = F.root_of_unity(3)
    base = IL.Rep(F, ["a", "b"], {"a": [[1, 1], [0, 1]], "b": [[1, 0], [(-w) % F.p, 1]]})
    assert base.check_relators([RS_RELATOR])
    gens, words, rewrite, rels, mu, lam = rs_cover(n)
    return base, IL.Rep(F, gens, {g: base.word(words[g]) for g in gens})


def part_b():
    out = dict(MT=[], RS=None)
    for n in range(1, 7):
        rels = mt_level(n)
        tors, free = h1_of(MT_GENS, rels)
        NN = lcm(12, lcm(*tors) if tors else 1); p = primes_for(NN)[0]; F = IL.GF(p); z = F.root_of_unity(NN)
        chars = characters(MT_GENS, rels, NN)
        checked = bad = inner = 0
        for c in chars:
            if checked >= 12:
                break
            if not any(c):
                continue
            val = {g: pow(z, 2 * x, p) for g, x in zip(MT_GENS, c)}
            h1, coc = IL.h1_and_cocycle(F, MT_GENS, rels, MT_MU, MT_LAM, val)
            if coc is None:
                continue
            cv = {g: pow(z, x, p) for g, x in zip(MT_GENS, c)}
            R = IL.Rep(F, MT_GENS, IL.reducible_rep(F, MT_GENS, cv, coc))
            assert R.check_relators(rels)
            bad += not all(R.word(mt_tau_of(r)) == F.eye(2) for r in rels)
            imgs = {g: g for g in MT_GENS}
            for _ in range(n):
                imgs = {g: mt_tau_of(imgs[g]) for g in MT_GENS}
            inner += all(R.word(imgs[g]) == F.mul(F.mul(R.word("t"), R.word(g)), R.word("T")) for g in MT_GENS)
            checked += 1
        out["MT"].append(dict(n=n, H1=tors, free=free, relator_lengths=[len(r) for r in rels], formal_tau=mt_formal_identity(n),
                              reps_checked=checked, tau_fails=bad, tau_n_inner=inner, phi_fixes_lambda=(apply(PHI, MT_LAM) == MT_LAM)))
    rs = {}
    F = IL.GF(601)
    for n in range(2, 7):
        gens, words, rewrite, rels, mu, lam = rs_cover(n)
        tau = rs_conj(n, 1)
        base, G = geometric_rs(F, n)
        rs[n] = dict(closed_form=(tau == {g: red(w) for g, w in rs_closed_form(n).items()}),
                     relators_trivial=all(G.word(subst(tau, r)) == F.eye(2) for r in rels),
                     conjugation_by_a=all(G.word(tau[g]) == F.mul(F.mul(base.M["a"], G.M[g]), base.M["A"]) for g in gens),
                     tau_n_is_conjugation_by_z=all(G.word(rs_conj(n, n)[g]) == F.mul(F.mul(G.M["z"], G.M[g]), G.M["Z"])
                                                   for g in gens))
    gens, words, rewrite, rels, mu, lam = rs_cover(6)
    base, G = geometric_rs(F, 6)
    rs["b1378_tau_relators_trivial"] = all(G.word(subst(B1378_TAU, r)) == F.eye(2) for r in rels)
    rs["b1378_tau2_relators_trivial"] = all(G.word(subst(B1378_TAU2, r)) == F.eye(2) for r in rels)
    rs["tau2_equals_conjugation_by_a2"] = ({g: red(subst(rs_conj(6, 1), rs_conj(6, 1)[g])) for g in gens} == rs_conj(6, 2))
    out["RS"] = rs
    return out


# ============================================================================================ C. the loci lemma
def part_c_exact(n, e):
    import sympy as sp
    s = sp.symbols("s")
    rels = mt_level(n)
    zeta = sp.exp(2 * sp.pi * sp.I / e) if e > 1 else sp.Integer(1)
    P = phi_power(n)
    Ea, Eb = IL.abelian_exponents(P["a"], ["a", "b"]), IL.abelian_exponents(P["b"], ["a", "b"])

    def fox_row(word, val):
        D = {g: sp.Integer(0) for g in MT_GENS}; pre = sp.Integer(1)
        for ch in word:
            g = ch.lower(); v = val[g]
            if ch.islower():
                D[g] += pre; pre = pre * v
            else:
                pre = pre / v; D[g] -= pre
        return D

    rows = []
    for x, y in itertools.product(range(e), repeat=2):
        if (Ea["a"] * x + Ea["b"] * y - x) % e or (Eb["a"] * x + Eb["b"] * y - y) % e:
            continue
        val = {"a": zeta ** x, "b": zeta ** y, "t": s}
        J = sp.Matrix([[sp.nsimplify(sp.expand(fox_row(r, val)[g])) for g in MT_GENS] for r in rels])
        minors = [sp.expand(sp.simplify(J[:, [i, j]].det() * s ** (2 * len(rels[1])))) for i, j in ((0, 1), (0, 2), (1, 2))]
        nz = [m for m in minors if m != 0]
        g = nz[0]
        for m in nz[1:]:
            g = sp.gcd(g, m, extension=True) if e > 2 else sp.gcd(g, m)
        coeffs = sp.Poly(g, s).all_coeffs()                      # highest degree first; strip the power of s in one step
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        lc = coeffs[0]
        g = sp.Poly([sp.nsimplify(sp.simplify(c / lc)) for c in coeffs], s)
        rows.append(dict(sigma=(x, y), gcd=str(g.as_expr())))
    return rows


def part_c_numeric(n):
    """every character with meridian values in mu_60 (and the full torsion): h^1 >= 1 only at t -> 1 with the fibre non-trivial.
    A locus has h^1 >= 1 at all three primes, as in the census: one prime alone can put a root of the golden locus s^2 - L_2n s + 1
    among its N-th roots of unity (661 does for n = 5: the roots 204 and 580 have order 22, which divides 660)"""
    P = Pres("MT", n, N=lcm(60, lcm(*h1_of(MT_GENS, mt_level(n))[0])))
    fields = [(F, F.root_of_unity(P.N)) for F in map(IL.GF, primes_for(P.N))]
    hits = Counter(); exceptions = first_prime_only = 0
    for c in P.chars:
        if not any(c):
            continue
        h1s = []
        for F, z in fields:
            val = {g: pow(z, x, F.p) for g, x in zip(P.gens, c)}
            h1s.append(IL.h1_and_cocycle(F, P.gens, P.rels, P.mu, P.lam, val)[0])
            if h1s[-1] == 0:
                break
        if min(h1s) >= 1:
            hits[c[2]] += 1
            exceptions += (c[2] != 0) or (c[0] == 0 and c[1] == 0)
        elif h1s[0] >= 1:
            first_prime_only += 1
    return dict(n=n, N=P.N, primes=[F.p for F, _ in fields], characters=len(P.chars), loci=sum(hits.values()),
                meridian_exponents=sorted(hits), exceptions=exceptions, first_prime_only=first_prime_only)


# ============================================================================================ E. pullbacks keep the index
def mt_restrict(V, n, m):
    F = V.F
    T = F.eye(V.d)
    for _ in range(n // m):
        T = F.mul(T, V.M["t"])
    return IL.Rep(F, MT_GENS, {"a": V.M["a"], "b": V.M["b"], "t": T})


def part_e(pairs=((1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 4), (2, 6), (3, 6))):
    out = []
    for m, n in pairs:
        Pm = Pres("MT", m)
        k = n // m
        C = Census(Pm, primes=primes_for(lcm(Pm.N, k)), verbose=False)
        rels_n = mt_level(n)
        F, z = C.fields[0]
        zk = F.root_of_unity(k) if k > 1 else 1
        total = kept = shapiro = firing = 0
        for (lam, a), I in C.I.items():
            V = C.module(lam, a, 0)
            R = mt_restrict(V, n, m)
            assert R.check_relators(rels_n)
            In = IL.index(R, rels_n, MT_MU, MT_LAM)[0]
            tw = 0
            for j in range(k):
                Lt = pow(zk, j, F.p) if k > 1 else 1
                W = IL.Rep(F, MT_GENS, {"a": V.M["a"], "b": V.M["b"], "t": F.scale(Lt, V.M["t"])})
                assert W.check_relators(Pm.rels)
                tw += IL.index(W, Pm.rels, MT_MU, MT_LAM)[0]
            total += 1; kept += (In == I); shapiro += (In == tw); firing += (In != 0)
        out.append(dict(base=m, cover=n, candidates=total, index_kept=kept, shapiro_twist_sum=shapiro, firing_pullbacks=firing))
        print("  ", out[-1], flush=True)
    return out


# ============================================================================================ F. the triplet, its descents, the root object
SEED_CHI = (0, 0, 15, 45, 0, 75, 105)          # B1378's seed on RS M6 (z, y_0..y_5), exponents mod 120
SEED_Y = (0, 0, 0, 0, 0, 0, 0)
SEED_G = (0, 30, 15, 15, 30, 75, 75)
N6 = 120


def rs_induce(F, V, n, m):
    """Ind from pi_1(M_n) to pi_1(M_m) (m | n; m = 1 means <a, b>), coset representatives a^(m i)"""
    gens_n, words_n, rewrite_n, *_ = rs_cover(n)
    if m == 1:
        gens_m, words_m = ["a", "b"], {"a": "a", "b": "b"}
    else:
        gens_m, words_m, *_ = rs_cover(m)
    k = n // m; d = V.d
    out = {}
    for g in gens_m:
        wg = words_m[g]
        eg = sum(1 if ch.islower() else -1 for ch in wg)
        assert eg % m == 0
        M = F.zeros(k * d, k * d)
        for i in range(k):
            j = (i + eg // m) % k
            hw, kk = rewrite_n("A" * (m * j) + wg + "a" * (m * i), 0)
            assert kk == 0
            blk = V.word(hw)
            for r in range(d):
                for c in range(d):
                    M[j * d + r][i * d + c] = blk[r][c]
        out[g] = M
    return IL.Rep(F, gens_m, out)


def rs_restrict_from_root(F, R, n):
    """a representation of <a, b> restricted to the RS generators of M_n"""
    gens, words, rewrite, rels, mu, lam = rs_cover(n)
    return IL.Rep(F, gens, {g: R.word(words[g]) for g in gens}), rels, mu, lam


def blockdiag(F, reps, gens):
    mats = {}
    for g in gens:
        dims = [R.d for R in reps]; D = sum(dims); O = F.zeros(D, D); off = 0
        for R, dd in zip(reps, dims):
            A = R.M[g]
            for i in range(dd):
                for j in range(dd):
                    O[off + i][off + j] = A[i][j]
            off += dd
        mats[g] = O
    return IL.Rep(F, gens, mats)


def rs_pullback_map(n, m):
    """the abelianized restriction H_1(M_n) -> H_1(M_m) for m | n (RS): each generator of Gamma_n as exponents in Gamma_m's"""
    gens_n, words_n, *_ = rs_cover(n)
    gens_m, words_m, rewrite_m, *_ = rs_cover(m)
    rows = []
    for g in gens_n:
        w, k = rewrite_m(words_n[g], 0)
        assert k == 0
        ab = IL.abelian_exponents(w, gens_m)
        rows.append([ab[h] for h in gens_m])
    return rows                                                    # (c o iota)(g_n) = sum_h rows[g][h] c[h]


def pullback(c, rows, N):
    return tuple(sum(r[j] * c[j] for j in range(len(c))) % N for r in rows)


def seed_classes():
    """the seed's six translates as (lam, alphas) classes on RS M6"""
    P6 = Pres("RS", 6, N=N6)
    out = []
    for j in range(6):
        chi, y, g = (P6.pull(c, j) for c in (SEED_CHI, SEED_Y, SEED_G))
        lam = P6.add(chi, coeffs=[2])
        als = tuple(P6.add(chi, y, g, coeffs=[1, sy, sg]) for (_, sy, sg) in SECTORS)
        out.append((lam, als))
    return P6, out


def part_f(primes=(601, 1201, 1321)):
    P6, S = seed_classes()
    res = dict(distinct_translates=len(set(S)), tau3_fixes_seed=(S[3] == S[0]),
               tau2_lambda_twist_order=None)
    d2 = P6.add(S[2][0], S[0][0], coeffs=[1, -1])
    res["tau2_lambda_twist_order"] = N6 // math.gcd(N6, math.gcd(*d2)) if any(d2) else 1
    # the seed's six-sector indices on M6, the tau^2-orbit sum and the full orbit
    gens6, words6, rw6, rels6, mu6, lam6 = rs_cover(6)
    # descents to s961 (RS M3) at N = 120: sector-level extensions, E6-consistent choices, their indices
    P3 = Pres("RS", 3, N=N6)
    rows = rs_pullback_map(6, 3)
    pb = {}
    for c in P3.chars:
        pb.setdefault(pullback(c, rows, N6), []).append(c)
    lam6_, als6 = S[0]
    lam3s = [c for c in pb.get(lam6_, []) if P3.val(c, P3.mu_ex) == 0]
    assert len(lam3s) == 1, lam3s                                   # T1: the extension character extends uniquely
    lam3 = lam3s[0]
    ext = [pb.get(a, []) for a in als6]
    assert all(len(e) == 2 for e in ext), [len(e) for e in ext]   # two extensions per sector
    fifth = defaultdict(list)
    for yy in P3.chars:
        fifth[tuple(5 * x % N6 for x in yy)].append(yy)
    descents = {}
    for choice in itertools.product(*ext):
        ad, aL = choice[3], choice[4]
        for yy in fifth.get(P3.add(ad, aL, coeffs=[1, -1]), []):
            kappa = P3.add(ad, yy, coeffs=[1, -2])
            als = tuple(P3.add(yy, kappa, lam3, coeffs=[sy, sg, (1 - sg) // 2]) for (_, sy, sg) in SECTORS)
            if als == tuple(choice):
                descents[als] = (kappa, yy)
    res["lam3_square"] = lam3 in P3.squares
    res["e6_descents"] = len(descents)
    # indices of every descent's six sectors on s961 (three primes)
    C3 = Census.__new__(Census)
    C3.P = P3; C3.primes = list(primes); C3.fields = []
    for p in primes:
        F = IL.GF(p); C3.fields.append((F, F.root_of_unity(N6)))
    C3.loci = {}
    cocs = []
    for (F, z) in C3.fields:
        val = {g: pow(z, x, F.p) for g, x in zip(P3.gens, lam3)}
        h1, coc = IL.h1_and_cocycle(F, P3.gens, P3.rels, P3.mu, P3.lam, val)
        assert h1 == 1 and coc is not None
        cocs.append(coc)
    C3.loci[lam3] = cocs
    drows = []
    for als in sorted(descents):
        merid = tuple(P3.val(a, P3.mu_ex) for a in als)
        idx = []
        for q in range(len(primes)):
            idx.append(tuple(C3.index(lam3, a, P3.add(a, lam3, coeffs=[1, -1]), q) for a in als))
        assert len(set(idx)) == 1, idx
        drows.append(dict(alphas_meridian=merid, all_candidates=all(m == 0 for m in merid), indices=idx[0]))
    res["descents"] = drows
    D0 = [als for als, r in zip(sorted(descents), drows) if r["all_candidates"]]
    assert len(D0) == 1
    D0 = D0[0]
    # D2: D0's orbit on s961 and its pullbacks
    orbit3 = [(P3.pull(lam3, k), tuple(P3.pull(a, k) for a in D0)) for k in range(3)]
    res["D0_orbit_on_s961"] = len(set(orbit3))
    res["D0_orbit_pulls_back_to_the_triplet"] = (sorted(set((pullback(l, rows, N6), tuple(pullback(a, rows, N6) for a in als))
                                                          for (l, als) in orbit3)) == sorted(set(S)))
    # the seed on M6: indices, the triplet sum, the full orbit; the root object R = Ind_{M3}^{m004} D0 restricted to M1..M6
    by_prime = []
    for p in primes:
        F = IL.GF(p); z = F.root_of_unity(N6)
        # M6 members
        mem = []
        sector_reps = [[] for _ in SECTORS]
        for (lam, als) in S[:3]:
            val = {g: pow(z, x, p) for g, x in zip(gens6, lam)}
            h1, coc = IL.h1_and_cocycle(F, gens6, rels6, mu6, lam6, val)
            assert h1 == 1 and coc is not None
            row = []
            for si, a in enumerate(als):
                b = P6.add(a, lam, coeffs=[1, -1])
                V = IL.Rep(F, gens6, ext_rep(F, z, gens6, a, b, coc, N6))
                assert V.check_relators(rels6)
                row.append(IL.index(V, rels6, mu6, lam6)[0]); sector_reps[si].append(V)
            mem.append(tuple(row))
        trip = tuple(IL.index(blockdiag(F, sector_reps[si], gens6), rels6, mu6, lam6)[0] for si in range(len(SECTORS)))
        # the root object from D0
        g3 = P3.gens
        val = {g: pow(z, x, p) for g, x in zip(g3, lam3)}
        h1, coc3 = IL.h1_and_cocycle(F, g3, P3.rels, P3.mu, P3.lam, val)
        level_counts = {}
        for si, a in enumerate(D0):
            b = P3.add(a, lam3, coeffs=[1, -1])
            V3 = IL.Rep(F, g3, ext_rep(F, z, g3, a, b, coc3, N6))
            assert V3.check_relators(P3.rels)
            R = rs_induce(F, V3, 3, 1)
            assert R.check_relators([RS_RELATOR])
            counts = [IL.index(R, [RS_RELATOR], "a", RS_LONGITUDE)[0]]
            for n in range(2, 7):
                Rn, rels_n, mu_n, lam_n = rs_restrict_from_root(F, R, n)
                assert Rn.check_relators(rels_n)
                counts.append(IL.index(Rn, rels_n, mu_n, lam_n)[0])
            level_counts[SECTORS[si][0]] = counts
        by_prime.append(dict(p=p, members=mem, triplet_sum=trip, root_object_counts_M1_to_M6=level_counts))
    res["by_prime"] = by_prime
    return res, (P3, lam3, D0)


# ============================================================================================ H. the s961 / M6 correspondence
def part_h(C3, classes3, C6, classes6):
    P3, P6 = C3.P, C6.P
    assert P3.N == P6.N
    rows = rs_pullback_map(6, 3)
    N = P6.N
    pulled = {}
    for key, Is in classes3.items():
        lam, als = key
        k6 = (pullback(lam, rows, N), tuple(pullback(a, rows, N) for a in als))
        pulled[key] = k6
    # D6: each pullback is a generation-shaped class of M6 with the same six counts, fixed by tau^3
    d6_in_census = sum(1 for k, k6 in pulled.items() if k6 in classes6)
    d6_same_counts = sum(1 for k, k6 in pulled.items() if classes6.get(k6) == classes3[k])
    d6_tau3 = sum(1 for k6 in pulled.values() if C6.deck_class(k6, 3) == k6)
    d6_lifted_on_M6 = sum(1 for k6 in pulled.values() if k6[0] in P6.squares)
    # P7: every tau^3-fixed generation-shaped class of M6 is a pullback
    fixed6 = [k for k in classes6 if C6.deck_class(k, 3) == k]
    images = set(pulled.values())
    p7 = sum(1 for k in fixed6 if k in images)
    return dict(s961_classes=len(classes3), pullbacks_in_M6_census=d6_in_census, pullbacks_same_counts=d6_same_counts,
                pullbacks_tau3_fixed=d6_tau3, pullbacks_lifted_on_M6=d6_lifted_on_M6,
                M6_tau3_fixed=len(fixed6), M6_tau3_fixed_lifted=sum(1 for k in fixed6 if k[0] in P6.squares),
                M6_tau3_fixed_that_are_pullbacks=p7)


# ============================================================================================ main
def main(parts):
    res = {}
    t0 = time.time()
    if "A" in parts:
        print("=== A. the covers of m004 ===", flush=True)
        res["A"] = part_a(); print(json.dumps(res["A"]), flush=True)
    if "B" in parts:
        print("=== B. presentations and the deck ===", flush=True)
        res["B"] = part_b()
        for r in res["B"]["MT"]:
            print("  MT", r, flush=True)
        print("  RS", res["B"]["RS"], flush=True)
    if "C" in parts:
        print("=== C. the loci lemma ===", flush=True)
        exact = {}
        for n, e in ((1, 1), (2, 5), (3, 4), (4, 15)):
            rows = part_c_exact(n, e)
            exact[n] = dict(sigmas=len(rows), gcds=dict(Counter(r["gcd"] for r in rows)))
            print(f"  MT M_{n} exact: {exact[n]}", flush=True)
        numeric = {n: part_c_numeric(n) for n in (5, 6)}
        for n, r in numeric.items():
            print(f"  MT M_{n} numeric: {r}", flush=True)
        res["C"] = dict(exact=exact, numeric=numeric)
    cens = {}
    if "D" in parts:
        print("=== D. the complete census ===", flush=True)
        res["D"] = {}
        for kind, n in (("MT", 1), ("MT", 2), ("MT", 3), ("MT", 4), ("RS", 1), ("RS", 2), ("RS", 3), ("RS", 4), ("RS", 5),
                        ("RS", 6)):
            P = Pres(kind, n, N=(N6 if (kind, n) == ("RS", 3) else None))
            C = Census(P)
            row, classes = census_summary(C, with_lifts=(kind == "RS" and n in (4, 5, 6)))
            res["D"][f"{kind}{n}"] = row
            cens[(kind, n)] = (C, classes)
            print("   ", {k: v for k, v in row.items() if k != "primes"}, flush=True)
    if "E" in parts:
        print("=== E. pullbacks keep the index ===", flush=True)
        res["E"] = part_e()
    if "F" in parts:
        print("=== F. the triplet, its descents, the root object ===", flush=True)
        res["F"], _ = part_f()
        print(json.dumps(res["F"], default=str), flush=True)
    if "H" in parts and ("RS", 3) in cens and ("RS", 6) in cens:
        print("=== H. the s961 / M6 correspondence ===", flush=True)
        (C3, cl3), (C6, cl6) = cens[("RS", 3)], cens[("RS", 6)]
        res["H"] = part_h(C3, cl3, C6, cl6)
        print("  ", res["H"], flush=True)
    res["seconds"] = round(time.time() - t0, 1)
    return res


if __name__ == "__main__":
    parts = [a.upper() for a in sys.argv[1:]] or list("ABCDEFH")
    res = main(parts)
    if parts == list("ABCDEFH"):
        json.dump(res, open(os.path.join(HERE, "the_level.json"), "w"), indent=1, default=str)
    print(f"DONE ({res['seconds']} s)")
