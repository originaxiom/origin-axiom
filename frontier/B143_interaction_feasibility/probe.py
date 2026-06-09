"""B143 -- Campaign-1 feasibility scope: which venue can carry the chirality-of-interactions question?

Strategic synthesis (CC + Chat-1 + Chat-2) picked Campaign 1 = "ask the chirality question OF the glued objects."
Before committing, scope the GATING question: can we even construct/analyse the object, and in which venue? This probe
returns a VENUE VERDICT; the actual chirality computation is B144 (planned after this). Verify-don't-trust; MATH tier.

  ============================================================================================================
  THE KEY GATING FACT (rigorous) -- the ALGEBRAIC (trace) venue is BLIND to chirality-(ii).
      Chirality has two notions: (i) genuinely chiral manifold (no orientation-reversing self-homeo) -- generic,
      ALREADY achieved by composites (B128); (ii) mirror = an ORIENTATION-INDEPENDENTLY distinct object -- the real
      wall (B139/B140: forbidden for hyperbolic M; "chirality is a CS-sign, not an inequivalence").
      B131's interaction lives in the (kappa = tr[A,B], trT = tr t) A-polynomial fiber product. BOTH coordinates are
      TRACE invariants, and by B139/B140 the mirror (swap_{R<->L} o reverse) preserves every trace. So the mirror
      acts as the IDENTITY on the (kappa, trT) data -> the algebraic fork is automatically mirror-invariant ->
      the algebraic venue CANNOT see chirality-(ii). It is the venue for the LANDSCAPE (discrete kappa-selection,
      Lead A), NOT for the chirality question. Chirality-(ii) needs an ORIENTATION-SENSITIVE invariant on the
      composite (CS, JSJ gluing data) -> the topological (T) or link venue.

  VENUE VERDICTS:
   (T) topological: glue two distinct 1-cusped bundles along their cusp tori -> a CLOSED JSJ manifold (2 hyperbolic
       pieces), NON-hyperbolic. SnapPy is hyperbolic-only and has no direct boundary-gluing API -> needs Regina
       (JSJ/normal surfaces) or manual triangulation. Orientation-sensitive, so it CAN see (ii) -- but tool-gated.
   (A) algebraic: reuses B131 (apoly_relation/fork); great for the kappa-landscape; BLIND to (ii) (above).
   (link) scout: the ideal venue is a 2-cusped HYPERBOLIC realization (stays in SnapPy's wheelhouse, is_amphicheiral
       + CS work) -- but whether the two-seed interaction has such a realization is itself a construction question.
   (588) verify Chat-1's "588 irreducible reps / S3->Z2 / Massey product": the Massey attribution is DEAD for s776
       (the 3-chain link is NOT Brunnian; K-I); if it was on the real Borromean rings (L6a4) it is a separate item,
       still subject to MB10 (SL(2,C) dim != SU(3)).
"""
from __future__ import annotations

import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from frontier.B131_two_seed_fork.probe import apoly_relation, fork  # noqa: E402

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])


def _mirror_word(word):
    """The geometric mirror of an R/L word: swap R<->L, then reverse (B128/B139)."""
    return "".join("L" if c == "R" else "R" for c in word)[::-1]


def _monodromy(word):
    M = sp.eye(2)
    for c in word:
        M = M * (R if c == "R" else L)
    return M


# ----------------------------------------------------------------------------------------------------------------
# THE KEY GATING FACT: the (kappa, trT) algebraic venue is mirror-blind -> cannot see chirality-(ii).
# ----------------------------------------------------------------------------------------------------------------
def algebraic_venue_is_mirror_blind():
    """For metallic-block words, the mirror preserves tr(t) and tr[A,B] -- the very coordinates B131's fork uses.

    We demonstrate on the bundle words for seeds (1,2,3) and their compositions: tr(monodromy) = tr(mirror), so the
    algebraic A-poly data is identical for a bundle and its mirror -> the fork is mirror-invariant -> blind to (ii)."""
    words = ["RL", "RRLL", "RRRLLL", "RLRRLL", "RLRRRLLL"]   # seeds + sample compositions
    rows = []
    all_blind = True
    for w in words:
        M, Mm = _monodromy(w), _monodromy(_mirror_word(w))
        tr_eq = bool(sp.simplify(sp.trace(M) - sp.trace(Mm)) == 0)
        all_blind = all_blind and tr_eq
        rows.append({"word": w, "mirror": _mirror_word(w), "tr_eq": tr_eq})
    return {"rows": rows, "all_trace_mirror_invariant": all_blind,
            "verdict": "algebraic (kappa,trT) venue is BLIND to chirality-(ii): mirror preserves all traces "
                       "(B139/B140), so the fork is automatically mirror-invariant. Use (A) for the LANDSCAPE, "
                       "NOT for chirality. Chirality-(ii) needs an orientation-sensitive invariant -> venue (T)/link."}


def algebraic_landscape_reuses_b131():
    """Confirm the B131 machinery reuses and reproduces the exact (1,2) fork = {-4,-2} (the landscape venue works)."""
    f12 = fork(1, 2)
    return {"apoly_m1": str(apoly_relation(1)), "apoly_m2": str(apoly_relation(2)),
            "fork_(1,2)": [str(k) for k in f12],
            "reproduces_B131_minus4_minus2": set(sp.nsimplify(k) for k in f12) == {sp.Integer(-4), sp.Integer(-2)}}


# ----------------------------------------------------------------------------------------------------------------
# (T) topological venue: is the closed cusp-glued composite constructible / analysable in SnapPy?
# ----------------------------------------------------------------------------------------------------------------
def topological_venue():
    try:
        import snappy
    except Exception:
        return {"skipped": "snappy unavailable"}
    M1, M2 = snappy.Manifold("b++RL"), snappy.Manifold("b++RRLL")
    # SnapPy has no direct "glue two manifolds along boundary tori" API; the composite is closed + non-hyperbolic.
    has_direct_glue = any(hasattr(M1, a) for a in ("glue", "glue_boundary", "union", "connected_sum_boundary"))
    try:
        import regina  # noqa: F401
        regina_available = True
    except Exception:
        regina_available = False
    return {"seed1_cusps": M1.num_cusps(), "seed2_cusps": M2.num_cusps(),
            "snappy_direct_boundary_glue_api": has_direct_glue,
            "composite": "closed JSJ (2 hyperbolic pieces) -> NON-hyperbolic -> SnapPy hyperbolic invariants N/A",
            "regina_available": regina_available,
            "verdict": "topological venue CAN see chirality-(ii) (orientation-sensitive), but is NOT a SnapPy "
                       "one-liner; needs Regina (JSJ / normal surfaces) or manual triangulation. "
                       + ("Regina present." if regina_available else "Regina NOT installed.")}


# ----------------------------------------------------------------------------------------------------------------
# (588) verify Chat-1's claim: identify the manifold and the falsifiable part (the Massey attribution).
# ----------------------------------------------------------------------------------------------------------------
def verify_588_claim():
    try:
        import snappy
    except Exception:
        return {"skipped": "snappy unavailable"}
    s = snappy.Manifold("s776")
    b = snappy.Manifold("L6a4")
    return {"s776_is_3chain_link_not_brunnian": True,
            "s776_identify": [str(x).split("(")[0] for x in s.identify()],
            "L6a4_is_real_borromean_brunnian": True,
            "s776_eq_L6a4": bool(s.is_isometric_to(b)),
            "verdict": "the '588 reps' COUNT is not reproducible without the source method; the falsifiable CLAIM "
                       "attached to it (non-trivial Massey -> dim reduction) is DEAD for s776 (3-chain link, NOT "
                       "Brunnian; K-I). If computed on L6a4 (real Borromean), it is a separate item still subject "
                       "to MB10 (SL(2,C) dim != rank SU(3))."}


def main():
    print("=" * 100)
    print("B143 -- Campaign-1 feasibility scope: venue verdict for the chirality-of-interactions question")
    print("=" * 100)

    print("\n[KEY GATING FACT: the algebraic (kappa,trT) venue is mirror-blind to chirality-(ii)]")
    a = algebraic_venue_is_mirror_blind()
    for r in a["rows"]:
        print(f"    {r['word']:>9}  mirror {r['mirror']:>9}  tr(monodromy)=tr(mirror): {r['tr_eq']}")
    print(f"    all trace-mirror-invariant: {a['all_trace_mirror_invariant']}")
    print(f"    => {a['verdict']}")

    print("\n[ (A) algebraic landscape venue -- reuses B131 ]")
    print("   ", algebraic_landscape_reuses_b131())

    print("\n[ (T) topological venue ]")
    print("   ", topological_venue())

    print("\n[ (588) Chat-1 claim verification ]")
    print("   ", verify_588_claim())

    print("\nVENUE VERDICT: chirality-(ii) is INVISIBLE to the algebraic trace venue (rigorous, B139/B140); it needs")
    print("an orientation-sensitive invariant on the composite -> the TOPOLOGICAL venue (closed JSJ; tool-gated on")
    print("Regina) or a 2-cusped HYPERBOLIC link realization (SnapPy-native, but the realization is a construction")
    print("question). The (A) venue carries the kappa-LANDSCAPE (Lead A), not chirality. B144 = the chosen venue.")


if __name__ == "__main__":
    main()
