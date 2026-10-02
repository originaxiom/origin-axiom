# B1521 — GENESIS v1.3: THE AUDIT LANE'S CORRECTIONS CARRIED, THE DECIDING TEST'S OUTCOME ON BOTH BENCHES, AND B1297'S P IS THE SWAP (IT FIXES ρ_q; THE INVERSION DUALISES IT)

**Date:** 2026-10-02. **Verdict: PROVED.** There are four checks, C1–C4, each with an opposite control.

**Not sealed.** Each item checks a stated claim whose answer the record already fixes: B1455's table, B1520's stabiliser,
B723's banner, and the probes of B37 and B130. No outcome that is still open is computed here. **creates_law is false.**
0 of 19 Standard-Model parameters; I-26 stays UNEARNED.

**Source.**
- The owner, verbatim (2026-10-02): *"do as u recomend with all independently, goal remains / dont ignore anything loadbearing
  including qualia, all oallowed not just m004, choice might be golden"*.
- The recommendation it answers: GENESIS v1.3 first, then the deciding test on all allowed states with the golden hypothesis
  sealed.
- The audit lane's relay of `1e3d17b9` (ACT_REGISTER AR1–AR6), which asks for three corrections in GENESIS:
  - FK12's never-reads sentence (AR3);
  - B723 cited with both of its retractions (AR6);
  - B130's elimination scoped (AR4).

## Seen first (the repo sweep and the literature)

**The repo sweep**, made before any GENESIS text was written.
- Every head was fetched first. Main had moved to `8d1c1329`, B1455's addendum, which credits B1455's three lines to B1297
  and "the count is the order" to B1438. The audit lane was at `7b088f50` (R80 sealed, not run). The seat lanes were
  unchanged (`0043be2b`, `7cda35aa`, `13d2c5b6`, `5d58b935`, `659487bb`).
- `scripts/checks/prior_work.py` ran on ten terms in the record's own vocabulary: "period-2", "a³b", "never reads",
  "self-model", "forced choice", "isolated component", "elimination ideal", "act of distinction", "registering",
  "homeomorphism-invariant". All are present; the heads and the hits read are in `arc_verdict.json`.
- Main's `topic_sweep.py`, run from a checkout of main at `8d1c1329`: *58 of 1327 arcs on main match (NEGATIVE 17, OPEN 2,
  PROVED 39); 8 other lanes match.*
- Read for this arc:
  - main's B1297 FINDINGS §4.2, §5.2 and §6, and its credit note; main's B1455 FINDINGS §1–§3 and §5, and its addendum;
  - the audit lane's `ACT_REGISTER.md`, `philosophy/P_ACT_AND_REGISTER_2026_10_02.md` and `GATE5Q_PHENOMENOLOGY_FIREWALL.md`;
  - B20, B37 and B130 (FINDINGS and probes), and B723's banner;
  - the verdicts of B871, B861, B330, B347, B353 and B786;
  - this seat's B1279 and B1520.

**What the sweep found that this arc must not present as new.**
- **"P is the swap."** This seat's B1279 (2026-09-06) found the object's eight isometries by word search in Riley's holonomy.
  It named the period-2 symmetry "the period-2 swap a ↔ b" and found that it inverts every torsion character. C1 is a check
  across two presentations, not a discovery.
- **"ρ_q ∘ swap ≅ ρ_q"** is a row of main's B1455 table and an element of B1520's stabiliser. C1's contribution is to put
  main's P and B1455's swap on one presentation. That corrects one sentence of main's B1455 addendum (§1).
- **AR1–AR6** are the audit lane's. C2–C4 re-derive AR3–AR6 with this seat's code.
- **L1–L3 are B1297's** (main's addendum). B1520 missed them; that miss is an E54 instance in `docs/ERROR_LEDGER.md`, and B1520
  carries an addendum.
- **"The count is the order"** is B1438's slope law (main's addendum).
- **Registering at the group layer** is already defined: B871 (PROVED), with B861.

**The literature.**
- S. A. Ballas, *Finite volume properly convex deformations of the figure-eight knot*, arXiv:1403.3314v3, p. 17: the family
  and its presentation (read for B1520, the same day).
- SnapPy's m004 (run, not cited from memory): the presentation ⟨a, b | aaabABBAb⟩, the meridian ab, the symmetry group D4.
- Nothing else is needed. The isomorphism is checked directly (ψ ∘ φ = id), with no appeal to Hopficity, and AR4's
  countermodel is a computation, not a citation.

## 1. Which symmetry dualises the family (C1, `verification/which_class_is_P.py`)

**The claim checked.** Main's B1455 addendum: *"B1297 §6 leaves open the modules for which 'ρ₁∘P is not dual to ρ₁ — nothing
forces it there'. On Ballas' SL(4) family it* is *dual, for every q > 0, by computation (two routes)."* B1297 writes P in
SnapPy's presentation as a ↦ a⁻¹, b ↦ a³b, orientation-preserving and +1 on the free part.

**1. The two presentations are one group.**
- SnapPy's SL(2, ℂ) holonomy sends the relator aaabABBAb to −I, so it is a lift only up to sign. a has exponent sum 1 in the
  relator, so a ↦ −a gives a genuine lift, which is faithful.
- In that holonomy, m = ab and n = aabA satisfy Ballas' relator mnMNmNMnmN. They give back a = MnmN and b = nMNmm.
- Proof by free-group words alone that φ: ⟨m, n | R′⟩ → π₁(m004) is an isomorphism:
  - ψ(φ(m)) = m freely;
  - ψ(φ(n)) = n times a cyclic conjugate of R′;
  - ψ(R), cyclically reduced and rotated by one, is the concatenation u·v of a cyclic conjugate u of R′ and one v of R′⁻¹.
  - So ψ is well defined and ψ ∘ φ = id. φ is injective, and onto because a and b are in its image.

**2. P transported.**
- P(m) = MnmNm and P(n) = nmN, with H₁ images (1, 1).
- In the faithful holonomy, P = conj(nM) ∘ s, where s swaps m and n. So **P is the swap's class in Out(π₁ m004)**.
- No conjugator puts P in the identity class; the search ran over words of length ≤ 8.

**3. Ballas, exact.** Own Fraction arithmetic, at q = 2, 3, 1/5 and 7/3:

| intertwiners towards ρ_q ∘ P from | dimension | invertible member |
|---|---|---|
| ρ_q | 1 | yes |
| ρ_q* | 0 | — |
| ρ_q ∘ s | 1 | yes |
| ρ_q ∘ θ (the inversion) | 0 | — |

At q = 1 all four coincide.

**So ρ_q ∘ P ≅ ρ_q, and not ρ_q*, for q ≠ 1.** The addendum's sentence holds for the inversion θ and for θ after P, not for
P itself.
- **What stands:** its conclusion at level one. Every reductive module of the family has index zero, through θ (main's B1455;
  sm:B1520).
- **What does not follow:** the extension to the levels. B1297's tower theorem uses P, which acts as −1 on every torsion
  character of every cyclic cover. The family's vanishing uses θ. On a level, a vacuum ρ_q ⊗ ψ is fixed by a count-odd map
  D ∘ σ only if one σ does both jobs.
- **Main's L242 (b) is therefore open.** This seat takes it next as sm:B1522, sealed before computing.

## 2. The audit lane's corrections, re-derived (C2–C4, `verification/audit_corrections.py`)

**C2 (AR3, B20 and B37).** The trace map T(x, y, z) = (z, x, 2xz − y) conserves I = x² + y² + z² − 2xyz − 1. With Fricke
coordinates X = 2x, Y = 2y, Z = 2z, κ − 2 = 4I.
- B37's self-model test is `any(component.has(I))` for a fresh symbol. B20's is `T.subs({I: c}) == T`. Both test for the
  literal presence of a symbol.
- On the record graph r = I, the map T′(x, y, z, r) = (z, x, 2xz − y + (r − I), r) equals (T, I). The graph is T′-invariant, so
  T′ and T are the same dynamics there.
- Both tests fire on T′ and not on T. **The test changes under a vacuous rewriting**, so it neither shows nor excludes a
  self-model.
- Opposite control: a genuine read off the graph (z′ = 2xz − y + r) changes the orbit when r ≠ I.
- B37's own definition asks for "reads AND branches"; its probe tests only presence.

**C3 (AR4 and AR5, B130).**
- The variety x(x − 1) = 0, x·k = 0 is the line x = 0 plus the point (1, 0). The point's Jacobian has rank 2, so it is an
  isolated component, and still the elimination ideal in k is zero.
- Opposite control: the point alone, (x − 1, x·k), eliminates to (k).
- B130's own computation at m = 2 is reproduced. φ₂ is composed as its probe composes it (Tb twice, then Ta twice), and the
  elimination ideal in κ is zero.
- So B130 shows that κ takes a continuum of values on the fixed locus. **Its reading that a unit is internally fork-free needs
  a componentwise proof**, which is open (sL-10 item 5; GENESIS v1.3 §8).
- **AR5.** The fields ℚ(√(m² + 4)) by squarefree part: m = 1, 4 and 11 all give ℚ(√5), since √20 = 2√5 and √125 = 5√5. B130's
  "distinct Perron eigenvalue fields" is wrong there. The incidence matrices [[m, 1], [1, 0]] have distinct traces, so the
  seeds stay non-conjugate.

**C4 (AR6, B723).**
- Complex conjugation sends √−3 to −√−3. It does not fix K = ℚ(√−3) pointwise, so it is not in Gal(K^ab/K). That is B942's
  correction, elementary.
- B723's banner, read from the file, carries both retractions: B942 (the chirality clause) and B957 (the values and torsor
  clause).

## 3. GENESIS v1.3 (`verification/merge_genesis_v13.py`)

The generator takes v1.2, kept byte-identical in `received/GENESIS_v1_2.md` (sha-256 `9cf58165…`), and makes exact
replacements. Each must match once. The changes, all marked **[v1.3]**:
- **§7.** B723 cited with the B942 and B957 retractions. What survives is the structure (a measurement as a choice of fibre
  functor with a Galois ambiguity), not either group assignment.
- **§8, FK9.**
  - The run of main's B1455 and sm:B1520: NEGATIVE at level one, frame F-HE, reach single.
  - The lemmas credited to B1297.
  - C1's correction: the dualising symmetry is the inversion, not P. The levels stay open (main's L242 (b)).
  - The owner's hypothesis "choice might be golden", registered and untested.
- **§8, FK12.**
  - The never-reads sentence scoped to B37's literal test (AR3), and B130's fork-free reading scoped (AR4).
  - On m004's family a symmetric law does land in states it does not fix, for half of the symmetries, but never for a
    count-odd one.
  - The owner's act-and-register priority, with its three questions kept apart:
    - whether a reduction loses data a later operation needs (AR1, AR2);
    - whether a registering mechanism is derived (the group layer has one, B871);
    - the experiential question, a hypothesis under Gate 5-Q, never a claim.
  - The measurer's exact referent: main's B1455 §5 and L241, with B1438.
- **§8, the frontier list.** Two items: the deciding test on the levels and on other states, and the componentwise fixed loci.
- **§9.** Four rows, AR5's field label among them.
- **§10.** The version log.

**No status changes.** v1.1's marks (21, 15 of them bold) and v1.2's bold marks (22) are unchanged, and v1.3 adds 12. FK1 and
FK12 stay the owner's to frame. The experiential question is named as such in GENESIS: Gate 5-Q (Q5) keeps its own vocabulary
in `philosophy/` and `speculations/`.

## 4. Elsewhere

- **The kill graph.** B20, B37 and B130 carry dated scope notes. Their judgement fields stay unset, as their routing requires.
- **`docs/OPEN_PROBLEMS.md` gate A.** A scope note on B130's part. The other classes there are not touched.
- **B1520.** An addendum (L1–L3 are B1297's; P is its s). Its sealed files and table are unchanged.
- **`docs/ERROR_LEDGER.md`.** An E54 instance for B1520's credit.
- **B1519's lock** now reads v1.2 from this arc's `received/` copy. GENESIS.md is v1.3.
- **Relays.**
  - To main, `SM_TO_CC_2026-10-02_P_IS_THE_SWAP_AND_GENESIS_V1_3.md`.
  - To the audit lane, `SM_TO_CODEX_2026-10-02_ACT_REGISTER_ANSWERED_GENESIS_V1_3.md`.
- **sL-10.** Item 4 is done. Item 2 is sharpened to the levels (sm:B1522). Item 5 is registered: the componentwise fixed loci,
  with the golden unit first.

## 5. Standing and firewall

**Standing: RE-DERIVED.** Each check agrees with a cited source:
- B1279 and B1455's table, for C1;
- the audit lane's AR3–AR6, for C2–C4.

What is added:
- the explicit bridge between the two presentations, which corrects one sentence of main's addendum;
- the record's own instance of the B130 elimination, reproduced.

GENESIS states the experiential question as a hypothesis under Gate 5-Q, and nothing is claimed about experience. No
Standard-Model number is touched: **0 of 19**.
