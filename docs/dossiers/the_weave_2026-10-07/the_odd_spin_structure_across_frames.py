#!/usr/bin/env python3
"""W33 of the weave: IS "THREE EXACTLY WHEN THE ODD SPIN STRUCTURE IS LEFT OUT" A LAW ACROSS THE RECORD'S FRAMES?
The rule is W33_RULE.md, committed before this ran (35d16dff). Every count is conditional on its frame (GENESIS GAP1).

  T1 the census: for E6 (V of rank 3), SO(10) (V of rank 4) and SU(5) (F-HE, W of rank 5), every sum of the common
     point's blocks with trivial determinant that L and R keep;
  T2 the counts under (B) W22's block rule, (N) naturality on every channel and (S) the spinor rule (naturality on the
     gauge -1 channels only);
  T3 the naive law; T4 the spinor-rule law; T5 the doublet sectors W and W + D; T6 the sources of each three under (N);
  T7 the verdict.

    python3 the_odd_spin_structure_across_frames.py   ->  the_odd_spin_structure_across_frames.json beside it
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_puncture_content as PC  # noqa: E402  (blocks, direct sums, thin commutants, components, generic lifts)
import the_spin_room as SR  # noqa: E402  (the doublet and the characters' values)
import the_chiral_triplet as CT  # noqa: E402  (the three parities)
import the_z6_twist_eater as Z  # noqa: E402  (compound matrices, subset sums, scalars on a subspace)
import the_order_three_flux as OT  # noqa: E402  (intertwiners)

inv = np.linalg.inv
FRAMES = [("E6", 3), ("SO(10)", 4), ("SU(5)", 5)]
EXPECTED = {  # the rule's T2: (B), (N), (S) for E6 and SO(10); the anomaly-free sets for SU(5)
    "E6": {"c0^3": ([0], [0, 3], [0]), "D + c0": ([1], [-1, 0, 1, 2], [-1, 1]), "P": ([0], [0, 3], [0])},
    "SO(10)": {"c0^4": ([0], [0, 4], [0]), "c0 + P": ([0], [0, 1, 3, 4], [0]), "D + c0^2": ([1], [-1, 1, 3], [-1, 1]),
               "D^2": ([2], [-2, 2], [-2, 2])},
    "SU(5)": {"c0^5": ([0], [0], [0]), "c0^2 + P": ([0], [0], [0]), "D + c0^3": ([], [1], []),
              "D + P": ([], [1, 4], []), "D^2 + c0": ([2], [-2, 2], [-2, 2])}}


def close(P, Q, tol=1e-8):
    return bool(np.allclose(P, Q, atol=tol))


def census(n):
    out = []
    for nD in range(n // 2 + 1):
        for n0, n1, n2, n3 in itertools.product(range(n + 1), repeat=4):
            if n0 + n1 + n2 + n3 + 2 * nD != n:
                continue
            counts = {"D": nD, "c0": n0, "c1": n1, "c2": n2, "c3": n3}
            names = ["D"] * nD + ["c0"] * n0 + ["c1"] * n1 + ["c2"] * n2 + ["c3"] * n3
            A, B = PC.direct_sum(names)
            if not (abs(np.linalg.det(A) - 1) < 1e-9 and abs(np.linalg.det(B) - 1) < 1e-9):
                continue
            UL = PC.generic(OT.intertwiners(A, B, A, A @ B))
            UR = PC.generic(OT.intertwiners(A, B, A @ B, B))
            if UL is not None and UR is not None:
                out.append((PC.name_of(counts), names, counts, A, B, UL, UR))
    return out


def coord_names(names):
    out = []
    for x in names:
        out += [x] * (2 if x == "D" else 1)
    return out


def sector(A, B, UL, UR):
    """one sector's index sets under (B), (N) and (S), and its natural components with their gauge sign"""
    n = A.shape[0]
    h = A @ B @ inv(A) @ inv(B)
    ev = np.round(np.linalg.eigvals(h).real, 9)
    assert close(h, np.diag(np.diag(h))) and set(ev) <= {-1.0, 1.0}
    r_minus = int(sum(ev < 0))
    C = PC.commutant([A, B], n)
    signed = []
    for Q, d, m in PC.components([UL, UR] + C, n):
        s = Z.scalar_on(Q, h)
        assert s is not None and abs(abs(s) - 1) < 1e-9
        signed.append((Q, d, m, int(round(s.real))))
    nat = sorted((d, m) for _, d, m, _ in signed)
    minus = sorted((d, m) for _, d, m, sg in signed if sg == -1)
    res = {"rank": n, "r_minus (two per doublet block)": r_minus,
           "natural structure [(dimension, multiplicity)]": nat, "its gauge -1 part": minus,
           "(B)": [r_minus // 2],
           "(N)": [d - r_minus // 2 for d in Z.subset_sums(nat)],
           "(S)": [d - r_minus // 2 for d in Z.subset_sums(minus)]}
    return res, signed


def sources_of(value, signed, r_minus, cnames):
    """the choices of natural pieces giving the count `value`, each read as the set of blocks it touches"""
    out = []
    for ks in itertools.product(*[range(m + 1) for _, _, m, _ in signed]):
        if sum(k * d for k, (_, d, _, _) in zip(ks, signed)) - r_minus // 2 != value:
            continue
        support = set()
        for k, (Q, _, _, _) in zip(ks, signed):
            if k:
                support |= {cnames[i] for i in range(Q.shape[0]) if np.linalg.norm(Q[i]) > 1e-6}
        out.append(sorted(support))
    return sorted(out)


def parity_doublets(with_zero):
    """W = the three parity doublets chi_p (x) rho_Q (rank 6), with the zero parity's doublet D added if asked"""
    blocks = [(SR.char_val(u, 1) * SR.RHO[1], SR.char_val(u, 2) * SR.RHO[2]) for u in CT.PAR]
    if with_zero:
        blocks.append((SR.RHO[1], SR.RHO[2]))
    n = 2 * len(blocks)
    A, B = np.zeros((n, n), dtype=complex), np.zeros((n, n), dtype=complex)
    for i, (a, b) in enumerate(blocks):
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2], B[2 * i:2 * i + 2, 2 * i:2 * i + 2] = a, b
    return A, B


def has_zero_parity(counts):
    return bool(counts["D"] or counts["c0"])


def run():
    res = {"rule": "W33_RULE.md (committed 35d16dff before this ran)",
           "the conventions": {"(B)": "W22's block rule: the whole gauge -1 eigenspace (doublet blocks +1, characters 0)",
                               "(N)": "naturality on every channel (W28, W32)",
                               "(S)": "the spinor rule: naturality on the gauge -1 channels, no gauge +1 channel"},
           "the moves": "L and R"}
    tables, threes, law_rows, t4, sources = {}, {}, {}, True, {}
    for frame, n in FRAMES:
        rows = {}
        for nm, names, counts, A, B, UL, UR in census(n):
            s1, signed = sector(A, B, UL, UR)
            row = {"blocks": counts, "the zero parity's blocks (c0 or D) present": has_zero_parity(counts)}
            if frame == "SU(5)":
                A2, B2 = Z.compound(A, 2), Z.compound(B, 2)
                s2, _ = sector(A2, B2, Z.compound(UL, 2), Z.compound(UR, 2))
                row["W (the 10-sector)"], row["Lambda^2 W (the 5-bar sector)"] = s1, s2
                for c in ("(B)", "(N)", "(S)"):
                    row["anomaly-free under " + c] = sorted(set(s1[c]) & set(s2[c]))
                sectors = (s1, s2)
            else:
                row["V"] = s1
                for c in ("(B)", "(N)", "(S)"):
                    row["counts under " + c] = s1[c]
                sectors = (s1,)
                if 3 in s1["(N)"]:
                    sources.setdefault(frame, {})[nm] = sources_of(3, signed, s1["r_minus (two per doublet block)"],
                                                                   coord_names(names))
            for sct in sectors:                                    # T4: under (S) a sector's count is +-k
                k = sct["r_minus (two per doublet block)"] // 2
                t4 &= sct["(S)"] == sorted({-k, k})
            rows[nm] = row
        tables[frame] = rows
        key = "anomaly-free under " if frame == "SU(5)" else "counts under "
        threes[frame] = {c: sorted(nm for nm, r in rows.items() if any(abs(x) == 3 for x in r[key + c]))
                         for c in ("(B)", "(N)", "(S)")}
        law_rows[frame] = {c: {"bundles with a three": threes[frame][c],
                               "bundles without the zero parity's blocks": sorted(
                                   nm for nm, r in rows.items() if not r["the zero parity's blocks (c0 or D) present"])}
                           for c in ("(B)", "(N)", "(S)")}
    res["T1 the census"] = {f: sorted(t) for f, t in tables.items()}
    res["T2 the counts"] = tables
    as_table = all(
        (tables[f][nm]["counts under (B)"], tables[f][nm]["counts under (N)"], tables[f][nm]["counts under (S)"]) == exp
        if f != "SU(5)" else
        (tables[f][nm]["anomaly-free under (B)"], tables[f][nm]["anomaly-free under (N)"],
         tables[f][nm]["anomaly-free under (S)"]) == exp
        for f, rows in EXPECTED.items() for nm, exp in rows.items() if nm in tables[f]) and all(
        sorted(tables[f]) == sorted(EXPECTED[f]) for f in EXPECTED)
    res["T2 as the rule's table (and the census as the rule's)"] = bool(as_table)
    law = {}
    for c in ("(B)", "(N)", "(S)"):
        holds = all(law_rows[f][c]["bundles with a three"] == law_rows[f][c]["bundles without the zero parity's blocks"]
                    for f in law_rows)
        law[c] = {"per frame": {f: law_rows[f][c] for f in law_rows}, "the law holds": bool(holds)}
    res["T3 the naive law (a three exactly for the bundles without the zero parity's blocks)"] = law
    res["T4 under (S) every sector's count is +-(its doublet blocks), in every frame"] = bool(t4)
    below_six = not any(threes[f][c] for f in threes for c in ("(B)", "(S)"))
    res["T4 so no three below rank six under (B) or (S)"] = bool(below_six)
    t5 = {}
    for label, with_zero in (("W (the three parity doublets, rank 6)", False),
                             ("W + D (the zero parity's doublet added, rank 8)", True)):
        A, B = parity_doublets(with_zero)
        UL = PC.generic(OT.intertwiners(A, B, A, A @ B))
        UR = PC.generic(OT.intertwiners(A, B, A @ B, B))
        s, _ = sector(A, B, UL, UR)
        t5[label] = {"kept by L and R": bool(UL is not None and UR is not None), "(N)": s["(N)"], "(S)": s["(S)"],
                     "natural structure": s["natural structure [(dimension, multiplicity)]"]}
    t5_ok = (t5["W (the three parity doublets, rank 6)"]["(N)"] == [-3, 3]
             and t5["W (the three parity doublets, rank 6)"]["(S)"] == [-3, 3]
             and t5["W + D (the zero parity's doublet added, rank 8)"]["(N)"] == [-4, 4]
             and t5["W + D (the zero parity's doublet added, rank 8)"]["(S)"] == [-4, 4])
    res["T5 the doublet sectors"] = t5
    res["T5 three parity doublets count +-3; with the zero parity's doublet added, +-4"] = bool(t5_ok)
    res["T6 the sources of each three under (N) (the blocks the kept pieces touch)"] = sources
    trivial_three = "c0^3" in threes.get("E6", {}).get("(N)", [])
    res["T7 the verdict"] = {
        "the census and the counts as the rule's tables": bool(as_table),
        "the naive law fails under (N)": bool(not law["(N)"]["the law holds"]),
        "it fails under (B) and (S) as well (no three at all below rank six)": bool(
            not law["(B)"]["the law holds"] and not law["(S)"]["the law holds"]),
        "under (N) the trivial bundle gives three (E6's c0^3): a rank count": bool(trivial_three),
        "under (S) three needs three doublet blocks: rank six (W23's conclusion as a law)": bool(t4 and below_six),
        "the precise form of the contemplation's point: the zero parity's doublet in the parity doublets' sector "
        "makes four": bool(t5_ok),
        "the contemplation's point 2 downgraded (the counts are label-blind on doublets)": bool(
            not law["(N)"]["the law holds"] and t5_ok)}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_odd_spin_structure_across_frames.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
