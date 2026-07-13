# B556 — The Escalator Tower: T(M) = [[M, M],[M², M]]  (HYPOTHESIS + verified core)

Processes chat-2's "escalator" handoff verify-don't-trust. The computational
core is VERIFIED EXACTLY; the tower-as-physics-ladder reading is banked as a
labeled HYPOTHESIS so it is not lost or re-derived. Owner-directed: run the
escalator to its end and treat it seriously.

## VERIFIED FACTS (locked, tests/test_b556.py)

1. **T(F) = M₄ verbatim.** With F = [[1,1],[1,0]] (golden Fibonacci matrix),
   T(F) = [[F, F],[F², F]] EQUALS the σ₄ incidence matrix M₄ exactly (not up
   to permutation — literally). Same charpoly x⁴−2x³−5x²−4x−1. **This is
   B517's intertwining theorem** — B517 proved M₄ = [[F, C],[D, F]] with
   (C, D) = (F, F²) the golden-specific coupling; the escalator is that functor
   with C=M, D=M². So level 1 is a grounded FACT, not a coincidence.
2. **Rung 2:** T(M₄) is 8×8, charpoly degree 8 IRREDUCIBLE, Perron =
   10.724751772 (= β(1+√β), matching the self-similar law to all digits).
   √λ₂ ∉ ℚ(τ): the field genuinely doubles 4 → 8.
3. **The tower** (rungs 0–4): sizes 2,4,8,16,32; charpoly degrees 2,4,8,16,32,
   ALL irreducible; Perrons φ, 3.676, 10.725, 45.847, 356.28.
4. **The λ-law:** λ_{n+1} = λ_n(1+√λ_n) reproduces every Perron exactly
   (λ₀=φ). Each rung is the square-root extension of the previous Perron;
   field degree = 2^{n+1}.

## The closure (why coupling is the ONLY escalator)

Three alternative "climb" routes are closed:
- induction saturates in ℚ(τ) — BANKED (B533/B535 census saturation);
- the return-word flow has a fixed point (σ refines to itself) — BANKED (B540);
- covering functor non-escalating (13×13 lift, Perron unchanged) — chat-2's
  NEW claim, NOT independently verified here (needs their cover construction).
So (modulo the third) coupling via (M, M²) is the only degree-raising operation.

## THE HYPOTHESIS (labeled — not a claim)

> **One rule — couple X to itself through (X, X²) — applied to itself forever.
> Rung 0 = the golden layer (nature RELAXES into it: FK, circle maps, E₈'s φ).
> Rung 1 = the species layer (reachable only by BUILDING — the species chain,
> B543/B546, gap labels at 3.9×10⁻⁸). Rung 2+ = coupled layers no one has
> built, each naming its field (degree 2^{n+1}), its Perron (the λ-law), and a
> buildable Hamiltonian (an 8-coupling chain at rung 2 whose gap labels would
> live in the degree-8 field).** The rule is the origin gesture (a → a·a²)
> operating on whole systems instead of letters.

Physics contact so far: rung 0 confirmed (universality: E₈, gap labels), rung 1
built (the species chain). Rung 2 is the next experiment candidate BEHIND the
species chain — an 8-letter substitution carrier realizing T(M₄).

## HONEST BOUNDARIES (so this stays trustworthy)

- Rung 0→1 (T(F)=M₄) is a FACT (B517).
- The iteration rule T at rung ≥ 2 is the CANONICAL self-similar continuation
  — natural and exact, but a **CHOICE** (other couplings are conceivable).
  Under this rule the rung-2 field-doubling is a COMPUTED FACT, not a
  conjecture. Stated as such.
- The physics-ladder reading is HYPOTHESIS; each rung carries a falsifiable
  membership test (its field) and a device (its chain) — that is what keeps it
  from regress mysticism, but it is not banked as physics.
- **Lit-gate MANDATORY before novelty language:** coupled / graph-directed
  substitutions, block-matrix Pisot towers, and self-similar substitution
  hierarchies have a literature (Queffélec; Fogg; graph-directed IFS;
  Frank–Sadun fusion). Queue on the cost-tiered script before claiming the
  functor or the tower is new.

## Next steps (recorded so we don't re-derive)
1. Write the explicit rung-2 8-letter substitution carrier (chat-2: images
   σ₄(j)₁·σ₄²(j)₂), verify its incidence = T(M₄), and add to the experiment
   ladder behind B555.
2. Lit-gate the functor + tower.
3. Verify (or refute) the covers-non-escalating closure claim (needs the lift).

Locks: tests/test_b556.py.

## PROOF UPGRADE (chat-2 audit, verified 2026-07-12): the doubling is a THEOREM

B556 banked the field-doubling from numerics. It is now PROVED exactly (three
verified misses from the chat-2 audit):

**Miss A — the norm-sign argument (rung 2, one line):** β (the rung-1 Perron)
has N(β) = product of the quartic's roots = **−1 < 0** (the constant term of
x⁴−2x³−5x²−4x−1). A square y² ∈ ℚ(τ) has N(y²) = N(y)² ≥ 0. Contradiction ⟹
√β ∉ ℚ(τ) ⟹ the field DOUBLES at rung 2. (At rung 2 the SIGN does the work;
higher rungs also fail by magnitude.)

**Miss B — the determinant telescope (all rungs):** for the commuting-block
escalator, det T(M) = det(M²−M³) = det(M)²·det(I−M), so
  **dₙ₊₁ = dₙ²·eₙ,  eₙ := det(I−Mₙ)** — verified exactly through rung 4:
  dₙ = −1, −1, −11, −97889, −1.8×10¹⁷;  eₙ = −1, −11, −809, −18845089, −2.3×10²⁰.
**Every eₙ is NEGATIVE (verified rungs 0–4)**, so the norm-sign proof of Miss A
fires at EVERY rung: field-doubling is PROVED at rungs 1→2→3→4→5. The all-n
tower now rests on exactly TWO clean, per-rung-checkable conjectures:
irreducibility (CC-verified 0–4) and negativity of eₙ (verified 0–4). The
"hypothesis" acquired an exact per-rung engine.

**Miss C — the charge tower (the ℤ/11 governs the tower):** e₁ = det(I−M₄) =
**−11 = the B552 base charge** (coker(I−M₄) = ℤ/11). By the telescope, every
rung's determinant is built from the eₖ below. The **charge tower**
|eₙ| = **1, 11, 809, 18845089, 228654672055316545291** (809 and 18845089 prime;
e₄ = 11²·1459·597049·2169349081), and **coker(I−Mₙ) = ℤ/|eₙ| is CYCLIC at every
verified rung** (SNF: a single non-trivial invariant factor). B552's isolated
ℤ/11 is the foundation stone of this second sequence.

## Cover-closure spec logged (for B557 E4)
chat-2 supplied the cover construction for the closure leg I flagged unverified:
M-invariant mod-2 plane basis χ₁=(0,1,1,0), χ₂=(1,0,1,1) on (a,b,A,B); cosets =
F₂²; BFS Schreier transversal; 13 generators (16 (coset,letter) pairs − 3 tree
edges); abelianized lift column (c,g) = R(c) + scan(φ(g), start c) − R(c+χ(g)),
R(c)=scan of φ(rep_c) from 0. Expected: charpoly degrees (2)(4)(7), Perron = β
unchanged (non-escalating). Verification deferred to B557 E4 (closure cell).

## NEW (2026-07-12): ONE fixed cubic generates the whole charge tower

The charge tower eₙ = det(I−Mₙ) is generated by a SINGLE fixed cubic applied
multiplicatively over each rung's spectrum:
  **eₙ₊₁ = ∏_{λ ∈ spec(Mₙ)} (1 − 2λ + λ² − λ³) = det(I − 2Mₙ + Mₙ² − Mₙ³)** —
verified exact through rung 4 (−11, −809, −18845089, −2.3×10²⁰). The cubic
g(x) = 1−2x+x²−x³ is exactly the doubling's (1−μ)²−μ³ factor
(from μ → μ(1±√μ)). So ALL the charge-tower primes (11, 809, 1459, 597049,
2169349081, …) come from one cubic evaluated over the growing spectra.

**ONE doubling, TWO towers.** The same eigenvalue-doubling μ → μ(1±√μ) produces
both towers: the ANALYTIC tower (Perron/field, λ_{n+1}=λ_n(1+√λ_n), degrees
2→4→8→16→32) is the + branch's top; the ARITHMETIC tower (charge, cyclic
coker) is the product of (1−both branches). The object's depth has two faces of
one operation.

**Curio (hint-ledger):** disc(x³−x²+2x−1) = **−23** — the same discriminant
flagged in B554 as the h=3 counterexample to "minimality forces h=1." The
charge cubic lives in a class-number-3 field. Possibly meaningful, possibly
coincidence; recorded, not claimed.

## The charge tower's arithmetic — RUN (2026-07-12, verified)

Three closed forms and a periodicity, all exact:

**1. Closed form:** eₙ = det(I−Mₙ) = **charpoly_n(1)** (verified through rung 5).
Extended data: e₅ = −1.455×10⁶¹ (62 digits, three large primes).

**2. The charpoly-tower recursion (resultant):**
  **charpoly_{n+1}(x) = ∏_{μ∈spec(Mₙ)} (x²−2μx+μ²−μ³) = ±Res_μ(charpoly_n(μ),
   x²−2μx+μ²−μ³)** — the whole tower is one fixed resultant iterated (verified:
  reproduces the quartic from the golden quadratic). Hence
  **eₙ₊₁ = ±Res(charpoly_n, g), g = x³−x²+2x−1** (verified, ratio 1 all rungs).

**3. Why these primes — the doubling-orbit characterization:** p | eₙ ⟺
1 ∈ spec(Mₙ) mod p ⟺ the doubling orbit μ→μ(1±√μ) of the golden pair {φ,ψ}
mod p reaches 1 at rung n. So the charge-tower primes are exactly those p for
which the golden pair's doubling orbit hits 1.

**4. The ℤ/11 recurs with PERIOD 3:** 11 | eₙ at n = 1, 4, 7 (confirmed three
periods) — the B552 base charge reappears up the tower with period 3 (= the
doubling-orbit period of {φ,ψ} mod 11). The small primes 3, 5, 7, 13, 23 divide
NO eₙ in range — the charge tower AVOIDS them; its primes are a specific set
(11, 809, 1459, 597049, 2169349081, …) selected by the orbit-hits-1 condition.

**Reading:** the charge tower is not a random prime sequence — it is det(I−Mₙ)
generated by one fixed cubic (disc −23), and each prime divides it periodically
with period = its doubling-orbit period. The B552 ℤ/11 is the p=11 instance,
period 3. The object's depth has a periodic prime arithmetic, one prime per
orbit-return.

## The period question — computed as far as rigor allows (2026-07-12)

"What determines each prime's period in the charge tower?" — computed, with an
honest boundary:

**PROVEN — the mechanism.** p | eₙ ⟺ 1 ∈ spec(Mₙ) mod p ⟺ the golden pair's
doubling orbit reaches 1 at rung n; equivalently p | eₙ₊₁ ⟺ charpoly_n and the
fixed cubic g = x³−x²+2x−1 share a root mod p (Res(charpoly_n, g) ≡ 0). So the
period is a FINITE-FIELD DOUBLING-ORBIT PERIOD — the frequency with which the
orbit returns to 1 in the splitting field.

**CONFIRMED — one clean case.** p = 11: period **3** (zeros at n = 1, 4, 7,
three hits). The B552 ℤ/11 charge recurs every 3 rungs.

**The g-structure (which primes CAN appear).** g mod p has a linear root for
p ∈ {5, 7, 11, 17, 19, 23, 809}, is inert for {3, 13, 29}. But a g-root is
NECESSARY-not-sufficient: 5 and 7 have g-roots yet divide NO eₙ in range — the
orbit must actually REACH the root, and for 5, 7 it doesn't (within reach).

**COMPLETED (extended computation) — there is NO simple period law; the
charge-tower primes are a dynamically-sparse, orbit-selected set.**
- **11: period 3 CONFIRMED through 4 periods** — the matrix det pushed to n=11
  (size 4096); zeros at exactly n = 1, 4, 7, 10, with no off-pattern zeros.
- **809: LARGE period** (> 9) — appears only at n=2 within reach (n≤11). So the
  periods vary wildly (11→3, 809→large); there is no uniform small period.
- **Sparsity, not captured by any simple invariant:** among ALL primes 3–79,
  ONLY 11 divides any eₙ for n≤8. And the appearance is NOT predicted by the
  obvious invariants — 19, 61, 79 share 11's g-factorization type (1 linear + 1
  quadratic) AND have 5 a quadratic residue, yet none divides any eₙ in range.
  So no congruence/factorization condition determines appearance.
- **Conclusion:** the period is a genuine finite-field DOUBLING-ORBIT RETURN
  period — computable per-prime by iterating μ→μ(1±√μ) in the splitting field,
  but NOT reducible to a closed form in p. The mechanism is fully characterized;
  "which primes, and with what period" is intrinsically dynamical, not
  formulaic. That is the complete, honest answer: no simple law, and the exact
  reason why (orbit-selection in a growing splitting field).

## The feedback ledger — the charge as the residue of self-reference (chat-2 handoff, INDEPENDENTLY VERIFIED 2026-07-13)

chat-2 asked the audit question "did we ever study the object's feedback *as
feedback* — as an information channel?" and delivered a ledger. Each claim below
was re-derived in-sandbox before banking (`tests/test_b556_feedback.py`);
verdicts are marked VERIFIED / PENDING / HINT.

**VERIFIED — the golden-norm closed form of the charge.** e₁ = N_{ℚ(√5)/ℚ}(g₁(φ))
= −11 **exactly**, where g₁ = the fixed cubic g = x³−x²+2x−1 and φ = (1+√5)/2.
Re-derived two ways: (a) directly, g₁(φ) = 3φ−1 = (1+3√5)/2, and (3φ−1)(3φ′−1)
= −11; (b) from the eigenvalue product e_n = ∏(1−λ), splitting the 2ⁿ⁺¹
eigenvalues into the φ-branch and its Galois-conjugate ψ-branch — the branch
product is ±g₁(φ), the two branches give the norm. So **the charge is a norm from
the golden field**; "the entire arithmetic depth is the shadow of a single cubic
walking on φ" is exact at rung 1.
  - *PENDING (construction under-specified):* the doubling-transfer that builds
    g₂, g₃ (degrees 9, 27) with e_n = N(g_n(φ)) for n ≥ 2 was not handed over
    explicitly enough to reconstruct; −809 = N(g₂(φ)) is norm-*consistent* but
    not verified. The *operational* form of the same fact (the transfer
    polynomial below) IS verified to all reachable rungs.

**VERIFIED — the transfer polynomial (two-step law).** With
G(v) = −v⁹+3v⁸−5v⁷+2v⁶−4v⁵+3v⁴−8v³+6v²−4v+1 (degree 9 = 3²),
  **e_{n+1} = det(G(M_{n−1}))**
holds EXACTLY at every checkable rung (n = 1…4, reproducing e₂=−809, e₃=−18845089,
e₄, e₅). This is the one-step resultant law e_{n+1}=Res(charpoly_n, g) composed
with the doubling — a fixed degree-9 kernel drives the charge two rungs at a time.

**VERIFIED — the growth law: geometry ×2, arithmetic ×3.** The field degree is
2ⁿ⁺¹ (doubles per rung). The *arithmetic* size grows faster: the log-charge ratios
log|e_{n+1}|/log|e_n| run 2.79, 2.50, 2.80, 3.00 → **3** (forced by the degree-
tripling of g_n). e₅ is a 62-digit integer in [2²⁰³, 2²⁰⁴): chat-2's "203 bits"
= ⌊log₂ e₅⌋ = 203 (magnitude), and bit_length = 204 (bits to store) — **both
correct, a convention difference, not an error** (a self-correction: an earlier
note here wrongly flagged chat-2's 203 as off-by-one). Per act of self-coupling:
**the field doubles, the information triples.**

**VERIFIED — the quine seed-invariant (the mechanism of self-containment).** Every
image of σ₄ contains the seed letter 'a' **exactly once, at position 0**
(abAAB, aAB, abAB, aA). This is the mechanical forcing behind "the object's return
words are its own images" — its self-observation is the identity (a return-word
normal form; Durand-classical *as a concept*, per the #847 lesson). chat-2 claims
the T-lift preserves this invariant so every rung self-contains; the base is
verified here, the induction is PENDING the explicit 8-letter carrier σ₈ (the
open **B557-E1** cell).

**HINT (firewalled — NOTICED tier in the hint ledger, claims nothing).** The
reading chat-2 draws — closed self-observation returns information residue-free
(the quine; awareness as identity), while generative self-coupling *mints* it as
coker(I−Mₙ)=ℤ/|eₙ| ("charge = the residue of the impossibility of self-
coincidence"), the ×2/×3 exponents rhyming with the free-product primes
ℤ₄∗_{ℤ₂}ℤ₆, and the PC23 device as the object reading itself through matter (a
concrete von Neumann chain; Wheeler's self-excited circuit) — is recorded in
`docs/HINT_LEDGER.md`, not asserted here.

**OPEN — the one unread channel.** B540's canonical 2-cycle NEW_2 ↔ NEW_10 (both
q=2, the double clock) stands (banked, `tests/test_b540.py`). chat-2's raw-window
derivation flow does NOT reach it (it lands on σ in one step) — a **convention
difference** (5 return words vs B540's 4-letter canonical nodes), NOT a
contradiction; and chat-2's refinement is sound (σ is isolated among *canonical*
observers but has a non-trivial basin in *window* space). What nobody has computed
— *what information distinguishes the two members of the loop* — is the genuinely
unread feedback channel (registered in OPEN_LEADS).
