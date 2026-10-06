#!/usr/bin/env python3
"""B1478 -- main's own checks of the web seat's five proposed amendments (the seat's scripts are re-run separately; their
outputs are rerun_*.txt).  A1: the parity rule.  A3: the census of primitive word states to length 8.  A4: the charges."""
import itertools, json, collections, pathlib, sys, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
out = {}

# A1 -- in dimension n the index integrand takes Ahat_j (degree 4j) times ch_k (degree 2k) with 4j + 2k = n;
#       ch_k(Vbar) = (-1)^k ch_k(V).  ind(V) - ind(Vbar) can be nonzero only if some odd k occurs.
out["A1"] = {n: sorted(k for k in range(0, n // 2 + 1) if (n - 2 * k) % 4 == 0 and k % 2) for n in range(2, 13, 2)}
assert all(bool(v) == (n % 4 == 2) for n, v in out["A1"].items())

# A4 -- (5 psi - 3 chi)/2 on one 27 of E6: (multiplicity, psi, chi)
states = {"Q,u^c,e^c (10 of SU(5) in 16)": (10, 1, -1), "d^c,L (5bar in 16)": (5, 1, 3), "nu^c (1 in 16)": (1, 1, -5),
          "5 in 10": (5, -2, 2), "5bar in 10": (5, -2, -2), "N (singlet)": (1, 4, 0)}
q = {k: (m, (5 * a - 3 * b) // 2) for k, (m, a, b) in states.items()}
out["A4"] = dict(charges={k: v[1] for k, v in q.items()}, dimension=sum(m for m, _ in q.values()), sum_q=sum(m * c for m, c in q.values()), sum_q3=sum(m * c ** 3 for m, c in q.values()))
assert out["A4"]["dimension"] == 27 and out["A4"]["sum_q"] == 0 and out["A4"]["sum_q3"] == 0
assert sorted(set(out["A4"]["charges"].values())) == [-8, -2, 4, 10]
# B1340's point, which A4 did not carry: on full 27s the check above cannot fail; the cube of the FAMILY part can.
out["A4"]["family_part"] = [-10, 5, 5]; out["A4"]["family_sum"] = sum(out["A4"]["family_part"]); out["A4"]["family_cube_sum"] = sum(f ** 3 for f in out["A4"]["family_part"])
assert out["A4"]["family_sum"] == 0 and out["A4"]["family_cube_sum"] == -750          # anomalous on a chiral spectrum; (0, t, -t) would give 0

# A3 -- primitive cyclic words in L, R up to the swap, length 2..8, both signs
if "--census" in sys.argv:
    import snappy
    def canon(w):
        sw = w.translate(str.maketrans("LR", "RL")); return min([w[i:] + w[:i] for i in range(len(w))] + [sw[i:] + sw[:i] for i in range(len(sw))])
    prim = lambda w: not any(w == w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
    words = sorted({canon("".join(t)) for n in range(2, 9) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t}, key=lambda x: (len(x), x))
    rows = []
    for w in words:
        if not prim(w): continue
        for sg in ("b++", "b+-"):
            M = snappy.Manifold(sg + w)
            if M.solution_type() != "all tetrahedra positively oriented" and M.volume() < 0.5: continue
            x = float(M.chern_simons()) % 0.5
            den = next((d for d in (1, 2, 3, 4, 6, 8, 12, 16, 24, 48) if abs(x * d - round(x * d)) < 1e-9), None)
            rows.append(dict(state=sg + w, cs_mod_half=round(x, 9), denominator=den, amphichiral=bool(M.symmetry_group().is_amphicheiral())))
    out["A3"] = dict(realisations=len(rows), rational=sum(1 for r in rows if r["denominator"]), irrational=sum(1 for r in rows if not r["denominator"]),
                     denominators=dict(collections.Counter(str(r["denominator"]) for r in rows if r["denominator"])), amphichiral=sum(1 for r in rows if r["amphichiral"]),
                     amphichiral_classes=sorted({min(r["cs_mod_half"], round(0.5 - r["cs_mod_half"], 9)) for r in rows if r["amphichiral"]}), rows=rows)
    json.dump(out, open(HERE / "checks.json", "w"), indent=1)
print(json.dumps({k: (v if k != "A3" else {kk: vv for kk, vv in v.items() if kk != "rows"}) for k, v in out.items()}, default=str))
