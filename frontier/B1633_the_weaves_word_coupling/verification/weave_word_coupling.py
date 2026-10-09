#!/usr/bin/env python3
"""B1633 -- THE WEAVE'S WORD COUPLING.  The SM seat's W42: a thread's own H^1 (its T part, by the Wang sequence the fixed space of
the thread's monodromy on T) reads the rule's word, and it breaks the parity grading -- but only democratically, and it is a
thread result.  The weave-level question: averaged over ALL threads of length n with the weave's uniform measure, what does
the coupling read?  Exact counting over the weave's group G (order 96): N_n(g) = the number of words of length n in L, R
whose lift is g (all words; the primitive ones differ by O(2^{n/2})), by dynamic programming.  Exact up to floating point;
no data.
 W1  the distribution of the lifts: the support of N_n (a coset of which subgroup) and its distance from uniform on it, in
     total variation, for n = 1 .. 40 (how fast the weave's measure equidistributes).
 W2  the averaged coupling Pi_n = sum_g N_n(g) P_g / sum_g N_n(g), P_g the orthogonal projector (in a G-invariant inner
     product) onto the fixed space of g on T: its trace (the mean zero-mode count), its distance from the nearest scalar
     (|| Pi_n - (tr Pi_n / 3) I ||), for n = 1 .. 40.
 W3  the limit: Pi_inf on each coset of the support (even and odd n) -- scalar (Schur) or not.
 W4  the fraction of words of length n whose lift has a non-zero fixed space on T (threads with zero modes), against the
     seat's census (237 of 745 primitive threads to length 12).
Writes weave_word_coupling.json."""
import json, pathlib, os, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("cp", FRONTIER / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)


def main():
    G = cp.Group([cp.W.ML, cp.W.MR]); n_el = G.n
    T0 = [cp.restrict(M, cp.TB) for M in G.els]
    K = sum(M.conj().T @ M for M in T0) / len(T0)
    w, E = np.linalg.eigh(K); Kh = E @ np.diag(np.sqrt(w)) @ E.conj().T; Khi = np.linalg.inv(Kh)
    T = [Kh @ M @ Khi for M in T0]
    unitary_defect = max(float(np.abs(M.conj().T @ M - np.eye(3)).max()) for M in T)
    iL = G.idx[cp.key(cp.W.ML)]; iR = G.idx[cp.key(cp.W.MR)]
    e = next(g for g in range(n_el) if np.allclose(G.els[g], np.eye(G.els[g].shape[0]), atol=1e-9))   # the identity, found, not assumed
    P = []
    for M in T:
        vals, vecs = np.linalg.eig(M)
        fix = [vecs[:, i] for i in range(3) if abs(vals[i] - 1) < 1e-9]
        if fix:
            Q, _ = np.linalg.qr(np.array(fix).T); P.append(Q @ Q.conj().T)
        else:
            P.append(np.zeros((3, 3), complex))
    N = np.zeros(n_el); N[e] = 1.0
    rows = []; supports = {}
    for n in range(1, 41):
        M2 = np.zeros(n_el)
        for g in range(n_el):
            if N[g]:
                M2[G.mult[g][iL]] += N[g]; M2[G.mult[g][iR]] += N[g]
        N = M2
        tot = N.sum(); supp = [g for g in range(n_el) if N[g] > 0]
        unif = np.zeros(n_el); unif[supp] = 1 / len(supp)
        tv = 0.5 * float(np.abs(N / tot - unif).sum())
        Pi = sum(N[g] * P[g] for g in supp) / tot
        tr = float(np.real(np.trace(Pi)))
        dist = float(np.linalg.norm(Pi - (np.trace(Pi) / 3) * np.eye(3)))
        frac_zm = float(sum(N[g] for g in supp if np.real(np.trace(P[g])) > 0.5) / tot)
        rows.append({"n": n, "support_size": len(supp), "tv_from_uniform_on_support": tv, "trace_Pi": round(tr, 9),
                     "distance_from_scalar": dist, "fraction_with_zero_modes": round(frac_zm, 9)})
        supports[n % 2] = supp
    out = {"G_order": n_el, "unitary_defect": unitary_defect, "W1_W2_W4": rows}
    lim = {}
    for par, supp in supports.items():
        Pi = sum(P[g] for g in supp) / len(supp)
        lim["even" if par == 0 else "odd"] = {"support_size": len(supp), "trace": round(float(np.real(np.trace(Pi))), 9),
                                             "distance_from_scalar": float(np.linalg.norm(Pi - (np.trace(Pi) / 3) * np.eye(3))),
                                             "commutes_with_all_of_G": bool(all(np.allclose(Pi @ M, M @ Pi, atol=1e-9) for M in T))}
    out["W3_limit_uniform_on_each_coset"] = lim
    json.dump(out, open(HERE / "weave_word_coupling.json", "w"), indent=1, default=str)
    print(json.dumps({"G": n_el, "W3": lim, "n=12": rows[11], "n=40": rows[39]}, indent=1, default=str))


if __name__ == "__main__":
    main()
