#!/usr/bin/env python3
"""W32 of the weave: WHAT THE PUNCTURE'S END CONDITION GIVES IN F-HE'S TWO SECTORS. The rule is W32_RULE.md, committed
before this ran (62138306). Every count is conditional on the frame F-HE (GENESIS GAP1).

  P1 the completion lemma (exact): three complete generations need the puncture's net 5-bar number zero;
  P2 the census: every rank-5 sum of the common point's blocks with trivial determinant that L and R keep;
  P3 the control: W22's block rule (each doublet block +1, each character block 0), W23's set;
  P4 naturality: the algebra of the lifts of L and R and the bulk commutant on the local solutions of W and of
     Lambda^2 W, the index sets n = -r_minus/2 + dim(Lambda_+), and the anomaly-free counts;
  P5 locality: Lambda_+ a sum of whole eigenspaces of the puncture holonomy;
  P6 what three would need on the weave's five: the plane x1 + x2 + x3 = 0 in the parity lines' local solutions;
  P7 the verdict.

    python3 the_puncture_content.py   ->  the_puncture_content.json beside it
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_spin_room as SR  # noqa: E402  (the doublet rho_Q: a -> i, b -> j; the characters' values)
import the_chiral_triplet as CT  # noqa: E402  (the three parities, as exponents of i on a, b)
import the_z6_twist_eater as Z  # noqa: E402  (thin null space, compound matrices, subset sums)
import the_order_three_flux as OT  # noqa: E402  (intertwiners)

inv = np.linalg.inv
EXP = {"c0": (0, 0), "c1": CT.PAR[0], "c2": CT.PAR[1], "c3": CT.PAR[2]}
RNG = np.random.default_rng(32)


def close(P, Q, tol=1e-8):
    return bool(np.allclose(P, Q, atol=tol))


def block(name):
    if name == "D":
        return SR.RHO[1].astype(complex), SR.RHO[2].astype(complex)
    u = EXP[name]
    return np.array([[SR.char_val(u, 1)]], dtype=complex), np.array([[SR.char_val(u, 2)]], dtype=complex)


def direct_sum(names):
    mats = [block(nm) for nm in names]
    n = sum(a.shape[0] for a, _ in mats)
    A, B = np.zeros((n, n), dtype=complex), np.zeros((n, n), dtype=complex)
    k = 0
    for a, b in mats:
        r = a.shape[0]
        A[k:k + r, k:k + r], B[k:k + r, k:k + r] = a, b
        k += r
    return A, B


def commutant(mats, n):
    """a basis of {X : X g = g X for every g}, by the thin null space (no full SVD of a tall matrix)"""
    M = np.vstack([np.kron(g.T, np.eye(n)) - np.kron(np.eye(n), g) for g in mats])
    N_ = Z.nullspace(M)
    return [N_[:, i].reshape(n, n, order="F") for i in range(N_.shape[1])]


def components(ops, n):
    """the isotypic components of the algebra the operators generate on C^n: [(Q, d, m)] (as Z.components, with the
    thin commutant)"""
    Bs = commutant(ops, n)
    k = len(Bs)
    if k == 1:
        return [(np.eye(n, dtype=complex), n, 1)]
    blocks = [np.column_stack([(Bj @ Bk - Bk @ Bj).flatten() for Bj in Bs]) for Bk in Bs]
    N_ = Z.nullspace(np.vstack(blocks))
    centre = [sum(c[j] * Bs[j] for j in range(k)) for c in N_.T]
    Zc = sum(complex(RNG.normal(), RNG.normal()) * Cc for Cc in centre)
    ev, vec = np.linalg.eig(Zc)
    groups = []
    for i, e in enumerate(ev):
        for gr in groups:
            if abs(gr[0] - e) < 1e-6:
                gr[1].append(i)
                break
        else:
            groups.append([e, [i]])
    out = []
    for _, idx in groups:
        Q, _ = np.linalg.qr(vec[:, idx])
        kW = len(commutant([Q.conj().T @ M @ Q for M in ops], len(idx)))
        m = int(round(kW ** 0.5))
        out.append((Q, len(idx) // m, m))
    return out


def generic(basis):
    """a generic element of a space of intertwiners, if it is invertible; otherwise None (the space then holds no
    isomorphism, since a generic element has the largest rank)"""
    if not basis:
        return None
    U = sum(complex(RNG.normal(), RNG.normal()) * X for X in basis)
    return U if abs(np.linalg.det(U)) > 1e-8 else None


def name_of(counts):
    parts = []
    if counts["D"]:
        parts.append("D" if counts["D"] == 1 else "D^%d" % counts["D"])
    if counts["c0"]:
        parts.append("c0" if counts["c0"] == 1 else "c0^%d" % counts["c0"])
    k = counts["c1"]
    if k and counts["c2"] == k and counts["c3"] == k:
        parts.append("P" if k == 1 else "P^%d" % k)
    else:
        for c in ("c1", "c2", "c3"):
            if counts[c]:
                parts.append(c if counts[c] == 1 else "%s^%d" % (c, counts[c]))
    return " + ".join(parts)


def sector(A, B, UL, UR):
    """for a representation (A, B) with lifts UL, UR: r_minus, the structures and the index sets"""
    n = A.shape[0]
    h = A @ B @ inv(A) @ inv(B)
    ev = np.round(np.linalg.eigvals(h).real, 9)
    assert close(h, np.diag(np.diag(h))) and set(ev) <= {-1.0, 1.0}
    assert all(close(h @ X, X @ h) for X in (A, B))              # central in the image
    r_minus = int(sum(ev < 0))
    r_plus = n - r_minus
    C = commutant([A, B], n)
    nat = sorted((d, m) for _, d, m in components([UL, UR] + C, n))
    loc = sorted((d, 1) for d in (r_plus, r_minus) if d)
    return {"rank": n, "r_minus": r_minus, "bulk commutant dimension": len(C),
            "naturality structure": nat, "locality structure": loc,
            "index under naturality": [d - r_minus // 2 for d in Z.subset_sums(nat)],
            "index under locality": [d - r_minus // 2 for d in Z.subset_sums(loc)],
            "index under W22's block rule": r_minus // 2}


def run():
    res = {"rule": "W32_RULE.md (committed 62138306 before this ran)",
           "the frame": "F-HE (GENESIS GAP1: a hypothesis); the 10 of SU(5)_g carries W, the 5-bar carries Lambda^2 W",
           "the moves": "L and R (main's S87: the swap and the tick sigma = L o P reverse the orientation the index needs)"}
    # ---------------------------------------------------------------------------------------------------------- P1
    a, b = sp.symbols("a b", integer=True)
    total10, total5b = 1 + a, 3 + b
    lemma = sp.simplify((total10 - total5b).subs(a, b + 2)) == 0
    res["P1 the completion lemma"] = {
        "the five reads (1, 3) under W22's rule (W23); localized net numbers (a, b) cancel its anomaly iff a - b = 2": True,
        "then n(10) - n(5-bar) = (1 + a) - (3 + b) = 0, and the count is 3 + b (exact)": bool(lemma),
        "so three complete generations need the puncture's net 5-bar number b = 0": bool(lemma)}
    # ---------------------------------------------------------------------------------------------------------- P2
    kept = []
    for nD in range(3):
        for n0, n1, n2, n3 in itertools.product(range(6), repeat=4):
            if n0 + n1 + n2 + n3 + 2 * nD != 5:
                continue
            counts = {"D": nD, "c0": n0, "c1": n1, "c2": n2, "c3": n3}
            names = ["D"] * nD + ["c0"] * n0 + ["c1"] * n1 + ["c2"] * n2 + ["c3"] * n3
            A, B = direct_sum(names)
            if not (abs(np.linalg.det(A) - 1) < 1e-9 and abs(np.linalg.det(B) - 1) < 1e-9):
                continue
            UL = generic(OT.intertwiners(A, B, A, A @ B))                            # the class kept: an
            UR = generic(OT.intertwiners(A, B, A @ B, B))                            # invertible intertwiner
            if UL is not None and UR is not None:
                kept.append((name_of(counts), names, A, B, UL, UR))
    res["P2 the census"] = {"the bundles L and R keep (rank 5, trivial determinant)": [k[0] for k in kept],
                            "how many": len(kept)}
    # ---------------------------------------------------------------------------------------------------------- P3-P5
    table = {}
    for nm, names, A, B, UL, UR in kept:
        assert close(UL @ A @ inv(UL), A) and close(UL @ B @ inv(UL), A @ B)
        assert close(UR @ A @ inv(UR), A @ B) and close(UR @ B @ inv(UR), B)
        s10 = sector(A, B, UL, UR)
        A2, B2 = Z.compound(A, 2), Z.compound(B, 2)
        s5b = sector(A2, B2, Z.compound(UL, 2), Z.compound(UR, 2))
        row = {"W (the 10-sector)": s10, "Lambda^2 W (the 5-bar sector)": s5b}
        for cond in ("naturality", "locality"):
            n10, n5b = s10["index under %s" % cond], s5b["index under %s" % cond]
            row["anomaly-free counts under %s" % cond] = sorted(set(n10) & set(n5b))
        row["W22's block rule: (n(10), n(5-bar))"] = [s10["index under W22's block rule"],
                                                      s5b["index under W22's block rule"]]
        table[nm] = row
    control = sorted(tuple(r["W22's block rule: (n(10), n(5-bar))"]) for r in table.values())
    res["P3 the control (W22's block rule)"] = {
        "readings": {nm: r["W22's block rule: (n(10), n(5-bar))"] for nm, r in table.items()},
        "the set is W23's SU(5) set {(0, 0), (1, 3), (2, 2)}": sorted(set(control)) == [(0, 0), (1, 3), (2, 2)]}
    res["P4 and P5 the bundles"] = table
    nat_free = {nm: r["anomaly-free counts under naturality"] for nm, r in table.items()}
    loc_free = {nm: r["anomaly-free counts under locality"] for nm, r in table.items()}
    three_nat = any(abs(x) == 3 for v in nat_free.values() for x in v)
    three_loc = any(abs(x) == 3 for v in loc_free.values() for x in v)
    res["P4 naturality: the anomaly-free counts"] = nat_free
    res["P4 a natural three (|n| = 3) for some bundle"] = bool(three_nat)
    res["P5 locality: the anomaly-free counts"] = loc_free
    res["P5 a local three for some bundle"] = bool(three_loc)
    # ---------------------------------------------------------------------------------------------------------- P6
    five = [k for k in kept if k[0] == "D + P"]
    p6 = {}
    if five:
        nm, names, A, B, UL, UR = five[0]
        idx, k = [], 0                                                             # the parity lines' rows (D has two)
        for x in names:
            if x in ("c1", "c2", "c3"):
                idx.append(k)
            k += 2 if x == "D" else 1
        perm = []
        for U in (UL, UR):
            sub = U[np.ix_(idx, idx)]
            Pm = (abs(sub) > 1e-9).astype(complex)                                 # the lift's pattern, entries 1
            assert close(Pm @ Pm.T, np.eye(3))
            perm.append(Pm)
        plane = np.array([[1, -1, 0], [0, 1, -1]], dtype=complex).T                # x1 + x2 + x3 = 0
        Pp = plane @ np.linalg.pinv(plane)                                         # its projector
        kept_by_perm = all(close(Pm @ Pp, Pp @ Pm @ Pp) for Pm in perm)
        C = commutant([A, B], A.shape[0])
        Csub = [X[np.ix_(idx, idx)] for X in C]
        kept_by_comm = all(close(X @ Pp, Pp @ X @ Pp) for X in Csub)
        perm_struct = sorted((d, m) for _, d, m in components(perm, 3))
        s10 = table[nm]["W (the 10-sector)"]
        s5b = table[nm]["Lambda^2 W (the 5-bar sector)"]
        n10_mixed = -s10["r_minus"] // 2 + s10["r_minus"] + 2                    # D's two kept, the plane
        p6 = {"the permutation lifts on the three parity lines: structure": perm_struct,
              "the plane x1 + x2 + x3 = 0 is kept by them": bool(kept_by_perm),
              "it is kept by the bulk commutant": bool(kept_by_comm),
              "n(10) with D's local solutions and the plane kept": n10_mixed,
              "n(5-bar) = 3 is natural (in the naturality set)": bool(3 in s5b["index under naturality"]),
              "n(10) = 3 is natural": bool(3 in s10["index under naturality"]),
              "so three in the 10-sector needs the parities mixed, and three in the 5-bar sector needs them kept apart":
                  bool(n10_mixed == 3 and kept_by_perm and not kept_by_comm and 3 in s5b["index under naturality"]
                       and 3 not in s10["index under naturality"])}
    res["P6 what three would need on the weave's five"] = p6
    # ---------------------------------------------------------------------------------------------------------- P7
    expected_nat = {"c0^5": [0], "c0^2 + P": [0], "D + c0^3": [1], "D + P": [1, 4], "D^2 + c0": [-2, 2]}
    expected_loc = {"c0^5": [0], "c0^2 + P": [0], "D + c0^3": [1], "D + P": [1], "D^2 + c0": [-2, 2]}
    res["P7 the verdict"] = {
        "the census is the rule's five": sorted(nat_free) == sorted(expected_nat),
        "naturality as the rule's table": nat_free == expected_nat,
        "locality as the rule's list": loc_free == expected_loc,
        "the control is W23's set": res["P3 the control (W22's block rule)"][
            "the set is W23's SU(5) set {(0, 0), (1, 3), (2, 2)}"],
        "no natural or local three for any bundle built from the common point's blocks": bool(
            not three_nat and not three_loc),
        "the weave's five is cured naturally only at one or four complete generations (b = -2 or +1)": nat_free.get(
            "D + P") == [1, 4],
        "NEGATIVE: in F-HE the puncture's end condition does not make three": bool(not three_nat and not three_loc)}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_puncture_content.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
