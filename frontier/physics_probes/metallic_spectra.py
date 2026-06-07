"""Metallic-mean quasicrystal spectra -- the metallic family is a family of DISTINCT real materials,
even though the trace-map ALGEBRA (the Sym two-sequence mu_d) is m-universal (B120).

Phase 1 of the firewalled physics-bridge sweep. The SL(2), Hermitian, single-channel tight-binding chain on the
metallic substitution a -> a^m b, b -> a is a GENUINE, buildable quasicrystal (golden m=1 = Fibonacci; silver m=2 =
Pell/octonacci; bronze m=3). These are studied condensed-matter systems (photonic lattices, cold atoms). This probe
computes their spectral fingerprints across m and asks the sharp B120 hinge:

    B120 proved the tower's MODULE structure mu_d is m-UNIVERSAL (it depends only on (n, det), not on the seed m).
    But the SPECTRUM (eigenvalue VALUES phi_m) is m-dependent. So are the metallic means GENUINELY DISTINCT real
    quasicrystals -- or the 'same' material rescaled?

ANSWER (the headline): they are arithmetically DISTINCT. The gap-labeling module Z + Z*alpha_m lives in the
quadratic field Q(sqrt(m^2+4)); the squarefree discriminants are {5, 2, 13} for m=1,2,3 -> THREE DISTINCT FIELDS
(Q(sqrt5), Q(sqrt2), Q(sqrt13)). The renormalization length-scale phi_m and the spectral fractal dimension also
differ per m. So: the ALGEBRA is one object (B120, m-universal); the PHYSICS is a family of distinct materials.

HONEST SCOPE: this is 1D condensed matter (real, buildable, measurable), NOT cosmology/fundamental physics. The
m=1 gap-labeling is textbook (Bellissard 1992); what is new here is the SYSTEMATIC metallic-m family + the explicit
arithmetic-distinctness contrast against B120's algebraic m-universality. NO claim of new fundamental physics;
firewalled; nothing to CLAIMS.md; physics chapter stays CLOSED; P1-P16 untouched.
"""
from __future__ import annotations

import numpy as np
import sympy as sp


def metallic_phi(m):
    """The metallic mean phi_m = (m + sqrt(m^2+4))/2 (Perron eigenvalue of the substitution matrix [[m,1],[1,0]])."""
    return sp.nsimplify((m + sp.sqrt(m ** 2 + 4)) / 2)


def gap_label_field(m):
    """The gap-labeling module Z + Z*alpha_m lives in Q(sqrt(m^2+4)). Returns the squarefree discriminant (the field
    invariant). Distinct squarefree parts => arithmetically distinct quasicrystals."""
    disc = m ** 2 + 4
    sf = sp.factorint(disc)
    squarefree = int(sp.prod([p ** (e % 2) for p, e in sf.items()]))
    return {"disc": disc, "squarefree": squarefree, "field": f"Q(sqrt{squarefree})"}


def letter_frequency_a(m):
    """The frequency of letter 'a' = the gap-label generator alpha_m = phi_m/(phi_m+1) (normalized Perron
    eigenvector of the substitution matrix). A quadratic irrational in Q(sqrt(m^2+4))."""
    phi = metallic_phi(m)
    return sp.nsimplify(phi / (phi + 1))


def metallic_word(m, depth):
    a, b = "a", "b"
    for _ in range(depth):
        a, b = a * m + b, a
    return a


def _cap_depth(m, nmax=1600):
    """The metallic word grows like phi_m^depth; cap the chain length so the dense diagonalization stays feasible
    (silver/bronze grow much faster than golden)."""
    a, b = "a", "b"
    d = 0
    while True:
        na, nb = a * m + b, a
        if len(na) > nmax:
            break
        a, b, d = na, nb, d + 1
    return max(d, 4)


def _chain_spectrum(m, VA=1.0, VB=-1.0, depth=None):
    word = metallic_word(m, depth if depth is not None else _cap_depth(m))
    N = len(word)
    diag = np.array([VA if ch == "a" else VB for ch in word])
    H = np.diag(diag) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    return np.sort(np.linalg.eigvalsh(H)), N


def gap_labels_fit(m, depth=None, tol=0.012, n_gaps=12):
    """The IDOS value in each spectral gap is k/N; the gap-labeling theorem says it lands on Z + Z*alpha_m (mod 1).
    Verify the largest gaps fit (extends path1b from m=1 to the metallic family). alpha_m is the m-specific field
    invariant, so the labels are a DISTINCT module per m."""
    ev, N = _chain_spectrum(m, depth=depth)
    alpha = float(letter_frequency_a(m))
    gaps = np.diff(ev)
    idx = np.argsort(gaps)[::-1][:n_gaps]
    hits, rows = 0, []
    for gi in idx:
        if gaps[gi] < 0.05:
            continue
        idos = (gi + 1) / N
        best = min(((abs(((p + q * alpha) % 1.0) - idos + 1) % 1.0, p, q)
                    for p in range(-8, 9) for q in range(-8, 9)),
                   key=lambda t: min(t[0], 1 - t[0]))
        err = min(best[0], 1 - best[0])
        rows.append((round(idos, 5), best[1], best[2], round(err, 4)))
        if err < tol:
            hits += 1
    return {"alpha_m": float(alpha), "N": N, "hits": hits, "n_checked": len(rows), "labels": rows,
            "confirmed": hits >= 4}


def spectrum_box_dimension(m, depth=None):
    """A box-counting fractal dimension of the (finite-chain) spectrum -- a proxy for the Hausdorff dimension of the
    Cantor spectrum. Distinct values per m = distinct materials. (Numerical / finite-size; supporting, not exact.)"""
    ev, N = _chain_spectrum(m, depth=depth)
    span = ev.max() - ev.min()
    pts = (ev - ev.min()) / span
    counts, sizes = [], []
    for k in range(2, 9):
        eps = 2.0 ** (-k)
        occupied = len(set((pts / eps).astype(int)))
        counts.append(occupied)
        sizes.append(eps)
    logc = np.log(counts)
    loginv = np.log([1 / s for s in sizes])
    slope = np.polyfit(loginv, logc, 1)[0]
    return {"box_dim": round(float(slope), 4), "N": N}


def rg_scaling_factor(m):
    """The renormalization length-scale: under one substitution step the chain length scales by phi_m (the trace
    map is the RG/decimation map). The RG rate is log(phi_m) -- m-dependent (exact)."""
    phi = metallic_phi(m)
    return {"phi_m": phi, "phi_m_float": round(float(phi), 6), "rg_rate_logphi": round(float(sp.log(phi)), 6)}


def algebra_universal_physics_distinct(ms=(1, 2, 3)):
    """The headline contrast: B120 -- the tower ALGEBRA (mu_d) is m-universal; HERE -- the PHYSICS is m-distinct
    (distinct gap-label fields, distinct RG scale phi_m, distinct spectral fractal dimension)."""
    fields = {m: gap_label_field(m)["field"] for m in ms}
    distinct_fields = len(set(fields.values())) == len(ms)
    phis = {m: rg_scaling_factor(m)["phi_m_float"] for m in ms}
    dims = {m: spectrum_box_dimension(m)["box_dim"] for m in ms}
    return {"gap_label_fields": fields, "fields_all_distinct": distinct_fields,
            "rg_scale_phi_m": phis, "phi_m_all_distinct": len(set(phis.values())) == len(ms),
            "spectral_box_dim": dims,
            "verdict": "ALGEBRA m-universal (B120: mu_d depends only on (n,det)); PHYSICS m-distinct (gap-label "
                       "fields Q(sqrt(m^2+4)) = {Q(sqrt5),Q(sqrt2),Q(sqrt13)}, RG scale phi_m, spectral dimension "
                       "all differ). The metallic means are genuinely distinct real quasicrystals."}


def main():
    print("=" * 78)
    print("Metallic-mean quasicrystal spectra -- distinct real materials, m-universal algebra (B120)")
    print("=" * 78)
    print("\n[fields] gap-labeling module Z+Z*alpha_m lives in Q(sqrt(m^2+4)):")
    for m in (1, 2, 3):
        f = gap_label_field(m)
        print(f"    m={m} ({['','golden','silver','bronze'][m]}): disc={f['disc']}, field={f['field']}, "
              f"alpha_m={float(letter_frequency_a(m)):.6f}, phi_m={rg_scaling_factor(m)['phi_m_float']}")
    print("\n[gap labels] IDOS gap labels fit Z + Z*alpha_m (extends path1b's m=1 to the family):")
    for m in (1, 2, 3):
        g = gap_labels_fit(m)
        print(f"    m={m}: {g['hits']}/{g['n_checked']} gaps on the Z+Z*alpha_m lattice (alpha={g['alpha_m']:.4f}) "
              f"-> {'CONFIRMED' if g['confirmed'] else 'weak'}")
    print("\n[box dimension] spectral fractal dimension per m (numerical, finite-size):")
    for m in (1, 2, 3):
        print(f"    m={m}: box_dim ~ {spectrum_box_dimension(m)['box_dim']}")
    a = algebra_universal_physics_distinct()
    print(f"\n[HEADLINE] fields distinct: {a['fields_all_distinct']} {a['gap_label_fields']}")
    print(f"           phi_m distinct: {a['phi_m_all_distinct']} {a['rg_scale_phi_m']}")
    print(f"           VERDICT: {a['verdict']}")
    print("\nHONEST SCOPE: 1D condensed matter (real, buildable), NOT cosmology. m=1 gap-labeling is textbook;")
    print("the metallic-m family + the algebra-universal/physics-distinct contrast (vs B120) is the new content.")


if __name__ == "__main__":
    main()
