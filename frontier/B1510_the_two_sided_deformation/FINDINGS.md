# B1510 — THE TWO-SIDED DEFORMATION: the 16's and the 16*'s singlets switched on together hold in the bulk without a source, push it onto the end, and count zero

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Verdict:** PROVED. The theorems were proved at the seal; the sealed
run reads D1–D6 as decided, P1–P4 YES and P5 NO. · **Price:** unchanged, 0 of 19 · **Seal:** `PREREGISTRATION.md`
(sha256 6010649413df2ade5d4fe0760b7dae29c8cdfa1a2ae12b0a2d714ee05d5786a3), committed and pushed at 0cb24e2b before the run.

## 0. Seen from above

B1509 switched on one singlet direction at a time on the audit lane's harmonic vacuum. Write ρ₀ = A ⊕ 1, with A = μρ_q (Ballas'
projective holonomy of m004 with a central twist).
- The 16's singlet c gives index −1 at μ = −1: one 10′.
- The 16*'s singlet c* gives +1.
- A one-sided extension is F-flat but not D-flat, so it needs a source.

This arc switches both on together, ρ_ε = (I + ε(s U_c + t U_{c*}) + …)ρ₀ with s t ≠ 0. It reads the result at the six points over
three primes, and exactly at order two. The answer is in four parts.

1. **In the bulk it holds without a source.** The free-end two-sided deformation exists to order 10 at all 18 point–prime pairs (P1).
   Every member with s t ≠ 0 is absolutely irreducible (Corollary A″), so its orbit is closed. Every sl(4) obstruction vanishes at
   every order (Theorem A, with Lemmas R and C). The only obstructions live in H²(A) ⊕ H²(A*), and at each odd order the free
   classes reach them along one line, which the obstruction lies on (P2).
2. **The source moves onto the end.** With the cusp holonomy held fixed, the deformation is obstructed at order two at all 18 pairs
   (D4).
   - The fixed-end class is the audit lane's F15 matter-retention row. In R56's language it is the F-term F_S = λ Q·Q̃ of the
     neutral q-mode, sourced by the singlet pair (Proposition F).
   - So the pair holds only if the end moves at second order.
3. **The trivial line can keep its cusp eigenvalues (1, 1) only at the double root.**
   - At ±i the line's longitude moves at order two, by s t κ̂_ℓ with κ̂_ℓ ≠ 0, so there is no chiral branch (D3, D5, Theorem B).
   - At μ = −1, where κ̂_ℓ = 0, a chiral branch exists to order 10 at all six pairs (P3).
4. **It counts zero.** Main's index is 0 on every two-sided deformation (Theorem C: upper semicontinuity of H², the Euler
   characteristic and the annihilator identity). It is 0 on every branch computed (D6).
   - On the chiral branch the data are (a1, b1, r1, q1) = (1, 1, 1, 1).
   - The pair is vector-like. B1509's 10′ belongs to the one-sided extension alone.

**The surprise (P5 NO).** At μ = −1 the instrument's free-end branch keeps the line's longitude at exactly 1. This holds through
order 10 in the sealed run and through order 14 post-run; only the meridian's eigenvalue moves.
- The cause is the branch's adjoint direction. It is the tangent of Ballas' q-family (post-run (d)).
- On the plane spanned by q and one more adjoint class, the order-four longitude condition is proportional to the odd obstruction.
- A free-end branch built on the third adjoint class moves the longitude at exactly order four, as P5 expected for a generic branch.

## 1. Setting

As in `PREREGISTRATION.md` §1:
- π = ⟨m, n | mnMNmNMnmN⟩, with ℓ = nMNmmNMn;
- the six points (17 ± 12√2, −1) and (7 ± 4√3, ±i);
- gl(5) = gl(4) ⊕ A ⊕ A* ⊕ F under Ad ρ₀;
- deformations ρ_ε(g) = (I + Σ ε^k U_k(g))ρ₀(g) with U₁ = s U_c + t U_{c*};
- line eigenvalues λ_m, λ_ℓ by the Schur fixed point;
- main's index over F((ε)) from ranks alone (`deform_lib.index_laurent`).

## 2. The theorems (proved at the seal; proofs in PREREGISTRATION §3)

- **Lemma 0.** H²(π; F) = 0, so H²(π; gl(5)) = H²(sl(4)) ⊕ H²(A) ⊕ H²(A*). The run reads the coker blocks sl(4)³ + A + A* at
  every pair.
- **Theorem A (the sl(4) obstructions vanish).** Cusp rigidity (R) and a regular cusp pair (C) make every sl(4) obstruction vanish at
  every order. The obstruction is seen by the cusp (duality), and the cusp's commuting variety is smooth there.
- **Lemma R.** (R) holds, from F15/R55's data: h¹ = 3, and the meridian restriction has rank 2 with kernel q. The q-tangent moves
  tr ρ_q(ℓ) = 3q + q⁻³.
- **Lemma C.** (C) holds: the meridian has Jordan type (3, 1), and ℓ separates V_q from V_{q⁻³}.
- **Corollary A″ (irreducibility).** s t ≠ 0 gives an absolutely irreducible deformation, with a closed orbit.
- **Theorem B (the longitude at order two).** λ_ℓ = 1 + s t κ̂_ℓ ε² + O(ε³), with κ̂_ℓ = ±⟨e ∪ c, c*⟩. It is zero iff e ∪ c = 0,
  iff the fibre monodromy has a Jordan block (B1509 T3), that is, exactly at μ = −1.
- **Proposition F (the fixed-end class).** The sl(4) part is the triple product τ(a) = ⟨[a ⌣ c], c*⟩; it is nonzero by F15. The line
  part at ℓ is s t κ̂_ℓ, and the block trace at ℓ is −s t κ̂_ℓ.
- **Theorem C (the count is zero).** If W_ε deforms A ⊕ 1 with a0 = b0 = 0, then I(W_ε) = 0, a1 = b1 ≤ 1 and r1 = q1 = t0. If the
  line keeps (1, 1), then a1 = b1 = r1 = q1 = 1.
- **Theorem D (parity; the shifted longitude condition).**
  - The order-k coefficient of λ_ℓ does not depend on U_k.
  - The order-k choice moves the order-(k + 1) coefficient only through (s δt + t δs) κ̂_ℓ.
  - So at μ = −1 the condition is imposed one step earlier.
  - *Correction of a descriptive sentence (post-run (b)):* the order-(k − 1) choice enters through the adjoint classes' trilinear
    term *and* through the twist. The centre, c and c* do not enter. The theorem's proved content is unchanged.

## 3. The sealed run against the predictions

`verification/two_sided.py --sealed --record` → `verification/two_sided_run.txt` (64 s). The banked identity passed first: B1509's 54
index rows, reproduced through this arc's own F((ε)) index.

| | Prediction | Result |
|---|---|---|
| D1 | h¹(sl(4)) = 3, restriction injective, h⁰(T; gl(4)) = 4 | **holds** at all 18 (h¹(gl(5)) = 7, Z¹ 30, B¹ 23; restriction rank 3) |
| D2 | order-two obstruction zero | **holds** at all 18 mod p and at all six exactly |
| D3 | κ̂_ℓ = 0 exactly at μ = −1 | **holds**: 0 at the six μ = −1 pairs and at both exact points; nonzero at the twelve ±i pairs and at all four exact ±i points (e.g. 1024 + 1024√3 − 4096√3 i at (7 − 4√3, i), for B1509's cocycle normalisation) |
| D4 | o_rel,sl = 1; line part κ̂_ℓ; block trace −κ̂_ℓ | **holds** at all 18 (e.g. 427 and 582 = −427 mod 1009) |
| D5 | no chiral branch at ±i | **holds**: the chiral solver stops at order two at all twelve ±i pairs |
| D6 | I = 0 on every branch; a0 = b0 = 0; r1 = q1 = t0; chiral (1, 1, 1, 1) | **holds** for I, a0, b0, r1, q1, t0 at N = 8 and 10 on every branch. The chiral (1, 1, 1, 1) holds at N = 8. At N = 10 the chiral jet's own edge gives (a1, b1) = (0, 0) with r1 = 1, impossible for a module; it is a truncation artifact (§4 (a); §7) |
| P1 | free-end branch to order 10 | **YES** at all 18 (relator to order 10, det = 1, parity-symmetric) |
| P2 | odd obstructions nonzero, on one line, solvable | **YES** at all 18: at order three A and A* are both nonzero; the rank is 1 on A and 1 on A*. The total is 2 with the det row, whose only column is the centre, so the odd rows together have rank 1. At ±i the twist lies on the same line (it was the column chosen) |
| P3 | chiral branch at μ = −1 to order 10; rank 4 at step three | **YES** at all six μ = −1 pairs (relator, det, λ_m ≡ λ_ℓ ≡ 1 to order 10); rank 4 |
| P4 | a1 = b1 = 0 on the free-end branch | **YES** at all 18, N = 8 and 10 |
| P5 | at μ = −1 the free-end branch's λ_ℓ − 1 has valuation exactly 4 | **NO**: λ_ℓ ≡ 1 through order 10 on the instrument's free-end branch at all six pairs (through order 14 post-run); λ_m moves at order 2 |

## 4. Post-run checks

`verification/post_run_checks.py` → `post_run_checks_run.txt` (about 70 s). No sealed reading rests on these, and none is changed.

- **(a) The chiral index at the edge.** The chiral branch was solved to order 12 and read from that one jet.
  - At N = 8 and N = 10: (a1, b1, r1, q1) = (1, 1, 1, 1), I = 0, with precision 8 and 10 left.
  - At N = 12, the new edge, the impossible (a1, b1) = (0, 0) with r1 = 1 reappears, its pivot at valuation 12.
  - So the last orders of a jet still carry free choices that later orders fix, and a rank read at the jet's own order is not a
    rank of any continuation.
- **(b) What moves the line at step three (μ = −1).**
  - The order-four longitude condition is moved by all three adjoint classes and by the twist. c, c* and the centre do not move it.
  - The order-two meridian condition is moved by the centre (+1) and the twist (−4).
  - The longitude row is not proportional to the odd-obstruction rows on (the adjoint classes, the base): the rank is 2.
- **(c) The free-end branch continued to order 14.** At all six μ = −1 pairs, λ_ℓ ≡ 1 through order 14. The twist is never chosen.
- **(d) The free-end branch's adjoint direction.**
  - The tangent of Ballas' q-family is a cocycle. Modulo coboundaries it is a multiple of the solver's first adjoint class, with
    zero on the other two.
  - The 2 × 2 minors [longitude; odd obstruction] × [class; base] are zero for q and for the second adjoint class, and nonzero for
    the third.
  - The free-end solver rerun with the adjoint classes reordered gives:
    - starting from the second class, λ_ℓ ≡ 1 through order 8;
    - starting from the third, λ_ℓ − 1 has valuation exactly 4.

  So the instrument's free-end branch is the q-direction branch, and P5's expectation holds on a generic branch, not on this one.

## 5. The physical reading

**Holding without a source.**
- In the bulk the singlet pair is an honest flat deformation:
  - irreducible, with a closed orbit (Corollary A″);
  - F-flat to order 10 at every point (P1);
  - D-flat by Corlette–Donaldson, for any genuine member, because it is semisimple.
- The source B1509 needed for one singlet is not needed in the bulk for the pair.
- The price is at the end. The fixed-end class is nonzero (D4): with the end's finite-norm data held fixed, R56's cubic gives
  F_S = λ Q₁Q̃₁ ≠ 0, and the pair sources the neutral q-mode.
- With the end free, the cusp holonomy moves at second order, by the class o_rel. So the source does not disappear: it is moved onto
  the end. The end's law (sL-8) decides whether that is allowed.

**The count.** Zero. In four-dimensional language, the 16's and 16*'s singlets pair, and a singlet with its conjugate partner is
vector-like (Theorem C).
- The necessary condition for a nonzero index on an irreducible module, that the line keeps (1, 1), is met on the chiral branch at
  μ = −1 (P3).
- Upper semicontinuity still forces r1 = 1 and I = 0.

So on this family the two-sided direction is not a route to chirality. The only nonzero counts remain B1509's one-sided extensions.
Their 10′ count is the end's (0, 1 or 2), and they need a source.

**The q-direction branch.** At μ = −1, the deformation that moves the projective structure along Ballas' own family keeps the trivial
line's longitude eigenvalue at 1 (§4 (c), (d)). Its meridian eigenvalue moves only because det = 1 brings in the centre. This is
observed to order 14, not proved (lead 1).

## 6. What this establishes, and what it does not

**It establishes the following.**
- Theorems A–D, Lemmas R and C, Corollaries A′ and A″, and Proposition F, proved.
- The formal two-sided deformation to order 10 at all 18 point–prime pairs, with det = 1 and parity.
- The fixed-end obstruction, identified with F15's row and R56's F-term.
- The chiral branch at μ = −1 to order 10.
- Main's index 0 on every branch computed, as Theorem C requires.
- The q-direction branch's longitude to order 14.
- The sweep for this claim (PREREGISTRATION §5.1) covered main 6085218c, this branch, the audit lane f7cdf281 and the paper-review
  lane 5d58b935. No two-sided deformation of A ⊕ 1, its chiral branch, its fixed-end class or its index appears there.
  - F15 has the matter-retention rows.
  - R56 has the cubic.
  - Main's B1440 bounds |I| ≤ 1 here.

**It does not establish the following.**
- Existence to all orders, or of an analytic family. The formal statement is to order 10, or 14 for the q-direction branch.
- A finite-energy background, or the end that absorbs o_rel.
- A selection of q, μ or the end condition.
- A 5̄′.
- **I-26 stays UNEARNED. 0 of 19.**

## 7. Record and disclosures

- **Order.**
  - `PREREGISTRATION.md` was committed and pushed at 0cb24e2b, with the instrument and `controls_run.txt`.
  - The sealed run started after the push and was recorded as `two_sided_run.txt`.
  - The post-run checks were written after the record.
- **Before the seal.**
  - Controls C0–C6 (C6 caught a transposed product in the adjoint-basis routine).
  - The meridian's Jordan type.
  - The sweep found F15 and R55 deciding two items an earlier draft carried as open. All of this is listed in the preregistration.
- **A reading-rule slip.** The preregistration read the index at N = 8 and N = 10 from the order-10 jet. N = 10 is that jet's own
  edge, where the last free choices are not yet fixed by later orders.
  - The sealed reading is recorded as is.
  - Post-run (a) shows (1, 1, 1, 1) at N = 8 and 10 from an order-12 jet, with the artifact moving to N = 12.
  - Rule from now on: read a jet solved to order N at orders ≤ N − 2, and check r1 ≤ a1 and q1 ≤ b1 before reading any index.
    ERROR_LEDGER row.
- **P5's premise.** P5 assumed a generic free-end branch. The instrument's branch moves the base point along the solver's first
  adjoint class, which is Ballas' q-tangent, and that branch is special. Recorded as NO; the expected behaviour was shown on a
  generic branch post-run.
- **Theorem D's descriptive sentence.** The twist enters too (§2). This is a correction of wording, not of the theorem.
- **Self-caught at design time.**
  - The first sweep brief named the wrong branch for the audit lane. It was redirected before the seal, and the right branch was
    read directly.
  - Heusener–Porti's component labels were recalled swapped. They were corrected from the source before the preregistration was
    written.

## 8. Leads (registered, not run; each sealed before computing)

1. **The q-direction longitude.** Prove that the two-sided branch along Ballas' q-tangent keeps λ_ℓ ≡ 1 to all orders at μ = −1. Find
   the reason for the proportionality on the plane (q, second class): perhaps the cusp type is preserved along Ballas' family.
2. **All orders at μ = −1.** Prove that the odd obstruction always lies on the τ-line, and so that the free-end and chiral branches
   are unobstructed. A gradient (Chern–Simons) structure on the boundary-acyclic blocks is the candidate.
3. **The end that absorbs o_rel.** Which cusp data move at second order? Does an end with R70's fixed-period law, or this seat's
   B1500–B1505 models, accept the move?
4. **The 5̄′.** Unchanged from B1509 lead 2.

## Verification

- `verification/two_sided.py --controls` → `controls_run.txt`: pre-seal; about 6 s.
- `verification/two_sided.py --sealed` → `two_sided_run.txt`: the sealed run; 64 s.
- `verification/post_run_checks.py` → `post_run_checks_run.txt`: post-run; about 70 s.
- `verification/deform_lib.py`: the library (formal families, line eigenvalues, the F((ε)) index).
- Lock: `tests/test_b1510_the_two_sided_deformation.py`.
