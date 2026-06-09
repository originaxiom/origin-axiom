"""B139 -- "SM through multiplicity": firewall CARTOGRAPHY (verify-don't-trust the load-bearing calc).

This stage banks THREE Chat-2 informatory calculations as cartography of the firewall -- NOT a result, NOT a
physics crossing. They CONFIRM the firewall: they map *why* it holds. The only load-bearing computation that needs
re-running before banking is Item 1's mirror trace-equality; this probe does that (plus the SnapPy CS-flip control).

  ============================================================================================================
  ITEM 1 -- THE CHIRALITY ARTICULATION (SM-side view of P009's det=-1 -> CS=0). VERIFIED HERE.
  ============================================================================================================
  For any once-punctured-torus-bundle word in R,L, the mirror (swap_{R<->L} o reverse) is a RELABELING that
  preserves the trace, hence the characteristic polynomial, hence the Perron field, hence the real hyperbolic
  geometry (volume) -- ONLY the Chern-Simons sign flips. So a bundle and its mirror are the SAME geometry with
  opposite CS: a symmetric pair. The SM's defining feature -- chirality WITHOUT a mirror partner (parity violation:
  the mirror is a DIFFERENT theory) -- is structurally absent, because the mirror DISTRIBUTES over the word.

  WHY THE TRACE EQUALITY IS TRIVIAL (the clean reason). With R = [[1,1],[0,1]] and L = [[1,0],[1,1]] = R^T, the
  swap R<->L is transposition (X_R^T = L, X_L^T = R), and reversal + transposition of a product is the transpose of
  the product:  M_mirror = (X_{c1} X_{c2} ... X_{cn})^T = M_word^T.  Therefore tr(M_mirror) = tr(M_word^T) =
  tr(M_word), EXACTLY, for every word. This is precisely why chirality is invisible at the trace level -- the
  SM-side face of det=-1 -> CS=0.

  THE LOAD-BEARING CAVEAT (rides with the banking): "structurally blocked" = blocked at every invariant computed
  (trace, char poly, Perron field, volume, CS). It is NOT a proof that NO invariant distinguishes a chiral bundle
  from its mirror. Banked claim: "chirality is a CS-SIGN, not an inequivalence, across all STANDARD invariants."

  ITEM 2 -- METHOD GUARD MB9 (group-level != gauge-level). A non-abelian symmetry GROUP is not non-abelian GAUGE
  content; the firewall is on the trace-ring / T[M] / fixed-locus (abelian x discrete), not the monodromy group
  (non-abelian for any hyperbolic object). Banked in REPRODUCIBILITY.md (text guard, nothing to compute here).

  ITEM 3 -- OPEN LEAD: does the chirality block survive the GENUS LADDER? (genus-1 special; MATH, trace-level
  first pass; the falsifier for Item 1). Registered in docs/OPEN_LEADS.md as an open lead; unrun.

MATH tier; cartography, not a result, not a crossing. Nothing to CLAIMS.md; P1-P16, B85, S031, merged B124-B138
untouched. The only physics that continues is the emergent K010 / kappa=2 / Lee-Yang, firewalled.
"""
from __future__ import annotations

import sympy as sp

# The chiral words from the handoff (single-block, non-palindromic R/L words). The trace equality holds for ALL
# words, achiral or chiral -- these are the named controls for which CS != 0.
CHIRAL_WORDS = ["RRL", "RRRL", "RRLRL", "RRRLL", "RRLLRL", "RRRLRL"]

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])  # L = R^T


def monodromy(word):
    """SL(2,Z) monodromy of an R/L word (left-to-right product)."""
    M = sp.eye(2)
    for ch in word:
        M = M * (R if ch == "R" else L)
    return M


def mirror_word(word):
    """The geometric mirror: swap R<->L, then reverse. (swap_{R<->L} o reverse)"""
    swapped = "".join("L" if ch == "R" else "R" for ch in word)
    return swapped[::-1]


def mirror_trace_equality(words=CHIRAL_WORDS):
    """ITEM 1, the load-bearing check: tr(M_word) == tr(M_mirror), with M_mirror = M_word^T, for every word.

    Returns the per-word trace pair + the Perron-field discriminant (tr^2 - 4) equality (same field), and the
    structural identity M_mirror == M_word^T (the trivial reason)."""
    rows = []
    all_eq = True
    all_transpose = True
    for w in words:
        M = monodromy(w)
        Mm = monodromy(mirror_word(w))
        t, tm = sp.trace(M), sp.trace(Mm)
        disc, discm = t * t - 4, tm * tm - 4            # Perron field = Q(sqrt(tr^2 - 4))
        eq = bool(sp.simplify(t - tm) == 0)
        is_T = bool(sp.simplify(Mm - M.T) == sp.zeros(2, 2))
        all_eq = all_eq and eq and bool(sp.simplify(disc - discm) == 0)
        all_transpose = all_transpose and is_T
        rows.append({"word": w, "mirror": mirror_word(w), "tr": int(t), "tr_mirror": int(tm),
                     "perron_disc": int(disc), "trace_equal": eq, "mirror_is_transpose": is_T})
    return {"rows": rows, "all_traces_equal": all_eq, "all_mirror_is_transpose": all_transpose,
            "reason": "M_mirror = M_word^T  =>  tr(M_mirror) = tr(M_word) exactly; chirality is invisible at trace level."}


def cs_flip_live(words=CHIRAL_WORDS):
    """SnapPy control (skips cleanly if absent): volume (Re of complex_volume) mirror-invariant, CS (Im) flips sign.

    Also probes ONE invariant outside the trace/CS/vol family -- H1 homology -- which (being orientation-blind) is
    also mirror-invariant: a small strengthening of the caveat (the standard invariants all symmetrize)."""
    try:
        import snappy
    except Exception:
        return None
    rows = []
    ok = True
    for w in words:
        M = snappy.Manifold("b++" + w)
        Mm = snappy.Manifold("b++" + mirror_word(w))
        cvM, cvMm = M.complex_volume(), Mm.complex_volume()
        vol_eq = abs(float(cvM.real()) - float(cvMm.real())) < 1e-9
        cs_flip = abs(float(cvM.imag()) + float(cvMm.imag())) < 1e-9
        h_eq = str(M.homology()) == str(Mm.homology())
        ok = ok and vol_eq and cs_flip and h_eq
        rows.append({"word": w, "vol_invariant": vol_eq, "cs_flips_sign": cs_flip,
                     "cs": round(float(cvM.imag()), 6), "homology_invariant": h_eq})
    return {"rows": rows, "all_vol_invariant_cs_flips_homology_invariant": ok}


def main():
    print("=" * 100)
    print("B139 -- firewall cartography: Item 1 (chirality articulation) load-bearing verification")
    print("=" * 100)
    r = mirror_trace_equality()
    print("\n[Item 1 -- mirror trace-equality  (M_mirror = M_word^T  =>  tr equal, same Perron field)]")
    for row in r["rows"]:
        print(f"    {row['word']:>7}  mirror {row['mirror']:>7}  tr={row['tr']:>3} = tr_mirror={row['tr_mirror']:<3}"
              f"  disc(tr^2-4)={row['perron_disc']:>4}  mirror==M^T: {row['mirror_is_transpose']}")
    print(f"\n  all traces equal: {r['all_traces_equal']}   all mirror==M^T: {r['all_mirror_is_transpose']}")
    print(f"  reason: {r['reason']}")

    print("\n[SnapPy control -- vol invariant, CS flips sign, H1 invariant]")
    cs = cs_flip_live()
    if cs is None:
        print("    SnapPy absent -- the trace-level proof above stands unconditionally (B128 recorded the live CS).")
    else:
        for row in cs["rows"]:
            print(f"    {row['word']:>7}  vol_inv={row['vol_invariant']}  CS_flip={row['cs_flips_sign']}"
                  f"  CS={row['cs']:>+9}  H1_inv={row['homology_invariant']}")
        print(f"    all (vol inv & CS flip & H1 inv): {cs['all_vol_invariant_cs_flips_homology_invariant']}")

    print("\nITEM 1 caveat (load-bearing): 'structurally blocked' = blocked at ALL STANDARD invariants (trace, char")
    print("poly, Perron field, volume, CS), NOT a proof no invariant distinguishes. Chirality is a CS-SIGN, not an")
    print("inequivalence. Item 2 = MB9 (group != gauge); Item 3 = the open genus-ladder probe (falsifier for Item 1).")


if __name__ == "__main__":
    main()
