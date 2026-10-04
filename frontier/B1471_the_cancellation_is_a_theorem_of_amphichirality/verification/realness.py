#!/usr/bin/env python3
"""B1471 -- the realness of the geometric twisted Alexander function across the 112-family, as a theorem of
amphichirality and not a pattern.  Main's own route to the sep16 lane's xB011 (L245).

For a one-cusped M with holonomy rho (SL(2,C) lift repaired) and phi: pi_1 -> Z primitive, the Wada function
    R_n(t) = det(Fox matrix of Sym^n rho (x) t^phi, the column of a generator with phi != 0 deleted) / det(Sym^n rho(g_j) t^phi(g_j) - 1)
is well defined up to +- t^k.  Three properties, each tested on the FUNCTION (several real points and unit-circle points),
not on one value:
    T1  conj(R(t)) = +- R(t) at real t              ("real up to a unit": all coefficients real, or all purely imaginary)
    T2  R(1/t) = +- t^k R(t)                        (duality / palindromicity)
    T3  conj(R(t)) = +- t^k R(1/t) at real t        (conjugate-palindromicity: the symmetry step alone)
and the geometry: every orientation-reversing self-isometry f of M (SnapPy isomorphisms_to, cusp map of det -1) with
its sign s(f) = +-1 on phi read from the peripheral curves.  The theorem's two steps are then checked member by member:
    amphichiral  ==>  conj(R)(t) =. R(t^{s(f)})     [Mostow: rho o f_* ~ conj(rho); invariance under f]
    duality      ==>  R(1/t) =. R(t)
so amphichiral + duality ==> T1 (real up to a unit).  Even n is the clean case (no lift sign); odd n is reported.
"""
import sys, json, pathlib, itertools, warnings
warnings.filterwarnings("ignore")
import snappy
from mpmath import mp, mpf, mpc, matrix, eye, zeros, det, nstr, exp, pi, conj as cj, inverse
mp.dps = 60
TOL = mpf(10) ** (-25)
HERE = pathlib.Path(__file__).resolve().parent


def to_mpc(z):
    return mpc(str(z.real()).replace(" ", ""), str(z.imag()).replace(" ", ""))


def mat2(A):
    return matrix([[to_mpc(A[i, j]) for j in range(2)] for i in range(2)])


def sym(M, n):
    """Sym^n of a 2 x 2 matrix on the basis x^{n-k} y^k, k = 0..n"""
    if n == 0: return eye(1)
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    from math import comb
    S = zeros(n + 1, n + 1)
    # (a x + c y)^{n-k} (b x + d y)^k  -> coefficient of x^{n-l} y^l
    for k in range(n + 1):
        # expand
        poly = {}
        for i in range(n - k + 1):          # choose i factors of c y from (a x + c y)^{n-k}
            for j in range(k + 1):          # choose j factors of d y from (b x + d y)^k
                coef = comb(n - k, i) * comb(k, j) * a ** (n - k - i) * c ** i * b ** (k - j) * d ** j
                poly[i + j] = poly.get(i + j, 0) + coef
        for l, v in poly.items(): S[l, k] = v
    return S


def word_mat(w, rho):
    A = eye(2)
    for ch in w: A = A * (rho[ch] if ch.islower() else inverse(rho[ch.lower()]))
    return A


def expvec(w, gens):
    v = [0] * len(gens)
    for ch in w: v[gens.index(ch.lower())] += 1 if ch.islower() else -1
    return v


def setup(name, randomize=0):
    M = snappy.ManifoldHP(name)
    for _ in range(randomize): M.randomize()
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    rho = {g: mat2(G.SL2C(g)) for g in gens}
    def relsign(r):
        A = word_mat(r, rho)
        p = max(abs(A[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
        m = max(abs(A[i, j] + (1 if i == j else 0)) for i in range(2) for j in range(2))
        return 0 if p < TOL else (1 if m < TOL else None)
    want = [relsign(r) for r in rels]
    if any(w is None for w in want): return None, "holonomy fails the relators"
    if any(want):   # repair the lift: signs s_g with sum_g s_g e_g(r) = want_r mod 2
        E = [[x % 2 for x in expvec(r, gens)] for r in rels]
        sol = None
        for bits in itertools.product((0, 1), repeat=len(gens)):
            if all(sum(E[i][k] * bits[k] for k in range(len(gens))) % 2 == want[i] for i in range(len(rels))):
                sol = bits; break
        if sol is None: return None, "the PSL representation does not lift"
        for k, g in enumerate(gens):
            if sol[k]: rho[g] = -rho[g]
        assert all(relsign(r) == 0 for r in rels), "lift repair failed"
    # phi: the primitive integer vector in the kernel of the exponent matrix (H_1 rank must be 1)
    import sympy as sp
    Rm = sp.Matrix([expvec(r, gens) for r in rels]); ns = Rm.nullspace()
    if len(ns) != 1: return None, "H_1 rank %d" % len(ns)
    v = ns[0]; L = sp.ilcm(*[sp.Rational(x).q for x in v]); v = [int(x * L) for x in v]
    g0 = 0
    for x in v: g0 = sp.igcd(g0, abs(x))
    phi = {gens[i]: v[i] // g0 for i in range(len(gens))}
    # peripheral curves and phi on them
    per = G.peripheral_curves()[0]
    phi_per = tuple(sum(phi[c.lower()] * (1 if c.islower() else -1) for c in w) for w in per)
    return dict(M=M, G=G, gens=gens, rels=rels, rho=rho, phi=phi, phi_per=phi_per, h1=str(M.homology())), None


def fox_terms(word, gen):
    """the Fox derivative d word / d gen as a list of (prefix as list of (letter, +-1), sign)"""
    out, prefix = [], []
    for ch in word:
        g, e = ch.lower(), (1 if ch.islower() else -1)
        if g == gen:
            if e == 1: out.append((list(prefix), +1))
            else: out.append((list(prefix) + [(g, -1)], -1))
        prefix.append((g, e))
    return out


class Wada:
    def __init__(self, pk, n):
        self.pk, self.n, self.d = pk, n, n + 1
        self.S = {g: sym(pk["rho"][g], n) for g in pk["gens"]}
        self.Sinv = {g: inverse(self.S[g]) for g in pk["gens"]}
        self.gj = [g for g in pk["gens"] if pk["phi"][g] != 0][0]
        self.keep = [g for g in pk["gens"] if g != self.gj]
        # the Fox matrix as a dict: (row, col) -> list of (matrix, exponent of t, sign); assembled once, evaluated at any t
        self.cells = {}
        for cj_, g in enumerate(self.keep):
            for ri, r in enumerate(pk["rels"]):
                terms = []
                for pre, sgn in fox_terms(r, g):
                    A = eye(self.d); te = 0
                    for (h, e) in pre:
                        A = A * (self.S[h] if e == 1 else self.Sinv[h]); te += e * pk["phi"][h]
                    terms.append((A, te, sgn))
                self.cells[(ri, cj_)] = terms

    def value(self, t):
        d = self.d; nR, nC = len(self.pk["rels"]) * d, len(self.keep) * d
        if nR != nC: return None
        Big = zeros(nR, nC)
        for (ri, cj_), terms in self.cells.items():
            for A, te, sgn in terms:
                f = sgn * t ** te
                for i in range(d):
                    for k in range(d): Big[ri * d + i, cj_ * d + k] += f * A[i, k]
        den = det(self.S[self.gj] * t ** self.pk["phi"][self.gj] - eye(d))
        if abs(den) < TOL: return None
        return det(Big) / den


def unit_match(x, y, t, kmax=12):
    """is x = +- t^k y for an integer |k| <= kmax?  returns (k, sign) or None"""
    if abs(y) < TOL and abs(x) < TOL: return (0, 1)
    if abs(y) < TOL or abs(x) < TOL: return None
    for k in range(-kmax, kmax + 1):
        for s in (1, -1):
            if abs(x - s * t ** k * y) < TOL * max(1, abs(x)): return (k, s)
    return None


def tests(W, reals=(mpf(2), mpf(3), mpf("0.6"), mpf("1.7")), angles=(mpf("0.37"), mpf("1.11"))):
    out = dict(T1=[], T2=[], T3=[], values={})
    for t in reals:
        v = W.value(t); vi = W.value(1 / t)
        if v is None or vi is None: out["T1"].append(None); out["T2"].append(None); out["T3"].append(None); continue
        out["values"][nstr(t, 4)] = nstr(v, 15)
        c = cj(v)
        out["T1"].append(unit_match(c, v, t))                   # conj R(t) = +- R(t)  (k forced 0 at |t| != 1)
        out["T2"].append(unit_match(vi, v, t))                  # R(1/t) = +- t^k R(t)
        out["T3"].append(unit_match(c, vi, t))                  # conj R(t) = +- t^k R(1/t)
    for th in angles:   # unit circle: conj(R(t)) vs R(1/t) = R(conj t) tests only with the coefficient structure; record values
        t = exp(mpc(0, 1) * th); v = W.value(t); vi = W.value(1 / t)
        if v is None or vi is None: continue
        out.setdefault("circle", []).append(dict(theta=nstr(th, 3), R=nstr(v, 12), R_inv=nstr(vi, 12),
                                                   T2=unit_match(vi, v, t), T1c=unit_match(cj(v), vi, t)))  # conj R(t) = R(conj t) if real coefficients, up to unit
    def summary(key):
        rows = [r for r in out[key] if r is not None]
        if len(rows) < 2: return "undetermined"
        ks = {r[0] for r in rows}; ss = {r[1] for r in rows}
        return ("holds k=%s sign=%s" % (sorted(ks), sorted(ss))) if len(ks) == 1 and len(ss) == 1 else "FAILS"
    # T1 is decided on the real points alone (a unit at real t != 1 must be +-1)
    out["T1_verdict"] = "real-up-to-unit" if all(r is not None for r in out["T1"]) and out["T1"] and len({r[1] for r in out["T1"]}) == 1 else "COMPLEX"
    if out["T1_verdict"] == "real-up-to-unit": out["T1_phase"] = "real" if out["T1"][0][1] == 1 else "purely imaginary"
    out["T2_verdict"] = summary("T2"); out["T3_verdict"] = summary("T3")
    return out


def isometries(pk):
    """the self-isometries: orientation (det of the cusp map) and the sign on phi"""
    M = pk["M"]; a, b = pk["phi_per"]; rows = []
    for iso in M.isomorphisms_to(M):
        cm = iso.cusp_maps()[0]; p, q, r, s = int(cm[0, 0]), int(cm[0, 1]), int(cm[1, 0]), int(cm[1, 1])
        d = p * s - q * r
        # f_*(mu) = p mu + r lam, f_*(lam) = q mu + s lam  (SnapPy's convention: columns are images); phi o f_* on (mu, lam)
        img = (p * a + r * b, q * a + s * b)
        sgn = None
        if (a, b) != (0, 0):
            if img == (a, b): sgn = +1
            elif img == (-a, -b): sgn = -1
            else:   # try the other convention
                img2 = (p * a + q * b, r * a + s * b)
                sgn = +1 if img2 == (a, b) else (-1 if img2 == (-a, -b) else ("?", img, img2))
        rows.append(dict(det=d, cusp_map=[[p, q], [r, s]], phi_sign=sgn))
    return rows


def run(name, ns=(1, 2, 3, 4), randomize=0):
    pk, err = setup(name, randomize)
    if err: return dict(name=name, error=err)
    out = dict(name=name, h1=pk["h1"], phi=pk["phi"], phi_per=pk["phi_per"], gens=len(pk["gens"]), relators=pk["rels"])
    iso = isometries(pk); out["isometries"] = iso
    rev = [r for r in iso if r["det"] == -1]
    out["amphichiral_by_isometry"] = bool(rev); out["reversing_signs"] = sorted({str(r["phi_sign"]) for r in rev})
    out["amphichiral_snappy"] = bool(pk["M"].symmetry_group().is_amphicheiral())
    out["n"] = {}
    for n in ns:
        W = Wada(pk, n)
        if W.value(mpf(2)) is None: out["n"][n] = dict(error="nonsquare or vanishing normaliser"); continue
        out["n"][n] = tests(W)
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.endswith(".json")]
    if args == ["--family"]:
        fam = json.load(open(HERE.parents[1] / "B1235_two_seat_harvest" / "verification" / "chirality_112.json"))
        names = [r["name"] for r in fam]; col = {r["name"]: r["amphicheiral"] for r in fam}
    else:
        names, col = args or ["m004"], {}
    res = []
    for nm in names:
        r = run(nm); r["amphichiral_B1235"] = col.get(nm); res.append(r)
        # presentation-independence control on three members
        if nm in ("m004", "m003", "s955"):
            r2 = run(nm, randomize=3); r["retriangulated"] = {n: (t.get("values"), t.get("T1_verdict")) for n, t in r2.get("n", {}).items()}
    for r in res:
        if "error" in r: print(r["name"], "ERROR", r["error"]); continue
        print(r["name"], r["h1"], "phi_per", r["phi_per"], "amphi(snappy)", r["amphichiral_snappy"], "amphi(iso)", r["amphichiral_by_isometry"], "signs", r["reversing_signs"])
        for n, tr in r["n"].items():
            if "error" in tr: print("   n=%d" % n, tr["error"]); continue
            print("   n=%d  T1 %s%s  T2 %s  T3 %s  R(2)=%s" % (n, tr["T1_verdict"], (" (" + tr.get("T1_phase", "") + ")") if "T1_phase" in tr else "", tr["T2_verdict"], tr["T3_verdict"], tr["values"].get("2.0")))
    json.dump(res, open(HERE / next((a for a in sys.argv[1:] if a.endswith(".json")), "realness.json"), "w"), indent=1, default=str)
