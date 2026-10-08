#!/usr/bin/env python3
"""B1606 -- GENESIS v1.27 (main's, B1604) -> v1.28 (main's): THREE ON THE WEAVE, GRADED -- the SM seat's W19-W24 and main's
verifications recorded at FK14 and FK11 with the grade: derived on the weave (the flavour three with its hand), readings,
the unearned dictionary, the negatives; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.28 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_27_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_27 = "a31b0eefff8ea40c24638ceb1c80b5465877011d8ae65a9fae5c15b7781f9449"

GRADE = ("**[v1.28] THREE ON THE WEAVE, GRADED (main, B1606; the SM seat's W19–W24, rows 932–940, with main's verifications of W20, W21, W22 at S85–S86).** "
         "The weave's own object (W19): its group is Aut⁺(F₂), the pure mapping class group of the twice-marked torus; its space M₁,₂, a complex surface with χ = 1/12 ≠ 0, the three parities its orbifold locus — the even-dimensional object the v1.27 condition asks for. On it (W20, verified by the amalgam ℤ/4 ∗ ℤ/6): −χ(Aut⁺(F₂); 27) = 3 through E₆'s principal sl₂ and every distinguished orbit, a sum of Riemann–Roch indices of powers of the records' Hodge line — an index of a non-flat bundle equal to three, and NOT chiral (the module is self-dual). The hand (W21, verified by the cup product on the ℤ/2-orbifold presentation): the parity-twisted spin space splits by Hodge type with one line per parity in each type; the Hodge–Riemann form is invariant under L, R and the sign, reversed by the swap, positive definite on the triplet T with χ(L) at 7/8 of a turn and negative on T̄ — the three holomorphic zero modes span T, one per parity. The puncture (W22 as qualified, verified): the six local solutions carry 2O with −1 acting as −1 and split 2 ⊕ 4, so every condition the moves keep has index −3, −1, +1 or +3 — odd, never zero — and with the parity grading only ±3. **The grade under THE_BAR.** DERIVED on the weave: three, alike, chiral under the weave's own group, one per parity — the number forced by the records' parities, the hand forced at the puncture; this is the flavour structure of three generations (the matter assignment of the modular S₄ flavour models, 3′ times a metaplectic character, as the seat notes). READINGS: that the triplet is the generations (FK14); that holomorphic zero modes on the fibre are the left-handed matter (FK11's compactification dictionary). UNEARNED: which fields carry the bundle 𝕎 ≅ ρ_Q ⊗ ℂ³ — W24's D4 proves the chiral gauge reading needs a Lagrangian half of the multiplicity space that no move-invariant, real, F₄ × SU(2)-invariant condition supplies, so the frame (E₆, SO(10), SU(5)) is a choice; gauge chirality itself. NEGATIVES: no index on a thread or a cover (v1.27); the E₈ frames on the fibre give at most two complete generations (W23); no six-dimensional object the weave forces gives three by the heterotic dictionary (W24: the character variety is forced and has no count; E³/G has a count and is not forced, 48, 16, 14). **The owner's question, 'did we derive three generations?': no — the flavour three is derived, the gauge three is a selection.** What would finish it: a forced complex structure on the gauge side — a bundle whose holonomy has complex representations — or the puncture's localized content (GAP2's place), neither yet forced. ")

CHANGES = [
 ("**Version 1.27 · 2026-10-08 · canonical.**", "**Version 1.28 · 2026-10-08 · canonical.**"),
 ("the ±LR pattern stays arithmeticity's, unexplained. **[v1.26] WM3, THE FORCED COVER ON EVERY THREAD",
  "the ±LR pattern stays arithmeticity's, unexplained. " + GRADE + "**[v1.26] WM3, THE FORCED COVER ON EVERY THREAD"),
 ("- **v1.27 · 2026-10-08 · main B1604.** The class index is not an index.\n",
  "- **v1.28 · 2026-10-08 · main B1606.** Three on the weave, graded.\n"
  "  - FK14/FK11: the SM seat's W19–W24 recorded with main's verifications (W20 the count three, not chiral; W21 the holomorphic triplet T; W22 the puncture index odd, ±3 with the grading) and the grade: the flavour three — alike, chiral under the weave's group, one per parity — is DERIVED on the weave; the gauge three is a selection (the dictionary unearned, W24's D4; W23; W24). The owner's question answered: no.\n"
  "- **v1.27 · 2026-10-08 · main B1604.** The class index is not an index.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_27, "the received v1.27 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.28 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.28, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
