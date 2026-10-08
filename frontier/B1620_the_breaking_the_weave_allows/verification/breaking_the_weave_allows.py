#!/usr/bin/env python3
"""B1620 -- THE BREAKING THE WEAVE ALLOWS.  The weave's group G (the lifts of L and R on W10's V; order 96; faithful on the
matter triplet T; B1611, B1612) acts irreducibly on T, so any value its symmetry fixes is degenerate (Schur).  Distinct
values need G broken.  Part A takes EVERY subgroup H of G -- none chosen -- as a possible residual symmetry of one sector
and counts what it leaves; part B asks whether the principle's own rule, outside the weave, separates the three parity
sectors.  Exact up to floating point; no data read.

 A1  the subgroup lattice of G: every subgroup (closure of the cyclic subgroups under joins until stable), up to
     conjugacy; orders.
 A2  for each subgroup H: T restricted to H as a sum of irreducibles (multiplicities m_i, dimensions d_i); the number of
     distinct masses a sector keeping H allows (the number of isotypic pieces, counted with their dimensions) and the
     number of free complex mass couplings, dim (T-bar (x) T)^H = sum m_i^2.
 A3  for each pair of subgroups (H1, H2), up to simultaneous conjugacy, with three distinct masses in each sector (both
     one-dimensional on every piece): the mixing is fixed; with a degenerate piece in one sector, the dimension of the
     family of mixing matrices it allows (the real dimension of the commutant's unitary group acting on the degenerate
     eigenspace, modulo phases); the minimal number of free flavour parameters per pair of sectors (masses + mixing).
 B1  the one-sided fixed point u of the rule sigma: a -> ab, b -> a, to length N = F_k (a Fibonacci number near 10^7):
     the frequencies of the four parity classes (A_n mod 2, B_n mod 2) among its prefixes, A_n, B_n the numbers of a's
     and b's in the prefix of length n.
 B2  the three non-trivial parity characters (-1)^{A_n}, (-1)^{B_n}, (-1)^{A_n + B_n} along u: their running means at
     n = F_j for every j, and the largest partial sum (the discrepancy) to N.
 B3  the same at the substitution's scales: the class of the prefix of length F_j for every j (the self-similar orbit the
     rule's 3-cycle on the parities drives).
Writes breaking_the_weave_allows.json."""
import json, pathlib, sys, os, importlib.util, itertools, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("cp", FRONTIER / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
G = cp.Group([cp.W.ML, cp.W.MR]); TB = cp.TB
T = [cp.restrict(M, TB) for M in G.els]


def closure_of(idx_set):
    S = set(idx_set) | {0}; frontier = list(S)
    while frontier:
        new = []
        for a in frontier:
            for b in list(S):
                for c in (G.mult[a][b], G.mult[b][a]):
                    if c not in S: S.add(c); new.append(c)
        frontier = new
    return frozenset(S)


def subgroup_lattice():
    cyc = {closure_of({g}) for g in range(G.n)}
    subs = set(cyc); frontier = set(cyc)
    while frontier:
        new = set()
        for H in frontier:
            for C in cyc:
                if not C <= H:
                    J = closure_of(H | C)
                    if J not in subs: new.add(J)
        subs |= new; frontier = new
    return sorted(subs, key=lambda H: (len(H), sorted(H)))


def conj_class_of(H):
    return min(tuple(sorted({G.mult[G.mult[g][h]][G.inv[g]] for h in H})) for g in range(G.n))


def decompose_T(H):
    mats = [T[h] for h in H]
    # isotypic pieces via the commutant's centre: eigenspaces of a random hermitian commutant element
    rows = np.vstack([np.kron(np.eye(3), M) - np.kron(M.T, np.eye(3)) for M in mats])
    _, s, Vh = np.linalg.svd(rows); c = int(sum(1 for x in s if x < 1e-8)) + max(0, 9 - len(s))
    basis = [Vh[-i - 1].conj().reshape(3, 3, order="F") for i in range(c)]
    # characters of T restricted to H, and the multiplicity structure: sum |chi|^2 / |H| = sum m_i^2 = commutant dim
    chis = [complex(np.trace(M)) for M in mats]
    inner = round(float(sum(abs(x) ** 2 for x in chis) / len(H)), 6)
    # the eigen-decomposition of a generic element of the commutant gives the irreducible pieces when multiplicity-free
    rng = np.random.default_rng(1620); X = sum((rng.normal() + 1j * rng.normal()) * B for B in basis); X = X + X.conj().T
    ev = np.linalg.eigvalsh(X); groups = collections.Counter(round(float(e), 5) for e in ev)
    return {"commutant_dim": c, "sum_m_squared": inner, "eigen_multiplicities_of_generic_commutant": sorted(groups.values())}


def part_A():
    subs = subgroup_lattice()
    classes = {}
    for H in subs:
        k = conj_class_of(H); classes.setdefault(k, H)
    out = {"number_of_subgroups": len(subs), "number_of_conjugacy_classes": len(classes), "classes": []}
    for k, H in sorted(classes.items(), key=lambda kv: len(kv[1])):
        d = decompose_T(H)
        # a sector keeping H: masses are the singular values of an H-invariant matrix: distinct masses = number of
        # distinct eigenvalue blocks of a generic commutant element (each block a degenerate mass of that multiplicity)
        distinct = len(d["eigen_multiplicities_of_generic_commutant"])
        row = {"order": len(H), "T_commutant_dim": d["commutant_dim"], "free_complex_mass_couplings": d["commutant_dim"],
               "mass_blocks": d["eigen_multiplicities_of_generic_commutant"], "distinct_masses": distinct,
               "three_distinct_masses": distinct == 3}
        if distinct == 3:
            # T restricted to H is a sum of three one-dimensional characters: their multiplicities m_i give the basis freedom
            rng = np.random.default_rng(16201); X = sum(rng.normal() * T[h] for h in H)
            _, V = np.linalg.eig(X); V = V / np.linalg.norm(V, axis=0)
            charvecs = [tuple(np.round([complex(np.vdot(V[:, i], T[h] @ V[:, i])) for h in sorted(H)], 5)) for i in range(3)]
            mult = sorted(collections.Counter(charvecs).values())
            row["character_multiplicities"] = mult
            row["basis_freedom_real"] = int(sum(m * m - m for m in mult))
        out["classes"].append(row)
    viable = [c for c in out["classes"] if c["three_distinct_masses"]]
    out["subgroup_classes_allowing_three_distinct_masses"] = len(viable)
    out["their_orders"] = sorted({c["order"] for c in viable})
    out["max_order_with_three_distinct_masses"] = max(c["order"] for c in viable) if viable else None
    # A3: the pair count -- two sectors, each with three distinct masses: masses 3 + 3, mixing freedom min(4, f1 + f2)
    fs = sorted({c["basis_freedom_real"] for c in viable})
    out["A3"] = {"basis_freedoms_available": fs,
                 "pair_mixing_freedoms": sorted({min(4, a + b) for a in fs for b in fs}),
                 "minimal_pair_parameters_masses_plus_mixing": (6 + min(min(4, a + b) for a in fs for b in fs)) if fs else None,
                 "standard_model_per_pair": 10}
    return out


def fibonacci_word(N):
    w = "a"
    while len(w) < N:
        w = "".join("ab" if ch == "a" else "a" for ch in w)
    return w[:N]


def part_B():
    fib = [1, 2]
    while fib[-1] < 10 ** 7: fib.append(fib[-1] + fib[-2])
    N = fib[-1]
    w = np.frombuffer(fibonacci_word(N).encode(), dtype=np.uint8) == ord("a")
    A = np.cumsum(w).astype(np.int64); B = np.cumsum(~w).astype(np.int64)        # prefixes of length 1..N
    pa, pb = A % 2, B % 2
    cls = 2 * pa + pb
    freq = {f"({x},{y})": float(np.mean(cls == 2 * x + y)) for x in (0, 1) for y in (0, 1)}
    chars = {"(-1)^A": 1 - 2 * pa, "(-1)^B": 1 - 2 * pb, "(-1)^(A+B)": 1 - 2 * ((pa + pb) % 2)}
    B2 = {}
    for name, c in chars.items():
        S = np.cumsum(c)
        absS = np.abs(S); runmax = np.maximum.accumulate(absS)
        rec_pos = (np.nonzero(np.diff(runmax) > 0)[0] + 2).tolist()            # prefix lengths at which a new record is set
        rec_val = [int(runmax[p - 1]) for p in rec_pos]
        firsts = {}
        for pos, val in zip(rec_pos, rec_val): firsts.setdefault(val, pos)
        vals = sorted(firsts); ratios = [round(firsts[vals[k + 1]] / firsts[vals[k]], 4) for k in range(len(vals) - 1)]
        B2[name] = {"mean_to_N": float(S[-1] / N), "max_abs_partial_sum": int(absS.max()),
                    "record_values_and_first_positions": {int(v): int(firsts[v]) for v in vals},
                    "ratios_of_successive_record_positions": ratios,
                    "phi_power_6": round(((1 + 5 ** 0.5) / 2) ** 6, 4),
                    "means_at_fibonacci_lengths": {int(f): round(float(S[f - 1] / f), 6) for f in fib if f <= N}}
    B3 = {int(f): [int(A[f - 1] % 2), int(B[f - 1] % 2)] for f in fib if f <= N}
    return {"N": int(N), "B1_class_frequencies": freq, "B2_characters": B2, "B3_class_at_fibonacci_lengths": B3}


def main():
    out = {"A": part_A(), "B": part_B()}
    json.dump(out, open(HERE / "breaking_the_weave_allows.json", "w"), indent=1, default=str)
    show = {"A": {k: v for k, v in out["A"].items() if k != "classes"}, "B": {k: v for k, v in out["B"].items() if k not in ("B2_characters", "B3_class_at_fibonacci_lengths")}}
    print(json.dumps(show, indent=1, default=str))


if __name__ == "__main__":
    main()
