# B604 — the Rosetta cell: the pair-to-block assignment DOES NOT EXIST

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
Chat-1's Rosetta handoff verified and resolved. Lock
`tests/test_b604_rosetta.py` (OA_SLOW). θ taken from the banked
intertwiner (θ(X) = −J⁻¹XᵀJ — convention-free); the diagram read off the
computed Cartan matrix; all root vectors exact.**

## Verification of chat-1's handoff (verify-don't-trust)

- **CONFIRMED:** 36 positive roots; 12 θ-fixed + 12 θ-pairs; pair heights
  (2,2,2,2,1,1,1,1); the even/odd dimension checks (52/26); the h=8 pair
  is (16,16); the h=4 pairs are both (D₅,16); one h=1 pair is (D₅,D₅).
- **REFUTED (their D₅/16 table at h = 2, 3):** the computed pair labels
  are {D₅,16} + {D₅,D₅} at EACH of h = 1, 2, 3 — three (D₅,D₅) pairs,
  not one. Their "every pair at heights 1–7 mixes D₅ and 16" fails at
  h = 2, 3. (The pair-label multiset is invariant under the end-node
  choice — b_{endQ} = a_{endP} for a pair {a, σa} — so this is not a
  convention artifact.)

## R1 — THE RESOLUTION: the question dissolves

At every ambiguous height h ∈ {1,2,3,4}, BOTH principal-block lines are
genuine MIXTURES of BOTH θ-odd pair-combinations, with exact integer
coefficients (banked in `rosetta_output.txt`; e.g. h = 4:
V₈-line = −o₁ + o₂, V₁₆-line = −443520·o₁ − 604800·o₂; h = 0: both
Cartan zeros mix (h_P−h_Q) and (h_mP−h_mQ)). **Chat-1's ask — "which
pair goes to V₈ and which to V₁₆" — has no answer because no assignment
exists: the principal grading and the θ-pair decomposition are
incompatible decompositions of the odd 26.** Their ambiguity was a true
feature, not a method limitation.

## The strengthened surviving finding

Since one pair at h = 1, 2, 3 is (D₅,D₅) and the other is (D₅,16), and
both block lines mix both pairs, **every line of both odd blocks carries
both D₅-subsystem and coset-16 root content** (the sole exception in
label type: V₁₆'s h = 8 line is the (16,16) pair). Chat-1's key finding
survives STRONGER than claimed: the mixing is not only within pairs — the
blocks mix the pairs themselves. [FIREWALL: "D₅ = gauge, 16 = matter" is
chat-1's physics reading; the mathematics banked here is subsystem/coset
root content. Under their reading, the consequence is as they stated:
the torsions τ₄, τ₈ label principal-depth strings, not gauge/matter
sectors, and any SM parameter reading would involve BOTH torsions in
combination.]

## Chat-1's ask 3 (the G_SM branching)

The premise ("which torsion corresponds to which SM coupling") is
REFUTED at the structural level by R1 — there is no sector alignment to
read off. A math-tier Spin(10)→SU(5)→G_SM branching table of the MIXED
block lines remains computable as a lead (registered, not run;
firewall-sensitive framing required).
