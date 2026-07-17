"""B666 cell 9, TASK B (R21-3), part 2: the DISCRETE-branch ID per word.

The discriminating fact, computed in-sandbox per word w:

  The once-punctured-torus bundle M_w = snappy.Manifold('b++'+w) (constructor
  verified: b++RL isometric to m004, b++RRLL isometric to m136).  For the
  adjoint (m=1, Sym^2) twisted Alexander/Wada torsion polynomial of M_w at
  the DISCRETE holonomy, taken w.r.t. the fibration class alpha (the unique
  Z-class; free rank of H1 is 1 for every word here), Milnor's fibration
  theorem gives: the monic-normalized torsion polynomial equals
      t^j * (t - 1)(t^2 - J t + 1)
  where {1, mu, 1/mu} are the eigenvalues of the monodromy acting on
  H^1(F; sl_2) = T X(F_2) = the (x,y,z) trace-variety tangent space at the
  discrete fixed character, and J = mu + 1/mu is exactly B626's branch
  invariant.  So the pipeline (B627's, verbatim) run on M_w's presentation
  reads off J_disc of the DISCRETE branch -- with no fiber-generator
  matching problem at all.  Calibration anchors: the banked fig-8
  tau_1 = -3 = 2 - 5 and silver tau_1 = -16 = 2 - 18 force J_disc(RL) = 5,
  J_disc(RRLL) = 18.

  The polished holonomy is taken at bits_prec=1200 (~360 digits) via
  polished_holonomy -- NOT ManifoldHP quad-double (the diagnosed B627
  input-precision ceiling); pipeline dps=300.

  The ID: match J_disc (>= 100 solid digits) against the EXACT branch
  inventory (cell9_taskB_branches.py, sympy-exact J values); certificate =
  match distance vs the minimum inter-branch separation.
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '/Users/dri/origin-axiom/frontier/B627_silver_heldout')
import pipeline as pl

WORDS = ['RL', 'RRL', 'RLRL', 'RRLL', 'RRRL', 'RRRRL', 'RRLLL', 'RRRLLL']
DPS = 300
BITS = 1200


def get_polished_holonomy(name, dps):
    import snappy
    mp.mp.dps = dps + 20
    M = snappy.Manifold(name)
    try:
        G = M.polished_holonomy(bits_prec=BITS)
    except TypeError:
        # SnapPy's lift_to_SL2C crashes on multi-torsion H1 (the B649-noted
        # bug); the PSL rep is fine here -- Sym^2 factors through PSL2.
        G = M.polished_holonomy(bits_prec=BITS, lift_to_SL2=False)
    gens = G.generators()
    relators = G.relators()

    def _s(x):
        return str(x).replace(' ', '').replace('E', 'e')

    out = {}
    for g in gens:
        m2 = G.SL2C(g)
        out[g] = mp.matrix([[mp.mpc(_s(m2[0, 0].real()), _s(m2[0, 0].imag())),
                             mp.mpc(_s(m2[0, 1].real()), _s(m2[0, 1].imag()))],
                            [mp.mpc(_s(m2[1, 0].real()), _s(m2[1, 0].imag())),
                             mp.mpc(_s(m2[1, 1].real()), _s(m2[1, 1].imag()))]])
    return M, gens, relators, out


def torsion_J(word):
    """Run the m=1 (adjoint) pipeline on b++word; extract J_disc from the
    monic quotient poly, asserting the (t-1)(t^2-Jt+1) shape."""
    name = 'b++' + word
    M, gens, relators, acts = get_polished_holonomy(name, DPS)
    assert len(relators) == len(gens) - 1, "not deficiency 1"
    alpha = pl.alpha_map(gens, relators)
    # verify holonomy precision: relator images
    for rel in relators:
        Mm = mp.eye(2)
        for ch in rel:
            gm = acts[ch.lower()]
            if ch.isupper():
                gm = gm ** -1
            Mm = Mm * gm
        dev = max(abs(Mm[0, 0] - 1), abs(Mm[0, 1]), abs(Mm[1, 0]),
                  abs(Mm[1, 1] - 1))
        dev_pm = max(abs(Mm[0, 0] + 1), abs(Mm[0, 1]), abs(Mm[1, 0]),
                     abs(Mm[1, 1] + 1))
        assert min(dev, dev_pm) < mp.mpf(10) ** (-250), \
            f"holonomy precision too low: {mp.nstr(min(dev,dev_pm),3)}"
    # dropped generator: any with alpha != 0
    dropped = next(g for g in gens if alpha[g] != 0)
    kept = [g for g in gens if g != dropped]
    tau, qn, maxrel, qdeg = pl.compute_tau_exact(
        1, gens, relators, kept, dropped, acts, alpha, dps=DPS,
        log=None, extra=8, probe_dps=100)
    # strip (numerically) zero coefficients at both ends
    tol = mp.mpf(10) ** (-100)
    lo = 0
    while lo < len(qn) and abs(qn[lo]) < tol:
        lo += 1
    core = qn[lo:]
    assert len(core) == 4, f"core degree != 3: {[mp.nstr(c,5) for c in qn]}"
    c0, c1, c2, c3 = core
    # shape: (t-1)(t^2 - J t + 1) = t^3 - (J+1) t^2 + (J+1) t - 1
    assert abs(c3 - 1) < tol and abs(c0 + 1) < tol and abs(c1 + c2) < tol, \
        f"shape violation: {[mp.nstr(c, 30) for c in core]}"
    J = c1 - 1
    return J, maxrel, M.volume(), qdeg, lo


def pslq_minpoly(Jval, maxdeg=8, prec_digits=200):
    """Independent certificate: the exact minimal polynomial of the numeric
    J_disc via PSLQ on (1, J, J^2, ...), lowest degree that yields an
    integer relation verifiable to high precision."""
    old = mp.mp.dps
    mp.mp.dps = prec_digits + 50
    try:
        for deg in range(1, maxdeg + 1):
            vec = []
            for k in range(deg + 1):
                z = Jval ** k
                vec.append(z)
            # PSLQ needs real input: run on real and imaginary stacked
            # (relation must kill both), so use the real embedding trick:
            # find integer c_k with sum c_k J^k = 0 -- do PSLQ on the
            # complex vector via two-row lattice: mpmath pslq handles real
            # only; use Re and Im interleaved with a common relation.
            re_vec = [mp.re(v) for v in vec]
            im_vec = [mp.im(v) for v in vec]
            if max(abs(v) for v in im_vec) < mp.mpf(10) ** (-(prec_digits // 2)):
                rel = mp.pslq(re_vec, maxcoeff=10 ** 12,
                              maxsteps=200000)
            else:
                # complex J: kill Re and Im simultaneously via pslq over
                # the vector of Re parts of (J^k) and i-parts folded:
                # mp.pslq accepts complex? It does accept complex vectors.
                rel = mp.pslq(vec, maxcoeff=10 ** 12, maxsteps=200000)
            if rel is None:
                continue
            resid = sum(c * vec[k] for k, c in enumerate(rel))
            if abs(resid) < mp.mpf(10) ** (-(prec_digits - 40)):
                return rel
        return None
    finally:
        mp.mp.dps = old


def main():
    import sympy as sp
    lam = sp.Symbol('lam')
    spectra = json.load(open('/Users/dri/origin-axiom/frontier/'
                             'B666_leads_campaign/cell9/taskB_jspectrum.json'))
    mp.mp.dps = 320
    results = {}
    for w in WORDS:
        print(f"===== word {w} (b++{w}) =====", flush=True)
        t0 = time.time()
        J_disc, maxrel, vol, qdeg, lo = torsion_J(w)
        print(f"  J_disc = {mp.nstr(J_disc, 45)}")
        print(f"  (vol {mp.nstr(vol, 12)}, fit maxrel {mp.nstr(maxrel, 3)}, "
              f"qdeg {qdeg}, t-power {lo}, {time.time()-t0:.0f}s)")
        # candidate roots: every (sign class, irreducible factor, root)
        cands = []
        for cls, rec in spectra[w].items():
            if rec.get('status') != 'OK':
                continue
            for fd in rec['factors']:
                fpoly = sp.Poly(sp.sympify(fd['factor']), lam)
                roots = mp.polyroots([mp.mpf(int(c)) for c in
                                      fpoly.all_coeffs()], maxsteps=200,
                                     extraprec=200)
                for ri, r in enumerate(roots):
                    d = abs(J_disc - r)
                    cands.append((d, cls, fd['factor'], ri, r, fd['mult']))
        cands.sort(key=lambda t: t[0])
        best = cands[0]
        sep = min((c[0] for c in cands[1:] if abs(c[4] - best[4]) > 1e-18),
                  default=mp.mpf('inf'))
        classes_sharing = sorted(set(c[1] for c in cands
                                     if abs(c[4] - best[4]) < 1e-18))
        print(f"  MATCHED branch: root #{best[3]} of {best[2]}  "
              f"~ {mp.nstr(best[4], 30)}")
        print(f"    sign classes carrying it: {classes_sharing}")
        print(f"    match distance {mp.nstr(best[0], 3)}; next-nearest "
              f"DISTINCT root at distance {mp.nstr(sep, 3)}")
        assert best[0] < mp.mpf(10) ** (-40), "no branch matches!"
        assert sep > mp.mpf(10) ** (-6), "branch separation too small"
        # independent certificate: evaluate EVERY candidate irreducible
        # factor at J_disc -- the matched factor must vanish to ~200 digits
        # while every other factor stays far from zero.
        factor_vals = {}
        for cls, rec in spectra[w].items():
            if rec.get('status') != 'OK':
                continue
            for fd in rec['factors']:
                if fd['factor'] in factor_vals:
                    continue
                fpoly = sp.Poly(sp.sympify(fd['factor']), lam)
                val = mp.mpc(0)
                for c in fpoly.all_coeffs():
                    val = val * J_disc + int(c)
                factor_vals[fd['factor']] = abs(val)
        matched_val = factor_vals[best[2]]
        other_min = min((v for f, v in factor_vals.items() if f != best[2]),
                        default=mp.mpf('inf'))
        print(f"    factor-evaluation certificate: |P_matched(J_disc)| = "
              f"{mp.nstr(matched_val, 3)}; min over other factors = "
              f"{mp.nstr(other_min, 3)}")
        assert matched_val < mp.mpf(10) ** (-150), "matched factor not ~0"
        assert other_min > mp.mpf(10) ** (-6), "another factor also ~0"
        pslq_str = None
        results[w] = dict(J_disc_numeric=mp.nstr(J_disc, 60),
                          matched_factor=best[2],
                          matched_root_index=int(best[3]),
                          matched_root_numeric=mp.nstr(best[4], 40),
                          sign_classes=classes_sharing,
                          match_distance=mp.nstr(best[0], 5),
                          next_nearest=mp.nstr(sep, 5),
                          pslq_minpoly=pslq_str,
                          volume=mp.nstr(mp.mpf(str(vol)), 15))
        json.dump(results, open('/Users/dri/origin-axiom/frontier/'
                                'B666_leads_campaign/cell9/'
                                'taskB_discrete_id.json', 'w'), indent=1)
    # calibration gates (the banked anchors)
    JRL = sp.Poly(sp.sympify(results['RL']['matched_factor']), lam)
    assert JRL.degree() == 1 and sp.sympify(
        results['RL']['matched_factor']).subs(lam, 5) == 0, "RL anchor failed"
    assert sp.sympify(results['RRLL']['matched_factor']).subs(lam, 18) == 0, \
        "RRLL anchor failed"
    print("\nCALIBRATION ANCHORS: RL -> J=5 (= 2-(-3), banked fig-8 tau_1), "
          "RRLL -> J=18 (= 2-(-16), banked silver tau_1): PASS")
    # the Chebyshev double-cover consistency: RLRL = (RL)^2
    print(f"RLRL double-cover consistency: matched root "
          f"{results['RLRL']['matched_root_numeric']} vs J(RL)^2-2 = 23")
    print("DONE")


if __name__ == '__main__':
    main()
