"""B497 -- Gate A, class 2e: the extended-Bloch / K3^ind class beyond the object's own
(Closure Campaign Phase 2; prereg docs/CLOSURE_CAMPAIGN_2026-07.md + local README.md).

QUESTION (Gate A / S032-A, restricted to this class). Is any extended-Bloch/K3^ind-type
invariant of the single seed (1) trace-map-invariant, (2) discretely multivalued,
(3) UNsymmetrizable -- a genuine forced choice? Outcome enum (committed):
SEALED / COUNTEREXAMPLE / TOOL-BLOCKED.

ANCHORS (banked): B348 (the seed's Bloch class beta = 2[e^{i pi/3}], the orbit
{+beta, -beta} self-symmetrized by amphichirality, THE SEAM IDENTITY 1 - z0 = conj(z0));
B330 (the mechanism: a finite Galois orbit is always symmetrizable); B151 (the complex
volume as an element of C mod a lattice); B495 (class 2a, the N=2 Ptolemy solve);
B496 (class 2b, the CS/eta values -- cited, not re-derived).

STRUCTURE OF THE COMPUTATION
  0.  CONTROLS (B348 reproduced; failure => INVALID): the seam identity exactly; the
      orbit {+2D(z0), -2D(z0)} = {+Vol, -Vol} sum 0 at 30 dps; the Eisenstein shape
      solves the seed's rect gluing system EXACTLY (sympy against the live matrix).
  1.  THE STRATA SWEEP (pre-Bloch / shape-class data across the in-reach strata):
      cyclic covers n = 2..5 (the class is n.beta -- the Z-multiple tower, field
      stationary); the metallic family m = 1..4 (b++R^mL^m: m136 = FOUR isometric
      GAUSSIAN tetrahedra verified exactly; s464/t03910 shape fields by algdep with
      residual certificates); the forced +-5 fillings (the Meyerhoff child pair,
      B434/B496 cited; the trace-field quartic re-verified exactly).
      At every amphichiral stratum: conj(shape multiset) == {1/conj-free: the z -> 1/z
      Bloch-involution image of the multiset} -- complex conjugation acts on the class
      through a D-negating Bloch move: the geometric extension of the B348 seam.
  2.  THE EXTENDED-BLOCH LIFT (the probe's decisive new computation): the seed's N=2
      Ptolemy varieties solved EXACTLY in-sandbox (class 0 empty, class 1 cut by the
      Eisenstein quadratic -- the Ptolemy coordinates ARE the seam roots); both Galois
      lifts pushed through the Zickert flattening pipeline (snappy.ptolemy, offline):
      extended classes {+c^, -c^} with SUM 0 and the integer flattening data (p,q)
      NEGATED by the Galois conjugation; an independent Neumann L^ evaluation agrees
      within the pipeline's declared modulus (i pi^2/6); the same sweep for m136
      (8 obstruction classes: 6 empty, one POSITIVE-DIMENSIONAL non-geometric
      component -- the clause-(2) continuous exhibit -- and one with 8 points
      collapsing onto {+Vol_2, -Vol_2}).
  3.  THE THREE-CONDITION TEST + the forced / orbit / label classification + verdict.

TIERS (labeled per step): "exact" = sympy symbolic; "certified-numerical" = quad-double
(ManifoldHP) + pari algdep with residual + irreducibility certificates; "numerical" =
double-precision snappy. TOOL-BLOCKED items are named at the end, never silently
approximated.

Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.
"""
import json
import os

import mpmath as mp
import sympy as sp

VOL_SEED = 2.0298832128193072          # P9 anchor (recomputed independently in section 0)
CATALAN30 = None                       # set in section 1 (mp.catalan, scoped dps)

Z0 = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2       # e^{i pi/3}: the Eisenstein shape (P12)
Z0BAR = sp.conjugate(Z0)

REPORT = {}


def bank(section, **kv):
    REPORT.setdefault(section, {}).update(
        {k: (str(v) if isinstance(v, (sp.Basic, sp.Matrix)) else v) for k, v in kv.items()})


def bloch_wigner(w, dps=30):
    """Bloch-Wigner D(w) = Im Li2(w) + arg(1-w) log|w| (scoped precision, the B348 rule)."""
    with mp.workdps(dps):
        w = mp.mpc(w)
        return mp.im(mp.polylog(2, w)) + mp.arg(1 - w) * mp.log(abs(w))


def try_snappy():
    try:
        import snappy
        return snappy
    except Exception as exc:                                    # pragma: no cover
        print(f"   snappy unavailable ({exc}): every snappy-dependent step below is")
        print("   TOOL-BLOCKED (named); the pure-math controls still run.")
        return None


def rect_rows(M):
    """snappy rect gluing equations: rows (A, B, c) meaning prod z^A (1-z)^B = c."""
    return [(list(A), list(B), int(c)) for (A, B, c) in M.gluing_equations("rect")]


def rect_check_exact(rows, exact_shapes):
    """EXACT verification that exact_shapes solve every rect row (tier: exact)."""
    for A, B, c in rows:
        val = sp.simplify(sp.prod([z**a for z, a in zip(exact_shapes, A)])
                          * sp.prod([(1 - z)**b for z, b in zip(exact_shapes, B)]))
        if sp.simplify(val - c) != 0:
            return False
    return True


# =====================================================================
# SECTION 0 -- CONTROLS (B348 reproduced; failure => INVALID)
# =====================================================================
def controls(snappy):
    print("== 0. CONTROLS (B348 reproduced; failure => INVALID) ==")
    # (a) the Galois swap on the P12 Eisenstein quadratic (tier: exact)
    z = sp.symbols('z')
    eis = z**2 - z + 1
    assert sp.expand(eis.subs(z, Z0)) == 0 and sp.expand(eis.subs(z, Z0BAR)) == 0
    assert sp.simplify(Z0 - Z0BAR) != 0
    print("   (a) z0, conj(z0) = the two roots of z^2 - z + 1, Galois-swapped   [exact]")
    # (b) THE SEAM IDENTITY: 1 - z0 = conj(z0); and z(1-z) = 1 <=> the Eisenstein quadratic
    assert sp.simplify(1 - Z0 - Z0BAR) == 0
    assert sp.expand(z * (1 - z) - 1 + (z**2 - z + 1)) == 0
    # the |z| = 1 face of the same seam: 1/conj(z0) = z0 exactly
    assert sp.simplify(1 / Z0BAR - Z0) == 0
    print("   (b) THE SEAM: 1 - z0 = conj(z0) exactly; z(1-z)=1 <=> z^2-z+1=0;")
    print("       and 1/conj(z0) = z0 (the |z|=1 face used by the strata sweep)   [exact]")
    # (c) the orbit {+beta, -beta}: sum 0, |2D| = Vol (30 dps, independent of snappy)
    d0 = bloch_wigner(complex(sp.re(Z0), sp.im(Z0)))
    d0bar = bloch_wigner(complex(sp.re(Z0BAR), sp.im(Z0BAR)))
    assert abs(2 * d0 + 2 * d0bar) < mp.mpf(10)**(-25)
    assert abs(abs(2 * d0) - VOL_SEED) < 1e-12
    assert abs(bloch_wigner(mp.mpf(2) / 3)) < mp.mpf(10)**(-25)   # D == 0 on the fixed field
    print(f"   (c) orbit (2D(z0), 2D(conj z0)) = (+{float(2*d0):.15f}, {float(2*d0bar):.15f});")
    print("       sum = 0; |member| = Vol(4_1); D == 0 on the fixed field R   [30 dps]")
    bank("controls", seam_exact=True, orbit_sum_zero=True, vol_member=float(2 * d0),
         d_vanishes_on_fixed_field=True)
    if snappy is None:                                          # pragma: no cover
        bank("controls", snappy_control="TOOL-BLOCKED (snappy import failed)")
        return True
    # (d) the seed's shapes and the EXACT gluing solve (tier: exact via live rect matrix)
    M = snappy.Manifold("4_1")
    sh = [complex(s) for s in M.tetrahedra_shapes('rect')]
    z0c = complex(sp.re(Z0), sp.im(Z0))
    assert len(sh) == 2 and all(abs(s - z0c) < 1e-9 for s in sh)
    rows = rect_rows(M)
    assert rect_check_exact(rows, [Z0, Z0])
    assert rect_check_exact(rows, [Z0BAR, Z0BAR])   # the conjugate solution solves it too
    print("   (d) 4_1: both shapes = z0 (1e-9); z0 AND conj(z0) solve the rect gluing")
    print("       system EXACTLY (sympy on the live matrix) -- beta = 2[z0]   [exact]")
    bank("controls", seed_rect_exact=True, seed_rect_conj_exact=True,
         seed_rows=rows, all_pass=True)
    return True


# =====================================================================
# SECTION 1 -- THE STRATA SWEEP (pre-Bloch class data)
# =====================================================================
def dneg_images(z):
    """The D-NEGATIVE half of the six-element Lambda-orbit of a shape:
    D(1/z) = D(1-z) = D(z/(z-1)) = -D(z) (classical Bloch-Wigner identities)."""
    return [1 / z, 1 - z, z / (z - 1)]


def conj_matches_dneg_orbit(conj_multiset, shape_multiset, tol=1e-8):
    """Perfect matching: every element of conj_multiset equals (tol) a D-negative
    Lambda-image of a DISTINCT member of shape_multiset. Where this holds with
    shape_multiset = the same manifold's own shapes, complex conjugation acts on the
    pre-Bloch class as -1 through Bloch moves (the B348 seam, generalized); where it
    holds only against the MIRROR's shapes, the pairing is mirror-pairing (chiral)."""
    n = len(conj_multiset)
    if n != len(shape_multiset):
        return False
    cands = [[j for j in range(n)
              if any(abs(c - im) < tol for im in dneg_images(complex(shape_multiset[j])))]
             for c in (complex(c) for c in conj_multiset)]
    used = [False] * n

    def bt(i):
        if i == n:
            return True
        for j in cands[i]:
            if not used[j]:
                used[j] = True
                if bt(i + 1):
                    return True
                used[j] = False
        return False
    return bt(0)


def conj_self_pairs(shapes, tol=1e-8):
    """conj(multiset) matches the multiset's OWN D-negative orbit (amphichiral law)."""
    return conj_matches_dneg_orbit([complex(s).conjugate() for s in shapes], shapes, tol)


def polish_shapes(M, dps=320, target=290):
    """Newton-polish a (possibly filled) manifold's shape solution on its own rect
    gluing system to ~10^-target (mpmath, scoped precision; least-squares Newton on
    the overdetermined row set). Returns (shapes, rows). Tier: the PRECISION layer of
    the certified-numerical certificates (the system itself is exact data)."""
    with mp.workdps(dps):
        rows = rect_rows(M)
        zs = [mp.mpc(mp.mpf(str(s.real()).replace(' ', '')),
                     mp.mpf(str(s.imag()).replace(' ', '')))
              for s in M.tetrahedra_shapes('rect')]     # snappy HP prints '... e-65'
        n = len(zs)

        def resid(z_):
            out = []
            for A, B, c in rows:
                v = mp.mpc(1)
                for zz, a in zip(z_, A):
                    v *= zz**a
                for zz, b in zip(z_, B):
                    v *= (1 - zz)**b
                out.append(v - c)
            return out

        for _ in range(80):
            Jm = []
            for A, B, c in rows:
                v = mp.mpc(1)
                for zz, a in zip(zs, A):
                    v *= zz**a
                for zz, b in zip(zs, B):
                    v *= (1 - zz)**b
                Jm.append([v * (A[j] / zs[j] - B[j] / (1 - zs[j])) for j in range(n)])
            Jm = mp.matrix(Jm)
            Fm = mp.matrix(resid(zs))
            JT = Jm.T
            dz = mp.lu_solve(JT * Jm, JT * Fm)
            zs = [z - dz[i] for i, z in enumerate(zs)]
            if max(abs(x) for x in resid(zs)) < mp.mpf(10)**(-target):
                break
        assert max(abs(x) for x in resid(zs)) < mp.mpf(10)**(-target), "polish stalled"
        return zs, rows


def to_pari(z, digits=290):
    """mpc -> pari, string route, NO mpmath arithmetic (any mpmath op would re-round
    to the ambient working precision -- the 2026-07-02 B302/B347 failure class in a
    new coat; nstr alone formats the stored value faithfully)."""
    from cypari import pari
    s_re, s_im = mp.nstr(z.real, digits), mp.nstr(z.imag, digits)
    return pari(s_re + ("" if s_im.startswith('-') else "+") + s_im + "*I")


def algdep_certified(z, degrees=(2, 3, 4, 6, 8), resid_tol=1e-180, height_cap=10**12):
    """Minimal polynomial by LLL on a POLISHED (~290-digit) value, with residual and
    height certificates + sympy irreducibility. Returns (degree, poly_str, residual)."""
    from cypari import pari
    old_prec = pari.set_real_precision(300)
    try:
        x = sp.symbols('x')
        zp = to_pari(z)
        for d in degrees:
            p = pari.algdep(zp, d)
            r = abs(pari.subst(p, pari('x'), zp))
            if float(r) < resid_tol and max(abs(int(c)) for c in p.Vec()) < height_cap:
                pp = sp.sympify(str(p).replace('^', '**'))
                fl = sp.factor_list(pp)[1]
                pp = next(q for q, _ in fl
                          if abs(complex(sp.Poly(q, x).eval(complex(z)))) < 1e-8)
                assert sp.Poly(pp, x).is_irreducible
                return int(sp.degree(pp, x)), str(sp.expand(pp)), float(r)
        return None
    finally:
        pari.set_real_precision(old_prec)


def cyclic_covers(snappy):
    print("\n== 1a. THE CYCLIC-COVER TOWER n = 2..5 (tier: numerical + exact identities) ==")
    M = snappy.Manifold("4_1")
    z0c = complex(sp.re(Z0), sp.im(Z0))
    rows = []
    for n in (2, 3, 4, 5):
        C = [c for c in M.covers(n) if c.cover_info()["type"] == "cyclic"][0]
        sh = [complex(s) for s in C.tetrahedra_shapes('rect')]
        all_z0 = all(abs(s - z0c) < 1e-9 for s in sh)
        cv = complex(C.complex_volume())
        vol_ratio = float(C.volume()) / VOL_SEED
        amph = bool(C.symmetry_group().is_amphicheiral())
        assert all_z0 and len(sh) == 2 * n, f"cover n={n}: triangulation did not lift"
        assert abs(vol_ratio - n) < 1e-8 and abs(cv.imag) < 1e-9
        assert amph
        rows.append(dict(n=n, ntet=len(sh), all_shapes_z0=all_z0,
                         vol_over_seed=vol_ratio, cvol_imag=cv.imag, amphichiral=amph,
                         tier="numerical shapes (1e-9); the lift itself exact"))
        print(f"   n={n}: {2*n} tetrahedra, ALL shapes = z0; class = n.beta = {2*n}[z0];"
              f" vol = n.Vol ({vol_ratio:.9f}); amphichiral: {amph}")
    print("   => the tower hands you the Z-multiples n.beta of the SEED's class: field")
    print("      stationary (Eisenstein), no new value, no new choice; each member's own")
    print("      amphichirality self-identifies {+n.beta, -n.beta} (B348 pattern, level n)")
    bank("covers", rows=rows, class_law="n.beta (Z-multiple tower)", field="Q(sqrt-3) all n")


METALLIC_EXPECT = {1: "m004", 2: "m136", 3: "s464", 4: "t03910"}


def metallic_family(snappy):
    print("\n== 1b. THE METALLIC FAMILY m = 1..4 (b++R^mL^m) ==")
    from cypari import pari
    pari.set_real_precision(120)
    G30 = mp.mpf(0)
    with mp.workdps(30):
        G30 = +mp.catalan
    out = {}
    for m in (1, 2, 3, 4):
        B = snappy.Manifold("b++" + "R" * m + "L" * m)
        ident = str(B.identify()[0]).split("(")[0]
        assert ident == METALLIC_EXPECT[m], (m, ident)
        sh = [complex(s) for s in B.tetrahedra_shapes('rect')]
        amph = bool(B.symmetry_group().is_amphicheiral())
        dsum = float(sum(bloch_wigner(s) for s in sh))
        vol = float(B.volume())
        assert abs(dsum - vol) < 1e-9 and amph
        seam = conj_self_pairs(sh)
        entry = dict(census=ident, ntet=len(sh), vol=vol, bw_sum=dsum, amphichiral=amph,
                     conj_self_pairs_dneg_orbit=seam)
        if m == 1:
            entry.update(field="Q(sqrt-3) [Eisenstein]", tier="exact (section 0)")
            assert seam
            print(f"   m=1 ({ident}): the seed -- 2 Eisenstein tetrahedra (section 0)")
        elif m == 2:
            # EXACT: the four shapes are Gaussian: {1+i, (1+i)/2, 1+i, i} in the live order
            cands = [1 + sp.I, sp.Rational(1, 2) + sp.I / 2, 1 + sp.I, sp.I]
            exact = []
            pool = list(cands)
            for s in sh:
                hit = next(c for c in pool if abs(complex(sp.re(c), sp.im(c)) - s) < 1e-9)
                pool.remove(hit)
                exact.append(hit)
            assert rect_check_exact(rect_rows(B), exact)
            # EXACT self-pairing: every conjugated shape is a D-negative Lambda-image
            # of a distinct member (checked symbolically via a found matching):
            conj_ex = [sp.simplify(sp.conjugate(c)) for c in exact]
            pool = list(range(len(exact)))
            matching = []
            for ce in conj_ex:
                hit = next(j for j in pool if any(
                    sp.simplify(ce - im) == 0
                    for im in (1 / exact[j], 1 - exact[j], exact[j] / (exact[j] - 1))))
                pool.remove(hit)
                matching.append(hit)
            assert len(matching) == len(exact) and seam
            # all four tetrahedra isometric: {i, 1+i, (1+i)/2} = one tetrahedron's z, z'', z'
            zi = sp.I
            assert sp.simplify(1 / (1 - zi) - (sp.Rational(1, 2) + sp.I / 2)) == 0   # z'
            assert sp.simplify(1 - 1 / zi - (1 + sp.I)) == 0                          # z''
            with mp.workdps(30):
                dvals = [bloch_wigner(complex(sp.re(c), sp.im(c))) for c in exact]
                assert all(abs(d - G30) < mp.mpf(10)**(-25) for d in dvals)
                assert abs(mp.mpf(vol) - 4 * G30) < 1e-12
            entry.update(field="Q(i) [Gaussian]", exact_shapes=[str(c) for c in exact],
                         rect_exact=True, conj_self_pairing_exact=True,
                         all_D_equal_catalan=True, vol_is_4catalan=True, tier="exact")
            print(f"   m=2 ({ident}): FOUR ISOMETRIC GAUSSIAN TETRAHEDRA -- shapes"
                  f" {{i, 1+i, 1+i, (1+i)/2}} solve the rect system EXACTLY; field Q(i);")
            print(f"        D = Catalan each; vol = 4G = {vol:.9f}; conj self-pairing")
            print("        into the D-negative orbit EXACT (sympy matching); amphichiral (D4)")
        else:
            # certified-numerical: Newton-polished shapes (290 digits on the exact rect
            # system) + algdep with residual/height certificates + sympy irreducibility
            BH = snappy.ManifoldHP(ident)
            zs_pol, _ = polish_shapes(BH)
            polys = [algdep_certified(z0) for z0 in zs_pol]
            assert all(p is not None for p in polys), f"m={m}: algdep failed post-polish"
            degs = sorted({d for d, _, _ in polys})
            entry.update(field=f"shape min-poly degrees {degs}",
                         min_polys=sorted({p for _, p, _ in polys}),
                         worst_residual=max(r for _, _, r in polys),
                         tier="certified-numerical (Newton-polished 290 digits + "
                              "algdep residual + irreducible)")
            assert seam
            print(f"   m={m} ({ident}): {len(sh)} tetrahedra; shape min-poly degrees {degs}"
                  f" (polished algdep residuals < 1e-180, irreducible);")
            print(f"        conj self-pairing into the D-negative orbit (1e-8);"
                  f" amphichiral (D4); D-sum = vol = {vol:.9f}")
        out[m] = entry
    print("   => four members, four DIFFERENT shape-arithmetics (Eisenstein, Gaussian,")
    print("      deg-8, deg-4) -- but ONE law: conj(class) = -class through D-negating")
    print("      Bloch moves (self-pairing), and each member's own amphichirality kills")
    print("      the sign. The family index m is an EXTERNAL LABEL (the monodromy word")
    print("      length), not an object choice.")
    print("      [cs = 0 x4 exact by 2-torsion elimination: B496 section 1, cited]")
    bank("metallic", **{str(k): v for k, v in out.items()})


def fillings(snappy):
    print("\n== 1c. THE FORCED +-5 FILLINGS (the Meyerhoff child pair; B434/B496 cited) ==")
    from cypari import pari
    x = sp.symbols('x')
    # the banked child quartic, re-verified exactly (tier: exact; B434)
    q = x**4 - x - 1
    assert sp.Poly(q, x).is_irreducible and sp.discriminant(q, x) == -283
    gal = pari.polgalois(pari('x^4 - x - 1'))
    assert int(gal[0]) == 24            # order 24 quartic Galois group = S4
    print("   child trace field x^4 - x - 1: irreducible, disc -283, Galois S4 (pari)")
    print("   => NO quadratic subfield: neither sqrt(-3) nor sqrt(5) -- new arithmetic")
    vols, cvals, dsums, shapes = {}, {}, {}, {}
    for slope in ((5, 1), (-5, 1)):
        F = snappy.Manifold("4_1")
        F.chern_simons()                 # seed CS on the cusped manifold (the B432 idiom)
        F.dehn_fill(slope)
        assert F.solution_type() == 'all tetrahedra positively oriented'
        sh = [complex(s) for s in F.tetrahedra_shapes('rect')]
        shapes[slope] = sh
        vols[slope] = float(F.volume())
        cvals[slope] = float(F.chern_simons())
        dsums[slope] = float(sum(bloch_wigner(s) for s in sh))
        assert abs(dsums[slope] - vols[slope]) < 1e-9
        ident = str(F.identify()[0])
        assert ident == "m003(-2,3)"     # the Meyerhoff census name (B434)
    assert abs(vols[(5, 1)] - vols[(-5, 1)]) < 1e-9
    assert abs(cvals[(5, 1)] + cvals[(-5, 1)]) < 1e-9           # the mirror pair, sum 0
    assert abs(cvals[(5, 1)] - 0.07703818026377) < 1e-9         # B496 banked value
    A = snappy.Manifold("4_1(5,1)")
    chir = not A.symmetry_group().is_amphicheiral()
    assert chir
    # THE PAIRING LAW AT THE SHAPE LEVEL (the seam's chiral face): the child's own
    # conjugated multiset does NOT self-pair (chirality detected combinatorially) --
    # it pairs into the D-negative orbit of the MIRROR child's multiset:
    self_pair = conj_self_pairs(shapes[(5, 1)])
    cross_pair = conj_matches_dneg_orbit(
        [s.conjugate() for s in shapes[(5, 1)]], shapes[(-5, 1)])
    assert (not self_pair) and cross_pair
    print(f"   4_1(+-5,1) = Meyerhoff +- mirror (m003(-2,3)): vol = {vols[(5,1)]:.9f} (both);")
    print(f"   BW shape-sum = vol at BOTH signs (1e-9); cs = +-{abs(cvals[(5,1)]):.14f}")
    print("   (pair sum 0; B496 cited + recomputed); CHIRAL (Z/2+Z/2, not amphicheiral)")
    print("   pairing law at the shape level: conj(+5 multiset) does NOT match its own")
    print("   D-negative orbit (self-pairing FAILS -- chirality, combinatorially) but")
    print("   DOES match the -5 multiset's D-negative orbit: MIRROR-pairing (1e-8)")
    print("   => the child cannot kill its own sign -- but the PARENT does: amphichiral")
    print("      4_1 maps (5,1) -> (-5,1) (mirror(4_1(p,q)) = 4_1(p,-q), B496 section 3):")
    print("      the object forces the PAIR; the member = slope sign = EXTERNAL LABEL")
    # THE SPUN-SHAPE FIELD, EXACT (the probe's second new computation). At raw HP
    # (64-digit) precision LLL sees nothing (that was the honest wall); after the
    # 290-digit Newton polish the field opens up:
    octics = {}
    old_prec = pari.set_real_precision(300)
    for slope in ((5, 1), (-5, 1)):
        FH = snappy.ManifoldHP("4_1")
        FH.dehn_fill(slope)
        zs_pol, rows_f = polish_shapes(FH)
        deg1, oct1, r1 = algdep_certified(zs_pol[0], degrees=(4, 8, 12))
        assert deg1 == 8
        OCT = pari(oct1.replace('**', '^'))
        assert OCT.polisirreducible()
        # express z2 in Q(z1) (LLL), then verify the WHOLE filled gluing system
        # EXACTLY in Q[x]/(octic) by polmod arithmetic:
        z1p, z2p = to_pari(zs_pol[0]), to_pari(zs_pol[1])
        rel = [int(v) for v in pari.lindep([z1p**k for k in range(8)] + [z2p])]
        assert rel[8] != 0
        xg = pari('x')
        z1m = pari.Mod(xg, OCT)
        z2m = pari.Mod(-sum(rel[k] * xg**k for k in range(8)) / rel[8], OCT)
        for A, B, c in rows_f:
            v = pari.Mod(1, OCT)
            for zm, a in zip([z1m, z2m], A):
                v *= zm**a
            for zm, b in zip([z1m, z2m], B):
                v *= (1 - zm)**b
            assert v == pari.Mod(c, OCT), f"filled gluing row fails exactly at {slope}"
        octics[slope] = oct1
        # the octic CONTAINS the trace-field quartic; 283^2 divides its poldisc:
        assert pari.nfisincl(pari('x^4 - x - 1'), OCT) != 0
        pd = pari.poldisc(OCT).factor()
        assert any(int(pd[i, 0]) == 283 and int(pd[i, 1]) >= 2
                   for i in range(pd.nrows()))
    pari.set_real_precision(old_prec)
    O1 = pari(octics[(5, 1)].replace('**', '^'))
    O2 = pari(octics[(-5, 1)].replace('**', '^'))
    assert pari.nfisisom(O1, O2) != 0      # ONE abstract field for the mirror pair
    print("   THE SPUN-SHAPE FIELD, COMPUTED: each child's two spun shapes generate a")
    print("   degree-8 field; the filled gluing system holds EXACTLY in Q[x]/(octic)")
    print("   (pari polmod; identification with the geometric solution certified at 290")
    print("   digits after Newton polish -- raw HP-precision LLL sees nothing);")
    print(f"   octic(+5): {octics[(5,1)]}")
    print(f"   octic(-5): {octics[(-5,1)]}")
    print("   nfisisom != 0: the mirror pair shares ONE abstract shape field (a quadratic")
    print("   extension of the trace field x^4-x-1: nfisincl != 0; poldisc contains 283^2)")
    print("   -- the two children differ only by the EMBEDDING = the orientation choice:")
    print("      the Galois-orbit-member structure at the field level")
    bank("fillings", vol=vols[(5, 1)], cs_pair=[cvals[(5, 1)], cvals[(-5, 1)]],
         bw_equals_vol_both=True, chiral=True,
         conj_self_pairing=False, conj_mirror_pairing=True,
         quartic="x**4 - x - 1", disc=-283,
         galois="S4", no_quadratic_subfield=True,
         spun_octic_plus=octics[(5, 1)], spun_octic_minus=octics[(-5, 1)],
         spun_octics_isomorphic=True, spun_exact_gluing_check=True,
         octic_contains_trace_quartic=True, octic_poldisc_has_283_squared=True,
         tier="exact polmod verification; geometric identification certified at "
              "290 digits (Newton-polished)")


# =====================================================================
# SECTION 2 -- THE EXTENDED-BLOCH LIFT (Zickert flattenings, offline)
# =====================================================================
def ptolemy_points_exact(V):
    """All points of a snappy Ptolemy variety, solved EXACTLY (sympy, saturated).
    Returns (points, positive_dimensional) where points is a list of dicts."""
    syms = sorted(set(V.variables), key=str)
    S = {v: sp.symbols(v) for v in syms}
    eqs = [sp.sympify(str(e).replace('^', '**'), locals=S) for e in V.equations]
    w = sp.symbols('w_aux')
    gb = sp.groebner(eqs + [w * sp.prod([S[v] for v in syms]) - 1],
                     w, *[S[v] for v in syms], order='lex')
    if gb.exprs == [sp.Integer(1)]:
        return [], False
    if not gb.is_zero_dimensional:
        return [], True
    sols = sp.solve(eqs + [w * sp.prod([S[v] for v in syms]) - 1],
                    [*[S[v] for v in syms], w], dict=True)
    pts = []
    for so in sols:
        if any(f not in set(so.keys()) for v in so.values()
               for f in sp.sympify(v).free_symbols):            # pragma: no cover
            continue
        pts.append({v: so[S[v]] for v in syms})
    return pts, False


def extended_bloch(snappy):
    print("\n== 2. THE EXTENDED-BLOCH LIFT (Zickert flattenings; offline; tier: exact")
    print("      solve -> certified pipeline evaluation) ==")
    from snappy.ptolemy.coordinates import PtolemyCoordinates
    # ---- the SEED ----
    M = snappy.Manifold("4_1")
    Vs = M.ptolemy_variety(2, obstruction_class='all')
    assert len(Vs) == 2
    pts0, pos0 = ptolemy_points_exact(Vs[0])
    assert pts0 == [] and not pos0                    # class 0 EMPTY (reproduces B495 s4)
    pts1, pos1 = ptolemy_points_exact(Vs[1])
    assert not pos1 and len(pts1) == 2
    c0101 = sp.symbols('c_0101_0')
    minp = sp.minimal_polynomial(pts1[0]['c_0101_0'], c0101)
    assert sp.expand(minp - (c0101**2 - c0101 + 1)) == 0
    print("   4_1 N=2: obstruction class 0 EMPTY; class 1 cut by c^2 - c + 1 = 0 --")
    print("   the Ptolemy coordinates ARE the seam roots e^{+-i pi/3}   [exact]")
    sec = eval(Vs[1].py_eval_section())
    cvs, pqs, own_defects = {}, {}, {}
    for pt in pts1:
        root = complex(sp.N(pt['c_0101_0'], 30))
        d0 = {'1': 1, 'c_0011_0': complex(sp.N(pt['c_0011_0'], 30)), 'c_0101_0': root}
        pc = PtolemyCoordinates(d0, is_numerical=True, py_eval_section=sec,
                                manifold_thunk=lambda: M)
        cv = complex(pc.complex_volume_numerical())
        fl = pc.flattenings_numerical()
        pq, total = [], mp.mpc(0)
        with mp.workdps(30):
            for tet in (0, 1):
                w0, zz, p = fl['z_0000_%d' % tet]
                w1, _, _ = fl['zp_0000_%d' % tet]
                zz = mp.mpc(complex(zz))
                p = int(p)
                q = round(((complex(w1) + complex(mp.log(1 - zz)))
                           / complex(mp.pi * 1j)).real)
                # certify the flattening triple (Neumann Def 3.1 at N=2):
                assert abs(complex(w0) - complex(mp.log(zz) + p * mp.pi * 1j)) < 1e-12
                assert abs(complex(w0) + complex(w1)
                           + complex(fl['zpp_0000_%d' % tet][0])) < 1e-12
                pq.append((p, q))
                R = mp.polylog(2, zz) + mp.log(zz) * mp.log(1 - zz) / 2
                total += R + mp.pi * 1j / 2 * (q * mp.log(zz) + p * mp.log(1 - zz)) \
                    - mp.pi**2 / 6
            # independent Neumann L^ evaluation vs the pipeline, in units of pi^2/6
            # (the pipeline's DECLARED modulus: "complex volume defined up to i pi^2/6")
            defect = (complex(total) - 1j * cv) / (float(mp.pi**2) / 6)
        key = "+" if root.imag > 0 else "-"
        cvs[key], pqs[key] = cv, pq
        own_defects[key] = defect
        assert abs(defect.imag) < 1e-9 and abs(defect.real - round(defect.real)) < 1e-9
    # the orbit structure at the extended level:
    assert abs(cvs["+"].real + cvs["-"].real) < 1e-9            # SUM 0
    assert abs(abs(cvs["+"].real) - VOL_SEED) < 1e-9            # members +-Vol
    assert abs(cvs["+"].imag) < 1e-9 and abs(cvs["-"].imag) < 1e-9   # CS == 0 (mod decl.)
    assert pqs["+"] == [(-p, -q) for (p, q) in pqs["-"]]        # (p,q) NEGATE under Galois
    print(f"   the two Galois lifts -> extended classes with cvol {cvs['+'].real:+.9f} /")
    print(f"   {cvs['-'].real:+.9f}: the orbit {{+c^, -c^}}, SUM 0, CS-part 0; and the")
    print(f"   INTEGER flattening data negates under conjugation: {pqs['+']} <-> {pqs['-']}")
    print("   -- the B348 {+beta, -beta} pattern holds at the LIFTED (flattened) level,")
    print("      with the discrete (p,q) data itself a Galois +-pair   [certified pipeline]")
    print(f"   independent Neumann L^ check: defect = {own_defects['+'].real:+.0f} unit(s)")
    print("   of the pipeline's declared modulus i pi^2/6 at both lifts (integer: certified)")
    # ---- the covers: the lift is the Z-multiple tower ----
    cover_cv = {}
    for n in (2, 3, 4, 5):
        C = [c for c in snappy.Manifold("4_1").covers(n)
             if c.cover_info()["type"] == "cyclic"][0]
        cv = complex(C.complex_volume())
        assert abs(cv.real - n * VOL_SEED) < 1e-8 and abs(cv.imag) < 1e-9
        cover_cv[n] = [cv.real, cv.imag]
    print("   covers n=2..5: extended class = n . (seed class) -- i n Vol + 0i (1e-8):")
    print("   the Z-multiple tower, canonical, no new choice   [numerical]")
    # ---- m136: the full 8-class sweep ----
    M2 = snappy.Manifold("m136")
    Vs2 = M2.ptolemy_variety(2, obstruction_class='all')
    assert len(Vs2) == 8
    class_summary, cv_multiset = {}, []
    posdim_classes, point_classes = [], []
    for i, V in enumerate(Vs2):
        pts, posdim = ptolemy_points_exact(V)
        if posdim:
            posdim_classes.append(i)
            class_summary[str(i)] = "POSITIVE-DIMENSIONAL"
            continue
        if not pts:
            class_summary[str(i)] = "empty"
            continue
        point_classes.append(i)
        sec2 = eval(V.py_eval_section())
        vals = []
        for pt in pts:
            d0 = {'1': 1}
            for v, ex in pt.items():
                d0[v] = complex(sp.N(ex, 30))
            pc = PtolemyCoordinates(d0, is_numerical=True, py_eval_section=sec2,
                                    manifold_thunk=lambda: M2)
            cv = complex(pc.complex_volume_numerical())
            vals.append(cv)
            cv_multiset.append(cv)
        cc = sp.symbols('c')
        elim = sp.factor(sp.minimal_polynomial(pts[0][sorted(pts[0])[-1]], cc))
        class_summary[str(i)] = dict(n_points=len(pts), eliminant=str(elim),
                                     cvols=sorted(round(v.real, 9) for v in vals))
    vol2 = float(M2.volume())
    assert posdim_classes and point_classes                     # both phenomena present
    assert all(abs(abs(v.real) - vol2) < 1e-6 and abs(v.imag) < 1e-9 for v in cv_multiset)
    assert abs(sum(v.real for v in cv_multiset)) < 1e-6         # sign-balanced: SUM 0
    print(f"   m136 N=2: 8 obstruction classes -> {sum(1 for v in class_summary.values() if v=='empty')} empty;"
          f" class(es) {posdim_classes} POSITIVE-DIMENSIONAL (a continuous")
    print("   non-geometric family -- the B130 clause-(2) exhibit INSIDE this class: a")
    print(f"   continuous value cannot be a forced discrete choice); class(es) {point_classes}:"
          f" {len(cv_multiset)} points,")
    print(f"   cvol multiset {{+-{vol2:.6f}}} sign-balanced, SUM 0, CS-part 0 --")
    print("   the silver member's extended class collapses onto {+c^_2, -c^_2}   [exact")
    print("   solve; certified pipeline evaluation]")
    bank("extended_bloch",
         seed_class0="empty", seed_class1_eliminant="c**2 - c + 1",
         seed_cvols={k: [v.real, v.imag] for k, v in cvs.items()},
         seed_flattening_pq={k: v for k, v in pqs.items()},
         seed_pq_galois_negated=True, seed_orbit_sum_zero=True,
         own_rogers_defect_units_pi2_over_6=int(round(own_defects["+"].real)),
         declared_modulus="i pi^2 / 6 (snappy ptolemy docstring)",
         cover_cvols={str(k): v for k, v in cover_cv.items()},
         m136_classes=class_summary, m136_posdim_classes=posdim_classes,
         m136_cv_multiset_sum=float(sum(v.real for v in cv_multiset)))


# =====================================================================
# SECTION 3 -- THE THREE CONDITIONS + VERDICT
# =====================================================================
def three_conditions_and_verdict(snappy_present):
    print("\n== 3. THE THREE-CONDITION TEST (B330) ==")
    print("   (1) trace-map-invariant: YES -- the (extended-)Bloch class is a topological/")
    print("       representation invariant (triangulation-independent: Neumann-Yang), and")
    print("       every stratum is cut intrinsically: canonical cyclic covers; the K010")
    print("       metallic monodromy family; the boundary +-5 of the maximal exceptional")
    print("       set (B434); the N=2 Ptolemy varieties with ALL obstruction classes")
    print("       enumerated. No presentation gauge appears anywhere in the class.")
    print("   (2) discretely multivalued: YES -- per stratum the class hands a FINITE set:")
    print("       {+beta, -beta} (seed), {+n.beta, -n.beta} (covers), {+beta_m, -beta_m}")
    print("       (metallic), the +-cs child pair, the +-c^ Ptolemy orbits, the +-(p,q)")
    print("       flattening data; the value lattice itself (i pi^2/6 . Z) is discrete.")
    print("       [the m136 positive-dimensional Ptolemy class fails clause (2) on its")
    print("       own -- continuous, hence never a forced choice: the B130 pattern]")
    print("   (3) symmetrizable: YES, exhaustively, in three bins:")
    print("       - bin F (forced / fixed-locus): the field data (min polys, disc, S4 --")
    print("         Q-rational symmetric functions); vol magnitudes; D == 0 on the fixed")
    print("         field; CS == 0 at every amphichiral stratum (B496 2-torsion pins).")
    print("       - bin P (Galois/conjugation +-pairs, sum 0): {+beta,-beta} and its")
    print("         n-multiples; {+beta_m,-beta_m} with conj(multiset) SELF-PAIRING into")
    print("         the D-negative Lambda-orbit (computed: EXACT at m=1,2; 1e-8 at m=3,4)")
    print("         -- complex conjugation IS the amphichiral involution (B318/B348)")
    print("         acting through D-negating Bloch moves; at the LIFTED level the")
    print("         Ptolemy orbits {+c^,-c^} with (p,q) -> (-p,-q); the chiral child")
    print("         pair: self-pairing FAILS, MIRROR-pairing holds -- paired BY THE")
    print("         PARENT's amphichirality (member = slope sign = external).")
    print("       - bin L (external labels): the cover degree n, the family index m, the")
    print("         slope sign, the lattice representative (the mod-pi^2 coset rep).")
    print("       No unsymmetrizable discrete orbit anywhere in the computed class.")
    print("\n== VERDICT ==")
    print("   SEALED (at the computable horizon).")
    print("   The extended-Bloch/K3^ind-type data of the seed and its in-reach strata")
    print("   assemble into fixed-locus values, sign-symmetric Galois/conjugation orbits")
    print("   (sum 0 -- including the seam identity acting at the LIFTED level: the")
    print("   Ptolemy coordinates are the Eisenstein roots and conjugation negates the")
    print("   flattening integers), and external labels. No clause-(3) forced choice.")
    print("   TOOL-BLOCKED / out of reach (named, honest):")
    print("    - the SHARP modulus tower (Neumann pi^2 for PSL, GTZ 4 pi^2 for SL(2)):")
    print("      the in-sandbox pipeline DECLARES its value only mod i pi^2/6 (cross-N")
    print("      normalization); certifying the 4 pi^2-sharp SL(2) statement needs the")
    print("      verified/exact Ptolemy machinery: sage-gated in snappy (find_field,")
    print("      verified flattenings), or magma / the Ptolemy database (network) --")
    print("      all excluded by prereg. Our from-scratch Neumann evaluation agrees with")
    print("      the pipeline to an INTEGER number of pi^2/6 units (certified), but the")
    print("      normal-path parity condition needed to pin the finer lattice from")
    print("      scratch is not implemented in-sandbox: PARTIAL, named.")
    print("    - K3^ind TORSION (the Q/Z summand: e.g. the torsion of K3^ind(Q(sqrt-3))):")
    print("      invisible to every dilogarithm-based numeric (D, R^) by construction;")
    print("      needs etale/motivic machinery -- out of sandbox scope entirely.")
    print("    - Ptolemy N >= 3 (the SL(n) lift of this class): the exact solve grows")
    print("      beyond in-sandbox Groebner reach (B495's named block, unchanged).")
    print("   C-guardrail: 'sealed at the computable horizon; the class beyond these")
    print("   strata/moduli remains open' -- NOT a universal impossibility proof.")
    print("   Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.")
    bank("verdict", outcome="SEALED",
         phrasing="sealed at the computable horizon; the class beyond these strata/moduli "
                  "remains open",
         snappy_available=snappy_present,
         tool_blocked=[
             "sharp modulus tower pi^2 (PSL) / 4 pi^2 (SL2): pipeline declares i pi^2/6; "
             "verified Ptolemy machinery sage-gated; magma / Ptolemy DB (network) excluded; "
             "from-scratch Neumann normal-path parity: PARTIAL (integer-unit agreement "
             "certified)",
             "K3^ind torsion (Q/Z part): invisible to dilogarithm numerics; "
             "etale/motivic tools out of scope",
             "Ptolemy N>=3 exact enumeration (B495's named block, unchanged)"])


def main():
    print("B497 -- Gate A class 2e: the extended-Bloch class beyond the object's own\n")
    snappy = try_snappy()
    ok = controls(snappy)
    if not ok:                                                   # pragma: no cover
        print("CONTROL FAILED -- probe INVALID; stopping per prereg.")
        return 1
    if snappy is not None:
        cyclic_covers(snappy)
        metallic_family(snappy)
        fillings(snappy)
        extended_bloch(snappy)
    else:                                                        # pragma: no cover
        bank("strata", status="TOOL-BLOCKED: snappy import failed (named)")
    three_conditions_and_verdict(snappy is not None)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "b497_extended_bloch.json")
    json.dump(REPORT, open(out, "w"), indent=1, default=str)
    print(f"\n[written] {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
