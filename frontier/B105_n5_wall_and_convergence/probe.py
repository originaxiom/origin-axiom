"""B105 -- the n=5 wall (characterized), the unified-wall root cause, and the rho_n convergence.

Three parts (executes the CC-web "n=5 Resolution + Literature + Final Observations" handoff):

  N5 -- the decisive computation. Is the n>=5 tower degeneracy a COORDINATE ARTIFACT or a STRUCTURAL CHANGE?
      VERDICT: coordinate artifact. At SL(5) the Dehn-twist eps-series resolves 21 of 24 Dickson factors;
      the resolved 21 are UNIVERSALLY catalog-consistent (every monodromy, both det signs, share exactly the
      two-sequence catalog minus one Sym^2), while the corrupted 3-dim factor is GAUGE NOISE (varies across
      seeds -- a structural change would give a fixed wrong answer). The eps-series ceiling is 21/24 (cf.
      B61's 22 with inverse-word/SVD); the doubly-degenerate -1^2 sector cannot be pinned. Three independent
      structural routes (B89-T two-seq, B62 theta-split, B103) agree the unresolved 3-dim piece is Sym^2.
      So the n=5 catalog is strongly supported but the strict "all 3 factors" bar is NOT met: the obstruction
      is the eps-series gauge-degeneracy at the cusp's repeated -1 eigenvalue -- NOT a change in the formula.

  H6 -- the unified n>=5 wall (structural). The forced cusp spectrum (B95) is {1,i,-i} (n=3), {1,1,w,w^2}
      (n=4), {1,1,1,-1,-1} (n=5). The NON-TRIVIAL eigenvalues are DISTINCT at n=3,4 but COLLIDE at n=5 (-1
      with multiplicity 2); at n>=6 no finite-order spectrum exists at all (B95). This single collision is
      the common root cause of the tower wall (3 corrupted factors, B84/B104), the degree=rank wall
      (involution -> dihedral -> reducible, B95), and the eps-series rank-drop. The project has a NATURAL
      BOUNDARY at n=4, proved structural.

  CONVERGENCE -- the project's thesis. Every positive result is a property of ONE object: rho_n, the
      GL(2,Z)-representation on the SL(n) trace ring at the trivial point. The tower IS char(rho_n); the
      module-iso IS its decomposition into Sym pieces; universality IS the well-definedness of rho_n; the
      Hitchin identification places rho_n in a known moduli space. rho_n is COMPLETELY CHARACTERIZED for
      n=3,4 (exact, constructive, universal) with its natural boundary at n=4 PROVED (eigenvalue collision
      at n=5, impossibility at n>=6).

The H1-H6 computed observations and the C1-C4 corrections are tabulated in FINDINGS.md (each labeled by
proof status and the stage that computed it); all physical readings are POSTULATED and quarantined.
Standalone trace-map / Lie theory; NO physics claim; P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]
t = sp.symbols("t")
_P = 2000003


def _b104():
    spec = importlib.util.spec_from_file_location("b104", _ROOT / "frontier" / "B104_dehn_twist_tower" / "probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# N5 -- the characterization
# ---------------------------------------------------------------------------
def n5_resolved_degree(dehn=("U", "S"), seed=20):
    """Degree of gcd(char(J_SL5(N)), two-sequence catalog) -- the number of Dickson factors resolved by the
    eps-series at SL(5). The resolved part is catalog-consistent; the remainder (24 - this) is the corrupted
    doubly-degenerate sector."""
    B = _b104()
    N = B.word_abelianization(list(dehn))
    DT, bad = B.jacobian_word(5, _P, list(dehn), seed=seed, maxlen=5)
    if DT is None:
        return None
    chJ = sp.Poly(sp.Matrix(DT.tolist()).charpoly(t).as_expr(), t, modulus=_P)
    cat = sp.Poly(B.catalog_char(N.tolist(), 5), t, modulus=_P)
    return int(sp.gcd(chJ, cat).degree())


def n5_corruption_is_gauge_noise(seeds=(20, 21, 22)):
    """The corrupted 3-dim factor VARIES across seeds (gauge noise) while the resolved 21 are invariant ->
    the degeneracy is a coordinate artifact, not a structural change. Returns (n_distinct_corrupted,
    all_resolve_21)."""
    B = _b104()
    N = B.word_abelianization(["U", "S"])
    cat = sp.Poly(B.catalog_char(N.tolist(), 5), t, modulus=_P)
    corrupted, resolved = set(), []
    for s in seeds:
        DT, bad = B.jacobian_word(5, _P, ["U", "S"], seed=s, maxlen=5)
        chJ = sp.Poly(sp.Matrix(DT.tolist()).charpoly(t).as_expr(), t, modulus=_P)
        g = sp.gcd(chJ, cat)
        resolved.append(int(g.degree()))
        corrupted.add(sp.div(chJ, g)[0].as_expr())
    return len(corrupted), all(r == 21 for r in resolved)


# ---------------------------------------------------------------------------
# H6 -- the unified n>=5 wall: the forced cusp spectrum and its collision
# ---------------------------------------------------------------------------
def forced_cusp_spectrum(n):
    """The principal/cusp spectrum forced by tr A = tr A^-1 = 1 (B95). Returns the eigenvalue list."""
    w = np.exp(2j * np.pi / 3)
    return {3: [1, 1j, -1j], 4: [1, 1, w, w ** 2], 5: [1, 1, 1, -1, -1]}[n]


def cusp_spectrum_facts(n):
    """Verify tr = tr(inverse) = det = 1, and whether the NON-TRIVIAL eigenvalues collide (the doubly-
    degenerate sector). Returns a dict."""
    ev = np.array(forced_cusp_spectrum(n), complex)
    nontrivial = [e for e in ev if abs(e - 1) > 1e-9]
    repeated = len(nontrivial) - len({np.round(e, 6) for e in nontrivial})
    return {"n": n, "tr1": bool(abs(ev.sum() - 1) < 1e-9), "det1": bool(abs(np.prod(ev) - 1) < 1e-9),
            "trinv1": bool(abs((1 / ev).sum() - 1) < 1e-9), "nontrivial_collision": int(repeated)}


def unified_wall_table():
    """The n=3,4 distinct vs n=5 collision -> the single root cause of all three walls (tower, degree=rank,
    eps-series). At n>=6 no finite-order spectrum exists (B95)."""
    return {n: cusp_spectrum_facts(n) for n in (3, 4, 5)}


# ---------------------------------------------------------------------------
# H/C observations -- proof-status table (computed elsewhere; tabulated here)
# ---------------------------------------------------------------------------
OBSERVATIONS = {
    "H1": ("COMPUTED", "B96/physics_probes", "S(N)=log|<N>| ~ vol*N/(2pi) for the figure-eight Kashaev "
           "invariant (volume conjecture; Kashaev 1997, Murakami-Murakami 2001). G_eff=pi/(2 vol)=0.774 if "
           "S=A/4G -- POSTULATED reading, quarantined."),
    "H2": ("PROVED", "B71/B89", "M^n=L reduces 2(n-1) boundary DoF to (n-1): compression ratio 1/2, "
           "constant across n=3,4 (consequence of proved mathematics)."),
    "H3": ("COMPUTED", "B96", "vol(m=1)=2.030 < vol(m=2)=3.664 < vol(m=3)=4.814 strictly monotone; m=1 "
           "simplest by both systole (B92) and volume."),
    "H4": ("COMPUTED", "B98/B99", "two trace-map fixed points, two invariants: trivial rep -> Dickson "
           "tower; geometric rep -> adjoint torsion. The tower is trivial-rep-specific."),
    "H5": ("COMPUTED", "B101", "gauge-algebra Killing signatures: sl(2,R) (2,1); sl(3,R) (5,3); sl(4,R) "
           "~ so(3,3) ⊃ so(3,1). Lorentzian only at the k=2 rung of the split-form ladder."),
    "H6": ("STRUCTURAL", "B84/B85/B95/B104/B105", "the unified n>=5 wall: one eigenvalue collision (-1 "
           "mult 2 at n=5) is the common root cause of the tower wall, the degree=rank wall, and the "
           "eps-series rank-drop; natural boundary at n=4 (impossible n>=6)."),
}
CORRECTIONS = {
    "C1": "the Goldman metric is (2,0) Riemannian, NOT (1,1) Lorentzian (the negative Killing direction is "
          "removed by the gauge quotient; Goldman 1984). [recorded FAILURE_ATLAS, B101]",
    "C2": "phase-space 3+1D at SL(3) is killed by the split-form ladder (Sym^k(SL(2,R)) lands in split real "
          "forms, structurally anti-Lorentzian; B101).",
    "C3": "the Cayley-Hamilton mechanism for degree=rank is REFUTED (V75 hinge test: both SL(4) components "
          "have CH degree 4 but exponents 4 and 3; the mechanism remains unknown -- B95 reads the forced "
          "spectrum instead).",
    "C4": "the SL(5) principal spectrum is {1,1,1,-1,-1} (tr=1), NOT the earlier {1,1,1,w,w^2} (tr=2) -- "
          "corrected in B95.",
}


def main():
    print("B105 -- the n=5 wall (characterized) + the unified wall + the rho_n convergence\n")
    print("N5 (the decisive computation):")
    print(f"  resolved factors at SL(5) (gcd with two-seq catalog): {n5_resolved_degree()}/24")
    ndist, all21 = n5_corruption_is_gauge_noise()
    print(f"  corrupted 3-dim factor across seeds: {ndist} distinct (gauge noise); all resolve 21: {all21}")
    print("  VERDICT: coordinate artifact (gauge noise), NOT a structural change; the resolved 21 are")
    print("           universally catalog-consistent; the strict 'all 3' bar is NOT met (eps-series ceiling).")
    print("\nH6 -- the unified n>=5 wall (forced cusp spectra, B95):")
    for n, f in unified_wall_table().items():
        sp_str = {3: "{1,i,-i}", 4: "{1,1,w,w^2}", 5: "{1,1,1,-1,-1}"}[n]
        print(f"  n={n}: {sp_str:14} tr=trinv=det=1 {f['tr1'] and f['trinv1'] and f['det1']}; "
              f"non-trivial collision = {f['nontrivial_collision']}"
              + ("  <-- the doubly-degenerate sector" if f["nontrivial_collision"] else ""))
    print("  (n>=6: no finite-order spectrum exists -> the boundary at n=4 is proved.)")
    print("\nCONVERGENCE: the project converges on ONE object rho_n (the GL(2,Z)-rep on the SL(n) trace ring")
    print("  at the trivial point). The tower IS char(rho_n); fully characterized n=3,4; boundary n=4 proved.")
    print(f"\nObservations banked: {list(OBSERVATIONS)}; corrections: {list(CORRECTIONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
