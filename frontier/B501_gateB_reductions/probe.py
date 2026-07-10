"""B501 -- CL-3B: Gate B in-sandbox reductions (Closure Campaign, Phase 3).

Pre-registered in docs/CLOSURE_CAMPAIGN_2026-07.md (CL-3B) + frontier/B501_gateB_reductions/README.md.
Enum per piece (committed): REDUCED / NEGATIVE / TOOL-BLOCKED. CLOSED is deliberately absent.
Firewalled; mathematics only; nothing promotes to CLAIMS.md.

PIECE 1 -- the sigma-stability register (H103/H104): a DECLARED bounded search for a chiral
(non-sigma-stable) 2T -> E6 embedding.
  Search space (declared exactly): all faithful 27-dim character assemblies V of G in {2T, A4}
  with (Sym^3 V)^G != 0 and complex character -- the B356 chirality window (70262 for 2T, 1028
  for A4; counts re-derived here, gated against the banked values). Every actual embedding
  G -> E6(C) (simply connected E6, acting on the 27) restricts the E6 tensor hierarchy, so the
  window is sieved by three EXACT necessary conditions:
    C1 (cross map)   Sym^2(27) = 27bar + V(2w1)  =>  Vbar <= Sym^2 V as G-characters;
    C3 (torsion)     every g in G of order n maps to an order-n torsion element of E6_sc; the
                     torsion classes are W-orbits on (1/n)Q/Q (simply laced: Q = Qv), so the
                     eigenvalue multiset of g on V must be achievable by some x in (Z/n)^6
                     acting on the 27 weights (exact; realizability at the element level);
    C2 (adjoint fit) 27 (x) 27bar = 1 + 78 + 650 and Sym^3(27) = 1 + 650 + V(3w1): a matching
                     torsion point x (from C3) determines candidate values chi_78(g), chi_650(g);
                     there must EXIST a choice of x-profiles -- one per maximal-cyclic class
                     family, consistent at the shared power classes -- making both would-be
                     class functions genuine characters (non-negative integer multiplicities),
                     with the 78 orthogonally realizable (finite G in E6(C) is conjugate into
                     the compact form, whose adjoint is a REAL representation: quaternionic
                     irreps must appear with even multiplicity).
  All E6 decompositions are DERIVED in-probe (exact Freudenthal + Weyl dimension formula over
  Fractions; the tensor weight-multisets are decomposed greedily and gated to zero remainder) --
  no transcribed branching tables. Controls: the two REALIZED canonical assemblies (B329:
  principal 3+3+3+18, trinification 9+3+3+6+6) MUST pass every layer; the attrition of the real
  (self-dual) window population is reported next to the chiral one.
  Report: found / not-found-in-bound; per-layer attrition.

PIECE 2 -- third-order {4,8} integrability, extended one depth: the depth-3 Massey bracket
(= the order-4 obstruction) on the escape sector, with B370's jet machinery extended to t^4.
  rho_t(g) = exp(t z1 + t^2 z2 + t^3 z3) rho(g); X_t(rel) = I + t P1 + ... + t^4 P4.
  ||P1||,||P2||,||P3|| ~ 0 gate the cocycle, the z2 solve and the z3 solve INSIDE the same
  expansion; ad(q4) = P4 defines the order-4 obstruction (exact-Gram normal equations, B352).
  Gauge discipline (declared): the order-3 class is first killed exactly by shifting z2 inside
  its indeterminacy span (P3/P4 are affine-linear in z2/z3, so unit finite differences are
  exact); the corrected order-3 class must sit at the floor before order 4 is read. The order-4
  verdict is taken modulo the z3-shift indeterminacy span (six unit cocycle shifts, full
  re-runs), with the MB12 random-vector control against the same span. Controls: coboundary
  (exact-tier zero at every order) and m=1 (the A-polynomial curve: integrable to all orders).
  Directions (declared): m=1 control, m=4, m=8, m=4+m=8 (polarization mix), coboundary.
  dps 100 (the banked B352/B370 discipline; a --dps knob exists and is logged).
  EXECUTION RECORD: the full treatment (gauge fix + z3-shift span, run_piece2/depth3_direction,
  ~85 min per direction) was banked for coboundary, m=1, m=4, m=8; the mix48 full run completed
  but lost its JSON to a file race with the staged re-run (numbers harvested from p2_mix48.log
  into the part JSON). A staged BASE mode (stage_solve/stage_jet4: minimal-norm defining system,
  no gauge sweep / span quotient, two bounded foreground calls per direction) was run for ALL
  five directions as a cross-check; base classes reproduce the full-run classes at the same
  floors (m=4: identical 1.018e-60; coboundary: identical 1.118e-94). Where the z3-shift span
  saturates C^6 (m=8, mix: deltas at q4-scale vs a floor-level class) MB12 goes vacuous and the
  verdict is read from the ABSOLUTE criterion: class >= 3 orders below the direction's own
  expansion-floor gates.

PIECE 3 -- the geometric theta-identification: does the manifold's involution induce theta?
  (a) EXACT: theta acts on B352's 78 chain vectors blockwise as the scalar (-1)^{m+1} -- theta
      is an automorphism OF THE pi_1-MODULE e6_{Ad rho} (it commutes with the principal sl2,
      hence fixes rho_geo = principal o rho_2 pointwise). Checked on all 78 basis vectors with
      integer arithmetic (B351's exact theta).
  (b) EXACT: the sl2-commutant lemma. Any linear map commuting with the principal sl2 is
      blockwise scalar (multiplicity-free, Schur); bracket preservation forces the scalars to
      satisfy lam_m lam_m' = lam_m'' over the EXACT block-coupling relations of the chain
      brackets. The solution group is computed by Smith normal form: expected Z/2 = {1, theta}.
      => the involution's tangent action is CANONICAL (inner intertwiner unique up to the
      trivially-acting centre), and theta is the ONLY nontrivial sl2-commuting automorphism.
  (c) NUMERIC (dps 100): the hyperelliptic involution's pullback on each H^1 line equals
      theta's module action modulo coboundaries: || Psi(z0) - eps_m z0 - d0 u || at the floor,
      with the wrong-sign control || Psi(z0) + eps_m z0 - d0 u || at O(1). The amphichiral
      (orientation-reversing) involution is re-derived as the real structure J (J^2 = +1 per
      line) -- it does NOT act by theta (it is antilinear); it COMMUTES with theta exactly
      (theta is real blockwise scalar).
  Note the sharpened statement: rho o psi_hyper = Ad(phi(D)) o rho is INNER (D in SL2, verified)
  -- the involution does not realize the outer class at the representation level; theta fixes
  rho_geo and the involution's canonical tangent action COINCIDES with theta's. That is the
  honest content of "the involution induces theta".

Reproducer:  .venv/bin/python frontier/B501_gateB_reductions/probe.py           (all pieces; hours)
Piecewise:   probe.py --piece 1|2|3 [--dirs cob,m1,m4,m8,mix48] [--dps 100] [--tag T]
             probe.py --merge-piece2      (collect b501_piece2_*.json -> b501_piece2.json)
Outputs:     b501_piece1.json / b501_piece2.json / b501_piece3.json (parameters logged inside).
"""
import argparse
import glob
import importlib.util
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.dirname(HERE)


# =====================================================================================
# shared loaders
# =====================================================================================
def _load_file(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(FRONTIER, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_CP = None
_MA = None


def load_cp(dps=100):
    """cup_product (B352) with _DPS patched to the declared value (logged parameter).
    The patched instance is registered as sys.modules['cup_product'] so that massey (B370)
    binds to the SAME instance."""
    global _CP
    if _CP is not None:
        return _CP
    path = os.path.join(FRONTIER, "B352_cup_product_obstruction", "cup_product.py")
    src = open(path).read()
    assert "_DPS = 100" in src
    src = src.replace("_DPS = 100", "_DPS = %d" % dps, 1)
    spec = importlib.util.spec_from_file_location("cup_product", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["cup_product"] = mod
    exec(compile(src, path, "exec"), mod.__dict__)
    _CP = mod
    return mod


def load_massey(dps=100):
    global _MA
    if _MA is None:
        load_cp(dps)
        _MA = _load_file("b370_massey", "B370_massey_depth2/massey.py")
    return _MA


# =====================================================================================
# PIECE 2 -- depth-3 Massey (order-4 obstruction) on the {4,8} sector
# =====================================================================================
def _lsq_span(mp, c0, deltas, cut=-30):
    """min-norm x with || c0 + sum x_j deltas_j || minimal; returns (x, resid_rel, rank)."""
    cols = [d for d in deltas if mp.norm(d) > mp.mpf(10) ** -60]
    if not cols:
        return [], float(mp.norm(c0)), 0
    M = mp.zeros(6, len(cols))
    for j, d in enumerate(cols):
        for i in range(6):
            M[i, j] = d[i]
    U, sv, Vh = mp.svd_c(mp.matrix(M), full_matrices=True)
    y = U.transpose_conj() * (-c0)
    x = mp.zeros(len(cols), 1)
    smax = max(abs(s) for s in sv)
    rank = 0
    for i in range(len(sv)):
        if abs(sv[i]) > smax * mp.mpf(10) ** cut:
            rank += 1
            for j in range(len(cols)):
                x[j] += mp.conj(Vh[i, j]) * y[i] / sv[i]
    resid = mp.norm(M * x + c0) / max(mp.norm(c0), mp.mpf(10) ** -200)
    xs = []
    k = 0
    for d in deltas:
        if mp.norm(d) > mp.mpf(10) ** -60:
            xs.append(x[k])
            k += 1
        else:
            xs.append(mp.mpf(0))
    return xs, float(resid), rank


def _solve_block_lsq(CP, rhs_chain):
    """w (chain, as (wa,wb)) with Fox d1_m w = rhs_chain_m per block (pseudo-inverse)."""
    mp = CP.mp
    wa, wb = mp.zeros(CP.DIM, 1), mp.zeros(CP.DIM, 1)
    worst = mp.mpf(0)
    for m in CP.EXPONENTS:
        d1, _ = CP.FOX[m]
        n, o = CP.N_OF[m], CP.OFFSET[m]
        rhs = mp.matrix([rhs_chain[o + k] for k in range(n)])
        U, sv, Vh = CP._svd(d1)
        y = U.transpose_conj() * rhs
        w = mp.zeros(2 * n, 1)
        smax = max(abs(s) for s in sv)
        for i in range(len(sv)):
            if abs(sv[i]) > smax * mp.mpf(10) ** -40:
                for j in range(2 * n):
                    w[j] += mp.conj(Vh[i, j]) * y[i] / sv[i]
        worst = max(worst, mp.norm(d1 * w - rhs))
        for k in range(n):
            wa[o + k] = w[k]
            wb[o + k] = w[k + n]
    scale = max(mp.norm(rhs_chain), mp.mpf(10) ** -200)
    return wa, wb, float(worst / scale)


def relator_jet4(CP, za_c, zb_c, wa_c, wb_c, va_c, vb_c):
    """Order-4 relator expansion for rho_t = exp(t z1 + t^2 z2 + t^3 z3) rho.
    Letter jets (single Lie exponential; no BCH transcription):
      exp(+Z) levels: I, A, B + A^2/2, C + (AB+BA)/2 + A^3/6,
                      (AC+CA)/2 + B^2/2 + (A^2B+ABA+BA^2)/6 + A^4/24
      exp(-Z) levels: I, -A, A^2/2 - B, (AB+BA)/2 - A^3/6 - C,
                      (AC+CA)/2 + B^2/2 - (A^2B+ABA+BA^2)/6 + A^4/24
    with A = ad z1(g), B = ad z2(g), C = ad z3(g) in root coordinates.
    Returns (||P1||, ||P2||, ||P3||, q4_root, ad_res, ||q4||)."""
    mp = CP.mp
    DIM = CP.DIM
    S = CP.S
    za, zb = S * za_c, S * zb_c
    wa, wb = S * wa_c, S * wb_c
    va, vb = S * va_c, S * vb_c
    A = {"a": CP.ad_root(za), "b": CP.ad_root(zb)}
    B = {"a": CP.ad_root(wa), "b": CP.ad_root(wb)}
    C = {"a": CP.ad_root(va), "b": CP.ad_root(vb)}
    half = mp.mpf(1) / 2
    sixth = mp.mpf(1) / 6
    tw4 = mp.mpf(1) / 24
    J = {}
    for g in "ab":
        Ag, Bg, Cg = A[g], B[g], C[g]
        A2 = Ag * Ag
        A3 = A2 * Ag
        A4 = A3 * Ag
        AB = Ag * Bg
        BA = Bg * Ag
        AB2 = AB + BA
        AC2 = Ag * Cg + Cg * Ag
        BB = Bg * Bg
        A2B = Ag * AB + AB * Ag + BA * Ag                 # A^2 B + A B A + B A^2
        E4p = AC2 * half + BB * half + A2B * sixth + A4 * tw4
        E4m = AC2 * half + BB * half - A2B * sixth + A4 * tw4
        X = CP.X_root(g)
        Xi = CP.X_root(g.upper())
        J[g] = [X, Ag * X, (Bg + A2 * half) * X,
                (Cg + AB2 * half + A3 * sixth) * X, E4p * X]
        J[g.upper()] = [Xi, -(Xi * Ag), Xi * (A2 * half - Bg),
                        Xi * (AB2 * half - A3 * sixth - Cg), Xi * E4m]
    P = [mp.eye(DIM)] + [mp.zeros(DIM, DIM) for _ in range(4)]
    for ch in CP.REL:
        L = J[ch]
        P = [P[0] * L[0],
             P[1] * L[0] + P[0] * L[1],
             P[2] * L[0] + P[1] * L[1] + P[0] * L[2],
             P[3] * L[0] + P[2] * L[1] + P[1] * L[2] + P[0] * L[3],
             P[4] * L[0] + P[3] * L[1] + P[2] * L[2] + P[1] * L[3] + P[0] * L[4]]
    MA = load_massey()
    q4, res = MA._solve_ad(P[4])
    return (float(mp.norm(P[1])), float(mp.norm(P[2])), float(mp.norm(P[3])),
            q4, float(res), float(mp.norm(q4)))


def depth3_direction(label, za, zb, zbasis, gauge_fix=True, do_deltas=True):
    """Full declared readout for one direction at order 4."""
    CP, MA = load_cp(), load_massey()
    mp = CP.mp
    t0 = time.time()
    out = {"label": label}
    # --- z2 (B370's solve), order-3 class, exact gauge fix inside the z2-indeterminacy
    wa, wb, first2, z2ls = MA.solve_z2(za, zb)
    p1a, p2a, q3, adres3, q3n = MA.relator_jet3(za, zb, wa, wb)
    c3 = MA.class_complex(q3)
    out["order3_class_norm"] = float(mp.norm(c3))
    out["z2_ls_residual"] = z2ls
    if gauge_fix and zbasis:
        deltas3 = []
        for (ka, kb) in zbasis:
            _, _, q3s, _, _ = MA.relator_jet3(za, zb, wa + ka, wb + kb)
            deltas3.append(MA.class_complex(q3s) - c3)
        xs, res3, rank3 = _lsq_span(mp, c3, deltas3)
        for x, (ka, kb) in zip(xs, zbasis):
            wa = wa + ka * x
            wb = wb + kb * x
        _, _, q3c, _, _ = MA.relator_jet3(za, zb, wa, wb)
        c3c = MA.class_complex(q3c)
        out["order3_gauge"] = {"rank": rank3, "span_residual": res3,
                               "corrected_class_norm": float(mp.norm(c3c))}
        q3_used = q3c
    else:
        out["order3_gauge"] = None
        q3_used = q3
    # --- z3: Fox d1 z3 = -q3_chain (blockwise); then the order-4 jet
    q3_chain = CP.S_INV * q3_used
    va, vb, z3ls = _solve_block_lsq(CP, -q3_chain)
    out["z3_ls_residual"] = z3ls
    p1, p2, p3, q4, adres4, q4n = relator_jet4(CP, za, zb, wa, wb, va, vb)
    out.update(gate_P1=p1, gate_P2=p2, gate_P3=p3,
               ad_solve_residual=adres4, q4_norm=q4n)
    c0 = MA.class_complex(q4)
    out["class_abs"] = [float(abs(c0[i])) for i in range(6)]
    out["class_norm"] = float(mp.norm(c0))
    # --- indeterminacy: z3-shifts by the six unit cocycles (P4 is affine in z3: exact)
    if do_deltas and zbasis:
        deltas4 = []
        for (ka, kb) in zbasis:
            _, _, _, q4s, _, _ = relator_jet4(CP, za, zb, wa, wb, va + ka, vb + kb)
            deltas4.append(MA.class_complex(q4s) - c0)
        resid, rank = MA._span_residual(c0, deltas4)
        out["indeterminacy_rank"] = rank
        out["transverse_residual"] = resid
        import random
        rnd = random.Random(11)
        mb12 = []
        for _ in range(3):
            v = mp.matrix([rnd.uniform(-1, 1) + 1j * rnd.uniform(-1, 1) for _ in range(6)])
            r, _ = MA._span_residual(v, deltas4)
            mb12.append(r)
        out["mb12_random_residuals"] = mb12
    else:
        out["indeterminacy_rank"] = None
        out["transverse_residual"] = out["class_norm"]
        out["mb12_random_residuals"] = None
    out["seconds"] = round(time.time() - t0, 1)
    return out


def run_piece2(dirs, dps, tag, deltas=True, gauge=True):
    CP, MA = load_cp(dps), load_massey(dps)
    mp = CP.mp
    rep = {"piece": 2, "dps": dps, "rel": CP.REL, "directions_requested": dirs,
           "gauge_fix": gauge, "deltas": deltas,
           "declared": "order-4 obstruction; z2 gauge-fixed at order 3; verdict modulo "
                       "the z3-shift span; controls: coboundary + m=1"}
    worst_rel, worst_auto = CP.rep_checks()
    rep["rep_checks"] = {"relator": float(worst_rel), "automorphism": float(worst_auto)}
    print("rep_checks:", rep["rep_checks"], flush=True)
    need_lines = deltas or gauge or any(d != "cob" for d in dirs)
    z = {m: CP.h1_line(m) for m in CP.EXPONENTS} if need_lines else {}
    zbasis = [z[m] for m in CP.EXPONENTS] if z else []
    results = []
    for d in dirs:
        if d == "cob":
            import random
            rnd = random.Random(5)
            v = mp.matrix([rnd.uniform(-1, 1) for _ in range(CP.DIM)])
            cza, czb = mp.zeros(CP.DIM, 1), mp.zeros(CP.DIM, 1)
            for m in CP.EXPONENTS:
                o, n = CP.OFFSET[m], CP.N_OF[m]
                vm = mp.matrix([v[o + k] for k in range(n)])
                wa_ = CP.BLK["a"][m] * vm - vm
                wb_ = CP.BLK["b"][m] * vm - vm
                for k in range(n):
                    cza[o + k] = wa_[k]
                    czb[o + k] = wb_[k]
            nrm = mp.sqrt(mp.norm(cza) ** 2 + mp.norm(czb) ** 2)
            r = depth3_direction("coboundary", cza / nrm, czb / nrm, zbasis,
                                 gauge_fix=False, do_deltas=False)
        elif d == "mix48":
            za = z[4][0] + z[8][0]
            zb = z[4][1] + z[8][1]
            nrm = mp.sqrt(mp.norm(za) ** 2 + mp.norm(zb) ** 2)
            r = depth3_direction("m=4+m=8", za / nrm, zb / nrm, zbasis,
                                 gauge_fix=gauge, do_deltas=deltas)
        else:
            m = int(d.lstrip("m"))
            r = depth3_direction("m=%d" % m, z[m][0], z[m][1], zbasis,
                                 gauge_fix=gauge, do_deltas=deltas)
        results.append(r)
        print("  %s: P1=%.1e P2=%.1e P3=%.1e |class4|=%.3e transverse=%.3e (%ss)"
              % (r["label"], r["gate_P1"], r["gate_P2"], r["gate_P3"],
                 r["class_norm"], r["transverse_residual"], r["seconds"]), flush=True)
    rep["directions"] = results
    out = os.path.join(HERE, "b501_piece2_%s.json" % tag)
    json.dump(rep, open(out, "w"), indent=1)
    print("wrote", out, flush=True)
    return rep


def _ser_vec(mp, v):
    return [(mp.mpc(v[i]).real._mpf_, mp.mpc(v[i]).imag._mpf_) for i in range(v.rows)]


def _de_vec(mp, lst):
    return mp.matrix([mp.make_mpc((re, im)) for (re, im) in lst])


def _direction_z(CP, d):
    """The declared direction vectors (chain coords, normalized)."""
    mp = CP.mp
    if d == "cob":
        import random
        rnd = random.Random(5)
        v = mp.matrix([rnd.uniform(-1, 1) for _ in range(CP.DIM)])
        za, zb = mp.zeros(CP.DIM, 1), mp.zeros(CP.DIM, 1)
        for m in CP.EXPONENTS:
            o, n = CP.OFFSET[m], CP.N_OF[m]
            vm = mp.matrix([v[o + k] for k in range(n)])
            wa_ = CP.BLK["a"][m] * vm - vm
            wb_ = CP.BLK["b"][m] * vm - vm
            for k in range(n):
                za[o + k] = wa_[k]
                zb[o + k] = wb_[k]
        label = "coboundary"
    elif d == "mix48":
        z4, z8 = CP.h1_line(4), CP.h1_line(8)
        za, zb = z4[0] + z8[0], z4[1] + z8[1]
        label = "m=4+m=8"
    else:
        m = int(d.lstrip("m"))
        za, zb = CP.h1_line(m)
        label = "m=%d" % m
    nrm = mp.sqrt(mp.norm(za) ** 2 + mp.norm(zb) ** 2)
    return label, za / nrm, zb / nrm


def stage_solve(d, tag, dps, repchecks=False):
    """Stage 1 (bounded, ~6-7 min foreground): z1 -> z2 (Fox lsq) -> q3 (order-3 jet)
    -> z3 (Fox lsq); checkpoint the six chain vectors exactly (mpf mantissa tuples)."""
    import pickle
    CP, MA = load_cp(dps), load_massey(dps)
    mp = CP.mp
    t0 = time.time()
    out = {"label": None, "dps": dps, "mode": "base: minimal-norm defining system "
           "(no gauge sweep / span quotient -- budget-capped; safe for unobstructed "
           "verdicts: a quotient can only shrink a class)"}
    rc = None
    if repchecks:
        worst_rel, worst_auto = CP.rep_checks()
        rc = {"relator": float(worst_rel), "automorphism": float(worst_auto)}
    label, za, zb = _direction_z(CP, d)
    out["label"] = label
    wa, wb, first2, z2ls = MA.solve_z2(za, zb)
    p1a, p2a, q3, adres3, q3n = MA.relator_jet3(za, zb, wa, wb)
    c3 = MA.class_complex(q3)
    out.update(order3_class_norm=float(mp.norm(c3)), order3_q3_norm=q3n,
               z2_ls_residual=z2ls, order3_ad_residual=adres3)
    va, vb, z3ls = _solve_block_lsq(CP, -(CP.S_INV * q3))
    out["z3_ls_residual"] = z3ls
    out["seconds_solve"] = round(time.time() - t0, 1)
    ck = {"meta": out, "rep_checks": rc,
          "vecs": {k: _ser_vec(mp, v) for k, v in
                   (("za", za), ("zb", zb), ("wa", wa),
                    ("wb", wb), ("va", va), ("vb", vb))}}
    path = os.path.join(HERE, "b501_ckpt_%s.pkl" % tag)
    pickle.dump(ck, open(path, "wb"))
    print("stage_solve %s: order3 class %.3e (q3 %.2e) z2ls %.1e z3ls %.1e (%ss)"
          % (label, out["order3_class_norm"], q3n, z2ls, z3ls,
             out["seconds_solve"]), flush=True)


def stage_jet4(tag, dps):
    """Stage 2 (bounded, ~6-7 min foreground): the order-4 jet on the checkpointed
    defining system; gates P1..P3 inside the same expansion; class of q4 per block."""
    import pickle
    CP, MA = load_cp(dps), load_massey(dps)
    mp = CP.mp
    ck = pickle.load(open(os.path.join(HERE, "b501_ckpt_%s.pkl" % tag), "rb"))
    out = ck["meta"]
    assert out["dps"] == dps
    V = {k: _de_vec(mp, v) for k, v in ck["vecs"].items()}
    t0 = time.time()
    p1, p2, p3, q4, adres4, q4n = relator_jet4(
        CP, V["za"], V["zb"], V["wa"], V["wb"], V["va"], V["vb"])
    c0 = MA.class_complex(q4)
    out.update(gate_P1=p1, gate_P2=p2, gate_P3=p3, ad_solve_residual=adres4,
               q4_norm=q4n, class_abs=[float(abs(c0[i])) for i in range(6)],
               class_norm=float(mp.norm(c0)))
    out["seconds_jet4"] = round(time.time() - t0, 1)
    path = os.path.join(HERE, "b501_piece2_%s.json" % tag)
    json.dump({"piece": 2, "dps": dps, "rel": CP.REL,
               "rep_checks": ck.get("rep_checks"),
               "directions": [out]}, open(path, "w"), indent=1)
    print("stage_jet4 %s: P1=%.1e P2=%.1e P3=%.1e |class4|=%.3e q4=%.2e (%ss)"
          % (out["label"], p1, p2, p3, out["class_norm"], q4n,
             out["seconds_jet4"]), flush=True)


def merge_piece2():
    files = sorted(glob.glob(os.path.join(HERE, "b501_piece2_*.json")))
    files = [f for f in files if not f.endswith("b501_piece2.json")]
    merged = None
    for f in files:
        rep = json.load(open(f))
        if merged is None:
            merged = {k: v for k, v in rep.items() if k != "directions"}
            merged["directions"] = []
            merged["merged_from"] = []
        if not merged.get("rep_checks") and rep.get("rep_checks"):
            merged["rep_checks"] = rep["rep_checks"]
        merged["directions"].extend(rep["directions"])
        merged["merged_from"].append(os.path.basename(f))
    assert merged, "no b501_piece2_*.json parts found"
    out = os.path.join(HERE, "b501_piece2.json")
    json.dump(merged, open(out, "w"), indent=1)
    print("wrote", out, "with", [r["label"] for r in merged["directions"]])
    return merged


# =====================================================================================
# PIECE 1 -- exact E6 lattice toolkit (Fractions; decompositions DERIVED, not transcribed)
# =====================================================================================
_E6A = [[2 if i == j else 0 for j in range(6)] for i in range(6)]
for _i, _j in ((0, 2), (2, 3), (3, 4), (4, 5), (1, 3)):     # Bourbaki: 1-3-4-5-6 chain, 2 on 4
    _E6A[_i][_j] = _E6A[_j][_i] = -1


def _e6_ainv():
    import sympy as sp
    M = sp.Matrix(_E6A).inv()
    return [[Fraction(int(M[i, j].p), int(M[i, j].q)) for j in range(6)] for i in range(6)]


_AINV = None
_POS = None            # positive roots, root coords
_LAB = None            # root labels A u


def _lattice():
    global _AINV, _POS, _LAB
    if _AINV is not None:
        return
    _AINV = _e6_ainv()
    simples = [tuple(1 if k == i else 0 for k in range(6)) for i in range(6)]
    seen = set(simples)
    frontier = list(simples)
    while frontier:
        nxt = []
        for u in frontier:
            n = [sum(_E6A[i][k] * u[k] for k in range(6)) for i in range(6)]
            for i in range(6):
                v = list(u)
                v[i] -= n[i]
                tv = tuple(v)
                if tv not in seen:
                    seen.add(tv)
                    nxt.append(tv)
        frontier = nxt
    assert len(seen) == 72
    _POS = sorted(t for t in seen if all(c >= 0 for c in t))
    assert len(_POS) == 36
    _LAB = {u: tuple(sum(_E6A[i][k] * u[k] for k in range(6)) for i in range(6)) for u in _POS}


def _nrm2(lab):
    """(mu, mu) for a weight given by Dynkin labels (Fraction)."""
    return sum(Fraction(lab[i]) * _AINV[i][j] * lab[j] for i in range(6) for j in range(6))


def weyl_dim(lam):
    _lattice()
    num = den = 1
    for u in _POS:
        num *= sum((lam[i] + 1) * u[i] for i in range(6))
        den *= sum(u[i] for i in range(6))
    assert num % den == 0
    return num // den


_FREUD_CACHE = {}


def freudenthal(lam):
    """{labels: multiplicity} for V(lam); gated by the Weyl dimension formula."""
    _lattice()
    lam = tuple(lam)
    if lam in _FREUD_CACHE:
        return _FREUD_CACHE[lam]
    top = _nrm2(tuple(x + 1 for x in lam))
    weights = {lam: 1}
    level = {lam}
    L = 0
    while level:
        L += 1
        cand = set()
        for n in level:
            for i in range(6):
                cand.add(tuple(n[j] - _E6A[j][i] for j in range(6)))
        nxt = set()
        for mu in cand:
            if mu in weights:
                continue
            num = 0
            for u in _POS:
                labu = _LAB[u]
                ht = sum(u)
                kmax = L // ht
                for k in range(1, kmax + 1):
                    nu = tuple(mu[j] + k * labu[j] for j in range(6))
                    if nu in weights:
                        num += weights[nu] * sum(nu[i] * u[i] for i in range(6))
            den = top - _nrm2(tuple(x + 1 for x in mu))
            if den <= 0:
                continue
            mult = Fraction(2 * num) / den
            assert mult.denominator == 1 and mult >= 0, (lam, mu, mult)
            if mult > 0:
                weights[mu] = int(mult)
                nxt.add(mu)
        level = nxt
    assert sum(weights.values()) == weyl_dim(lam), lam
    _FREUD_CACHE[lam] = weights
    return weights


def _height(lab):
    """Height of a weight = sum of its simple-root coordinates (Fraction)."""
    return sum(_AINV[i][j] * lab[j] for i in range(6) for j in range(6))


def decompose_multiset(ms):
    """Greedy exact decomposition of a weight multiset into irreducibles; gated to
    zero remainder with never-negative intermediate counts."""
    ms = dict(ms)
    out = []
    while True:
        live = [(n, v) for n, v in ms.items() if v]
        if not live:
            break
        top = max((n for n, v in live), key=_height)
        assert all(x >= 0 for x in top), ("leading weight not dominant", top)
        mult = ms[top]
        assert mult > 0
        W = freudenthal(top)
        for n, v in W.items():
            ms[n] = ms.get(n, 0) - mult * v
            assert ms[n] >= 0, ("negative remainder", top, n)
        out.append((top, mult))
    return sorted(out, key=lambda t: weyl_dim(t[0]))


def e6_tensor_facts():
    """Derive the E6 decompositions the sieve relies on. Returns the fact dict and
    the weight systems of 27, 78 = V(w2), 650 = the shared constituent."""
    from collections import Counter
    from itertools import combinations_with_replacement
    _lattice()
    w27d = freudenthal((1, 0, 0, 0, 0, 0))
    assert set(w27d.values()) == {1} and len(w27d) == 27
    W27 = sorted(w27d)
    dual = Counter(tuple(-x for x in n) for n in W27)
    tens = Counter()
    for a in W27:
        for b in W27:
            tens[tuple(a[i] - b[i] for i in range(6))] += 1
    dec_tens = decompose_multiset(tens)
    sym2 = Counter()
    for a, b in combinations_with_replacement(W27, 2):
        sym2[tuple(a[i] + b[i] for i in range(6))] += 1
    dec_sym2 = decompose_multiset(sym2)
    sym3 = Counter()
    for a, b, c in combinations_with_replacement(W27, 3):
        sym3[tuple(a[i] + b[i] + c[i] for i in range(6))] += 1
    dec_sym3 = decompose_multiset(sym3)
    dims_tens = [(weyl_dim(l), m) for l, m in dec_tens]
    dims_sym2 = [(weyl_dim(l), m) for l, m in dec_sym2]
    dims_sym3 = [(weyl_dim(l), m) for l, m in dec_sym3]
    # the facts the sieve needs
    assert dims_tens == [(1, 1), (78, 1), (650, 1)], dims_tens
    assert dims_sym2 == [(27, 1), (351, 1)], dims_sym2
    assert dims_sym3 == [(1, 1), (650, 1), (3003, 1)], dims_sym3
    lam78 = next(l for l, m in dec_tens if weyl_dim(l) == 78)
    lam650_t = next(l for l, m in dec_tens if weyl_dim(l) == 650)
    lam650_s = next(l for l, m in dec_sym3 if weyl_dim(l) == 650)
    assert lam650_t == lam650_s, "the 650s of 27x27bar and Sym^3 27 differ"
    lam27b = next(l for l, m in dec_sym2 if weyl_dim(l) == 27)
    assert Counter(freudenthal(lam27b)) == dual, "Sym^2 27 does not contain 27bar"
    facts = {"27_tensor_27bar": [[list(l), m, weyl_dim(l)] for l, m in dec_tens],
             "sym2_27": [[list(l), m, weyl_dim(l)] for l, m in dec_sym2],
             "sym3_27": [[list(l), m, weyl_dim(l)] for l, m in dec_sym3]}
    return facts, W27, freudenthal(lam78), freudenthal(lam650_t)


def torsion_profiles(orders, W27, W78, W650):
    """For each n in orders: {key27: set of (key78, key650)} over ALL x in (1/n)Q/Q
    (= all order-dividing-n torsion classes of simply-connected E6, up to W).
    keyN = tuple of eigenvalue counts (exponent j/n, j = 0..n-1) on the named rep."""
    import numpy as np
    from itertools import product as iproduct
    L27 = np.array(W27, dtype=np.int64)
    L78 = np.array(sorted(W78), dtype=np.int64)
    M78 = np.array([W78[tuple(r)] for r in L78.tolist()], dtype=np.int64)
    L650 = np.array(sorted(W650), dtype=np.int64)
    M650 = np.array([W650[tuple(r)] for r in L650.tolist()], dtype=np.int64)
    out = {}
    for n in orders:
        grid = np.array(list(iproduct(range(n), repeat=6)), dtype=np.int64)
        d = {}
        chunk = 4096
        for s in range(0, len(grid), chunk):
            C = grid[s:s + chunk]
            R27 = (C @ L27.T) % n
            R78 = (C @ L78.T) % n
            R650 = (C @ L650.T) % n
            k27 = np.stack([(R27 == j).sum(axis=1) for j in range(n)], axis=1)
            k78 = np.stack([((R78 == j) * M78).sum(axis=1) for j in range(n)], axis=1)
            k650 = np.stack([((R650 == j) * M650).sum(axis=1) for j in range(n)], axis=1)
            for r in range(len(C)):
                d.setdefault(tuple(k27[r]), set()).add((tuple(k78[r]), tuple(k650[r])))
        out[n] = d
    return out


# ---------------------------------------------------------------- the G side + sieve --
def _group_side(name):
    """Exact 2T/A4 data via B356's self-verifying builder + full power maps and
    per-irrep eigenvalue counts per class."""
    import cmath
    SS = _load_file("b356_ss", "B356_sigma_stability_scan/sigma_stability.py")
    gd = SS.group_data(name)
    ct = SS.character_table(gd)
    k = len(ct["sizes"])
    chis = [[complex(v) for v in chi] for chi in ct["irreps"]]
    # element order + full power map per class: pcl[c][j] = class of g^j, j = 0..o-1
    G, mul, one = gd["G"], gd["mul"], gd["G"][gd["classes"][gd["one_class"]][0]]
    key, idx, class_of = gd["key"], gd["idx"], gd["class_of"]
    orders, pcl = [], []
    for cl in gd["classes"]:
        g = G[cl[0]]
        row = []
        p = one
        while True:
            row.append(class_of[idx[key(p)]])
            p = mul(p, g)
            if key(p) == key(one):
                break
        orders.append(len(row))
        pcl.append(row)
    # per-irrep eigenvalue counts at each class (DFT over the cyclic subgroup; exact snap)
    counts = []
    for i in range(len(chis)):
        per_class = []
        for c in range(k):
            o = orders[c]
            row = []
            for j in range(o):
                s = sum(chis[i][pcl[c][kk]] * cmath.exp(-2j * cmath.pi * j * kk / o)
                        for kk in range(o)) / o
                assert abs(s.imag) < 1e-6 and abs(s.real - round(s.real)) < 1e-6, (i, c, j, s)
                row.append(int(round(s.real)))
            assert sum(row) == ct["dims"][i]
            per_class.append(tuple(row))
        counts.append(per_class)
    return dict(name=name, gd=gd, ct=ct, chis=chis, k=k, orders=orders, pcl=pcl,
                counts=counts, sizes=ct["sizes"], dims=ct["dims"], fs=ct["fs"])


def _enumerate_window(gs):
    """All faithful 27-dim assemblies with (Sym^3 V)^G != 0 (B356's window), collected
    as multiplicity vectors, split into chiral (complex) and real (self-dual)."""
    chis, k, dims = gs["chis"], gs["k"], gs["dims"]
    gd = gs["gd"]
    sizes, n = gs["sizes"], gd["n"]
    kernels = [{c for c in range(k) if abs(chis[i][c] - dims[i]) < 1e-9} for i in range(len(chis))]
    conj_of = []
    for i in range(len(chis)):
        cc = [v.conjugate() for v in chis[i]]
        conj_of.append(next(j for j in range(len(chis))
                            if max(abs(cc[c] - chis[j][c]) for c in range(k)) < 1e-9))
    p2, p3 = gd["p2"], gd["p3"]
    one_c = gd["one_class"]
    order = sorted(range(len(chis)), key=lambda i: -dims[i])
    chiral, real = [], []

    def sym3_ok(chiV):
        tot = 0
        for c in range(k):
            tot += sizes[c] * (chiV[c] ** 3 + 3 * chiV[c] * chiV[p2[c]] + 2 * chiV[p3[c]]) / 6
        m = tot / n
        assert abs(m.imag) < 1e-6 and abs(m.real - round(m.real)) < 1e-6, m
        return round(m.real) >= 1

    def rec(pos, remaining, mult):
        if remaining == 0:
            used = [i for i in range(len(chis)) if mult[i] > 0]
            ker = set(range(k))
            for i in used:
                ker &= kernels[i]
            if ker != {one_c}:
                return
            chiV = [sum(mult[i] * chis[i][c] for i in used) for c in range(k)]
            if not sym3_ok(chiV):
                return
            if any(mult[i] != mult[conj_of[i]] for i in range(len(chis))):
                chiral.append(tuple(mult))
            else:
                real.append(tuple(mult))
            return
        if pos == len(order):
            return
        i = order[pos]
        for m_ in range(remaining // dims[i], -1, -1):
            mult[i] = m_
            rec(pos + 1, remaining - m_ * dims[i], mult)
        mult[i] = 0

    rec(0, 27, [0] * len(chis))
    return chiral, real, conj_of


def _sieve(gs, assemblies, conj_of, achievable):
    """Apply C1 (Sym^2 cross), C3 (torsion realizability), C2 (adjoint/650 profile fit)
    to a list of assemblies. Returns attrition dict + survivors list."""
    import numpy as np
    chis, k, sizes = gs["chis"], gs["k"], gs["sizes"]
    orders, pcl, counts, fs, dims = gs["orders"], gs["pcl"], gs["counts"], gs["fs"], gs["dims"]
    n_grp = gs["gd"]["n"]
    if not assemblies:
        return {"input": 0, "pass_C1": 0, "pass_C3": 0, "pass_C1C3": 0, "pass_all": 0}, []
    N = np.array(assemblies, dtype=np.int64)
    T = np.array(chis, dtype=complex)                       # irreps x classes
    chiV = N @ T                                            # asm x classes
    p2idx = np.array(gs["gd"]["p2"])
    # ---- C1: Sym^2 V - Vbar >= 0
    sym2 = (chiV ** 2 + chiV[:, p2idx]) / 2
    f = sym2 - np.conj(chiV)
    w = np.array(sizes, dtype=float)
    M = (f * w) @ np.conj(T.T) / n_grp                      # asm x irreps multiplicities
    assert np.abs(M.imag).max() < 1e-6 and np.abs(M - np.round(M.real)).max() < 1e-6
    Mi = np.round(M.real).astype(np.int64)
    c1 = (Mi >= 0).all(axis=1)
    # ---- C3: torsion realizability per class (orders >= 2)
    c3 = np.ones(len(N), dtype=bool)
    keys_per_class = {}
    for c in range(k):
        o = orders[c]
        if o == 1:
            continue
        K = np.array([counts[i][c] for i in range(len(chis))], dtype=np.int64)
        rows = N @ K                                        # asm x o eigen counts
        ach = achievable[o]
        keys = list(map(tuple, rows.tolist()))
        keys_per_class[c] = keys
        ok = np.array([kk in ach for kk in keys], dtype=bool)
        c3 &= ok
    # ---- C2 on C1&C3 survivors: profile fit
    both = c1 & c3
    one_c = gs["gd"]["one_class"]
    reps = [c for c in range(k) if orders[c] >= 2 and not any(
        orders[c2] > orders[c] and c in gs["pcl"][c2][1:] for c2 in range(k))]
    covered = {one_c} | set(reps)
    for r_ in reps:
        covered |= set(pcl[r_])
    assert covered == set(range(k)), "class family cover incomplete"
    Tconj = np.conj(np.array(chis, dtype=complex))
    quat = [i for i in range(len(chis)) if fs[i] == -1]
    import cmath as _cm

    def c2_pass(row_idx):
        choice_sets = []
        for c in reps:
            o = orders[c]
            key = keys_per_class[c][row_idx]
            profs = achievable[o][key]
            choice_sets.append(sorted(profs))
        from itertools import product as iprod
        for combo in iprod(*choice_sets):
            v78 = {one_c: complex(78)}
            v650 = {one_c: complex(650)}
            ok = True
            for (c, (k78, k650)) in zip(reps, combo):
                o = orders[c]
                for kk in range(1, o):
                    cls = pcl[c][kk]
                    z78 = sum(k78[j] * _cm.exp(2j * _cm.pi * j * kk / o) for j in range(o))
                    z650 = sum(k650[j] * _cm.exp(2j * _cm.pi * j * kk / o) for j in range(o))
                    if cls in v78:
                        if abs(v78[cls] - z78) > 1e-6 or abs(v650[cls] - z650) > 1e-6:
                            ok = False
                            break
                    else:
                        v78[cls] = z78
                        v650[cls] = z650
                if not ok:
                    break
            if not ok or len(v78) != k:
                continue
            f78 = np.array([v78[c] for c in range(k)])
            f650 = np.array([v650[c] for c in range(k)])
            m78 = (f78 * w) @ Tconj.T / n_grp
            m650 = (f650 * w) @ Tconj.T / n_grp
            good = True
            for arr in (m78, m650):
                if np.abs(arr.imag).max() > 1e-6 or np.abs(arr - np.round(arr.real)).max() > 1e-6:
                    good = False
                    break
                if (np.round(arr.real) < 0).any():
                    good = False
                    break
            if not good:
                continue
            m78i = np.round(m78.real).astype(np.int64)
            if any(m78i[i] % 2 for i in quat):
                continue
            # the 3003-part of Sym^3 V must also be a genuine character (non-negative)
            chiV_r = chiV[row_idx]
            sym3 = np.array([(chiV_r[c] ** 3 + 3 * chiV_r[c] * chiV_r[gs["gd"]["p2"][c]]
                              + 2 * chiV_r[gs["gd"]["p3"][c]]) / 6 for c in range(k)])
            f3003 = sym3 - 1 - f650
            m3003 = (f3003 * w) @ Tconj.T / n_grp
            if np.abs(m3003.imag).max() > 1e-6 or np.abs(m3003 - np.round(m3003.real)).max() > 1e-6:
                continue
            if (np.round(m3003.real) < 0).any():
                continue
            return True
        return False

    survivors = []
    n_c2 = 0
    for ridx in range(len(N)):
        if not both[ridx]:
            continue
        if c2_pass(ridx):
            n_c2 += 1
            survivors.append(assemblies[ridx])
    att = {"input": int(len(N)), "pass_C1": int(c1.sum()), "pass_C3": int(c3.sum()),
           "pass_C1C3": int(both.sum()), "pass_all": n_c2}
    return att, survivors


def run_piece1():
    print("== PIECE 1: bounded search for a chiral 2T->E6 embedding ==", flush=True)
    t0 = time.time()
    facts, W27, W78, W650 = e6_tensor_facts()
    print("  E6 tensor facts derived:", {k_: [d for _, __, d in v] for k_, v in facts.items()},
          flush=True)
    rep = {"piece": 1, "declared_bound":
           "B356 chirality window sieved by exact necessary conditions C1 (Sym^2 cross map), "
           "C3 (torsion-class realizability on the 27, all x in (1/n)Q/Q, n = element order), "
           "C2 (existence of consistent 78/650 torsion profiles giving genuine characters; "
           "78 orthogonally realizable: even quaternionic multiplicities)",
           "e6_facts": facts}
    results = {}
    for name, banked in (("2T", (71192, 70262)), ("A4", (1089, 1028))):
        gs = _group_side(name)
        orders_needed = sorted({o for o in gs["orders"] if o >= 2})
        ach = torsion_profiles(orders_needed, W27, W78, W650)
        chiral, real, conj_of = _enumerate_window(gs)
        assert (len(chiral) + len(real), len(chiral)) == banked, \
            (name, len(chiral) + len(real), len(chiral), "window mismatch vs banked B356")
        att_c, surv_c = _sieve(gs, chiral, conj_of, ach)
        att_r, surv_r = _sieve(gs, real, conj_of, ach)
        # controls: the two REALIZED canonical assemblies must pass every layer (2T only)
        controls = None
        if name == "2T":
            controls = _canonical_controls(gs, ach)
        results[name] = {"orders": orders_needed,
                         "achievable_sizes": {n: len(ach[n]) for n in orders_needed},
                         "window_total": len(chiral) + len(real),
                         "window_chiral": len(chiral),
                         "attrition_chiral": att_c, "attrition_real": att_r,
                         "chiral_survivors": [list(v) for v in surv_c[:50]],
                         "chiral_survivor_count": att_c["pass_all"],
                         "real_survivor_count": att_r["pass_all"],
                         "controls": controls}
        print("  %s: window %d (chiral %d) | chiral attrition %s | real attrition %s"
              % (name, len(chiral) + len(real), len(chiral), att_c, att_r), flush=True)
    rep["groups"] = results
    ch2t = results["2T"]["chiral_survivor_count"]
    rep["verdict_data"] = ("NOT-FOUND-IN-BOUND: no chiral assembly survives"
                           if ch2t == 0 else
                           "%d chiral 2T assemblies survive all declared layers" % ch2t)
    rep["seconds"] = round(time.time() - t0, 1)
    out = os.path.join(HERE, "b501_piece1.json")
    json.dump(rep, open(out, "w"), indent=1)
    print("  wrote %s (%.0fs)" % (out, rep["seconds"]), flush=True)
    return rep


def _canonical_controls(gs, ach):
    """The two REALIZED 2T assemblies (B329): principal 3.1+3.1'+3.1''+6.3 and
    trinification 9.1+3.1'+3.1''+3.2'+3.2''. Both must pass C1, C3, C2."""
    import numpy as np
    chis, dims, fs, k = gs["chis"], gs["dims"], gs["fs"], gs["k"]
    one_i = next(i for i in range(len(chis))
                 if dims[i] == 1 and all(abs(chis[i][c] - 1) < 1e-9 for c in range(k)))
    om = [i for i in range(len(chis)) if dims[i] == 1 and i != one_i]
    two_q = [i for i in range(len(chis)) if dims[i] == 2 and fs[i] == -1]
    two_c = [i for i in range(len(chis)) if dims[i] == 2 and fs[i] == 0]
    three = [i for i in range(len(chis)) if dims[i] == 3]
    assert len(om) == 2 and len(two_q) == 1 and len(two_c) == 2 and len(three) == 1
    princ = [0] * len(chis)
    princ[one_i] = 3
    princ[om[0]] = princ[om[1]] = 3
    princ[three[0]] = 6
    trin = [0] * len(chis)
    trin[one_i] = 9
    trin[om[0]] = trin[om[1]] = 3
    trin[two_c[0]] = trin[two_c[1]] = 3
    out = {}
    for label, vec in (("principal", princ), ("trinification", trin)):
        att, surv = _sieve(gs, [tuple(vec)], list(range(len(chis))), ach)
        out[label] = {"vector": vec, "passes_all": att["pass_all"] == 1, "attrition": att}
        assert att["pass_all"] == 1, ("REALIZED control failed the sieve", label, att)
    return out


# =====================================================================================
# PIECE 3 -- the geometric theta-identification
# =====================================================================================
def _chain_bracket_couplings(CP):
    """EXACT block-coupling relations of the chain brackets: for every pair of chain
    basis vectors, express [w, w'] exactly in the chain basis (small Fraction solves
    per weight space) and record which blocks receive nonzero components."""
    E6 = CP.E6
    COLS = CP.COLS
    CH = CP.CHAINS
    by_weight = {}
    for (m, k) in COLS:
        by_weight.setdefault(2 * m - 2 * k, []).append((m, k))

    def solve_in_chain_basis(vec, wt):
        basis = by_weight.get(wt, [])
        if not vec:
            return {}
        assert basis, ("bracket weight outside chain weights", wt)
        support = sorted(set(vec) | {i for b in basis for i in CH[b[0]][b[1]]})
        rows = len(support)
        Amat = [[Fraction(CH[b[0]][b[1]].get(i, 0)) for b in basis] for i in support]
        bvec = [Fraction(vec.get(i, 0)) for i in support]
        # Gaussian elimination (exact)
        ncols = len(basis)
        piv = []
        r = 0
        for c in range(ncols):
            pr = next((i for i in range(r, rows) if Amat[i][c] != 0), None)
            if pr is None:
                continue
            Amat[r], Amat[pr] = Amat[pr], Amat[r]
            bvec[r], bvec[pr] = bvec[pr], bvec[r]
            pivval = Amat[r][c]
            Amat[r] = [x / pivval for x in Amat[r]]
            bvec[r] = bvec[r] / pivval
            for i in range(rows):
                if i != r and Amat[i][c] != 0:
                    f = Amat[i][c]
                    Amat[i] = [x - f * y for x, y in zip(Amat[i], Amat[r])]
                    bvec[i] = bvec[i] - f * bvec[r]
            piv.append(c)
            r += 1
        sol = {c: Fraction(0) for c in range(ncols)}
        for i, c in enumerate(piv):
            sol[c] = bvec[i]
        for i in range(r, rows):
            assert bvec[i] == 0, "bracket not in the chain span (impossible)"
        # verify
        chk = {}
        for c in range(ncols):
            if sol[c]:
                for i, x in CH[basis[c][0]][basis[c][1]].items():
                    chk[i] = chk.get(i, Fraction(0)) + sol[c] * Fraction(x)
        assert {i for i, v in chk.items() if v} == {i for i, v in vec.items() if v}
        for i, v in vec.items():
            assert chk.get(i, Fraction(0)) == Fraction(v), "solve verification failed"
        return {basis[c]: sol[c] for c in range(ncols) if sol[c]}

    relations = set()
    for i1, (m1, k1) in enumerate(COLS):
        for (m2, k2) in COLS[i1:]:
            br = E6.brk(CH[m1][k1], CH[m2][k2])
            br = {i: v for i, v in br.items() if v}
            if not br:
                continue
            comps = solve_in_chain_basis(br, (2 * m1 - 2 * k1) + (2 * m2 - 2 * k2))
            for (m3, _k3) in comps:
                relations.add((m1, m2, m3))
    return sorted(relations)


def _commutant_lemma(CP):
    """Solutions lam: EXPONENTS -> C* of lam_m lam_m' = lam_m'' over the exact coupling
    relations = the sl2-commutant of Aut(e6) (blockwise scalars by Schur). Computed by
    Smith normal form of the relation lattice. Expected: Z/2 = {1, theta}."""
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    rels = _chain_bracket_couplings(CP)
    idx = {m: i for i, m in enumerate(CP.EXPONENTS)}
    rows = []
    for (m1, m2, m3) in rels:
        row = [0] * 6
        row[idx[m1]] += 1
        row[idx[m2]] += 1
        row[idx[m3]] -= 1
        if any(row):
            rows.append(row)
    R = sp.Matrix(rows)
    snf = smith_normal_form(R)
    inv_factors = [int(snf[i, i]) for i in range(min(snf.shape)) if snf[i, i] != 0]
    rank = len(inv_factors)
    free_rank = 6 - rank
    n_solutions = None
    if free_rank == 0:
        n_solutions = 1
        for d in inv_factors:
            n_solutions *= d
    # verify the two expected solutions exactly
    eps = {m: (-1) ** (m + 1) for m in CP.EXPONENTS}
    ok_triv = all(1 * 1 == 1 for _ in rels)
    ok_eps = all(eps[m1] * eps[m2] == eps[m3] for (m1, m2, m3) in rels)
    return {"n_relations": len(rels), "relations": [list(r) for r in rels],
            "invariant_factors": inv_factors, "free_rank": free_rank,
            "n_solutions": n_solutions, "trivial_is_solution": ok_triv,
            "theta_pattern_is_solution": ok_eps}


def _zeval_block(CP, word, za, zb, m):
    mp = CP.mp
    n, o = CP.N_OF[m], CP.OFFSET[m]
    comp = {"a": mp.matrix([za[o + k] for k in range(n)]),
            "b": mp.matrix([zb[o + k] for k in range(n)])}
    z = mp.zeros(n, 1)
    P = mp.eye(n)
    for ch in word:
        if ch in "ab":
            zc = comp[ch]
        else:
            zc = -(CP.BLK[ch][m] * comp[ch.lower()])
        z = z + P * zc
        P = P * CP.BLK[ch][m]
    return z


def _conjv(mp, v):
    return mp.matrix([mp.conj(v[i]) for i in range(v.rows)])


def _involution_action(CP, inv, za, zb, m):
    """(Psi z)(g) = Sym(D) . (conj?) z(sinv(g)) per block -- B347's convention, in the
    B352 normalized-chain basis."""
    mp = CP.mp
    ea = _zeval_block(CP, inv["sinv"]["a"], za, zb, m)
    eb = _zeval_block(CP, inv["sinv"]["b"], za, zb, m)
    if inv["conjugate"]:
        ea, eb = _conjv(mp, ea), _conjv(mp, eb)
    RD = inv["RD"][m]
    return RD * ea, RD * eb


def _cob_residual(CP, m, ta, tb):
    """Relative distance of the block cochain (ta, tb) from im d^0 (least squares)."""
    mp = CP.mp
    _, d0 = CP.FOX[m]
    n = CP.N_OF[m]
    t = mp.matrix([ta[i] for i in range(n)] + [tb[i] for i in range(n)])
    U, sv, Vh = CP._svd(d0)
    y = U.transpose_conj() * t
    x = mp.zeros(n, 1)
    smax = max(abs(s) for s in sv)
    for i in range(len(sv)):
        if abs(sv[i]) > smax * mp.mpf(10) ** -40:
            for j in range(n):
                x[j] += mp.conj(Vh[i, j]) * y[i] / sv[i]
    return float(mp.norm(d0 * x - t))


def run_piece3():
    print("== PIECE 3: the geometric theta-identification ==", flush=True)
    t0 = time.time()
    CP = load_cp()
    CP._guard()
    mp = CP.mp
    E6, TG = CP.E6, CP.TG
    rep = {"piece": 3, "dps": int(CP._DPS)}
    eps = {m: (-1) ** (m + 1) for m in CP.EXPONENTS}
    # (a) EXACT: theta acts on ALL 78 chain vectors as the blockwise scalar (-1)^{m+1}
    th = E6.theta_map()
    exact_ok = True
    for (m, k) in CP.COLS:
        v = CP.CHAINS[m][k]
        tv = E6._apply(th, v)
        want = {i: eps[m] * c for i, c in v.items()}
        if not E6._vec_eq(tv, want):
            exact_ok = False
    rep["theta_blockwise_scalar_exact"] = exact_ok
    assert exact_ok, "theta is not the blockwise scalar (-1)^{m+1} on the chain basis"
    # theta fixes the geometric rep: Ad rho is block-diagonal, theta is blockwise scalar
    # => [theta, Ad rho(g)] = 0 exactly (structural; no computation needed).
    # (b) EXACT: the sl2-commutant of Aut(e6) is {1, theta}
    lem = _commutant_lemma(CP)
    rep["commutant_lemma"] = {k_: v for k_, v in lem.items() if k_ != "relations"}
    rep["commutant_lemma"]["relations_sample"] = lem["relations"][:12]
    assert lem["free_rank"] == 0 and lem["n_solutions"] == 2 \
        and lem["theta_pattern_is_solution"], lem
    print("  commutant lemma: %d relations, invariant factors %s -> exactly 2 solutions "
          "{1, theta}" % (lem["n_relations"], lem["invariant_factors"]), flush=True)
    # (c) NUMERIC: per-line intertwining at dps 100
    D_hyp = TG._solveD({"a": ("A", False), "b": ("B", False)})
    D_amp = TG._solveD({"a": ("ababAB", True), "b": ("baBA", True)})
    # intertwiner quality at the SL2 level
    def d_res(D, tgt, conj):
        worst = mp.mpf(0)
        for g in "ab":
            L = TG._ev(tgt[g])
            R = TG._BASE[g]
            if conj:
                R = mp.matrix([[mp.conj(R[i, j]) for j in range(2)] for i in range(2)])
            worst = max(worst, mp.norm(L - D * R * D ** -1))
        return float(worst)
    rep["sl2_intertwiner_residuals"] = {
        "hyperelliptic": d_res(D_hyp, {"a": "A", "b": "B"}, False),
        "amphichiral": d_res(D_amp, {"a": "ababAB", "b": "baBA"}, True)}
    HYP = dict(sinv={"a": "A", "b": "B"}, conjugate=False, RD=CP._block_rep(D_hyp))
    AMP = dict(sinv={"a": "abABab", "b": "BAba"}, conjugate=True, RD=CP._block_rep(D_amp))
    lines = {}
    for m in CP.EXPONENTS:
        za, zb = CP.h1_line(m)
        n, o = CP.N_OF[m], CP.OFFSET[m]
        z0a = mp.matrix([za[o + k] for k in range(n)])
        z0b = mp.matrix([zb[o + k] for k in range(n)])
        # hyperelliptic action
        ha, hb = _involution_action(CP, HYP, za, zb, m)
        r_theta = _cob_residual(CP, m, ha - eps[m] * z0a, hb - eps[m] * z0b)
        r_wrong = _cob_residual(CP, m, ha + eps[m] * z0a, hb + eps[m] * z0b)
        r_z0 = _cob_residual(CP, m, z0a, z0b)               # non-vacuity: z0 is no coboundary
        # amphichiral J^2 = +1 (the banked real structure), re-derived here
        ja, jb = _involution_action(CP, AMP, za, zb, m)
        jja, jjb = _involution_action(CP, AMP,
                                      _embed(CP, ja, m, "a"), _embed(CP, jb, m, "b"), m)
        r_j2 = _cob_residual(CP, m, jja - z0a, jjb - z0b)
        lines[m] = {"eps_expected": eps[m], "r_theta_match": r_theta,
                    "r_wrong_sign": r_wrong, "z0_noncoboundary": r_z0, "r_J2": r_j2}
        print("  m=%2d: |Psi z - (%+d) z mod B1| = %.2e | wrong sign %.2e | J^2 %.2e"
              % (m, eps[m], r_theta, r_wrong, r_j2), flush=True)
    rep["lines"] = {str(m): v for m, v in lines.items()}
    rep["seconds"] = round(time.time() - t0, 1)
    out = os.path.join(HERE, "b501_piece3.json")
    json.dump(rep, open(out, "w"), indent=1)
    print("  wrote %s (%.0fs)" % (out, rep["seconds"]), flush=True)
    return rep


def _embed(CP, vec_block, m, which):
    mp = CP.mp
    out = mp.zeros(CP.DIM, 1)
    o, n = CP.OFFSET[m], CP.N_OF[m]
    for k in range(n):
        out[o + k] = vec_block[k]
    return out


# =====================================================================================
# CLI
# =====================================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--piece", default="all", choices=["1", "2", "3", "all"])
    ap.add_argument("--dirs", default="cob,m1,m4,m8,mix48")
    ap.add_argument("--dps", type=int, default=100)
    ap.add_argument("--tag", default="main")
    ap.add_argument("--no-deltas", action="store_true")
    ap.add_argument("--no-gauge", action="store_true")
    ap.add_argument("--merge-piece2", action="store_true")
    ap.add_argument("--stage", choices=["solve", "jet4"], default=None,
                    help="piece-2 staged foreground mode (one direction per stage)")
    ap.add_argument("--dir", default=None)
    ap.add_argument("--repchecks", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    if args.merge_piece2:
        merge_piece2()
        return
    if args.stage == "solve":
        stage_solve(args.dir, args.tag, args.dps, repchecks=args.repchecks)
        return
    if args.stage == "jet4":
        stage_jet4(args.tag, args.dps)
        return
    if args.piece in ("1", "all"):
        run_piece1()
    if args.piece in ("3", "all"):
        run_piece3()
    if args.piece in ("2", "all"):
        run_piece2(args.dirs.split(","), args.dps, args.tag,
                   deltas=not args.no_deltas, gauge=not args.no_gauge)
        if args.piece == "all":
            merge_piece2()
    print("total %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
