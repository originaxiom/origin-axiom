# B1812 — THE TOWERS IN F-THEORY's 7-BRANE FRAME (P-415, THE OWNER's TOWERS QUESTION; P-419's CARD; DATA-FREE): THE GENESIS WORD LR (TRACE 3) LIES IN THE SINGLE SL(2, ℤ) CLASS THAT DeWOLFE–HAUER–IQBAL–ZWIEBACH ASSIGN TO THE E₁₀ = E₈^H CONFIGURATION, WHOSE NESTED SUBCONFIGURATIONS A^(N−1)BCC CARRY su(3) ⊕ su(2), su(5), so(10), E₆, E₇, E₈, Ê₈. BUT ONLY so(10) THROUGH E₈ CAN COLLAPSE TO SINGULARITIES; su(3) ⊕ su(2) AND su(5) SIT ON HYPERBOLIC CLASSES OF NEGATIVE TRACE AND CANNOT, SO THEIR ALGEBRAS ORGANISE MASSIVE BPS STATES, NOT GAUGE SYMMETRIES AT A POINT. NEGATIVE FOR "THE STANDARD MODEL's TOWERS MEETING AT LOCI" IN THIS FRAME; THE OBJECT FIXES THE TOTAL CLASS, NOT WHERE ANY TOWER SITS

**Verdict: NEGATIVE** for the towers-meeting-at-loci reading of P-415 in this frame. The structure is **PROVED**, by exact
computation and read in the source. Data-free; none of the 19. cc (main), 2026-10-29. Corrected before landing at its
hostile referee (§ 5): four blocking findings.

> *Scope corrected 2026-10-30 (Review 73: its reader's finding; main's own check, `verification/review73_subcollections.py`
> → `.json`). The NEGATIVE holds for the E_N realisation of the lowest rungs, not for their algebras. Inside the same
> twelve-brane configuration A⁹BCC the contiguous sub-collections A⁵ ⊂ A⁵BC ⊂ A⁵BCC have Kodaira monodromies with
> matching brane numbers, I₅ (su(5)) ⊂ I₁* (so(10)) ⊂ IV* (e₆), and A³ and A² those of I₃ and I₂ (su(3), su(2)). So
> SU(5) ⊂ SO(10) ⊂ E₆ can meet at a point in this frame, and the Standard Model's algebra can sit at points, as stacks of
> A-branes. What stays NEGATIVE: su(3) ⊕ su(2) and su(5) as the nested E₃ and E₄ subconfigurations (hyperbolic, not
> collapsible), and the object's fixing of any meeting: it fixes the total class, not where the branes sit. By P-415's
> own criterion (a breakthrough only if the object fixes where the towers meet) the verdict stands; its reason, in the
> title and in § 3, is narrowed here. The class: E9, a closure stated wider than the computation.*

**0 of 19.**

## The frame card (WORKING_RULES, the rule of 2026-10-29)

| item | value | label |
|---|---|---|
| frame | F-theory 7-branes: the SL(2, ℤ) monodromy acting on τ and on the (p, q) charges, as DeWolfe–Hauer–Iqbal–Zwiebach classify (hep-th/9812028, DHIZ-I; hep-th/9812209, DHIZ-II); a configuration's algebra from its junction lattice | CHOSEN (the frame) |
| identification | the object's word LR (GENESIS: L = [[1,1],[0,1]], R = [[1,0],[1,1]], LR = [[2,1],[1,1]]) as such a monodromy. On τ alone A and −A coincide, and −A's class is E₄'s, so the sign is load-bearing | CHOSEN; UNEARNED (IDENTIFICATION_LEDGER's sense) |
| what follows | LR's conjugacy class: the single class at trace 3 (h⁺(5) = 1), which DHIZ-II § 6 names E₁₀ ≅ E₈^H | FORCED given the identification |
| the configuration | E₁₀ on 12 branes, A⁹BCC | rests on DHIZ's conjecture that configurations are classified by monodromy, brane number and ℓ, and on minimality (12 + 12k branes also realise the class) |
| outputs | algebras, monodromies, collapsibility | no value; none of the 19 |

## 1. Computed (`verification/e_n_monodromy.py` → `.json`, `_run.txt`; exact; every reported number computed there)

- **Conventions** (DHIZ-I eq. 2.4: for branes X₁ … Xₙ, K = K_{zₙ} ⋯ K_{z₁}): K_[p,q] = [[1 + pq, −p²], [q², 1 − pq]],
  with A = [1, 0], B = [1, −1], C = [1, 1].
- **The series.** K(E_N) = K_C K_C K_B K_A^(N−1) = [[−2, 2N − 9], [−1, N − 5]], with Tr = N − 7 for N = 1, …, 12
  (DHIZ-I eq. 7.56). Every K(E_N) has content 1.
- **E₁₀ and the object's word.** K(E₁₀) = [[−2, 11], [−1, 5]]. g = [[−3, 7], [5, −12]] ∈ SL(2, ℤ) satisfies
  g·K(E₁₀)·g⁻¹ = LR = [[2, 1], [1, 1]] (GENESIS); g₀ = [[−3, 7], [2, −5]] gives RL.
- **Why the conjugacy holds.** Trace 3 is one class because h⁺(5) = 1. (LR)⁻¹ is conjugate to LR for the same reason.
- **The sister's sign.** g = [[−5, −3], [−8, −5]] takes K(E₄) to −RL: trace −3, the sign class of m003's word (B781).
  On τ alone ±RL coincide.
- **E₃ and E₄** have traces −4 and −3: hyperbolic, negative trace.
- **The metallic word states LⁿRⁿ** have traces 3, 6, 11, 18 and content n. For n ≥ 2 they are therefore not conjugate to
  any K(E_N), which all have content 1. **Among the metallic words only the golden one is an E-series monodromy.**

## 2. Read in the source

- **DHIZ-I, § 4.2.** A^(N−1)BCC realises E₁ = A₁, E₂ = A₁ ⊕ u(1), E₃ = A₂ ⊕ A₁, E₄ = A₄ and E₅ = D₅. (The passage's
  "A^N BCC" is a typo: its own (2.12), E₁ = BCC and E₅ = A⁴BCC fix A^(N−1)BCC.) E₅ ≅ D₅ is explicit at (2.9)–(2.11).
- **DHIZ-I, introduction and § 7.4.** The configurations collapse into Kodaira singularities only for D_N (N ≥ 4), E₅–E₈
  and H₀–H₂. "None of the hyperbolic conjugacy classes correspond to collapsible configurations."
- **DHIZ-II, §§ 5–6** (the referee's read; main read DHIZ-I).
  - E₁–E₄ are associated with hyperbolic classes of negative trace.
  - E₉ ≅ Ê₈ is affine and parabolic, and not collapsible.
  - E₁₀ = E₈^H is hyperbolic Kac–Moody, the single class at t = 3.
  - E_N for N > 10 are Lorentzian Kac–Moody algebras, not hyperbolic.
  - On non-collapsible configurations the algebras are spectrum-generating: they organise massive BPS junctions.
- **The nesting** (the referee's junction-lattice check). The zero-charge junction lattices of A^(N−1)BCC are nested
  isometric sublattices, giving regular subalgebras E₃ ⊂ … ⊂ E₁₀. They are negative definite up to N = 8, have one null
  direction at N = 9, and are even unimodular of signature (9, 1) at N = 10.

## 3. What it means

- **For the towers question (P-415): NEGATIVE in this frame.** One configuration in the object's class carries the whole
  chain, su(3) ⊕ su(2) ⊂ su(5) ⊂ so(10) ⊂ E₆ ⊂ E₇ ⊂ E₈ ⊂ Ê₈ ⊂ E₁₀, as nested subconfigurations.
  - Only so(10), E₆, E₇ and E₈ can collapse to Kodaira singularities (I₁*, IV*, III*, II*), i.e. be gauge symmetries at
    a point: towers meeting at loci.
  - su(3) ⊕ su(2) and su(5) sit on hyperbolic classes of negative trace and cannot; nor can Ê₈ or E₁₀.
  - So the Standard Model's and SU(5)'s algebras are exactly the ones that are not gauge symmetries at a point here.
    *[Withdrawn 2026-10-30 (Review 73): true of their E₃ and E₄ realisations only; as stacks of A-branes they collapse
    (the dated note under the verdict).]*
  - The object fixes only the total class. Where the branes sit, and hence which subconfigurations collapse, is a
    modulus.
- **What it does not give.**
  - No value and none of the 19. The literature read (main's notes, audit room; the papers cited below) gives no mechanism by which a
    τ-monodromy fixes Yukawas or mixings: Yukawas localise at E₆ and SO(12) points and depend on moduli and flux.
  - "SU(3) × SU(2)" is meant at the Lie-algebra level only. The global form and hypercharge are not fixed (E₃ has rank 3;
    hypercharge is its commutant in E₄).
- **What is new.** Only that the genesis word has trace 3, together with the sign remark (m003's −RL is E₄'s class). The
  classification, the chain and the collapsibility are DHIZ's.
  - **It complements B1343,** which proved the object's monodromy conjugate to no Kodaira fibre: the object's class is the
    first positive-trace hyperbolic (non-collapsible) class.
  - The same algebras occur in the record's E₈ (B1752's container) and E₆ (B727, generic). No map from those to these
    subconfigurations is shown.
- **0 of 19.**

## 4. Scope

- One frame (F-theory 7-branes in DHIZ's classification), with the identification CHOSEN.
- The configuration's brane number by minimality.

## 5. The referee (hostile, read-only; `verification/referee/`, its REPORT.md)

- **Its verdict:** BLOCK; PASS WITH CORRECTIONS once applied. All were applied.
- **What it recomputed independently:** the conventions (DHIZ-I 2.4), the traces, H(3) = 1 (gp; reduced-form cycles),
  the junction-lattice nesting, the algebras.
- **Blocking findings:**
  - (C1) the draft read "up to E₈ can collapse" as including su(3) ⊕ su(2) and su(5). The source says E₁–E₄ are
    hyperbolic and non-collapsible, which turns this arc's reading into the NEGATIVE above.
  - (C2) the metallic claim was false for n ≥ 2 (the content invariant).
  - (C3) the draft's matrices used the transposed L and R (its "LR" was GENESIS's RL).
  - (C4) its JSON carried keys the script did not write.
- **Corrections:** the sign (C7); "FORCED" scoped to the class (C8); the source's typo (C9); the wording (C5, C6, C10,
  C11); the Seen first (C12: B1343, S041, B1344, B781); the novelty (C13); the record's E₈ and E₆ (C14); the algebra
  level (C15).
- **Main's verification:**
  - the collapsibility sentences, in DHIZ-I's text main extracted;
  - GENESIS's convention (§ 2);
  - the content argument;
  - B1343's statement;
  - the script, which now computes every reported number.

## Seen first

`VERDICT topic-sweep /E_?10|E₁₀|7-brane|DeWolfe|monodromy.{0,30}(trace 3|F-theory)|axio.dilaton/ (full text): 14 of 1558
arcs, 0 register rows` (the referee's). No hit links the object to 7-branes or E₁₀.

**Bearing on it:**
- B1343 (no Kodaira fibre: the elliptic bridge closed);
- S041 (F-theory rated generic and blocked);
- B1344 C6;
- B781 (the sister m003);
- speculations/S061 (E₁₀ as cosmological billiards: a different role).

**Literature:**
- DHIZ-I (read on the bench), DHIZ-II (the referee's read);
- Donagi–Wijnholt, Beasley–Heckman–Vafa, Heckman–Vafa (through the notes).
