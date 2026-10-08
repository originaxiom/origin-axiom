#!/usr/bin/env python3
"""B1621 -- THE PRINCIPLE'S CLOCK AND TICK ON THE MATTER.  B1620 found that with couplings in tau alone the residual always
contains the inner automorphisms (the parity grading K), so every mixing matrix is a permutation, and the observed mixing
needs something that breaks the grading.  The principle supplies two forced data outside the weave (B1620 part B, B1083):
the CLOCK -- the parity class of the fixed-point word's prefix, (A_n, B_n) mod 2 -- and the TICK -- sigma^2 = LR, the rule's
double step.  This arc asks what each does to the weave's triplet T, and what their invariant means give under the three
mass tensors.  Exact up to floating point; no data is read except B1612's transcription in P2.
 K1  the clock acts within the grading: the lifts of conjugation by a and by b are diagonal in T's parity basis with the
     lines' characters as entries, they commute, and the product along every prefix of the word up to N1 equals
     diag(chi_p(A_n, B_n)) (up to one overall sign, recorded).
 K2  the span of the clock's matrices along the word is the diagonal algebra (dimension 3): every clock-reading coupling,
     under every tensor, is diagonal in the parity lines.
 K3  the clock's invariant mean on T: (1/N) sum_n diag(chi_p(c_n)) to N = F_30; its largest entry.
 T1  the tick: T(LR)'s eigenvalues on T (as turns), its action on the parity lines (a cyclic permutation or not), and the
     moduli squared of its eigenvectors in the parity basis.
 T2  the tick's operator mean (1/3) sum_{k<3} T(LR)^k (T(LR) has order 3 on T): its rank, the moduli of its entries in the
     parity basis, and whether it commutes with the clock (the grading).
 T3  the tick's means acting on the clock's forms D (generic diagonal), under each tensor: T-bar(x)T by conjugation
     (1/3) sum T^-k D T^k; T(x)T and Sym^2 T by (1/3) sum (T^k)^T D T^k: the singular values (degenerate or zero?).
 P1  mixing at leading order: two sectors both reading the tick by its operator mean (the heavy lines aligned: |V_33| = 1);
     a tick sector against a clock sector (the heavy line's overlaps with the parity lines).
 P2  against B1612's transcription (no new data): the tick-against-clock overlap row/column (1/3, 1/3, 1/3) placed on the
     sole heaviest state -- the tau row (charged leptons reading the tick) or the nu_3 column (neutrinos reading the tick,
     normal ordering; an inverted ordering has two heavy states, which a rank-one mean cannot give) -- inside NuFIT 6.0's
     3-sigma |U| ranges?  And the quark case: |V_tb| = 1 at leading order against PDG's |V_tb|.
Writes clock_and_tick.json."""
import json, pathlib, os, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("om", FRONTIER / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
om = importlib.util.module_from_spec(spec); spec.loader.exec_module(om)
cp = om.cp
DATA = json.load(open(FRONTIER / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"))


def T_of(auto): return cp.restrict(om.M_of(auto), cp.TB)


def fib_word(N):
    w = "a"
    while len(w) < N: w = "".join("ab" if ch == "a" else "a" for ch in w)
    return w[:N]


def main():
    out = {}
    L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}
    Ta, Tb = T_of({"a": "a", "b": "abA"}), T_of({"a": "baB", "b": "b"})
    TLR = T_of(om.compose(L, R))
    # the parity basis: the joint eigenbasis of the two commuting inner lifts (B1618's construction), orthonormalised
    _, P = np.linalg.eig(Ta + 0.3719 * Tb); P, _ = np.linalg.qr(P)
    Pa, Pb = P.conj().T @ Ta @ P, P.conj().T @ Tb @ P
    chars = [(complex(Pa[i, i]), complex(Pb[i, i])) for i in range(3)]
    diag_ok = bool(np.allclose(Pa, np.diag(np.diag(Pa)), atol=1e-9) and np.allclose(Pb, np.diag(np.diag(Pb)), atol=1e-9))
    commute = bool(np.allclose(Ta @ Tb, Tb @ Ta, atol=1e-9))
    # K1 along the word: the product of the letters' inner lifts against diag(chi_p(class))
    N1 = 121393                                                        # F_26
    w = fib_word(N1); cur = np.eye(3, dtype=complex); worst = 0.0; sign_seen = set()
    da, db = np.diag(Pa), np.diag(Pb); A = B = 0
    span = []
    for n, ch in enumerate(w, 1):
        cur = cur @ (Pa if ch == "a" else Pb)
        if ch == "a": A += 1
        else: B += 1
        target = np.diag(da ** A * db ** B)
        worst = max(worst, float(np.abs(cur - target).max()))
        if n <= 64: span.append(cur.ravel())
    out["K1"] = {"inner_lifts_diagonal_in_parity_basis": diag_ok, "inner_lifts_commute": commute,
                 "line_characters_(a,b)": [[round(x.real, 6), round(y.real, 6)] for x, y in chars],
                 "characters_real_signs": all(abs(x.imag) < 1e-9 and abs(y.imag) < 1e-9 and abs(abs(x) - 1) < 1e-9 for x, y in chars),
                 "prefix_product_equals_diag_chi_to_N1": bool(worst < 1e-8), "N1": N1, "worst_deviation": worst}
    S = np.array(span); rank = int(np.linalg.matrix_rank(S, tol=1e-8))
    offdiag = float(max(np.abs(np.array(span).reshape(-1, 3, 3) * (1 - np.eye(3))).max(), 0.0))
    out["K2"] = {"span_dimension": rank, "max_offdiagonal_entry": offdiag, "span_is_the_diagonal_algebra": bool(rank == 3 and offdiag < 1e-9)}
    # K3: the clock's mean to F_30
    N3 = 1346269
    arr = np.frombuffer(fib_word(N3).encode(), dtype=np.uint8) == ord("a")
    Ac = np.cumsum(arr); Bc = np.cumsum(~arr)
    means = []
    for i in range(3):
        sa = 1 if round(chars[i][0].real) == 1 else -1; sb = 1 if round(chars[i][1].real) == 1 else -1
        vals = np.where(Ac % 2 == 1, sa, 1) * np.where(Bc % 2 == 1, sb, 1)
        means.append(float(np.mean(vals)))
    out["K3"] = {"N": N3, "mean_of_each_line_character": means, "max_abs_mean": max(abs(m) for m in means)}
    # T1: the tick
    PL = P.conj().T @ TLR @ P
    ev, V = np.linalg.eig(PL); V = V / np.linalg.norm(V, axis=0)
    perm = [int(np.argmax(np.abs(PL[:, i]))) for i in range(3)]
    is_monomial = all(np.sum(np.abs(PL[:, i]) > 1e-9) == 1 for i in range(3))
    out["T1"] = {"eigen_turns": sorted(round(float(np.angle(e) / (2 * np.pi)) % 1, 6) for e in ev),
                 "unitary": bool(np.allclose(PL.conj().T @ PL, np.eye(3), atol=1e-9)),
                 "monomial_in_parity_basis": bool(is_monomial), "line_images": perm,
                 "cyclic": bool(is_monomial and sorted(perm) == [0, 1, 2] and all(perm[i] != i for i in range(3))),
                 "eigvec_moduli_sq_in_parity_basis": np.round(np.abs(V) ** 2, 6).tolist(),
                 "order_on_T": int(next(k for k in range(1, 25) if np.allclose(np.linalg.matrix_power(PL, k), np.eye(3), atol=1e-9)))}
    # T2: the tick's operator mean
    k3 = out["T1"]["order_on_T"]
    Mbar = sum(np.linalg.matrix_power(PL, k) for k in range(k3)) / k3
    sv = np.linalg.svd(Mbar, compute_uv=False)
    out["T2"] = {"rank": int(sum(sv > 1e-9)), "singular_values": [round(float(x), 9) for x in sv],
                 "entry_moduli_in_parity_basis": np.round(np.abs(Mbar), 6).tolist(),
                 "commutes_with_the_clock": bool(np.allclose(Mbar @ Pa, Pa @ Mbar, atol=1e-9) and np.allclose(Mbar @ Pb, Pb @ Mbar, atol=1e-9))}
    # T3: the tick's means acting on the clock's forms, under each tensor
    rng = np.random.default_rng(1621); res = {}
    for name in ("Tbar_x_T", "T_x_T", "Sym2_T"):
        spectra = []
        for _ in range(5):
            D = np.diag(rng.normal(size=3) + 1j * rng.normal(size=3))
            if name == "Tbar_x_T":
                Rm = sum(np.linalg.matrix_power(PL, -k) @ D @ np.linalg.matrix_power(PL, k) for k in range(k3)) / k3
            else:
                Rm = sum(np.linalg.matrix_power(PL, k).T @ D @ np.linalg.matrix_power(PL, k) for k in range(k3)) / k3
            s = np.sort(np.linalg.svd(Rm, compute_uv=False)); spectra.append(s)
        degenerate_or_zero = all(s[-1] < 1e-9 or (abs(s[0] - s[1]) < 1e-9 * s[-1] or abs(s[1] - s[2]) < 1e-9 * s[-1]) for s in spectra)
        res[name] = {"normalised_spectra": [[round(float(x / max(s[-1], 1e-300)), 6) for x in s] for s in spectra],
                     "max_singular_value": float(max(s[-1] for s in spectra)), "degenerate_or_zero": bool(degenerate_or_zero)}
    out["T3"] = res
    # P1: leading-order mixing
    heavy = np.linalg.svd(Mbar)[0][:, 0]                                # the tick mean's heavy line, in the parity basis
    out["P1"] = {"tick_tick_heavy_overlap": round(float(abs(np.vdot(heavy, heavy)) ** 2), 9),
                 "tick_clock_heavy_row": [round(float(abs(heavy[i]) ** 2), 6) for i in range(3)]}
    # P2: against B1612's transcription
    lo = np.array(DATA["pmns_abs_3sigma"]["NO"]["lo"]); hi = np.array(DATA["pmns_abs_3sigma"]["NO"]["hi"])
    tri = np.sqrt(np.array(out["P1"]["tick_clock_heavy_row"]))
    inside = lambda vals, l, h: bool(all(l[i] - 1e-12 <= vals[i] <= h[i] + 1e-12 for i in range(3)))
    tau_row = any(inside(np.array(p), lo[2], hi[2]) for p in __import__("itertools").permutations(tri))
    nu3_col = any(inside(np.array(p), lo[:, 2], hi[:, 2]) for p in __import__("itertools").permutations(tri))
    rows_cols = {f"row_{r}": any(inside(np.array(p), lo[i], hi[i]) for p in __import__("itertools").permutations(tri)) for i, r in enumerate("e mu tau".split())}
    rows_cols.update({f"col_{c}": any(inside(np.array(p), lo[:, j], hi[:, j]) for p in __import__("itertools").permutations(tri)) for j, c in enumerate(("1", "2", "3"))})
    ck = np.array(DATA["ckm_abs"]["value"]); cs = np.array(DATA["ckm_abs"]["sigma"])
    out["P2"] = {"tau_row_trimaximal_inside_3sigma": tau_row, "nu3_column_trimaximal_inside_3sigma": nu3_col,
                 "every_row_and_column": rows_cols,
                 "Vtb_data": float(ck[2, 2]), "Vtb_sigma": float(cs[2, 2]),
                 "Vtb_leading_order_pull_sigma": round(float((1 - ck[2, 2]) / cs[2, 2]), 2)}
    json.dump(out, open(HERE / "clock_and_tick.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
