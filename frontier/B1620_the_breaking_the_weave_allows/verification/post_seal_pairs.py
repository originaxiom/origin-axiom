#!/usr/bin/env python3
"""B1620 -- POST-SEAL CHECK of A2's "abelian image" and A3's data clause (written after the sealed instrument ran; disclosed in
FINDINGS).  The sealed instrument counts each subgroup's basis freedom and caps a pair's mixing freedom at min(4, f1 + f2);
it neither tests abelianness nor reads data.  This script grades the two clauses the sealed text states but the instrument
does not compute:
 P1  for every subgroup H of G: is H abelian, and is T restricted to H a sum of one-dimensional characters?  (A2 says the
     second happens only on abelian images; G is faithful on T, so image and group agree.)
 P2  for every ordered pair (H_u, H_d) of subgroups with three distinct masses: the REAL DIMENSION of the family of mixing
     matrices the pair allows -- the rank of the map from the free unitaries U(m) on each repeated character's piece to the
     physical invariants (the nine |V_ij|^2 and the Jarlskog J) -- and the block sums tr(Pi_a^u Pi_b^d), which every member
     of the family shares.
 P3  against the data B1612 already transcribed (data.json, read there after its own seal; no new data is read here):
     CKM (PDG 2025 global fit, sigma symmetrised) -- a pair passes the NECESSARY test if, for some assignment of the
     generations to the pieces, every block sum lies within 3 sigma of the data's block sum; PMNS (NuFIT 6.0 3-sigma
     moduli ranges) -- every block sum inside the interval [sum lo^2, sum hi^2].  For every pair that passes with a family
     of dimension below 4, a fit over the family (many starts) decides whether the data are actually reached.
 P4  the control: the pairs of dimension 0 must give exactly B1612's six full patterns, none passing either data set.
The neutrino sector is treated like a Dirac sector (left-handed rotations commuting with H): a superset of the Majorana
case, enough for the negative statements.  Writes post_seal_pairs.json."""
import json, pathlib, itertools, collections, importlib.util
import numpy as np
from scipy.optimize import minimize
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bw", HERE / "breaking_the_weave_allows.py")
bw = importlib.util.module_from_spec(spec); spec.loader.exec_module(bw)
G, T0 = bw.G, bw.T
DATA = json.load(open(HERE.parents[1] / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"))
B1612 = json.load(open(HERE.parents[1] / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "mixing_on_the_weave.json"))

# a G-invariant inner product on T: average the standard one, then work in an orthonormal basis for it
K = sum(M.conj().T @ M for M in T0) / len(T0)
w, E = np.linalg.eigh(K); Kh = E @ np.diag(np.sqrt(w)) @ E.conj().T; Khi = np.linalg.inv(Kh)
T = [Kh @ M @ Khi for M in T0]
UNITARY_DEFECT = max(float(np.abs(M.conj().T @ M - np.eye(3)).max()) for M in T)


def is_abelian(H):
    H = list(H)
    return all(G.mult[a][b] == G.mult[b][a] for a in H for b in H)


def pieces(H):
    """isotypic pieces of T restricted to H, as orthonormal bases; None unless every piece is one-dimensional-character"""
    H = sorted(H); rng = np.random.default_rng(len(H) * 7 + H[-1])
    X = sum((rng.normal() + 1j * rng.normal()) * T[h] for h in H)
    _, V = np.linalg.eig(X)
    chars = []
    for i in range(3):
        v = V[:, i] / np.linalg.norm(V[:, i]); chi = np.array([np.vdot(v, T[h] @ v) for h in H])
        if not np.allclose([abs(np.linalg.norm(T[h] @ v - c * v)) for h, c in zip(H, chi)], 0, atol=1e-7):
            return None                                   # v is not a common eigenvector: a higher-dimensional piece
        chars.append(chi)
    distinct = []
    for c in chars:
        if not any(np.allclose(c, d, atol=1e-7) for d in distinct): distinct.append(c)
    out = []
    for c in distinct:
        P = sum(np.conj(ch) * T[h] for h, ch in zip(H, c)) / len(H)
        u, s, _ = np.linalg.svd(P); r = int(round(float(np.real(np.trace(P)))))
        out.append(u[:, :r])
    assert sum(q.shape[1] for q in out) == 3
    return out


def herm_basis(m):
    B = []
    for i in range(m):
        E_ = np.zeros((m, m), complex); E_[i, i] = 1; B.append(E_)
        for j in range(i + 1, m):
            E_ = np.zeros((m, m), complex); E_[i, j] = E_[j, i] = 1; B.append(E_)
            E_ = np.zeros((m, m), complex); E_[i, j] = -1j; E_[j, i] = 1j; B.append(E_)
    return B


def generators(pcs):
    gens = []
    for Q in pcs:
        if Q.shape[1] > 1:
            gens += [Q @ h @ Q.conj().T for h in herm_basis(Q.shape[1])]
    return gens


def expm_h(A):
    w_, E_ = np.linalg.eigh(A); return E_ @ np.diag(np.exp(1j * w_)) @ E_.conj().T


def family(pu, pd):
    Uu0 = np.hstack(pu); Ud0 = np.hstack(pd); gu, gd = generators(pu), generators(pd)
    def V(x):
        Wu = expm_h(sum(t * g for t, g in zip(x[:len(gu)], gu))) if gu else np.eye(3)
        Wd = expm_h(sum(t * g for t, g in zip(x[len(gu):], gd))) if gd else np.eye(3)
        return Uu0.conj().T @ Wu.conj().T @ Wd @ Ud0
    return V, len(gu) + len(gd)


def invariants(M):
    A = np.abs(M) ** 2
    J = np.imag(M[0, 0] * M[1, 1] * np.conj(M[0, 1]) * np.conj(M[1, 0]))
    return np.concatenate([A.ravel(), [J]])


def family_dim(V, npar, seed):
    if npar == 0: return 0
    rng = np.random.default_rng(seed); best = 0
    for _ in range(3):
        x = rng.normal(size=npar); h = 1e-6
        Jm = np.array([(invariants(V(x + h * e)) - invariants(V(x - h * e))) / (2 * h) for e in np.eye(npar)]).T
        s = np.linalg.svd(Jm, compute_uv=False); best = max(best, int(sum(s > max(1e-5, 1e-6 * s[0]))))
    return best


def groupings(dims):
    """assignments of three generations to the pieces: tuples of index lists, one per piece"""
    seen = set(); out = []
    for p in itertools.permutations(range(3)):
        g = []; k = 0
        for d in dims: g.append(tuple(sorted(p[k:k + d]))); k += d
        if tuple(g) not in seen: seen.add(tuple(g)); out.append(g)
    return out


CK = np.array(DATA["ckm_abs"]["value"]); CS = np.array(DATA["ckm_abs"]["sigma"])
PLO = np.array(DATA["pmns_abs_3sigma"]["NO"]["lo"]); PHI = np.array(DATA["pmns_abs_3sigma"]["NO"]["hi"])


def block_test(B, du, dd):
    """returns (ckm_pass, pmns_pass) for the block-sum matrix B under some assignment"""
    ck = pm = False
    for gu in groupings(du):
        for gd in groupings(dd):
            okc = okp = True
            for a, ra in enumerate(gu):
                for b, cb in enumerate(gd):
                    idx = [(i, j) for i in ra for j in cb]
                    S = sum(CK[i, j] ** 2 for i, j in idx); sS = np.sqrt(sum((2 * CK[i, j] * CS[i, j]) ** 2 for i, j in idx))
                    if abs(B[a, b] - S) > 3 * max(sS, 1e-12) + 1e-9: okc = False
                    lo = sum(PLO[i, j] ** 2 for i, j in idx); hi = sum(PHI[i, j] ** 2 for i, j in idx)
                    if not (lo - 1e-9 <= B[a, b] <= hi + 1e-9): okp = False
            ck |= okc; pm |= okp
    return ck, pm


def fit(V, npar, which, seed):
    """best fit over the family and the 36 row/column permutations: max pull (CKM, in sigma) or max excursion outside the
    3-sigma range in units of the range's half-width (PMNS); <= 1 (CKM: <= 3 sigma) means reached"""
    rng = np.random.default_rng(seed); best = np.inf
    perms = [(r, c) for r in itertools.permutations(range(3)) for c in itertools.permutations(range(3))]
    def score(x, r, c):
        A = np.abs(V(x))[np.ix_(r, c)]
        if which == "ckm": return float(np.max(np.abs(A - CK) / CS))
        half = (PHI - PLO) / 2; mid = (PHI + PLO) / 2
        return float(np.max(np.maximum(np.abs(A - mid) - half, 0) / half))
    for r, c in perms:
        for _ in range(6 if npar else 1):
            x0 = rng.normal(size=npar) * 2
            if npar:
                res = minimize(lambda x: score(x, r, c), x0, method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-12})
                best = min(best, res.fun)
            else:
                best = min(best, score(x0, r, c))
    return best


def main():
    subs = bw.subgroup_lattice()
    rows = []; viable = []
    for H in subs:
        pcs = pieces(H); ab = is_abelian(H)
        rows.append({"order": len(H), "abelian": ab, "sum_of_characters": pcs is not None})
        if pcs is not None: viable.append((H, pcs))
    P1 = {"subgroups": len(subs), "unitary_defect_after_averaging": UNITARY_DEFECT,
          "abelian": sum(r["abelian"] for r in rows), "sum_of_characters": sum(r["sum_of_characters"] for r in rows),
          "sum_of_characters_iff_abelian": all(r["abelian"] == r["sum_of_characters"] for r in rows),
          "orders_abelian": sorted({r["order"] for r in rows if r["abelian"]})}
    # P2-P4 over every ordered pair
    tally = collections.Counter(); ck_pass = []; pm_pass = []; fixed_patterns = []
    for (Hu, pu), (Hd, pd) in itertools.product(viable, viable):
        V, npar = family(pu, pd); dim = family_dim(V, npar, len(Hu) * 1000 + len(Hd))
        du = [q.shape[1] for q in pu]; dd = [q.shape[1] for q in pd]
        B = np.array([[float(np.linalg.norm(qu.conj().T @ qd) ** 2) for qd in pd] for qu in pu])
        c, p = block_test(B, du, dd)
        tally[(dim, c, p)] += 1
        if dim == 0:
            P = np.round(np.abs(V(np.zeros(0))) ** 2, 6)
            fixed_patterns.append(P)
        rec = {"orders": [len(Hu), len(Hd)], "piece_dims": [du, dd], "family_dim": dim, "nominal_params": npar}
        if c: ck_pass.append((rec, V, npar))
        if p: pm_pass.append((rec, V, npar))
    # canonical forms of the fixed patterns (sorted rows of sorted columns), for the B1612 control
    def canon(P):
        best = None
        for r in itertools.permutations(range(3)):
            for cc in itertools.permutations(range(3)):
                k = tuple(np.round(P[np.ix_(r, cc)], 4).ravel())
                if best is None or k < best: best = k
        return best
    ours = sorted({canon(P) for P in fixed_patterns})
    theirs = sorted({canon(np.array(p["matrix"])) for p in B1612["M3"]["patterns"]})
    P4 = {"distinct_fixed_patterns": len(ours), "B1612_patterns": len(theirs),
          "fixed_patterns_include_B1612s": set(theirs) <= set(ours), "fixed_patterns": [list(k) for k in ours]}
    # P3 fits for every pass with family dimension below 4 (deduplicated by the pair's invariant fingerprint)
    def fitted(passes, which):
        out = []; seen = set()
        for rec, V, npar in passes:
            if rec["family_dim"] >= 4: continue
            fp = (rec["family_dim"], tuple(np.round(np.sort(np.abs(V(np.zeros(npar))).ravel() ** 2), 4)))
            if fp in seen: continue
            seen.add(fp)
            s = fit(V, npar, which, seed=len(out) + 7)
            out.append({**rec, "best_score": round(s, 4), "reached": bool(s <= (3.0 if which == "ckm" else 1.0) + 1e-6)})
        return out
    ckm_fits = fitted(ck_pass, "ckm"); pmns_fits = fitted(pm_pass, "pmns")
    def min_dim(passes, fits):
        reached_low = [f["family_dim"] for f in fits if f["reached"]]
        full = any(r["family_dim"] >= 4 for r, _, _ in passes)
        return min(reached_low) if reached_low else (4 if full else None)
    P3 = {"pairs": sum(tally.values()),
          "tally_(family_dim,ckm_block_pass,pmns_block_pass)": {str(k): v for k, v in sorted(tally.items())},
          "ckm_block_passes_below_4": [f for f in ckm_fits], "pmns_block_passes_below_4": [f for f in pmns_fits],
          "ckm_min_family_dim_reaching_data": min_dim(ck_pass, ckm_fits),
          "pmns_min_family_dim_reaching_data": min_dim(pm_pass, pmns_fits)}
    out = {"P1": P1, "P3": P3, "P4": P4}
    json.dump(out, open(HERE / "post_seal_pairs.json", "w"), indent=1, default=str)
    print(json.dumps({"P1": P1, "P3": P3, "P4": {k: v for k, v in P4.items() if k != "fixed_patterns"}}, indent=1, default=str))


if __name__ == "__main__":
    main()
