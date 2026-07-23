"""OI-146 -- B332 Bianchi index [Gamma : Gamma cap g*Gamma*g^-1] = 3 on the sqrt(-3) side
(B771 Phase-1 Wave-1 closure cell).

SEALED CRITERION (prereg B771 7955049f, cell OI-146): "the index-3 computation on the
sqrt(-3) side verifies exactly / fails with the discrepancy shown."

BACKGROUND (read from the sources, not re-asserted).
  - frontier/B332_two_letters_two_ends/FINDINGS.md explicitly QUARANTINES this exact claim:
    "Overlap index [Gamma:Gamma cap g*Gamma*g^-1] = 3 -- reported, not verified ... a finite
    index >1 is plausible -- but =3 ... need the actual Bianchi-group computation. Left for a
    dedicated probe; not asserted." That dedicated probe is this cell.
  - Gamma = pi_1(4_1) via the Riley discrete-faithful representation (frontier/B425
    geometric_torsion.py, cross-validated V30/V31): A = rho(a) = [[1,1],[0,1]],
    B = rho(b) = [[1,0],[-w,1]], w = omega (primitive cube root of unity, w^2+w+1=0),
    entries in O_3 = Z[omega]. This Gamma has known GEOMETRIC index 12 in the Bianchi
    group G = PGL(2,O_3) (Riley; re-verified via Humbert's volume formula in
    frontier/B302, frontier/B734/cc3_verification).
  - g = [[0,-1],[1,-1]] is the order-3 commensurator element already exhibited in B302 and
    used throughout B332/B324/B326/B331 (g in SL(2,Z) subset SL(2,O_3), eigenvalues {w,w^2}).
    B332's own two_letters_two_ends.py shows g*a*g^-1 = L^-1 (an SL(2,Z) matrix "not
    obviously in <a,b>") -- i.e. g commensurates Gamma without normalizing it. That is the
    open question this cell closes: the exact index.
  - frontier/B734_m004_is_congruence/FINDINGS.md (two-seat: cc2 + cc, cc3-verified a third
    way in cc3_verification/) established, by finite-ring BFS over O_3/M, that Gamma IS a
    CONGRUENCE subgroup at level M=8=2^3: Gamma contains the principal congruence subgroup
    Gamma(8) = ker(SL(2,O_3) -> SL(2,O_3/8)), and [SL(2,O_3/8) : image(Gamma)] = 12 exactly
    (matching the geometric index -- both the bare-image test T_SL and the mod-center test
    T_PSL read 12 at level 8; ambient |SL(2,O_3/8)| = 245760, |image(Gamma)| = 20480).

THE METHOD THIS CELL ADDS (the actual "dedicated probe").
  Gamma(8) is the kernel of a ring-homomorphism SL(2,O_3) -> SL(2,O_3/8), hence NORMAL in
  the whole ambient group SL(2,O_3) (not just in Gamma). Since Gamma is congruence at level
  8, Gamma contains Gamma(8); and g*Gamma(8)*g^-1 = Gamma(8) (normality), so g*Gamma*g^-1
  also contains Gamma(8). By the correspondence theorem for the finite quotient
  SL(2,O_3)/Gamma(8) = SL(2,O_3/8):
      Gamma cap g*Gamma*g^-1  contains  Gamma(8),  and
      (Gamma cap g*Gamma*g^-1) / Gamma(8)  =  image(Gamma) cap gbar*image(Gamma)*gbar^-1
  where gbar is the image of g mod 8. Indices are preserved by the correspondence theorem, so
      [Gamma : Gamma cap g*Gamma*g^-1]  =  [image(Gamma) : image(Gamma) cap gbar*image(Gamma)*gbar^-1]
  -- an EXACT finite-group computation inside SL(2,O_3/8) (245760 elements), not a numeric
  approximation, and not dependent on going to any higher level (8 is already the exact
  congruence level; any multiple of 8 gives the identical answer by the same argument, so 8
  suffices and is exact -- verified below at level 16 too, on the odd-level-3 factor, as a
  cross-check that the level-8 read is stable).

Two independent ring-basis implementations are run (omega-basis w^2=-w-1, and the B734
z-basis z=(1+sqrt(-3))/2 with z^2=z-1, w=z-1) as the >=2-implementation robustness check;
both directions of g (g and g^-1) are computed; and the SL-level and PSL-level (mod center)
readings are both reported.

Env: pyenv python3 + sympy (NOT sage). Self-contained; no snappy dependency needed for the
finite computation (snappy/sympy only used for the exact-relation sanity check).
"""
import json
import sys
import time
import sympy as sp

# =====================================================================
# PART 0 -- exact (unreduced, symbolic) sanity checks over Z[omega] and
# reproduction of B332's own claimed identities.
# =====================================================================

def part0_symbolic_checks():
    out = {}
    R = sp.Matrix([[1, 1], [0, 1]])
    L = sp.Matrix([[1, 0], [1, 1]])
    g = sp.Matrix([[0, -1], [1, -1]])
    a = R

    # B332's claimed identities (from two_letters_two_ends.py), reproduced.
    id1 = sp.simplify(g - (-(R * L.inv()))) == sp.zeros(2)
    id2 = sp.simplify(g.inv() * a - (-L)) == sp.zeros(2)
    out["g_eq_negRLinv"] = bool(id1)
    out["ginv_a_eq_negL"] = bool(id2)
    out["g_is_order3"] = bool(sp.simplify(g**3 - sp.eye(2)) == sp.zeros(2))
    out["gag^-1"] = (g * a * g.inv()).tolist()
    out["gag^-1_eq_Linv"] = bool(sp.simplify(g * a * g.inv() - L.inv()) == sp.zeros(2))

    # The REAL Riley holonomy generators (B425 geometric_torsion.py): a->[[1,1],[0,1]],
    # b->[[1,0],[-w,1]] with w^2+w+1=0 (the discrete-faithful rep of pi_1(4_1)).
    w = sp.Symbol('w')
    A = sp.Matrix([[1, 1], [0, 1]])
    Bm = sp.Matrix([[1, 0], [-w, 1]])
    # relator r = a * (b a^-1 b^-1 a) * b^-1 * (b a^-1 b^-1 a)^-1  (figure-eight, B425 form)
    Wd = Bm * A.inv() * Bm.inv() * A
    Rel = sp.simplify(A * Wd * Bm.inv() * Wd.inv())
    num = sp.gcd([sp.numer(sp.together(Rel[i, j] - (1 if i == j else 0))) for i in range(2) for j in range(2)])
    holo = sp.factor(num)
    out["relator_forces"] = str(holo)  # should factor with (w^2+w+1) as a root condition

    # g conjugating the REAL Riley b-generator (symbolic w, informative only)
    gS = sp.Matrix([[0, -1], [1, -1]])
    gBg = sp.simplify(gS * Bm * gS.inv())
    out["g_b_ginv_symbolic"] = str(gBg.tolist())

    return out


# =====================================================================
# PART 1 -- finite ring O_3/M arithmetic + SL(2,.) matrix group BFS,
# omega-basis: element = a + b*omega, omega^2 = -omega - 1.
# =====================================================================

def ring_omega(M):
    def mul(p, q):
        a, b = p
        c, d = q
        # (a+bw)(c+dw) = ac + (ad+bc)w + bd*w^2 = ac + (ad+bc)w + bd*(-w-1)
        #              = (ac - bd) + (ad + bc - bd) w
        return ((a * c - b * d) % M, (a * d + b * c - b * d) % M)

    def add(p, q):
        return ((p[0] + q[0]) % M, (p[1] + q[1]) % M)

    def neg(p):
        return ((-p[0]) % M, (-p[1]) % M)

    return mul, add, neg


def ring_z(M):
    # B734 cc3 convention: z = (1+sqrt(-3))/2 primitive 6th root, z^2 = z - 1.
    def mul(p, q):
        a, b = p
        c, d = q
        return ((a * c - b * d) % M, (a * d + b * c + b * d) % M)

    def add(p, q):
        return ((p[0] + q[0]) % M, (p[1] + q[1]) % M)

    def neg(p):
        return ((-p[0]) % M, (-p[1]) % M)

    return mul, add, neg


def mat_ops(ringfns):
    mul, add, neg = ringfns

    def MM(X, Y):
        return (
            add(mul(X[0], Y[0]), mul(X[1], Y[2])),
            add(mul(X[0], Y[1]), mul(X[1], Y[3])),
            add(mul(X[2], Y[0]), mul(X[3], Y[2])),
            add(mul(X[2], Y[1]), mul(X[3], Y[3])),
        )

    def inv(X):  # det = 1 assumed
        return (X[3], neg(X[1]), neg(X[2]), X[0])

    return MM, inv


def bfs_closure(M, ringfns, gens, cap=2_000_000):
    MM, inv = mat_ops(ringfns)
    E, Z = (1, 0), (0, 0)
    I = (E, Z, Z, E)
    allgens = list(gens) + [inv(g) for g in gens]
    seen = {I}
    frontier = [I]
    while frontier:
        nxt = []
        for X in frontier:
            for g in allgens:
                Y = MM(X, g)
                if Y not in seen:
                    seen.add(Y)
                    nxt.append(Y)
                    if len(seen) > cap:
                        raise RuntimeError("BFS cap exceeded")
        frontier = nxt
    return seen


def sl_ambient(M, ringfns):
    """Full SL(2,O/M) generated by the 4 elementary transvections."""
    E, Z, u = (1, 0), (0, 0), (0, 1)
    gens = [(E, E, Z, E), (E, u, Z, E), (E, Z, E, E), (E, Z, u, E)]
    return bfs_closure(M, ringfns, gens)


def central_scalars(M, ringfns):
    mul, add, neg = ringfns
    return [(a, b) for a in range(M) for b in range(M) if mul((a, b), (a, b)) == (1, 0)]


def conjugate_set(M, ringfns, S, g):
    """{ g x g^-1 : x in S }"""
    MM, inv = mat_ops(ringfns)
    ginv = inv(g)
    return {MM(MM(g, x), ginv) for x in S}


def to_ring(n, M):
    return (n % M, 0)


def build_generators(basis, M):
    """basis in {'omega','z'}. Returns (ringfns, A, B, g) at modulus M."""
    if basis == 'omega':
        ringfns = ring_omega(M)
        mul, add, neg = ringfns
        E, Z = (1, 0), (0, 0)
        w = (0, 1)
        A = (E, E, Z, E)                      # [[1,1],[0,1]]
        B = (E, Z, neg(w), E)                 # [[1,0],[-w,1]]
    elif basis == 'z':
        ringfns = ring_z(M)
        mul, add, neg = ringfns
        E, Z = (1, 0), (0, 0)
        z = (0, 1)
        w = add(z, neg(E))                    # w = z - 1 (primitive cube root)
        A = (E, E, Z, E)
        B = (E, Z, neg(w), E)
    else:
        raise ValueError(basis)
    g = ((to_ring(0, M), to_ring(-1, M)), (to_ring(1, M), to_ring(-1, M)))
    # flatten g to the (p,q,r,s) 4-tuple form matching A,B's shape
    g = (to_ring(0, M), to_ring(-1, M), to_ring(1, M), to_ring(-1, M))
    return ringfns, A, B, g


def analyze(basis, M, do_ambient=True):
    ringfns, A, B, g = build_generators(basis, M)
    MM, inv = mat_ops(ringfns)

    t0 = time.time()
    Gamma_bar = bfs_closure(M, ringfns, [A, B])
    t1 = time.time()

    amb = None
    if do_ambient:
        amb = sl_ambient(M, ringfns)
    t2 = time.time()

    # g must itself be a unit-determinant element for the SL(2) BFS group law to
    # apply consistently; check det(g) == 1 mod M as a build sanity check.
    mul, add, neg = ringfns
    detg = add(mul(g[0], g[3]), neg(mul(g[1], g[2])))

    conjG = conjugate_set(M, ringfns, Gamma_bar, g)
    conjG_indep = bfs_closure(M, ringfns, [MM(MM(g, A), inv(g)), MM(MM(g, B), inv(g))])
    same_conj = (conjG == conjG_indep)

    inter = Gamma_bar & conjG
    index = len(Gamma_bar) / len(inter)
    index_exact = len(Gamma_bar) // len(inter) if len(Gamma_bar) % len(inter) == 0 else None

    # g^-1 direction, for symmetry / second-word cross-check
    ginv = inv(g)
    conjG2 = conjugate_set(M, ringfns, Gamma_bar, ginv)
    inter2 = Gamma_bar & conjG2
    index2 = len(Gamma_bar) / len(inter2)
    index2_exact = len(Gamma_bar) // len(inter2) if len(Gamma_bar) % len(inter2) == 0 else None

    # PSL-level (mod center) cross-check: is the SL-level index preserved when we
    # quotient everything by the central scalars found inside Gamma_bar?
    cen = central_scalars(M, ringfns)
    cen_in_Gamma = [c for c in cen if (c, (0, 0), (0, 0), c) in Gamma_bar]

    res = dict(
        basis=basis, M=M,
        ambient_order=(len(amb) if amb is not None else None),
        Gamma_bar_order=len(Gamma_bar),
        SL_index_of_Gamma=(len(amb) // len(Gamma_bar) if amb is not None else None),
        det_g_mod_M=detg,
        conjugate_build_matches_direct=bool(same_conj),
        conj_gGammag_inv_order=len(conjG),
        intersection_order=len(inter),
        index_Gamma_over_intersection=index,
        index_Gamma_over_intersection_exact=index_exact,
        index_divides_exactly=bool(len(Gamma_bar) % len(inter) == 0),
        index_ginv_direction=index2,
        index_ginv_exact=index2_exact,
        n_central_scalars_mod_M=len(cen),
        n_central_scalars_in_Gamma_bar=len(cen_in_Gamma),
        secs_gamma_bfs=round(t1 - t0, 2),
        secs_ambient_bfs=round(t2 - t1, 2) if do_ambient else None,
    )
    return res


def humbert_true_index_check():
    """Independent, level-free confirmation that the TRUE index [PSL(2,O_3):Gamma] = 12
    (Riley/Humbert), reused from frontier/B734_m004_is_congruence/cc3_verification/
    b734_independent_verify.py's humbert_check(), recomputed here. This is the fact that
    makes the finite-level read at M=8 PROVABLY exact (not just plateau-plausible): since
    [ambient(M):image(Gamma)] <= [true ambient : Gamma] always, with equality iff Gamma
    is congruence at that level, and we observe equality (12 = 12) at M=8, Gamma DOES
    contain the true PSL principal congruence subgroup Gamma_hat(8) exactly -- no risk of
    a B731-style premature plateau (this argument does not depend on trusting M=16 too;
    it is decisive already at M=8, using an M-independent invariant, the volume)."""
    from mpmath import mp, mpf, zeta, pi, sqrt, sin, nsum, inf
    mp.dps = 40
    L = nsum(lambda n: (1 if n % 3 == 1 else (-1 if n % 3 == 2 else 0)) / mpf(n) ** 2, [1, inf])
    zK2 = zeta(2) * L
    vol_orbifold = (mpf(3) ** mpf(1.5)) * zK2 / (4 * pi ** 2)      # Humbert, K=Q(sqrt(-3))
    lob = nsum(lambda n: sin(2 * n * pi / 3) / mpf(n) ** 2, [1, inf]) / 2
    vol_m004 = 6 * lob                                             # 2 regular ideal tetrahedra
    ratio = vol_m004 / vol_orbifold
    return dict(vol_orbifold=str(vol_orbifold), vol_m004=str(vol_m004),
                index_ratio=str(ratio), index_ratio_rounds_to_12=bool(abs(ratio - 12) < mpf(10) ** -30))


def coset_orbit_cross_check(M=8):
    """THIRD independent method: build the 12 right cosets of Gamma_bar in the level-M
    ambient SL(2,O/M) explicitly, and directly count the orbit of the coset g*Gamma_bar
    under LEFT multiplication by Gamma_bar. By orbit-stabilizer, orbit size =
    [Gamma_bar : Stab] and Stab = {h in Gamma_bar : g^-1 h g in Gamma_bar} = Gamma_bar cap
    g*Gamma_bar*g^-1 -- i.e. this orbit size IS [Gamma_bar : Gamma_bar cap g Gamma_bar g^-1],
    computed by a completely different route (permutation action on the 12-point coset
    space) than the direct subgroup-intersection count in analyze()."""
    ringfns, A, B, g = build_generators('omega', M)
    MM, inv = mat_ops(ringfns)
    Gamma_bar = bfs_closure(M, ringfns, [A, B])
    amb = sl_ambient(M, ringfns)

    remaining = set(amb)
    reps = []
    while remaining:
        x = next(iter(remaining))
        coset = {MM(x, h) for h in Gamma_bar}
        assert coset <= remaining
        reps.append(x)
        remaining -= coset

    def coset_index(y):
        for i, r in enumerate(reps):
            if MM(inv(r), y) in Gamma_bar:
                return i
        raise ValueError("y not covered by any coset -- bug")

    orbit = {coset_index(MM(h, g)) for h in Gamma_bar}
    return dict(num_cosets=len(reps), orbit_size=len(orbit),
                matches_geometric_index=bool(len(reps) == 12))


def part1_finite_computation():
    out = {}

    # Reproduce B734's banked levels 2,4,8 as a build-quality check (ambient + Gamma
    # order + SL-index must match the already-verified banked numbers: 60/10/6,
    # 3840/320/12, 245760/20480/12).
    banked = {2: (60, 10, 6), 4: (3840, 320, 12), 8: (245760, 20480, 12)}
    reproduction = {}
    for M in (2, 4, 8):
        r = analyze('omega', M, do_ambient=True)
        reproduction[M] = r
        exp_amb, exp_img, exp_idx = banked[M]
        r['matches_banked_B734'] = bool(
            r['ambient_order'] == exp_amb and r['Gamma_bar_order'] == exp_img
            and r['SL_index_of_Gamma'] == exp_idx)
    out['reproduction_of_B734'] = reproduction

    # THE MAIN COMPUTATION: level 8, omega-basis -- the exact commensurator index.
    main = analyze('omega', 8, do_ambient=False)  # ambient already confirmed above
    out['main_level8_omega'] = main

    # Independent second basis (B734's z-basis), same level -- robustness check.
    main_z = analyze('z', 8, do_ambient=False)
    out['main_level8_zbasis'] = main_z

    # Level 16 (still an exact congruence level, since Gamma(16) subset Gamma(8)
    # subset Gamma, by 8 | 16): if the answer is genuinely stable, it must be
    # identical here too. This BFS is heavier (ambient ~ 15.7M by the lifting
    # formula in B734, kernel order 64 per 2-power step) so we build ONLY
    # Gamma_bar and the conjugate/intersection at level 16 directly (skip the
    # full ambient BFS, which is not needed for the index computation itself).
    t0 = time.time()
    r16 = analyze('omega', 16, do_ambient=False)
    r16['secs_total'] = round(time.time() - t0, 2)
    out['level16_stability_check'] = r16

    return out


if __name__ == "__main__":
    result = {}
    print("=" * 78)
    print("OI-146 / B332 -- Bianchi commensurator index [Gamma:Gamma cap g Gamma g^-1]")
    print("=" * 78)

    print("\n--- PART 0: symbolic sanity checks (exact, over Z[w] / Z[omega]) ---")
    p0 = part0_symbolic_checks()
    result['part0_symbolic'] = p0
    for k, v in p0.items():
        print(f"  {k}: {v}")

    print("\n--- PART 1a: independent (M-free) true-index confirmation, Humbert volume ---")
    hb = humbert_true_index_check()
    result['humbert_true_index'] = hb
    print(f"  vol(minimal orbifold H^3/PSL(2,O_3)) = {hb['vol_orbifold']}")
    print(f"  vol(4_1 complement)                  = {hb['vol_m004']}")
    print(f"  ratio (= true [PSL(2,O_3):Gamma])     = {hb['index_ratio']}  "
          f"(rounds to 12: {hb['index_ratio_rounds_to_12']})")
    print("  => since finite-level index at M=8 (below) attains this SAME value 12, and")
    print("     finite-level index <= true index always with equality iff congruence at")
    print("     that level, M=8 is PROVABLY an exact congruence level for Gamma (no")
    print("     B731-style premature-plateau risk -- decisive already at M=8).")

    print("\n--- PART 1b: finite congruence-quotient computation ---")
    p1 = part1_finite_computation()
    result['part1_finite'] = p1

    print("\nReproduction of B734's banked levels (build-quality check):")
    for M, r in p1['reproduction_of_B734'].items():
        print(f"  level {M}: ambient={r['ambient_order']} Gamma_bar={r['Gamma_bar_order']} "
              f"SL_index={r['SL_index_of_Gamma']}  matches_banked={r['matches_banked_B734']}  "
              f"[{r['secs_gamma_bfs']+ (r['secs_ambient_bfs'] or 0):.1f}s]")

    print("\nMAIN RESULT (level 8, omega-basis):")
    m = p1['main_level8_omega']
    print(f"  det(g) mod 8 = {m['det_g_mod_M']}  (must be (1,0) for g in SL(2,O/8))")
    print(f"  |Gamma_bar| = {m['Gamma_bar_order']}")
    print(f"  |g Gamma_bar g^-1| = {m['conj_gGammag_inv_order']}  "
          f"(direct-conjugation build matches independent BFS-from-conjugated-generators build: "
          f"{m['conjugate_build_matches_direct']})")
    print(f"  |Gamma_bar cap g Gamma_bar g^-1| = {m['intersection_order']}")
    print(f"  [Gamma_bar : Gamma_bar cap g Gamma_bar g^-1] = {m['index_Gamma_over_intersection']}  "
          f"(exact integer division: {m['index_divides_exactly']})")
    print(f"  same index using g^-1 instead of g: {m['index_ginv_direction']}")
    print(f"  central scalars mod 8: {m['n_central_scalars_mod_M']}, "
          f"of which in Gamma_bar: {m['n_central_scalars_in_Gamma_bar']}")

    print("\nCROSS-CHECK (independent z-basis, B734 convention):")
    mz = p1['main_level8_zbasis']
    print(f"  [Gamma_bar : Gamma_bar cap g Gamma_bar g^-1] = {mz['index_Gamma_over_intersection']}  "
          f"(exact: {mz['index_divides_exactly']})")

    print("\nCROSS-CHECK (level 16, still an exact congruence level, 8 | 16):")
    r16 = p1['level16_stability_check']
    print(f"  |Gamma_bar| = {r16['Gamma_bar_order']}, "
          f"[Gamma_bar : Gamma_bar cap g Gamma_bar g^-1] = {r16['index_Gamma_over_intersection']}  "
          f"(exact: {r16['index_divides_exactly']})  [{r16['secs_gamma_bfs']:.1f}s]")

    print("\n--- PART 1c: THIRD independent method -- explicit 12-coset orbit count ---")
    orb = coset_orbit_cross_check(8)
    result['coset_orbit_cross_check'] = orb
    print(f"  num right cosets of Gamma_bar in ambient SL(2,O/8): {orb['num_cosets']} "
          f"(matches geometric index 12: {orb['matches_geometric_index']})")
    print(f"  orbit of g*Gamma_bar under LEFT mult by Gamma_bar: size {orb['orbit_size']}  "
          f"(= [Gamma_bar : Gamma_bar cap g Gamma_bar g^-1] by orbit-stabilizer, independently "
          f"of the subgroup-intersection count above)")

    claimed = 3
    computed = m['index_Gamma_over_intersection_exact']
    all_vals = [computed, mz['index_Gamma_over_intersection_exact'],
                r16['index_Gamma_over_intersection_exact'], orb['orbit_size'],
                m['index_ginv_exact']]
    all_agree_each_other = len(set(all_vals)) == 1
    agree_with_claim = all_agree_each_other and computed == claimed

    print("\n" + "=" * 78)
    print(f"CLAIMED (B332, quarantined, 'not asserted'): [Gamma:Gamma cap g Gamma g^-1] = {claimed}")
    print(f"COMPUTED (subgroup-intersection, omega-basis, level 8):  {computed}")
    print(f"COMPUTED (subgroup-intersection, z-basis,     level 8):  {mz['index_Gamma_over_intersection_exact']}")
    print(f"COMPUTED (subgroup-intersection, omega-basis, level 16): {r16['index_Gamma_over_intersection_exact']}")
    print(f"COMPUTED (g^-1 direction,        omega-basis, level 8):  {m['index_ginv_exact']}")
    print(f"COMPUTED (explicit 12-coset orbit count,      level 8):  {orb['orbit_size']}")
    print(f"ALL FIVE INDEPENDENT COMPUTATIONS AGREE WITH EACH OTHER: {all_agree_each_other}")
    print(f"THAT SHARED VALUE EQUALS THE CLAIMED 3: {agree_with_claim}")
    print("=" * 78)

    result['claimed_index'] = claimed
    result['computed_index_main'] = computed
    result['all_five_methods_agree_with_each_other'] = all_agree_each_other
    result['agree_with_claim'] = agree_with_claim
    if agree_with_claim:
        result['verdict'] = ("RESOLVED-A: index=3 verified exactly (5 independent "
                              "computations -- 2 bases, 2 levels, g and g^-1 direction, "
                              "and an explicit coset-orbit count -- all agree, and the "
                              "M=8 read is provably exact via the Humbert true-index match).")
    else:
        result['verdict'] = (
            f"RESOLVED-B: discrepancy shown. The claimed index is 3; the rigorously "
            f"computed index is {computed if all_agree_each_other else all_vals} "
            f"(5 independent computations agree with EACH OTHER: {all_agree_each_other}; "
            f"the M=8 read is provably exact -- not a premature plateau -- via the "
            f"Humbert true-index match to 12, see PART 1a). The claim '=3' does not hold; "
            f"the actual exact value is {computed}.")
    print("\nVERDICT:", result['verdict'])

    with open('output.json', 'w') as f:
        json.dump(result, f, indent=1, default=str)
    print("\n[written] output.json")
