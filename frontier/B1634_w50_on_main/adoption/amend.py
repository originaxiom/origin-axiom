#!/usr/bin/env python3
"""B1634 -- GENESIS v1.40 (main's, B1632) -> v1.41 (main's): v1.40's qualification resolved -- the weave's own lifts on T are a
genuine representation of Mp2(Z), exactly the multiplier of eta^21 (theta_2^2, theta_3^2, theta_4^2); B1632's "projective" was
an instrument's sign (lift_of takes the first of +-g); chi_{3/2} = 0 by the formula and by an independent algebraic count --
and the SM seat's W50 verified: on the ruled branch the inner automorphisms by a and by b are not moves, so the statements
that use them as symmetries (v1.34's order-48 residual, v1.36's permutation mixing, B1630's line at i) are scoped to the
frames where they act; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.41 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_40_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_40 = "0b723329ff6386fef1d9d4be8a27c40d49227fa9d8fcad95febe2158bdd7923c"

ADD_UNIT = (" **[v1.41] Resolved (B1634, main):** the qualification above came from an instrument, not from the weave. The "
            "helper that lifts an automorphism takes the first of ±g, and for S̃ = R L⁻¹ R it took the sign opposite to the product of "
            "the move matrices. The move matrices themselves satisfy the braid relation exactly, and Δ⁴ acts on T as −1, so they "
            "are a genuine representation of B₃/⟨Δ⁸⟩ = Mp2(ℤ). With S = H₁(S̃) and T = H₁(L) (the lifts compose in reverse, so "
            "ρ(γ) = lift(γ)⁻¹), the relations hold with no rescaling, and the representation is exactly the multiplier of "
            "η²¹·(θ₂², θ₃², θ₄²) (a monomial intertwiner; θ₃² on the clock's line) — W41's multiplier, T's exponents (⅛, ⅜, ⅞). "
            "Its dual is not allowed at weight 3/2. χ_{3/2} = 0 by the formula and by an independent count (the modular forms of "
            "Γ(4) as polynomials in θ₂², θ₃², θ₄² modulo Jacobi's quadric, which agrees with the formula at every weight from −½ "
            "to 27/2). So the payoff is again \"given Λ and the unit\": W45's core is verified on main. The five-to-one split "
            "of v1.40 is the six flat twists by η's character (χ_{3/2} = 1 at one of them), W47's territory.")
ADD_SCOPE = (" **[v1.41] Scoped (B1634, the SM seat's W50 verified on main):** the inner automorphisms by a and by b are not "
             "moves of the ruled weave. ⟨L, R⟩ ≅ B₃ meets Inn(F₂) only in ⟨Δ⁴⟩ = ⟨conj(a b⁻¹ a⁻¹ b)⟩ (to length 12: 1,944 "
             "relators, 196 words for conj(c) and 196 for its inverse, none for conj(a) or conj(b)); they enter only with the sign "
             "(GM5b) or the swap (GM5c), both ruled out (v1.33). So the statements that take them as symmetries at every τ — "
             "v1.34's order-48 residual at ω, the permutation mixing above (T-TAU-ONLY-PERMUTATION) and B1630's single line at "
             "i — hold where they act: on the sign or swap branches, or if the records' base point is given moves of its own "
             "(point-pushing on M₁,₂), a move §2 does not name and the owner's to add. On the ruled branch the residual on T "
             "is four scalars at a generic τ, cyclic of order 8 at i (a plane containing the clock's line and a line in the "
             "two letter lines' span) and cyclic of order 12 at ω (three lines, each meeting every parity line with weight "
             "⅓). So there the modulus τ is the state that breaks the weave's group: couplings in τ alone are "
             "vector-valued modular forms for the theta constants' multiplier, and the flavour numbers are their values at τ "
             "— the SM seat's W50 finds them non-permutation at a generic τ and degenerate at i and ω (registered, not yet "
             "recomputed on main). τ = ω stays retired as a working postulate (v1.35) and the choice of τ stays open "
             "(the seat's W51: the weave's joint determinant Π|θ_p/η|² = 4 is flat; the canonical functionals pick ω or the "
             "cusp; registered).")
CHANGES = [
 ("**Version 1.40 · 2026-10-09 · canonical.**", "**Version 1.41 · 2026-10-09 · canonical.**"),
 ("until it is, the payoff is \"given Λ, the unit and W41\".",
  "until it is, the payoff is \"given Λ, the unit and W41\"." + ADD_UNIT),
 ("With couplings in τ alone every residual contains the inner automorphisms and every mixing matrix is a permutation, so the observed mixing needs a vacuum that breaks the parity grading.",
  "With couplings in τ alone every residual contains the inner automorphisms and every mixing matrix is a permutation, so the observed mixing needs a vacuum that breaks the parity grading." + ADD_SCOPE),
 ("- **v1.40 · 2026-10-09 · main B1632.**",
  "- **v1.41 · 2026-10-09 · main B1634.** v1.40's qualification resolved; the inner automorphisms scoped off the ruled branch.\n"
  "  - The weave's lifts are a genuine Mp2(ℤ) representation, exactly the theta constants' multiplier; B1632's \"projective\" was an instrument's sign; χ_{3/2} = 0 twice. The ±3 is \"given Λ and the unit\".\n"
  "  - The SM seat's W50 verified: ⟨L, R⟩ ∩ Inn(F₂) = ⟨Δ⁴⟩; the order-48 residual, the permutation mixing and B1630's line hold where the inner automorphisms act; on the ruled branch τ breaks the weave's group.\n"
  "- **v1.40 · 2026-10-09 · main B1632.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_40, "the received v1.40 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.41 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.41, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
