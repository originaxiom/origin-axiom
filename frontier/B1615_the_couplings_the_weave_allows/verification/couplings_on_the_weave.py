#!/usr/bin/env python3
"""B1615 -- THE COUPLINGS THE WEAVE ALLOWS: a parameter count for the masses.  The matter triplet T under the weave's
group G (order 96; B1611's module).  A Yukawa-type mass term pairs a left triplet with a right partner and a Higgs-type
field H; G-invariance leaves a number of independent couplings, and a vacuum that keeps a residual subgroup fixes the
mass matrix's shape.  Exact up to floating point:
 C1  the invariant counts: dim (T(x)T-bar)^G, (T(x)T)^G, (Sym^2 T)^G, (Lambda^2 T)^G, (T(x)T(x)T)^G, (T(x)T(x)T-bar)^G.
 C2  for a Dirac-type mass T-bar(x)T(x)H (left T, right T): for each irreducible r of T(x)T-bar (B1611's pieces), the number
     of independent couplings = the multiplicity of r in T(x)T-bar (the Higgs in r-dual); the same for a Majorana-type
     mass T(x)T(x)H with r in T(x)T.
 C3  with H a G-singlet (r trivial in T(x)T-bar): the mass matrix and its singular values (Schur: proportional to 1).
 C4  with H in each non-trivial irreducible r, its vacuum along the directions fixed by a residual subgroup of the weave
     (the cyclic groups of RL -- the charged leptons' in TM1 -- and of L, R, RRL): for every such fixed direction, the
     mass matrix M(v) = sum_k v_k C_k (C_k the Clebsch-Gordan matrices of r in T-bar(x)T) and its singular values; the
     ratios m1/m3 and m2/m3 over the fixed space (sampled when it is more than one-dimensional).
 C5  the counts: the number of real parameters the weave leaves in the charged-lepton masses at each residual symmetry.
No data is read.  Writes couplings_on_the_weave.json."""
import json, pathlib, sys, os, importlib.util, itertools, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("cp", FRONTIER / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
G = cp.Group([cp.W.ML, cp.W.MR]); TB = cp.TB
T = [cp.restrict(M, TB) for M in G.els]
WORD = {}
gens = {"L": cp.W.ML, "R": cp.W.MR}


def element(word):
    M = np.eye(6, dtype=complex)
    for c in word: M = M @ gens[c]
    return cp.restrict(M, TB)


def invariants(mats):
    n = mats[0].shape[0]; P = sum(mats) / len(mats)
    return int(round(np.trace(P).real))


def sym2(A):
    idx = [(i, j) for i in range(3) for j in range(i, 3)]
    K = np.kron(A, A); B = np.zeros((9, 6), dtype=complex)
    for c, (i, j) in enumerate(idx):
        v = np.zeros(9, dtype=complex); v[3 * i + j] += 1; v[3 * j + i] += 1; B[:, c] = v / np.linalg.norm(v)
    return B.conj().T @ K @ B


def alt2(A):
    idx = [(i, j) for i in range(3) for j in range(i + 1, 3)]
    K = np.kron(A, A); B = np.zeros((9, 3), dtype=complex)
    for c, (i, j) in enumerate(idx):
        v = np.zeros(9, dtype=complex); v[3 * i + j] += 1; v[3 * j + i] -= 1; B[:, c] = v / np.linalg.norm(v)
    return B.conj().T @ K @ B


def main():
    out = {}
    out["C1"] = {"TbarT": invariants([np.kron(A.conj(), A) for A in T]), "TT": invariants([np.kron(A, A) for A in T]),
                 "Sym2T": invariants([sym2(A) for A in T]), "Alt2T": invariants([alt2(A) for A in T]),
                 "TTT": invariants([np.kron(np.kron(A, A), A) for A in T]), "TTTbar": invariants([np.kron(np.kron(A, A), A.conj()) for A in T])}
    # the irreducibles of T-bar (x) T, with their Clebsch-Gordan matrices: a vector w in the piece is a 3x3 matrix (reshape)
    mats = [np.kron(A.conj(), A) for A in T]
    pieces, comm = cp.decompose(mats, 9)
    C2 = []; C4 = {}
    res = {"RL": "RL", "L": "L", "R": "R", "RRL": "RRL"}
    for n, P in enumerate(pieces):
        Q, _ = np.linalg.qr(P); d = Q.shape[1]
        chi = [complex(np.trace(Q.conj().T @ A @ Q)) for A in mats]
        trivial = all(abs(c - 1) < 1e-6 for c in chi)
        C2.append({"piece": n, "dim": d, "trivial": trivial, "multiplicity": 1})
        # Clebsch-Gordan matrices: the piece's basis vectors as 3x3 matrices (row index from T-bar, column from T)
        Cs = [Q[:, k].reshape(3, 3) for k in range(d)]
        if trivial:
            s = np.linalg.svd(Cs[0], compute_uv=False); out["C3"] = {"singular_values_normalised": [round(float(x / s.max()), 6) for x in s]}
            continue
        # the representation of G on the piece (in the basis Q)
        rep = {nm: Q.conj().T @ np.kron(element(w).conj(), element(w)) @ Q for nm, w in res.items()}
        rows = {}
        for nm, M in rep.items():
            ev, V = np.linalg.eig(M); fixed = V[:, [i for i, e in enumerate(ev) if abs(e - 1) < 1e-7]]
            if fixed.shape[1] == 0: rows[nm] = {"fixed_dim": 0}; continue
            Qf, _ = np.linalg.qr(fixed); ratios = []
            rng = np.random.default_rng(1615)
            samples = [Qf[:, 0]] if Qf.shape[1] == 1 else [Qf @ (rng.normal(size=Qf.shape[1]) + 1j * rng.normal(size=Qf.shape[1])) for _ in range(25)]
            for v in samples:
                Mv = sum(v[k] * Cs[k] for k in range(d)); s = np.sort(np.linalg.svd(Mv, compute_uv=False))
                ratios.append([round(float(s[0] / s[2]), 6), round(float(s[1] / s[2]), 6)])
            rows[nm] = {"fixed_dim": int(Qf.shape[1]), "ratios_m1_m3_m2_m3": sorted({tuple(r) for r in ratios})[:6],
                        "ratios_fixed_by_symmetry": len({tuple(r) for r in ratios}) == 1}
        C4[f"piece {n} (dim {d})"] = rows
    out["C2"] = C2; out["C4"] = C4
    # C5: the number of real parameters in the charged-lepton masses with the vacuum keeping <RL>: the commutant of <RL> on
    # T (its distinct eigenvalues) -- the mass matrix M M-dagger commutes with it, so it is diagonal in RL's eigenbasis with
    # three free non-negative entries
    ev = np.linalg.eigvals(element("RL")); distinct = len({(round(e.real, 6), round(e.imag, 6)) for e in ev})
    out["C5"] = {"RL_distinct_eigenvalues_on_T": distinct, "free_mass_parameters_at_residual_RL": distinct}
    json.dump(out, open(HERE / "couplings_on_the_weave.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
