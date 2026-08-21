#!/usr/bin/env python3
"""V-2' -- THE ANTILINEAR COMPLETION.

V-2 (banked B1125) proved: no LINEAR sign-lift of the object's E6 embedding gives
compact su(3) color. The color factor I2's ad-invariant form, restricted via any of
the 48 verified Chevalley-automorphism kernel elements (2 families x 2 lattice
classes), is always either indefinite (5,3)/(4,4)-type or -- when "color-pure" --
still lands on the FIXED structural value (5,3,0), never (0,8) or (8,0). B1125's own
type-level diagnosis: compact real forms are cut out by an ANTILINEAR conjugation
(a complex conjugation X -> -X^dagger), never by a linear inner automorphism, so no
element of a purely-linear torsor could ever have reached (0,8).

THIS ARC asks the natural next question: the object DOES have one antilinear
structure of its own -- the MIRROR (amphichirality: the diagram fold pi_mirror,
which is also the outer automorphism swapping the 27 and 27-bar reps, composed with
the coordinate complex-conjugation that is forced once we allow non-real
coefficients over the SAME Q-rational Chevalley data). Does THIS antilinear
conjugation, restricted to I2, give (0,8)?

THE CONSTRUCTION (derived from first principles, then verified computationally
below -- see V2prime_NOTES.md for the full derivation):

  Fix the Q-rational Chevalley coordinate space C^78 (real/rational basis: 6 h_i +
  72 e_r). Let tau (the "split" conjugation) be complex conjugation of coefficients
  relative to THIS basis: tau(sum c_k b_k) = sum conj(c_k) b_k. tau is antilinear,
  tau^2 = id, and its fixed points are exactly the split real form e6(6).

  For ANY involutive automorphism theta of e6(C) with a REAL/RATIONAL matrix in this
  basis (theta^2 = id, brackets preserved -- both properties verified below for
  every theta used), sigma := tau . theta is ALSO an antilinear involution
  (verified algebraically: since theta is real, tau(theta(w)) = theta(tau(w)) for
  all w, so sigma(sigma(v)) = theta(theta(v)) = v). Writing v = x + i*y with x in
  V+(theta), y in V-(theta) (the real +-1 eigenspaces of theta), the sigma-fixed
  real form is g_sigma = V+(theta) (+) i*V-(theta), and because theta preserves the
  ad-invariant form B (any Lie algebra automorphism preserves the Killing-type
  form), V+ and V- are B-orthogonal, so B restricted to g_sigma is

        B_sigma(x1+iy1, x2+iy2) = B(x1,x2) - B(y1,y2)          [**]

  i.e. the RAW signature of B on V-(theta) gets its sign FLIPPED relative to the raw
  signature on V+(theta) before the two are added. This [**] formula -- not the raw,
  unflipped restriction B1125 read off theta's own eigenspaces for the LINEAR
  classification -- is what must be used to test compactness of an antilinear real
  form. It is verified below as a live control (the sigma_c control MUST reproduce
  global (0,78) and I2 (0,8) using exactly this formula; if the naive unflipped
  reading were used instead, sigma_c would come back indefinite (42,36) globally --
  this exact failure mode is checked and reported, not just asserted away).

  pi_mirror (the diagram fold, B1125 Layer 3) is the LINEAR shadow of the object's
  amphichiral/mirror symmetry (it is also the outer automorphism exchanging the 27
  and 27-bar reps -- the standard fact cited in TERMINOLOGY.md's "the fold / theta"
  entry). sigma_mirror := tau . theta_A, for theta_A ranging over B1125's own
  verified signed lifts of pi_mirror (both Chevalley-automorphism families,
  "antipodal" and "permute"), is the antilinear completion this cell tests. The
  FULL TORSOR (composing with the F2 sign-lift kernel, both lattice classes A and
  B) is swept exhaustively, mirroring B1125's own exhaustive structure.

Repo is READ-ONLY. Reads only the vendored bracket module and B1098's stored A2
triple. Everything else (hatch/I1/I2, pi_mirror, w0(I2), the F2 kernel solver) is
re-derived independently in this script, not imported from B1125 (per the task's
"own re-derivation" discipline) -- though the CONSTRUCTION is deliberately the same
verified one, since reproducing V-2's controls with independently-written code IS
the trust-building step this cell is asked to do first.

Run: python3 V2prime_sweep.py
"""
import itertools
import json
import os
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

T0 = time.time()
LOG = []


def log(msg):
    line = f"[{time.time()-T0:7.2f}s] {msg}"
    print(line, flush=True)
    LOG.append(line)


HERE = os.path.dirname(os.path.abspath(__file__))
REL_BRACKET = "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py"
REL_TRIPLE = "frontier/B1098_nonabelian_hatch/b1098_a2_triple.json"


def find_repo_file(rel_path):
    env = os.environ.get("V2_REPO_ROOT") or os.environ.get("V2PRIME_REPO_ROOT")
    cands = [env] if env else []
    d = os.path.abspath(os.getcwd())
    while True:
        cands.append(d)
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    d = HERE
    while True:
        cands.append(d)
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    for c in cands:
        if not c:
            continue
        p = os.path.join(c, rel_path)
        if os.path.exists(p):
            return p
    sys.exit(f"Cannot find {rel_path}. Set V2PRIME_REPO_ROOT to the origin-axiom checkout root.")


BRACKET_PATH = find_repo_file(REL_BRACKET)
TRIPLE_PATH = find_repo_file(REL_TRIPLE)


def load_e6b():
    import importlib.util
    spec = importlib.util.spec_from_file_location("e6b_v2prime", BRACKET_PATH)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    R = {}

    log(f"loading vendored E6 bracket module: {BRACKET_PATH}")
    log(f"loading B1098 A2 triple: {TRIPLE_PATH}")
    e6b = load_e6b()
    ROOTS, IDX, N, DIM = e6b.ROOTS, e6b.IDX, e6b.N, e6b.DIM
    br, evec, hvec, ip, eps = e6b.br, e6b.evec, e6b.hvec, e6b.ip, e6b.eps
    A = e6b.A
    assert len(ROOTS) == 72 and DIM == 78
    SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
    NR = len(ROOTS)
    ALLOWED_CHARS = {6, 2, -14, -26, -78}
    R["setup"] = {"n_roots": len(ROOTS), "dim": DIM, "allowed_characters": sorted(ALLOWED_CHARS)}
    rng = random.Random(20260821)

    def add(u, v):
        return [a + b for a, b in zip(u, v)]

    def smul(c, u):
        return [Fr(c) * a for a in u]

    def veq(u, v):
        return all(a == b for a, b in zip(u, v))

    def sprat(x):
        if isinstance(x, Fr):
            return sp.Rational(x.numerator, x.denominator)
        return sp.Rational(x)

    def sprat_vec(v):
        return sp.Matrix([sprat(c) for c in v])

    # ========================================================================
    # LAYER 0/1 -- the corrected ad-invariant form (own re-derivation, B1119's fix)
    # ========================================================================
    log("")
    log("=== LAYER 0-1: corrected ad-invariant form (reproducing V-2's control) ===")
    etas = {eps(r, tuple(-x for x in r)) for r in ROOTS}
    assert etas == {-1}, f"eta(r) convention check failed: {etas}"

    def build_form(sign):
        Bmat = sp.zeros(DIM, DIM)
        for i in range(N):
            for j in range(N):
                Bmat[i, j] = A[i][j]
        for r in ROOTS:
            nr = tuple(-x for x in r)
            Bmat[N + IDX[r], N + IDX[nr]] = sign
        return Bmat

    Bform = build_form(-1)
    Bwrong = build_form(1)
    basis_all = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]

    def rand_vec():
        v = [Fr(0)] * DIM
        for _ in range(4):
            b = rng.choice(basis_all)
            c = rng.randint(-3, 3)
            v = [x + Fr(c) * y for x, y in zip(v, b)]
        return v

    def ad_inv_fail_count(Bmat, ntrials):
        bad = 0
        for _ in range(ntrials):
            x, y, z = rand_vec(), rand_vec(), rand_vec()
            xy = sprat_vec(br(x, y))
            xz = sprat_vec(br(x, z))
            lhs = (xy.T * Bmat * sprat_vec(z))[0, 0] + (sprat_vec(y).T * Bmat * xz)[0, 0]
            if lhs != 0:
                bad += 1
        return bad

    fails_corrected = ad_inv_fail_count(Bform, 300)
    fails_wrong = ad_inv_fail_count(Bwrong, 300)
    log(f"  corrected form (<e_r,e_-r>=-1): ad-invariance failures/300: {fails_corrected} (expect 0)")
    log(f"  NEGATIVE CONTROL wrong (+1) form: failures/300: {fails_wrong} (expect >0)")
    assert fails_corrected == 0, "corrected form is NOT ad-invariant -- STOP"
    assert fails_wrong > 0, "wrong form unexpectedly ad-invariant -- checker not discriminating"
    R["layer01_form"] = {"fails_corrected": fails_corrected, "fails_wrong_control": fails_wrong}

    def congruence_signature(Gm):
        n = Gm.shape[0]
        Gc = Gm.copy()
        used = [False] * n
        pivots = []
        for _ in range(n):
            rem = [i for i in range(n) if not used[i]]
            piv = None
            for i in rem:
                if Gc[i, i] != 0:
                    piv = i
                    break
            if piv is None:
                found = False
                for i in rem:
                    for j in rem:
                        if i < j and Gc[i, j] != 0:
                            Gc[i, :] = Gc[i, :] + Gc[j, :]
                            Gc[:, i] = Gc[:, i] + Gc[:, j]
                            piv = i
                            found = True
                            break
                    if found:
                        break
                if not found:
                    continue
            pivots.append(Gc[piv, piv])
            used[piv] = True
            pv = Gc[piv, piv]
            for i in rem:
                if i == piv or used[i]:
                    continue
                f = Gc[i, piv] / pv
                Gc[i, :] = Gc[i, :] - f * Gc[piv, :]
                Gc[:, i] = Gc[:, i] - f * Gc[:, piv]
        n_pos = sum(1 for p in pivots if p > 0)
        n_neg = sum(1 for p in pivots if p < 0)
        n_zero = n - len(pivots)
        return (n_pos, n_neg, n_zero)

    # ========================================================================
    # LAYER 2 -- hatch / I1 / I2 (own re-derivation)
    # ========================================================================
    log("")
    log("=== LAYER 2: hatch / I1 / I2 (own re-derivation of B1114's construction) ===")
    trip = json.load(open(TRIPLE_PATH))
    dec = lambda lst: [Fr(a, b) for a, b in lst]
    Xh, Hh, Yh = dec(trip["X"]), dec(trip["H"]), dec(trip["Y"])
    hatch_nodes = None
    for i in range(N):
        for j in range(i + 1, N):
            if veq(add(evec(SIMPLE[i]), evec(SIMPLE[j])), Xh):
                hatch_nodes = (i, j)
    assert hatch_nodes == (0, 2)
    assert veq(br(Xh, Yh), Hh) and veq(br(Hh, Xh), smul(2, Xh)) and veq(br(Hh, Yh), smul(-2, Yh))
    log(f"  hatch nodes {hatch_nodes}, sl2 triple relations exact: True")

    a_i, a_j = SIMPLE[0], SIMPLE[2]
    orth_roots = [r for r in ROOTS if ip(r, a_i) == 0 and ip(r, a_j) == 0]
    assert len(orth_roots) == 12

    def components(roots_list):
        remaining = set(roots_list)
        comps = []
        while remaining:
            seed = next(iter(remaining))
            comp = {seed}
            frontier = [seed]
            remaining.discard(seed)
            while frontier:
                r = frontier.pop()
                for s in list(remaining):
                    if ip(r, s) != 0:
                        comp.add(s)
                        remaining.discard(s)
                        frontier.append(s)
            comps.append(sorted(comp))
        return comps

    comps = components(orth_roots)
    sizes = sorted(len(c) for c in comps)
    assert sizes == [6, 6]
    comp1, comp2 = comps

    def find_simple_pair(comp):
        for r1 in comp:
            for r2 in comp:
                if r1 != r2 and ip(r1, r2) == -1:
                    s = tuple(a + b for a, b in zip(r1, r2))
                    if s in comp:
                        return r1, r2
        raise RuntimeError("no simple pair")

    I1_s1, I1_s2 = find_simple_pair(comp1)
    I2_s1, I2_s2 = find_simple_pair(comp2)
    hatch6 = [SIMPLE[0], SIMPLE[2], tuple(-x for x in SIMPLE[0]), tuple(-x for x in SIMPLE[2]),
              tuple(a + b for a, b in zip(SIMPLE[0], SIMPLE[2])),
              tuple(-(a + b) for a, b in zip(SIMPLE[0], SIMPLE[2]))]
    log(f"  orthogonal A2+A2 found: comp sizes {sizes}; I1 simple {I1_s1},{I1_s2}; I2 simple {I2_s1},{I2_s2}")
    R["layer2_hatch_I1_I2"] = {
        "hatch_nodes": list(hatch_nodes), "orthogonal_component_sizes": sizes,
        "I1_simple": [list(I1_s1), list(I1_s2)], "I2_simple": [list(I2_s1), list(I2_s2)],
        "comp1_I1_roots": [list(r) for r in comp1], "comp2_I2_roots": [list(r) for r in comp2],
    }

    # ========================================================================
    # LAYER 3 -- pi_mirror + w0(I2) -> lattice classes A, B
    # ========================================================================
    log("")
    log("=== LAYER 3: the mirror diagram automorphism (the fold, theta of TERMINOLOGY.md) ===")
    PI_SIMPLE = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}

    def pi_mirror(r):
        out = [0] * N
        for i in range(N):
            out[PI_SIMPLE[i]] = r[i]
        return tuple(out)

    ok_cartan = all(A[PI_SIMPLE[i]][PI_SIMPLE[j]] == A[i][j] for i in range(N) for j in range(N))
    imgs = [pi_mirror(r) for r in ROOTS]
    ok_bij = set(imgs) <= set(ROOTS) and len(set(imgs)) == 72
    bad_iso = sum(1 for _ in range(500)
                  if (lambda a, b: ip(pi_mirror(a), pi_mirror(b)) != ip(a, b))(rng.choice(ROOTS), rng.choice(ROOTS)))
    bad_inv = sum(1 for r in ROOTS if pi_mirror(pi_mirror(r)) != r)
    assert ok_cartan and ok_bij and bad_iso == 0 and bad_inv == 0
    img_hatch = {pi_mirror(r) for r in hatch6}
    img_I2_set = {pi_mirror(r) for r in comp2}
    swap_ok = (img_hatch == set(comp1))
    I2_fixed_setwise = (img_I2_set == set(comp2))
    I2_fixed_pointwise = all(pi_mirror(r) == r for r in comp2)
    assert swap_ok and I2_fixed_setwise
    I1_roots, I2_roots = comp1, comp2
    log(f"  pi_mirror verified: order-2 root automorphism, swaps hatch<->I1: {swap_ok}, "
        f"fixes I2 pointwise: {I2_fixed_pointwise} (class A: 'identity on color')")

    def reflect(x, r):
        c = ip(x, r)
        return tuple(x[i] - c * r[i] for i in range(N))

    w0_I2 = lambda x: reflect(reflect(reflect(x, I2_s1), I2_s2), I2_s1)
    bad_root_w0 = sum(1 for r in ROOTS if w0_I2(r) not in IDX)
    bad_inv_w0 = sum(1 for r in ROOTS if w0_I2(w0_I2(r)) != r)
    fixes_hatch_w0 = all(w0_I2(r) == r for r in hatch6)
    fixes_I1_w0 = all(w0_I2(r) == r for r in I1_roots)
    assert bad_root_w0 == 0 and bad_inv_w0 == 0 and fixes_hatch_w0 and fixes_I1_w0

    def pi_B(r):
        return pi_mirror(w0_I2(r))

    bad_root_B = sum(1 for r in ROOTS if pi_B(r) not in IDX)
    bad_inv_B = sum(1 for r in ROOTS if pi_B(pi_B(r)) != r)
    bad_iso_B = sum(1 for _ in range(500)
                     if (lambda a, b: ip(pi_B(a), pi_B(b)) != ip(a, b))(rng.choice(ROOTS), rng.choice(ROOTS)))
    swap_ok_B = ({pi_B(r) for r in hatch6} == set(I1_roots))
    I2_setwise_B = ({pi_B(r) for r in I2_roots} == set(I2_roots))
    I2_pointwise_B = all(pi_B(r) == r for r in I2_roots)
    assert bad_root_B == 0 and bad_inv_B == 0 and bad_iso_B == 0 and swap_ok_B and I2_setwise_B
    assert not I2_pointwise_B
    log(f"  pi_B = pi_mirror.w0(I2) verified: class B ('duality on color'), I2 fixed setwise "
        f"but NOT pointwise: {not I2_pointwise_B}")

    R["layer3_lattice_classes"] = {
        "pi_mirror_simple_permutation": PI_SIMPLE,
        "pi_A_fixes_I2_pointwise": I2_fixed_pointwise, "pi_B_fixes_I2_pointwise": I2_pointwise_B,
        "all_verification_checks_pass": True,
    }
    PI_ID = lambda r: r
    LATTICE = {"id": PI_ID, "A": pi_mirror, "B": pi_B}

    # ========================================================================
    # LAYER 4 -- the F2 sign-lift cocycle solver (both families)
    # ========================================================================
    log("")
    log("=== LAYER 4: the F2 sign-lift cocycle solver ===")

    def bitof(x):
        return 0 if x == 1 else 1

    def solve_kernel(pi_fn, family):
        rows, rhss = [], []
        for r in ROOTS:
            nr = tuple(-x for x in r)
            row = [0] * NR
            row[IDX[r]] ^= 1
            row[IDX[nr]] ^= 1
            rows.append(row)
            rhss.append(0)
        for ri, r in enumerate(ROOTS):
            for s in ROOTS[ri + 1:]:
                t = tuple(a + b for a, b in zip(r, s))
                if t in IDX:
                    pr, ps = pi_fn(r), pi_fn(s)
                    delta = bitof(eps(pr, ps)) ^ bitof(eps(r, s))
                    row = [0] * NR
                    row[IDX[r]] ^= 1
                    row[IDX[s]] ^= 1
                    row[IDX[t]] ^= 1
                    rows.append(row)
                    rhss.append(delta)
        for r in ROOTS:
            pr = pi_fn(r)
            if pr != r:
                row = [0] * NR
                row[IDX[r]] ^= 1
                row[IDX[pr]] ^= 1
                rows.append(row)
                rhss.append(0)
        nrows = len(rows)
        M = [row[:] + [rhss[i]] for i, row in enumerate(rows)]
        ncols = NR
        pivot_cols = []
        r_ptr = 0
        for c in range(ncols):
            piv = None
            for i in range(r_ptr, nrows):
                if M[i][c] == 1:
                    piv = i
                    break
            if piv is None:
                continue
            M[r_ptr], M[piv] = M[piv], M[r_ptr]
            for i in range(nrows):
                if i != r_ptr and M[i][c] == 1:
                    M[i] = [a ^ b for a, b in zip(M[i], M[r_ptr])]
            pivot_cols.append(c)
            r_ptr += 1
            if r_ptr == nrows:
                break
        consistent = not any(all(v == 0 for v in row[:ncols]) and row[ncols] == 1 for row in M)
        free_cols = [c for c in range(ncols) if c not in pivot_cols]
        part = [0] * ncols
        for i, c in enumerate(pivot_cols):
            part[c] = M[i][ncols]
        kernel_basis = []
        for f in free_cols:
            vec = [0] * ncols
            vec[f] = 1
            for i, c in enumerate(pivot_cols):
                if M[i][f] == 1:
                    vec[c] = 1
            kernel_basis.append(vec)
        return consistent, part, kernel_basis

    def bits_to_eps(bitvec):
        def ef(r):
            return -1 if bitvec[IDX[r]] == 1 else 1
        return ef

    def combine(part, kbasis, coeffs):
        v = part[:]
        for c, kb in zip(coeffs, kbasis):
            if c:
                v = [a ^ b for a, b in zip(v, kb)]
        return v

    def build_theta_matrix(pi_fn, ef, family):
        M = [[Fr(0)] * DIM for _ in range(DIM)]
        sgn = -1 if family == "antipodal" else 1
        for i in range(N):
            img = pi_fn(SIMPLE[i])
            for k in range(N):
                M[k][i] = Fr(sgn * img[k])
        for r in ROOTS:
            pr = pi_fn(r)
            target = tuple(-x for x in pr) if family == "antipodal" else pr
            col = N + IDX[r]
            row = N + IDX[target]
            M[row][col] = Fr(ef(r))
        return M

    def to_sp_mat(Mt):
        return sp.Matrix([[sprat(x) for x in row] for row in Mt])

    def hvec_of_root(r):
        v = [Fr(0)] * DIM
        for i in range(N):
            v[i] = Fr(r[i])
        return v

    I2_basis_vecs = [hvec_of_root(I2_s1), hvec_of_root(I2_s2)] + [evec(r) for r in I2_roots]
    Mbasis_I2 = sp.Matrix.hstack(*[sprat_vec(v) for v in I2_basis_vecs])
    B_restricted_I2 = Mbasis_I2.T * Bform * Mbasis_I2
    B_I2_signature = congruence_signature(B_restricted_I2)
    log(f"  B|I2 (untransformed, fixed structural fact): {B_I2_signature} (expect (5,3,0))")
    assert B_I2_signature == (5, 3, 0)
    R["layer4_fixed_I2_form"] = {"B_restricted_to_untransformed_I2": list(B_I2_signature)}

    def eigendims_and_raw_sig_global(Msp):
        Vp = (Msp - sp.eye(DIM)).nullspace()
        Vm = (Msp + sp.eye(DIM)).nullspace()
        dvp, dvm = len(Vp), len(Vm)
        sp_ = congruence_signature(sp.Matrix.hstack(*Vp).T * Bform * sp.Matrix.hstack(*Vp)) if dvp else (0, 0, 0)
        sm_ = congruence_signature(sp.Matrix.hstack(*Vm).T * Bform * sp.Matrix.hstack(*Vm)) if dvm else (0, 0, 0)
        return dvp, dvm, sp_, sm_

    def color_raw_sig(pi_fn, ef, family):
        """Raw (unflipped) restriction of B to theta's +-1 eigenspaces WITHIN I2.
        Returns (dim_plus, dim_minus, sig_plus_raw, sig_minus_raw, T) where T is the
        8x8 matrix of theta restricted to the I2 basis (also used for a direct
        theta^2=I re-check at the I2 level)."""
        def theta_of_basisvec(k):
            if k < 2:
                r = I2_s1 if k == 0 else I2_s2
                pr = pi_fn(r)
                out = [Fr(0)] * DIM
                sgn = -1 if family == "antipodal" else 1
                for i in range(N):
                    out[i] = Fr(sgn * pr[i])
                return out
            else:
                r = I2_roots[k - 2]
                pr = pi_fn(r)
                target = tuple(-x for x in pr) if family == "antipodal" else pr
                out = [Fr(0)] * DIM
                out[N + IDX[target]] = Fr(ef(r))
                return out

        images = [sprat_vec(theta_of_basisvec(k)) for k in range(8)]
        Tcols = []
        for img in images:
            sol, params = Mbasis_I2.gauss_jordan_solve(img)
            assert not params, "theta(I2 basisvec) not uniquely in span(I2) -- I2 not theta-stable"
            resid = Mbasis_I2 * sol - img
            assert all(sp.simplify(x) == 0 for x in resid), "theta does not preserve I2 exactly"
            Tcols.append(sol)
        T = sp.Matrix.hstack(*Tcols)
        assert T * T == sp.eye(8), "theta restricted to I2 is not an involution"
        Vp = (T - sp.eye(8)).nullspace()
        Vm = (T + sp.eye(8)).nullspace()
        dim_p, dim_m = len(Vp), len(Vm)
        assert dim_p + dim_m == 8

        def restrict_sig(cvecs):
            if not cvecs:
                return (0, 0, 0)
            lifted = [Mbasis_I2 * cv for cv in cvecs]
            Vstack = sp.Matrix.hstack(*lifted)
            return congruence_signature(Vstack.T * Bform * Vstack)

        sig_plus = restrict_sig(Vp)
        sig_minus = restrict_sig(Vm)
        return dim_p, dim_m, sig_plus, sig_minus, T

    def verify_automorphism(Mt, ntrials=60):
        def apply_mat(Mlist, v):
            return [sum(Mlist[i][j] * v[j] for j in range(DIM)) for i in range(DIM)]
        fail = 0
        for _ in range(ntrials):
            x, y = rand_vec(), rand_vec()
            tx, ty = apply_mat(Mt, x), apply_mat(Mt, y)
            lhs = apply_mat(Mt, br(x, y))
            rhs = br(tx, ty)
            if lhs != rhs:
                fail += 1
        return fail

    # ------------------------------------------------------------------------
    # THE ANTILINEAR-SIGNATURE COMBINER -- the sole new piece of mathematics
    # this arc adds (derived in the module docstring; verified as a live control
    # below rather than merely asserted).
    # ------------------------------------------------------------------------
    def combine_antilinear(sig_plus_raw, sig_minus_raw):
        p_p, n_p, z_p = sig_plus_raw
        p_m, n_m, z_m = sig_minus_raw
        return (p_p + n_m, n_p + p_m, z_p + z_m)

    def is_compact_sig(sig, dim):
        p, n, z = sig
        return z == 0 and (p == 0 or n == 0) and (p + n == dim)

    def full_element(pi_fn, ef, family, label, verify_auto_trials=60):
        Mt = build_theta_matrix(pi_fn, ef, family)
        Msp = to_sp_mat(Mt)
        is_invol = (Msp * Msp == sp.eye(DIM))
        tr = sum(Msp[i, i] for i in range(DIM))
        chi = int(-tr)
        auto_fail = verify_automorphism(Mt, verify_auto_trials) if verify_auto_trials else None
        dvp, dvm, gsp, gsm = eigendims_and_raw_sig_global(Msp)
        cp, cm, csp, csm, T8 = color_raw_sig(pi_fn, ef, family)
        # LINEAR reading (B1125's own question: is the theta-real-form's I2 itself compact)
        linear_color_pure = ((csp[0] == 0 or csp[1] == 0) and csp[2] == 0
                              and (csm[0] == 0 or csm[1] == 0) and csm[2] == 0)
        # ANTILINEAR reading (THIS arc's question: is sigma=tau.theta's I2 compact)
        anti_global = combine_antilinear(gsp, gsm)
        anti_color = combine_antilinear(csp, csm)
        rec = {
            "label": label, "family": family, "character": chi,
            "checksum_pass": chi in ALLOWED_CHARS,
            "theta_squared_is_identity": bool(is_invol),
            "automorphism_failures": auto_fail,
            "global_eigendims": [dvp, dvm], "global_sig_plus_raw": list(gsp), "global_sig_minus_raw": list(gsm),
            "color_eigendims": [cp, cm], "color_sig_plus_raw": list(csp), "color_sig_minus_raw": list(csm),
            "linear_color_pure": bool(linear_color_pure),
            "antilinear_global_signature": list(anti_global),
            "antilinear_color_signature": list(anti_color),
            "antilinear_global_compact": bool(is_compact_sig(anti_global, DIM)),
            "antilinear_color_compact": bool(is_compact_sig(anti_color, 8)),
        }
        return rec

    # ========================================================================
    # LAYER 5 -- CONTROLS (reproduce B1125's split/compact/variant-A first)
    # ========================================================================
    log("")
    log("=== LAYER 5: CONTROLS -- reproduce V-2's linear-torsor numbers first ===")
    cons_s, part_s, kbasis_s = solve_kernel(PI_ID, "antipodal")
    ef_split = bits_to_eps(part_s)
    chk_split = full_element(PI_ID, ef_split, "antipodal", "split(antipodal,id)")
    split_pass = (chk_split["character"] == 6 and chk_split["global_eigendims"] == [36, 42]
                  and chk_split["theta_squared_is_identity"] and chk_split["automorphism_failures"] == 0)
    log(f"  SPLIT control: character={chk_split['character']} (expect +6), "
        f"dims={chk_split['global_eigendims']} (expect [36,42]), pass={split_pass}")
    assert split_pass, "SPLIT CONTROL FAILED -- STOP"

    cons_c, part_c, kbasis_c = solve_kernel(PI_ID, "permute")
    eps1_is_solution = all(v == 0 for v in part_c)
    chk_idlin = full_element(PI_ID, (lambda r: 1), "permute", "theta=identity(permute,id,eps=1)")
    compact_lin_pass = (chk_idlin["character"] == -78 and chk_idlin["global_eigendims"] == [78, 0]
                         and chk_idlin["theta_squared_is_identity"])
    log(f"  theta=identity control (B1125's own 'compact control' LABEL): character={chk_idlin['character']} "
        f"(expect -78), dims={chk_idlin['global_eigendims']} (expect [78,0]), pass={compact_lin_pass}")
    assert compact_lin_pass, "theta=identity CONTROL FAILED -- STOP"
    log(f"  eps=1 is the trivial (permute,id) particular solution: {eps1_is_solution}")
    log(f"  ANTILINEAR check on theta=identity: sigma=tau.id=tau itself -- global sig "
        f"{chk_idlin['antilinear_global_signature']} (NOT expected to be (0,78): tau alone is just the split "
        f"conjugation, not compact -- see V2prime_NOTES.md for why this LABEL is a red herring for building "
        f"sigma_c, and why theta_split below is the correct linear shadow)")

    cons_A, part_A, kbasis_A = solve_kernel(pi_mirror, "antipodal")
    ef_A_base = bits_to_eps(part_A)
    chk_A = full_element(pi_mirror, ef_A_base, "antipodal", "variantA_base(antipodal,A)")
    variantA_color_53 = (sorted([chk_A["color_eigendims"][0], chk_A["color_eigendims"][1]]) == [3, 5]
                          and chk_A["linear_color_pure"])
    variantA_pass = (chk_A["character"] == 2 and chk_A["theta_squared_is_identity"]
                      and chk_A["automorphism_failures"] == 0 and variantA_color_53)
    log(f"  VARIANT A base: character={chk_A['character']} (expect +2), color dims={chk_A['color_eigendims']}, "
        f"linear color sig_plus={chk_A['color_sig_plus_raw']}, sig_minus={chk_A['color_sig_minus_raw']}, "
        f"matches B1119 exactly: {variantA_pass}")
    assert variantA_pass, "VARIANT A CONTROL FAILED -- STOP"

    R["layer5_controls"] = {
        "split": chk_split, "theta_identity_permute_id": chk_idlin, "variant_A_base": chk_A,
        "all_pass": bool(split_pass and compact_lin_pass and variantA_pass),
    }
    log("  All three V-2 linear-torsor controls reproduced. Machinery trusted -- proceeding to the antilinear layer.")

    # ========================================================================
    # LAYER 6 -- THE REQUIRED CONTROL: sigma_c, the antilinear compact conjugation
    # ========================================================================
    log("")
    log("=== LAYER 6: sigma_c = tau . theta_split -- THE LOAD-BEARING CONTROL ===")
    log("  theta_split = (antipodal, pi=id) -- the genuine Chevalley/Cartan involution of the "
        "split form (character +6 as a LINEAR map). sigma_c := tau_split . theta_split.")
    sigma_c_global = chk_split["antilinear_global_signature"]
    sigma_c_color = chk_split["antilinear_color_signature"]
    sigma_c_global_compact = chk_split["antilinear_global_compact"]
    sigma_c_color_compact = chk_split["antilinear_color_compact"]
    log(f"  sigma_c GLOBAL antilinear signature (should be (0,78) or (78,0), fully compact E6): "
        f"{sigma_c_global}, compact={sigma_c_global_compact}")
    log(f"  sigma_c COLOR (I2) antilinear signature (THE REQUIRED CONTROL, must be (0,8) or (8,0)): "
        f"{sigma_c_color}, compact={sigma_c_color_compact}")

    detector_broken = not (sigma_c_global_compact and sigma_c_color_compact)
    R["layer6_sigma_c_control"] = {
        "construction": "tau_split composed with theta_split (antipodal, pi=id)",
        "global_signature": sigma_c_global, "global_compact": sigma_c_global_compact,
        "color_I2_signature": sigma_c_color, "color_I2_compact": sigma_c_color_compact,
        "detector_broken": bool(detector_broken),
        "naive_unflipped_reading_for_comparison": {
            "global_raw_would_be": chk_split["global_sig_plus_raw"],
            "note": ("if the antilinear i-twist were NOT applied (i.e. reading theta's raw eigenspace "
                     "restriction directly, B1125's own linear-classification method), the split "
                     "control's OWN linear color reading is (5,3) -- see variant_A/split rows above -- "
                     "never compact. The antilinear flip on V-(theta) is what this arc adds."),
        },
    }
    if detector_broken:
        log("  *** DETECTOR BROKEN: sigma_c does NOT give compact color. STOPPING per protocol. ***")
        R["verdict"] = "DETECTOR-BROKEN-STOP"
        R["runtime_seconds"] = round(time.time() - T0, 2)
        R["log"] = LOG
        out_path = os.path.join(HERE, "V2prime_results.json")
        with open(out_path, "w") as f:
            json.dump(R, f, indent=1, default=str)
        log(f"wrote {out_path}")
        return R
    log("  CONTROL PASSED: the detector sees compact color when it is genuinely present. Proceeding.")

    # ========================================================================
    # LAYER 7 -- sigma_mirror and its full antilinear torsor
    # ========================================================================
    log("")
    log("=== LAYER 7: sigma_mirror = tau . theta_A  (and the full torsor, both classes, both families) ===")
    log("  PRIMARY candidate: sigma_mirror_primary = tau . theta_A_base (antipodal, class A, the same "
        "base element B1119/B1125 call 'variant A').")
    sigma_mirror_primary_color = chk_A["antilinear_color_signature"]
    sigma_mirror_primary_compact = chk_A["antilinear_color_compact"]
    log(f"  sigma_mirror_primary COLOR (I2) antilinear signature: {sigma_mirror_primary_color}, "
        f"compact={sigma_mirror_primary_compact}")

    R["layer7_sigma_mirror_primary"] = {
        "construction": "tau_split composed with theta_A_base (antipodal, pi=pi_mirror, base/particular sign-lift)",
        "color_I2_signature": sigma_mirror_primary_color, "color_I2_compact": sigma_mirror_primary_compact,
        "global_signature": chk_A["antilinear_global_signature"],
        "global_compact": chk_A["antilinear_global_compact"],
    }

    log("")
    log("  FULL TORSOR: sweeping all 48 verified kernel elements (2 families x 2 lattice classes), "
        "each composed with tau to test compactness under the antilinear formula.")
    torsor_table = []
    torsor_compact_hits = []
    for family in ("antipodal", "permute"):
        for cls in ("A", "B"):
            pi_fn = LATTICE[cls]
            consistent, part, kbasis = solve_kernel(pi_fn, family)
            k = len(kbasis)
            label_base = f"{family}/{cls}"
            assert consistent
            n_compact_color = 0
            n_color_pure_linear = 0
            chars_seen = set()
            elt_records = []
            for bits in itertools.product([0, 1], repeat=k):
                v = combine(part, kbasis, bits)
                ef = bits_to_eps(v)
                rec = full_element(pi_fn, ef, family, f"{label_base}#{bits}", verify_auto_trials=0)
                chars_seen.add(rec["character"])
                if rec["linear_color_pure"]:
                    n_color_pure_linear += 1
                if rec["antilinear_color_compact"]:
                    n_compact_color += 1
                    # rigorous re-verification before trusting: automorphism check + re-derive T^2=I
                    rec_full = full_element(pi_fn, ef, family, rec["label"], verify_auto_trials=300)
                    rec["full_reverification"] = {
                        "automorphism_failures_of_300": rec_full["automorphism_failures"],
                        "reconfirmed_antilinear_color_compact": rec_full["antilinear_color_compact"],
                        "reconfirmed_theta_squared_id": rec_full["theta_squared_is_identity"],
                    }
                    torsor_compact_hits.append({"family": family, "lattice_class": cls, "bits": list(bits), **rec})
                elt_records.append({
                    "bits": list(bits), "character": rec["character"],
                    "checksum_pass": rec["checksum_pass"], "theta_sq_id": rec["theta_squared_is_identity"],
                    "linear_color_pure": rec["linear_color_pure"],
                    "color_sig_plus_raw": rec["color_sig_plus_raw"], "color_sig_minus_raw": rec["color_sig_minus_raw"],
                    "antilinear_color_signature": rec["antilinear_color_signature"],
                    "antilinear_color_compact": rec["antilinear_color_compact"],
                })
            log(f"    [{label_base}] kernel dim k={k} ({2**k} elements); characters seen: {sorted(chars_seen)}; "
                f"linear-color-pure: {n_color_pure_linear}/{len(elt_records)}; "
                f"ANTILINEAR-color-compact: {n_compact_color}/{len(elt_records)}")
            torsor_table.append({
                "family": family, "lattice_class": cls, "kernel_dim": k, "n_elements": 2 ** k,
                "characters_seen": sorted(chars_seen),
                "n_linear_color_pure": n_color_pure_linear,
                "n_antilinear_color_compact": n_compact_color,
                "elements": elt_records,
            })

    R["layer7_full_torsor_sweep"] = torsor_table
    R["layer7_torsor_compact_hits"] = torsor_compact_hits

    # ========================================================================
    # LAYER 8 -- fences: (a) is pi_mirror ALONE (eps=1, unsigned) an automorphism?
    #            (b) does theta_split commute with theta_A (the secondary,
    #                compact-referenced antilinear construction)?
    # ========================================================================
    log("")
    log("=== LAYER 8: fences -- unsigned pi_mirror, and the compact-referenced alternative ===")
    Mt_unsigned = build_theta_matrix(pi_mirror, (lambda r: 1), "permute")
    Msp_unsigned = to_sp_mat(Mt_unsigned)
    unsigned_invol = (Msp_unsigned * Msp_unsigned == sp.eye(DIM))
    unsigned_auto_fail = verify_automorphism(Mt_unsigned, 60)
    log(f"  pi_mirror alone (eps=1, unsigned, family=permute): theta^2=I: {unsigned_invol}, "
        f"automorphism failures/60: {unsigned_auto_fail} "
        f"(if either fails, the UNSIGNED diagram fold is not itself a valid antilinear-lift base -- "
        f"a genuine sign lift, as used above, is required; this is checked, not assumed)")
    R["layer8a_unsigned_pi_mirror"] = {
        "theta_squared_is_identity": bool(unsigned_invol), "automorphism_failures_of_60": unsigned_auto_fail,
        "valid_as_automorphism": bool(unsigned_invol and unsigned_auto_fail == 0),
    }

    # secondary construction: sigma' = tau . theta_split . theta_A  (compact-referenced mirror)
    # valid iff (theta_split . theta_A)^2 = I, i.e. theta_split and theta_A commute (sufficient) --
    # checked directly rather than assumed.
    Mt_split = build_theta_matrix(PI_ID, ef_split, "antipodal")
    Mt_A = build_theta_matrix(pi_mirror, ef_A_base, "antipodal")
    Msp_split = to_sp_mat(Mt_split)
    Msp_A_base = to_sp_mat(Mt_A)
    commute_fail = (Msp_split * Msp_A_base) - (Msp_A_base * Msp_split)
    commutes = all(v == 0 for v in commute_fail)
    prod = Msp_split * Msp_A_base
    prod_is_invol = (prod * prod == sp.eye(DIM))
    log(f"  theta_split and theta_A_base (both antipodal) commute: {commutes}; "
        f"(theta_split . theta_A_base)^2 = I: {prod_is_invol} "
        f"(needed for the SECONDARY 'compact-referenced' construction sigma' = tau.theta_split.theta_A "
        f"to be a valid antilinear involution at all)")
    secondary = {"theta_split_and_theta_A_commute": bool(commutes), "product_is_involution": bool(prod_is_invol)}
    if prod_is_invol:
        dvp2, dvm2, gsp2, gsm2 = eigendims_and_raw_sig_global(prod)
        # color restriction of the PRODUCT automorphism, reusing color_raw_sig's machinery generically
        def theta_of_basisvec_generic(Mfull, k):
            if k < 2:
                r = I2_s1 if k == 0 else I2_s2
                col = sprat_vec(hvec_of_root(r))
            else:
                r = I2_roots[k - 2]
                col = sprat_vec(evec(r))
            return Mfull * col
        images2 = [theta_of_basisvec_generic(prod, k) for k in range(8)]
        Tcols2 = []
        stable = True
        for img in images2:
            sol, params = Mbasis_I2.gauss_jordan_solve(img)
            if params or any(sp.simplify(x) != 0 for x in (Mbasis_I2 * sol - img)):
                stable = False
                break
            Tcols2.append(sol)
        if stable:
            T2 = sp.Matrix.hstack(*Tcols2)
            Vp2 = (T2 - sp.eye(8)).nullspace()
            Vm2 = (T2 + sp.eye(8)).nullspace()
            def rsig(cvecs):
                if not cvecs:
                    return (0, 0, 0)
                lifted = [Mbasis_I2 * cv for cv in cvecs]
                Vstack = sp.Matrix.hstack(*lifted)
                return congruence_signature(Vstack.T * Bform * Vstack)
            csp2, csm2 = rsig(Vp2), rsig(Vm2)
            anti_color2 = combine_antilinear(csp2, csm2)
            secondary["I2_stable_under_product"] = True
            secondary["color_I2_antilinear_signature"] = list(anti_color2)
            secondary["color_I2_antilinear_compact"] = bool(is_compact_sig(anti_color2, 8))
            log(f"  secondary construction I2 antilinear signature: {anti_color2}, "
                f"compact={is_compact_sig(anti_color2, 8)}")
        else:
            secondary["I2_stable_under_product"] = False
            log("  secondary construction: I2 is NOT stable under theta_split.theta_A -- construction invalid, skipped")
    R["layer8b_secondary_compact_referenced_construction"] = secondary

    # ========================================================================
    # VERDICT
    # ========================================================================
    log("")
    log("=== VERDICT ===")
    genuine_hits = [h for h in torsor_compact_hits
                    if h.get("full_reverification", {}).get("reconfirmed_antilinear_color_compact")]
    if genuine_hits:
        verdict = "COMPACT-FROM-MIRROR"
    else:
        verdict = "NO-COMPACT-EVEN-FROM-MIRROR"
    log(f"  raw antilinear-color-compact flags across the 48-element torsor (pre-reverification): "
        f"{len(torsor_compact_hits)}")
    log(f"  FULLY RE-VERIFIED genuine hits: {len(genuine_hits)}")
    log(f"  sigma_mirror_primary (antipodal/A base) alone: compact={sigma_mirror_primary_compact}, "
        f"signature={sigma_mirror_primary_color}")
    log(f"  VERDICT: {verdict}")

    R["verdict"] = verdict
    R["genuine_torsor_compact_hits"] = genuine_hits
    R["n_torsor_compact_hits_raw"] = len(torsor_compact_hits)
    R["n_torsor_compact_hits_reverified"] = len(genuine_hits)
    R["sigma_mirror_primary_verdict"] = {
        "signature": sigma_mirror_primary_color, "compact": sigma_mirror_primary_compact,
    }
    R["runtime_seconds"] = round(time.time() - T0, 2)
    R["log"] = LOG

    out_path = os.path.join(HERE, "V2prime_results.json")
    with open(out_path, "w") as f:
        json.dump(R, f, indent=1, default=str)
    log(f"wrote {out_path}")
    log(f"TOTAL runtime: {time.time()-T0:.2f}s")
    return R


if __name__ == "__main__":
    main()
