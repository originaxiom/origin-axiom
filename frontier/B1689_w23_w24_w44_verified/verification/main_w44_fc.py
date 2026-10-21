"""P-229: the SM seat's W44, its frame F_c (c gauge; the residuals are the subgroups of B3 = {+-1} x O = O_h acting on T by
signed permutations), the CKM clause: every residual pair whose mixing family has dimension below 4 fails the necessary
block test against PDG (3 sigma). Main's own code, from W44's recorded read-out.
For every tensor the left-handed rotation diagonalising M M^dagger commutes with the residual's action on T, so it is
fixed up to unitaries inside the residual's isotypic blocks on T. A residual with a two- or three-dimensional irreducible
constituent forces degenerate masses (not viable); a residual acting by scalars leaves a full U(3) (family dimension 4).
So a pair below dimension 4 has both residuals non-scalar with one-dimensional constituents only, and then the block sums
sum_{i in a, j in b} |V_ij|^2 = tr(P_a P_b) are fixed. The test: is there an assignment of the three up masses to H_u's
blocks and the three down masses to H_d's blocks (block sizes respected) with every block sum within 3 sigma of PDG's?"""
import itertools, json, pathlib, numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
data = json.loads((ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json").read_text())
V, S = np.array(data["ckm_abs"]["value"]), np.array(data["ckm_abs"]["sigma"])
V2, S2 = V ** 2, 2 * V * S                                        # |V|^2 and its 1-sigma
signed = []
for perm in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3)); [M.__setitem__((i, perm[i]), s[i]) for i in range(3)]; signed.append(M)
key = lambda M: (M + 0.0).astype(int).tobytes()
idx = {key(M): i for i, M in enumerate(signed)}
def closure(ids):
    els = {idx[key(np.eye(3))]} | set(ids); frontier = list(els)
    while frontier:
        new = []
        for a in frontier:
            for b in list(els):
                for p in (key(signed[a] @ signed[b]), key(signed[b] @ signed[a])):
                    k = idx[p]
                    if k not in els: els.add(k); new.append(k)
        frontier = new
    return frozenset(els)
subs = {closure([i]) for i in range(48)}
grow = set(subs)
while grow:
    new = set()
    for a in grow:
        for b in list(subs):
            j = closure(sorted(a | b))
            if j not in subs: new.add(j)
    subs |= new; grow = new
subs = sorted(subs, key=len)
def blocks(H):
    """isotypic blocks of H on C^3 by a generic central element: returns (projectors, whether every constituent is 1-d,
    whether H acts by scalars)"""
    els = [signed[i] for i in H]
    rng = np.random.default_rng(44)
    # classes of H
    cl = {}
    for g in els:
        c = frozenset(key(h @ g @ np.linalg.inv(h)) for h in els); cl.setdefault(c, []).append(g)
    Z = sum(rng.normal() * sum(g for g in grp) for grp in cl.values())
    w, U = np.linalg.eig(Z)
    # group eigenvalues
    groups = []
    for k, ev in enumerate(w):
        for gr in groups:
            if abs(w[gr[0]] - ev) < 1e-7: gr.append(k); break
        else: groups.append([k])
    P = []
    for gr in groups:
        B = U[:, gr]; Q, _ = np.linalg.qr(B); P.append(Q @ Q.conj().T)
    # constituents 1-d iff the image is abelian on the block: check commutativity of the restricted action
    oned = all(np.allclose(g @ h, h @ g) for g in els for h in els)
    scalar = len(P) == 1 and oned
    return P, oned, scalar
info = {H: blocks(H) for H in subs}
viable_nonscalar = [H for H in subs if info[H][1] and not info[H][2]]
def passes(Pu, Pd):
    nu, nd = [int(round(np.trace(P).real)) for P in Pu], [int(round(np.trace(P).real)) for P in Pd]
    T = np.array([[np.trace(a @ b).real for b in Pd] for a in Pu])
    for pu in itertools.permutations(range(3)):
        # assign up masses (rows 0, 1, 2 of the CKM) to H_u's blocks respecting sizes
        rows = []; k = 0
        for n in nu: rows.append(list(pu[k:k + n])); k += n
        for pd in itertools.permutations(range(3)):
            cols = []; k = 0
            for n in nd: cols.append(list(pd[k:k + n])); k += n
            ok = True
            for a, r in enumerate(rows):
                for b, c in enumerate(cols):
                    meas = V2[np.ix_(r, c)].sum(); sig = np.sqrt((S2[np.ix_(r, c)] ** 2).sum())
                    if abs(meas - T[a, b]) > 3 * sig: ok = False; break
                if not ok: break
            if ok: return True
    return False
n_pairs = 0; passing = []
for Hu in viable_nonscalar:
    for Hd in viable_nonscalar:
        n_pairs += 1
        if passes(info[Hu][0], info[Hd][0]): passing.append((len(Hu), len(Hd)))
# controls: the bite -- the pair (trivial, trivial) is scalar (family 4); a fabricated "measured" CKM equal to a group pattern passes
out = {"subgroups_of_O_h": len(subs), "viable_nonscalar_residuals": len(viable_nonscalar), "pairs_tested": n_pairs,
       "pairs_passing_the_block_test": len(passing), "passing": passing[:10]}
V2_save = V2.copy()
Hz = [H for H in viable_nonscalar if len(info[H][0]) == 3][0]
Pz = info[Hz][0]
V2 = np.array([[np.trace(a @ b).real for b in Pz] for a in Pz]); S2 = np.full((3, 3), 1e-3)
out["control_pattern_passes"] = bool(passes(Pz, Pz))
V2 = V2_save
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1); print(json.dumps(out, indent=1))
