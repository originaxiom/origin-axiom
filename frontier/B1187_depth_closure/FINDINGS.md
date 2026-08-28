# B1187 — L187 THE DEPTH-CLOSURE SITTING: the 7 under-proved kills dispositioned (2 were already closed; 2 close here; 2 extend with corrected instruments; 1 obstruction-route refuted with a census instrument)

**Status: banked (frontier). Verdict PROVED** (the sitting's dispositions, each cell graded
honestly; two full closures earned here, two prior closures surfaced, one blanket-genericity clause
REVERSED on better statistics). Owner's GO on queue row 3. `verification/reproduce.sh` →
`REPRODUCES` (fast path; `OA_SLOW=1` re-runs the full sweeps). Gate 5 clean.

## The registration correction first

L187 was registered (B1172) as "7 EXPOSED kills, named stabilization paths, **none executed**" —
STALE at registration: **B767 (R28-10, 2026-07-23) had already run 6 of the 7** and fully
STABILIZED two. The closure program's Phase-1 record knew this ("B767 already closed B489 and
TOMB-L255"); the L187 row didn't. Corrected here; the queue's row-3 content was really five cells,
not seven.

## The seven dispositions

| cell | disposition | grounds |
|---|---|---|
| **B489** | **CLOSED (was: B767)** | Binet induction: torsion = \|L(2n)−2\| = (φⁿ−φ⁻ⁿ)² > 0 for ALL n — the n≤8 check became an all-n theorem. Verified standing. |
| **TOMB-L255** | **CLOSED (was: B767)** | The polynomial functor theorem: Symᵈ eigenvalues {(−1)ʲφ^(d−2j)} for ALL d. Verified standing. |
| **WALL-7** | **CLOSED-mod-q, all t** (this arc) | dim = 0 for the twisted (f3) intertwiner at **every** t ∈ {1..865}, **all 8 patterns, both primes q = 1009, 1999** (866 = deg-bound+2 points; t=0 is the degenerate straight-weld label, excluded by construction). Plus **a logic error in B767 corrected**: "865 points ⇒ no roots" was wrong as stated — ≥deg+1 nonvanishing points prove D ≢ 0 (generic-t closure, which B767's 18 exact points already gave over K); all-t closure needs root exclusion, achieved here mod two primes (the K-exact route — two-minor interpolation + gcd — is spec'd in the committed script's docstring, named as the remaining exact step). |
| **B685** | **EXTENDED 3×/4×** (this arc) | The v₅(denominator) = 0 kind-mismatch re-verified at object-side depth K = 60 (was 20) and hearing-side n ≤ 240 (was 60), all checks passing; the structural WHY stands (5 inert in ℚ(√−3), Legendre(−3\|5) = −1 — computation lives over ℤ[ω]); full closure still requires the 3-integrality theorem (named, unexecuted). |
| **TOMB-L310** | **RE-SCOPED CLOSURE + a clause REVERSED** (this arc) | The kill stands on its drift-artifact grounds (B189's C2: d_MM tracks truncation level — the hallmark of a graded poset, not a spacetime dimension; the null reproduces the ~4 to within 4%). But the per-level matched-null test (100 seeds/level, new here) **reverses B189's C3 "indistinguishable" clause**: Ω is NOT statistically null — z = (−2.2, −2.8, −2.3, +0.6, **+11.2**) at L = 6..10; at the full poset Ω sits 11σ ABOVE its null (3.936 vs 3.782 ± 0.014, excess transitive reach). The 5-point convergence inference is retired as non-verdict-bearing; the structured deviation is registered as a lead-grade observation (L190). The L11 DAG rebuild is NOT needed for the verdict-bearing claim. |
| **TOMB-L34** | **CLOSED** (this arc) | The N-stability gap closed **on B742's own test design** (the one-cut profile S(L) at fixed N): fitted profile slope a(N) stable across **7 sizes N = 233..4181 × 2 word windows** (big-N range [0.139, 0.210]) with discriminating controls — random word a = 0.022 (10× smaller), periodic a = 0.000. The log class is N-stable, window-stable, and control-separated: the genericity kill is proved at depth. **Two B767 defects corrected**: its "3 seeds" were vacuous (the model is deterministic; RNG was seeded but never drawn), and its estimator c_eff = S/log L conflates the additive constant (S = a·log L + b ⇒ S/log L drifts as b/log L — exactly the 0.64→0.26 "inconclusive plateau" it saw; an estimator artifact, not physics). |
| **B500** | **OBSTRUCTION-ROUTE REFUTED + instrument banked; kill stays PROVISIONAL** (this arc) | The depth-uniform closure route (B502's parity conjecture: interaction-born fields all have 2 \| d_K, which would exclude d_K = −283 at every depth) is **refuted at the signature level**: the mod-2 étale census (new instrument — fixed schemes of all all-three-verb words over GF(16), étaleness by det(J−I) ≠ 0, Frobenius orbits) shows **étale degree-4 closed points are ABUNDANT from depth 5 on** (depth 4: 0 signature words — matching the clean depth-4 hunt; depth 5: 50/150; depth 7: 420/1806; through depth 10). The 2-inert signature the child needs is compatible with the word space, so no cheap mod-2 exclusion exists. The depth-5 kill stays PROVISIONAL as banked, its ledge honestly named; the census doubles as a **targeting instrument** (signature words are where a deeper hunt should look — under the B398 airlock). |

## The sitting's meta-lesson (for the review)

Three of the five executed cells turned on **instrument defects in the prior stabilization pass**
(the vacuous seeds, the wrong estimator, the no-roots logic error) — and one banked clause
("indistinguishable from null") **reversed under better statistics** (30 → 100 seeds, per-level).
The depth-closure backlog was as much about re-verifying the verifiers as extending the data — the
same class as B1186's one-sided control. Verify-the-verifier belongs in the next review's checklist
alongside cc3's verified-vs-used sweep (B8151).

## Fences

WALL-7's all-t closure is mod-q (two primes); the K-exact all-t route is specified, not executed —
over K the proved statement is generic-t (B767's exact points) + all-t mod 1009 and 1999. B685's
closure remains conditional on 3-integrality (extension is evidence, not proof — the E22 lesson
applied to ourselves). The B500 census's exclusion power is bounded by the index caveat (2 dividing
a coordinate-order index can hide inert behavior), stated in the script; its refutation power
(signature EXISTS) has no such caveat. TOMB-L34's oscillating small-window fits are the known
log-periodic oscillations of quasiperiodic chains; the verdict uses big-N windows. The my-side bug
narrated: the first L34 harness had an empty-slice window bug (shift beyond the built word, S ≡ 0)
— caught by the impossible exact zeros, fenced in the committed script. L310's per-level nulls use
B189's own estimator + null design, extended per-level. No firewall crossing; no measured value.
