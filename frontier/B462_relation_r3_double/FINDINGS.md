# B462 — Relation R3: the double — the φ-scan, the chirality payload, and the κ-diagonal

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (committed before
computation, PR #611). Engine gate: my (Z, S, T) conventions reproduce B441's banked
τ_r(4₁(5,1)) bit-for-bit at r = 5, 7, 9, 11 BEFORE any φ-scan value was read. Verdict:
every exact structure found LAUNDERS through a named generic mechanism or is derived
arithmetic of the banked curve; the quantum-vs-classical landscape table is NEW-MATH-grade
exact data; no H1.**

## Machinery

- Z-vector: Z_n(K) = qd(n)·J_n(K) (B441's weighting); ρ_r(φ) by word in the standard
  SU(2)_r S/T matrices; sesquilinear pairing H(φ) = ⟨Z(M̄), ρ(φ)Z(N)⟩ = the mirror-double,
  bilinear B(φ) = Zᵀρ(φ)Z = the same-orientation double.
- 5₂'s colored Jones: **Masbaum's cyclotomic expansion** for twist knots K_p (lit-gate:
  Masbaum AGT 2003; formula transcribed in-session from Fuji–Gukov–Sułkowski
  arXiv:1209.1409 eq. 2.4 + Table 2: p=−1 → 4₁, p=2 → 5₂). Root-of-unity trap handled by
  computing SYMBOLICALLY in ℤ[q^{±1}] first (Habiro integrality asserted per coefficient),
  specializing second. **Three gates passed**: G1 p=−1 ≡ B441's validated `cj_fig8` (all
  colors, r = 5, 7, 9); G2 J₂(K₂) = Jones(5₂) (this convention = the Knot-Atlas mirror,
  noted); G3 p=1 ≡ the trefoil single-sum.

## The φ-scan (4₁ double): two exact structures, both FORCED — adjudicated before reading

| structure | value | mechanism (verified exactly) |
|---|---|---|
| T² pairing | **0 at every odd r** (≤1e-27) | Kirby–Melvin symmetry J_{r−n} = J_n (any 0-framed knot) + tw(r−n)² = −tw(n)² at odd r ⇒ pairwise cancellation. **Class-generic — LAUNDERS.** Verified to hold for 5₂ too (KM dev ≤ 1e-18). |
| ST = TS | exact equality | bilinear: transpose invariance of a scalar (ANY knot). Sesquilinear for 4₁: the Z-vector is REAL — which is amphichirality. **The realness is the object datum; the equality is forced given it.** |
| id pairing | ‖Z‖² > 0 | the prereg's engine gate; zero-information as a verdict (F3), reported as gate only. |

The quantum table against B174's classical fork sizes (CONTINUUM/9/10/16/32/32): the
quantum pairing does NOT see the classical fork's size — T² has a 10-point classical fork
but an identically-zero quantum pairing (symmetry-forced), while the identity (classical
continuum) has the largest quantum value (‖Z‖²). **The two landscapes measure different
things: fork size counts glued vacua; the pairing is one number per φ weighted by quantum
dimensions. No correspondence — and the absence is itself forced, not a discovery.**

## The chirality payload (5₂ ∪ 5̄₂ vs 5₂ ∪ 5₂) — the live cell

4₁'s version is equal-by-theorem (Z real ⇒ H ≡ B — verified ≤ 3.6e-28 over all words and
levels, the prereg's CUT). For chiral 5₂ both live observables fire (r = 9 shown; full
tables in `payload.py`):

- **mirror-double ≠ same-double**: |H| − |B| = +33.17 (id), −13.86 (S), +33.76 (STS) —
  the chirality of the piece survives into every gluing of the double, in both magnitude
  and phase.
- **the sesquilinear ST-vs-TS split**: |H(ST)| = 43.93 vs |H(TS)| = 27.02, while the
  bilinear stays forced-equal (B(ST) = B(TS) = 35.78, transpose-forced) — the split lives
  ONLY in the conjugation, i.e. exactly where chirality can live and nowhere else.
- KM symmetry holds for 5₂ (dev ≤ 5.6e-28) ⇒ the TT-zero is forced for the chiral knot
  too — the T² cell stays empty for the same class-generic reason.

**The mixed control (4₁ ∪_φ 5₂): H = B to machine zero at every word and level — FORCED,
not a finding**: the left vector Z(4₁) is real (amphichirality), so the conjugation acts
trivially regardless of the right factor. The control confirms the mechanism assignment:
the H/B gap is carried by the conjugated factor's chirality alone.

## R3b — the κ-diagonal (the fork CONTENTS B174 never extracted)

Per-φ exact κ-value sets of the fig-8 self-glue (gate: per-φ degree totals reproduce
B174's banked fork sizes 9/10/16/32/32 — ALL PASS):

| φ | κ-set structure (fig-8, m=1) |
|---|---|
| T | (κ+2)² · a degree-7 field (disc −7215127) |
| T² | (κ+2)⁴ · **the cyclic cubic of conductor 7** (x³−2x²−x+1, disc 49 = ℚ(ζ₇)⁺)² |
| S | (κ+2) · the same conductor-7 cubic · a degree-12 field |
| ST | (κ+2)² · a degree-30 field |
| TS | (κ+2)² · a different degree-30 field |
| STS | (κ+2)⁶ · (κ−2)⁶ · **ℚ(√5)** (x²−2x−4, roots 1±√5)² · a quartic (disc 229) |

**Adjudication (silver m=2 control, identical machinery, predictions fixed before the
run):**
- **The parabolic law — κ = −2 appears in EVERY fork, both objects**: tr[A,B] = −2 is the
  defining cusp equation of every once-punctured-torus bundle (the complete/parabolic
  locus survives every gluing). **Class-generic — LAUNDERS.** (It is also the banked
  Markov/heartbeat surface, B448 — the heartbeat locus is exactly the part of the glued
  variety every relation keeps.)
- **The fields do NOT transfer**: silver gets ℚ(√21), a disc −59 cubic, two sextics — no
  ℚ(√5), no conductor-7 cubic. So the fig-8's ζ₇⁺-cubic (shared by T² and S) and its
  ℚ(√5) at STS are the object's OWN arithmetic — but they are DERIVED data: the κ-sets
  are roots of explicitly-constructed resultants of the banked B67 curve under the word
  action (the closed form F(word, f) exists and predicted the silver table by the same
  construction). Under burden-inversion: **derivable — no H1.** The Inversion-Law reading
  (K020): the object forces its arithmetic; the glue re-expresses it.
- Note: 7 appears at m=1 (disc 49; also the banked chirality field ℚ(√−7) is conductor 7)
  and 21 = 3·7 at m=2's swap — recorded as an observation on the derived tables, nothing
  claimed.

## Verdict

R3a′: the φ-scan's exact structures are forced (KM symmetry; transpose; amphichirality);
the quantum/classical landscape non-correspondence is itself explained. R3b: the κ-diagonal
is exact NEW-MATH-grade content for the B174 landscape (the values, not just the counts),
with the parabolic law laundering the only cross-object regularity. The chirality payload
gives 5₂'s H/B gap + sesquilinear ST/TS split as the live chiral observables, with the
mechanism localized (the conjugated slot) by the mixed control's forced equality. **No
H1. The relational register again shows: what transfers across objects is the class's
(parabolic law, KM symmetry, transpose); what doesn't transfer is derivable from the
object's banked curve (the κ-fields) or is the piece's own chirality re-expressed (the
5₂ splits).**

## Reproduce
```
python3 phi_scan.py        # engine gate + the 4_1 phi-scan
python3 masbaum.py         # the three Masbaum gates
python3 payload.py         # 5_2 doubles + mixed control + F-c check
python3 kappa_diagonal.py  # R3b exact kappa-sets, B174 size gates
pytest ../../tests/test_b462.py
```
