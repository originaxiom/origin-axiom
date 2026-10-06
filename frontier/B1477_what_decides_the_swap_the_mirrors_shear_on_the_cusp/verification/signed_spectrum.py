#!/usr/bin/env python3
"""B1477 instrument: the spin-signed trace spectrum.  For a spin structure s (an SL(2,C) lift rho_s) the multiset
T_s(l) = { tr rho_s(gamma) : gamma a closed geodesic of length <= l } is an invariant of (M, s).  An orientation-reversing
isometry fixing s carries it to its complex conjugate, so  T_s != conj(T_s)  certifies that NO mirror fixes s -- with no
enumeration of isometries, for any H_1 rank, closed manifolds included.  (Symmetry is necessary, not sufficient.)"""
import sys, json, itertools, collections, warnings; warnings.filterwarnings("ignore")
import snappy
from mpmath import mp, mpc, matrix, eye
mp.dps = 40
TOL = 1e-9


def to_mpc(z): return mpc(str(z.real()).replace(" ", ""), str(z.imag()).replace(" ", ""))
def mat2(A): return matrix([[to_mpc(A[0, 0]), to_mpc(A[0, 1])], [to_mpc(A[1, 0]), to_mpc(A[1, 1])]])
def inv2(A): return matrix([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])
def word_mat(w, rho, rinv):
    A = eye(2)
    for ch in w: A = A * (rho[ch] if ch.islower() else rinv[ch.lower()])
    return A


def lifts(name):
    """every SL(2,C) lift of the holonomy on the UNSIMPLIFIED presentation (the one the length spectrum's words use)"""
    M = snappy.ManifoldHP(name)
    G = M.fundamental_group(simplify_presentation=False, fillings_may_affect_generators=False, minimize_number_of_generators=False)
    gens, rels = G.generators(), G.relators()
    rho = {g: mat2(G.SL2C(g)) for g in gens}; rinv = {g: inv2(rho[g]) for g in gens}
    def relsign(r, signs):
        A = word_mat(r, rho, rinv); s = 1
        for ch in r: s *= signs[ch.lower()]
        p = max(abs(s * A[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
        m = max(abs(s * A[i, j] + (1 if i == j else 0)) for i in range(2) for j in range(2))
        return 0 if p < 1e-25 else (1 if m < 1e-25 else None)
    out = []
    for bits in itertools.product((1, -1), repeat=len(gens)):
        signs = dict(zip(gens, bits))
        if all(relsign(r, signs) == 0 for r in rels): out.append(signs)
    return M, G, gens, rho, rinv, out


def spectrum(name, cutoff):
    M, G, gens, rho, rinv, ls = lifts(name)
    Ml = snappy.Manifold(name)
    spec = Ml.length_spectrum(cutoff, include_words=True, grouped=False)
    words = [g["word"] for g in spec]
    base = [word_mat(w, rho, rinv) for w in words]
    tr0 = [complex(A[0, 0] + A[1, 1]) for A in base]
    rows = []
    for signs in ls:
        T = []
        for w, t in zip(words, tr0):
            s = 1
            for ch in w: s *= signs[ch.lower()]
            T.append(s * t)
        key = lambda z: (round(z.real, 6), round(z.imag, 6))
        A = collections.Counter(key(z) for z in T); B = collections.Counter(key(z.conjugate()) for z in T)
        diff = sum(((A - B) + (B - A)).values())
        # the first length at which the two multisets part
        first = None
        if diff:
            bad = set((A - B).keys()) | set((B - A).keys())
            first = min(float(g["length"].real()) for g, z in zip(spec, T) if key(z) in bad or key(z.conjugate()) in bad)
        rows.append(dict(signs=[signs[g] for g in gens], symmetric=(diff == 0), mismatch=diff, first_asymmetric_length=first))
    return dict(name=name, cutoff=cutoff, geodesics=len(words), n_spin=len(ls), rows=rows,
                n_symmetric=sum(r["symmetric"] for r in rows))


if __name__ == "__main__":
    cutoff = float(sys.argv[1])
    for nm in sys.argv[2:]:
        r = spectrum(nm, cutoff)
        print(nm, "cutoff", cutoff, "geodesics", r["geodesics"], "spin", r["n_spin"], "symmetric:", r["n_symmetric"], [(x["symmetric"], x["mismatch"], x["first_asymmetric_length"]) for x in r["rows"]], flush=True)
