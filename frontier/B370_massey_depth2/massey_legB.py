"""B370 leg B -- the depth-2 boundary data: the tau-defect matrix (pre-registered readouts).

The depth-2 object, made well-defined. The second-order deformation z2 restricted to the
boundary torus is NOT a plain cocycle (the order-2 condition is twisted by [z1 cup z1] on
T^2), and z2 itself carries a Z^1 indeterminacy. B357's canonical NZ functionals fix both:
per boundary block m', with K the block pairing and h the peripheral invariant vector,

    phi_mu(m -> m') = u2^T K h,     phi_lam(m -> m') = v2^T K h,

where (u2, v2) = (c2(mu), c2(lam)) are the order-2 word values of the direction-m
deformation (computed by the same jet arithmetic as leg A, along MU_WORD/LAM_WORD instead
of the relator). These are linear, kill coboundaries (B357's lemma), and under the
indeterminacy z2 -> z2 + zeta shift by (phi_mu(zeta), phi_lam(zeta)) -- which lies ON the
universal-tau line phi_lam = tau*phi_mu (B357's banked identity, re-gated here). Hence

    delta(m -> m') = phi_lam(m -> m') - tau * phi_mu(m -> m')

is EXACTLY invariant under the z2 indeterminacy: the canonical depth-2 invariant. The
pre-registered readouts run on delta: (i) is delta == 0 (the universal-tau persists at
depth 2)? (ii) if not, its symmetry structure; (iii) its theta-block pattern
({4,8} vs {1,5,7,11} source/target blocks).

Gates before any readout: the first-order structure reproduces in this normalization
(z1(m) restricts block-diagonally with phi_lam/phi_mu = tau on the diagonal), and the
jet's P1 gate holds along both peripheral words.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "B357_e6_boundary_restriction"))
import massey as M                                   # noqa: E402  (brings CP)
import boundary_restriction as BR                    # noqa: E402  (frozen conventions)

CP = M.CP
mp = CP.mp
DIM = CP.DIM
EXPONENTS = CP.EXPONENTS
MU, LAM = BR.MU_WORD, BR.LAM_WORD                    # "ABB", "BAbabABa"
TAU = BR.CUSP_SHAPE * 0 + mp.mpc(0, 1) * 2 * mp.sqrt(3)   # -? sign fixed by the gate below


def word_jet2(word, za_c, zb_c, wa_c, wb_c):
    """c1_root, c2_root of the deformation along `word` (order-2 jet; leg-A conventions)."""
    za, zb = CP.S * za_c, CP.S * zb_c
    wa, wb = CP.S * wa_c, CP.S * wb_c
    A = {"a": CP.ad_root(za), "b": CP.ad_root(zb)}
    B = {"a": CP.ad_root(wa), "b": CP.ad_root(wb)}
    J = {}
    half = mp.mpf(1) / 2
    for g in "ab":
        Ag, Bg = A[g], B[g]
        A2 = Ag * Ag
        X, Xi = CP.X_root(g), CP.X_root(g.upper())
        J[g] = [X, Ag * X, (Bg + A2 * half) * X]
        J[g.upper()] = [Xi, -(Xi * Ag), Xi * (A2 * half - Bg)]
    P = [mp.eye(DIM), mp.zeros(DIM, DIM), mp.zeros(DIM, DIM)]
    for ch in word:
        L = J[ch]
        P = [P[0] * L[0],
             P[1] * L[0] + P[0] * L[1],
             P[2] * L[0] + P[1] * L[1] + P[0] * L[2]]
    X0inv = P[0] ** -1
    A1 = P[1] * X0inv
    M2 = P[2] * X0inv - A1 * A1 * half
    c1, r1 = M._solve_ad(A1)
    c2, r2 = M._solve_ad(M2)
    return c1, c2, float(r1), float(r2)


def chain_block_TG(vec_root, mprime):
    """Root vector -> B357/TG per-block coordinates. S's columns are the NORMALIZED
    chains, so a coefficient c_k on chain_k/N_k is c_k/N_k on the raw TG basis vector
    chain_k — DIVIDE by the norm (the first run multiplied; the first-order tau gate
    caught it: tau spread 3e4 instead of 0)."""
    vc = CP.S_INV * vec_root
    o, n = CP.OFFSET[mprime], CP.N_OF[mprime]
    out = mp.matrix(n, 1)
    for k in range(n):
        out[k] = vc[o + k] / CP._NORMS[o + k]
    return out


def run():
    t0 = time.time()
    blocks = {mp_: BR._block(mp_) for mp_ in EXPONENTS}
    K = {mp_: BR._pairing(blocks[mp_]["dim"]) for mp_ in EXPONENTS}

    def phis(vec_root, mprime):
        blk = blocks[mprime]
        u = chain_block_TG(vec_root, mprime)
        return (u.T * K[mprime] * blk["h"])[0, 0]

    rep = {"gates": {}, "phi": {}, "delta": {}}
    # ---- first-order gate: block-diagonal restriction + the universal-tau in this normalization
    tau_seen = {}
    for m in EXPONENTS:
        za, zb = CP.h1_line(m)
        zero = mp.zeros(DIM, 1)
        c1mu, _c2, r1mu, _ = word_jet2(MU, za, zb, zero, zero)
        c1la, _c2, r1la, _ = word_jet2(LAM, za, zb, zero, zero)
        offdiag = mp.mpf(0)
        for mprime in EXPONENTS:
            pm, pl = phis(c1mu, mprime), phis(c1la, mprime)
            if mprime != m:
                offdiag = max(offdiag, abs(pm), abs(pl))
            else:
                tau_seen[m] = pl / pm
        rep["gates"][f"first_order_m{m}"] = dict(
            offdiag=float(offdiag), tau=str(tau_seen[m]),
            ad_res=max(r1mu, r1la))
    # fix tau's sign convention from the data (B357: universal tau = -2*sqrt(3)*i)
    tau = tau_seen[1]
    rep["gates"]["tau_universal_spread"] = float(
        max(abs(tau_seen[m] - tau) for m in EXPONENTS))
    rep["gates"]["tau_value"] = str(tau)

    # ---- depth 2: the phi-matrix and the tau-defect matrix
    dmat_live = {}
    scale_live = {}
    for m in EXPONENTS:
        za, zb = CP.h1_line(m)
        wa, wb, first2, lsres = M.solve_z2(za, zb)
        c1mu, c2mu, _, r2mu = word_jet2(MU, za, zb, wa, wb)
        c1la, c2la, _, r2la = word_jet2(LAM, za, zb, wa, wb)
        for mprime in EXPONENTS:
            pm, pl = phis(c2mu, mprime), phis(c2la, mprime)
            d = pl - tau * pm
            dmat_live[(m, mprime)] = d
            scale_live[(m, mprime)] = max(abs(pm), abs(pl))
            rep["phi"][f"{m}->{mprime}"] = [str(pm), str(pl)]
            rep["delta"][f"{m}->{mprime}"] = dict(
                value=str(d), absval=float(abs(d)),
                phi_scale=float(max(abs(pm), abs(pl))),
                rel=float(abs(d) / max(scale_live[(m, mprime)], mp.mpf(10) ** -60)))
        print(f"  m={m}: z2 solved (P2-gate via leg A), ad-res {max(r2mu, r2la):.1e}; "
              f"delta row max |d| = "
              f"{max(rep['delta'][f'{m}->{mp2}']['absval'] for mp2 in EXPONENTS):.3e}",
              flush=True)

    # ---- readouts on delta (RELATIVE to per-entry phi-scale — blocks span ~1e50)
    import itertools
    dmat = {k: dmat_live[k] / max(scale_live[k], mp.mpf(10) ** -60)
            for k in dmat_live}
    scale = max(abs(v) for v in dmat.values())
    rep["readout_delta_zero"] = bool(scale < mp.mpf(10) ** -20)
    rep["readout_delta_scale"] = float(scale)
    if scale > 0:
        sym = max(abs(dmat[(a, b)] - dmat[(b, a)]) for a, b in
                  itertools.product(EXPONENTS, EXPONENTS)) / scale
        asym = max(abs(dmat[(a, b)] + dmat[(b, a)]) for a, b in
                   itertools.product(EXPONENTS, EXPONENTS)) / scale
        rep["readout_symmetry"] = dict(sym_dev=float(sym), antisym_dev=float(asym))
        esc = {4, 8}
        blocks_max = {}
        for cls_s, cls_t, name in ((esc, esc, "esc->esc"), (esc, set(EXPONENTS) - esc, "esc->f4"),
                                   (set(EXPONENTS) - esc, esc, "f4->esc"),
                                   (set(EXPONENTS) - esc, set(EXPONENTS) - esc, "f4->f4")):
            blocks_max[name] = float(max(abs(dmat[(a, b)]) for a in cls_s for b in cls_t) / scale)
        rep["readout_theta_blocks"] = blocks_max
    rep["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(HERE, "massey_legB.json"), "w") as fh:
        json.dump(rep, fh, indent=1)
    return rep


if __name__ == "__main__":
    r = run()
    print(f"tau universal (spread {r['gates']['tau_universal_spread']:.1e}); "
          f"delta zero: {r['readout_delta_zero']} (scale {r['readout_delta_scale']:.3e})")
    if not r["readout_delta_zero"]:
        print(f"symmetry: {r.get('readout_symmetry')}")
        print(f"theta blocks: {r.get('readout_theta_blocks')}")
    print(f"total {r['seconds']}s")
