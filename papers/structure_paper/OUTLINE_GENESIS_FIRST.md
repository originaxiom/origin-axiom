# OUTLINE — GENESIS-FIRST (the full chain paper)

**Status: DRAFT OUTLINE. Publication owner-gated. Gate 5 stands throughout.**
Companion to `SKELETON.md` (the algebra half, 35 KB, unchanged and reused) and
`ABSTRACT_DRAFT.md` (titles, MSC, abstract). **Mathematics only; no physics
identification in the body.** Internal names are names of mathematical objects,
glossed at first use and in Appendix C.

*Owner decision 2026-08-14: **one paper, genesis-first.** This outline extends
`SKELETON.md` backwards through the genesis and forwards through the negatives; the
skeleton's §§2–11 compress into this outline's §§6–8.*

---

## 0. What the paper claims

**A cost theorem, not a discovery.** From a minimal-description principle, with **three
declared choices whose alternatives are computed**, and with **no measured quantity
entering any computation**, one reaches a specific hyperbolic 3-manifold; its own
arithmetic then forces the exceptional Jordan structure, and a cascade of centralizers
lands on `su(3)⊕su(2)⊕u(1)³` with the `ℤ₆` global form. **The paper states exactly what
follows and exactly what does not** — including five sealed predictions that failed and a
theorem that the object is blind to scale.

**The one-sentence version.** *Three priced choices buy a knot; from that knot to E₆, the
27, and the gauge algebra, every step is a theorem.*

---

## 1. Section plan

| § | title | content | source |
|---|---|---|---|
| **1** | Introduction | the cost claim; what is and is not asserted; the reader's map | new |
| **2** | The principle and its price | minimal description; **C3/C4/C5 with their forks EXHIBITED** — C5's Gieseking sibling named in the body, not a footnote | B749 |
| **3** | From minimal description to a knot | C1 Morse–Hedlund ⟹ Sturmian; C2 self-selection ⟹ φ; geometrize; orient; C6 Thurston/Riley ⟹ m004 | new |
| **4** | The object's own arithmetic | C7 forced V₄ of faces; C8 interface-only census; C9 congruence; C10 character-rigidity; C11–C15 the two-column law, chord, mixing, hearing | new |
| **5** | ## **THE DOORWAY** ⚠ **REWRITTEN** | the hearing group **`2I × ℤ/3`** at level 15 (order **360**, the tone census's own count); **the level-15 form is IRREDUCIBLE** — being(3) and hearing(5) *interfere*, 59/60 primes falsify L-factorization; then **e₆ is *handed over*** (Part III's own verb). **E₆/E₈ arrive at the two CURVATURE ENDS** of the cone-angle deformation — hyperbolic `ℚ(√−3)/2T/E₆`, spherical `ℚ(√5)/2I/E₈` (B981/B248). **Plus the forcedness census (39/43).** **The genericity caveat then the door's uniqueness, in that order.** | new; **see §4 gap D1** |
| **6** | The frame | Chevalley `𝔢₆`; the four 2T-charges; the charge cubic μ | SKELETON §2 |
| **7** | The cascade | FMT (Thm A) · magic square (Thm B) · SMT (Thm C) — compressed, citing banked detail | SKELETON §§3–5 |
| **8** | The real form and the 27 | e₆(2) selection (Thm D) · atoms · signature split · D₂ (Thm E) | SKELETON §§6–8, 10 |
| **9** | ## **What the chain does NOT yield** | **five sealed crossings, five misses**; the value-contact surface **enumerated and exhausted**; **scale-blindness by theorem** (`∂S/∂k = −CS ≡ 0` ≡ amphichirality); the open ratios; Gate 5 | new |
| **10** | Falsifiers | the named kill-shots; reopening conditions; what would end the programme | Part IX |
| **A** | Methodology | seals, priced axioms, non-weakening, the floors discipline | SKELETON App. A |
| **B** | ## **Verification** | one runnable check per numerical claim; `verify_all.py` | SKELETON App. B + new |
| **C** | Glossary | **one referent per term** — the vocabulary discipline | SKELETON App. C + `TERMINOLOGY.md` |

**§5 is the paper's spine.** **§9 is its credibility** and must not be cut.

---

## 2. Citation registry — the genesis half (extends `SKELETON.md` §3's 35 rows)

| # | claim | arc | lock |
|---|---|---|---|
| G1 | Morse–Hedlund: aperiodic ⟹ `p(n) ≥ n+1`; Sturmian achieves equality | B749/F7 | `tests/test_b749_genesis_forks.py` |
| G2 | Self-selection: Hurwitz extremality at φ = the all-1s continued fraction | B749 | ## **GAP — see §3** |
| G3 | C3 priced: periodic sibling degenerates (F2); shadow variants degenerate/conjugate away (F4) | B749/F2,F4 | `tests/test_b749_genesis_forks.py`, `tests/test_b749_f2_f8_locks.py` |
| G4 | C4 priced: non-geometric carriers see only the hearing; **ℚ(√−3) bought at geometrization** | B749/F8 | `tests/test_b749_f2_f8_locks.py` |
| G5 | C5 priced: the discarded det −1 sibling **is** the Gieseking manifold | B749/F5 | `tests/test_b749_genesis_forks.py` |
| G6 | Mapping torus of the once-punctured torus under `[[2,1],[1,1]]` **is** m004; trace field ℚ(√−3) | B285, B282 | `tests/test_b285_commutator_phase.py` |
| G7 | The intrinsic arithmetic forces exactly three quadratic faces = one `V₄` | B730 | `tests/test_b730_faces_cosmos.py` |
| G8 | The `V₄` is a property of the **open** object (census) | B288/B740/B747/B748 | `tests/test_b747_b748_sweeps.py` |
| G9 | m004 **is** congruence | B734 | `tests/test_b734_m004_congruence.py` |
| G10 | Character-rigidity: the continuous spectrum is ONE channel | B739, B737 | `tests/test_b737_candidate_zero.py`, `tests/test_b739_rigidity.py` |
| G11 | The two-column law (10 of 12 floors carry a forced golden appearance) | B746, B749/F6 | ## **GAP — lock unnamed in ledger** |
| G12 | The chord: trace map θ-equivariant; odd golden powers | B48/B54/B64 | ## **GAP — "the B64/B48-family locks", not a resolvable path** |
| G13 | The mixing structure: θ-odd block unitary, unistochastic, golden-exact | B753 | `tests/test_b753_mixing.py` |
| G14 | The pure-3 symmetrized series | B755 cell 3 | ## **GAP — lock unnamed** |
| G15 | The hearing multiplication law | B756/DOOR3 | `tests/test_b756_doors.py` |
| G16 | The threefold refusal (NO-GO) | B750 | `tests/test_b750_lack_ledger.py` |
| G17 | The SM record (NO-GO), four mechanisms | B754, B736, B751/B752, B757 | `tests/test_b736_abc.py` |
| **D1a** | the hearing group is `2I × ℤ/3` at level 15, order 360; deaf subgroup Q₈; five absolute tones | chain Part II | ## **GAP — arc not identified** |
| **D1b** | ## **the level-15 form is IRREDUCIBLE** (being ∩ hearing INTERFERE; 59/60 primes falsify L-factorization) | `LAW_MAP` — THE LEVEL-15 HANDSHAKE | ## **GAP — arc not identified** |
| **D1c** | E₆/E₈ at the two **curvature ends**: hyperbolic `ℚ(√−3)/2T/E₆`, spherical `ℚ(√5)/2I/E₈`; CS pair 0 vs π²/5 | **B981 / B248** (via `THE_LAMBDA_POSITION`) | ## **GAP — locks not identified; cc3 read at one level of indirection** |
| **D2** | ## **The forcedness census: 39 of 43 links forced; axioms at C3,C4,C5,C18; C6→C17 axiom-free** | `docs/THEOREM_LEDGER.md` | ## `scripts/checks/forcedness_census.py` |

## 3. Citation registry — the negatives (§9)

| # | claim | arc | lock |
|---|---|---|---|
| N1 | Crossing 1 — NEGATIVE | B915 | `tests/test_b915_crossing.py` |
| N2 | Crossing 2 — NEGATIVE (Outcome B verbatim) | B925 | per arc |
| N3 | Crossing 3 — HIT-SHAPE; **Tier 2 MISS**, the direct identification dead | B929 | per arc |
| N4 | Crossing 4 — ALL-MISS, powered both sectors | B1027 | per arc |
| N5 | The refresh — **all four variants, both targets, eight misses**; NuFIT 6.1 + JUNO companion | B1063, B1066 | per arc |
| N6 | ## **The value-contact surface ENUMERATED and EXHAUSTED** — exactly two target-shaped relations existed; both fired; both missed | B1066 | per arc |
| N7 | ## **Scale-blindness by theorem**: `S = −CS·k − Vol·σ`, `∂S/∂k = −CS ≡ 0`; k-blindness **is** amphichirality | B811, B1012 | per arc |
| N8 | Gravity route **obstructed at the torus**: amphichirality deletes the quantized boundary sector | B1064 | per arc |

## 4. Gaps to close before drafting (named, not hidden)

1. ## **G2 — the self-selection lock.** The ledger's own correction (B998, 2026-08-09): *"that file tests F4, F5, F6, F7 only. **There is NO F3 test.**"* C2 is a **THEOREM in the chain with no executable lock.** **Highest-priority gap** — it is the link where φ enters.
2. **G11, G12, G14** — locks cited as families or unnamed; need resolvable `tests/...py` paths.
3. ## ⚠ **D1 — the doorway. cc3's FIRST VERSION OF THIS ROW WAS FALSE AND WAS BANKED** (`27d9ceb9` §2.1, withdrawn in `1a0b5a90`). cc3 wrote *"15 = 3·5 ⟹ CRT ⟹ 2T × 2I ⟹ McKay ⟹ E₆ × E₈"* — but the hearing group is **`2I × ℤ/3` (order 360)**, not `2T × 2I` (2880); and `LAW_MAP` banks the level-15 form as **IRREDUCIBLE**, the opposite of a factorization. **The real mechanism is the curvature ends (D1c).** ## **The paper's spine still has no citation row, and the first attempt to supply one produced a false theorem — this row must be sourced by the bench before §5 is drafted.**
4. **The skeleton says "the two data contacts (the crossings)".** There are **five**, and the surface is exhausted. `SKELETON.md` §12.2 must be rewritten before reuse.

## 5. Figures (extends `SKELETON.md` §4's eight)

| Fig | content |
|---|---|
| **0** | ## **The doorway**: `15 = 3·5` → `SL(2,3)×SL(2,5)` → `2T × 2I` → McKay → **E₆ × E₈** |
| **0b** | ## **The chain as a bar**: 43 links, 4 axioms marked, the C6→C17 axiom-free stretch shaded |
| 1–8 | as in `SKELETON.md` §4 (cascade ladder, plane stratification, tiling, magic square, concordance, ε-census, 15 atoms, Klein group) |

## 6. Declared

- **cc3 has not opened `SKELETON.md` §2's per-section content lists in full** — only its
  section headings, registry, and figures list. The compression in §§6–8 must be done
  against the full text, not against this outline's summary of it.
- **Every "GAP" above is a real hole in the paper's spine, not a formatting note.**
- The genesis registry rows are transcribed from `docs/THEOREM_LEDGER.md`; **cc3 has not
  re-run the cited locks** except `test_b749_genesis_forks.py`, `test_b285_commutator_phase.py`,
  `test_b749_f2_f8_locks.py`, and `scripts/checks/forcedness_census.py`.
