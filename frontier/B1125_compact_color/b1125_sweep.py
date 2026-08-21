#!/usr/bin/env python3
"""V-2 -- THE COMPACT-COLOR KERNEL SWEEP.

Question (C-AR1, from B1119): the sign-lifts realizing so(3,1) (+) su(3) inside a
real form of E6 form a torsor over a finite F2-kernel. Does ANY kernel element, over
BOTH lattice classes, give a real form with COMPACT su(3) color?

This script is a from-scratch, independent reconstruction of the sign-lift machinery
(the outside bench's B1118/B1119 code is not in-repo -- only its prose memos and
captured stdout survive). Every piece is derived and verified here:

  1. THE CORRECTED AD-INVARIANT FORM (B1119's fix: <e_r,e_-r> = -1, not +1).
     Verified ad-invariant on 300 random triples; the WRONG (+1) form is verified to
     FAIL ad-invariance (a negative control reproducing B1119's own bug detection).

  2. HATCH / I1 / I2 (own re-derivation of B1114's construction: the hatch A2, the
     orthogonal A2+A2 = I1 (+) I2, I1 = the OTHER Lorentz factor, I2 = the joint
     centralizer = color). Uses only the vendored bracket + B1098's stored triple as
     read-only inputs.

  3. THE MIRROR DIAGRAM AUTOMORPHISM pi_mirror of E6 (0<->5, 2<->4, fix 1,3 in this
     module's Bourbaki-like labeling), verified as a genuine order-2 root-system
     automorphism (isometry, involution, roots->roots). COMPUTATIONALLY VERIFIED to
     swap hatch's A2 with I1's A2 exactly, and fix I2 setwise (in fact pointwise).
     This is LATTICE CLASS A ("identity on color").

  4. w0(I2), the longest Weyl element of I2's OWN A2 factor, composed with
     pi_mirror to give LATTICE CLASS B ("duality on color") -- verified to be a
     DIFFERENT genuine order-2 root-system automorphism that ALSO swaps hatch<->I1
     but acts nontrivially (not pointwise) within I2.

  5. For EACH of two Chevalley-basis-automorphism ansatze ("Family 1", antipodal-
     type: theta(h)=-pi(h), theta(e_r)=eps(r).e_{-pi(r)} -- generalizes the standard
     Cartan involution of the split form; and "Family 2", permute-type:
     theta(h)=+pi(h), theta(e_r)=eps(r).e_{pi(r)} -- generalizes the trivial/compact-
     commuting twists) CROSSED with each of the two pi's (A, B): solve the F2 sign-
     lift cocycle for eps: (72 roots) -> {+-1}, INCLUDING the theta^2=id constraint
     (found by direct falsification to be REQUIRED beyond the base cocycle+evenness
     conditions -- some naive "solutions" of the cocycle alone are NOT involutions).
     Enumerate the FULL kernel (a finite (Z/2)^k), build every theta EXACTLY, verify
     theta^2=I and the full bracket-automorphism property, compute the character via
     exact trace, apply the classification checksum (character in
     {+6,+2,-14,-26,-78}), compute the I2-restricted (color) signature, and check
     PURITY (does B restrict to a one-sided/definite form on each of I2's theta-
     eigenspaces? -- found to be a NECESSARY second-level check: a character can pass
     the classification checksum while the underlying theta is not a genuine, cleanly
     split Cartan involution -- an indefinite/impure restriction means the reading is
     not a valid real-form realization even though the trace-character alone looks
     legal).

  6. CONTROLS reproduced first: split (Family 1, pi=id) -> character +6, dims
     (36,42), matching literature E6(6) exactly; compact (Family 2, pi=id,
     eps=1, i.e. theta=identity) -> character -78; variant A (Family 1, pi=A,
     properly theta^2=id-filtered kernel) -> character +2, color signature (5,3),
     matching B1118/B1119's reported variant A EXACTLY (both the character and the
     exact color signature).

Repo is READ-ONLY. This script and its outputs live entirely in this scratchpad
directory. Machine-independent: reads the vendored bracket module and stored A2
triple via env var override (V2_REPO_ROOT) or relative-path fallback (walking up
from this file's location), never a hardcoded absolute path in the logic.

Run: python3 V2_sweep.py
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
    env = os.environ.get("V2_REPO_ROOT")
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
    sys.exit(f"Cannot find {rel_path}. Set V2_REPO_ROOT to the origin-axiom checkout root.")


BRACKET_PATH = find_repo_file(REL_BRACKET)
TRIPLE_PATH = find_repo_file(REL_TRIPLE)


def load_e6b():
    import importlib.util
    spec = importlib.util.spec_from_file_location("e6b_v2", BRACKET_PATH)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ============================================================================
def main():
    R = {}  # -> V2_results.json

    log(f"loading vendored E6 bracket module: {BRACKET_PATH}")
    e6b = load_e6b()
    ROOTS, IDX, N, DIM = e6b.ROOTS, e6b.IDX, e6b.N, e6b.DIM
    br, evec, hvec, ip, eps = e6b.br, e6b.evec, e6b.hvec, e6b.ip, e6b.eps
    A = e6b.A
    assert len(ROOTS) == 72 and DIM == 78
    SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
    NR = len(ROOTS)
    ALLOWED_CHARS = {6, 2, -14, -26, -78}
    log(f"  E6 loaded: {len(ROOTS)} roots, dim {DIM}")
    R["setup"] = {"n_roots": len(ROOTS), "dim": DIM, "allowed_characters": sorted(ALLOWED_CHARS)}

    def add(u, v):
        return [a + b for a, b in zip(u, v)]

    def smul(c, u):
        return [Fr(c) * a for a in u]

    def is_zero(v):
        return all(x == 0 for x in v)

    def veq(u, v):
        return all(a == b for a, b in zip(u, v))

    def sprat(x):
        if isinstance(x, Fr):
            return sp.Rational(x.numerator, x.denominator)
        return sp.Rational(x)

    def sprat_vec(v):
        return sp.Matrix([sprat(c) for c in v])

    # ========================================================================
    # LAYER 0 -- eta(r) = eps(r,-r) check + eps(-a,-b)=eps(a,b) identity
    # ========================================================================
    log("")
    log("=== LAYER 0: paper-convention checks on the vendored eps cocycle ===")
    etas = {eps(r, tuple(-x for x in r)) for r in ROOTS}
    log(f"  eta(r)=eps(r,-r) over all 72 roots: {etas} (expect {{-1}}, the paper's "
        f"convention [e_r,e_-r]=-h_r)")
    assert etas == {-1}
    rng = random.Random(20260821)
    bad = 0
    for _ in range(500):
        a, b = rng.choice(ROOTS), rng.choice(ROOTS)
        na, nb = tuple(-x for x in a), tuple(-x for x in b)
        if eps(na, nb) != eps(a, b):
            bad += 1
    log(f"  eps(-a,-b)==eps(a,b) identity (500 random pairs): {bad} failures")
    assert bad == 0
    R["layer0_cocycle_checks"] = {"eta_values": sorted(etas), "eps_negation_identity_failures": bad}

    # ========================================================================
    # LAYER 1 -- THE CORRECTED AD-INVARIANT FORM (B1119's fix)
    # ========================================================================
    log("")
    log("=== LAYER 1: the corrected ad-invariant form ===")

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
    log(f"  CORRECTED form (<e_r,e_-r>=-1): ad-invariance failures on 300 random triples: {fails_corrected}")
    log(f"  NEGATIVE CONTROL -- WRONG form (<e_r,e_-r>=+1): failures on 300 triples: {fails_wrong} "
        f"(expect >0 -- confirms our checker catches the known B1119 bug)")
    assert fails_corrected == 0, "corrected form is NOT ad-invariant -- STOP, broken instrument"
    assert fails_wrong > 0, "wrong form unexpectedly passed ad-invariance -- checker is not discriminating"
    R["layer1_corrected_form"] = {
        "ad_invariance_failures_corrected_form": fails_corrected,
        "ad_invariance_failures_WRONG_form_negative_control": fails_wrong,
        "pass": fails_corrected == 0 and fails_wrong > 0,
    }

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
    # LAYER 2 -- hatch / I1 / I2 (own re-derivation of B1114)
    # ========================================================================
    log("")
    log("=== LAYER 2: hatch / I1 / I2 (own code, B1114's construction) ===")
    trip = json.load(open(TRIPLE_PATH))
    dec = lambda lst: [Fr(a, b) for a, b in lst]
    Xh, Hh, Yh = dec(trip["X"]), dec(trip["H"]), dec(trip["Y"])
    hatch_nodes = None
    for i in range(N):
        for j in range(i + 1, N):
            if veq(add(evec(SIMPLE[i]), evec(SIMPLE[j])), Xh):
                hatch_nodes = (i, j)
    log(f"  hatch nodes: {hatch_nodes} (expect (0,2))")
    assert hatch_nodes == (0, 2)
    ok_XY = veq(br(Xh, Yh), Hh)
    ok_HX = veq(br(Hh, Xh), smul(2, Xh))
    ok_HY = veq(br(Hh, Yh), smul(-2, Yh))
    assert ok_XY and ok_HX and ok_HY
    log(f"  hatch sl2 triple relations exact: {ok_XY and ok_HX and ok_HY}")

    a_i, a_j = SIMPLE[0], SIMPLE[2]
    orth_roots = [r for r in ROOTS if ip(r, a_i) == 0 and ip(r, a_j) == 0]
    log(f"  roots orthogonal to hatch's A2: {len(orth_roots)} (expect 12)")
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
    log(f"  orthogonal-subsystem component sizes: {sizes} (expect [6,6])")
    assert sizes == [6, 6]
    comp1, comp2 = comps  # will confirm comp1=I1 (paired w/ hatch), comp2=I2 (color) below

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
    log(f"  I1 simple pair: {I1_s1}, {I1_s2}")
    log(f"  I2 simple pair: {I2_s1}, {I2_s2}")
    R["layer2_hatch_I1_I2"] = {
        "hatch_nodes": list(hatch_nodes), "triple_relations_exact": True,
        "orthogonal_component_sizes": sizes,
        "I1_simple": [list(I1_s1), list(I1_s2)], "I2_simple": [list(I2_s1), list(I2_s2)],
        "comp1_I1_roots": [list(r) for r in comp1], "comp2_I2_roots": [list(r) for r in comp2],
    }

    # ========================================================================
    # LAYER 3 -- pi_mirror (the E6 diagram automorphism) + w0(I2) -> pi_A, pi_B
    # ========================================================================
    log("")
    log("=== LAYER 3: the mirror diagram automorphism + the two lattice classes ===")
    PI_SIMPLE = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}

    def pi_mirror(r):
        out = [0] * N
        for i in range(N):
            out[PI_SIMPLE[i]] = r[i]
        return tuple(out)

    ok_cartan = all(A[PI_SIMPLE[i]][PI_SIMPLE[j]] == A[i][j] for i in range(N) for j in range(N))
    imgs = [pi_mirror(r) for r in ROOTS]
    ok_bij = set(imgs) <= set(ROOTS) and len(set(imgs)) == 72
    bad_iso = 0
    for _ in range(500):
        a, b = rng.choice(ROOTS), rng.choice(ROOTS)
        if ip(pi_mirror(a), pi_mirror(b)) != ip(a, b):
            bad_iso += 1
    bad_inv = sum(1 for r in ROOTS if pi_mirror(pi_mirror(r)) != r)
    log(f"  pi_mirror: preserves Cartan matrix={ok_cartan}, roots->roots bijection={ok_bij}, "
        f"isometry failures={bad_iso}, involution failures={bad_inv}")
    assert ok_cartan and ok_bij and bad_iso == 0 and bad_inv == 0

    img_hatch = {pi_mirror(r) for r in hatch6}
    img_I2_set = {pi_mirror(r) for r in comp2}
    swap_ok = (img_hatch == set(comp1))
    I2_fixed_setwise = (img_I2_set == set(comp2))
    I2_fixed_pointwise = all(pi_mirror(r) == r for r in comp2)
    log(f"  pi_mirror(hatch) == I1 (comp1) exactly: {swap_ok}")
    log(f"  pi_mirror(I2) == I2 setwise: {I2_fixed_setwise}; pointwise: {I2_fixed_pointwise}")
    assert swap_ok and I2_fixed_setwise
    # relabel so comp1 IS "I1" (confirmed paired with hatch by the mirror)
    I1_roots, I2_roots = comp1, comp2
    log("  CLASS A (pi_A = pi_mirror): 'identity on color' -- I2 fixed pointwise")

    def reflect(x, r):
        c = ip(x, r)
        return tuple(x[i] - c * r[i] for i in range(N))

    w0_I2 = lambda x: reflect(reflect(reflect(x, I2_s1), I2_s2), I2_s1)
    bad_root_w0 = sum(1 for r in ROOTS if w0_I2(r) not in IDX)
    bad_inv_w0 = sum(1 for r in ROOTS if w0_I2(w0_I2(r)) != r)
    fixes_hatch_w0 = all(w0_I2(r) == r for r in hatch6)
    fixes_I1_w0 = all(w0_I2(r) == r for r in I1_roots)
    log(f"  w0(I2): roots->roots fail={bad_root_w0}, involution fail={bad_inv_w0}, "
        f"fixes hatch pointwise={fixes_hatch_w0}, fixes I1 pointwise={fixes_I1_w0}")
    assert bad_root_w0 == 0 and bad_inv_w0 == 0 and fixes_hatch_w0 and fixes_I1_w0

    def pi_B(r):
        return pi_mirror(w0_I2(r))

    bad_root_B = sum(1 for r in ROOTS if pi_B(r) not in IDX)
    bad_inv_B = sum(1 for r in ROOTS if pi_B(pi_B(r)) != r)
    bad_iso_B = 0
    for _ in range(500):
        a, b = rng.choice(ROOTS), rng.choice(ROOTS)
        if ip(pi_B(a), pi_B(b)) != ip(a, b):
            bad_iso_B += 1
    swap_ok_B = ({pi_B(r) for r in hatch6} == set(I1_roots))
    I2_setwise_B = ({pi_B(r) for r in I2_roots} == set(I2_roots))
    I2_pointwise_B = all(pi_B(r) == r for r in I2_roots)
    log(f"  pi_B = pi_mirror . w0(I2): roots->roots fail={bad_root_B}, involution fail={bad_inv_B}, "
        f"isometry fail={bad_iso_B}")
    log(f"  pi_B(hatch)==I1: {swap_ok_B}; pi_B(I2)==I2 setwise: {I2_setwise_B}, pointwise: {I2_pointwise_B} "
        f"(expect NOT pointwise -- 'duality on color')")
    assert bad_root_B == 0 and bad_inv_B == 0 and bad_iso_B == 0 and swap_ok_B and I2_setwise_B
    assert not I2_pointwise_B, "pi_B should act nontrivially on I2 (the duality twist) -- construction error"
    log("  CLASS B (pi_B = pi_mirror . w0(I2)): 'duality on color' -- I2 permuted nontrivially")

    R["layer3_lattice_classes"] = {
        "pi_mirror_simple_permutation": PI_SIMPLE,
        "pi_A_swaps_hatch_I1": swap_ok, "pi_A_fixes_I2_pointwise": I2_fixed_pointwise,
        "pi_B_swaps_hatch_I1": swap_ok_B, "pi_B_fixes_I2_setwise": I2_setwise_B,
        "pi_B_fixes_I2_pointwise": I2_pointwise_B,
        "verification_checks_all_pass": (ok_cartan and ok_bij and bad_iso == 0 and bad_inv == 0
                                          and swap_ok and I2_fixed_setwise and bad_root_B == 0
                                          and bad_inv_B == 0 and bad_iso_B == 0 and swap_ok_B
                                          and I2_setwise_B and not I2_pointwise_B),
    }

    PI_ID = lambda r: r
    LATTICE = {"id": PI_ID, "A": pi_mirror, "B": pi_B}

    # ========================================================================
    # LAYER 4 -- the F2 sign-lift cocycle solver (both families), WITH the
    # theta^2=id constraint (found necessary -- some cocycle-only solutions are
    # not involutions; verified by direct falsification during development).
    # ========================================================================
    log("")
    log("=== LAYER 4: the F2 sign-lift cocycle solver (both Chevalley-automorphism families) ===")

    def bitof(x):
        return 0 if x == 1 else 1

    def solve_kernel(pi_fn, family):
        """family: 'antipodal' (Family 1: theta(h)=-pi(h), theta(e_r)=eps(r)e_{-pi(r)})
        or 'permute' (Family 2: theta(h)=+pi(h), theta(e_r)=eps(r)e_{pi(r)}).
        Cocycle target root for the eps-consistency check is the SAME shape either
        way (uses pi(r),pi(s) directly in the eps-ratio obstruction; the antipodal
        sign is absorbed structurally, verified empirically to give the right
        controls) PLUS evenness eps(-r)=eps(r) PLUS the theta^2=id constraint
        eps(pi(r))=eps(r) when pi(r)!=r."""
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
    log(f"  B restricted to I2 (fixed, untransformed) signature: {B_I2_signature} "
        f"(fixed structural fact: A2's Cartan(pos def,2) + 3 hyperbolic pairs -> (5,3))")
    assert B_I2_signature == (5, 3, 0)

    def color_signature(pi_fn, ef, family):
        """Build the 8x8 restriction of theta to I2 (I2 verified theta-stable by
        construction), find its +-1 eigenspaces EXACTLY, lift to the 78-dim ambient
        space, compute B's signature on each eigenspace. Returns dict with dims,
        raw (pos,neg,zero) signatures on each part, and a purity flag."""
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

        sig_plus = restrict_sig(Vp)     # V+ part of I2 -- "compact-like" iff purely negative
        sig_minus = restrict_sig(Vm)    # V- part of I2 -- "compact-like" iff purely positive... or could
        # ALSO both be pure the other way; purity (one-sidedness) is what we actually require, the LABEL
        # (which sign is "positive" overall) is a convention, so we report both raw triples and let the
        # verdict logic decide compactness from purity + total counts.
        purity_plus = (sig_plus[0] == 0 or sig_plus[1] == 0) and sig_plus[2] == 0
        purity_minus = (sig_minus[0] == 0 or sig_minus[1] == 0) and sig_minus[2] == 0
        pure = purity_plus and purity_minus
        return {
            "dim_plus": dim_p, "dim_minus": dim_m,
            "sig_plus_raw": list(sig_plus), "sig_minus_raw": list(sig_minus),
            "pure": pure,
        }

    def global_definiteness(Msp):
        Vp = (Msp - sp.eye(DIM)).nullspace()
        Vm = (Msp + sp.eye(DIM)).nullspace()
        dvp, dvm = len(Vp), len(Vm)
        sp_ = congruence_signature(sp.Matrix.hstack(*Vp).T * Bform * sp.Matrix.hstack(*Vp)) if dvp else (0, 0, 0)
        sm_ = congruence_signature(sp.Matrix.hstack(*Vm).T * Bform * sp.Matrix.hstack(*Vm)) if dvm else (0, 0, 0)
        pure = ((sp_[0] == 0 or sp_[1] == 0) and sp_[2] == 0 and (sm_[0] == 0 or sm_[1] == 0) and sm_[2] == 0)
        return dvp, dvm, sp_, sm_, pure

    def full_check_element(pi_fn, ef, family, verify_automorphism=True, ntrials=60):
        Mt = build_theta_matrix(pi_fn, ef, family)
        Msp = to_sp_mat(Mt)
        is_invol = (Msp * Msp == sp.eye(DIM))
        tr = sum(Msp[i, i] for i in range(DIM))
        chi = int(-tr)
        auto_fail = 0
        if verify_automorphism:
            def apply_mat(Mlist, v):
                return [sum(Mlist[i][j] * v[j] for j in range(DIM)) for i in range(DIM)]
            for _ in range(ntrials):
                x, y = rand_vec(), rand_vec()
                tx, ty = apply_mat(Mt, x), apply_mat(Mt, y)
                lhs = apply_mat(Mt, br(x, y))
                rhs = br(tx, ty)
                if lhs != rhs:
                    auto_fail += 1
        checksum_pass = chi in ALLOWED_CHARS
        dvp, dvm, gsp, gsm, gpure = global_definiteness(Msp)
        colorinfo = color_signature(pi_fn, ef, family)
        # compact color iff I2 splits with ONE side dim 0 and the other side dim 8 AND pure
        compact = colorinfo["pure"] and (
            (colorinfo["dim_plus"] == 8 and colorinfo["dim_minus"] == 0 and colorinfo["sig_plus_raw"][2] == 0
             and (colorinfo["sig_plus_raw"][0] == 0 or colorinfo["sig_plus_raw"][1] == 0)
             and (colorinfo["sig_plus_raw"][0] == 8 or colorinfo["sig_plus_raw"][1] == 8))
            or
            (colorinfo["dim_minus"] == 8 and colorinfo["dim_plus"] == 0 and colorinfo["sig_minus_raw"][2] == 0
             and (colorinfo["sig_minus_raw"][0] == 8 or colorinfo["sig_minus_raw"][1] == 8))
        )
        return {
            "theta_squared_is_identity": bool(is_invol),
            "automorphism_check_trials": ntrials if verify_automorphism else 0,
            "automorphism_failures": auto_fail,
            "character": chi,
            "classification_checksum_pass": checksum_pass,
            "global_eigendims": [dvp, dvm], "global_sig_plus": list(gsp), "global_sig_minus": list(gsm),
            "global_purity": bool(gpure),
            "color": colorinfo,
            "compact_color": bool(compact),
            "valid_cartan_involution": bool(is_invol and auto_fail == 0 and checksum_pass),
        }

    # ========================================================================
    # LAYER 5 -- CONTROLS
    # ========================================================================
    log("")
    log("=== LAYER 5: CONTROLS (reproduce B1119 exactly before the sweep) ===")

    # split control: Family "antipodal", pi=id, base (particular) solution
    cons_s, part_s, kbasis_s = solve_kernel(PI_ID, "antipodal")
    log(f"  split kernel (Family=antipodal, pi=id): consistent={cons_s}, dim={len(kbasis_s)}")
    ef_split = bits_to_eps(part_s)
    chk_split = full_check_element(PI_ID, ef_split, "antipodal")
    log(f"  SPLIT CONTROL: character={chk_split['character']} (expect +6), "
        f"theta^2=I:{chk_split['theta_squared_is_identity']}, "
        f"automorphism_fail:{chk_split['automorphism_failures']}, "
        f"global dims={chk_split['global_eigendims']} (expect [36,42]), "
        f"global_purity={chk_split['global_purity']}")
    split_pass = (chk_split["character"] == 6 and chk_split["global_eigendims"] == [36, 42]
                  and chk_split["theta_squared_is_identity"] and chk_split["automorphism_failures"] == 0
                  and chk_split["global_purity"])
    assert split_pass, "SPLIT CONTROL FAILED -- STOP, broken instrument"

    # compact control: Family "permute", pi=id, eps=1 (theta = identity map exactly)
    cons_c, part_c, kbasis_c = solve_kernel(PI_ID, "permute")
    ef_compact = bits_to_eps(part_c)  # particular solution for pi=id, permute family
    chk_compact_probe = full_check_element(PI_ID, ef_compact, "permute")
    # the pure trivial theta=identity is eps=+1 EVERYWHERE; confirm the particular
    # solution IS eps=1 everywhere (bits=0 -> part_c should already be all-zero if
    # eps=1 solves the homogeneous cocycle trivially, which it must for pi=id)
    eps1_is_solution = all(v == 0 for v in part_c)
    log(f"  compact kernel (Family=permute, pi=id): consistent={cons_c}, dim={len(kbasis_c)}, "
        f"trivial (eps=1) particular solution: {eps1_is_solution}")
    chk_compact = full_check_element(PI_ID, (lambda r: 1), "permute")
    log(f"  COMPACT CONTROL (theta=identity exactly): character={chk_compact['character']} (expect -78), "
        f"theta^2=I:{chk_compact['theta_squared_is_identity']}, "
        f"global dims={chk_compact['global_eigendims']} (expect [78,0])")
    compact_pass = (chk_compact["character"] == -78 and chk_compact["global_eigendims"] == [78, 0]
                    and chk_compact["theta_squared_is_identity"])
    assert compact_pass, "COMPACT CONTROL FAILED -- STOP, broken instrument"

    # variant A control: Family "antipodal", pi=pi_A(mirror), full kernel, look for
    # the base element -> expect character +2, color signature (5,3)
    cons_A, part_A, kbasis_A = solve_kernel(pi_mirror, "antipodal")
    log(f"  variant-A kernel (Family=antipodal, pi=A/mirror): consistent={cons_A}, "
        f"dim={len(kbasis_A)} (2^{len(kbasis_A)}={2**len(kbasis_A)} elements)")
    ef_A_base = bits_to_eps(part_A)
    chk_A = full_check_element(pi_mirror, ef_A_base, "antipodal")
    log(f"  VARIANT A base element: character={chk_A['character']} (expect +2), "
        f"theta^2=I:{chk_A['theta_squared_is_identity']}, auto_fail:{chk_A['automorphism_failures']}, "
        f"color dims(+,-)=({chk_A['color']['dim_plus']},{chk_A['color']['dim_minus']}), "
        f"color sig_plus={chk_A['color']['sig_plus_raw']}, color sig_minus={chk_A['color']['sig_minus_raw']}, "
        f"pure={chk_A['color']['pure']}")
    variantA_color_53 = (sorted([chk_A["color"]["dim_plus"], chk_A["color"]["dim_minus"]]) == [3, 5]
                          and chk_A["color"]["pure"])
    variantA_pass = (chk_A["character"] == 2 and chk_A["theta_squared_is_identity"]
                      and chk_A["automorphism_failures"] == 0 and variantA_color_53)
    log(f"  VARIANT A reproduction: character+2={chk_A['character']==2}, color=(5,3) pure={variantA_color_53}, "
        f"OVERALL MATCH to B1118/B1119's reported (char=+2, color sl(3,R) sig (5,3)): {variantA_pass}")

    R["layer5_controls"] = {
        "split": {"character": chk_split["character"], "global_dims": chk_split["global_eigendims"],
                  "expected_character": 6, "expected_dims": [36, 42], "pass": split_pass},
        "compact": {"character": chk_compact["character"], "global_dims": chk_compact["global_eigendims"],
                    "expected_character": -78, "expected_dims": [78, 0], "pass": compact_pass},
        "variant_A": {"character": chk_A["character"], "color_dims": [chk_A["color"]["dim_plus"],
                      chk_A["color"]["dim_minus"]], "color_pure": chk_A["color"]["pure"],
                      "expected_character": 2, "expected_color_signature": [5, 3],
                      "matches_B1118_B1119_exactly": variantA_pass},
        "variant_B_note": ("Family=antipodal, pi=B (mirror.w0(I2), 'duality on color') was searched "
                            "as the natural candidate for variant B; its base element gives character "
                            "-2 (checksum FAILS, impossible) and its full (theta^2=id-filtered) kernel "
                            "gives ONLY {+2,-2} (see the full sweep below) -- variant B's reported "
                            "(character +6, color su(2,1) signature (4,4)) was NOT reproduced by this "
                            "construction. An extensive systematic search (12 further candidates built "
                            "from mirror composed with matched Weyl-group twists of hatch/I1, all "
                            "verified as genuine involutions swapping hatch<->I1 and fixing I2 setwise) "
                            "ALSO found only {+2,-2}, never +6, within the ANTIPODAL family. Family="
                            "'permute' with pi=B (and pi=A) DOES reach +6 (see sweep) but this is a "
                            "structurally different construction than variant A's; whether it matches "
                            "variant B's ORIGINAL construction is UNVERIFIED (discrepancy honestly "
                            "flagged, not swept under the rug -- see V2_NOTES.md)."),
    }

    # ========================================================================
    # LAYER 6 -- THE FULL SWEEP: both families x both lattice classes
    # ========================================================================
    log("")
    log("=== LAYER 6: THE FULL KERNEL SWEEP -- both families x both lattice classes ===")
    sweep_table = []
    kernel_summary = {}
    compact_hits = []

    for family in ("antipodal", "permute"):
        for cls in ("A", "B"):
            pi_fn = LATTICE[cls]
            consistent, part, kbasis = solve_kernel(pi_fn, family)
            k = len(kbasis)
            label = f"{family}/{cls}"
            log(f"  [{label}] consistent={consistent}, kernel dim k={k} (2^{k}={2**k} elements)")
            kernel_summary[label] = {
                "consistent": consistent, "k": k, "n_elements": 2 ** k,
                "kernel_basis_bitvectors_by_root_index": [kb for kb in kbasis],
                "particular_solution_bitvector": part,
            }
            if not consistent:
                log(f"    [{label}] INCONSISTENT -- no sign-lift exists for this (family,pi); skipping")
                continue
            elt_records = []
            for bits in itertools.product([0, 1], repeat=k):
                v = combine(part, kbasis, bits)
                ef = bits_to_eps(v)
                chk = full_check_element(pi_fn, ef, family, verify_automorphism=False)
                # cheap per-element pass; automorphism re-verified below for any
                # checksum-passing + globally-pure candidate (the ones that matter)
                rec = {"bits": list(bits), "character": chk["character"],
                       "checksum_pass": chk["classification_checksum_pass"],
                       "theta_sq_id": chk["theta_squared_is_identity"],
                       "global_dims": chk["global_eigendims"], "global_purity": chk["global_purity"],
                       "color_dims": [chk["color"]["dim_plus"], chk["color"]["dim_minus"]],
                       "color_sig_plus": chk["color"]["sig_plus_raw"],
                       "color_sig_minus": chk["color"]["sig_minus_raw"],
                       "color_pure": chk["color"]["pure"], "compact_color": chk["compact_color"]}
                elt_records.append(rec)
                if chk["compact_color"]:
                    # full rigorous re-verification (automorphism on many trials) before trusting
                    chk_full = full_check_element(pi_fn, ef, family, verify_automorphism=True, ntrials=300)
                    rec["full_reverification"] = {
                        "automorphism_failures_of_300": chk_full["automorphism_failures"],
                        "confirmed": chk_full["automorphism_failures"] == 0 and chk_full["compact_color"],
                    }
                    compact_hits.append({"family": family, "lattice_class": cls, **rec})
            chars_seen = sorted({e["character"] for e in elt_records})
            n_theta2_ok = sum(1 for e in elt_records if e["theta_sq_id"])
            n_checksum_ok = sum(1 for e in elt_records if e["checksum_pass"])
            n_globally_pure = sum(1 for e in elt_records if e["global_purity"])
            n_color_pure = sum(1 for e in elt_records if e["color_pure"])
            log(f"    [{label}] characters over the full kernel: {chars_seen}")
            log(f"    [{label}] theta^2=I: {n_theta2_ok}/{len(elt_records)}; checksum-pass: "
                f"{n_checksum_ok}/{len(elt_records)}; globally pure: {n_globally_pure}/{len(elt_records)}; "
                f"color-pure: {n_color_pure}/{len(elt_records)}")
            sweep_table.append({
                "family": family, "lattice_class": cls, "kernel_dim": k,
                "characters_seen": chars_seen, "n_theta2_ok": n_theta2_ok,
                "n_checksum_pass": n_checksum_ok, "n_globally_pure": n_globally_pure,
                "n_color_pure": n_color_pure, "elements": elt_records,
            })

    R["layer6_kernel_summary"] = kernel_summary
    R["layer6_sweep_table"] = sweep_table
    R["compact_color_hits"] = compact_hits

    # ========================================================================
    # VERDICT
    # ========================================================================
    log("")
    log("=== VERDICT ===")
    genuine_compact_hits = [h for h in compact_hits
                             if h.get("full_reverification", {}).get("confirmed")]
    if genuine_compact_hits:
        verdict = "COMPACT-COLOR-FOUND"
    else:
        verdict = "NO-COMPACT-HOST"
    log(f"  raw compact_color flags (pre-reverification): {len(compact_hits)}")
    log(f"  FULLY RE-VERIFIED genuine compact-color elements: {len(genuine_compact_hits)}")
    log(f"  VERDICT: {verdict}")

    all_allowed_chars_seen = sorted({c for t in sweep_table for c in t["characters_seen"]})
    log(f"  all classification-checksum-allowed characters reached anywhere in the sweep "
        f"(union over both families x both classes): "
        f"{[c for c in all_allowed_chars_seen if c in ALLOWED_CHARS]}")
    log(f"  any impossible (checksum-failing) character reached: "
        f"{[c for c in all_allowed_chars_seen if c not in ALLOWED_CHARS]}")

    R["verdict"] = verdict
    R["genuine_compact_color_hits"] = genuine_compact_hits
    R["all_characters_seen_allowed"] = [c for c in all_allowed_chars_seen if c in ALLOWED_CHARS]
    R["all_characters_seen_disallowed"] = [c for c in all_allowed_chars_seen if c not in ALLOWED_CHARS]
    R["runtime_seconds"] = round(time.time() - T0, 2)
    R["log"] = LOG

    out_path = os.path.join(HERE, "V2_results.json")
    with open(out_path, "w") as f:
        json.dump(R, f, indent=1, default=str)
    log(f"wrote {out_path}")
    log(f"TOTAL runtime: {time.time()-T0:.2f}s")
    return R


if __name__ == "__main__":
    main()
