"""B370 leg A -- the third-order obstruction (Massey leg), executed as pre-registered.

METHOD (jet arithmetic through the relator; no transcription of the BCH formula anywhere):
deform each generator image as rho_t(g) = exp(t*z1(g) + t^2*z2(g)) rho(g) and expand the
relator product X_t(rel) as a formal series I + t*P1 + t^2*P2 + t^3*P3 in the adjoint
representation (B352's two-basis architecture, dps 100). Then, self-gating:

  ||P1|| ~ 0   gates that z1 is a cocycle              (B352's first-order gate)
  ||P2|| ~ 0   gates that z2 solves the second order   (solved here per Fox block)
  ad(q3) = P3  defines the third-order obstruction vector (exact-Gram normal equations)

The class of q3 in H^2 is read per exponent block against B352's coker functionals, as
COMPLEX components (not magnitudes -- span arithmetic needs phases). The Massey verdict is
taken MODULO THE INDETERMINACY: z2 is defined up to Z^1, and shifting z2 by a basis cocycle
zeta_j moves the class by Delta_j = class(q3(z2+zeta_j)) - class(q3(z2)), computed by
finite differences on the SAME jet machinery (convention-safe). Verdict per direction:
the least-squares residual of class(q3) against span{Delta_j} -- compared to (i) the m=1
integrable control (must sit at the floor), (ii) an MB12 random-vector control against the
same span (must be O(1)).

Letter jets (exp of a single Lie element -- no BCH):
  lowercase g:  [X, A X, (B + A^2/2) X, ((AB+BA)/2 + A^3/6) X]
  uppercase g:  [Xi, -Xi A, Xi (A^2/2 - B), Xi ((AB+BA)/2 - A^3/6)]
with A = ad(z1(g)), B = ad(z2(g)) in root coordinates, X = Ad rho(letter).
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B352_cup_product_obstruction"))
import cup_product as CP                      # noqa: E402

mp = CP.mp
DIM = CP.DIM
EXPONENTS = CP.EXPONENTS
REL = CP.REL


def _to_root(vec_c):
    return CP.S * vec_c


def _solve_ad(P):
    """q with ad(q) = P via the exact-Gram normal equations (B352's solve)."""
    ads = CP._ad_sparse()
    b = mp.matrix([sum(c * P[k, j] for (k, j), c in ads[i].items()) for i in range(DIM)])
    q = mp.lu_solve(CP._gram(), b)
    R = mp.zeros(DIM, DIM)
    for i in range(DIM):
        qi = q[i]
        if qi != 0:
            for (k, j), c in ads[i].items():
                R[k, j] += qi * c
    res = mp.norm(R - P) / max(mp.norm(P), mp.mpf(10) ** -200)
    return q, res


def solve_z2(za_c, zb_c):
    """Blockwise least-squares z2 with d1_m w = -q2_chain_m; returns chain vectors."""
    q2, first, res = CP.obstruction_vector(za_c, zb_c)
    q2_c = CP.S_INV * q2
    wa, wb = mp.zeros(DIM, 1), mp.zeros(DIM, 1)
    worst_ls = mp.mpf(0)
    for m in EXPONENTS:
        d1, _ = CP.FOX[m]
        n, o = CP.N_OF[m], CP.OFFSET[m]
        rhs = mp.matrix([-q2_c[o + k] for k in range(n)])
        U, sv, Vh = CP._svd(d1)
        # pseudo-inverse solve (rank n-1; the H^2 residual is B352's banked zero)
        y = U.transpose_conj() * rhs
        w = mp.zeros(2 * n, 1)
        smax = max(abs(s) for s in sv)
        for i in range(len(sv)):
            if abs(sv[i]) > smax * mp.mpf(10) ** -40:
                for j in range(2 * n):
                    w[j] += mp.conj(Vh[i, j]) * y[i] / sv[i]
        worst_ls = max(worst_ls, mp.norm(d1 * w - rhs))   # absolute; scaled below
        for k in range(n):
            wa[o + k] = w[k]
            wb[o + k] = w[k + n]
    scale = max(mp.norm(q2_c), mp.mpf(10) ** -200)
    return wa, wb, float(first), float(worst_ls / scale)


def relator_jet3(za_c, zb_c, wa_c, wb_c):
    """(||P1||, ||P2||, q3_root, ad_res, q3_norm) of the order-3 relator expansion."""
    za, zb = _to_root(za_c), _to_root(zb_c)
    wa, wb = _to_root(wa_c), _to_root(wb_c)
    A = {"a": CP.ad_root(za), "b": CP.ad_root(zb)}
    B = {"a": CP.ad_root(wa), "b": CP.ad_root(wb)}
    J = {}
    for g in "ab":
        Ag, Bg = A[g], B[g]
        A2 = Ag * Ag
        AB = Ag * Bg + Bg * Ag
        A3 = A2 * Ag
        X = CP.X_root(g)
        Xi = CP.X_root(g.upper())
        half = mp.mpf(1) / 2
        sixth = mp.mpf(1) / 6
        J[g] = [X, Ag * X, (Bg + A2 * half) * X, (AB * half + A3 * sixth) * X]
        J[g.upper()] = [Xi, -(Xi * Ag), Xi * (A2 * half - Bg),
                        Xi * (AB * half - A3 * sixth)]
    P = [mp.eye(DIM), mp.zeros(DIM, DIM), mp.zeros(DIM, DIM), mp.zeros(DIM, DIM)]
    for ch in REL:
        L = J[ch]
        P = [P[0] * L[0],
             P[1] * L[0] + P[0] * L[1],
             P[2] * L[0] + P[1] * L[1] + P[0] * L[2],
             P[3] * L[0] + P[2] * L[1] + P[1] * L[2] + P[0] * L[3]]
    q3, res = _solve_ad(P[3])
    return float(mp.norm(P[1])), float(mp.norm(P[2])), q3, float(res), float(mp.norm(q3))


def class_complex(q_root):
    """COMPLEX H^2 class components per exponent block (phases kept for span math)."""
    q_c = CP.S_INV * q_root
    comps = []
    for m in EXPONENTS:
        u = CP.h2_functional(m)
        o, n = CP.OFFSET[m], CP.N_OF[m]
        comps.append(sum(mp.conj(u[k]) * q_c[o + k] for k in range(n)))
    return mp.matrix(comps)


def _span_residual(c0, deltas):
    """Least-squares residual of c0 against span{deltas} in C^6 (relative)."""
    Mcols = [d for d in deltas if mp.norm(d) > mp.mpf(10) ** -60]
    if not Mcols:
        return float(mp.norm(c0)), 0
    M = mp.zeros(6, len(Mcols))
    for j, d in enumerate(Mcols):
        for i in range(6):
            M[i, j] = d[i]
    U, sv, Vh = CP._svd(M)
    y = U.transpose_conj() * c0
    x = mp.zeros(len(Mcols), 1)
    smax = max(abs(s) for s in sv)
    rank = 0
    for i in range(len(sv)):
        if abs(sv[i]) > smax * mp.mpf(10) ** -30:
            rank += 1
            for j in range(len(Mcols)):
                x[j] += mp.conj(Vh[i, j]) * y[i] / sv[i]
    resid = mp.norm(M * x - c0) / max(mp.norm(c0), mp.mpf(10) ** -200)
    return float(resid), rank


def massey_direction(label, za_c, zb_c, zbasis):
    """Full pre-registered readout for one direction."""
    t0 = time.time()
    wa, wb, first2, lsres = solve_z2(za_c, zb_c)
    p1, p2, q3, adres, q3n = relator_jet3(za_c, zb_c, wa_c=wa, wb_c=wb)
    c0 = class_complex(q3)
    deltas = []
    for (ka, kb) in zbasis:
        _, _, q3s, _, _ = relator_jet3(za_c, zb_c, wa + ka, wb + kb)
        deltas.append(class_complex(q3s) - c0)
    resid, rank = _span_residual(c0, deltas)
    # MB12: random vectors must NOT sit in the indeterminacy span
    import random
    rnd = random.Random(11)
    mb12 = []
    for _ in range(3):
        v = mp.matrix([rnd.uniform(-1, 1) + 1j * rnd.uniform(-1, 1) for _ in range(6)])
        r, _ = _span_residual(v, deltas)
        mb12.append(r)
    return {
        "label": label,
        "gate_P1": p1, "gate_P2": p2, "z2_ls_residual": lsres,
        "ad_solve_residual": adres, "q3_norm": q3n,
        "class_abs": [float(abs(c0[i])) for i in range(6)],
        "class_norm": float(mp.norm(c0)),
        "indeterminacy_rank": rank,
        "transverse_residual": resid,
        "mb12_random_residuals": mb12,
        "seconds": round(time.time() - t0, 1),
    }


def run_all():
    rep = {}
    worst_rel, worst_auto = CP.rep_checks()
    rep["rep_checks"] = {"relator": float(worst_rel), "automorphism": float(worst_auto)}
    z = {m: CP.h1_line(m) for m in EXPONENTS}
    zbasis = [z[m] for m in EXPONENTS]
    # gate (ii): the coboundary control -- its class must be trivial at order 3 too
    import random
    rnd = random.Random(5)
    v = mp.matrix([rnd.uniform(-1, 1) for _ in range(DIM)])
    cza, czb = mp.zeros(DIM, 1), mp.zeros(DIM, 1)
    for m in EXPONENTS:
        o, n = CP.OFFSET[m], CP.N_OF[m]
        vm = mp.matrix([v[o + k] for k in range(n)])
        wa_ = CP.BLK["a"][m] * vm - vm
        wb_ = CP.BLK["b"][m] * vm - vm
        for k in range(n):
            cza[o + k] = wa_[k]
            czb[o + k] = wb_[k]
    nrm = mp.sqrt(mp.norm(cza) ** 2 + mp.norm(czb) ** 2)
    results = []
    r = massey_direction("coboundary", cza / nrm, czb / nrm, zbasis)
    results.append(r)
    print(f"  {r['label']}: P1={r['gate_P1']:.1e} |class|={r['class_norm']:.3e} "
          f"transverse={r['transverse_residual']:.3e}", flush=True)
    order = [1] + [m for m in EXPONENTS if m != 1]        # the m=1 control FIRST
    for m in order:
        r = massey_direction(f"m={m}", z[m][0], z[m][1], zbasis)
        results.append(r)
        print(f"  {r['label']}: P1={r['gate_P1']:.1e} P2={r['gate_P2']:.1e} "
              f"|class|={r['class_norm']:.3e} transverse={r['transverse_residual']:.3e} "
              f"rank={r['indeterminacy_rank']} mb12={min(r['mb12_random_residuals']):.2f} "
              f"({r['seconds']}s)", flush=True)
    rep["directions"] = results
    with open(os.path.join(HERE, "massey_legA.json"), "w") as fh:
        json.dump(rep, fh, indent=1)
    return rep


if __name__ == "__main__":
    t0 = time.time()
    run_all()
    print(f"total: {time.time() - t0:.0f}s")
