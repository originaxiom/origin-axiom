"""B105 -- the n=5 wall (characterized), the unified-wall root cause, and the rho_n convergence.

Three parts (executes the CC-web "n=5 Resolution + Literature + Final Observations" handoff):

  *** CORRECTIONS A & B applied (V90 audit, explicit downgrade -- see CORRECTIONS_V90 below). Two prior
      inferences in this stage overreached the evidence; the corrected statements are what this stage now
      asserts. The COMPUTATION (21/24 universal) and the rho_n thesis are unchanged. ***

  N5 -- the decisive computation. At SL(5) the Dehn-twist eps-series resolves 21 of 24 Dickson factors, and
      the resolved 21 are UNIVERSALLY catalog-consistent (the same two-sequence catalog across seeds AND
      across monodromies, both det signs) -- strong evidence on the RESOLVED sector. The 3 unresolved factors
      are supported as Sym^2 by the STRUCTURAL routes (B62 theta-split, B89-T two-seq, B103), NOT by the
      seed-variation. [CORRECTION A]: the seed-variation of the 3 unresolved factors is the EXPECTED signature
      of the eps-series rank-deficiency (B84: dx is rank-deficient there, so DX.pinv(dx) returns
      approach/seed-dependent values regardless of the true factorization) -- it is UNINFORMATIVE about the
      truth at the unresolved sector (Appendix A demonstrates this: the contested eigenvalue's seed-spread is
      identical whether the true value is the catalog value or a wildly different deviation). So a structural
      deviation at the unresolved sector is NEITHER RULED IN NOR RULED OUT by this computation. The strict
      "all 3 factors" bar is NOT met; the explicit n=5 catalog is OPEN.

  H6 -- the forced cusp spectrum (structural OBSERVATION; B95). {1,i,-i} (n=3), {1,1,w,w^2} (n=4),
      {1,1,1,-1,-1} (n=5): the NON-TRIVIAL eigenvalues are DISTINCT at n=3,4 but COLLIDE at n=5 (-1 with
      multiplicity 2); n>=6 has no finite-order spectrum (B95). [CORRECTION B]: this collision is a CANDIDATE
      common root cause across the tower / degree=rank / eps-series walls -- recorded as a structural
      observation, NOT a proof that it causes them, and NOT a "natural boundary." There is NO mathematical
      boundary: B103's factor-through-N makes char(J(n)) = the catalog a CLASS FUNCTION FOR ALL n (the tower
      does not stop at n=4). What walls at n=4/5 is the explicit COMPUTATION -- the eps-series (pinv
      non-convergence, B84) and the engine-free trace-ring (non-closure) -- a methodological ceiling, not a
      theorem.

  CONVERGENCE -- the project's thesis (endorsed). Every positive result is a property of ONE object: rho_n,
      the GL(2,Z)-representation on the SL(n) trace ring at the trivial point. The tower IS char(rho_n); the
      module-iso IS its decomposition into Sym pieces; universality IS the well-definedness of rho_n; the
      Hitchin identification places rho_n in a known moduli space. rho_n is fully characterized at n=3,4
      (exact, constructive, universal); the explicit n>=5 catalog is OPEN (walled from two methods). THE OPEN
      FRONTIER: prove char(rho_n) = the Dickson catalog DIRECTLY from rho_n (B103) + B62's multiplicities --
      around the sigma-construction, never building it. That would close n>=5 by PROOF and settle Correction
      A's open question. This stage SETS UP the thesis; it does NOT attempt that proof.

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


def n5_unresolved_factor_varies_with_seed(seeds=(20, 21, 22)):
    """The 3 unresolved factors VARY across seeds while the resolved 21 are invariant. [CORRECTION A, V90]:
    this is the EXPECTED signature of the eps-series rank-deficiency (B84) and is UNINFORMATIVE about the true
    factorization at the unresolved sector -- it does NOT imply 'coordinate artifact, not structural change'
    (Appendix A / B105 FINDINGS). The genuine evidence is the resolved-21 universal catalog-consistency.
    Returns (n_distinct_unresolved, all_resolve_21)."""
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
    """The forced cusp spectra n=3,4,5 (structural OBSERVATION). n>=6 has no finite-order spectrum (B95).
    [V91]: a CANDIDATE common context, NOT 'one collision' -- see three_obstacle_distinction()."""
    return {n: cusp_spectrum_facts(n) for n in (3, 4, 5)}


def _opposition_split_A4_height2():
    """The A_4 height-2 root space split under the opposition involution theta=-w0 (the diagram flip
    alpha_i<->alpha_{5-i}); returns (+1, -1) eigenspace dims over the POSITIVE roots."""
    flip = {1: 4, 2: 3, 3: 2, 4: 1}
    ht2 = [(1, 2), (2, 3), (3, 4)]                       # height-2 positive roots of A_4
    theta = lambda r: tuple(sorted(flip[i] for i in r))
    fixed = sum(1 for r in ht2 if theta(r) == r)
    pairs = {frozenset((r, theta(r))) for r in ht2 if theta(r) != r}
    return fixed + len(pairs), len(pairs)               # (+1, -1) = sum-of-pair + diff-of-pair


def three_obstacle_distinction():
    """[V91] n=5 is a THRESHOLD where THREE distinct obstacles degenerate -- not one collision. Returns the
    verified table distinguishing them by eigenvalue / derivation / onset."""
    # (i) degree=rank (B95): 2cos(theta)=3-n -> at n=5 eig -1 (A^2=I)
    n5_dr = 3 - 5
    degree_rank_eig = -1.0 if abs(n5_dr + 2) < 1e-12 else None
    # (ii) tower/eps-series (B62): char(M^2)=t^2-3t+1, golden roots phi^2,1/phi^2
    phi2 = (3 + 5 ** 0.5) / 2
    char_m2_roots = sorted(np.roots([1, -3, 1]))         # [1/phi^2, phi^2]
    plus, minus = _opposition_split_A4_height2()
    return {
        "degree_rank": {"source": "B95", "eigenvalue": degree_rank_eig, "is_root_of_unity": True,
                        "onset_n": 5, "mechanism": "A^2=I degenerates tAt^-1=A^2B"},
        "tower_eps_series": {"source": "B62", "eigenvalue_pair": [round(char_m2_roots[1], 4), round(char_m2_roots[0], 4)],
                             "is_golden": bool(abs(char_m2_roots[1] - phi2) < 1e-9), "onset_n": 5,
                             "A4_height2_theta_split_pos": [plus, minus],   # (2,1) over positive roots -> (4,2) over +/-
                             "mechanism": "opposition involution; char(M^2)^2; no reference to A's spectrum"},
        "trace_ring_nonclosure": {"source": "engine-free", "eigenvalue": None, "onset_n": 4,
                                  "mechanism": "n^2-1 coords don't generate the SL(n) trace ring (algebraic)"},
        "distinct_eigenvalues": bool(degree_rank_eig is not None and abs(degree_rank_eig - phi2) > 1),
        "verdict": "THREE distinct obstacles at the n=5 threshold (different eigenvalues, independent "
                   "derivations, different onset) -- NOT one collision.",
    }


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
    "H6": ("STRUCTURAL-OBSERVATION", "B62/B84/B95/B105", "n=5 is a THRESHOLD where THREE DISTINCT obstacles "
           "degenerate -- NOT one collision [V91]: degree=rank (B95, eigenvalue -1, A^2=I, onset n=5); the "
           "tower/eps-series doubling (B62, golden char(M^2)^2, A_4 height-2 theta-split, onset n=5); and "
           "trace-ring non-closure (engine-free, algebraic, onset n=4). Different eigenvalues, independent "
           "derivations, different onset."),
}
# Explicit downgrades of two B105 inferences (V90 audit; banked, not silently edited):
CORRECTIONS_V90 = {
    "A": "DOWNGRADE: 'seed-variation of the 3 unresolved factors => coordinate artifact, NOT a structural "
         "change' is INVALID. A rank-deficient DX.pinv(dx) (B84) returns approach/seed-dependent values at "
         "the unresolvable sector REGARDLESS of the true factorization (Appendix A: the contested "
         "eigenvalue's seed-spread is identical for the catalog value vs a wild deviation). Seed-variation is "
         "UNINFORMATIVE about the truth there. Corrected: the resolved 21 are universally catalog-consistent "
         "(real evidence); the 3 unresolved are supported as Sym^2 by STRUCTURAL routes (B62/B89-T/B103), not "
         "by seed-variation; a structural deviation there is NEITHER ruled in NOR ruled out.",
    "B": "DOWNGRADE: 'natural boundary at n=4, proved structural / mathematically complete at n=4' OVERSTATES. "
         "B103's factor-through-N makes char(J(n)) = the catalog a CLASS FUNCTION FOR ALL n -- there is NO "
         "mathematical boundary. What walls is the explicit COMPUTATION (eps-series pinv non-convergence; "
         "engine-free trace-ring non-closure) -- a methodological ceiling, not a theorem. Corrected: explicit "
         "catalog is a computed theorem THROUGH n=4; structure holds ALL n; explicit n>=5 catalog is OPEN, "
         "walled from two methods; the cusp collision is a candidate root cause, not a proof.",
}
# Further downgrade (V91): B105's "one collision is the common root cause" overreaches -- it is THREE
# distinct obstacles that degenerate at the n=5 THRESHOLD, not one.
CORRECTIONS_V91 = {
    "three-obstacles": "DOWNGRADE of 'one collision (the repeated -1) is the common root cause'. n=5 is a "
        "structural THRESHOLD where several distinct A_{n-1} features degenerate together -- but NOT a single "
        "collision. (i) DEGREE=RANK (B95): A's forced principal spectrum 2cos(theta)=3-n reaches -1 at n=5 "
        "(A^2=I), a ROOT OF UNITY, degenerating the figure-eight relation tAt^-1=A^2 B. (ii) TOWER/EPS-SERIES "
        "(B62): the height-2 root space of A_4 splits (4,2) under the opposition involution theta=-w0, giving "
        "char(M^2)^2 with eigenvalue char(M^2)={phi^2,1/phi^2} (GOLDEN), pure root-system combinatorics with "
        "NO reference to A's spectrum. (iii) TRACE-RING NON-CLOSURE (engine-free): the n^2-1 coords do not "
        "generate the SL(n) trace ring, purely algebraic, onset n=4, no eigenvalue degeneracy. DIFFERENT "
        "eigenvalues (-1 vs phi^2), INDEPENDENT derivations (B95 vs B62), DIFFERENT onset (n=5 vs n=4). "
        "Verified: 2cos=3-n gives -1 only at n=5; char(M^2)=t^2-3t+1 has golden roots; the A_4 height-2 "
        "theta=-w0 split is (4,2). So 'one collision' is a narrative over distinct mechanisms -- WITHDRAWN.",
    "rho_n-target": "SHARPENED open frontier (A4). Prove char(rho_n)=the Dickson catalog by showing the rho_n "
        "decomposition reproduces the OPPOSITION-INVOLUTION multiplicities (theta=-w0 eigenspace dims on each "
        "height-h A_{n-1} root space), directly from the GL(2,Z)-rep, WITHOUT building sigma. The contested "
        "n=5 piece is ONLY B62's height-2 char(M^2)^2 (which B62 already supplies structurally); the "
        "degree=rank -1 (B95) and the trace-ring non-closure are SEPARATE problems the catalog proof need NOT "
        "touch. That bound is the useful output: a referee-defensible target, not 'resolve the n=5 wall'.",
    "n4-scope-hedge": "HEDGE (A5). 'Explicit catalog through n=4 for all monodromies' rests at n=4 on the "
        "B104 eps-series (clean at n=4 -- B80-validated, not gauge-corrupted -- but not independently "
        "reproduced by the verification chat). Hedged statement: n=3 genuine-non-metallic both det signs "
        "VERIFIED (the 23-monodromy sweep); n=4 metallic PROVED (B80), non-metallic via the B104 eps-series.",
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
    print(f"  resolved factors at SL(5) (gcd with two-seq catalog): {n5_resolved_degree()}/24"
          " (universally catalog-consistent -- the genuine evidence)")
    ndist, all21 = n5_unresolved_factor_varies_with_seed()
    print(f"  3 unresolved factors across seeds: {ndist} distinct; all resolve 21: {all21}")
    print("  [CORRECTION A] seed-variation is the eps-series RANK-DEFICIENCY signature (B84), UNINFORMATIVE")
    print("    about the truth there; a structural deviation is NEITHER ruled in NOR out. The 3 are supported")
    print("    as Sym^2 by STRUCTURAL routes (B62/B89-T/B103). The strict 'all 3' bar is NOT met -> n=5 OPEN.")
    print("\nH6 -- the forced cusp spectra (structural OBSERVATION; B95):")
    for n, f in unified_wall_table().items():
        sp_str = {3: "{1,i,-i}", 4: "{1,1,w,w^2}", 5: "{1,1,1,-1,-1}"}[n]
        print(f"  n={n}: {sp_str:14} tr=trinv=det=1 {f['tr1'] and f['trinv1'] and f['det1']}; "
              f"non-trivial collision = {f['nontrivial_collision']}"
              + ("  <-- candidate root cause" if f["nontrivial_collision"] else ""))
    print("  [CORRECTION B] no MATHEMATICAL boundary: char(J(n))=catalog is a class function ALL n (B103);")
    print("    n=4 is a methodological CEILING (eps-series + trace-ring non-closure), not a proved boundary.")
    print("\n[V91] n=5 is a THRESHOLD of THREE DISTINCT obstacles -- NOT one collision:")
    o = three_obstacle_distinction()
    print(f"  (i)  degree=rank (B95): eigenvalue {o['degree_rank']['eigenvalue']} (root of unity, A^2=I), onset n=5")
    print(f"  (ii) tower/eps-series (B62): char(M^2)^2 golden {o['tower_eps_series']['eigenvalue_pair']}, "
          f"A_4 height-2 theta-split {o['tower_eps_series']['A4_height2_theta_split_pos']}(+,-) over pos roots, onset n=5")
    print(f"  (iii)trace-ring non-closure (engine-free, algebraic), onset n=4")
    print(f"  distinct eigenvalues (-1 vs phi^2): {o['distinct_eigenvalues']} => {o['verdict']}")
    print("\nCONVERGENCE: the project converges on ONE object rho_n (the GL(2,Z)-rep on the SL(n) trace ring).")
    print("  Fully characterized n=3,4; explicit n>=5 OPEN. SHARPENED OPEN FRONTIER [V91]: prove char(rho_n)=")
    print("  catalog by reproducing the opposition-involution multiplicities (theta=-w0 eigenspace dims on")
    print("  each height-h A_{n-1} root space) directly from rho_n; the contested n=5 piece is ONLY B62's")
    print("  char(M^2)^2 -- the degree=rank -1 and trace-ring non-closure are separate, untouched problems.")
    print(f"\nObs {list(OBSERVATIONS)}; C {list(CORRECTIONS)}; V90 {list(CORRECTIONS_V90)}; V91 {list(CORRECTIONS_V91)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
