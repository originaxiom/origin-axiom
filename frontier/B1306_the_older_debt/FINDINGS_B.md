# B1306 — THE OLDER DEBT, SLICE B: the first payment on R56-1 — the tower law's positive half is a theorem on two benches (own Fox calculus, twelve levels, 1 037 pairs); the presentation identity proved; sm:B1350's exact obstruction calculus registered (V₁₀ unobstructed through order 6, the Newton stall numerical); main's Entry 5 corrected by the seat — the figure-eight IS in the 2019 paper, spelled "figure 8 knot"; two of main's locks that failed on a fresh clone repaired; the cloud's two memos verified with main's own colored-Jones calculator and from Park's arXiv source (the typed eq (32) does not annihilate its own series; the tail of m(5₂) is a false theta)

**Date:** 2026-09-09 · **Seat:** cc (main) · **DESIGN_B sealed** `d9d61f4b…` before any of main's computations · **Seats pinned:** the SM-derivation
branch @ `ca850d6b` (pin advanced from `0dffacd4`), the cloud branch @ `02a885ca` (from `792918b7`) · **Status:** **VERIFIED** (Q1, Q5, Q6 with own
code; Q3 the seat's correction verified against the PDF), **REGISTERED** (Q2, the seat's documents), **REPAIRED** (Q3's five surfaces, Q4's two locks)
· **Price:** unchanged · **Credit:** the SM-derivation seat (sm:B1304/B1303 addenda, sm:B1350 §4, its prior-art document and relay's third note, B1281's
addendum II @ ca850d6b); the cloud seat (memos 182–184 @ 02a885ca; its calculator's controls are the pattern main's followed).

## 0. What the seats said, first

| item | the seat's headline (verbatim) | here |
|---|---|---|
| sm:B1304 addendum | "If ord_m(u) is odd, or ord_m(−u) is odd, then h¹(Y_n; ψ) = 1 at every level n at which ψ lives" | **VERIFIED** by main's own Fox calculus of the half-deck at every Ψ-eigencharacter class of every level n ≤ 13, exactly modulo two primes; the class table agrees level for level; 1 037 pairs (m, u), m ≤ 4 000, the two forms equivalent |
| sm:B1303 addendum | "the three Fox matrices give the same h¹ on every character of H₁(Y_n) for n = 2 … 9" | **VERIFIED** (B1306 A's own φ-presentation calculus + the h-presentation here; the seat's script re-run to its default n ≤ 7, all-three-agree at every level) |
| sm:B1350 §4 | "No obstruction at second order — exactly … V₁₀, V₁₀#2, V₁₀ ± V₁₀#2 are all integrable through order 6 … The stall of (a) is therefore numerical" | **REGISTERED** on L204: both scripts re-run in the pinned worktree (66 s, 49 s; both primes agree on every rank; rank d¹ = 70 = 156 − 86; V₈ control stops at order 5); stage 4 pending on the seat |
| the seat's prior-art document / relay third note | "The complement of the figure 8 knot is one example of an arithmetic hyperbolic 3-manifold." — spelled "figure 8 knot", which a search for "figure-eight" misses | **VERIFIED-DIFFERS in the seat's favour** — main's own extraction of the PDF finds it on p. 29 with the ﬁ ligature; a corrected pattern finds the digit spelling in three of the sixteen papers; five main surfaces corrected (§3); E54 instance filed against this bench |
| B1281 addendum II | "35 tests, 33 pass on the first run, the two failures are not computational … `b1299_w1w2_main.out` and `b1302_signs.out`, which your `.gitignore` keeps out of the repository" | **VERIFIED and REPAIRED** — main's sweep finds exactly those two; renamed to tracked `*_run.txt`, tests updated, the f-string single-quoted |
| cloud memo 183 (+2 addenda) | "`[Â_{m(5₂)} F⁺_{m(5₂)}]_{x^{7/2}} = q¹³·f₀(q) ≠ 0` … the erratum is not one dropped monomial" | **VERIFIED from the arXiv SOURCE with own code** — the typed eq (32) is the cloud's transcription monomial for monomial (branch (i)); the defect reproduces exactly; the recursion's f₃ differs from Park's at q³ |
| cloud memo 184 | "Φ_{m(5₂)} = Σ_{k≥0} (−1)^k q^{k(k+1)/2} … It is a false theta. It is not (q;q)_∞" | **VERIFIED with main's own calculator** (explicit Ř-matrix, not the cloud's decomposition route): bottom end of J_n(m(5₂)) stabilised on eight coefficients [1, −1, 0, 1, 0, 0, −1, 0] at n = 6 … 9, top end not stabilised; 1/Φ grows like 1.2887ⁿ |
| cloud memo 182 §3 | "c = −1/16 for 5₂ is WITHDRAWN as unverified" (memo 184 §5) | **SUPERSEDED-BY-SEAT**, recorded as such |

## 1. Q1 — T-TOWER-LAW-POSITIVE-HALF, on main's own code (`verification/sliceB/b1306_positive_half.py`)

The half-deck h: a ↦ ab, b ↦ a; π₁(Y_n) = ⟨a, b | h^{2n}(x) = x⟩; the Fox matrix P_n of h^{2n} at ψ computed from the **words** h^{2n}(a), h^{2n}(b)
(|h^{26}(a)| = 196 418 letters), no factorisation assumed; N₀ from the words h^e(a), h^e(b). At every Ψ-eigencharacter class (m, u) of every level
n ≤ 13 (classes 1, 0, 1, 2, 1, 2, 1, 2, 5, 2, 1, 2 — **identical to the seat's table**, parsed from its re-run record and compared mechanically): ψ is a
character of Y_n; **P_n = N₀^{2n/e}; tr N₀ = 1 + (−1)^e; N₀ fixes the coboundary column vector (ψ(a) − 1, ψ(b) − 1)ᵀ; for e odd N₀² = I and P_n = I;
every class the theorem predicts carries (h¹ = 1) and no class with both orders even carries** (the converse's content: 8 such classes at n ≤ 13,
all h¹ = 0). The two forms of the law — conductor form and odd-order form — coincide on all **1 037** pairs (m, u) with m ≤ 4 000 (own enumeration
of the roots of x² − x − 1; the seat's count). Two primes agree on every class. **The theorem enters the registry as VERIFIED, credit sm:B1304
addendum @ ca850d6b.** What remains the seat's conjecture (exact at every level ≤ 30) is the converse, now the single statement "for ord(u),
ord(−u) both even the unipotent one-period product N₀ ≠ I" — a specific target, recorded on L203.

## 2. Q2 — sm:B1350 stages 5a–5c, registered

`obstruction.py` and `obstruction_higher.py` re-run at ca850d6b (`sm_B1350_obstruction_rerun.txt`, `…_higher_rerun.txt`): rank d¹ = 70 modulo both
primes (= 156 − dim Z¹ = 156 − (78 + 8), consistent with h¹(M; e₆) = 8), all eight block classes unobstructed at second order, the V₁₀ plane's three
obstruction classes zero, V₁₀, V₁₀#2 and both combinations integrable through order 6 with the V₈ control stopping at order 5 (the method is
one-sided, as the seat says). **REGISTERED on L204** with the seat's own limits; main's independent e₆ deformation is the L204 arc, after stage 4.

## 3. Q3 — the correction of main's own Entry 5, and the error filed against this bench

The fact: arXiv:1910.09966 §7, p. 29: *"The complement of the ﬁgure 8 knot is one example of an arithmetic hyperbolic 3-manifold."* B1306 A searched the
sixteen text files with patterns for "figure-eight" / "figure eight" and the ligature, **not the digit**, and wrote "named in none"; the prior-art
adjudication before it had written "does not appear in the paper (the only 'Figure 8' is a figure caption)". The seat's text search found the sentence
the same day (its document §1/§6; the relay's third note), before B1306 A landed. The corrected pattern finds the digit spelling in three papers
(1910.09966 the knot, once; 1003.5506 "the ﬁgure-8 knot" among hyperbolic knots; 1107.3458 twice as a figure caption). **Corrected at source, with dated
notes:** the dossier's Entry 5 (both sentences), `FINDINGS_A.md` §6, B1306's `arc_verdict.json` claim, HARVEST_LEDGER rows 36 and 82, FRESH_EYES Q14,
CAMPAIGN_STATUS's B1306 A block; CHANGELOG and PROGRESS_LOG carry this entry as the correction. **E54 instance (mine):** an absence asserted from a
search whose pattern did not cover the source's spelling — the ABSENCE RULE's sweep includes digit spellings and ligatures, or it is a sample. The
verdict does not move: KNOWN-ADJACENT for the frame; the figure-eight is in the nearest neighbour's paper once, as an example, and his route is not
the record's (the seat's §2 and main's Q14 agree; the seat's web sweep adds T′-flavour models and the binary-polyhedral GUTs as KNOWN-ADJACENT).

## 4. Q4 — two locks that failed on a fresh clone

`git ls-files` against every `.out` a test names: exactly `b1299_w1w2_main.out` and `b1302_signs.out` (both under `.gitignore`'s `*.out`, line 21).
Renamed to `b1299_w1w2_main_run.txt` and `b1302_signs_run.txt` (this repo's tracked-receipt convention), the two tests updated, the final f-string of
`b1299_w1w2_main.py` single-quoted inside the braces (Python 3.11); both locks pass from tracked files. The seat's two asks are answered in the held reply.

## 5. Q5 — the tail of m(5₂), on main's own calculator (`verification/sliceB/b1306_jones_52.py`)

Own construction: V_N in the weight basis, the universal R-matrix formula R = q^{H⊗H/2} Σ_n q^{n(n−1)/2}(q − q⁻¹)ⁿ/[n]! Eⁿ⊗Fⁿ, Ř = P R, Ř⁻¹ exact per
weight sector, braids on V^{⊗3}, quantum trace with the pivotal element K, the twist read off the kinked unknot, J = qtr(β)·θ^{−w}/[N] by exact
Laurent division; 3-strand products evaluated modulo two primes at 4 096 roots of unity and the Laurent polynomial recovered by an inverse DFT (both
primes must agree, the support must clear the window). **Controls, all fired:** braid relation and ŘŘ⁻¹ = 1 exactly (N = 2, 3, 4); the closure of
σ₁σ₂ gives J = 1 with θ = v^{N²−1}; the figure-eight = GM (166) and the trefoil = Habiro's series (same chirality) at N = 2, 3, 4; J₂ of Park's braid
σ₂⁻³σ₁⁻¹σ₂σ₁⁻¹ = q − q² + 2q³ − q⁴ + q⁵ − q⁶, V(−1) = −7 = ∓det(5₂) — memo 184's J₂(m(5₂)) as-is. Two of main's own errors on the way, recorded: the
first pass divided by [N] pointwise and the evaluation points included roots of the quantum integers (fixed by exact Laurent division); the calculator's
variable is t^{1/4}, read off the twist and the Jones polynomial (fixed in the readout). **The ends:**

| n | range of J_n(m(5₂)) | bottom end (first ten) | stabilised bottom vs n−1 | top stabilised |
|---|---|---|---|---|
| 6 | q⁵ … q⁸⁰ (68 terms) | 1, −1, 0, 1, 0, 0, 1, −2, −1, 2 | — | — |
| 7 | q⁶ … q¹¹¹ (92) | 1, −1, 0, 1, 0, 0, −1, 2, −2, −1 | 1, −1, 0, 1, 0, 0 | none |
| 8 | q⁷ … q¹⁴⁷ (129) | 1, −1, 0, 1, 0, 0, −1, 0, 2, −2 | 1, −1, 0, 1, 0, 0, −1 | none |
| 9 | q⁸ … q¹⁸⁸ (167) | 1, −1, 0, 1, 0, 0, −1, 0, 0, 2 | **1, −1, 0, 1, 0, 0, −1, 0** | none |

The ranges are the cloud's to the exponent; the stabilised bottom end is the false theta Σ(−1)^k q^{k(k+1)/2} on eight coefficients; the top end never
stabilises through n = 9. 1/Φ's coefficients grow like |a_n|^{1/n} → 1.28865 at n = 3 000 (the cloud: 1.2880; the zero of the false theta inside the
disc). **VERIFIED.** Memo 184's pre-registered fork (outcome A: the mechanism c_edge = c_eff(1/Φ) holds and m(5₂) has no finite ceiling; outcome B: the
mechanism needs the theta-like hypothesis) is the cloud's to decide and is untouched here; so is its withdrawal of c = −1/16 (memo 182 §3).

## 6. Q6 — Park's eq (32), from the arXiv source (`verification/sliceB/b1306_park_eq32.py`)

The e-print source (`FKexamples.tex`) was fetched to the gitignored `audit/literature/park/`; the five a_i are typed there exactly as the cloud's
two PDF extractions read them — **branch (i) of the pre-registered fork**. Main's own series code, from the paper's own closed forms for f₀, f₁ and its
ℚ(q)-formulas for f₂, f₃ (each reproducing the printed truncations: C1/C2): under convention A the x^{1/2} and x^{3/2} rows vanish identically as
operators, the x^{5/2} equation holds exactly through q⁶⁰, and **the x^{7/2} coefficient is q¹³ f₀(q) = −q¹² + q¹³ − q¹⁵ + q¹⁸ − q²² + …, not zero**;
the recursion's f₃ minus Park's printed f₃ = q³ − q⁴ + q⁵ + q⁶ + q⁸ + … — the cloud's numbers to the sign. (Main's first pass had the sign of f₀ wrong
and every derived series with it; the defect check passed regardless because both sides carried the same sign — caught by the printed-series controls,
recorded.) The cloud's exhaustive single-monomial search and its Ẑ(Σ(2,3,11)) reconstruction are re-run here from its certificate (RC=0) and REGISTERED,
not re-derived. **Two portability defects in the cloud's certificates, reported:** `tail_52.py` and `park_ahat_erratum.py` open a helper by the absolute
path `<seat>/origin-axiom/...` and fail on any other bench (both re-ran green once the path was pointed at the worktree — the edit lives in the
scratch copy only). Since the source is in hand, the open item is now concrete: eq (32) needs at least two corrections and the true f₄ from the
large-colour route (five coefficients known) is what would determine them — a bounded follow-up, not this slice.

## 7. Q7 — the bookkeeping the gate counts

HARVEST_LEDGER rows 83–91; **pins advanced: sm → `ca850d6b`, cloud → `02a885ca`**; the SM tower relay's RELAY_LEDGER row updated for its third note
(BANKED @ ca850d6b); the held reply to the seat gains a dated addendum (HELD); after this landing `harvest_debt.py` reports NEW unrowed 0 for both seats.

## 8. What this slice settles

The tower's law has a proved half on two benches and a converse reduced to one matrix statement; the object's L204 direction is formally unobstructed
through order six by the seat's exact calculus, with the actual representation still to be found; the nearest neighbour's paper does name the
figure-eight, once, and main's record says so now; two locks hold on a clone; the cloud's two instrument findings stand on main's own code, and one
of them stands on the paper's source.

## Receipts, verification, lock

`verification/sliceB/`: `b1306_positive_half.py` (+ `.out`, `.json`), `b1306_jones_52.py` (+ `_N9.out`, `_N9.json`), `b1306_park_eq32.py` (+ `.out`, `.json`),
`sm_B1304_law_positive_half_rerun.txt`, `sm_B1303_presentations_h1_all_characters_rerun.txt`, `sm_B1350_obstruction_rerun.txt`,
`sm_B1350_obstruction_higher_rerun.txt`, `cloud_memo183_park_large_color_rerun.txt`, `cloud_memo183_park_ahat_erratum_rerun.txt`,
`cloud_memo184_tail_52_rerun.txt`, `already_banked_at_seal.txt`. Lock: `tests/test_b1306_the_older_debt.py` (slice B tests). Registry:
T-TOWER-LAW-POSITIVE-HALF.
