#!/usr/bin/env python3
"""B1618 -- POST-SEAL CELL (2026-10-08): THE MAJORANA TERM AT EVERY AUTOMORPHY PHASE OF THE SIGN.  B1618's sealed
instrument took the sign iota (= -I in SL(2, Z), fixing every tau) with eigenvalue +1 on the coupling, the even-weight case,
and found nothing fixed in Sym^2 T; the odd-weight case was left uncomputed (FINDINGS; the audit lane's relay of
2026-10-08 named it again).  For a coupling of weight k, iota acts with the automorphy factor (-1)^k (with a multiplier
system, any root of unity), and the inner automorphisms with factor 1.  This cell takes EVERY eigenvalue lambda of iota on
Sym^2 T:
 O1  the subspace of Sym^2 T fixed by both inner automorphisms on which iota acts as lambda; its dimension.
 O2  where it is non-zero: whether U (the stabiliser of omega) preserves it, U's eigenvalues on it, and the Takagi values
     (singular values) of every U-eigenvector -- degenerate or not -- and, away from omega, of a generic element of the
     subspace (the coupling at a general tau, where U imposes nothing).
No data is read.  Writes post_seal_odd_weight.json."""
import json, pathlib, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wo", HERE / "weighted_at_omega.py")
wo = importlib.util.module_from_spec(spec); spec.loader.exec_module(wo)
om, cp, nm = wo.om, wo.cp, wo.nm


def main():
    TB = cp.TB
    L = {"a": "a", "b": "ab"}; Linv = {"a": "a", "b": "Ab"}; R = {"a": "ab", "b": "b"}
    U = om.compose(Linv, R) if np.array_equal(om.h1(om.compose(Linv, R)), np.array([[0, -1], [1, 1]])) else om.compose(R, Linv)
    iota = {"a": "A", "b": "B"}; inn_a = {"a": "a", "b": "abA"}; inn_b = {"a": "baB", "b": "b"}
    TU, Ti, Ta, Tb = (cp.restrict(om.M_of(x), TB) for x in (U, iota, inn_a, inn_b))
    Bm = nm.sym_basis(); act = lambda A: Bm.conj().T @ np.kron(A, A) @ Bm
    Ai, Aa, Ab, AU = act(Ti), act(Ta), act(Tb), act(TU)
    n = Ai.shape[0]
    # the inner-fixed subspace first
    stack = np.vstack([Aa - np.eye(n), Ab - np.eye(n)])
    _, s, Vh = np.linalg.svd(stack); k = int(sum(1 for x in s if x < 1e-8)) + max(0, n - len(s))
    F = Vh[n - k:].conj().T if k else np.zeros((n, 0)); F, _ = np.linalg.qr(F) if k else (F, None)
    out = {"inner_fixed_dim_in_Sym2T": k, "iota_eigenvalues_on_Sym2T": sorted({(round(float(np.real(e)), 6), round(float(np.imag(e)), 6)) for e in np.linalg.eigvals(Ai)})}
    cells = []
    if k:
        Ir = F.conj().T @ Ai @ F
        for lam in sorted({complex(round(float(np.real(e)), 6), round(float(np.imag(e)), 6)) for e in np.linalg.eigvals(Ir)}, key=lambda z: np.angle(z)):
            st = Ir - lam * np.eye(k); _, s2, Vh2 = np.linalg.svd(st)
            d = int(sum(1 for x in s2 if x < 1e-8)) + max(0, k - len(s2))
            E = F @ Vh2[k - d:].conj().T; E, _ = np.linalg.qr(E)
            Ur = E.conj().T @ AU @ E
            pres = bool(np.allclose(E @ Ur, AU @ E, atol=1e-8))
            rows = []
            ev, V = np.linalg.eig(Ur)
            for i in range(d):
                M3 = (Bm @ (E @ V[:, i])).reshape(3, 3); sv = np.sort(np.linalg.svd(M3, compute_uv=False))
                rows.append({"U_eigenvalue_turns": round(float(np.angle(ev[i]) / (2 * np.pi)) % 1, 6),
                             "takagi_normalised": [round(float(x / sv[-1]), 9) for x in sv]})
            rng = np.random.default_rng(1618); g = E @ (rng.normal(size=d) + 1j * rng.normal(size=d))
            sv = np.sort(np.linalg.svd((Bm @ g).reshape(3, 3), compute_uv=False))
            cells.append({"iota_eigenvalue": [lam.real, lam.imag], "dim": d, "U_preserves": pres, "at_omega": rows,
                          "generic_tau_takagi_normalised": [round(float(x / sv[-1]), 9) for x in sv]})
    out["cells"] = cells
    out["every_omega_spectrum_degenerate_or_zero"] = all(
        any(abs(r["takagi_normalised"][i] - r["takagi_normalised"][j]) < 1e-6 for i in range(3) for j in range(i + 1, 3))
        for c in cells for r in c["at_omega"])
    json.dump(out, open(HERE / "post_seal_odd_weight.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
