# B354 — the metallic interface pairing: exact certificates, the divisibility law, the parity texture

**Status: banked (frontier) — the verified layer of a cross-session (Chat-2 solo, 2026-07-02) computation,
integrated per verify-don't-trust: every banked item was independently re-derived or gate-checked in this repo
(reproducer: `interface_certificates.py`, all gates exact sympy). Firewalled; nothing to `CLAIMS.md`; no physics
claim.**

## Lineage — what was already banked (cited, not re-claimed)

The *mechanism* is **B131/V120** (banked 2026-06-09): each seed's fixed locus traces an A-polynomial curve in the
shared boundary-torus character plane `(m,l) = (tr t, tr[a,b])`; distinct seeds → distinct curves → discrete
(Bézout) fork; same seed → continuum. The golden/silver interface relations `l = m⁴−5m²+2` (=B67) and `l = m²−6`
(=B69/V33) and the exact `(1,2)` fork `κ ∈ {−4,−2}` are B131's. Prior art: **Kitano–Nozaki 2020**
(`NOVELTY_AUDIT` R2). The same-seed gluing-map landscape is **B174/V168**. The cross-session handoff presented
these as new ("a table nobody has"); they are not — the *first column* of that table is B131, and the genuinely
new axis is the cross-seed/γ-gluing part (below + L56).

## Banked here (new beyond B131, each independently verified)

**1. The strong-channel kill (EXACT — re-derived by Gröbner in this repo).** The common fixed representations of
two *distinct* seeds' trace maps are exactly the trivial `(2,2,2)` and quaternion `(0,0,0)` points — equal to
`Fix(T_a) ∩ Fix(T_b)` (Gröbner basis `[x−z, y−z, z²−2z]` for golden×silver; same for golden×bronze). So the
*bulk-sharing* channel is family-universal and carries **no pair information**; the pair-labeled channel is the
*boundary* one (B131's). Bookkeeping: the shared quaternion bulk point presents *different* interface data per
seed (golden `m=±1`, silver `m=0`, both at `l=−2`) — the two channels are genuinely inequivalent.

**2. The exact pair-point certificates (EXACT).** The minimal polynomials of the `(1,3)` and `(2,3)` boundary
pair points, in `T = m²`:

- `(1,3)`: `T⁵ − 13T⁴ + 60T³ − 121T² + 114T − 47` (irreducible quintic)
- `(2,3)`: `T³ − 16T² + 68T − 72` (irreducible cubic)

Verified: the κ-images of their full root sets under the *banked* interface relations reproduce **B131's banked
numeric forks on all 8 values** (e.g. cubic → κ = −4.397, −1.427, 3.824). B131 left these forks as Newton
numerics; these are their exact algebraic certificates.

**3. The classical seam-null (EXACT consequence of 2).** Both pair-point fields have **prime odd degree** (5, 3),
so they contain **no quadratic subfield** — in particular no `√−15`, no `√5`, no `√−3`. The seam `ℚ(√−15)` does
not enter the classical pair arithmetic: a **third independent channel closed** (after the single object, B336,
and — cross-session, unverified here — the quantum traces). The classical interface arithmetic is genuinely *new*
arithmetic, belonging to neither member.

**4. The divisibility law (EXACT, one line).** The abelianized metallic monodromy is
`RᵐLᵐ = [[1+m², m],[m, 1]]`, so `RᵐLᵐ ≡ I (mod p) ⟺ p | m`. One elementary congruence underlying: the seed-parity
texture at `p=2` (even seeds act trivially on mod-2 data), the bronze mod-3 scalar behaviour, and the
cross-session prediction that seed 15 trivializes at the seam level.

**5. The parity-texture exact legs (EXACT).** On the `l = −2` fiber: golden carries `m² ∈ {1,4}` — the
trace-`±1` (2T ω-coset) interface state **present** — while silver carries `m² = 4` **only** — the state
**provably absent**. The odd/even texture claim for seeds 3, 4 remains numerical (cross-session), untested here.

## Conditional / unverified (quarantined, honest tiers)

- **CONDITIONAL (numerical):** the `(±√2, −4)` golden–silver pair point is **absent from bronze's** `l=−4` slice
  (pair-specificity) — Chat-2's 900-start search, reproduced end-to-end (their reproducer, gates passing; `m²=2`
  and the seed-index-numerology control `m²=3` both absent). Exact certificate needs `A_bronze(m,l)` by
  elimination — the named open follow-up.
- **UNVERIFIED (not banked):** the cross-session Weil-representation results — the trace nulls, the level-15
  overlap "pair-fingerprint" tables, the `(1,2)`-only quartic `2025T⁴−3375T³+1935T²−435T+31`, and the "flattening"
  no-go (real overlaps force the Eisenstein end rational at level 15). The checkable *arithmetic* of these claims
  passes spot-checks (the quartic is irreducible with all four roots real in `(0,1)`, factors over `ℚ(√5)`, disc
  `3¹⁴·5⁷`; `ℚ(ζ₉)⁺` is a real cubic, so level 45 is the first aperture), but **no reproducer was received** —
  the whole quantum layer waits on code + an independent conventions check. Registered as **L56**.

## Firewall

Character-variety and congruence mathematics of the metallic family; the "interaction through the interface with
nothing" reading is the owner's thesis being *tested*, not asserted — and the honest verdict so far is: the
classical pair channel produces **pair-labeled structure** (forks, certificates, textures) and **no values, no
seam** (nulls fired at every level tried, including a pre-registered PMNS coincidence killed cross-session by its
own declared test). Nothing promotes.

**Provenance.** Mechanism + first column: B131/V120, K014; gluing landscape: B174/V168; prior art:
Kitano–Nozaki 2020 (`NOVELTY_AUDIT` R2); single-object seam wall: B336; deck correction consumed alongside:
B332 (annotated this date). Cross-session source: Chat-2 solo 2026-07-02 (handoff + reproducer, verified);
quantum layer: L56. Reproducer: `interface_certificates.py`; test:
`tests/test_b354_interface_pairing_certificates.py`.
