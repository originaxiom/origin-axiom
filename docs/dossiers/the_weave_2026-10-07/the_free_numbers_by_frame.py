"""W44 (the rule: W44_RULE.md, committed before this script). The free-number count in every frame on record, with a
strict fit predicate.

  F_all  B1620's frame: every element c(g) S(g) of the weave's group G is flavour; the residuals are G's subgroups.
  F_c    W43's frame: c is gauge; the residuals are the subgroups of B3 = {+-1} x O acting on T by +-S.
  (F_S, W24's frame, where every S(g) is gauge, is by hand: the flavour group acts by scalars and constrains nothing.)

For each frame and tensor, every ordered pair of viable residuals (exact viability, W42), one representative per orbit
of simultaneous conjugation:
  - the block sums tr(P_a P_b) of the residuals' isotypic projectors (fixed on the family), and B1620's necessary block
    test against B1612's data (received/B1612_data.json, verbatim);
  - the family dimension, the most common rank over five points of the map to the nine |U_ij|^2 and J;
  - for every orbit of dimension below 4 passing a block test, a fit over the family with the 36 row and column
    permutations: CKM reached when every |V_ij| is within 3 sigma; PMNS reached when every |U_ij| lies inside NuFIT's
    3-sigma range to 1e-6 (the strict predicate); every witness kept;
  - at dimension 4, a constructive witness: a unitary in the standard parametrisation fitted to the data, which the pair
    of trivial residuals realises (its family is all of U(3) on both sides).
D3 regrades B1620's stored PMNS families below four dimensions (received/B1620_post_seal_tensors.json) by matching
orders, piece dimensions and block sums.

Run: python3 the_free_numbers_by_frame.py  ->  the_free_numbers_by_frame.json beside it.
"""
import itertools
import json
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_breaking_verified as BV  # noqa: E402  (W42: the group, exact viability)
import the_trimaximal_families as TF  # noqa: E402  (W43: the lattice, the families, the TM columns)

OUT = HERE / "the_free_numbers_by_frame.json"
DATA = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))
B1620 = json.loads((HERE / "received" / "B1620_post_seal_tensors.json").read_text(encoding="utf-8"))
CK = np.array(DATA["ckm_abs"]["value"])
CS = np.array(DATA["ckm_abs"]["sigma"])
PLO = np.array(DATA["pmns_abs_3sigma"]["NO"]["lo"])
PHI = np.array(DATA["pmns_abs_3sigma"]["NO"]["hi"])
TENSORS = BV.TENSORS
PERMS = [(list(r), list(c)) for r in itertools.permutations(range(3)) for c in itertools.permutations(range(3))]
ROWS = np.array([list(r) for r in itertools.permutations(range(3))])
RI, CI = ROWS[:, None, :, None], ROWS[None, :, None, :]                  # all 36 permuted copies at once: A[RI, CI]


def num(x):
    return np.exp(2j * np.pi * x[0] / 24) * np.array(x[1], dtype=complex)


def pieces(H, seed):
    """the isotypic projectors of an abelian residual on T: the eigenspaces of a generic combination of its elements"""
    rng = np.random.default_rng(seed)
    X = sum((rng.normal() + 1j * rng.normal()) * num(h) for h in H)
    w, V = np.linalg.eig(X)
    groups = []
    for i, z in enumerate(w):
        for g in groups:
            if abs(g[0] - z) < 1e-7:
                g[1].append(i)
                break
        else:
            groups.append([z, [i]])
    P = []
    for _, idx in groups:
        Q, _ = np.linalg.qr(V[:, idx])
        Q = Q[:, :len(idx)]
        P.append(Q @ Q.conj().T)
    assert np.allclose(sum(P), np.eye(3), atol=1e-9)
    assert all(np.allclose(num(h) @ p, p @ num(h), atol=1e-9) for h in H for p in P)
    return P


def groupings(dims):
    seen, out = set(), []
    for p in itertools.permutations(range(3)):
        g, k = [], 0
        for d in dims:
            g.append(tuple(sorted(p[k:k + d])))
            k += d
        if tuple(g) not in seen:
            seen.add(tuple(g))
            out.append(g)
    return out


def block_test(S, du, dd):
    """B1620's necessary test: for some assignment of the generations to the pieces, every block sum agrees with the
    data's (CKM within 3 sigma, sigma propagated linearly; PMNS between the sums of lo^2 and hi^2)"""
    ck = pm = False
    for gu in groupings(du):
        for gd in groupings(dd):
            okc = okp = True
            for a, ra in enumerate(gu):
                for b, cb in enumerate(gd):
                    idx = [(i, j) for i in ra for j in cb]
                    s = sum(CK[i, j] ** 2 for i, j in idx)
                    ss = np.sqrt(sum((2 * CK[i, j] * CS[i, j]) ** 2 for i, j in idx))
                    if abs(S[a, b] - s) > 3 * max(ss, 1e-12) + 1e-9:
                        okc = False
                    lo, hi = sum(PLO[i, j] ** 2 for i, j in idx), sum(PHI[i, j] ** 2 for i, j in idx)
                    if not lo - 1e-9 <= S[a, b] <= hi + 1e-9:
                        okp = False
            ck |= okc
            pm |= okp
    return ck, pm


def family_dim_mode(Bu, Bd, rng, npts=5):
    nl, nn = 2 * len(Bu), 2 * len(Bd)

    def V(x):
        return TF.left(TF.member(Bu, x[:nl])).conj().T @ TF.left(TF.member(Bd, x[nl:]))

    ranks = []
    for _ in range(npts):
        x = rng.normal(size=nl + nn)
        h = 1e-6
        Jm = np.array([(TF.invariants(V(x + h * e)) - TF.invariants(V(x - h * e))) / (2 * h) for e in np.eye(nl + nn)]).T
        s = np.linalg.svd(Jm, compute_uv=False)
        ranks.append(int(sum(s > max(1e-5, 1e-6 * s[0]))))
    top = Counter(ranks).most_common()
    tie = len(top) > 1 and top[0][1] == top[1][1]
    mode = min(r for r, c in top if c == top[0][1])
    return mode, ranks, tie


def score(B, which):
    if which == "pmns":
        return float(np.max(np.maximum(np.maximum(PLO - B, B - PHI), 0)))
    return float(np.max(np.abs(B - CK) / CS))


def reached(s, which):
    return s <= (1e-6 if which == "pmns" else 3.0)


def objective(B, which):
    if which == "pmns":
        return float(np.sum(np.maximum(PLO - B, 0) ** 2 + np.maximum(B - PHI, 0) ** 2))
    return float(np.sum(((B - CK) / CS) ** 2))


def fit(Bu, Bd, which, rng, starts=8, maxiter=800):
    nu, nd = 2 * len(Bu), 2 * len(Bd)

    def A_of(x):
        return np.abs(TF.left(TF.member(Bu, x[:nu])).conj().T @ TF.left(TF.member(Bd, x[nu:])))

    def f(x):
        B = A_of(x)[RI, CI]
        if which == "pmns":
            v = np.sum(np.maximum(PLO - B, 0) ** 2 + np.maximum(B - PHI, 0) ** 2, axis=(2, 3))
        else:
            v = np.sum(((B - CK) / CS) ** 2, axis=(2, 3))
        return float(v.min())

    best = None
    for _ in range(starts):
        res = minimize(f, rng.normal(size=nu + nd), method="L-BFGS-B", options={"maxiter": maxiter})
        A = A_of(res.x)
        r, c = min(PERMS, key=lambda rc: objective(A[np.ix_(rc[0], rc[1])], which))
        B = A[np.ix_(r, c)]
        s = score(B, which)
        if best is None or s < best["score"]:
            best = {"score": s, "reached": reached(s, which), "rows": r, "columns": c,
                    "|U| at the witness": np.round(B, 6).tolist(), "parameters": np.round(res.x, 10).tolist()}
        if best["reached"]:
            break
    return best


def standard(t12, t13, t23, d):
    s12, c12, s13, c13, s23, c23 = np.sin(t12), np.cos(t12), np.sin(t13), np.cos(t13), np.sin(t23), np.cos(t23)
    e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def standard_witness(which, rng):
    best = None
    for _ in range(40):
        res = minimize(lambda p: objective(np.abs(standard(*p)), which), rng.uniform(0, 1.6, size=4) * [1, 0.2, 1, 4],
                       method="L-BFGS-B")
        B = np.abs(standard(*res.x))
        s = score(B, which)
        if best is None or s < best["score"]:
            best = {"score": s, "reached": reached(s, which), "angles and phase": np.round(res.x, 10).tolist(),
                    "|U| at the witness": np.round(B, 6).tolist()}
        if best["reached"]:
            break
    return best


def frame_census(G, subs, tensor, seed):
    idx = {x: i for i, x in enumerate(G)}
    inv = {x: next(y for y in G if BV.emul(x, y) == TF.IDENT) for x in G}
    keys = [frozenset(H) for H in subs]
    where = {k: i for i, k in enumerate(keys)}
    conj = [[where[frozenset(BV.emul(BV.emul(x, h), inv[x]) for h in H)] for x in G] for H in subs]
    rng_exact = random.Random(seed)
    rng = np.random.default_rng(seed)
    viable = {}
    for i, H in enumerate(subs):
        basis = BV.fixed_basis(H, tensor)
        if BV.viable_exact(basis, tensor, rng_exact) > 0:
            viable[i] = (TF.numeric_basis(basis, tensor), pieces(H, seed + i))
    orbits = {}
    for i, j in itertools.product(viable, viable):
        rep = min((conj[i][x], conj[j][x]) for x in range(len(G)))
        orbits.setdefault(rep, []).append((i, j))
    tally, low = Counter(), {"pmns": [], "ckm": []}
    smallest_block = {"pmns": None, "ckm": None}
    for (i, j), members in sorted(orbits.items()):
        Bu, Pu = viable[i]
        Bd, Pd = viable[j]
        S = np.array([[float(np.real(np.trace(a @ b))) for b in Pd] for a in Pu])
        du, dd = [int(round(np.real(np.trace(p)))) for p in Pu], [int(round(np.real(np.trace(p)))) for p in Pd]
        ck, pm = block_test(S, du, dd)
        if not (ck or pm):
            tally[("not computed", False, False)] += len(members)
            continue
        dim, ranks, tie = family_dim_mode(Bu, Bd, rng)
        tally[(dim, ck, pm)] += len(members)
        for which, ok in (("pmns", pm), ("ckm", ck)):
            if ok and (smallest_block[which] is None or dim < smallest_block[which]):
                smallest_block[which] = dim
            if ok and dim < 4:
                f = fit(Bu, Bd, which, rng)
                cols = sorted(TF.fixed_columns(Bu, Bd, rng)) if which == "pmns" else []
                low[which].append({"orders": [len(subs[i]), len(subs[j])], "pairs in the orbit": len(members),
                                   "piece dimensions": [du, dd], "block sums": np.round(S, 6).tolist(),
                                   "family dimension": dim, "ranks at five points": ranks, "rank tie": tie,
                                   "fixed trimaximal columns": cols, "fit": f})
    out = {"viable residuals": len(viable), "ordered pairs": len(viable) ** 2, "orbits": len(orbits),
           "pairs by (dimension, CKM block test, PMNS block test); dimension computed only when a block test passes":
               {str(k): v for k, v in sorted(tally.items(), key=lambda kv: str(kv[0]))}}
    for which in ("pmns", "ckm"):
        hits = sorted(r["family dimension"] for r in low[which] if r["fit"]["reached"])
        out[which.upper() + ": the smallest dimension passing the block test"] = smallest_block[which]
        out[which.upper() + ": the smallest dimension below 4 with a witness"] = hits[0] if hits else None
        out[which.upper() + ": orbits below 4 passing the block test, fitted"] = low[which]
    return out


def regrade(F_all):
    """B1620's stored PMNS families below four dimensions, matched to this run's orbits by orders, piece dimensions and
    block sums (as multisets of (piece dimension pair, block sum))"""
    def canon(du, dd, S):
        return tuple(sorted((du[a], dd[b], round(float(S[a][b]), 4)) for a in range(len(du)) for b in range(len(dd))))
    rows = []
    for t, key in (("T-bar (x) T", "Tbar_x_T"), ("T (x) T", "T_x_T"), ("Sym^2 T", "Sym2_T")):
        mine = F_all[t]["PMNS: orbits below 4 passing the block test, fitted"]
        for e in B1620[key]["pmns_fits_below_4"]:
            dl, dn = e["piece_dims"]
            S = np.array(e["block_sums"]).reshape(len(dl), len(dn))
            c = canon(dl, dn, S)
            match = [m for m in mine if m["orders"] == e["orders"]
                     and canon(m["piece dimensions"][0], m["piece dimensions"][1], m["block sums"]) == c]
            rows.append({"tensor": t, "orders": e["orders"], "family_dim": e["family_dim"], "piece_dims": e["piece_dims"],
                         "B1620's score": e["best_score"], "B1620 reached": e["reached"],
                         "matching orbits here": len(match),
                         "family dimensions here": [m["family dimension"] for m in match],
                         "reached here (strict)": [m["fit"]["reached"] for m in match],
                         "best excess here": [round(m["fit"]["score"], 6) for m in match]})
    return rows


def main():
    G, _, _, _ = BV.the_group_exact()
    subs_all, _ = TF.lattice(G)
    B3 = sorted((k, S) for S in BV.rotations() for k in (0, 12))
    subs_c, _ = TF.lattice(B3)
    F_all = {t: frame_census(G, subs_all, t, 401 + i) for i, t in enumerate(TENSORS)}
    F_c = {t: frame_census(B3, subs_c, t, 501 + i) for i, t in enumerate(TENSORS)}
    rng = np.random.default_rng(601)
    witness4 = {"CKM": standard_witness("ckm", rng), "PMNS": standard_witness("pmns", rng)}
    D3 = regrade(F_all)

    def nz(v):
        return 4 if v is None else v

    def minima(F):
        out = {}
        for t in TENSORS:
            p = F[t]["PMNS: the smallest dimension below 4 with a witness"]
            c = F[t]["CKM: the smallest dimension below 4 with a witness"]
            out[t] = {"PMNS": p if p is not None else (4 if witness4["PMNS"]["reached"] else None),
                      "CKM": c if c is not None else (4 if witness4["CKM"]["reached"] else None),
                      "PMNS: below it, every orbit fails the block test":
                          nz(F[t]["PMNS: the smallest dimension passing the block test"]) >= nz(p),
                      "CKM: below it, every orbit fails the block test":
                          nz(F[t]["CKM: the smallest dimension passing the block test"]) >= nz(c)}
        return out

    m_all, m_c = minima(F_all), minima(F_c)

    def tm_types(F, t):
        return sorted({c for r in F[t]["PMNS: orbits below 4 passing the block test, fitted"]
                       if r["family dimension"] == 2 and r["fit"]["reached"] for c in r["fixed trimaximal columns"]})

    expected = {"T-bar (x) T": {"PMNS": 2, "CKM": 4}, "T (x) T": {"PMNS": 2, "CKM": 4}, "Sym^2 T": {"PMNS": 4, "CKM": 4}}
    checks = {
        "D1: F_all, the minima are PMNS 2 / 2 / 4 and CKM 4 / 4 / 4": all(
            m_all[t]["PMNS"] == expected[t]["PMNS"] and m_all[t]["CKM"] == expected[t]["CKM"] for t in TENSORS),
        "D1: F_all, below the minima every orbit fails the block test": all(
            m_all[t]["PMNS: below it, every orbit fails the block test"]
            and m_all[t]["CKM: below it, every orbit fails the block test"] for t in TENSORS),
        "D1: F_all, the dimension-2 PMNS witnesses carry TM1 under T-bar (x) T and only TM2 under T (x) T": (
            "TM1" in tm_types(F_all, "T-bar (x) T") and tm_types(F_all, "T (x) T") == ["TM2"]),
        "D2: F_c, the same minima": all(
            m_c[t]["PMNS"] == expected[t]["PMNS"] and m_c[t]["CKM"] == expected[t]["CKM"] for t in TENSORS),
        "D2: F_c, below the minima every orbit fails the block test": all(
            m_c[t]["PMNS: below it, every orbit fails the block test"]
            and m_c[t]["CKM: below it, every orbit fails the block test"] for t in TENSORS),
        "D3: B1620's TM-type families (score 0) stay reached under the strict predicate": all(
            all(r["reached here (strict)"]) and r["matching orbits here"] > 0
            for r in D3 if r["B1620's score"] == 0.0 and r["family_dim"] == 2),
        "the dimension-4 witnesses exist (CKM and PMNS, standard parametrisation)": bool(
            witness4["CKM"]["reached"] and witness4["PMNS"]["reached"]),
    }
    checks = {k: bool(v) for k, v in checks.items()}
    out = {"status": "W44: the free-number count in every frame on record (the rule first; B1612's data verbatim; "
                     "B1620's stored fits read first)",
           "the minima, F_all": m_all, "the minima, F_c": m_c,
           "TM types of the dimension-2 PMNS witnesses": {"F_all": {t: tm_types(F_all, t) for t in TENSORS},
                                                         "F_c": {t: tm_types(F_c, t) for t in TENSORS}},
           "the dimension-4 witnesses (realised by the pair of trivial residuals)": witness4,
           "F_all": F_all, "F_c": F_c, "D3: B1620's PMNS families below four dimensions, regraded strictly": D3,
           "checks": checks, "every check holds": all(checks.values())}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"minima F_all": m_all, "minima F_c": m_c, "checks": checks}, indent=1))
    print("every check holds:", all(checks.values()))


if __name__ == "__main__":
    main()
