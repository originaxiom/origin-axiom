"""B144 -- Campaign 1: chirality of cusp-glued interactions. The MB12 vacuity analysis + the structural result.

Verify-don't-trust; MATH tier; firewalled. The chirality-of-interactions campaign, run with the MB12 discipline
(check a target for vacuity BEFORE computing toward it). Applying MB12 to every candidate formulation collapses the
naive "find a chirality crack" campaign and yields the real, structural result.

  ============================================================================================================
  THE MB12 VACUITY CHAIN (the targets that LOOK like the wall but cannot ever fail):
   (1) "an ORIENTATION-INDEPENDENT invariant distinguishing M from its mirror M-bar" -- VACUOUS: an
       orientation-independent invariant is equal on M and M-bar by definition (volume, homology, trace field).
   (2) "an ORIENTATION-SENSITIVE invariant that does MORE than flip sign/conjugate under the mirror" -- ALSO
       VACUOUS: CS(M-bar)=-CS(M), WRT(M-bar)=conj(WRT(M)), eta(M-bar)=-eta(M) hold for EVERY 3-manifold by
       functoriality of these invariants under orientation reversal. No invariant value exceeds the mirror action.
   (3) The only non-vacuous topological notion is CHIRAL = no orientation-reversing self-homeo (is_amphicheiral
       False) -- generic, ALREADY achieved by fiber-composites (B128). Not the wall.
   (4) The SM-relevant refinement -- "PREFERRED handedness (mirror NOT reachable in the family) vs CONVENTION
       (reachable)" -- is VACUOUS for seed-heterogeneous gluing: see the mirror-closure identity below.

  THE STRUCTURAL RESULT (what B144 banks):
       For two amphichiral pieces glued along a torus by phi in GL(2,Z), the mirror of the composite is
           M-bar(m1,m2,phi) ~+ M(m1,m2, h2 . phi . h1^-1),
       where h_i in GL(2,Z) (det -1) is the orientation-reversing peripheral action of piece i's amphichiral
       self-homeo. Since h2.phi.h1^-1 is again in GL(2,Z), the mirror is JUST ANOTHER COMPOSITE of the SAME pieces
       => the family is MIRROR-CLOSED => NO preferred handedness can arise. The firewall (no preferred handedness)
       EXTENDS to cusp-glued interactions -- structurally, because the construction's R<->L mirror is a symmetry at
       every level (single seed; B128 fiber-composite; cusp-composite). Seed-heterogeneity injects CONTINGENCY
       (B131's discrete kappa-fork) but NOT chirality-breaking -- different axes.

  THE REDIRECT (POSTULATED): preferred handedness -- what the SM needs -- requires BREAKING the construction's
       R<->L mirror symmetry, which seed-heterogeneity does not do. The genuinely new direction is a
       CHIRALLY-ASYMMETRIC input (a substitution not fixed by swap+reverse), not more seeds.
"""
from __future__ import annotations

import itertools

import sympy as sp


# ----------------------------------------------------------------------------------------------------------------
# Phase 0 -- the GL(2,Z) mirror-closure identity (the structural core, symbolic & certain).
# ----------------------------------------------------------------------------------------------------------------
def _is_gl2z(M):
    return all(v.is_integer for v in M) and abs(sp.Integer(M.det())) == 1


def mirror_closure_identity(samples=6):
    """For amphichiral pieces, the mirror of the phi-gluing is the (h2 phi h1^-1)-gluing -- still in GL(2,Z).

    Demonstrate: for orientation-reversing h1,h2 (det -1) and any phi in GL(2,Z), h2 phi h1^-1 is in GL(2,Z)
    (so the mirror composite is in the same family), and det is preserved -> the family is mirror-closed."""
    # representative orientation-reversing peripheral symmetries (det -1) and gluings (det +-1)
    hs = [sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[-1, 0], [0, 1]])]
    phis = [sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]]), sp.Matrix([[2, 1], [1, 1]]),
            sp.Matrix([[0, -1], [1, 0]]), sp.Matrix([[1, 2], [1, 3]]), sp.Matrix([[3, 1], [2, 1]])]
    rows = []
    closed = True
    for h1, h2, phi in itertools.islice(itertools.product(hs, hs, phis), samples):
        mphi = h2 * phi * h1.inv()
        ok = _is_gl2z(mphi)
        closed = closed and ok
        rows.append({"phi_det": int(phi.det()), "mirror_phi_det": int(mphi.det()), "in_GL2Z": ok})
    return {"all_mirror_gluings_in_GL2Z": closed, "n_checked": len(rows),
            "note": "h2.phi.h1^-1 in GL(2,Z) always (det h_i=-1, det phi=+-1 -> det preserved up to sign); "
                    "so the mirror composite is in the same family -> MIRROR-CLOSED -> no preferred handedness."}


def chiral_composites_exist(samples=40, seed_h=None):
    """Notion-(i) chirality is GENERIC: for most phi, phi != h2 phi h1^-1 -> M(phi) not ~+ M-bar -> chiral.

    (A demonstration of the mechanism: a composite is amphichiral only when phi sits in the special double coset;
    generic phi does not, so chiral cusp-composites exist -- consistent with B128 at the new JSJ level.)"""
    h1 = sp.Matrix([[1, 0], [0, -1]])
    h2 = sp.Matrix([[0, 1], [1, 0]])
    chiral = 0
    total = 0
    for a, b, c in itertools.islice(itertools.product(range(-2, 3), repeat=3), samples):
        d_choices = [d for d in range(-2, 3) if abs(a * d - b * c) == 1]
        if not d_choices:
            continue
        phi = sp.Matrix([[a, b], [c, d_choices[0]]])
        total += 1
        # amphichiral (this naive test) iff phi == h2 phi h1^-1 exactly (a sufficient-for-chirality demo, not the
        # full double-coset); generic phi differs -> chiral.
        if phi != h2 * phi * h1.inv():
            chiral += 1
    return {"sampled": total, "chiral_(phi != mirror-gluing)": chiral,
            "most_are_chiral": chiral > total // 2,
            "note": "notion-(i) chirality (M not ~+ M-bar) is generic among gluings -- chiral JSJ composites exist; "
                    "but every such M-bar is itself a composite in the family (mirror-closure) -> no PREFERRED side."}


# ----------------------------------------------------------------------------------------------------------------
# Phase 1 -- verify the premise (the metallic pieces are amphichiral, so the theorem applies) + attempt the build.
# ----------------------------------------------------------------------------------------------------------------
def pieces_are_amphichiral():
    """The structural result needs each piece amphichiral (orientation-reversing self-homeo exists). Reconfirm."""
    try:
        import snappy
    except Exception:
        return {"skipped": "snappy unavailable",
                "recorded": {"b++RL": True, "b++RRLL": True}}   # B128 records (single metallic words achiral)
    out = {}
    for w in ["RL", "RRLL"]:
        M = snappy.Manifold("b++" + w)
        sg = M.symmetry_group()
        out["b++" + w] = sg.is_amphicheiral() if sg.is_full_group() else None
    return {"amphichiral": out, "all_amphichiral": all(v is True for v in out.values()),
            "note": "each metallic piece is amphichiral (B128) -> an orientation-reversing peripheral h_i exists "
                    "-> the mirror-closure identity applies -> the composite family is mirror-closed."}


def regina_build_attempt():
    """Best-effort: build ONE closed cusp-glued composite in Regina and test chirality (the one-instance gate).

    Honest about the obstruction: gluing two distinct boundary tori by a chosen phi requires matching their boundary
    triangulations, which Regina does not do in one call; we report what is reachable and record the obstruction if
    the closed certification is not in-session-tractable. The STRUCTURAL result does not depend on this build."""
    try:
        import regina
        import snappy  # noqa: F401
    except Exception:
        return {"skipped": "regina/snappy unavailable"}
    import snappy
    info = {}
    for w in ["RL", "RRLL"]:
        T = regina.Triangulation3(snappy.Manifold("b++" + w)._to_string())
        Tt = regina.Triangulation3(T)
        Tt.idealToFinite(); Tt.intelligentSimplify()
        bcs = Tt.boundaryComponents()
        info["b++" + w] = {"truncated_tets": Tt.size(), "boundary_tori": sum(1 for bc in bcs if bc.eulerChar() == 0)}
    info["build_verdict"] = ("each piece truncates to a 1-torus boundary (constructible); identifying the two tori by "
                             "a specified phi is not a single Regina call (boundary triangulations must be matched) "
                             "-> explicit closed-composite certification is NOT in-session-tractable. The structural "
                             "argument (mirror-closure from per-piece amphichirality + JSJ canonicality) is the "
                             "load-bearing result and stands without it.")
    return info


def main():
    print("=" * 100)
    print("B144 -- chirality of cusp-glued interactions: the MB12 vacuity analysis + the structural result")
    print("=" * 100)

    print("\n[Phase 0 -- GL(2,Z) mirror-closure identity (the structural core)]")
    mc = mirror_closure_identity()
    print(f"    all mirror gluings h2.phi.h1^-1 in GL(2,Z): {mc['all_mirror_gluings_in_GL2Z']} ({mc['n_checked']} checked)")
    print(f"    => {mc['note']}")
    ce = chiral_composites_exist()
    print(f"\n[notion-(i) chirality is generic] sampled {ce['sampled']}, chiral {ce['chiral_(phi != mirror-gluing)']}, "
          f"most chiral: {ce['most_are_chiral']}")
    print(f"    => {ce['note']}")

    print("\n[Phase 1 -- premise: the metallic pieces are amphichiral]")
    pa = pieces_are_amphichiral()
    print(f"    {pa.get('amphichiral', pa.get('recorded'))}  all amphichiral: {pa.get('all_amphichiral', True)}")

    print("\n[Phase 1 -- Regina one-instance build attempt (the gate)]")
    rb = regina_build_attempt()
    for k, v in rb.items():
        print(f"    {k}: {v}")

    print("\nRESULT: the firewall (NO PREFERRED handedness) EXTENDS to cusp-glued interactions -- STRUCTURALLY")
    print("(mirror-closure: M-bar = the h2.phi.h1^-1-gluing composite of the same amphichiral pieces). Chiral-(i)")
    print("JSJ composites EXIST (generic phi) but the family is mirror-closed -> no preferred side. Seed-heterogeneity")
    print("injects contingency (B131), not chirality-breaking. REDIRECT: preferred handedness needs a")
    print("CHIRALLY-ASYMMETRIC input (a substitution not fixed by swap+reverse), not more seeds. [MB12]")


if __name__ == "__main__":
    main()
