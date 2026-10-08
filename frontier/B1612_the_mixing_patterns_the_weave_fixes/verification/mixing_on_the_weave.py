#!/usr/bin/env python3
"""B1612 -- THE MIXING PATTERNS THE WEAVE FIXES.  Lam's rule (2008): a sector whose mass matrix (M M-dagger) keeps an
abelian subgroup H of the flavour group, with one-dimensional joint eigenspaces on the triplet, is diagonal in H's joint
eigenbasis U_H (up to phases and order); two sectors mix by |U_H1-dagger U_H2|^2.  On the weave the flavour group on the
matter triplet T is the image of G (the lifts of L and R on W10's V, order 96; B1611's module) -- the swap is not in it
(B1610, B1611: on the chiral double-tick weave the swap is not a move).  Exact up to floating point (1e-9):
 M1  G's image on T: order, faithfulness, the elements' projective eigenvalue structure.
 M2  the basis-fixing abelian subgroups: cyclic ones (one element, three distinct eigenvalues) and two-generated ones
     (two commuting elements, one-dimensional joint eigenspaces); their distinct eigenbases.
 M3  the FULLY FIXED patterns |U_H1-dagger U_H2|^2 over all pairs of distinct bases, up to row and column permutations
     (36): the set, each with a count and a witness (the shortest words in L, R of the generators); named where they
     equal a classical pattern (identity, democratic, tri-bimaximal TBM, bimaximal BM).
 M4  the ONE-COLUMN patterns: a full basis against an element with exactly one non-degenerate eigenline (a residual
     involution-type symmetry fixing one column, the TM1/TM2 families): the set of fixed columns |U_H-dagger v|^2.
 M5  the look-elsewhere count: the number of distinct full patterns times 36 permutations, and of one-column patterns
     times 3 x 3 placements.
No data is read by this instrument.  Writes mixing_on_the_weave.json."""
import json, pathlib, sys, os, importlib.util, itertools, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("cp", FRONTIER / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
G = cp.Group([cp.W.ML, cp.W.MR]); TB = cp.TB
GT = [cp.restrict(M, TB) for M in G.els]


def words_for_elements():
    """the shortest word in L, R (letters 'L', 'R', inverses 'l', 'r') for each element of G"""
    gens = {"L": cp.W.ML, "R": cp.W.MR, "l": np.linalg.inv(cp.W.ML), "r": np.linalg.inv(cp.W.MR)}
    word = {0: ""}; frontier = [0]
    while frontier:
        nxt = []
        for i in frontier:
            for s, M in gens.items():
                j = G.idx[cp.key(G.els[i] @ M)]
                if j not in word: word[j] = word[i] + s; nxt.append(j)
        frontier = nxt
    return word


WORD = words_for_elements()


def eig_lines(A, tol=1e-7):
    """eigenvalues of A grouped (A unitary): list of (eigenvalue, basis of its eigenspace)"""
    ev, V = np.linalg.eig(A); groups = []
    for e, v in zip(ev, V.T):
        for g in groups:
            if abs(g[0] - e) < tol: g[1].append(v); break
        else:
            groups.append([e, [v]])
    return [(e, np.linalg.qr(np.array(vs).T)[0]) for e, vs in groups]


def joint_basis(mats):
    """joint eigenbasis of commuting unitaries if every joint eigenspace is one-dimensional, else None"""
    spaces = [np.eye(3, dtype=complex)]
    for A in mats:
        new = []
        for S in spaces:
            if S.shape[1] == 1: new.append(S); continue
            B = S.conj().T @ A @ S
            for e, W in eig_lines(B): new.append(S @ W)
        spaces = new
    return np.hstack(spaces) if all(S.shape[1] == 1 for S in spaces) and len(spaces) == 3 else None


def basis_key(U):
    """an order- and phase-free key of a basis: the sorted rounded projectors"""
    ps = []
    for k in range(3):
        v = U[:, k] / np.linalg.norm(U[:, k]); P = np.outer(v, v.conj())
        ps.append(((np.round(P.real, 6) + 0.0).tobytes(), (np.round(P.imag, 6) + 0.0).tobytes()))
    return tuple(sorted(ps))


def canon(P):
    best = None
    for rp in itertools.permutations(range(3)):
        for cpm in itertools.permutations(range(3)):
            t = tuple(round(float(P[r, c]), 6) + 0.0 for r in rp for c in cpm)
            if best is None or t < best: best = t
    return best


NAMED = {"identity": np.eye(3), "democratic": np.full((3, 3), 1 / 3),
         "TBM": np.array([[2 / 3, 1 / 3, 0], [1 / 6, 1 / 3, 1 / 2], [1 / 6, 1 / 3, 1 / 2]]),
         "BM": np.array([[1 / 2, 1 / 2, 0], [1 / 4, 1 / 4, 1 / 2], [1 / 4, 1 / 4, 1 / 2]])}
NAMED_C = {canon(v): k for k, v in NAMED.items()}


def main():
    out = {}
    imgs = {}
    for i, A in enumerate(GT): imgs.setdefault(cp.key(A), i)
    proj = {}
    for i, A in enumerate(GT):
        ph = np.linalg.det(A) ** (1 / 3); proj.setdefault(cp.key(np.round(A / ph, 9)), i)
    out["M1"] = {"order_G": G.n, "order_image_on_T": len(imgs),
                 "faithful_on_T": len(imgs) == G.n,
                 "elements_with_three_distinct_eigenvalues": sum(1 for A in GT if len(eig_lines(A)) == 3)}
    bases = collections.OrderedDict()
    for i, A in enumerate(GT):
        U = joint_basis([A])
        if U is not None: bases.setdefault(basis_key(U), (U, ("cyclic", WORD[i])))
    for i, j in itertools.combinations(range(G.n), 2):
        A, B = GT[i], GT[j]
        if not np.allclose(A @ B, B @ A, atol=1e-8): continue
        U = joint_basis([A, B])
        if U is not None: bases.setdefault(basis_key(U), (U, ("two-generated", WORD[i] + "," + WORD[j])))
    out["M2"] = {"distinct_eigenbases": len(bases),
                 "from_cyclic": sum(1 for v in bases.values() if v[1][0] == "cyclic")}
    pats = collections.OrderedDict(); blist = list(bases.values())
    for (U1, w1), (U2, w2) in itertools.combinations(blist, 2):
        P = np.abs(U1.conj().T @ U2) ** 2; c = canon(P)
        if c not in pats: pats[c] = {"count": 0, "witness": [w1, w2], "matrix": [[round(float(x), 6) for x in row] for row in np.array(c).reshape(3, 3)]}
        pats[c]["count"] += 1
    full = []
    for c, d in pats.items():
        d = dict(d); d["name"] = NAMED_C.get(c); full.append(d)
    out["M3"] = {"distinct_full_patterns": len(full), "patterns": full,
                 "named_present": sorted({d["name"] for d in full if d["name"]})}
    cols = collections.OrderedDict()
    lines_ = []
    for i, A in enumerate(GT):
        ls = eig_lines(A)
        if len(ls) == 2:
            for e, Wv in ls:
                if Wv.shape[1] == 1: lines_.append((Wv[:, 0], WORD[i]))
    for (U, w) in blist:
        for v, wv in lines_:
            col = tuple(sorted(round(float(abs(np.vdot(U[:, k], v)) ** 2), 6) + 0.0 for k in range(3)))
            if col not in cols: cols[col] = {"count": 0, "witness": [w, wv]}
            cols[col]["count"] += 1
    out["M4"] = {"distinct_fixed_columns": len(cols), "columns": [{"column_sorted": list(c), **d} for c, d in cols.items()],
                 "TM1_column_present": (round(1 / 6, 6), round(1 / 6, 6), round(2 / 3, 6)) in cols,
                 "TM2_column_present": (round(1 / 3, 6), round(1 / 3, 6), round(1 / 3, 6)) in cols}
    out["M5"] = {"full_patterns_times_permutations": len(full) * 36, "columns_times_placements": len(cols) * 9}
    json.dump(out, open(HERE / "mixing_on_the_weave.json", "w"), indent=1, default=str)
    print(json.dumps({k: (v if k not in ("M3", "M4") else {kk: vv for kk, vv in v.items() if kk not in ("patterns", "columns")}) for k, v in out.items()}, indent=1, default=str))


if __name__ == "__main__":
    main()
