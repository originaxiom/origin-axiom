#!/usr/bin/env python3
"""B1483 cell C2 (the SM seat's ask of 2026-10-06): Theorem A on a cover with several cusps.

For a cyclic cover N of a base manifold: every spin structure s' of N (every SL(2,C) lift of N's holonomy), SnapPy's
complete list of self-isometries of N, and for every orientation-reversing isometry f and every ODD orbit of f on the cusps (length l; l = 1 is an
invariant cusp): the return map of f^l on the orbit's first cusp, its type (rectangular: = 1 mod 2; rhombic otherwise),
the class w it fixes mod 2 when rhombic, and sigma_{s'}(w) = tr rho_{s'}(w) / 2.
Theorem A (B1477) in orbit form: if f fixes s' so does the mirror f^l, which preserves that cusp; so if the return map is
rhombic and sigma_{s'}(w) = -1, f does not fix s'.
A spin structure is EXCLUDED FOR EVERY MIRROR if every reversing isometry has an odd orbit where that happens."""
import sys, json, itertools, pathlib, warnings; warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent; FR = next(p for p in HERE.parents if p.name == "frontier")
sys.path.insert(0, str(FR / "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp" / "verification"))


def setup_manifold(N):
    """B1476's setup_any for a Manifold object: the holonomy on SnapPy's presentation with the SL(2,C) lift repaired"""
    import cusp_shear as CSH
    R = CSH.R
    M = N.high_precision(); G = M.fundamental_group(); gens, rels = G.generators(), G.relators()
    rho = {g: R.mat2(G.SL2C(g)) for g in gens}
    def relsign(r):
        A = R.word_mat(r, rho)
        p = max(abs(A[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2)); m = max(abs(A[i, j] + (1 if i == j else 0)) for i in range(2) for j in range(2))
        return 0 if p < R.TOL else (1 if m < R.TOL else None)
    want = [relsign(r) for r in rels]
    if any(w is None for w in want): raise ValueError("holonomy fails the relators")
    if any(want):
        import sympy as sp
        E = sp.Matrix([[x % 2 for x in R.expvec(r, gens)] for r in rels]); b = sp.Matrix(want)
        # solve E x = want over F_2 by elimination (the generators are too many to enumerate on a large cover)
        A, piv = gf2_rref(E.row_join(b))
        sol = [0] * len(gens)
        for row, c in piv: sol[c] = A[row][-1]
        for k, g in enumerate(gens):
            if sol[k]: rho[g] = -rho[g]
        assert all(relsign(r) == 0 for r in rels), "lift repair failed"
    return dict(M=M, G=G, gens=gens, rels=rels, rho=rho), R


def gf2_rref(A):
    A = [[int(x) % 2 for x in A.row(i)] for i in range(A.rows)]; piv = []; r = 0; ncol = len(A[0]) - 1
    for c in range(ncol):
        p = next((i for i in range(r, len(A)) if A[i][c]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(len(A)):
            if i != r and A[i][c]: A[i] = [(x + y) % 2 for x, y in zip(A[i], A[r])]
        piv.append((r, c)); r += 1
    assert all(not row[-1] for row in A[r:]), "the PSL representation does not lift"
    return A, piv


def characters(gens, rels):
    """Hom(pi_1, +-1) as sign vectors on the generators: the kernel over F_2 of the relators' exponent matrix"""
    E = [[sum(1 for ch in r if ch.lower() == g) % 2 for g in gens] for r in rels]
    A = [row + [0] for row in E]; M = __import__("sympy").Matrix(A) if A else None
    red, piv = gf2_rref(M) if M is not None else ([], [])
    pc = {c for _, c in piv}; free = [c for c in range(len(gens)) if c not in pc]; out = []
    for bits in itertools.product((0, 1), repeat=len(free)):
        x = [0] * len(gens)
        for f, b in zip(free, bits): x[f] = b
        for row, c in piv: x[c] = sum(red[row][k] * x[k] for k in free) % 2
        out.append({g: (-1 if x[k] else 1) for k, g in enumerate(gens)})
    return out


def analyse(N, label):
    pk, R = setup_manifold(N); gens, rels = pk["gens"], pk["rels"]; chars = characters(gens, rels); per = pk["G"].peripheral_curves()
    inv = lambda w: w[::-1].swapcase()
    def pw(i, x, y):
        mw, lw = per[i]; return (mw * x if x >= 0 else inv(mw) * (-x)) + (lw * y if y >= 0 else inv(lw) * (-y))
    isos = N.is_isometric_to(N, return_isometries=True); mirrors = []
    mul = lambda X, Y: [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]], [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]
    for iso in isos:
        maps = [[[int(m[0, 0]), int(m[0, 1])], [int(m[1, 0]), int(m[1, 1])]] for m in iso.cusp_maps()]; imgs = list(iso.cusp_images())
        if {m[0][0] * m[1][1] - m[0][1] * m[1][0] for m in maps} != {-1}: continue
        fixed = []; cyc_all = cycles(imgs)
        for cyc in cyc_all:
            if len(cyc) % 2 == 0: continue
            # the return map of f^l on the first cusp of an odd cycle, columns = images (the convention B1477 checked on
            # m003's longitude); it must be an involution of determinant -1 over Z, or the composition is wrong
            F = [[1, 0], [0, 1]]
            for k in cyc: F = mul(maps[k], F)
            if mul(F, F) != [[1, 0], [0, 1]]: fixed.append(dict(cusp=cyc[0], orbit=len(cyc), type="INVALID", w=None)); continue
            F2 = [[x % 2 for x in row] for row in F]
            if F2 == [[1, 0], [0, 1]]: fixed.append(dict(cusp=cyc[0], orbit=len(cyc), type="rectangular", w=None)); continue
            w = [v for v in ((1, 0), (0, 1), (1, 1)) if ((F2[0][0] * v[0] + F2[0][1] * v[1]) % 2, (F2[1][0] * v[0] + F2[1][1] * v[1]) % 2) == v]
            fixed.append(dict(cusp=cyc[0], orbit=len(cyc), type="rhombic", w=list(w[0]) if len(w) == 1 else None))
        mirrors.append(dict(cycle_type=sorted(len(c) for c in cyc_all), fixed=fixed))
    # the sign of each spin structure on each (cusp, class mod 2)
    def sign(chi, i, v):
        rho = {g: chi[g] * pk["rho"][g] for g in gens}; A = R.word_mat(pw(i, v[0], v[1]), rho); t = complex(A[0, 0] + A[1, 1])
        assert abs(abs(t.real) - 2) < 1e-6 and abs(t.imag) < 1e-6, ("not parabolic", t); return 1 if t.real > 0 else -1
    need = sorted({(f["cusp"], tuple(f["w"])) for m in mirrors for f in m["fixed"] if f["type"] == "rhombic" and f["w"]})
    spin = []
    for chi in chars:
        sg = {k: sign(chi, k[0], k[1]) for k in need}
        excluded = [any(f["type"] == "rhombic" and f["w"] and sg[(f["cusp"], tuple(f["w"]))] == -1 for f in m["fixed"]) for m in mirrors]
        spin.append(dict(signs={"%d:%s" % (k[0], "".join(map(str, k[1]))): v for k, v in sg.items()}, mirrors_excluded=sum(excluded), excluded_for_every_mirror=bool(mirrors) and all(excluded)))
    try: cs = float(N.chern_simons()) % 0.5
    except Exception: cs = None
    return dict(label=label, tetrahedra=N.num_tetrahedra(), cusps=N.num_cusps(), h1=str(N.homology()), cs_mod_half=cs, isometries=len(isos), mirrors=len(mirrors),
                mirror_patterns=sorted({(tuple(m["cycle_type"]), tuple(sorted((f["orbit"], f["type"]) for f in m["fixed"]))) for m in mirrors}),
                invalid=sum(1 for m in mirrors for f in m["fixed"] if f["type"] == "INVALID"), fixed_classes=["%d:%s" % (k[0], "".join(map(str, k[1]))) for k in need],
                spin_structures=len(spin), excluded_for_every_mirror=sum(1 for s in spin if s["excluded_for_every_mirror"]),
                sign_patterns=sorted({tuple(sorted(s["signs"].items())) for s in spin}), spin=spin)


def cycles(perm):
    seen, out = set(), []
    for c in range(len(perm)):
        if c in seen: continue
        cyc = [c]; seen.add(c); x = perm[c]
        while x != c: cyc.append(x); seen.add(x); x = perm[x]
        out.append(cyc)
    return out


if __name__ == "__main__":
    base, degree, ncusps = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    covs = [N for N in snappy.Manifold(base).covers(degree, cover_type="cyclic") if N.num_cusps() == ncusps]
    print("cyclic covers of %s of degree %d with %d cusps: %d" % (base, degree, ncusps, len(covs)), flush=True)
    out = []
    for k, N in enumerate(covs):
        r = analyse(N, "%s~%d#%d" % (base, degree, k)); out.append(r)
        print(json.dumps({x: y for x, y in r.items() if x not in ("spin",)}, default=str)[:900], flush=True)
    json.dump(out, open(HERE / ("cover_%s_%d_%d.json" % (base, degree, ncusps)), "w"), indent=0, default=str)
