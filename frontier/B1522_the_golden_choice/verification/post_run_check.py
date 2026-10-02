#!/usr/bin/env python3
"""B1522 -- post-run checks (written and run AFTER the sealed census; disclosed as such in FINDINGS).

Both routes of the census implement Lemma C's criterion. A flaw in the criterion itself would pass them both. So:

X1 (P5 directly). From route F's flags: no character whose p-primary part is a nonzero vector on one golden eigenline, at a split
   prime p, is fixed at generic lam (on every level n <= 12).
X2 (the criterion bypassed). For every character of M_n (n = 1 ... 6), build V = nu (x) rho_q on pi_n's Reidemeister-Schreier
   generators over a finite field F_p (zeta_N and i in F_p; q = 2), check that V satisfies every Reidemeister-Schreier relator,
   and test directly, for every automorphism beta in the candidate list iota^a eps^b alpha^c tau^k (a, b in {0, 1}, c in {0..3},
   k < n; 16n words covering the 8n isometries), whether (V o beta)^* is isomorphic to a target module. No dualising flag, no
   sigma, no Lemma C and no Lemma Z is used: (V o beta)(g) is computed from the word beta(g) itself.
   lam is a primitive root g of F_p whose square is not an N-th root of unity (the stand-in for a lam that is not a root of
   unity). Three readings, as in Lemma C:
     generic:  the target is V;
     real:     the targets are V and its conjugate (-v, lam) (rho_q is real; a real lam is its own conjugate);
     unitary:  the targets are V and its conjugate (-v, lam^-1) (conj(nu) = nu^-1 when |nu| = 1).
   Expected: generic and real fixed iff E, unitary fixed iff E or A, character by character, and the fixed counts equal |T_n|
   minus the census's unfixed counts. Every fixing word should be dualising (an odd number of eps and alpha letters).
   A trace filter (isomorphic modules have equal traces) only skips the linear solve when a trace already differs.
X3 (the firing members directly). The same module test on all 196 firing members (levels 1 ... 6) at their own lam (1, -1, i,
   -i), with the targets V and (-v, lam^-1).
X4 (a live control: the test can say more). The same instrument at the hyperbolic point q = 1 (t = 1/2) on levels 5 and 6, where
   rho_1 is self-dual and every isometry keeps it. Expected: at a unitary lam every character is fixed (Lemma U); at a generic lam
   a character is fixed iff some element of route F's group with sigma = -1, of either d, has vB = +-v; and non-dualising words
   now fix. So the zero non-dualising count of X2 is a property of q != 1, not of the code.
Usage: python3 post_run_check.py   (writes post_run_check.json)"""
import itertools
import json
import random
import sys
import time
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import census as C  # noqa: E402
import route_fibre as RF  # noqa: E402
import route_rs as RR  # noqa: E402

# p = 1 mod lcm(N, 4); N = 1, 5, 4, 15, 11, 40 on levels 1 ... 6
PRIMES = {1: 13, 2: 41, 3: 13, 4: 61, 5: 89, 6: 241}
IDENT = [[int(i == j) for j in range(4)] for i in range(4)]


# ------------------------------------------------------------------ F_p linear algebra
def mat_mul(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) % p for j in range(4)] for i in range(4)]


def mat_inv(A, p):
    n = len(A)
    M = [list(A[i]) + [int(i == j) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] % p), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        iv = pow(M[c][c], -1, p)
        M[c] = [x * iv % p for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] % p:
                f = M[r][c]
                M[r] = [(a - f * b) % p for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def transpose(A):
    return [list(r) for r in zip(*A)]


def scal(s, A, p):
    return [[s * x % p for x in r] for r in A]


def trace(A, p):
    return sum(A[i][i] for i in range(4)) % p


def nullspace(rows, ncols, p):
    M = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], -1, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % p
        out.append(v)
    return out


def det(A, p):
    n = len(A)
    M = [list(r) for r in A]
    d = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] % p), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d = d * M[c][c] % p
        iv = pow(M[c][c], -1, p)
        for r in range(c + 1, n):
            f = M[r][c] * iv % p
            M[r] = [(a - f * b) % p for a, b in zip(M[r], M[c])]
    return d % p


def hom_test(A, B, p):
    """A, B: the images of the same generators. Returns (dim Hom, isomorphic): an invertible X with A(g) X = X B(g) for all g."""
    rows = []
    for Ag, Bg in zip(A, B):
        for i in range(4):
            for j in range(4):
                row = [0] * 16
                for k in range(4):
                    row[k * 4 + j] = (row[k * 4 + j] + Ag[i][k]) % p
                    row[i * 4 + k] = (row[i * 4 + k] - Bg[k][j]) % p
                rows.append(row)
    basis = nullspace(rows, 16, p)
    if not basis:
        return 0, False
    if len(basis) == 1:
        X = [basis[0][i * 4:(i + 1) * 4] for i in range(4)]
        return 1, det(X, p) != 0
    # dim Hom > 1: an invertible member exists iff a random combination is invertible, up to probability (4/p)^40
    rng = random.Random(1522)
    for _ in range(40):
        coefs = [rng.randrange(p) for _ in basis]
        v = [sum(c * b[t] for c, b in zip(coefs, basis)) % p for t in range(16)]
        if det([v[i * 4:(i + 1) * 4] for i in range(4)], p):
            return len(basis), True
    return len(basis), False


def is_prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def primitive_root(p):
    fac = C.factor(p - 1)
    return next(g for g in range(2, p) if all(pow(g, (p - 1) // r, p) != 1 for r in fac))


# ------------------------------------------------------------------ the representation on pi_n
def ballas_p(q, p):
    inv2 = pow(2, -1, p)
    t = q * inv2 % p
    it = pow(t, -1, p)
    m = [[1, 0, 1, (t - 1) % p], [0, 1, 1, t], [0, 0, 1, (t + inv2) % p], [0, 0, 0, 1]]
    n = [[1, 0, 0, 0], [(2 + it) % p, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]]
    return m, n


def rs_generators(n):
    """the nontrivial Reidemeister-Schreier generators of pi_n as words in m, n: gamma_{k,n} (k < n) and z = m^n"""
    gens = [RR.transversal_word(n, k, "n") for k in range(n)]
    gens.append("m" * n)
    return gens


def rewrite(w, n):
    """a word of pi_n -> list of (generator index, +-1) in the generators of rs_generators(n); gamma_{k,m} with k < n - 1 is
    trivial, gamma_{n-1,m} = z is index n"""
    out = []
    k = 0
    for c in w:
        g = c.lower()
        if c.islower():
            if g == "n":
                out.append((k, 1))
            elif k == n - 1:
                out.append((n, 1))
            k = (k + 1) % n
        else:
            k = (k - 1) % n
            if g == "n":
                out.append((k, -1))
            elif k == n - 1:
                out.append((n, -1))
    assert k == 0, "not in pi_n"
    return out


def compose(im1, im2):
    """beta1 o beta2 (apply beta2 first): g -> beta1(beta2(g))"""
    return {g: RR.sub(im2[g], im1) for g in ("m", "n")}


def candidates(n):
    I = {"m": "m", "n": "n"}
    syms = {s: RR.SYMS[s][0] for s in RR.SYMS}
    out = []
    for a, b, c, k in itertools.product((0, 1), (0, 1), range(4), range(n)):
        im = dict(I)
        for _ in range(k):
            im = compose(syms["tau"], im)
        for _ in range(c):
            im = compose(syms["alpha"], im)
        if b:
            im = compose(syms["eps"], im)
        if a:
            im = compose(syms["iota"], im)
        out.append(((a, b, c, k), im))
    return out


class Level:
    def __init__(self, n, q=2):
        p = PRIMES[n]
        self.n, self.p, self.q = n, p, q
        self.chars, self.order, self.N = RF.characters(n)
        N = self.N
        assert is_prime(p) and (p - 1) % (N * 4 // gcd(N, 4)) == 0, (n, p, N)
        g = primitive_root(p)
        assert pow(g, 2 * N, p) != 1, "g^2 must not be an N-th root of unity"
        self.g, self.zeta, self.i4 = g, pow(g, (p - 1) // N, p), pow(g, (p - 1) // 4, p)
        m, nn = ballas_p(q, p)
        self.R = {"m": m, "n": nn, "M": mat_inv(m, p), "N": mat_inv(nn, p)}
        assert self.rho(RR.R_WORD) == IDENT, "rho_q mod p must kill the relator"
        assert self.rho("m") != IDENT and self.rho("n") != IDENT
        self.gens = rs_generators(n)
        self.rho_g = [self.rho(w) for w in self.gens]
        self.rho_g_inv = [mat_inv(X, p) for X in self.rho_g]
        self.tr_g = [trace(X, p) for X in self.rho_g]
        # the Reidemeister-Schreier relators (R from every coset) and a check of the rewriting itself
        self.relators = []
        for k in range(n):
            w = RR.red("m" * k + RR.R_WORD + "M" * k)
            rw = rewrite(w, n)
            assert self.rho_rw(rw) == self.rho(w) == IDENT
            self.relators.append(rw)
        self.cands = []
        for key, im in candidates(n):
            assert self.rho(RR.sub(RR.R_WORD, im)) == IDENT, ("not an automorphism mod p", key)
            data = []
            for w in self.gens:
                bw = RR.sub(w, im)
                rw = rewrite(bw, n)      # beta preserves pi_n: asserts the word returns to the trivial coset
                Rb = self.rho(bw)
                assert self.rho_rw(rw) == Rb, "rewriting must not change the element"
                e = [0] * (n + 1)
                for idx, s in rw:
                    e[idx] += s
                Rd = transpose(mat_inv(Rb, p))
                data.append((e, Rd, trace(Rd, p)))
            dualising = (key[1] + key[2]) % 2
            self.cands.append((key, dualising, data))

    def rho(self, w):
        X = IDENT
        for c in w:
            X = mat_mul(X, self.R[c], self.p)
        return X

    def rho_rw(self, rw):
        X = IDENT
        for idx, s in rw:
            X = mat_mul(X, self.rho_g[idx] if s == 1 else self.rho_g_inv[idx], self.p)
        return X

    def nu(self, v, lam):
        """nu on the generators: nu(gamma_k) = zeta^{(v Phi^k)_0} (times lam for k = n - 1, as gamma_{n-1} = tau^{n-1}(x) z),
        nu(z) = lam"""
        n, N, p = self.n, self.N, self.p
        out, row = [], (v[0] % N, v[1] % N)
        for k in range(n):
            val = pow(self.zeta, row[0], p)
            if k == n - 1:
                val = val * lam % p
            out.append(val)
            row = RF.act(row, RF.PHI, N)
        out.append(lam % p)
        return out

    def check_relators(self, nu):
        p = self.p
        for rw in self.relators:
            s = 1
            for idx, e in rw:
                s = s * pow(nu[idx], e, p) % p
            if s != 1:
                return False
        return True

    def fixing_words(self, v, lam, targets):
        """targets: list of (name, character, lam) for the target modules. Returns the list of (word key, target, dim Hom,
        dualising) for every candidate beta with (V o beta)^* isomorphic to a target."""
        p, n = self.p, self.n
        nu = self.nu(v, lam)
        assert self.check_relators(nu), "V must satisfy every Reidemeister-Schreier relator"
        tg = []
        for name, tv, tl in targets:
            tnu = self.nu(tv, tl)
            assert self.check_relators(tnu)
            tg.append((name, tnu, [tnu[i] * self.tr_g[i] % p for i in range(n + 1)]))
        found = []
        for key, dualising, data in self.cands:
            s_inv = []
            for e, Rd, trd in data:
                s = 1
                for j, ej in enumerate(e):
                    if ej:
                        s = s * pow(nu[j], ej, p) % p
                s_inv.append(pow(s, -1, p))
            trA = [s_inv[i] * data[i][2] % p for i in range(n + 1)]
            A = None
            for name, tnu, trT in tg:
                if trA != trT:
                    continue
                if A is None:
                    A = [scal(s_inv[i], data[i][1], p) for i in range(n + 1)]
                B = [scal(tnu[i], self.rho_g[i], p) for i in range(n + 1)]
                dim, iso = hom_test(A, B, p)
                if iso:
                    found.append({"word": list(key), "target": name, "dim Hom": dim, "dualising": dualising})
        return found


def main():
    t0 = time.time()
    census = json.loads((HERE / "census.json").read_text(encoding="utf-8"))
    by_n = {r["n"]: r for r in census["levels"]}
    res = {}
    # X1
    x1 = {}
    for n in range(1, 13):
        f = RF.flags(n)
        chars, order, N = RF.characters(n)
        split = [p for p in C.factor(order) if C.prime_type(p) == "split"] if order > 1 else []
        bad = 0
        for v in chars:
            if not f["flags"][v]["E"]:
                continue
            if any(C.eigen_type(v, N, p) in ("phi-line", "phibar-line") for p in split):
                bad += 1
        x1[str(n)] = {"split primes": split, "E-fixed characters with a single-eigenline component": bad}
    res["X1"] = {"passed": all(v["E-fixed characters with a single-eigenline component"] == 0 for v in x1.values()), "levels": x1}
    print("X1", res["X1"]["passed"], flush=True)
    # X2
    x2 = {}
    ok = True
    levels = {}
    for n in range(1, 7):
        t1 = time.time()
        L = Level(n)
        levels[n] = L
        f = RF.flags(n)
        lam = L.g
        lam_inv = pow(lam, -1, L.p)
        for kind in ("generic", "real", "unitary"):
            fixed, nondual, maxdim, mism = 0, 0, 0, []
            for v in L.chars:
                vbar = ((-v[0]) % L.N, (-v[1]) % L.N)
                targets = [("V", v, lam)]
                if kind == "real":
                    targets.append(("conj", vbar, lam))
                if kind == "unitary":
                    targets.append(("conj", vbar, lam_inv))
                found = L.fixing_words(v, lam, targets)
                is_fixed = bool(found)
                fixed += is_fixed
                nondual += sum(1 for w in found if not w["dualising"])
                maxdim = max([maxdim] + [w["dim Hom"] for w in found])
                expect = f["flags"][v]["E"] if kind in ("generic", "real") else (f["flags"][v]["E"] or f["flags"][v]["A"])
                if is_fixed != expect:
                    mism.append({"char": list(v), "direct": is_fixed, "census": expect, "words": found[:4]})
            unfixed_key = "unfixed at unitary lam" if kind == "unitary" else "unfixed at generic lam"
            expected_fixed = by_n[n]["order"] - by_n[n][unfixed_key]
            row = {"p": L.p, "lam": lam, "characters": len(L.chars), "fixed directly": fixed,
                   "fixed by the census": expected_fixed, "agree character by character": not mism,
                   "mismatches": mism[:10], "non-dualising fixing words": nondual, "largest Hom dimension": maxdim}
            ok = ok and not mism and fixed == expected_fixed and nondual == 0
            x2[f"{n} {kind}"] = row
            print("X2", n, kind, {k: row[k] for k in ("p", "characters", "fixed directly", "fixed by the census",
                                                     "agree character by character", "non-dualising fixing words",
                                                     "largest Hom dimension")}, f"({round(time.time() - t1, 1)} s)", flush=True)
    res["X2"] = {"passed": ok, "rows": x2}
    # X3: every firing member at its own lam, the conjugate allowed
    x3 = []
    ok3 = True
    for m in census["firing"]["rows"]:
        n = m["level"]
        L = levels[n]
        p = L.p
        lam = {"1": 1, "-1": p - 1, "i": L.i4, "-i": (p - L.i4) % p}[m["lam"]]
        v = tuple(m["char at level"])
        vbar = ((-v[0]) % L.N, (-v[1]) % L.N)
        found = L.fixing_words(v, lam, [("V", v, lam), ("conj", vbar, pow(lam, -1, p))])
        x3.append({"level": n, "char": list(v), "lam": m["lam"], "source": m["source"], "fixed directly": bool(found),
                   "fixing words": len(found), "non-dualising": sum(1 for w in found if not w["dualising"])})
        ok3 = ok3 and bool(found) and all(w["dualising"] for w in found)
    res["X3"] = {"passed": ok3, "members": len(x3), "fixed": sum(1 for r in x3 if r["fixed directly"]),
                 "unfixed": [r for r in x3 if not r["fixed directly"]], "rows": x3}
    print("X3", {k: res["X3"][k] for k in ("passed", "members", "fixed")}, flush=True)
    # X4: the hyperbolic point as a live control
    x4 = {}
    ok4 = True
    for n in (5, 6):
        L1 = Level(n, q=1)
        chars, order, N, G = RF.group(n)
        sigma_minus = [B for (B, s_, d_) in G if s_ == -1]
        lam = L1.g
        lam_inv = pow(lam, -1, L1.p)
        for kind in ("generic", "unitary"):
            fixed, nondual, mism = 0, 0, []
            for v in L1.chars:
                vbar = ((-v[0]) % L1.N, (-v[1]) % L1.N)
                targets = [("V", v, lam)] + ([("conj", vbar, lam_inv)] if kind == "unitary" else [])
                found = L1.fixing_words(v, lam, targets)
                fixed += bool(found)
                nondual += sum(1 for w in found if not w["dualising"])
                neg = ((-v[0]) % N, (-v[1]) % N)
                expect = True if kind == "unitary" else any(RF.act(v, B, N) in (v, neg) for B in sigma_minus)
                if bool(found) != expect:
                    mism.append({"char": list(v), "direct": bool(found), "expected": expect})
            row = {"p": L1.p, "characters": len(L1.chars), "fixed directly": fixed,
                   "expected fixed": sum(1 for v in L1.chars if (kind == "unitary" or any(RF.act(v, B, N) in (v, ((-v[0]) % N, (-v[1]) % N)) for B in sigma_minus))),
                   "agree character by character": not mism, "mismatches": mism[:10], "non-dualising fixing words": nondual,
                   "fixed at q = 2 (X2)": x2[f"{n} {kind}"]["fixed directly"]}
            ok4 = ok4 and not mism and nondual > 0 and fixed >= x2[f"{n} {kind}"]["fixed directly"]
            x4[f"{n} {kind}"] = row
            print("X4 (q = 1)", n, kind, {k: row[k] for k in ("characters", "fixed directly", "expected fixed",
                                                            "agree character by character", "non-dualising fixing words",
                                                            "fixed at q = 2 (X2)")}, flush=True)
    more = any(r["fixed directly"] > r["fixed at q = 2 (X2)"] for r in x4.values())   # the control must say more somewhere
    res["X4"] = {"passed": ok4 and more, "fixes more than at q = 2 somewhere": more, "rows": x4}
    res["seconds"] = round(time.time() - t0, 1)
    res["all passed"] = res["X1"]["passed"] and res["X2"]["passed"] and res["X3"]["passed"] and res["X4"]["passed"]
    (HERE / "post_run_check.json").write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str) + "\n")
    print("ALL PASSED" if res["all passed"] else "SOME FAILED", f"({res['seconds']} s)")


if __name__ == "__main__":
    main()
