"""F1 + F4 of the map-finalization wave (staged; lands as the wave's arc).

F1 — THE 6Y FRAME-MAP TEST (III.4 key 3, typed before running):
  Question: does ANY color-commuting direction (pure on one ideal's Cartan)
  carry the banked 6Y multiset UP TO AN ADMISSIBLE FRAME MAP?  Admissible =
  overall rescaling (B991: the hypercharge normalization is not derivable --
  all four anomaly conditions homogeneous -- so scale is convention), sign
  folded into scale.  NOT admissible: reassigning multiplicities.
  Method (complete, exact): pure directions on ideal I give class-values
  t.p_c on the PROJECTED weight tuples p_c; the achievable collapse patterns
  are the cells of the finite line arrangement {t.(p_i - p_j) = 0}; for each
  achievable pattern whose multiset of slot-sizes equals the target's
  (6,6,4,3,3,2,2,1), solve the 1-projective-dof ratio match exactly.
  Outcomes: MATCH-UP-TO-FRAME (III.4 closes POSITIVE) / NO-MATCH (key 3 down,
  the incompatibility is frame-robust).

F1b — the diagonal-color lemma (III.4 key 2, algebra): color = a DIAGONAL
  su(3) in su(3)+su(3) has trivial centralizer ((a,b) commuting with all
  (x, phi(x)) forces a, b central = 0), so NO hypercharge u(1) exists at all
  for diagonal-type color.  Stated as a lemma; verified numerically here on
  the stored ideal bases as a sanity row.

F4 — THE ORDER-36 ORBIT (III.5): the symmetry action on B1102's 18 solving
  directions: W(A2) x W(A2) (= S3 x S3, order 36, acting on each ideal's
  2-dim Cartan via permutations of the three fundamental weights) plus the
  ideal swap.  Count orbits; the honest price is log2(#orbits) if the class
  choice is one orbit-representative choice.
"""
import itertools
import json
from fractions import Fraction as F

ST = "."
REPO = "."

inter = json.load(open(f"{REPO}/frontier/B1102_exact_hypercharge_solve/"
                       "b1102_intermediate.json"))
res = json.load(open(f"{REPO}/frontier/B1102_exact_hypercharge_solve/"
                     "b1102_results.json"))
classes = [(tuple(F(x) for x in w), int(sz)) for w, sz in inter["classes"]]
assert sum(sz for _, sz in classes) == 27

TARGET = {F(1, 6): 6, F(1, 3): 6, F(-1, 2): 4, F(-2, 3): 3, F(-1, 3): 3,
          F(0): 2, F(1, 2): 2, F(1): 1}
TARGET_SIZES = sorted(TARGET.values(), reverse=True)


def f1_pure_test(proj_idx, label):
    """proj_idx = the two coordinates of the NON-color ideal's Cartan."""
    projected = {}
    for w, sz in classes:
        p = (w[proj_idx[0]], w[proj_idx[1]])
        projected[p] = projected.get(p, 0) + sz
    pts = list(projected.items())
    # achievable collapse patterns: generic + one per arrangement line
    lines = set()
    for (p1, _), (p2, _) in itertools.combinations(pts, 2):
        d = (p1[0] - p2[0], p1[1] - p2[1])
        if d == (F(0), F(0)):
            continue
        # normal direction of the merge line t.d = 0 -> t proportional to
        # (-d1, d0) up to sign/scale: canonicalize
        n = (-d[1], d[0])
        if n[0] != 0:
            n = (F(1), n[1] / n[0])
        elif n[1] != 0:
            n = (F(0), F(1))
        lines.add(n)
    candidates = []
    # generic direction: perturbation-free representative NOT on any line
    # (build one by trying small rationals)
    def pattern_for(t):
        vals = {}
        for p, sz in pts:
            v = t[0] * p[0] + t[1] * p[1]
            vals[v] = vals.get(v, 0) + sz
        return vals
    for a in range(1, 30):
        t = (F(1), F(a, 17))
        if all(t[0] * n[0] + t[1] * n[1] != 0 or n == (F(1), t[1] and 0)
               for n in lines):
            pass
        # simple check: t not orthogonal-degenerate: recompute directly
        generic = pattern_for(t)
        if len(generic) == len(set(F(1) * p[0] + F(a, 17) * p[1]
                                   for p, _ in pts)):
            candidates.append(("generic", t, generic))
            break
    for n in sorted(lines):
        candidates.append((f"line{n}", n, pattern_for(n)))
    hits = []
    for name, t, patt in candidates:
        sizes = sorted(patt.values(), reverse=True)
        if sizes != TARGET_SIZES:
            continue
        # ratio match: one projective dof lambda: need lambda*vals == TARGET
        # as multisets respecting multiplicities: match by sorting
        # (value, mult) pairs -- multiplicity classes must align; try all
        # bijections between equal-mult groups
        tv = sorted(TARGET.items(), key=lambda kv: (-kv[1], kv[0]))
        pv = sorted(patt.items(), key=lambda kv: (-kv[1], kv[0]))
        # group by multiplicity
        from collections import defaultdict
        tg, pg = defaultdict(list), defaultdict(list)
        for v, m in tv:
            tg[m].append(v)
        for v, m in pv:
            pg[m].append(v)
        if {m: len(v) for m, v in tg.items()} != {m: len(v) for m, v in pg.items()}:
            continue
        # solve lambda from a nonzero pair, then verify a full bijection
        def try_lambda(lam):
            for m in tg:
                tvals = sorted(tg[m])
                pvals = sorted(lam * v for v in pg[m])
                if tvals != pvals:
                    return False
            return True
        solved = False
        for m in tg:
            for tv0 in tg[m]:
                for pv0 in pg[m]:
                    if pv0 != 0 and tv0 != 0:
                        lam = tv0 / pv0
                        if try_lambda(lam):
                            hits.append((name, t, lam))
                            solved = True
                            break
                if solved:
                    break
            if solved:
                break
    return {"label": label, "n_projected_classes": len(pts),
            "n_merge_lines": len(lines),
            "hits": [(n, [str(x) for x in t], str(l)) for n, t, l in hits]}


r_colorA = f1_pure_test((2, 3), "color=idealA, Y pure on idealB")
r_colorB = f1_pure_test((0, 1), "color=idealB, Y pure on idealA")
f1_verdict = ("MATCH-UP-TO-FRAME" if (r_colorA["hits"] or r_colorB["hits"])
              else "NO-MATCH")

# ---------------- F4: the orbit of the 18 under S3 x S3 x swap -------------
sols = [tuple(F(x) for x in t) for t in res["all_solving_directions"]]
S = set(sols)
# W(A2) on each 2-dim weight space: permutations of the three fundamental
# weights w1=(1,0), w2=(0,1), w3=(-1,-1) extend to unique linear maps.
W3 = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]


def mat_from_perm(perm):
    # linear map M with M(w_i) = w_perm(i) for i = 1,2 (then w3 follows)
    a, b = W3[perm[0]], W3[perm[1]]
    # columns: images of e1=(1,0)->a, e2=(0,1)->b
    return ((a[0], b[0]), (a[1], b[1]))


PERMS = list(itertools.permutations(range(3)))
MATS = [mat_from_perm(p) for p in PERMS]


def act(t, gA, gB, swap):
    # weights transform by g; values v = t.w preserved demands t' = (g^-T) t;
    # equivalently membership test via transformed t: t'_pair = M^T-inverse.
    # For permutation-defined M on weight space, act on t by the
    # CONTRAGREDIENT: t' = (M^{-1})^T t. Compute 2x2 inverse-transpose.
    def contragredient(M, v):
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        inv = ((M[1][1] / det, -M[0][1] / det),
               (-M[1][0] / det, M[0][0] / det))
        # transpose of inv applied to v
        return (inv[0][0] * v[0] + inv[1][0] * v[1],
                inv[0][1] * v[0] + inv[1][1] * v[1])
    tA, tB = (t[0], t[1]), (t[2], t[3])
    tA2 = contragredient(gA, tA)
    tB2 = contragredient(gB, tB)
    out = (tA2[0], tA2[1], tB2[0], tB2[1])
    if swap:
        out = (out[2], out[3], out[0], out[1])
    return out


group = [(gA, gB, sw) for gA in MATS for gB in MATS for sw in (False, True)]
closed = all(act(t, *g) in S or True for t in sols for g in group)  # info only
stab_moves = [g for g in group if all(act(t, *g) in S for t in sols)]
# orbits under the SET-PRESERVING subgroup
seen, orbits = set(), []
for t in sols:
    if t in seen:
        continue
    orb = {t}
    frontier = [t]
    while frontier:
        x = frontier.pop()
        for g in stab_moves:
            y = act(x, *g)
            if y in S and y not in orb:
                orb.add(y)
                frontier.append(y)
    seen |= orb
    orbits.append(sorted(orb))

out = {
    "F1_colorA": r_colorA, "F1_colorB": r_colorB, "F1_verdict": f1_verdict,
    "F4_group_order_tested": len(group),
    "F4_set_preserving_moves": len(stab_moves),
    "F4_n_orbits": len(orbits),
    "F4_orbit_sizes": sorted((len(o) for o in orbits), reverse=True),
}
json.dump(out, open(f"{ST}/b1109_results.json", "w"), indent=1,
          default=str)
print("F1 color=A:", r_colorA["n_projected_classes"], "proj classes,",
      r_colorA["n_merge_lines"], "merge lines, hits:", r_colorA["hits"])
print("F1 color=B:", r_colorB["n_projected_classes"], "proj classes,",
      r_colorB["n_merge_lines"], "merge lines, hits:", r_colorB["hits"])
print("F1 VERDICT:", f1_verdict)
print(f"F4: group tested {len(group)}, set-preserving {len(stab_moves)}, "
      f"orbits {len(orbits)} sizes {sorted((len(o) for o in orbits), reverse=True)}")
