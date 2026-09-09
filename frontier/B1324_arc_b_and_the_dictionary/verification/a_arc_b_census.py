#!/usr/bin/env python3
"""B1324 PART A -- Phase 2 Arc B: the amphichirality census of the 87 covers of m004 to degree 10 (DESIGN section 3).
Per cover: degree, index, type, cusps, H1 (torsion orders; 3-divisible?), symmetry order, amphichirality by two methods,
and for one-cusped covers the set of sign triples (orientation, s_m, s_l) with l verified rationally trivial by own abelianisation."""
import json, pathlib, sys, time
import numpy as np, sympy as sp, snappy
HERE = pathlib.Path(__file__).resolve().parent
B1295 = HERE.parents[2] / "frontier" / "B1295_the_caveat_closed_by_computation" / "verification" / "cover_scan.json"

def cusp_mat(m):
    try: return np.array([[int(m[0, 0]), int(m[0, 1])], [int(m[1, 0]), int(m[1, 1])]])
    except Exception: return np.array([[int(m[0][0]), int(m[0][1])], [int(m[1][0]), int(m[1][1])]])

def isometry_dets(M, N):
    isos = M.is_isometric_to(N, return_isometries=True)
    out = []
    for iso in isos:
        dets = {int(round(np.linalg.det(cusp_mat(c)))) for c in iso.cusp_maps()}
        out.append((iso, dets))
    return out

def amphichiral_two_ways(N):
    G = N.symmetry_group(); a1 = bool(G.is_amphicheiral())
    Nb = N.copy(); Nb.reverse_orientation()
    a2 = any(d == {1} for _, d in isometry_dets(N, Nb))      # an isometry N -> mirror(N) preserving both given orientations
    return a1, a2, G.order()

def rational_triviality(N):
    """for each cusp: (m rationally trivial?, l rationally trivial?) from the presentation's abelianisation (own code)."""
    G = N.fundamental_group(); gens = list(G.generators()); rels = G.relators(); per = G.peripheral_curves()
    def ab(w):
        v = [0] * len(gens)
        for ch in w: v[gens.index(ch.lower())] += 1 if ch.islower() else -1
        return v
    R = sp.Matrix([ab(r) for r in rels]) if rels else sp.zeros(0, len(gens)); rk = R.rank() if rels else 0
    def triv(w): return (R.col_join(sp.Matrix(ab(w)).T).rank() if rels else sp.Matrix(ab(w)).T.rank()) == rk
    return [(triv(m), triv(l)) for m, l in per]

def triples(N):
    """sign triples over self-isometries of a one-cusped N in SnapPy's (m, l) basis; None entries when a cusp map is not diagonal."""
    out = set(); nondiag = 0
    for iso, _ in isometry_dets(N, N):
        A = cusp_mat(iso.cusp_maps()[0]); det = int(round(np.linalg.det(A)))
        if A[0, 1] != 0 or A[1, 0] != 0: nondiag += 1; out.add((det, None, None)); continue
        out.add((det, int(np.sign(A[0, 0])), int(np.sign(A[1, 1]))))
    return sorted(out, key=str), nondiag

def main():
    M = snappy.Manifold("m004")
    ref = json.loads(B1295.read_text(encoding="utf-8")); ref_rows = ref["rows"] if isinstance(ref, dict) else ref
    ref_by = {(r["degree"], r["index"]): r for r in ref_rows}
    rows = []; t0 = time.time(); mismatches = []
    for d in range(2, 11):
        covs = M.covers(d)
        for i, N in enumerate(covs):
            info = N.cover_info(); H = N.homology(); divs = [int(x) for x in H.elementary_divisors()]
            tors = sorted(x for x in divs if x not in (0, 1)); b1 = divs.count(0)
            a1, a2, order = amphichiral_two_ways(N)
            rec = dict(degree=d, index=i, type=info.get("type"), cusps=N.num_cusps(), H1=str(H), torsion=tors, b1=b1,
                       has_3_divisible_torsion=any(t % 3 == 0 for t in tors), sym_order=order, amphichiral=a1, amphichiral_by_isometry=a2,
                       tets=N.num_tetrahedra(), volume=float(N.volume()))
            r = ref_by.get((d, i))
            if r is not None and (r["cusps"] != rec["cusps"] or r["H1"] != rec["H1"]): mismatches.append((d, i, r["cusps"], rec["cusps"], r["H1"], rec["H1"]))
            if N.num_cusps() == 1:
                rec["rational_triviality_(m,l)"] = rational_triviality(N)
                rec["triples"], rec["nondiagonal_cusp_maps"] = triples(N)
                rec["identity_holds"] = all(t[1] is not None and t[0] == t[1] * t[2] for t in rec["triples"])
            rows.append(rec)
        print(f"degree {d}: {len(covs)} covers ({round(time.time()-t0,1)} s)", flush=True)
    by_type = {}
    for r in rows: by_type.setdefault(r["type"], [0, 0]); by_type[r["type"]][0] += 1; by_type[r["type"]][1] += (not r["amphichiral"])
    chiral = [r for r in rows if not r["amphichiral"]]
    disagreements = [(r["degree"], r["index"]) for r in rows if r["amphichiral"] != r["amphichiral_by_isometry"]]
    one_cusped_chiral_3 = [(r["degree"], r["index"], r["H1"]) for r in rows if r["cusps"] == 1 and not r["amphichiral"] and r["has_3_divisible_torsion"]]
    out = dict(covers=len(rows), per_degree={d: sum(1 for r in rows if r["degree"] == d) for d in range(2, 11)}, b1295_mismatches=mismatches,
               by_type_total_and_chiral=by_type, chiral_total=len(chiral), amphichiral_total=len(rows) - len(chiral),
               methods_disagree=disagreements, one_cusped=sum(1 for r in rows if r["cusps"] == 1),
               one_cusped_chiral_with_3_divisible_torsion=one_cusped_chiral_3,
               A1_covers_inherit_amphichirality=(len(chiral) == 0), A2_chiral_one_cusped_3_divisible=bool(one_cusped_chiral_3),
               A3_identity_holds_on_all_one_cusped=all(r.get("identity_holds", True) for r in rows if r["cusps"] == 1),
               triple_sets_one_cusped={f"{r['degree']}.{r['index']} {r['type']}": r["triples"] for r in rows if r["cusps"] == 1},
               rows=rows, seconds=round(time.time() - t0, 1))
    (HERE / "a_arc_b_census.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print("covers", out["covers"], "per degree", out["per_degree"], "| B1295 mismatches", len(mismatches))
    print("by type (total, chiral):", by_type, "| chiral", len(chiral), "amphichiral", out["amphichiral_total"], "| methods disagree", disagreements)
    print("A1 covers inherit amphichirality:", out["A1_covers_inherit_amphichirality"])
    print("A2 chiral one-cusped with 3-divisible torsion:", one_cusped_chiral_3)
    print("A3 identity det = s_m*s_l on all one-cusped:", out["A3_identity_holds_on_all_one_cusped"])
    for k, v in out["triple_sets_one_cusped"].items(): print("   ", k, v)

if __name__ == "__main__":
    main()
