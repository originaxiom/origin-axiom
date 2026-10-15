#!/usr/bin/env python3
"""Referee checks (read-only use of main's arcs extracted into ./main). Not part of the repo."""
import os, sys, math, itertools, importlib.util, pathlib, json
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
FR = HERE / "main" / "frontier"
os.environ["OA_FRONTIER"] = str(FR)
spec = importlib.util.spec_from_file_location("cp", FR / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
H = cp.H
TB = cp.TB
AL = cp.restrict(cp.W.ML, TB); AR = cp.restrict(cp.W.MR, TB)
A_RL = cp.restrict(cp.W.MR @ cp.W.ML, TB); A_RRL = cp.restrict(cp.W.MR @ cp.W.MR @ cp.W.ML, TB)
G = cp.Group([cp.W.ML, cp.W.MR]); GT = [cp.restrict(M, TB) for M in G.els]
print("|G| =", len(GT))
# 1. is T invariant, are restricted matrices unitary in TB coords, and the HR form on T in TB coords
print("T invariant:", all(np.allclose(TB @ cp.restrict(M, TB), M @ TB, atol=1e-9) for M in G.els))
print("max unitarity defect of restricted group (TB std Hermitian):", max(np.abs(A.conj().T @ A - np.eye(3)).max() for A in GT))
Ht = TB.conj().T @ H.Hm @ TB
print("HR (Hm) restricted to T in TB coords, eigenvalues:", np.round(np.linalg.eigvalsh((Ht + Ht.conj().T) / 2), 12))
print("Ht proportional to I? dev:", np.abs(Ht / Ht[0, 0] - np.eye(3)).max())
print("TB orthonormal (std):", np.abs(TB.conj().T @ TB - np.eye(3)).max())

# 2. invariant symmetric forms: solve A^T B A = chi(A) B for all group elements, independent route (stack over all 96)
def sym_basis():
    out = []
    for a in range(3):
        for b in range(a, 3):
            E = np.zeros((3, 3), complex); E[a, b] = 1; E[b, a] = 1; out.append(E)
    return out
SYM = sym_basis()
# for each candidate character value on generators, nullspace
def inv_forms(gens):
    sols = []
    # characters: chi(AL), chi(AR) must be such that A^T B A = chi B; chi = eig of phi(A); scan
    def phi(A):
        M = np.array([(A.T @ E @ A).flatten() for E in SYM]).T
        S = np.array([E.flatten() for E in SYM]).T
        return np.linalg.lstsq(S, M, rcond=None)[0]
    P = [phi(A) for A in gens]
    for lams in itertools.product(*[np.linalg.eigvals(p) for p in P]):
        Mst = np.vstack([p - l * np.eye(6) for p, l in zip(P, lams)])
        _, s, Vh = np.linalg.svd(Mst)
        for k in range(6):
            if s[5 - k] < 1e-9:
                c = Vh[5 - k].conj(); Bm = sum(ci * E for ci, E in zip(c, SYM)); Bm /= np.linalg.norm(Bm)
                if all(abs(np.vdot(Bm.flatten(), S0.flatten())) < 1 - 1e-8 for S0 in sols): sols.append(Bm)
    return sols
sols = inv_forms([AL, AR])
print("invariant symmetric forms (gens):", len(sols))
Bf = sols[0] / np.linalg.svd(sols[0], compute_uv=False)[0]
print("B singular values:", np.linalg.svd(Bf, compute_uv=False))
print("B invariant (up to char) for all 96:", max(np.linalg.norm(A.T @ Bf @ A - (np.trace(np.linalg.pinv(Bf) @ A.T @ Bf @ A) / 3) * Bf) for A in GT))
# 3. the frame
def sig(w, B=None):
    w = np.asarray(w, complex); bb = w @ w if B is None else w @ B @ w
    return float(abs(bb) / np.vdot(w, w).real)
def axis(A):
    ev, V = np.linalg.eig(A)
    return max((V[:, k] / np.linalg.norm(V[:, k]) for k in range(3)), key=lambda v: sig(v, Bf))
fL, fR = axis(AL), axis(AR)
_, _, Vh3 = np.linalg.svd(np.vstack([fL.conj(), fR.conj()])); f3 = Vh3[-1].conj()
ph = lambda f: f / np.sqrt(f @ Bf @ f)
fL, fR, f3 = ph(fL), ph(fR), ph(f3)
F = np.column_stack([fL, fR, f3])
print("frame Hermitian-orthonormal:", np.abs(F.conj().T @ F - np.eye(3)).max(), " B-orthonormal:", np.abs(F.T @ Bf @ F - np.eye(3)).max())
Finv = np.linalg.inv(F)
def in_frame(A): return Finv @ A @ F
def real_part_up_to_scalar(A):
    Af = in_frame(A); k = np.argmax(np.abs(Af)); z = Af.flatten()[k] / abs(Af.flatten()[k])
    S = Af / z; return z, S, np.abs(S.imag).max()
for name, A in (("L", AL), ("R", AR), ("RL", A_RL), ("RRL", A_RRL)):
    z, S, im = real_part_up_to_scalar(A)
    Sr = S.real
    ang = math.degrees(math.acos(max(-1, min(1, (np.trace(Sr) - 1) / 2))))
    ev, V = np.linalg.eig(Sr); ax = V[:, np.argmin(np.abs(ev - 1))].real
    print(f"{name}: imag defect {im:.1e}, det {np.linalg.det(Sr):+.3f}, rotation angle {ang:.1f} deg, axis {np.round(ax / np.max(np.abs(ax)), 4)}")
np.save(HERE / "frame.npy", F); np.save(HERE / "Bf.npy", Bf)
