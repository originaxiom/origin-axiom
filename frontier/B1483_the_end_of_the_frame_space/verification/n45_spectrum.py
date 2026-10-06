#!/usr/bin/env python3
"""B1483, the optional cell of the seal: the spin-signed trace spectrum of N_45 (m003's five-cusped cyclic cover of
degree 45).  POST-SEAL VARIANT of B1477's signed_spectrum.py, disclosed: that instrument enumerates sign vectors on the
unsimplified presentation's generators (2^n), which is impossible at 90 tetrahedra; here the lifts are found by linear
algebra over F_2 (cover_theorem_a.characters).  The test is the same: for a spin structure s the multiset
{tr rho_s(gamma) : length(gamma) <= cutoff} against its complex conjugate."""
import sys, json, collections, pathlib, warnings, time; warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); FR = next(p for p in HERE.parents if p.name == "frontier")
sys.path.insert(0, str(FR / "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp" / "verification"))
import cover_theorem_a as C, signed_spectrum as SP
cutoff = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
t0 = time.time()
N = [x for x in snappy.Manifold("m003").covers(45, cover_type="cyclic") if x.num_cusps() == 5][0]
spec = N.length_spectrum(cutoff, include_words=True, grouped=False); print("geodesics to %.2f: %d (%.0f s)" % (cutoff, len(spec), time.time() - t0), flush=True)
M = N.high_precision(); G = M.fundamental_group(simplify_presentation=False, fillings_may_affect_generators=False, minimize_number_of_generators=False)
gens, rels = G.generators(), G.relators(); rho = {g: SP.mat2(G.SL2C(g)) for g in gens}; rinv = {g: SP.inv2(rho[g]) for g in gens}
# repair the lift on this presentation (signs x with E x = want over F_2), then all characters
def relsign(r):
    A = SP.word_mat(r, rho, rinv)
    p = max(abs(A[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2)); m = max(abs(A[i, j] + (1 if i == j else 0)) for i in range(2) for j in range(2))
    return 0 if p < 1e-25 else (1 if m < 1e-25 else None)
want = [relsign(r) for r in rels]; assert all(w is not None for w in want)
import sympy as sp
E = sp.Matrix([[sum(1 for ch in r if ch.lower() == g) % 2 for g in gens] + [w] for r, w in zip(rels, want)])
red, piv = C.gf2_rref(E)
for row, c in piv:
    if red[row][-1]: rho[gens[c]] = -rho[gens[c]]; rinv[gens[c]] = -rinv[gens[c]]
assert all(relsign(r) == 0 for r in rels)
chars = C.characters(gens, rels); print("generators %d, spin structures %d (%.0f s)" % (len(gens), len(chars), time.time() - t0), flush=True)
words = [g["word"] for g in spec]; tr0 = [complex(SP.word_mat(w, rho, rinv)[0, 0] + SP.word_mat(w, rho, rinv)[1, 1]) for w in words]
key = lambda z: (round(z.real, 6), round(z.imag, 6)); rows = []
T2 = [z * z for z in tr0]; A2 = collections.Counter(key(z) for z in T2); B2 = collections.Counter(key(z.conjugate()) for z in T2)
for chi in chars:
    T = []
    for w, t in zip(words, tr0):
        s = 1
        for ch in w: s *= chi[ch.lower()]
        T.append(s * t)
    A = collections.Counter(key(z) for z in T); B = collections.Counter(key(z.conjugate()) for z in T)
    rows.append(dict(symmetric=(A == B), mismatch=sum(((A - B) + (B - A)).values())))
out = dict(cutoff=cutoff, geodesics=len(words), spin_structures=len(chars), symmetric=sum(r["symmetric"] for r in rows), sign_free_multiset_symmetric=(A2 == B2), seconds=time.time() - t0, rows=rows)
json.dump(out, open(HERE / "n45_spectrum.json", "w"), indent=0); print(json.dumps({k: v for k, v in out.items() if k != "rows"}), flush=True)
