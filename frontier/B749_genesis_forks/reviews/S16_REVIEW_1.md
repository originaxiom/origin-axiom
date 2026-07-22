# S16 REVIEW 1 — Arc B749 (the genesis forks) — Pre-execution design review

REVIEWER: fresh, non-authoring adversarial factual reviewer (GOVERNANCE §16)
NONCE: B749R1-LIVE-3f7a1c88
DATE: Tue Jul 21 23:26:16 CEST 2026
BRANCH: genesis/axiom-chain
SCOPE: PREREGISTRATION.md + MEASUREMENTS.md sealed in ARTIFACT_HASHES.txt v1,
       against philosophy/P019_the_genesis_axiom_chain.md
PROTOCOL: hardened incremental — each check's finding appended immediately after
          it is run; this file is the only trusted channel.

---
## CHECK 1 — Seal integrity: PASS
Recomputed sha-256 (working tree) — all three match ARTIFACT_HASHES.txt v1 exactly:
- fbabd790...f65b63a  PREREGISTRATION.md  (match)
- 33bdf7d8...efe6866  MEASUREMENTS.md     (match)
- efb3a40a...3ee923ba P019_the_genesis_axiom_chain.md (match)
HEAD blob hashes for all three files are byte-identical to the working tree (verified
via `git show HEAD:<path> | shasum -a 256`).
Branch structure matches the recorded base: HEAD = 1e432778 "B749: prereg + measurements
SEALED (v1)" sitting directly on ced69b62 "P019 v2 ... + B749 prereg DRAFT". The seal
commit touches only ARTIFACT_HASHES.txt + MEASUREMENTS.md; PREREGISTRATION.md entered at
the base commit ced69b62 and is unchanged since. Working tree clean apart from the
untracked reviews/ dir (this review's own channel).

## CHECK 2 — Authorization chain: PASS (with one benign observation)
Reservation: origin/main HEAD IS the reservation commit beb74314 "B749 + P019 reserved
(cc3 genesis track; cc = sole merge gate) (#1241)". docs/SEAL_LEDGER.md@origin/main line
270 carries the row: "RESERVED: B749 (cc3 — the genesis fork-computation arc ... branch
genesis/axiom-chain; PR-only, cc = sole merge gate) ... P019 reserved for the chain
document (relay CC3_TO_CC_2026-07-21_genesis_reservation + cc ACK)". beb74314 is an
ancestor of the review branch. Observation (benign): the LOCAL main ref is stale (at
da5f1def, pre-#1239); verification done against origin/main after fetch.
Relay GO: <cc2-seat>/seat-work/relay/CC_TO_CC3_2026-07-21_p019v2_go.md reads
"The owner has approved P019 v2 as committed (ced69b62) — the red pen is CLOSED" and its
GO section unblocks exactly the sequence being executed: "MEASUREMENTS.md fixed per fork →
hash-seal the prereg (§16) → execute B749 → PR to me." The relay independently restates
the sealed priors (F5 FRAGILE Gieseking-parent, F3 half-fragile, F2/F4/F6/F7 ROBUST, F8
no prior) — cross-checked against the sealed docs in Check 3. Ordering is consistent:
relay dated 2026-07-21, seal stamped 23:25:43 CEST same day and cites the GO.
Relay also imposes verify-on-receipt (committed scripts + deterministic seeds + printed
check-lines) — carried into Check 5.

## CHECK 3 — P019 <-> B749 consistency: PASS (two notes, neither a contradiction)
Fork coverage: F2,F3,F4,F5,F6,F7,F8 each appear in (i) the prereg fork list, (ii) P019's
fork table, (iii) a dedicated MEASUREMENTS.md block. F1 is excluded in both (P019 row F1:
"not computable; excluded from B749 by design — A0 stays philosophy"; prereg: "F1 excluded
by design — A0 stays philosophy"); MEASUREMENTS has no F1 block. Sibling objects agree per
fork (F3 m=2 bundle; F5 det −1 mapping torus of [[1,1],[1,0]]; F6 closed bundle of
[[2,1],[1,1]]; F7 non-quadratic-slope Sturmian vs P019's "non-golden, non-metallic (e.g.
transcendental)" — the sealed witness class, transcendental, satisfies both).
Priors: prereg §"Preregistered expectations" and P019's closing block state IDENTICAL
priors: F5 FRAGILE (Gieseking-parent, m004's double-cover parent), F3 half-fragile
(arithmeticity survives; m=1 rests on K009/B313 selectors), F2/F4/F6/F7 ROBUST. F8:
prereg says explicitly "no expectation recorded — genuinely open"; P019's expectations
block simply omits F8 (no prior recorded) — same no-prior state, and the cc relay
confirms "F8 genuinely open (no prior — correct and keep it so)". Priors-not-criteria is
explicit in both: prereg "Expectations are priors to be tested, never criteria; a result
contradicting them is a finding, not a failure"; P019 table header "expectation to test
(not assume)" + "E20 hygiene ... BEFORE B749 computes".
Note 1 (benign): MEASUREMENTS F4 adds a third variant (the swap a→b, b→ab) beyond P019's
two (inert, reversed); P019's F4 sibling column anticipates "conjugate carriers", which is
exactly the swap's expected identification — extension, not contradiction.
Note 2 (benign): F8 uses declared verdict labels GEOMETRY-NECESSARY / GEOMETRY-REDUNDANT
instead of ROBUST/FRAGILE — declared at seal, two-outcome preserved, consistent with the
no-prior status.

## CHECK 4 — Measurement adequacy (MB12): FAIL ON F7 (one false identity in sealed text); F2/F3/F4/F5/F6/F8 PASS
All claims below verified by direct computation (sympy 3.12.1 sandbox; snappy 3.3.2).

F2 — PASS. For det=+1 (the world A6 fixes): |tr|>2 gives real eigenvalues off the unit
circle (Anosov); |tr|<2 gives |eig|=1 (elliptic/finite-order); edge cases verified: tr=+2
=> eigenvalue 1 (identity or parabolic — reducible), tr=−2 => eigenvalue −1 (−I finite
order, or −parabolic) — neither Anosov. So |trace|≤2 ⟺ not Anosov is CORRECT for det +1,
edge cases included. Scope caveat (recorded, not a defect): the criterion is false for
det=−1 ([[1,1],[1,0]], tr 1, eigs φ,−1/φ IS Anosov) — but det −1 is F5's fork, not F2's,
and F2's periodic-word siblings live in the orientation-preserving world.

F4 — PASS. Computed abelianizations (M_ij = count of letter i in σ(j)):
  σ_inert (a→ab,b→b):  [[1,0],[1,1]], det=1  — invertible, but NON-primitive (verified:
    σ⁶(b)=b, no 'a' ever) and fixed word = a·b^∞ eventually periodic (verified by
    iteration) — the stated failure mode ("non-primitive → eventually periodic") is right.
  σ_rev (a→ab,b→ba):   [[1,1],[1,1]], det=0  — the sealed claim "σ_rev det 0 → no mapping
    class" is CORRECT (singular matrix induces no automorphism of ℤ²=H₁(T²)). (σ_rev is
    the Thue–Morse substitution: primitive and aperiodic, so det-0 non-realizability is
    exactly the discriminating failure, as sealed.)
  swap (a→b,b→ab):     [[0,1],[1,1]], det=−1 — realizable; verified P·M_fib·P = M_swap
    with P the letter-exchange, so the sealed hedge "swap = Fibonacci conjugate — record
    as identification" is well-grounded and correctly conditional.

F5 — PASS (construction well-defined AND live-tested). snappy expresses everything the
sealed measurement needs: Manifold('m000') is non-orientable, vol 1.0149416064 (= the
sealed "1.0149…"), and M.orientation_cover().is_isometric_to(Manifold('m004')) returns
True (run live in this sandbox). The det −1 bundle is also directly constructible in
bundle notation: 'b-+R'/'b--R'/'b-+L'/'b--L' all yield vol 1.0149416064 and are isometric
to m000. Execution pitfall worth recording: naive sign-flips of the RL word ('b-+RL',
'b--RL') give a DIFFERENT non-orientable manifold (vol 1.8319311884 = 2·Catalan, NOT
isometric to m000) — the sealed text commits to no specific string, so this is a warning
to the executor, not a defect. Two-invariant rule satisfiable (volume + isometry).

F6 — PASS. H₁(bundle) = ℤ ⊕ coker(A−I) is the standard Wang-sequence formula; for
A=[[2,1],[1,1]] (verified = [[1,1],[1,0]]²; tr 3, det 1), det(A−I) = −1 so coker is
trivial and H₁ = ℤ — formula and instance both correct. Anosov-⇒-Sol via trichotomy is
the standard closed-bundle geometrization statement, computable from tr(A)=3>2.

F3 (side-verified while checking adequacy) — PASS. [[2,1],[1,0]]² = [[5,2],[2,1]], trace 6
(matches sealed). Knot-ness discriminator works: Smith form of A−I = diag(2,2), so H₁ =
ℤ ⊕ (ℤ/2)² ≠ ℤ. Independently confirmed in snappy: Manifold('b++RRLL') (= R²L² = the
silver monodromy) is hyperbolic, vol 3.6638623767, H₁ = ℤ + ℤ/2 + ℤ/2 — matching exactly.

F8 — PASS. The Fibonacci abelianization [[1,1],[1,0]] is SYMMETRIC, so "direct limit under
the substitution matrix" vs "under the transpose" coincide here (the transpose subtlety is
moot). det = −1 (unimodular) ⇒ the limit group is ℤ²; the order comes from the PF
eigenvector (verified M·(φ,1)ᵀ = φ·(φ,1)ᵀ): ordered K₀ ≅ (ℤ², φ-cone) ≅ ℤ[φ] — the
Effros–Shen golden dimension group. Standard, computable, and the two declared outcomes
(being-face recoverable / not recoverable) are both non-vacuous.

F7 — FAIL (one sealed sentence is mathematically false; the core theorem use is fine).
Correct part: "CF eventually periodic iff the slope is quadratic" is Lagrange's theorem,
correctly stated for slopes, and the witness protocol (concrete transcendental slope ⇒
non-periodic CF ⇒ no self-similar generator) is sound; the E-class instrument check is
well-designed.
FALSE part: the sealed sentence "the self-similar locus within Sturmian = quadratic
slopes = exactly the metallic family" asserts an identity that is wrong: the quadratic
slopes STRICTLY contain the metallic family. Verified counterexample: α = [0;1,2,1,2,…]
= √3 − 1 (minimal polynomial x²+2x−2, degree 2 — quadratic), not equal to any metallic
[0;m,m,…] (checked m=1..5 exactly; metallic values are (√(m²+4)−m)/2). The Sturmian
system of slope α IS self-similar (its CF is purely periodic; by CF renormalization the
subshift is substitutive — and α is even a Sturm number, conjugate −1−√3 ∉ (0,1), so the
characteristic word is substitution-invariant in the strict sense). The falsehood
propagates into F7's sealed ROBUST verdict language — "(the family is the self-similarity
locus)" — so executing as sealed would bank a false universal claim: self-similarity
selects the QUADRATIC class, not the metallic family; metallicity requires the further
all-equal-digits condition (T4's actual selector). P019 itself does NOT contain this
error (its F7 row and T4 are clean); the error is confined to MEASUREMENTS.md F7 but is
inside the hash-sealed v1 design. MB12 discriminating power for the chosen witness is
intact; the defect is a false factual identity in verdict-bearing sealed text.

## CHECK 5 — Instrument rules: PASS
cc2's lindep lesson is stated as BINDING in the sealed cross-fork rules (MEASUREMENTS.md
lines 67-70): "every exact field claim double-checked (numeric relation + exact factornf —
cc2's lindep lesson is binding)"; it is also instantiated concretely inside F3(b)
("algdep-verified with residual guard ... coefficient-size-aware thresholds, exact
factornf confirmation"). Two-invariants-per-identification is explicit: "every snappy
identification confirmed by two independent invariants (volume + isometry check, never
volume alone)" — and F5's design already obeys it (volume AND double-cover isometry).
Determinism + printed check-lines for cc's re-execution gate: "all scripts deterministic
with printed check-lines for cc's re-execution gate; verdicts journal-only" — which
matches the relay GO's verify-on-receipt demand (committed scripts + deterministic seeds +
printed check-lines) and the prereg's Conventions section ("every computation
deterministic with declared conventions"; verify-on-receipt via cc's B745 pattern).

## CHECK 6 — Tool preconditions: PASS
python 3.12.1 (exactly as declared in the prereg Conventions), sympy 1.14.0, mpmath 1.3.0,
snappy 3.3.2 — all import cleanly. Bundle notation WORKS: Manifold('b++RL') builds and
gives volume 2.02988321282 (= m004, isometry-confirmed in Check 4). Non-orientable
punctured-torus bundles are likewise reachable ('b-+R' etc. = m000 = the Gieseking, vol
1.0149416064), and the census route Manifold('m000') + orientation_cover() +
is_isometric_to('m004') was executed live and returned True. F5 and F3 are both fully
executable in this sandbox (F3's silver bundle = 'b++RRLL', hyperbolic, vol 3.6638623767).
Only environment blemish: a benign tkinter/plink GUI warning on snappy import (no effect
on computation).

## CHECK 7 — Directory sweep: PASS
frontier/B749_genesis_forks/ contains exactly the three sealed-arc files
(ARTIFACT_HASHES.txt, MEASUREMENTS.md, PREREGISTRATION.md — all git-tracked, no hidden
files, no ignored files) plus reviews/ holding only this review file. No pre-written
verdicts anywhere: a repo-wide grep for B749-adjacent VERDICT/ROBUST/FRAGILE/SEAL-READY
strings hits only the two sealed documents themselves (where ROBUST/FRAGILE appear as
outcome DEFINITIONS, verified by full read in Check 3 — no outcome values recorded), and
no literal "VERDICT" exists in the arc dir outside reviews/. No other B749-named files or
scripts exist anywhere in the repo.

## CHECK 8 — Independent anchors: PASS (two recorded, both verified absent from the arc)
ANCHOR 1 (live clock): `date +%s` -> 1784669758  (= 2026-07-21 ~23:35 CEST, matching this
review's wall-clock; not derivable from any sealed file).
ANCHOR 2 (independent computation): `python3 -c "import snappy;
print(snappy.Manifold('m015').volume())"` -> 2.82812208833  (the 5_2-knot complement — a
manifold uninvolved in B749). Verified by grep that neither value nor 'm015' appears in
any of the three sealed files or ARTIFACT_HASHES.txt (absence-exit=1).

---
## SUMMARY
1 Seal integrity ................ PASS
2 Authorization chain ........... PASS (local main ref stale — verified against origin/main)
3 P019<->B749 consistency ....... PASS (two benign notes)
4 Measurement adequacy (MB12) ... FAIL on F7 (F2,F3,F4,F5,F6,F8 all PASS, verified by computation)
5 Instrument rules .............. PASS
6 Tool preconditions ............ PASS
7 Directory sweep ............... PASS
8 Independent anchors ........... PASS

The single failure: MEASUREMENTS.md F7 (sealed v1) contains the false identity "the
self-similar locus within Sturmian = quadratic slopes = exactly the metallic family",
repeated in F7's ROBUST verdict language as "(the family is the self-similarity locus)".
Counterexample verified in-sandbox: slope √3−1 = [0;1,2,1,2,…] is quadratic (minpoly
x²+2x−2), self-similar (purely periodic CF; a Sturm number), and not metallic. The true
statement is: self-similarity selects the QUADRATIC slopes; the metallic family is the
all-equal-digits proper subfamily, selected only by T4's extremality — which is exactly
the distinction P019's chain depends on. Executing as sealed would bank a false universal
that silently overstates T4's selection. Remedy is one corrected sentence in F7 and a
v2 re-seal; every other premise of the design survives adversarial checking, including
the F5 construction (live-tested end to end) and all stated determinants, traces, H₁
formulas, and the dimension-group computation.

VERDICT: STOP — Check 4/F7: sealed MEASUREMENTS.md v1 asserts "quadratic slopes = exactly the metallic family" (false; verified counterexample slope √3−1 = [0;1,2,1,2,…] — quadratic, self-similar, non-metallic) inside F7's verdict-bearing text; correct F7 and re-seal (v2) before execution. All other premises PASS.
