#!/usr/bin/env python3
"""B1640 -- GENESIS v1.41 (main's, B1634) -> v1.42 (main's): the frame audit of 2026-10-13. Two statements that took a frame or
a convention for forced are scoped: the degeneracy at omega that grounded v1.35's retirement of tau = omega, and 'no choice
is made' in v1.41's multiplier; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.42 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_41_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_41 = "6ce527af24f06be696b804cf3d9ded81c1993121d77defad0ce45a6467414125"

OMEGA = (" **[v1.42] Audited (B1640, the frame audit): \"degenerate at i and ω\" holds at ω for the single symmetric and "
         "antisymmetric pieces of T ⊗ T only.** Under T̄ ⊗ T (B1618's Dirac tensor) the masses at ω are distinct in B1635's "
         "own sealed read-outs (nine members, e.g. 1 : 0.674 : 0.448), and so are T ⊗ T couplings that mix the symmetric and "
         "antisymmetric pieces (B1640, live members at weights 3 and 5). B1618's 'degenerate for every weight' used the inner "
         "automorphisms, which are not moves here. So on the ruled branch v1.35's retirement of τ = ω stands as \"no hierarchy "
         "found\", not as a degeneracy; the near-fixed-point regime is not computed. The TM1 reading (P10) needs residuals of RL's "
         "and RRL's type; on the ruled branch the theta multiplier of RL shares its eigenlines only with order-3 stabilisers "
         "(ω-type points) and that of RRL only with order-2 ones (i-type points), so one τ cannot give both.")
HAND = (" **[v1.42] The hand (B1640): \"no choice is made\" is scoped.** ρ(γ) = lift(γ)⁻¹ is one of two homomorphisms the "
        "reverse-composing lifts give; the transpose is the other, and for these unitary lifts it is the complex conjugate. Which "
        "of V's two pieces is T is a second binary choice. Together they decide between the theta constants' multiplier and its "
        "conjugate. The record's choice allows weight 3/2 (W45's index) and the symmetric weight-1 coupling (B1636's golden "
        "coupling); the conjugate allows neither (at weight 1 its only coupling is antisymmetric). So the index and the golden "
        "coupling come with the same hand. Which hand the matter carries is not derived; a derivation from the zero modes' period "
        "map is owed.")
GM5D = (" **[v1.42] Scoped (B1640, after the archive's independent audit): positivity excludes −I from the physical updates, a "
        "semigroup; it does not exclude it from the group the modular forms use.** On homology (R L⁻¹ R)² = −I, and on the ruled "
        "branch Δ⁴ acts on T as −1 (B1634). So \"excludes the sign\" says which counts are reached; the symmetry and lift group "
        "⟨L, R⟩ ≅ B₃, from which the multiplier and the couplings are built, contains −I on homology. Results built on the group "
        "and results built on positivity concern different objects, and each says which it uses.")
CHANGES = [
 ("ich every spin structure carries a hand (B1479, B1481) — are exactly what positivity removes. |",
  "ich every spin structure carries a hand (B1479, B1481) — are exactly what positivity removes." + GM5D + " |"),
 ("**Version 1.41 · 2026-10-09 · canonical.**", "**Version 1.42 · 2026-10-13 · canonical.**"),
 ("the canonical functionals pick ω or the cusp; registered).",
  "the canonical functionals pick ω or the cusp; registered)." + OMEGA),
 ("W47's territory. | an end condition derived from physics (sL-8) |",
  "W47's territory." + HAND + " | an end condition derived from physics (sL-8) |"),
 ("- **v1.41 · 2026-10-09 · main B1634.**",
  "- **v1.42 · 2026-10-13 · main B1640.** The frame audit: the degeneracy at ω, the multiplier's hand and positivity's reach scoped.\n"
  "  - At ω only the single pieces of T ⊗ T are degenerate; T̄ ⊗ T and mixed T ⊗ T are not (B1635's own read-outs). τ = ω stays retired as \"no hierarchy found\". One τ cannot give the TM1 residual pair.\n"
  "  - ρ = lift⁻¹ against its conjugate is two binary conventions; the record's allows the index's weight 3/2 and the golden coupling, the conjugate neither; the hand is not derived.\n"
  "  - GM5d: positivity excludes −I from the updates (a semigroup), not from the group ⟨L, R⟩ the multiplier uses, which contains it on homology.\n"
  "- **v1.41 · 2026-10-09 · main B1634.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_41, "the received v1.41 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.42 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.42, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
