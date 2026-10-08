#!/usr/bin/env python3
"""B1618 -- THE WEIGHTED CELL AT omega (given tau = omega).  B1617 left owed: Yukawa couplings as modular forms of weight k,
which at the fixed point omega lie in an eigenspace of the stabiliser U at the automorphy phase, not in the invariant line.
Two facts fix their shape for every weight:
  (i)  the inner automorphisms act trivially on tau (automorphy factor 1) and on the matter as the parity signs (B1617), so
       a coupling that is a function of tau lies, at every tau, in the subspace they fix;
  (ii) at omega it is moreover an eigenvector of U's lift, with eigenvalue a root of unity fixed by the weights.
Exact up to floating point, on the Dirac term T-bar (x) T and the Majorana term Sym^2 T:
 Q1  the subspace fixed by the inner automorphisms (and the sign): its dimension; whether it is the diagonal in T's parity
     lines (each line carrying a distinct parity character).
 Q2  for every phase zeta in the 24th roots of unity (all integral and half-integral weights, any matter weights): the
     zeta-eigenspace of U's lift on that subspace -- its dimension, and for each eigenvector the singular values of the
     mass matrix it defines (equal moduli = degenerate masses).
 Q3  the near-omega lemma checked numerically on the eigenvector structure: U cycles the three diagonal entries (the
     permutation it induces on T's parity lines), so the entries' leading Taylor coefficients at omega have equal moduli
     and equal orders of vanishing (stated; the check is that U acts on the diagonal as a 3-cycle times phases).
No data is read.  Writes weighted_at_omega.json."""
import json, pathlib, sys, os, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("om", FRONTIER / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
om = importlib.util.module_from_spec(spec); spec.loader.exec_module(om)
cp = om.cp; nm = om.nm; TB = cp.TB


def main():
    out = {}
    L = {"a": "a", "b": "ab"}; Linv = {"a": "a", "b": "Ab"}; R = {"a": "ab", "b": "b"}
    U = om.compose(Linv, R) if om.np.array_equal(om.h1(om.compose(Linv, R)), np.array([[0, -1], [1, 1]])) else om.compose(R, Linv)
    assert np.array_equal(om.h1(U), np.array([[0, -1], [1, 1]]))
    iota = {"a": "A", "b": "B"}; inn_a = {"a": "a", "b": "abA"}; inn_b = {"a": "baB", "b": "b"}
    MU, Mi, Ma, Mb = (om.M_of(x) for x in (U, iota, inn_a, inn_b))
    TU, Ti, Ta, Tb = (cp.restrict(M, TB) for M in (MU, Mi, Ma, Mb))
    res = {}
    for label, kind in (("Dirac T-bar(x)T", "dirac"), ("Majorana Sym2 T", "majorana")):
        if kind == "dirac":
            act = lambda A: np.kron(A.conj(), A); Bm = np.eye(9, dtype=complex)
        else:
            Bm = nm.sym_basis(); act = lambda A: Bm.conj().T @ np.kron(A, A) @ Bm
        gens = [act(Ti), act(Ta), act(Tb)]
        P = np.eye(gens[0].shape[0], dtype=complex)
        # the subspace fixed by the inner automorphisms and the sign: common eigenvalue-1 space
        stack = np.vstack([g - np.eye(g.shape[0]) for g in gens])
        _, s, Vh = np.linalg.svd(stack); k = int(sum(1 for x in s if x < 1e-8)) + max(0, stack.shape[1] - len(s))
        F = Vh[-k:].conj().T if k else np.zeros((stack.shape[1], 0))
        Fq, _ = np.linalg.qr(F)
        Ured = Fq.conj().T @ act(TU) @ Fq
        # is the fixed subspace preserved by U?
        preserved = bool(np.allclose(Fq @ Ured, act(TU) @ Fq, atol=1e-8))
        rows = []
        for n in range(24):
            z = np.exp(2j * np.pi * n / 24)
            ev, V = np.linalg.eig(Ured); sel = [i for i, e in enumerate(ev) if abs(e - z) < 1e-7]
            if not sel: continue
            for i in sel:
                v = Fq @ V[:, i]; M3 = (Bm @ v).reshape(3, 3)
                sv = np.sort(np.linalg.svd(M3, compute_uv=False))
                rows.append({"phase_24ths": n, "singular_values_normalised": [round(float(x / sv[-1]), 9) for x in sv]})
        res[label] = {"inner_fixed_dim": k, "U_preserves_it": preserved, "eigen_phases_24ths": sorted({r["phase_24ths"] for r in rows}),
                      "spectra": rows, "every_spectrum_degenerate": all(abs(r["singular_values_normalised"][0] - 1) < 1e-6 for r in rows)}
    out["Q1_Q2"] = res
    # Q3: U's action on T's parity lines: the eigenlines of the inner automorphisms on T and how U permutes them
    _, VA = np.linalg.eig(Ta + 0.3719 * Tb)                           # the joint eigenbasis of the two commuting inner lifts
    VA = VA / np.linalg.norm(VA, axis=0)
    lines = []
    for i in range(3):
        v = VA[:, i]; lines.append((round(float(np.real(np.vdot(v, Ta @ v)))), round(float(np.real(np.vdot(v, Tb @ v))))))
    perm = []
    for i in range(3):
        w = TU @ VA[:, i]
        overl = [abs(np.vdot(VA[:, j], w)) for j in range(3)]; perm.append(int(np.argmax(overl)))
    out["Q3"] = {"parity_characters_of_T_lines_(a,b)": lines, "U_permutes_lines": perm,
                 "U_is_a_3_cycle_on_the_lines": sorted(perm) == [0, 1, 2] and all(perm[i] != i for i in range(3))}
    json.dump(out, open(HERE / "weighted_at_omega.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
