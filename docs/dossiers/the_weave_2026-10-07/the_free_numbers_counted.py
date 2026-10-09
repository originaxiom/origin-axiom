"""W52 (the rule: W52_RULE.md, committed before this script). The count of free numbers in the weave's modular
structure, on the ruled branch, given Lambda, with couplings in tau alone (W50) and tau free (W51).

  C1  the coupling spaces' dimensions d(k) at k = 1, 3, 5, 7, recomputed: T (x) T (D + O+ + O-) and Sym^2 T (D + O+).
  C2  for every weight assignment (k_u, k_d, k_e) in {1, 3, 5, 7}^3 in both frames: P = 2 + sum_s (2 d(k_s) - 1), the
      number of observables that can vary N_var (sectors grouped when they share a one-dimensional space), and the rank
      of the 13 x P Jacobian of the observables at three generic points, against min(P, N_var).
  C3  the geometry's weight (all k = 3) in both frames: the ranks, and Sym^2 T's mixing.
  C4  the smallest P with u and d not grouped, in each frame, and the rank there.

  The observables: the nine log singular values of Y_u, Y_d, Y_e; |V_12|, |V_23|, |V_13| and
  J = Im(V_12 V_23 conj(V_13) conj(V_22)), V = U_u^H U_d from the left singular vectors in increasing order.
  The parameters: tau (two reals); per sector a log scale for the first form's coefficient and a complex coefficient
  for each further form.

  Extra read-outs (no prior): the singular values of the k = 1 and k = 3 forms along x = 0 at y = 1.2, 2, 3; the
  Jacobian's singular-value gap at each assignment.

Run: python3 the_free_numbers_counted.py  ->  the_free_numbers_counted.json beside it.
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_weaves_functionals_on_tau as WF  # noqa: E402  (W51: the vectorised forms)

PG = WF.PG                                   # W50: rho_T in the basis t_p, the coupling pieces
GM, H = PG.GM, PG.H
OUT = HERE / "the_free_numbers_counted.json"
KS = (1, 3, 5, 7)
SECTORS = ("u", "d", "e")
PREDICTED_D = {"T (x) T": {1: 1, 3: 2, 5: 4, 7: 5}, "Sym^2 T": {1: 1, 3: 1, 5: 3, 7: 3}}
FRAMES = {"T (x) T": ("D", "O+", "O-"), "Sym^2 T": ("D", "O+")}


def basis_functions():
    """for each frame and weight: the list of forms, each a function tau -> 3 x 3 matrix in the basis t_p"""
    names, U = GM.units()
    named, _ = H.triplets()
    C = named["T"]
    _, _, xs, ell, lhat, _, _ = GM.M1(C, U)
    Ct = GM.t_basis(C, xs, ell, lhat)
    A, Tm = PG.rho_T(Ct)
    rS9, rT9 = np.kron(A.conj(), A.conj()), np.kron(Tm.conj(), Tm.conj())
    pcs = PG.pieces()
    per_piece = {}
    for name in ("D", "O+", "O-"):
        B = pcs[name]
        rS, rT = B.conj().T @ rS9 @ B, B.conj().T @ rT9 @ B
        for k in KS:
            null, Z, evv, _ = WF.forms_vec(rS, rT, k)
            fs = []
            for i in range(null):
                c = Z[:, i]
                fs.append(lambda t, c=c, evv=evv, B=B: (B @ evv(c, t)[:, 0]).reshape(3, 3))
            per_piece[(name, k)] = fs
    out = {fr: {k: [f for p in pieces for f in per_piece[(p, k)]] for k in KS} for fr, pieces in FRAMES.items()}
    return out, {f"{p} at k = {k}": len(v) for (p, k), v in per_piece.items()}


def observables(params, forms_by_sector):
    tau = params[0] + 1j * params[1]
    pos = 2
    Us, logs = {}, []
    for s in SECTORS:
        fs = forms_by_sector[s]
        Y = np.exp(params[pos]) * fs[0](tau)
        pos += 1
        for f in fs[1:]:
            Y = Y + (params[pos] + 1j * params[pos + 1]) * f(tau)
            pos += 2
        Uy, sv, _ = np.linalg.svd(Y)
        idx = np.argsort(sv)
        Us[s] = Uy[:, idx]
        logs += list(np.log(sv[idx]))
    V = Us["u"].conj().T @ Us["d"]
    J = (V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])).imag
    return np.array(logs + [abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), J])


def n_params(ds):
    return 2 + sum(2 * d - 1 for d in ds)


def n_var(ks, ds):
    groups = []
    for i, (k, d) in enumerate(zip(ks, ds)):
        for g in groups:
            j = g[0]
            if ks[j] == k and ds[j] == 1 and d == 1:
                g.append(i)
                break
        else:
            groups.append([i])
    ud_grouped = any(0 in g and 1 in g for g in groups)
    return 2 * len(groups) + 3 + (0 if ud_grouped else 4), ud_grouped


def jacobian_rank(forms_by_sector, ds, rng, h=1e-6):
    P = n_params(ds)
    tau = complex(rng.uniform(-0.4, 0.4), rng.uniform(1.05, 1.6))
    p0 = [tau.real, tau.imag]
    for d in ds:
        p0 += [rng.normal() * 0.3] + list(rng.normal(size=2 * (d - 1)))
    p0 = np.array(p0)
    Jm = np.zeros((13, P))
    for i in range(P):
        e = np.zeros(P)
        e[i] = h
        Jm[:, i] = (observables(p0 + e, forms_by_sector) - observables(p0 - e, forms_by_sector)) / (2 * h)
    s = np.linalg.svd(Jm, compute_uv=False)
    r = int(sum(s > 1e-6 * s[0]))
    gap = [float(s[r - 1]) if r >= 1 else None, float(s[r]) if r < len(s) else None]
    return r, gap


def scan(forms):
    rows, ok = {}, True
    for f_idx, fr in enumerate(FRAMES):
        for a_idx, ks in enumerate(itertools.product(KS, repeat=3)):
            ds = [len(forms[fr][k]) for k in ks]
            P = n_params(ds)
            nv, ud = n_var(ks, ds)
            pred = min(P, nv)
            rng = np.random.default_rng(5200 + 100 * f_idx + a_idx)
            got = [jacobian_rank({s: forms[fr][k] for s, k in zip(SECTORS, ks)}, ds, rng) for _ in range(3)]
            ranks = [g[0] for g in got]
            key = f"{fr}: {ks}"
            rows[key] = {"d": ds, "P": P, "N_var": nv, "u and d grouped": ud, "predicted rank": pred,
                         "ranks at three points": ranks, "gaps (smallest kept, largest dropped)": [g[1] for g in got]}
            ok &= ranks == [pred] * 3
    return rows, bool(ok)


def extra_profiles(forms):
    out = {}
    for fr in FRAMES:
        for k in (1, 3):
            for i, f in enumerate(forms[fr][k]):
                vals = []
                for y in (1.2, 2.0, 3.0):
                    sv = np.linalg.svd(f(1j * y), compute_uv=False)
                    vals.append([round(float(x / sv[0]), 9) for x in sv])
                out[f"{fr}, k = {k}, form {i}"] = vals
    return out


def main():
    forms, by_piece = basis_functions()
    dims = {fr: {k: len(forms[fr][k]) for k in KS} for fr in FRAMES}
    rows, c2 = scan(forms)
    geo = {fr: rows[f"{fr}: (3, 3, 3)"] for fr in FRAMES}
    sym_forms = {s: forms["Sym^2 T"][3] for s in SECTORS}
    p0 = np.array([0.11, 1.27] + [0.2, -0.1, 0.05])
    o = observables(p0, sym_forms)
    smallest = {}
    for fr in FRAMES:
        cand = [(v["P"], key) for key, v in rows.items() if key.startswith(fr) and not v["u and d grouped"]]
        pmin = min(P for P, _ in cand)
        at = [key for P, key in cand if P == pmin]
        smallest[fr] = {"P": pmin, "assignments": at, "ranks": [rows[a]["ranks at three points"] for a in at]}
    checks = {
        "C1: the coupling spaces' dimensions are d = 1, 2, 4, 5 (T (x) T) and 1, 1, 3, 3 (Sym^2 T)": dims == {
            fr: dict(v) for fr, v in PREDICTED_D.items()},
        "C2: every assignment's Jacobian rank equals min(P, N_var) at all three points (128 assignments)": c2,
        "C3: at k = 3 everywhere, T (x) T has rank 11 and Sym^2 T rank 5 with |V_12| = |V_23| = |V_13| = 0": bool(
            geo["T (x) T"]["ranks at three points"] == [11, 11, 11]
            and geo["Sym^2 T"]["ranks at three points"] == [5, 5, 5] and max(abs(o[9]), abs(o[10]), abs(o[11])) < 1e-12),
        "C4: the smallest P with u and d not grouped is 7 (T (x) T) and 5 (Sym^2 T), with rank P there": bool(
            smallest["T (x) T"]["P"] == 7
            and sorted(smallest["T (x) T"]["assignments"]) == ["T (x) T: (1, 3, 1)", "T (x) T: (3, 1, 1)"]
            and smallest["Sym^2 T"]["P"] == 5 and len(smallest["Sym^2 T"]["assignments"]) == 4
            and all(r == [smallest[fr]["P"]] * 3 for fr in FRAMES for r in smallest[fr]["ranks"])),
    }
    out = {"status": "W52: the free numbers counted in the weave's modular structure (the rule first)",
           "C1: the dimensions by frame and weight": {fr: {str(k): v for k, v in d.items()} for fr, d in dims.items()},
           "C1: by piece": by_piece,
           "C2: the scan": rows,
           "C3: the geometry's weight (all k = 3)": geo,
           "C3: Sym^2 T's mixing at a sample point (|V_12|, |V_23|, |V_13|, J)": [float(x) for x in o[9:]],
           "C4: the smallest structures with u and d not grouped": smallest,
           "extra read-outs (not predicted)": {"singular values over the largest along x = 0 at y = 1.2, 2, 3":
                                               extra_profiles(forms)},
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
