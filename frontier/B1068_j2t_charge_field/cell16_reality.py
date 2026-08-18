"""NOTE (added 2026-08-17, B1073): THIS CELL'S tau IS NOT GATED FOR INTERTWINING.
It uses the 64 inner sign gradings -- the 2-torsion slice of the family of
root-lattice characters -- and contains no check that T(X.v) = theta(X).T(v).
B1073 builds tau as a general character, gates the intertwining over all 78x27
pairs, and finds B = A ^ tau(A) of Killing rank 3, not 24.  Read B1073 before
quoting any reality verdict computed here."""
"""AXIS 3 -- is the su(5) REAL?  Stab(s) intersect Stab(s-bar).

The su(5) found stabilises a pure spinor on the OMEGA line, and the omega covariants
require sqrt(-3).  So that su(5) lives in e6 (x) C, not e6 (x) R.  A real form needs a
CONJUGATION-STABLE subalgebra.

Conjugation here is the omega <-> omega^2 swap, i.e. sqrt(-3) -> -sqrt(-3), i.e.
Phi <-> Psi.  Pure spinors were found on BOTH lines.  If s is on the omega line and
s-bar on the omega^2 line, then Stab(s) ^ Stab(s-bar) is conjugation-stable -- a REAL
subalgebra.

SEALED BEFORE READING:
  dim 24, Killing rank 24  -> the su(5) survives conjugation: it is REAL.  Physics.
  anything smaller         -> reality costs something, and the cost is the answer.
  Report the exact (dim, reductive) either way.
"""
import os, sys, pathlib, itertools
import numpy as np, sympy as sp
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093
src = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cell5_spinor_test.py")).read_text()
src = src.split('print("\\nSTABILISER')[0].replace(
    "PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093", f"PRIME = {PRIME}")
exec(compile(src, "c5", "exec"))
import e8_build as E

def act_arr(s_arr, blk, idx):
    rows = []
    for Xb in E6_BASIS:
        d = {E.N+E.IDX[blk[i2]]: Fraction(int(s_arr[i2])%P) for i2 in range(27) if int(s_arr[i2])%P}
        img = E.br(Xb, d); col = [0]*27
        for k, val in img.items():
            col[idx[E.ROOTS[k-E.N]]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
        rows.append(col)
    return np.array(rows, dtype=np.int64).T%P

def line_and_pures(forms):
    S = [(Pm16@vec(embed_form(f, n, TWENTYSEVEN)))%P for f, n in forms]
    ind = []
    for s_ in S:
        T = np.array([[int(t)%P for t in u] for u in ind+[s_]], dtype=np.int64)
        if rank_mod_p(T) > len(ind): ind.append(s_)
    out = []
    for t in range(P):
        s_ = (ind[0]+t*ind[1])%P
        if not np.count_nonzero(s_): continue
        rws = [[int(z)%P for z in (A_.astype(object)@s_)%P] for A_ in ops]
        if 45-rank_mod_p(np.array(rws, dtype=np.int64).T%P) == 34: out.append((t, s_))
    return out

OM  = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
OM2 = [(sp.expand(Phi**2), 8), (sp.expand(Psi**4), 16), (sp.expand(Wp*Phi**2), 16)]
pw, pw2 = line_and_pures(OM), line_and_pures(OM2)
print(f"pure spinors: omega line {len(pw)} at t={[t for t,_ in pw]}, "
      f"omega^2 line {len(pw2)} at t={[t for t,_ in pw2]}", flush=True)

print("\nindividual stabilisers (control -- each must be dim 34, reductive 24):")
for nm, lst in (("omega", pw), ("omega^2", pw2)):
    for t, s_ in lst:
        print(f"  {nm} t={t}: {reductive_dim(act_arr(s_, TWENTYSEVEN, IDX27))}")

print("\nTHE REALITY TEST -- Stab(s) INTERSECT Stab(s-bar), conjugation-stable:")
for (t1, s1) in pw:
    for (t2, s2) in pw2:
        M = np.vstack([act_arr(s1, TWENTYSEVEN, IDX27), act_arr(s2, TWENTYSEVEN, IDX27)])%P
        d, kr = reductive_dim(M)
        tag = "   <<< su(5) SURVIVES CONJUGATION -- REAL >>>" if kr == 24 else ""
        print(f"  s(omega,t={t1}) ^ s(omega^2,t={t2}):  dim {d}, reductive {kr}{tag}")
