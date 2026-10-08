"""W43 (the rule: W43_RULE.md, committed before this script). Which trimaximal family each mass tensor allows, in the
record's frame (every element c(g) S(g) of the weave's group is flavour; B1620's) and in the frame where c is gauge (the
flavour group O acting by S, with the +-1 a charged Higgs leaves: the signed permutation group B3 = {+-1} x O).

  F1  the record's frame: for every ordered pair of viable residuals (W42's exact viability) under each tensor, the
      fixed columns of the mixing |U|^2 = |W_l^dagger W_nu|^2 (TM1: (2/3, 1/6, 1/6); TM2: (1/3, 1/3, 1/3), each up to
      the order of its entries) and B1620's family dimension (the rank of the couplings -> nine |U_ij|^2 and J);
  F2  B1620's stored fits (received/B1620_post_seal_tensors.json, verbatim): each PMNS family below four dimensions,
      its fixed columns and rows classified (a transcription, read before the rule);
  F3  the frame where c is gauge: B3's lattice, viability under each tensor, O's invariant in Sym^2 T, and F1's census;
  F4  every rotation t of order 3 with every twist u in mu_24: the Sym^2 T fixed space of u t, exactly.

Run: python3 the_trimaximal_families.py  ->  the_trimaximal_families.json beside it.
"""
import itertools
import json
import random
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_breaking_verified as BV  # noqa: E402  (W42: the group, exact viability)

OUT = HERE / "the_trimaximal_families.json"
RECEIVED = HERE / "received" / "B1620_post_seal_tensors.json"
TENSORS = BV.TENSORS
TARGETS = {"TM1": np.array([1 / 6, 1 / 6, 2 / 3]), "TM2": np.array([1 / 3, 1 / 3, 1 / 3])}
IDENT = (0, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))


def lattice(G):
    """every subgroup of the group G (a list of exact encodings (k, S)), as frozensets of encodings"""
    idx = {x: i for i, x in enumerate(G)}
    MUL = [[idx[BV.emul(x, y)] for y in G] for x in G]
    E = idx[IDENT]

    def closure(gens):
        S, fr = {E}, [E]
        while fr:
            nx = []
            for x in fr:
                for g in gens:
                    y = MUL[x][g]
                    if y not in S:
                        S.add(y)
                        nx.append(y)
            fr = nx
        return frozenset(S)

    subs = {}
    for g in range(len(G)):
        subs.setdefault(closure([g]), [g])
    queue = list(subs.items())
    while queue:
        Hs, gens = queue.pop()
        for g in range(len(G)):
            if g not in Hs:
                J = closure(gens + [g])
                if J not in subs:
                    subs[J] = gens + [g]
                    queue.append((J, gens + [g]))
    subs = sorted(subs, key=lambda s: (len(s), sorted(s)))
    abelian = [all(MUL[a][b] == MUL[b][a] for a in Hs for b in Hs) for Hs in subs]
    return [[G[h] for h in sorted(Hs)] for Hs in subs], abelian


def numeric(z):
    return sum(c * np.exp(2j * np.pi * m / 24) for m, c in enumerate(z))


def numeric_basis(basis, tensor):
    out = []
    for v in basis:
        M = np.zeros((3, 3), complex)
        for (i, j), z in v.items():
            M[i, j] += numeric(z)
            if tensor == "Sym^2 T" and i != j:
                M[j, i] += numeric(z)
        out.append(M)
    return out


def member(B, x):
    n = len(B)
    return sum((x[k] + 1j * x[n + k]) * B[k] for k in range(n))


def left(M):
    return np.linalg.eigh(M @ M.conj().T)[1]


def invariants(U):
    A = np.abs(U) ** 2
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))
    return np.concatenate([A.ravel(), [J]])


def fixed_columns(Bl, Bn, rng, samples=4):
    """the trimaximal column types present at every sampled member of the pair's family"""
    found = None
    for _ in range(samples):
        Ul = left(member(Bl, rng.normal(size=2 * len(Bl))))
        Un = left(member(Bn, rng.normal(size=2 * len(Bn))))
        A = np.abs(Ul.conj().T @ Un) ** 2
        here = {n for n, t in TARGETS.items() for k in range(3) if np.allclose(np.sort(A[:, k]), t, atol=1e-8)}
        found = here if found is None else found & here
    return found


def family_dim(Bl, Bn, rng):
    nl, nn = 2 * len(Bl), 2 * len(Bn)

    def V(x):
        return left(member(Bl, x[:nl])).conj().T @ left(member(Bn, x[nl:]))

    best = 0
    for _ in range(3):
        x = rng.normal(size=nl + nn)
        h = 1e-6
        Jm = np.array([(invariants(V(x + h * e)) - invariants(V(x - h * e))) / (2 * h) for e in np.eye(nl + nn)]).T
        s = np.linalg.svd(Jm, compute_uv=False)
        best = max(best, int(sum(s > max(1e-5, 1e-6 * s[0]))))
    return best


def census(subs, tensor, seed):
    """viability (exact, W42's method) and the trimaximal families of every ordered pair of viable residuals"""
    rng_exact = random.Random(seed)
    rng = np.random.default_rng(seed)
    viable = []
    for H in subs:
        basis = BV.fixed_basis(H, tensor)
        if BV.viable_exact(basis, tensor, rng_exact) > 0:
            viable.append((H, numeric_basis(basis, tensor)))
    tally = {"TM1": {}, "TM2": {}}
    examples = {"TM1": set(), "TM2": set()}
    for (Hl, Bl), (Hn, Bn) in itertools.product(viable, viable):
        types = fixed_columns(Bl, Bn, rng)
        if types:
            d = family_dim(Bl, Bn, rng)
            for t in types:
                tally[t][str(d)] = tally[t].get(str(d), 0) + 1
                if d == 2:
                    examples[t].add((len(Hl), len(Hn)))
    return {"viable residuals": len(viable), "ordered pairs": len(viable) ** 2,
            "pairs with a fixed TM1 column, by family dimension": dict(sorted(tally["TM1"].items())),
            "pairs with a fixed TM2 column, by family dimension": dict(sorted(tally["TM2"].items())),
            "TM1 allowed (a fixed column with family dimension 2)": bool(tally["TM1"].get("2", 0)),
            "TM2 allowed (a fixed column with family dimension 2)": bool(tally["TM2"].get("2", 0)),
            "orders (charged leptons, neutrinos) of the TM1 pairs of dimension 2": sorted(examples["TM1"]),
            "orders (charged leptons, neutrinos) of the TM2 pairs of dimension 2": sorted(examples["TM2"])}


def name_of(vals):
    v = np.sort(np.array(vals, float))
    for n, t in TARGETS.items():
        if np.allclose(v, t, atol=1e-4):
            return n
    return "other"


def transcribe():
    """B1620's PMNS families below four dimensions: fixed columns (a neutrino piece of dimension 1 against three
    charged-lepton lines) and fixed rows (the reverse), from its stored block sums"""
    d = json.loads(RECEIVED.read_text(encoding="utf-8"))
    out = {}
    for t, key in (("T-bar (x) T", "Tbar_x_T"), ("T (x) T", "T_x_T"), ("Sym^2 T", "Sym2_T")):
        rows = []
        for e in d[key]["pmns_fits_below_4"]:
            dl, dn = e["piece_dims"]
            B = np.array(e["block_sums"]).reshape(len(dl), len(dn))
            cols = [name_of(B[:, k]) for k in range(len(dn)) if dn[k] == 1] if dl == [1, 1, 1] else []
            rws = [name_of(B[i, :]) for i in range(len(dl)) if dl[i] == 1] if dn == [1, 1, 1] else []
            rows.append({"orders": e["orders"], "family_dim": e["family_dim"], "piece_dims": e["piece_dims"],
                         "fixed columns": cols, "fixed rows": rws, "reached": e["reached"]})
        out[t] = {"entries": rows,
                  "a TM1 column in some entry": any("TM1" in r["fixed columns"] for r in rows),
                  "a TM2 column in some entry": any("TM2" in r["fixed columns"] for r in rows)}
    return out


def main():
    G, _, _, _ = BV.the_group_exact()
    subs_rec, _ = lattice(G)
    F1 = {t: census(subs_rec, t, 101 + i) for i, t in enumerate(TENSORS)}
    F2 = transcribe()

    B3 = sorted((k, S) for S in BV.rotations() for k in (0, 12))
    subs_U, ab_U = lattice(B3)
    deltas = BV.fixed_basis(B3, "Sym^2 T")
    delta_ok = len(deltas) == 1 and set(deltas[0]) == {(0, 0), (1, 1), (2, 2)} and len(
        {c for c in deltas[0].values()}) == 1
    F3 = {"B3: order": len(B3), "subgroups": len(subs_U), "abelian": sum(ab_U),
          "Sym^2 T invariants of B3 (and of O): the identity alone": bool(delta_ok),
          **{t: census(subs_U, t, 201 + i) for i, t in enumerate(TENSORS)}}

    rng = random.Random(301)
    order3 = [S for S in BV.rotations() if BV.stype(S) == "3-cycle"]
    F4_rows, F4_ok = [], True
    for S in order3:
        for k in range(24):
            x, cyc = (k, S), [IDENT]
            while True:
                y = BV.emul(cyc[-1], x)
                if y == IDENT:
                    break
                cyc.append(y)
            basis = BV.fixed_basis(cyc, "Sym^2 T")
            passed = BV.viable_exact(basis, "Sym^2 T", rng)
            F4_ok &= passed == 0
            F4_rows.append((len(basis), passed))
    F4 = {"rotations of order 3": len(order3), "twists": 24, "cases": len(F4_rows),
          "fixed dimensions seen": sorted({r[0] for r in F4_rows}),
          "none viable under Sym^2 T": bool(F4_ok)}

    checks = {
        "F1: the record's frame: TM1 and TM2 under T-bar (x) T; TM2 but not TM1 under T (x) T; neither under Sym^2 T": (
            F1["T-bar (x) T"]["TM1 allowed (a fixed column with family dimension 2)"]
            and F1["T-bar (x) T"]["TM2 allowed (a fixed column with family dimension 2)"]
            and not F1["T (x) T"]["TM1 allowed (a fixed column with family dimension 2)"]
            and F1["T (x) T"]["TM2 allowed (a fixed column with family dimension 2)"]
            and not F1["Sym^2 T"]["TM1 allowed (a fixed column with family dimension 2)"]
            and not F1["Sym^2 T"]["TM2 allowed (a fixed column with family dimension 2)"]),
        "F1: the viable counts are W42's (57 / 24 / 16)": [F1[t]["viable residuals"] for t in TENSORS] == [57, 24, 16],
        "F2: B1620's T (x) T families carry TM2's column and never TM1's; its T-bar (x) T families both": (
            F2["T (x) T"]["a TM2 column in some entry"] and not F2["T (x) T"]["a TM1 column in some entry"]
            and F2["T-bar (x) T"]["a TM1 column in some entry"] and F2["T-bar (x) T"]["a TM2 column in some entry"]),
        "F3: B3 has 98 subgroups, 66 abelian; viable 66 / 66 / 49; O's Sym^2 T invariant is the identity": (
            (F3["subgroups"], F3["abelian"]) == (98, 66)
            and [F3[t]["viable residuals"] for t in TENSORS] == [66, 66, 49]
            and F3["Sym^2 T invariants of B3 (and of O): the identity alone"]),
        "F3: where c is gauge, TM1 and TM2 under T-bar (x) T and T (x) T, neither under Sym^2 T": all(
            F3[t]["TM1 allowed (a fixed column with family dimension 2)"]
            and F3[t]["TM2 allowed (a fixed column with family dimension 2)"] for t in ("T-bar (x) T", "T (x) T"))
            and not F3["Sym^2 T"]["TM1 allowed (a fixed column with family dimension 2)"]
            and not F3["Sym^2 T"]["TM2 allowed (a fixed column with family dimension 2)"],
        "F4: no twist of a 3-cycle is viable under Sym^2 T": F4["none viable under Sym^2 T"] and F4["cases"] == 192,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    out = {"status": "W43: the trimaximal families each tensor allows, in the record's frame and where c is gauge "
                     "(the rule first; F2 transcribes B1620's stored fits, read before the rule)",
           "F1: the record's frame": F1, "F2: B1620's stored PMNS families below four dimensions": F2,
           "F3: the frame where c is gauge (B3 = {+-1} x O acting by +-S)": F3,
           "F4: the 3-cycles with every twist in mu_24 under Sym^2 T": F4,
           "checks": checks, "every check holds": all(checks.values())}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(checks, indent=1))
    print("every check holds:", all(checks.values()))


if __name__ == "__main__":
    main()
