#!/usr/bin/env python3
"""B1620 -- POST-SEAL CHECK UNDER THREE MASS TENSORS (written after the sealed instrument ran and after the SM seat's W39 and
the audit lane's relay of 2026-10-08 were read; disclosed in FINDINGS).  The sealed part A takes the mass term in
T-bar (x) T (B1615's tensor: M commutes with the residual group).  The SM seat's W39 reads, given Lambda, every left-handed
field of a generation in T, so the flavour tensor is T (x) T, and Sym^2 T with E6's cubic and one 27 Higgs; the audit lane
asks that the two be kept explicit.  This script repeats A2 and A3 under all three, uniformly:
  invariance  T-bar(x)T: T(h)^dagger M T(h) = M;   T(x)T: T(h)^T M T(h) = M;   Sym^2 T: the same with M symmetric;
  masses      the singular values of a generic invariant M; a sector is VIABLE when they are three, distinct and non-zero;
  mixing      V = W_u^dagger W_d, W the eigenbasis of M M^dagger (the left-handed rotations; for the two T(x)T tensors the
              physical rotation is its complex conjugate, which leaves every |V_ij| and the rank below unchanged);
  family dim  the rank of the map from the pair's free couplings (real and imaginary parts) to the nine |V_ij|^2 and J;
  data        the block-sum test against the CKM (3 sigma) and the PMNS (3-sigma ranges) data B1612 transcribed (no new
              data is read), then a fit over the family for every pass of dimension below 4.
Writes post_seal_tensors.json."""
import json, pathlib, itertools, collections, importlib.util
import numpy as np
from scipy.optimize import minimize
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ps", HERE / "post_seal_pairs.py")
ps = importlib.util.module_from_spec(spec); spec.loader.exec_module(ps)
G, T, bw = ps.G, ps.T, ps.bw
TENSORS = ("Tbar_x_T", "T_x_T", "Sym2_T")


def invariant_basis(H, tensor):
    if tensor == "Sym2_T":
        E = []
        for i in range(3):
            for j in range(i, 3):
                X = np.zeros((3, 3), complex); X[i, j] = X[j, i] = 1; E.append(X)
    else:
        E = [np.eye(9, dtype=complex)[k].reshape(3, 3) for k in range(9)]
    def reyn(X):
        if tensor == "Tbar_x_T": return sum(T[h].conj().T @ X @ T[h] for h in H) / len(H)
        return sum(T[h].T @ X @ T[h] for h in H) / len(H)
    imgs = np.array([reyn(X).ravel() for X in E])
    u, s, vh = np.linalg.svd(imgs); r = int(sum(s > 1e-9))
    return [vh[k].reshape(3, 3) for k in range(r)]


def mass_matrix(basis, x):
    n = len(basis); c = x[:n] + 1j * x[n:2 * n]
    return sum(ci * B for ci, B in zip(c, basis))


def left_basis(M):
    w, W = np.linalg.eigh(M @ M.conj().T); return W, w


def viable(basis, seed):
    if not basis: return False, []
    rng = np.random.default_rng(seed); out = []
    for _ in range(3):
        M = mass_matrix(basis, rng.normal(size=2 * len(basis)))
        s = np.sort(np.linalg.svd(M, compute_uv=False)); s = s / s[-1]
        out.append(bool(s[0] > 1e-6 and s[1] - s[0] > 1e-6 and s[2] - s[1] > 1e-6))
    return all(out), [round(float(v), 6) for v in s]


def pair_V(bu, bd):
    nu, nd = 2 * len(bu), 2 * len(bd)
    def V(x):
        Wu, _ = left_basis(mass_matrix(bu, x[:nu])); Wd, _ = left_basis(mass_matrix(bd, x[nu:nu + nd]))
        return Wu.conj().T @ Wd
    return V, nu + nd


def family_dim(V, npar, seed):
    rng = np.random.default_rng(seed); best = 0
    for _ in range(3):
        x = rng.normal(size=npar); h = 1e-6
        Jm = np.array([(ps.invariants(V(x + h * e)) - ps.invariants(V(x - h * e))) / (2 * h) for e in np.eye(npar)]).T
        s = np.linalg.svd(Jm, compute_uv=False); best = max(best, int(sum(s > max(1e-5, 1e-6 * s[0]))))
    return best


def blocks(H, V, npar, tensor):
    """block sums on the isotypic pieces (of T, or of its conjugate for the T(x)T tensors -- the same real numbers);
    checked to be shared by the family at two random points"""
    pcs = ps.pieces(H)
    if pcs is None: return None, None
    if tensor != "Tbar_x_T": pcs = [q.conj() for q in pcs]
    return pcs, [q.shape[1] for q in pcs]


def fit(V, npar, which, seed):
    """best fit over the family and the 36 row/column permutations.  A smooth squared objective (L-BFGS-B from several
    starts), then the reported score: the max pull in sigma (CKM) or the max excursion outside the 3-sigma range in units
    of the range's half-width (PMNS); CKM <= 3 and PMNS <= 1 mean reached"""
    rng = np.random.default_rng(seed); best = np.inf
    perms = [(r, c) for r in itertools.permutations(range(3)) for c in itertools.permutations(range(3))]
    half = (ps.PHI - ps.PLO) / 2; mid = (ps.PHI + ps.PLO) / 2
    def resid(x, r, c):
        A = np.abs(V(x))[np.ix_(r, c)]
        if which == "ckm": return (A - ps.CK) / ps.CS
        return np.maximum(np.abs(A - mid) - half, 0) / half
    for r, c in perms:
        for _ in range(3):
            res = minimize(lambda x: float(np.sum(resid(x, r, c) ** 2)), rng.normal(size=npar), method="L-BFGS-B",
                           options={"maxiter": 400})
            best = min(best, float(np.max(np.abs(resid(res.x, r, c)))))
            if best <= (3.0 if which == "ckm" else 1.0): return best
    return best


def main():
    subs = bw.subgroup_lattice()
    out = {}
    for tensor in TENSORS:
        vs = []; prof = collections.Counter()
        for H in subs:
            b = invariant_basis(H, tensor); ok, spec_ = viable(b, len(H) * 31 + min(H) + max(H))
            prof[(len(H), len(b), ok, ps.is_abelian(H))] += 1
            if ok: vs.append((H, b))
        P1 = {"viable_subgroups": len(vs), "viable_orders": sorted({len(H) for H, _ in vs}),
              "viable_all_abelian": all(ps.is_abelian(H) for H, _ in vs),
              "profile_(order,inv_dim,viable,abelian):count": {str(k): v for k, v in sorted(prof.items())}}
        tally = collections.Counter(); ck_low = {}; pm_low = {}; any_full_ck = any_full_pm = False; shared_ok = True
        for (Hu, bu), (Hd, bd) in itertools.product(vs, vs):
            V, npar = pair_V(bu, bd); dim = family_dim(V, npar, len(Hu) * 997 + len(Hd))
            pu, du = blocks(Hu, V, npar, tensor); pd, dd = blocks(Hd, V, npar, tensor)
            # block sums from the family's own V at a random point (projectors' overlap), and their invariance
            rng = np.random.default_rng(len(Hu) + 13 * len(Hd))
            def bsum(x):
                Wu, _ = left_basis(mass_matrix(bu, x[:2 * len(bu)])); Wd, _ = left_basis(mass_matrix(bd, x[2 * len(bu):]))
                A = np.abs(Wu.conj().T @ Wd) ** 2
                # group W's columns by the piece they lie in
                gu = [[i for i in range(3) if np.linalg.norm(q.conj().T @ Wu[:, i]) > 0.5] for q in pu]
                gd = [[j for j in range(3) if np.linalg.norm(q.conj().T @ Wd[:, j]) > 0.5] for q in pd]
                return np.array([[A[np.ix_(a, b)].sum() for b in gd] for a in gu])
            B1, B2 = bsum(rng.normal(size=npar)), bsum(rng.normal(size=npar))
            shared_ok &= bool(B1.shape == (len(du), len(dd)) and np.allclose(B1, B2, atol=1e-8))
            c, p = ps.block_test(B1, du, dd)
            tally[(dim, c, p)] += 1
            key = (dim, tuple(du), tuple(dd), tuple(np.round(B1.ravel(), 5)))
            if c:
                if dim >= 4: any_full_ck = True
                else: ck_low.setdefault(key, (V, npar, [len(Hu), len(Hd)]))
            if p:
                if dim >= 4: any_full_pm = True
                else: pm_low.setdefault(key, (V, npar, [len(Hu), len(Hd)]))
        def run_fits(low, which):
            res = []
            for k, (V, npar, orders) in sorted(low.items(), key=lambda kv: kv[0][0]):
                s = fit(V, npar, which, seed=len(res) + 11)
                res.append({"family_dim": k[0], "piece_dims": [list(k[1]), list(k[2])], "block_sums": list(k[3]),
                            "orders": orders, "best_score": round(float(s), 4),
                            "reached": bool(s <= (3.0 if which == "ckm" else 1.0) + 1e-6)})
            return res
        print(tensor, "viable", len(vs), "pairs done; fits to run: ckm", len(ck_low), "pmns", len(pm_low), flush=True)
        ckf, pmf = run_fits(ck_low, "ckm"), run_fits(pm_low, "pmns")
        def mind(fits, full):
            r = [f["family_dim"] for f in fits if f["reached"]]
            return min(r) if r else (4 if full else None)
        out[tensor] = {"P1": P1, "pairs": sum(tally.values()), "block_sums_shared_by_family": shared_ok,
                       "tally_(family_dim,ckm_block,pmns_block)": {str(k): v for k, v in sorted(tally.items())},
                       "ckm_fits_below_4": ckf, "pmns_fits_below_4": pmf,
                       "ckm_min_family_dim_reaching_data": mind(ckf, any_full_ck),
                       "pmns_min_family_dim_reaching_data": mind(pmf, any_full_pm)}
        print(tensor, json.dumps({k: v for k, v in out[tensor].items() if k not in ("ckm_fits_below_4", "pmns_fits_below_4")}, default=str)[:1500], flush=True)
    json.dump(out, open(HERE / "post_seal_tensors.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
