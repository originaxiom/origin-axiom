# ADDENDUM (cc3, audit seat, 2026-07-21) — third-seat verification of B734, and the LEVEL under the standard definition

*Filed with the banking-repair PR that commits B734's artifacts (see PROGRESS_LOG entry of this
date: PR #1217 merged with only the test_b731 deletion; the FINDINGS above, the test's 2 locks,
the B731 retraction header, E22, and the R26-5 correction sat uncommitted until this PR).*

## 1. The verification (independent, third seat)

Recomputed in-sandbox with an independent implementation (`cc3_verification/`): different ring
basis (ζ = (1+√−3)/2, ζ² = ζ−1, vs the test's cube-root convention), ambient orders
**BFS-computed from elementary generators, not cited** (the test hardcodes 60/960/30720), both
index conventions computed at every level, odd primes included, and the geometric index 12
verified numerically via Humbert's volume formula against SnapPy's independent
vol(m004) = 2.0298832128 (ratio 11.9999999999). Riley-pair tether: the figure-eight two-bridge
relation **wA = Bw, w = AB⁻¹A⁻¹B** holds EXACTLY over ℤ[ζ] for the pair
A = [[1,1],[0,1]], B = [[1,0],[ζ,1]] (both parabolic, irreducible, entries in O₃;
tr AB = (3−√−3)/2, tr [A,B] = (3+√−3)/2); the −ζ pair used in B731/B734 is its
GL(2,O₃)-conjugate by diag(1,−1), so all image orders/indices are identical (verified
concretely at every level, `plusz_output.txt`). Faithfulness of the parabolic rep at the Riley
root remains the one cited ingredient (Riley 1975).

**Every number in B734, E21, E22 and cc2's stage-2 reproduces exactly:**
|SL(2,O₃/m)| = 60, 3840, 245760 at m = 2,4,8 (computed); knot SL-image orders 10, 320, 20480;
central scalars in the image 1, 2, 8 of |Z| = 1, 4, 8; mod-center indices **6, 6, 12**;
index 12 stable at m = 16; full image (index 1) at the odd primes 3, 5.

## 2. The finding: under the STANDARD definition, the congruence level is (4), not (8)

Two inequivalent "principal congruence subgroup" notions were in play in this thread:

- **P Γ(I) (standard):** the image in PSL(2,O₃) of Γ_SL(I) = ker(SL(2,O₃) → SL(2,O₃/I)).
  Containment test: [SL(2,O₃/I) : image of ⟨A,B,−I⟩] = 12 (the geometric index).
- **Γ̂(I) (what E21 declared "the rigorous test which alone decides"):**
  ker(PSL(2,O₃) → SL(2,O₃/I)/Z(I)), Z(I) the full scalar center. Γ̂(I) ⊇ PΓ(I), so containing
  Γ̂ is the STRONGER demand; its test is the mod-center index B734 computed.

Computed facts (both conventions, every level):

| level m | 2 | 4 | 8 | 16 |
|---|---|---|---|---|
| [SL : ⟨A,B,−I⟩-image] (standard test) | 6 | **12** | 12 | 12 |
| [SL/Z : image·Z/Z] (mod-center test, = B734's) | 6 | 6 | **12** | 12 |

At m = 4 the standard test already reaches 12: with img = ⟨Ā,B̄,−I⟩ of order 320 in
SL(2,O₃/4) of order 3840, the preimage P = π⁻¹(img) ⊆ SL(2,O₃) has index 12 and contains
Γ̃ = ⟨A,B,−I⟩ (index 12, geometric) ⟹ P = Γ̃ ⟹ ker π ⊆ Γ̃ ⟹ **Γ ⊇ PΓ((4))**.
Minimality: index 6 ≠ 12 at m = 2, (2) is inert (the only divisors of (4) are (1),(2),(4)),
and the image is full at odd primes ⟹ **the standard congruence level of m004 is exactly (4).**

So: **B734's headline "m004 IS congruence" is RECONFIRMED and STRENGTHENED** (the knot's
congruence structure sits one 2-adic power shallower than stated); the specific claim
"level (2)³ = (8)" is correct FOR the mod-center filtration Γ̂ but overshoots the standard
level. E21's standing rule fixed a real bug (the SL-order over-read) but over-corrected in
declaring the mod-center index the test that "alone decides" — it decides Γ̂-containment,
which is sufficient, not necessary, for congruence at level I. The sisters' picture becomes
m003 at (2)¹, m004 at (2)² standard / (2)³ mod-center.

## 3. Status and scope

- The E21 refinement + a proposed **E23** (definitional over-correction class) are **pending
  cc2 cross-verify** (relayed this date) before any shared-ledger or LAW_MAP edit; LAW_MAP
  rows 128/129 keep their "(8)" wording until that consensus lands.
- The Serre-defying caveat of the FINDINGS stands unchanged (a fortiori at the shallower
  level); external literature cross-check still open.
- Nothing here touches CLAIMS (pure mathematics; Gate 5 not in scope).

Artifacts: `cc3_verification/` (scripts, outputs, sealed hashes; sandbox paths scrubbed per
WORKING_RULES 11 — pre-scrub sha-256 of the as-run scripts recorded in HASHES.txt).
