#!/usr/bin/env python3
"""Phase 1a (THE SPIN SWAP) -- the matrix-level route to fix/swap, independent of the torsion.

For an amphichiral M with lifted holonomy rho: SL(2,C), an orientation-reversing isometry f induces tau = f_* on pi_1 with
rho o tau ~ conj(rho) in PSL(2,C).  Lifting: there is C in SL(2,C) and a character eta: pi_1 -> {+-1} with
        C * conj(rho(g)) * C^-1 = eta(g) * rho(tau(g))     for every generator g.
eta trivial  <=> the mirror FIXES the spin structure of rho;  eta nontrivial <=> it SWAPS it with rho (x) eta.
tau is found by search: words w_g (length <= L) with tr rho(w_g) = +- conj(tr rho(g)), a common C solving the
intertwiner equations for all generators at once, and the relators preserved.  Controls: m004 (B279: FIX) and m003
(today's torsion: SWAP by eta = (-1)^phi)."""
import sys, json, itertools, warnings, pathlib; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = next((p for p in HERE.parents if p.name == "frontier"), pathlib.Path.cwd() / "frontier")   # in the arc, or run from the repo root
sys.path.insert(0, str(FRONTIER / "B1471_the_cancellation_is_a_theorem_of_amphichirality" / "verification"))
import realness as R
from mpmath import mp, mpf, mpc, matrix, eye, inverse, svd_c, norm, nstr, conj as cj
mp.dps = 50
TOL = mpf(10) ** -25


def conjm(M): return matrix([[cj(M[i, j]) for j in range(2)] for i in range(2)])


def words(gens, L):
    letters = [g for g in gens] + [g.upper() for g in gens]
    for n in range(1, L + 1):
        for w in itertools.product(letters, repeat=n):
            # reduced words only
            if any(w[i].lower() == w[i + 1].lower() and w[i] != w[i + 1] for i in range(n - 1)): continue
            yield "".join(w)


def intertwiner_pm(Xs, Ys):
    """C with C X_g C^-1 = eta_g Y_g for all g, eta_g = +-1: try all sign patterns; return (C, eta) or None"""
    n = len(Xs)
    for signs in itertools.product((1, -1), repeat=n):
        rows = []
        for X, Y, s in zip(Xs, Ys, signs):
            Y = s * Y
            for i in range(2):
                for j in range(2):
                    row = [mpc(0)] * 4
                    for a in range(2):
                        row[i * 2 + a] += X[a, j]; row[a * 2 + j] -= Y[i, a]
                    rows.append(row)
        U, S, Vh = svd_c(matrix(rows), full_matrices=True)
        if abs(S[3]) < TOL and abs(S[2]) > TOL:
            v = [Vh[3, i].conjugate() for i in range(4)]; C = matrix([[v[0], v[1]], [v[2], v[3]]])
            d = C[0, 0] * C[1, 1] - C[0, 1] * C[1, 0]
            if abs(d) < TOL: continue
            return C / d ** mpf("0.5"), signs
    return None


def find_tau(pk, L=5, max_solutions=40):
    """post-seal efficiency repair (the route is unchanged): C is solved from the first TWO generators' candidate pair
    (an 8 x 4 system), and the remaining generators are TESTED against their candidates by matrix distance, instead of
    an SVD per full tuple.  Candidates are tried shortest-first so solutions appear early."""
    gens, rels, rho = pk["gens"], pk["rels"], pk["rho"]
    target = {g: conjm(rho[g]) for g in gens}
    ttr = {g: target[g][0, 0] + target[g][1, 1] for g in gens}
    cand = {g: [] for g in gens}; cache = {}
    for w in words(gens, L):
        Mw = R.word_mat(w, rho); cache[w] = Mw; tr = Mw[0, 0] + Mw[1, 1]
        for g in gens:
            if abs(tr - ttr[g]) < TOL or abs(tr + ttr[g]) < TOL: cand[g].append(w)
    g0, g1 = gens[0], gens[1] if len(gens) > 1 else gens[0]
    rest = gens[2:]
    def apply(sub, word):
        out = ""
        for ch in word:
            w = sub[ch.lower()]; out += w if ch.islower() else w.swapcase()[::-1]
        return out
    sols = []
    for w0 in cand[g0]:
        for w1 in (cand[g1] if len(gens) > 1 else [None]):
            pair = intertwiner_pm([target[g0]] + ([target[g1]] if w1 else []), [cache[w0]] + ([cache[w1]] if w1 else []))
            if pair is None: continue
            C, signs = pair; Ci = inverse(C)
            sub = {g0: w0}; eta = {g0: signs[0]}
            if w1: sub[g1] = w1; eta[g1] = signs[1]
            ok = True
            for g in rest:                      # test: C conj rho(g) C^-1 must equal +- rho(w) for some candidate w
                X = C * target[g] * Ci; hit = None
                for w in cand[g]:
                    Y = cache[w]
                    if norm(X - Y) < TOL: hit = (w, 1); break
                    if norm(X + Y) < TOL: hit = (w, -1); break
                if hit is None: ok = False; break
                sub[g] = hit[0]; eta[g] = hit[1]
            if not ok: continue
            relok = True
            for rel in rels:
                Mr = R.word_mat(apply(sub, rel), rho)
                if min(norm(Mr - eye(2)), norm(Mr + eye(2))) > TOL: relok = False; break
            if not relok: continue
            char_ok = all((sum(1 for ch in rel if eta[ch.lower()] == -1) % 2 == 0) for rel in rels)
            if not char_ok:                 # guard (the audit lane's point 2): a sign pattern that is not a character of pi_1 is not a witness
                raise AssertionError("eta is not a character of pi_1 on %s: %s" % (list(rels), eta))
            sols.append(dict(tau=dict(sub), eta=dict(eta), eta_is_character=char_ok, eta_trivial=all(v == 1 for v in eta.values())))
            if len(sols) >= max_solutions: return sols
    return sols


def classify(nm, Ls=(5, 6, 7)):
    """search at increasing word length until a solution appears; return the member's verdict and the set of eta's.
    Post-seal cap, disclosed: members with no orientation-reversing isometry by SnapPy are searched to L = 5 only
    (exhausting L = 7 on a three-generator chiral member costs hours and can only confirm an absence SnapPy states)."""
    pk, err = R.setup(nm)
    if err: return dict(name=nm, error=err)
    amph = bool(pk["M"].symmetry_group().is_amphicheiral())
    if not amph: Ls = (5,)
    for L in Ls:
        sols = find_tau(pk, L=L)
        if sols: break
    etas = sorted({tuple(sorted(s["eta"].items())) for s in sols})
    verdict = None if not sols else ("FIX" if all(s["eta_trivial"] for s in sols) else ("SWAP" if all(not s["eta_trivial"] for s in sols) else "MIXED"))
    return dict(name=nm, gens=pk["gens"], rels=pk["rels"], phi=pk["phi"], h1=pk["h1"], amphichiral_snappy=amph, L=L, n_solutions=len(sols), etas=[dict(e) for e in etas],
                verdict=verdict if sols else ("NONE-at-L%d" % L), solutions=sols[:6])


if __name__ == "__main__":
    args = sys.argv[1:]
    outname = next((a for a in args if a.endswith(".json")), "spin_swap.json"); args = [a for a in args if not a.endswith(".json")]
    if args == ["--family"]:
        fam = json.load(open(FRONTIER / "B1235_two_seat_harvest" / "verification" / "chirality_112.json"))
        names = [r["name"] for r in fam]
    else:
        names = args or ["m004", "m003"]
    out = {}
    for nm in names:
        r = classify(nm); out[nm] = r
        json.dump(out, open(pathlib.Path(__file__).parent / outname, "w"), indent=1, default=str)
        if "error" in r: print(nm, "ERR", r["error"]); continue
        print(nm, r["h1"], "gens", len(r["gens"]), "L", r["L"], "solutions", r["n_solutions"], "etas", r["etas"], "->", r["verdict"])

