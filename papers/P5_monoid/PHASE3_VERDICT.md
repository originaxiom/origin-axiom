# P5 Phase 3 — VERDICT: the paper does not stand. The core is prior art from 1993.

cc banking seat, 2026-08-01. Six adversarial lenses, **all six returned FINDINGS: 7 fatal, 28 major,
8 minor.** Gate 5 untouched.

## The decisive finding, verified from the source

**Baake, Grimm & Joseph, "Trace maps, invariants, and some of their applications", Int. J. Mod. Phys.
B 7 (1993) 1527** — `math-ph/9904025`. **I extracted and read the PDF rather than trusting the
reviewer's report.** It contains P5's spine, verbatim:

| P5 claim | BGJ 1993 |
|---|---|
| the object: the endomorphism **monoid** of F₂ | *"the set of homomorphisms becomes a monoid… **We call this monoid Θ₂ = Hom(F₂)**"* |
| **U1** — `(κ−2)` divides `(κ′−2)`, with a per-verb multiplier | **Eq. (2.16):** *"for ϱ ∈ Hom(F₂), one finds `I(F_ϱ) = P_ϱ·I`… called the **transformation polynomial** of ϱ"* |
| **§1** — classification by the Hopf coordinate | *"ϱ is **invertible iff P_ϱ ≡ 1**; ϱ has **nontrivial kernel iff P_ϱ ≡ 0**; ϱ is **injective but not onto iff P_ϱ ≢ const**"* |
| **U2** — the classical floor is toral | *"a homomorphism is induced from **Θ₂ = Hom(F₂) to Mat(2,ℤ)**"* |

**Attribution:** conjectured by **Kolář & Ali**, Phys. Rev. A 42 (1990) 7112; *"proved shortly
after"* by **Peyrière, J. Stat. Phys. 62 (1991) 411**.

> **BGJ's classification is FINER than P5's.** Theirs separates *invertible* from *injective-but-not-
> onto* by the multiplier itself. P5's §1 used `inj + det ±1` for "Aut" — **and three independent
> lenses produced counterexamples showing that is not Aut.**

## My Gate B said "no prior art found." That was wrong, and I can say why.

**The outline's own gate list named "Axel–Peyrière."** Peyrière proved this in 1991. I ran that gate
as a search for *"Axel Peyriere Bellissard Lyapunov exponent random Fibonacci"* — the **spectral/drift**
angle — got nothing decisive, wrote *"the method is classical"* for Gate D, and moved on.

> **The gate named the right person. I asked the wrong question of him.** Searching
> "Peyrière + trace map + substitution + invariant" would have returned this in one query. The
> lit-gate did not fail; **my execution of it did.**

## The other six fatals

1. **Q2's EVIDENCE cell reports a null for a predicate the script never evaluates.** φ_TM is
   cancellation-free, so `|φ^k(w)|_cyc = 2^k|w|` exactly; the guard `m ≤ 4` therefore admits only
   **k ∈ {1,2}**, and **m = 1 — an actual periodic class — is unreachable at every k.** Of 702 (w,k)
   pairs, 234 reach the test, **zero at k = 3..6.** The stated bound "k ≤ 6" is fiction.
2. **Q2 should be CUT, and for a humiliating reason: atoroidality is a three-line theorem sitting
   inside the row's own reproducer.** Cancellation-free ⟹ length strictly doubles ⟹ `φ^k([w]) = [w]`
   is impossible. **Proved, unbounded.** A bounded search offered as evidence for that is *"a weaker
   restatement of a theorem the author had in hand and did not notice."*
3. **Stratum 1 ≠ Aut.** `ψ: a↦a, b↦b[a,b]` has det +1, is injective, is **not** surjective, and
   `κ′ ≠ κ`. Independently: `a↦a, b↦bab⁻²`, det −1, injective, `κ = −2 → κ′ = 178`. **The κ′ = κ law
   is a law of Aut(F₂), not of "injective + det ±1"** — and a control confirms the Nielsen generators
   do preserve κ, so the test discriminates.
4. **The "κ-law" column is not a function of the stratum.** Inside stratum 2, `a↦a²,b↦b²` gives
   `x²y²` but `a↦a³,b↦b³` gives `(x²−1)²(y²−1)²`. Inside stratum 3, TM gives degree 3 and
   `a↦a²b, b↦ba²` gives degree 8. **The header says "exact"; §2 already calls it per-verb.**
5. **§2's "projections (3), constants (4)" is false AND self-refuting.** Both citizens abelianize to
   `[[1,1],[1,1]]` — *that is §2.2's own witness pair*. A rank-1 matrix acts as a projection, never a
   constant; and if the sentence were true it would **refute §2.2 outright.** *"Twenty lines separate
   a claim from its own refutation."*
6. **§2.2's consequence is broader than the witness supports.** By the Hopf dichotomy,
   **det ≠ 0 ⟹ injective**, so the Hopf coordinate *is* a function of the abelianization off det 0.
   Strata 1, 2/2′ and the block {3,4} **are separated downstairs, by det — a toral invariant.** The
   witness licenses exactly one sentence: **the 3-vs-4 cut is not toral.** *(I had computed
   "det 0 is forced" myself and drew the opposite moral from it.)*
7. **The witness sits outside Gate E's collision zone.** **SL₂(ℕ) consists of det-1 matrices**, and
   the witness pair's shared abelianization has **det 0** — not in that monoid at all. So *"free
   generation of SL₂(ℕ) cannot distinguish 3 from 4"* is **vacuously true**. In the region where
   End(F₂) and Stern–Brocot actually meet (det 1 ⟹ injective), **the Hopf coordinate is constant and
   separates nothing.** The reviewer supplies a working replacement — `id` vs `a↦a, b↦b[a,b]`, both
   abelianizing to the identity — where **the live invariant is SURJECTIVITY, not injectivity.**

## And the artifact certifying the load-bearing sentence was VACUOUS — mine

`hopf_separation.py` **computed nothing.** `TM` and `S4` were built from the *same literal argument*;
the words `ab`/`ba`/`ab` were never parsed; `same = (TM == S4)` was **true by construction**. The
"injectivity witness" was two hardcoded tuples compared for inequality. The "kernel witness" was a
`print` of the string `-> True`.

**The values are correct — the reviewer recomputed them — but the script supplied zero evidence.**

> **This is MB12 vacuity, in the artifact certifying the sentence the paper says everything rests on,
> written by the seat that spent this entire session cataloguing MB12 vacuity.**

**It is worse in the bank:** `verify_monoid.py`'s `s4_kernel = ((A_*B_)*((A_*B_)**-1)).is_identity`
is **True for every element of every group** and never mentions the endomorphism. That is a **banked**
reproducer, green in `tests/test_b497_monoid.py`, certifying nothing.

## Verdict

**P5-monoid is not a paper.** Its classification, its two universal laws, and its object are
Baake–Grimm–Joseph 1993 after Kolář–Ali 1990 and Peyrière 1991 — **with a finer classification than
the draft's, which was also wrong about Aut.**

**What may survive, and needs its own gate before anyone writes a word:**
- the **drift ledger** (`E[log mult_D] = −2`, `E[log mult_M] = 0`) — BGJ define the multiplier but do
  not obviously compute its log-expectation
- **Q3**: `BS(1,2) ⊂ G_dec` ⟹ not word-hyperbolic — exact, and untouched by BGJ
- the observation that **det ≠ 0 ⟹ injective**, hence the forgetting is confined to det 0

**B497 and B498 need correction, not just the draft** — the Aut mis-definition and the vacuous
`s4_kernel` are banked.

`tests/test_p5_phase3.py`

## RE-CHECK (2026-08-01, on the owner's challenge) — the verdict HOLDS, and one supporting claim was overstated

The verdict was re-verified against the extracted PDF in both directions — **what died and what
survives** — because a prior-art call that only checks the death half is half a check.

**The classification quote is real and in context.** It sits in a bulleted list of properties of
`P_ϱ`, immediately before *"We cannot give the proofs here, many of which can be found in the work of
**Peyrière** and coworkers."* Eq. (2.16) and the Appendix's (A.1) both state the transformation law.

**But the reviewer's phrase "Eq. (2.16)/(A.1) is U1 plus the multiplier table VERBATIM" is an
overstatement, and I repeated part of it.** Measured in the text:

| P5's specific multiplier | in BGJ? |
|---|---|
| `x²y²` (decimation) | **0 hits** — the word "decimation" does not appear either |
| `x²+y²−xyz` (Thue–Morse) | **not given**; "Thue-Morse" appears **once**, in a *spectral* gap-labelling context, not as a trace map |
| BGJ's own worked multiplier | `P_ϱ = (U_{k−1}(x))²` for their generalised-Fibonacci family |

> **BGJ gives the LAW and one family's multiplier, not P5's table.** The correction does not rescue
> the paper — computing a specific `P_ϱ` from Eq. (2.16) is mechanical, so P5's table is a
> **corollary of prior art**, not new work — but *"verbatim"* was wrong and is corrected here.

**The survival list is confirmed by absence, measured:**

| searched in BGJ | hits |
|---|---|
| Lyapunov · expectation · average · random · Haar | **0 · 0 · 0 · 0 · 0** |
| mapping tor· · Baumslag · BS(1, · hyperbolic · HNN · atoroidal | **0 · 0 · 0 · 0 · 0 · 0** |

> **BGJ contains no probabilistic content and no group-theoretic geometry whatsoever.** The **drift
> ledger** and **Q3** are untouched by it — not by assumption, but by a zero-hit search over the full
> extracted text.

**Verdict unchanged: the spine is prior art.** The object, U1, U2 and the injective/kernel/onto
classification are BGJ 1993 after Kolář–Ali 1990 and Peyrière 1991 — **and BGJ's classification is
correct where §1's was not.** What is not theirs is the drift ledger, Q3, and `det ≠ 0 ⟹ injective`.
