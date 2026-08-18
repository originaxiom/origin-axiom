"""NOTE (added 2026-08-17, B1073): THIS CELL'S tau IS NOT GATED FOR INTERTWINING.
It uses the 64 inner sign gradings -- the 2-torsion slice of the family of
root-lattice characters -- and contains no check that T(X.v) = theta(X).T(v).
B1073 builds tau as a general character, gates the intertwining over all 78x27
pairs, and finds B = A ^ tau(A) of Killing rank 3, not 24.  Read B1073 before
quoting any reality verdict computed here."""
"""AXIS 3c -- EXHAUST the inner real forms, not just the compact one.

The compact test (cell16) gave so(10): su(5) is not tau_compact-stable.  By THE RULE that
names a class -- ONE conjugation -- and the boundary is the other real forms.  B907 found
this object's first measurement wall is real in e6(2) and ONLY there, which is NOT compact.

Every real form's conjugation is tau_theta = theta o tau_compact for an involutive
automorphism theta.  The INNER ones are exactly the 63 nontrivial sign-gradings of the E6
root system (verified in this session: all 63 fix the full Cartan).  So this sweeps every
inner real form EXHAUSTIVELY -- 63 of 63, no sampling.

    tau_theta(e_r) = eps(r) * (-e_{-r}),  with coefficient conjugation sqrt(-3) -> -sqrt(-3)

SEALED: report, for each grading, dim and Killing rank of Stab(s) ^ Stab(tau_theta s).
  reductive 24 -> su(5) is real in that form.  PHYSICS.
  reductive 45 -> so(10), as in the compact case.
  anything else reported as found.
"""
import os, sys, pathlib, itertools
import numpy as np, sympy as sp
from fractions import Fraction
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093
src = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cell5_spinor_test.py")).read_text()
src = src.split('print("\\nSTABILISER')[0].replace(
    "PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093", f"PRIME = {PRIME}")
exec(compile(src, "c5", "exec"))
import e8_build as E

BARB = [r for r in E.ROOTS if r[6] % 3 == 2 and r[7] == 0]
IB = {r: i for i, r in enumerate(BARB)}
assert all(tuple(-x for x in r) in IB for r in TWENTYSEVEN), "27 does not negate into 27-bar"

def line(forms):
    S = [(Pm16@vec(embed_form(f, n, TWENTYSEVEN)))%P for f, n in forms]
    ind = []
    for s_ in S:
        T = np.array([[int(t)%P for t in u] for u in ind+[s_]], dtype=np.int64)
        if rank_mod_p(T) > len(ind): ind.append(s_)
    return ind

OM  = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
OM2 = [(sp.expand(Phi**2), 8), (sp.expand(Psi**4), 16), (sp.expand(Wp*Phi**2), 16)]
iw, iw2 = line(OM), line(OM2)

def act_blk(s_arr, blk, idx):
    rows = []
    for Xb in E6_BASIS:
        d = {E.N+E.IDX[blk[i2]]: Fraction(int(s_arr[i2])%P) for i2 in range(27) if int(s_arr[i2])%P}
        img = E.br(Xb, d); col = [0]*27
        for k, val in img.items():
            col[idx[E.ROOTS[k-E.N]]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
        rows.append(col)
    return np.array(rows, dtype=np.int64).T%P

def pures(ind):
    out = []
    for t in range(P):
        s_ = (ind[0]+t*ind[1])%P
        if not np.count_nonzero(s_): continue
        rws = [[int(z)%P for z in (A_.astype(object)@s_)%P] for A_ in ops]
        if 45-rank_mod_p(np.array(rws, dtype=np.int64).T%P) == 34: out.append((t, s_))
    return out

pw, pw2 = pures(iw), pures(iw2)
d2 = dict(pw2)
print(f"pure spinors: omega t={[t for t,_ in pw]}, omega^2 t={[t for t,_ in pw2]}", flush=True)

def tau_theta(s_conj_arr, eps):
    """tau_theta(s) : coefficient-conjugated (= the omega^2 vector), roots negated,
       and scaled by the sign character eps on each root."""
    out = np.zeros(27, dtype=object)
    for i2, r in enumerate(TWENTYSEVEN):
        c = int(s_conj_arr[i2]) % P
        if c:
            sgn = -1 if sum(eps[k]*r[k] for k in range(6)) % 2 else 1
            out[IB[tuple(-x for x in r)]] = (-sgn*c) % P
    return out

gradings = [e for e in itertools.product((0, 1), repeat=6) if any(e)]
print(f"inner real forms to sweep: {len(gradings)} (all 63 nontrivial sign-gradings)\n", flush=True)
spec = Counter(); hits = []
for eps in gradings:
    for (t, s1) in pw:
        ts = tau_theta(d2[t], eps)
        M = np.vstack([act_blk(s1, TWENTYSEVEN, IDX27), act_blk(ts, BARB, IB)])%P
        d, kr = reductive_dim(M)
        spec[(d, kr)] += 1
        if kr == 24: hits.append((eps, t, d, kr))
print("(dim, reductive) over all 63 inner real forms x 2 pure spinors:")
for (d, kr) in sorted(spec):
    tag = "   <<<<<< su(5) REAL IN THIS FORM >>>>>>" if kr == 24 else ("   <- so(10)" if kr == 45 else "")
    print(f"  dim {d:3d}  reductive {kr:3d}   ({spec[(d,kr)]} of {2*len(gradings)}){tag}")
print(f"\nIS su(5) REAL IN ANY INNER FORM?  {bool(hits)}")
if hits:
    print(f"  {len(hits)} hits; first few gradings: {[h[0] for h in hits[:5]]}")
