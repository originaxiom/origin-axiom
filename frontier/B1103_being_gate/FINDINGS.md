# B1103 — THE BEING GATE: the ζ₃ phase reads exactly the abelianization; κ lives where it cannot see

**Status: banked (frontier). Verdict PROVED. Harvest arc (integrate-don't-merge): the
theorem and its first proof are an OUTSIDE SESSION's (the owner relayed the result and
its self-sufficient package for verification); rebanked here under a new number after
the banking seat's independent two-engine verification. Gate 5 untouched (no measured
value anywhere; the instrument is the banked B593/B238 machinery). Lock
`tests/test_b1103_being_gate.py` (fast core + `OA_SLOW=1` full sweep).**

## THE THEOREM (the outside session's statement, verified verbatim)

Let w be a word in the free group on {a, A, b, B} (A = a⁻¹, B = b⁻¹) acting through
the SU(3)₂ modular representation (a ↦ R = T, b ↦ L = S⁻¹T⁻¹S — the banked B238
instrument), and let h(w) be B593's θ-odd coupling (the u₃ quadratic form, twisted
sign). Write p = #a − #A, q = #b − #B (the abelianization). Then h **factorizes**:

> **h(w) = ζ₃^(p−q) × (an element of ℚ(ζ₅))** — the BEING end a pure phase, the
> HEARING end the whole magnitude — and consequently
> **h(w) ∈ ℚ(ζ₅) ⟺ p − q ≡ 0 (mod 3), or h(w) = 0.**

The h = 0 clause is real, not cosmetic: exactly **28 of the 1364** words to length 5
sit on the vanishing locus (and the original proof's first pass missed them — the
outside session found and disclosed its own gap before shipping).

**Proof shape** (theirs; clean): the θ-odd plane carries χ ⊗ V₂(2I) (B1011's banked
factorization); σ₁₁ generates Gal(ℚ(ζ₃₀)/ℚ(ζ₅)), fixing ζ₅ and conjugating ζ₃; the
odd-compression determinants give χ(a) = ζ₃, χ(b) = ζ₃⁻¹ exactly; χ is a
homomorphism, so inverses count negatively and the exponent is the abelianized p − q.
The ⟹ direction of the gate follows from ζ₃ ∉ ℚ(ζ₅) (field disjointness).

## Structural consequences (all verified exact)

- **The being phase reads exactly the abelianization; the commutator subgroup is the
  kernel.** χ ≡ 1 on every commutator (μ₃ is abelian — one line), so the ENTIRE
  commutator subgroup lies in the ℚ(ζ₅) locus: **252/252** census commutators exact,
  every real part exactly one of the nine banked Niven letters.
- **κ = tr[a,b] is capital-resident.** The framework's founding quantity is a
  commutator — literally unwritable in the positive monoid {R, L} — and the being
  face is structurally blind to it while the hearing face sees it (h varies across
  the commutator subgroup; h(abAB) = h(ab) = 1/(2φ) + i·sin(2π/5)/√5 exactly, the
  banked B593 hearing coupling, because the being factor is 1 on both).
- **The complementarity is image-vs-kernel of one map** — a sharper statement of the
  two-face architecture than "each possesses what the other lacks": being reads the
  abelian quotient; κ is the non-abelian residue; they partition the word's
  information by construction.
- **Adjacency, typed precisely (not conflated):** B1083 located the ARROW in the
  positive monoid's non-surjectivity (structure T, the capital-free half); this arc
  proves the being phase cannot see the capital-generated (commutator) content. Two
  different precise statements that rhyme; neither implies the other.

## Verification (verify-don't-trust, two independent engines + the vendored certificate)

1. **The banking seat's own ζ₆₀ engine** (`b1103_exact_engine.py`): integer-coefficient
   arithmetic mod Φ₆₀, the instrument REBUILT from B238's own Kac–Peterson formulas
   (exact S certified: unitarity symbolic, ν² = 75, entrywise 1e−15 vs banked
   numerics), Galois membership via σ₁₁/σ₃₁ fixed-point test. Result: factorization
   AND gate **1364/1364, zero failures**; all quoted values certified exact
   (h(ab) = the banked coupling; h(abAB) = h(ab); h(aabAAB) = −1/2 − iφ·sin(2π/5)/√5;
   h(aB) ∉ ℚ(ζ₅)); census 252/252.
2. **The float engine** (`b1103_float_engine.py`): independent numeric pass; also
   pinned the sign convention (the twisted form is identically −1 × the untwisted on
   the C-odd u₃ — a proven identity, so the convention is global and harmless).
3. **The outside session's own certificate** (`check_being_gate_vendored.py`, sha256
   in its header): inspected for conditional exit paths (its author's own error
   ledger includes a hardcoded-pass catch — the inspection was mandatory), run fresh:
   **1364/1364, h = 0 in 28 — the same 28 the independent engine counts** — and
   negative-controlled (modulus 3 → 2 DRIFTs at 484/1364 exactly as shipped).

## Flags carried honestly

- **"Eight of nine letters appear" is census-definition-dependent and UNREPRODUCED**:
  the natural 252-word census hits 4 letters in one sign convention; the outside
  session's 196-element census was not fully specified. Banked as
  OBSERVED-UNREPRODUCED; the theorem does not depend on it.
- The instrument scope is one listener (u₃), one root, length ≤ 5 exhaustive (the
  proof itself is length-free; the certificate is the bounded part).

## Named follow-ups (the outside session's ranked queue, carried; none claimed)

(i) **The h = 0 locus** — the vanishing count was channel-independent in every channel
tested; if the locus is a word-property independent of listener, that is a fourth
theorem in this family, one run away. (ii) **Other listeners in the odd plane** —
is the gate a property of the sector or of u₃? (iii) **F₄(ℤ) on orthogonal PAIRS of
rank-1 idempotents** — the outside session's integral-Jordan machinery pointed at
Route A's pair space (B1094: "the pair is the object"). Registered in OPEN_LEADS at
this bank.
